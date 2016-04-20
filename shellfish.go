/*package shellfish contains code for computing the splashback shells of
halos in N-body simulations.*/
package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path"
	"strings"

	"github.com/phil-mansfield/shellfish/cmd"
	"github.com/phil-mansfield/shellfish/cmd/env"
	"github.com/phil-mansfield/shellfish/version"
)

func modeDescriptions() string {
	return "My help mode is:\n" +
	"shellfish help\n\n" +

	"My setup mode is:\n" +
	"shellfish setup ____.setup.config\n\n" +

	"My other modes are:\n" +
	"shellfish id     [flags] ____.config [____.id.config]\n" +
	"shellfish tree ____.config\n" +
	"shellfish coord ____.config\n" +
	"shellfish shell  [flags] ____.config [____.shell.config]\n" +
	"shellfish stats  [flags] ____.config [____.stats.config]\n\n"
}

func main() {
	args := os.Args
	if len(args) <= 1 {
		fmt.Fprintf(
			os.Stderr, "I was not supplied with a mode.\nFor help, type " +
			"'./shellfish help'.\n",
		)
		os.Exit(1)
	}


	if args[1] == "setup" {
		// TODO: Implement the setup command.
		panic("NYI")
	} else if args[1] == "help" {
		fmt.Print(modeDescriptions())
		os.Exit(0)
		// TODO: Implement the help command.
	} else if args[1] == "version" {
		fmt.Printf("Shellfish version %s\n", version.SourceVersion)
		os.Exit(0)
	}

	mode, ok := cmd.ModeNames[args[1]]
	if !ok {
		fmt.Fprintf(
			os.Stderr, "You passed me the mode '%s', which I don't " +
			"recognize.\nFor help, type './shellfish help'\n", args[1],
		)
		os.Exit(1)
	}

	var lines []string
	switch args[1] {
	case "tree", "coord", "shell", "stats":
		var err error
		lines, err = stdinLines()
		if err != nil {
			fmt.Fprintf(os.Stderr, err.Error())
			os.Exit(1)
		}
	}

	flags := getFlags(args)
	gConfigName, gConfig, err := getGlobalConfig(args)
	if err != nil {
		log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
	}
	config, ok := getConfig(args)

	if ok {
		if err = mode.ReadConfig(config); err != nil {
			log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
		}
	} else {
		if err = mode.ReadConfig(""); err != nil {
			log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
		}
	}

	if err = checkMemoDir(gConfig.MemoDir, gConfigName); err != nil {
		log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
	}

	e := &env.Environment{MemoDir: gConfig.MemoDir}
	initCatalogs(gConfig, e)
	initHalos(args[1], gConfig, e)

	if err != nil {
		log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
	}

	if err != nil {
		log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
	}

	out, err := mode.Run(flags, gConfig, e, lines)
	if err != nil {
		log.Fatalf("Error running mode %s:\n%s\n", args[1], err.Error())
	}

	for i := range out { fmt.Println(out[i]) }
}


// stdinLines reads stdin and splits it into lines.
func stdinLines() ([]string, error) {
	bs, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return nil, fmt.Errorf(
			"Error reading stdin: %s.", err.Error(),
		)
	}
	text := string(bs)
	lines := strings.Split(text, "\n")
	if lines[len(lines) - 1] == "" { lines = lines[:len(lines) - 1] }
	return lines, nil
}

// getFlags reutrns the flag tokens from the command line arguments.
func getFlags(args []string) ([]string) {
	return args[1:len(args) - 1 - configNum(args)]
}

// getGlobalConfig returns the name of the base config file from the command
// line arguments.
func getGlobalConfig(args []string) (string, *cmd.GlobalConfig, error) {
	name := ""
	switch configNum(args) {
	case 0:
		return "", nil, fmt.Errorf("No config files provided in command " +
			"line arguments")
	case 1:
		name = args[len(args) - 1]
	case 2:
		name = args[len(args) - 2]
	}

	config := &cmd.GlobalConfig{}
	err := config.ReadConfig(name)
	if err != nil { return "", nil, err }
	return name, config, nil
}

// getConfig return the name of the mode-specific config file from the command
// line arguments.
func getConfig(args []string) (string, bool) {
	if configNum(args) == 2 {
		return args[len(args) - 1], true
	}
	return "", false
}

// configNum returns the number of configuration files at the end of the
// argument list (up to 2).
func configNum(args []string) int {
	num := 0
	for i := len(args) - 1; i >= 0 && i >= len(args) - 2; i-- {
		if isConfig(args[i]) {
			num++
		} else {
			break
		}
	}
	return num
}

// isConfig returns true if the fiven string is a config file name.
func isConfig(s string) bool {
	return len(s) >= 7 &&  s[len(s) - 7:] == ".config"
}

// cehckMemoDir checks whether the given MemoDir corresponds to a GlobalConfig
// file with the exact same variables. If not, a non-nil error is returned.
// If the MemoDir does not have an associated GlobalConfig file, the current
// one will be copied in.
func checkMemoDir(memoDir, configFile string) error {
	memoConfigFile := path.Join(memoDir, "memo.config")
	
	if _, err := os.Stat(memoConfigFile); err != nil {
		// File doesn't exist, directory is clean.
		err = copyFile(memoConfigFile, configFile)
		return err
	}

	config, memoConfig := &cmd.GlobalConfig{}, &cmd.GlobalConfig{}
	if err := config.ReadConfig(configFile); err != nil { return err }
	if err := memoConfig.ReadConfig(memoConfigFile); err != nil { return err }

	if !configEqual(config, memoConfig) {
		return fmt.Errorf("The variables in the config file '%s' do not " +
			"match the varables used when creating the MemoDir, '%s.' These " +
			"variables can be compared by inspecting '%s' and '%s'",
			configFile, memoDir, configFile, memoConfigFile,
		)
	}
	return nil
}

// copyFile copies a file from src to dst.
func copyFile(dst, src string) error {
	srcFile, err := os.Open(src)
	if err != nil { return err }
	defer srcFile.Close()

	dstFile, err := os.Create(dst)
	if err != nil { return err }
	defer dstFile.Close()

	if _, err = io.Copy(dstFile, srcFile); err != nil { return err }
	return dstFile.Sync()
}

func configEqual(m, c *cmd.GlobalConfig) bool {
	return c.Version == m.Version &&
		c.SnapshotFormat == m.SnapshotFormat &&
		c.SnapshotType == m.SnapshotType &&
		c.HaloDir == m.HaloDir &&
		c.HaloType == m.HaloType &&
		c.TreeDir == m.TreeDir &&
		c.TreeType == m.TreeType &&
		c.MemoDir == m.MemoDir &&
		int64sEqual(c.FormatMins, m.FormatMins) &&
		int64sEqual(c.FormatMaxes, m.FormatMaxes) &&
		c.SnapMin == m.SnapMin &&
		c.SnapMax == m.SnapMax &&
		c.Endianness == m.Endianness &&
		c.ValidateFormats == m.ValidateFormats
}

func int64sEqual(xs, ys []int64) bool {
	if len(xs) != len(ys) { return false }
	for i := range xs {
		if xs[i] != ys[i] { return false }
	}
	return true
}

func initHalos(
	mode string, gConfig *cmd.GlobalConfig, e *env.Environment,
) error {
	switch mode {
	case "shell", "stats": return nil
	}

	switch gConfig.HaloType {
	case "nil":
		return fmt.Errorf("You may not use nil as a HaloType for the " +
			"mode '%s.'\n", mode)
	case "Rockstar":
		return e.InitRockstar(gConfig.HaloDir, gConfig.SnapMin, gConfig.SnapMax)
		if gConfig.TreeType != "consistent-trees"{
			return fmt.Errorf("You're trying to use the '%s' TreeType with " +
				"the 'Rockstar' HaloType.")
		}
	}
	if gConfig.TreeType == "nil" {
		return fmt.Errorf("You may not use nil as a TreeType for the " +
			"mode '%s.'\n", mode)
	}

	panic("Impossible")
}

func initCatalogs(gConfig *cmd.GlobalConfig, e *env.Environment) error {
	switch gConfig.SnapshotType {
	case "gotetra":
		return e.InitGotetra(
			gConfig.SnapshotFormat, gConfig.SnapMin, gConfig.SnapMax,
			gConfig.FormatMins, gConfig.FormatMaxes, gConfig.ValidateFormats,
		)
	case "LGadget-2":
		panic("Not yet implemented.")
	}
	panic("Impossible.")
}

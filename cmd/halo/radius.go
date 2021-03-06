package halo

import (
	"fmt"
	"math"

	"github.com/phil-mansfield/shellfish/cosmo"
	"github.com/phil-mansfield/shellfish/io"
)

type Radius int

const (
	R200c Radius = iota
	R200m
	R500c
	R2500c
)


func RadiusFromString(s string) (r Radius, ok bool) {
	switch s {
	case "R200m":
		return R200m, true
	case "R200c":
		return R200c, true
	case "R500c":
		return R500c, true
	case "R2500c":
		return R2500c, true
	}
	return -1, false
}

func (r Radius) MassString() string {
	switch r {
	case R200m:
		return "M200m"
	case R200c:
		return "M200c"
	case R500c:
		return "R500c"
	case R2500c:
		return "M2500c"
	}
	panic(":3")
}


func (r Radius) String() string {
	switch r {
	case R200m:
		return "R200m"
	case R200c:
		return "R200c"
	case R500c:
		return "R500c"
	case R2500c:
		return "R2500c"
	}
	panic(":3")
}

func (r Radius) Radius(c *io.CosmologyHeader, ms, out []float64) {
	var rho float64
	h0 := c.H100 * 100
	
	switch r {
	case R200c:
		rho = 200 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	case R200m:
		rho = 200 * cosmo.RhoAverage(h0, c.OmegaM, c.OmegaL, c.Z)
	case R500c:
		rho = 500 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	case R2500c:
		rho = 2500 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	default:
		panic(":3")
	}
	
	a := 1 / (1 + c.Z)
	factor := rho * 4 * math.Pi / 3
	
	for i, m := range ms {
		out[i] = math.Pow(m/factor, 1.0/3) / a
	}
}

func (r Radius) Mass(c *io.CosmologyHeader, rs, out []float64) {
	var rho float64
	h0 := c.H100 * 100

	switch r {
	case R200c:
		rho = 200 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	case R200m:
		rho = 200 * cosmo.RhoAverage(h0, c.OmegaM, c.OmegaL, c.Z)
	case R500c:
		rho = 500 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	case R2500c:
		rho = 2500 * cosmo.RhoCritical(h0, c.OmegaM, c.OmegaL, c.Z)
	}

	a := 1 / (1 + c.Z)
	factor := rho * 4 * math.Pi / 3
	for i, r := range rs {
		r = r * a
		out[i] = factor * (r * r * r)
	}
}

// UnitConversionFactor returns the multiplicative factor needed to convert
// the given units into cMpc/h.
func UnitConversionFactor(unitStr string, cosmo *io.CosmologyHeader) float64 {
	switch unitStr {
	case "cMpc/h": return 1
	case "ckpc/h": return 1e-3
	case "pMpc/h": return (1 + cosmo.Z)
	case "pkpc/h": return 1e-3 * (1 + cosmo.Z)
	case "cMpc": return cosmo.H100
	case "ckpc": return 1e-3 * cosmo.H100
	case "pMpc": return (1 + cosmo.Z) * cosmo.H100
	case "pkpc": return 1e-3 * (1 + cosmo.Z) * cosmo.H100
	default: panic(fmt.Sprintf("Unrecognized unit string '%s'", unitStr))
	}
}
import numpy as np
acs = np.array([
         0.2,  0.2276,  0.2552,  0.2828,  0.3103,  0.3379,  0.3655,  0.3931,  0.4207,  0.4483,  0.4759,  0.5034,   0.531,  0.5586,  0.5862,  0.6138,  0.6414,   0.669,  0.6966,  0.7241,  0.7517,  0.7793,  0.8069,  0.8345,  0.8621,  0.8897,  0.9172,  0.9448,  0.9724,       1,
])

bcs = np.array([
         0.2,  0.2276,  0.2552,  0.2828,  0.3103,  0.3379,  0.3655,  0.3931,  0.4207,  0.4483,  0.4759,  0.5034,   0.531,  0.5586,  0.5862,  0.6138,  0.6414,   0.669,  0.6966,  0.7241,  0.7517,  0.7793,  0.8069,  0.8345,  0.8621,  0.8897,  0.9172,  0.9448,  0.9724,       1,
])

ac_grid = np.array([
      0.8342,  0.8233,  0.8138,  0.8086,  0.8004,   0.793,  0.7917,  0.7834,   0.783,  0.7803,  0.7775,  0.7732,  0.7727,  0.7715,  0.7693,  0.7677,   0.766,  0.7651,  0.7637,   0.764,  0.7618,   0.762,  0.7615,    0.76,  0.7599,  0.7594,  0.7583,  0.7575,   0.759,  0.7569,
           0,  0.8392,  0.8275,  0.8203,  0.8145,  0.8058,  0.8048,  0.7991,  0.7957,   0.793,  0.7883,  0.7873,  0.7836,  0.7824,  0.7799,  0.7799,  0.7787,   0.778,  0.7762,   0.774,  0.7745,  0.7721,  0.7706,  0.7705,  0.7711,  0.7691,  0.7694,  0.7684,  0.7679,  0.7671,
           0,       0,  0.8433,   0.832,  0.8275,  0.8211,  0.8156,  0.8133,  0.8075,  0.8057,  0.8024,  0.7972,  0.7972,  0.7951,  0.7925,  0.7889,  0.7897,  0.7879,  0.7864,  0.7855,  0.7842,  0.7833,  0.7817,  0.7819,  0.7806,   0.779,   0.779,  0.7782,  0.7759,  0.7776,
           0,       0,       0,   0.848,  0.8396,  0.8329,  0.8291,  0.8253,  0.8199,  0.8157,  0.8134,  0.8115,  0.8082,  0.8048,   0.803,  0.8016,  0.8001,  0.7975,  0.7974,  0.7957,  0.7943,  0.7938,  0.7918,  0.7928,  0.7909,    0.79,  0.7905,  0.7899,  0.7885,  0.7878,
           0,       0,       0,       0,  0.8528,   0.846,  0.8417,  0.8353,  0.8317,  0.8268,  0.8249,  0.8215,  0.8199,  0.8175,  0.8133,  0.8134,  0.8114,  0.8102,   0.808,  0.8064,  0.8048,  0.8045,  0.8037,  0.8022,  0.8014,  0.8011,  0.7999,  0.8005,   0.799,  0.7985,
           0,       0,       0,       0,       0,  0.8577,  0.8524,  0.8482,  0.8419,  0.8397,  0.8364,  0.8317,  0.8302,  0.8278,  0.8264,  0.8239,  0.8213,  0.8195,  0.8196,  0.8182,  0.8158,  0.8156,  0.8143,  0.8121,  0.8122,  0.8126,    0.81,  0.8084,  0.8097,  0.8087,
           0,       0,       0,       0,       0,       0,  0.8649,  0.8582,  0.8545,  0.8508,  0.8465,  0.8445,   0.842,  0.8383,  0.8371,  0.8333,  0.8335,  0.8306,  0.8309,   0.828,  0.8272,  0.8253,  0.8242,  0.8236,  0.8222,  0.8211,  0.8216,  0.8207,  0.8194,  0.8193,
           0,       0,       0,       0,       0,       0,       0,  0.8698,  0.8637,  0.8587,  0.8584,  0.8545,   0.852,  0.8485,   0.848,  0.8455,  0.8433,  0.8424,  0.8397,  0.8387,  0.8361,  0.8351,   0.835,  0.8335,  0.8327,  0.8322,  0.8299,   0.831,  0.8297,   0.829,
           0,       0,       0,       0,       0,       0,       0,       0,  0.8751,  0.8711,  0.8693,  0.8651,  0.8622,  0.8596,  0.8565,   0.856,  0.8518,  0.8526,  0.8501,  0.8475,  0.8471,  0.8449,  0.8458,  0.8447,  0.8427,  0.8428,  0.8405,  0.8405,  0.8393,  0.8396,
           0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8803,  0.8777,  0.8728,  0.8728,  0.8685,  0.8667,  0.8657,  0.8638,  0.8618,    0.86,  0.8594,  0.8579,  0.8573,  0.8545,  0.8544,  0.8537,  0.8517,  0.8521,  0.8506,  0.8501,  0.8491,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8873,  0.8813,  0.8815,  0.8795,  0.8764,  0.8751,  0.8723,  0.8719,  0.8698,  0.8675,  0.8664,  0.8667,  0.8654,  0.8629,  0.8631,  0.8592,  0.8608,  0.8589,  0.8587,  0.8604,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8932,  0.8904,  0.8892,  0.8867,  0.8836,  0.8832,  0.8804,  0.8783,  0.8768,  0.8763,  0.8757,  0.8736,  0.8717,  0.8711,  0.8716,  0.8696,  0.8679,  0.8692,  0.8687,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8985,  0.8958,  0.8941,  0.8927,  0.8912,  0.8892,  0.8879,  0.8881,  0.8849,  0.8853,  0.8823,  0.8819,  0.8815,  0.8805,  0.8786,  0.8779,  0.8771,  0.8782,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9054,  0.9033,   0.901,  0.9006,  0.8995,  0.8958,  0.8958,   0.893,  0.8928,  0.8917,  0.8918,    0.89,  0.8882,  0.8891,  0.8872,  0.8858,  0.8867,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9125,  0.9098,  0.9073,  0.9066,  0.9047,  0.9039,  0.9015,  0.9031,  0.8996,  0.8998,  0.8976,   0.896,  0.8965,   0.896,  0.8961,  0.8952,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9177,  0.9169,  0.9147,  0.9142,  0.9115,  0.9114,  0.9095,  0.9087,  0.9084,  0.9068,  0.9069,  0.9061,  0.9047,  0.9035,  0.9031,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   0.923,  0.9214,  0.9191,  0.9197,  0.9168,  0.9188,  0.9174,  0.9152,  0.9166,  0.9139,  0.9129,   0.914,  0.9129,  0.9119,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9302,  0.9286,  0.9269,  0.9262,  0.9267,  0.9244,  0.9238,  0.9236,  0.9232,  0.9204,  0.9215,  0.9211,  0.9195,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9359,  0.9342,  0.9336,   0.932,  0.9314,  0.9323,  0.9308,    0.93,  0.9291,  0.9284,  0.9272,  0.9279,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   0.942,  0.9409,  0.9386,  0.9388,  0.9379,  0.9377,   0.937,   0.936,  0.9351,  0.9342,  0.9361,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   0.949,  0.9459,  0.9463,  0.9462,   0.944,  0.9431,   0.944,  0.9442,  0.9436,  0.9426,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9542,  0.9524,  0.9533,  0.9521,  0.9526,  0.9506,  0.9497,  0.9509,  0.9488,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9596,  0.9595,  0.9579,  0.9577,  0.9573,  0.9579,  0.9574,  0.9566,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9659,  0.9645,  0.9644,  0.9643,  0.9633,  0.9631,  0.9647,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9705,  0.9716,  0.9705,  0.9706,  0.9707,  0.9705,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9789,  0.9765,  0.9784,  0.9768,   0.977,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9838,  0.9847,  0.9836,  0.9832,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9893,  0.9881,  0.9885,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9942,  0.9943,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.001,
])

bc_grid = np.array([
      0.8328,  0.8513,  0.8631,  0.8787,  0.8897,  0.8969,  0.9096,  0.9142,  0.9261,  0.9333,  0.9403,  0.9423,  0.9509,  0.9559,  0.9603,  0.9641,  0.9663,  0.9705,  0.9757,  0.9784,  0.9802,  0.9843,  0.9877,  0.9881,  0.9914,  0.9922,  0.9939,  0.9966,       1,   1.001,
           0,  0.8388,  0.8501,  0.8639,  0.8774,  0.8853,  0.8999,  0.9082,  0.9162,  0.9231,  0.9289,  0.9395,  0.9437,   0.949,  0.9542,  0.9607,  0.9654,  0.9695,  0.9733,  0.9754,  0.9802,  0.9803,  0.9841,  0.9857,  0.9906,  0.9914,  0.9947,   0.997,  0.9974,   1.002,
           0,       0,  0.8422,  0.8527,  0.8667,  0.8779,  0.8896,  0.8996,  0.9069,  0.9176,  0.9249,  0.9302,  0.9378,  0.9447,  0.9487,  0.9524,  0.9605,  0.9631,  0.9677,  0.9727,  0.9737,  0.9792,  0.9809,  0.9864,  0.9884,   0.991,  0.9942,  0.9944,  0.9945,   1.002,
           0,       0,       0,  0.8473,  0.8584,  0.8695,  0.8816,  0.8932,  0.9005,  0.9092,  0.9167,  0.9253,  0.9312,  0.9363,  0.9418,  0.9485,  0.9541,  0.9604,  0.9648,  0.9686,  0.9726,  0.9768,  0.9799,  0.9847,  0.9864,  0.9893,  0.9952,  0.9977,  0.9979,   1.001,
           0,       0,       0,       0,  0.8525,  0.8642,  0.8756,  0.8845,  0.8941,  0.9012,  0.9114,  0.9189,  0.9263,  0.9331,   0.938,  0.9467,  0.9507,   0.957,  0.9603,  0.9653,  0.9706,  0.9745,  0.9786,  0.9812,   0.985,  0.9889,   0.991,  0.9965,   0.997,   1.001,
           0,       0,       0,       0,       0,  0.8568,  0.8692,  0.8808,  0.8861,  0.8971,  0.9071,  0.9134,  0.9213,  0.9293,  0.9364,  0.9415,  0.9469,  0.9525,  0.9581,  0.9641,  0.9673,  0.9707,  0.9771,  0.9795,  0.9854,  0.9869,  0.9915,  0.9923,   0.998,   1.003,
           0,       0,       0,       0,       0,       0,  0.8639,  0.8738,  0.8829,  0.8929,  0.9011,  0.9082,  0.9182,  0.9234,  0.9324,  0.9371,   0.946,  0.9509,  0.9561,  0.9608,  0.9662,  0.9709,  0.9735,  0.9788,   0.983,  0.9875,  0.9913,  0.9944,   0.996,   1.001,
           0,       0,       0,       0,       0,       0,       0,   0.869,  0.8789,  0.8861,  0.8967,  0.9055,  0.9129,  0.9204,  0.9297,   0.935,  0.9426,  0.9481,  0.9522,  0.9583,  0.9624,  0.9689,  0.9732,  0.9774,  0.9818,  0.9868,  0.9882,  0.9932,  0.9971,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,  0.8747,  0.8839,  0.8944,  0.9017,  0.9112,   0.917,  0.9243,  0.9326,  0.9374,  0.9475,  0.9509,  0.9565,  0.9619,  0.9664,  0.9727,  0.9774,  0.9802,  0.9854,  0.9873,  0.9928,  0.9956,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8791,  0.8901,  0.8967,  0.9083,   0.915,  0.9225,  0.9297,  0.9364,  0.9427,  0.9502,  0.9556,  0.9605,  0.9664,  0.9718,  0.9761,  0.9808,  0.9842,  0.9903,  0.9927,  0.9975,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8869,  0.8936,  0.9052,  0.9122,  0.9191,  0.9276,  0.9329,  0.9414,  0.9458,  0.9528,  0.9584,  0.9659,  0.9703,  0.9744,  0.9797,  0.9822,  0.9872,  0.9916,  0.9965,   1.003,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8929,  0.9022,  0.9102,  0.9179,  0.9243,   0.933,  0.9384,  0.9456,  0.9511,  0.9579,  0.9641,  0.9688,   0.973,  0.9781,  0.9848,  0.9885,  0.9907,  0.9968,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.8972,  0.9068,  0.9145,  0.9219,   0.931,  0.9376,  0.9435,   0.951,   0.955,  0.9634,  0.9668,  0.9729,  0.9774,  0.9827,  0.9868,  0.9896,  0.9967,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9045,  0.9134,    0.92,  0.9291,  0.9346,  0.9423,  0.9489,  0.9534,  0.9606,  0.9669,  0.9732,  0.9763,  0.9803,  0.9876,   0.991,  0.9937,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9117,  0.9188,   0.926,  0.9333,   0.941,   0.948,  0.9523,   0.961,  0.9649,  0.9714,  0.9755,  0.9796,  0.9862,  0.9915,   0.995,       1,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9167,  0.9241,  0.9326,  0.9383,  0.9464,  0.9533,  0.9591,  0.9644,  0.9711,  0.9762,  0.9822,  0.9868,  0.9908,  0.9945,       1,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9222,  0.9312,  0.9366,  0.9438,  0.9501,  0.9587,   0.964,  0.9701,  0.9757,  0.9797,  0.9843,  0.9916,  0.9958,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9297,   0.936,  0.9431,  0.9499,  0.9573,   0.962,   0.969,  0.9741,  0.9812,  0.9848,  0.9896,  0.9958,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9351,  0.9422,  0.9486,  0.9552,  0.9628,  0.9689,  0.9731,  0.9803,  0.9856,  0.9903,  0.9952,       1,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9407,  0.9486,  0.9546,  0.9624,   0.966,   0.974,  0.9799,   0.984,  0.9891,  0.9952,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9481,  0.9536,  0.9611,  0.9673,  0.9714,  0.9785,  0.9838,  0.9898,  0.9936,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9531,  0.9612,  0.9676,  0.9725,  0.9786,  0.9841,  0.9898,  0.9947,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9585,  0.9662,   0.972,   0.978,  0.9839,   0.991,  0.9943,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9658,  0.9713,  0.9784,   0.984,  0.9886,  0.9945,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9702,  0.9778,  0.9826,  0.9899,  0.9955,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9781,  0.9832,  0.9898,  0.9955,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9829,  0.9899,  0.9945,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9886,  0.9929,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9941,   1.001,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       1,
])

c_grid = np.array([
       1.137,   1.134,   1.133,   1.129,   1.129,    1.13,   1.126,   1.129,   1.125,   1.124,   1.123,   1.125,   1.123,   1.122,   1.122,   1.121,   1.122,   1.121,    1.12,   1.119,    1.12,   1.119,   1.118,   1.119,   1.118,   1.118,   1.118,   1.118,   1.116,   1.117,
           0,   1.132,   1.132,   1.129,   1.126,   1.128,   1.122,   1.122,   1.121,    1.12,   1.121,   1.117,   1.118,   1.117,   1.117,   1.115,   1.114,   1.113,   1.113,   1.114,   1.112,   1.113,   1.113,   1.113,   1.111,   1.112,   1.111,   1.111,   1.111,    1.11,
           0,       0,   1.128,   1.128,   1.124,   1.123,   1.121,   1.118,   1.118,   1.115,   1.114,   1.115,   1.112,   1.111,   1.111,   1.112,   1.109,   1.109,   1.108,   1.107,   1.108,   1.106,   1.107,   1.105,   1.105,   1.105,   1.104,   1.105,   1.106,   1.103,
           0,       0,       0,   1.123,   1.122,    1.12,   1.117,   1.114,   1.114,   1.112,   1.111,   1.109,   1.108,   1.108,   1.107,   1.106,   1.105,   1.104,   1.103,   1.102,   1.102,   1.101,   1.101,   1.099,   1.099,   1.099,   1.097,   1.097,   1.097,   1.097,
           0,       0,       0,       0,   1.118,   1.116,   1.113,   1.112,    1.11,    1.11,   1.107,   1.105,   1.103,   1.102,   1.103,     1.1,   1.099,   1.098,   1.098,   1.097,   1.096,   1.095,   1.094,   1.094,   1.094,   1.093,   1.093,    1.09,   1.091,    1.09,
           0,       0,       0,       0,       0,   1.114,   1.111,   1.107,   1.108,   1.105,   1.102,   1.102,     1.1,   1.098,   1.096,   1.096,   1.095,   1.094,   1.092,   1.091,   1.091,    1.09,   1.089,   1.089,   1.087,   1.086,   1.087,   1.087,   1.085,   1.084,
           0,       0,       0,       0,       0,       0,   1.107,   1.106,   1.103,   1.101,     1.1,   1.098,   1.095,   1.095,   1.092,   1.092,   1.089,   1.089,   1.087,   1.087,   1.085,   1.085,   1.084,   1.083,   1.082,   1.081,    1.08,   1.079,    1.08,   1.078,
           0,       0,       0,       0,       0,       0,       0,   1.102,   1.101,     1.1,   1.096,   1.094,   1.092,   1.091,   1.087,   1.087,   1.085,   1.083,   1.083,   1.082,   1.082,    1.08,   1.079,   1.078,   1.077,   1.076,   1.076,   1.074,   1.074,   1.073,
           0,       0,       0,       0,       0,       0,       0,       0,   1.097,   1.095,   1.091,    1.09,   1.088,   1.087,   1.085,   1.082,   1.083,   1.079,   1.079,   1.078,   1.076,   1.076,   1.073,   1.072,   1.072,    1.07,   1.071,   1.069,   1.069,   1.067,
           0,       0,       0,       0,       0,       0,       0,       0,       0,   1.093,   1.089,   1.089,   1.084,   1.083,   1.081,   1.079,   1.077,   1.076,   1.074,   1.072,   1.071,   1.069,   1.069,   1.068,   1.066,   1.066,   1.064,   1.064,   1.063,   1.062,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.087,   1.086,   1.081,   1.079,   1.078,   1.075,   1.074,   1.071,   1.071,   1.069,   1.068,   1.065,   1.064,   1.064,   1.062,   1.063,   1.061,    1.06,   1.059,   1.056,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.081,   1.079,   1.076,   1.074,   1.073,   1.069,   1.069,   1.067,   1.066,   1.063,   1.061,   1.061,    1.06,   1.059,   1.056,   1.056,   1.056,   1.054,   1.052,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.077,   1.074,   1.072,    1.07,   1.067,   1.065,   1.063,    1.06,    1.06,   1.057,   1.057,   1.055,   1.054,   1.053,   1.052,   1.052,    1.05,   1.048,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.071,   1.068,   1.067,   1.063,   1.062,    1.06,   1.058,   1.057,   1.055,   1.053,   1.051,   1.051,    1.05,   1.047,   1.047,   1.047,   1.044,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.065,   1.063,   1.062,   1.059,   1.057,   1.055,   1.054,    1.05,    1.05,   1.048,   1.048,   1.047,   1.044,   1.043,   1.042,    1.04,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.061,   1.058,   1.056,   1.054,   1.052,   1.049,   1.048,   1.047,   1.044,   1.043,   1.041,    1.04,   1.039,   1.039,   1.037,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.057,   1.054,   1.053,    1.05,   1.048,   1.044,   1.043,   1.042,   1.039,   1.039,   1.038,   1.035,   1.034,   1.033,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.051,   1.049,   1.047,   1.045,   1.042,   1.041,   1.039,   1.037,   1.035,   1.035,   1.033,   1.031,    1.03,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.046,   1.044,   1.042,    1.04,   1.038,   1.035,   1.034,   1.032,   1.031,    1.03,   1.028,   1.026,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.042,   1.039,   1.038,   1.035,   1.034,   1.031,    1.03,   1.029,   1.027,   1.026,   1.023,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.036,   1.036,   1.033,    1.03,    1.03,   1.028,   1.026,   1.023,   1.022,    1.02,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.033,    1.03,   1.028,   1.026,   1.024,   1.023,   1.021,   1.019,   1.018,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.029,   1.026,   1.024,   1.022,   1.021,   1.018,   1.017,   1.015,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.024,   1.022,    1.02,   1.018,   1.017,   1.015,   1.012,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,    1.02,   1.017,   1.016,   1.014,   1.012,    1.01,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.015,   1.014,   1.011,    1.01,   1.008,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.011,   1.009,   1.007,   1.005,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.007,   1.006,   1.004,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,   1.004,   1.002,
           0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,       0,  0.9997,
])

ac_grid = np.reshape(ac_grid, (30, 30))
bc_grid = np.reshape(bc_grid, (30, 30))
c_grid = np.reshape(c_grid, (30, 30))

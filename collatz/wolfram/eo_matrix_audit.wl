(* Exact independent audit of the E/O affine-matrix Collatz formulation.

   This file is deliberately separate from collatz/src/eo_matrix_audit.py.
   All logical comparisons use exact Wolfram integers/rationals.
*)

ClearAll[ME, MO, affineR, firstCrossingQ, mechanicalWord,
  smallFirstCrossingAudit, finiteMechanicalScan];

ME = {{1/2, 0}, {0, 1}};
MO = {{3/2, 1/2}, {0, 1}};

Print["generator commutator = ", MatrixForm[MO.ME - ME.MO]];
If[MO.ME - ME.MO =!= {{0, 1/4}, {0, 0}}, Abort[]];

affineR[w_List] := Module[{q = 0, r = 0},
  Do[
    If[w[[k + 1]] == 1,
      r = 3 r + 2^k;
      q++
    ],
    {k, 0, Length[w] - 1}
  ];
  {Length[w], q, r}
];

firstCrossingQ[w_List] := Module[{q = 0, h = Length[w]},
  And @@ Table[
    q += w[[k]];
    If[k < h, 3^q >= 2^k, 3^q < 2^k],
    {k, 1, h}
  ]
];

mechanicalWord[q_Integer?Positive] := Module[{sigma, pos, w},
  sigma = IntegerLength[3^q, 2];
  pos = Table[IntegerLength[3^i, 2] - 1, {i, 0, q - 1}];
  w = ConstantArray[0, sigma];
  Scan[(w[[# + 1]] = 1) &, pos];
  w
];

smallFirstCrossingAudit[maxQ_Integer?Positive] := Table[
  Module[{sigma, ws, mw, rs, rm},
    sigma = IntegerLength[3^q, 2];
    ws = Select[
      Tuples[{0, 1}, sigma],
      Total[#] == q && firstCrossingQ[#] &
    ];
    mw = mechanicalWord[q];
    rs = affineR[#][[3]] & /@ ws;
    rm = affineR[mw][[3]];
    If[! firstCrossingQ[mw] || rm =!= Max[rs], Abort[]];
    {q, sigma, Length[ws], rm}
  ],
  {q, 1, maxQ}
];

finiteMechanicalScan[sigmaLimit_Integer?Positive, verifiedBits_Integer?Positive] :=
 Module[{q = 1, p3 = 3, r = 1, sigma, d, count = 0,
   failures = {}, best = None, bestR = 0, bestD = 1},
  While[True,
    sigma = IntegerLength[p3, 2];
    If[sigma > sigmaLimit, Break[]];
    d = 2^sigma - p3;
    count++;
    If[!(r < 2^verifiedBits d), AppendTo[failures, {sigma, q}]];
    If[best === None || r bestD > bestR d,
      best = {sigma, q, r, d};
      bestR = r;
      bestD = d
    ];
    (* q -> q+1: add the exact rightmost mechanical odd position *)
    r = 3 r + 2^(IntegerLength[p3, 2] - 1);
    p3 *= 3;
    q++
  ];
  {count, best, failures}
];

small = smallFirstCrossingAudit[8];
Print["small first-crossing audit = ", small];

expected = {
  {1, 2, 1, 1},
  {2, 4, 1, 5},
  {3, 5, 2, 23},
  {4, 7, 3, 85},
  {5, 8, 7, 319},
  {6, 10, 12, 1085},
  {7, 12, 30, 3767},
  {8, 13, 85, 13349}
};
If[small =!= expected, Abort[]];

scan = finiteMechanicalScan[20000, 71];
Print["mechanical first crossings scanned = ", scan[[1]]];
Print["best {sigma,q,R,D} = ", scan[[2]]];
Print["best R/D ~= ", N[scan[[2, 3]]/scan[[2, 4]], 30]];
Print["bound failures = ", scan[[3]]];
If[scan[[3]] =!= {}, Abort[]];

Print["E/O affine-matrix Wolfram audit: PASS"];

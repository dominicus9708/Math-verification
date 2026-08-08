(* Cross-base rank diagnostic for Ansari's recursively sufficient Cantor core.
   For fixed ternary depth m, enumerate
      x = 4(3^m + sum a_i 3^i) + 3, a_i in {0,1},
   test whether the coefficient barrier 3^{q_k} >= 2^k survives through
   B = ceil(m log_2 3 + 2), reshape the Boolean truth table across a half-digit
   cut, and compute exact matrix rank.

   This is a complexity diagnostic, not a Collatz proof. *)

ClearAll[tfun, survives, rankTest];

tfun[n_Integer] := If[EvenQ[n], Quotient[n, 2], Quotient[3 n + 1, 2]];

survives[x_Integer, B_Integer] := Catch[
  Module[{nn = x, qq = 0},
    Do[
      If[OddQ[nn], qq++];
      nn = tfun[nn];
      If[3^qq < 2^k, Throw[0]],
      {k, 1, B}
    ];
    1
  ]
];

rankTest[m_Integer] := Module[{B, base, weights, vals, a, mat},
  B = Ceiling[m N[Log[2, 3], 80] + 2];
  base = 4 3^m + 3;
  weights = Table[4 3^i, {i, 0, m - 1}];
  vals = Table[
    survives[
      base + Sum[BitGet[b, i] weights[[i + 1]], {i, 0, m - 1}],
      B
    ],
    {b, 0, 2^m - 1}
  ];
  a = Floor[m/2];
  mat = ArrayReshape[vals, {2^a, 2^(m - a)}];
  {m, B, Total[vals], MatrixRank[mat], Min[Dimensions[mat]]}
];

Table[rankTest[m], {m, 4, 13}]

(* Verified output on 2026-08-09:
{4,9,4,4,4}
{5,10,7,4,4}
{6,12,15,7,8}
{7,14,24,8,8}
{8,15,38,14,16}
{9,17,70,16,16}
{10,18,114,32,32}
{11,20,209,32,32}
{12,22,362,64,64}
{13,23,664,64,64}
*)

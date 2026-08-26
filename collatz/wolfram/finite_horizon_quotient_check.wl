(* Exact Wolfram cross-check for the finite-horizon Collatz quotient.

   This script has two purposes:
   1. reproduce the counterexample to the older all-future same-endpoint
      dominance claim;
   2. independently test the safe finite-horizon cylinder signature on small
      depths.

   All arithmetic is exact integer arithmetic.
*)

ClearAll[qMin, step, levels, suffixMap];

qMin[k_Integer] := Module[{q = 0},
  While[3^q < 2^k, q++];
  q
];

step[{r_, q_, y_}, k_Integer] :=
  Select[
    Table[
      Module[{b = bb, c, rr, yy, qq = q},
        c = BitXor[b, Mod[y, 2]];
        rr = r + c 2^k;
        yy = y + c 3^q;
        If[b == 0,
          yy = Quotient[yy, 2],
          yy = Quotient[3 yy + 1, 2];
          qq++
        ];
        {rr, qq, yy, b}
      ],
      {bb, 0, 1}
    ],
    #[[2]] >= qMin[k + 1] &
  ];

levels[0] = {{0, 0, 0}};
levels[k_Integer] := levels[k] =
  Flatten[(step[#, k - 1][[All, 1 ;; 3]]) & /@ levels[k - 1], 1];

suffixMap[state_, k_Integer, m_Integer] := Module[
  {cur = <|"" -> state|>, nxt, j, b, c, r, q, y, rr, qq, yy, path},
  For[j = 0, j < m, j++,
    nxt = <||>;
    KeyValueMap[
      (
        path = #1;
        {r, q, y} = #2;
        Do[
          c = BitXor[b, Mod[y, 2]];
          rr = r + c 2^(k + j);
          yy = y + c 3^q;
          qq = q;
          If[b == 0,
            yy = Quotient[yy, 2],
            yy = Quotient[3 yy + 1, 2];
            qq++
          ];
          If[qq >= qMin[k + j + 1],
            AssociateTo[nxt, path <> ToString[b] -> {rr, qq, yy}]
          ],
          {b, 0, 1}
        ]
      ) &,
      cur
    ];
    cur = nxt;
  ];
  cur
];

(* 1. Counterexample to global common-endpoint dominance. *)

s1 = {127, 8, 820};
s2 = {383, 7, 820};
d1 = suffixMap[s1, 10, 5];
d2 = suffixMap[s2, 10, 5];
best1 = First@SortBy[KeyValueMap[Append[#2, #1] &, d1], First];
best2 = First@SortBy[KeyValueMap[Append[#2, #1] &, d2], First];

Print["endpoint counterexample: ", {best1, best2}];
If[best1 =!= {2175, 11, 11765, "01101"} ||
   best2 =!= {1407, 12, 22841, "11111"},
  Print["FAIL: counterexample mismatch"];
  Exit[1]
];

(* 2. Small exhaustive test of the safe same-q finite-horizon signature. *)

results = Reap[
  Do[
    ss = levels[k];
    modulus = 2^m;
    groups = GatherBy[ss, {#[[2]], Mod[#[[3]], modulus]} &];
    Do[
      If[Length[group] >= 2,
        sorted = SortBy[group, First];
        base = First[sorted];
        A = suffixMap[base, k, m];
        Do[
          B = suffixMap[other, k, m];
          ok = Sort[Keys[A]] === Sort[Keys[B]] &&
            And @@ Table[
              A[path][[1]] <= B[path][[1]] &&
              B[path][[1]] - A[path][[1]] == other[[1]] - base[[1]],
              {path, Keys[A]}
            ];
          Sow[ok],
          {other, Rest[sorted]}
        ]
      ],
      {group, groups}
    ],
    {k, 1, 8},
    {m, 1, Min[4, 8 - k]}
  ]
][[2, 1]];

Print["finite-horizon tests: ", {Length[results], And @@ results}];
If[! And @@ results, Exit[2]];

Print["PASS"];

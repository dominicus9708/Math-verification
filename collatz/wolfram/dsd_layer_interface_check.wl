(* Exact independent audit for the DSD/Collatz layer interface. *)

ClearAll[affinePair, corr, traceCorr, cnt, words];

affinePair[w_List] := Fold[
  If[#2 == 0,
    {#[[1]]/2, #[[2]]/2},
    {3 #[[1]]/2, (3 #[[2]] + 1)/2}
  ] &,
  {1, 0},
  w
];

cnt[w_List] := {Length[w] - Total[w], Total[w]};

(* Standard odd-position correction. *)
corr[w_List] := Module[{pos = Flatten@Position[w, 1] - 1, q},
  q = Length[pos];
  Sum[2^pos[[i]] 3^(q - i), {i, 1, q}]
];

(* Ordered-trace functional on the occurrence support. *)
traceCorr[w_List] := Module[{h = Length[w], q = Total[w], pref},
  If[h == 0, Return[0]];
  pref = Accumulate[w];
  Sum[w[[j + 1]] 2^j 3^(q - pref[[j + 1]]), {j, 0, h - 1}]
];

words[h_Integer] := Tuples[{0, 1}, h];

allWordChecks = And @@ Flatten@Table[
  Table[
    With[{w = ww, q = Total[ww], ab = affinePair[ww]},
      ab[[1]] == 3^q/2^h &&
      ab[[2]] == corr[w]/2^h &&
      traceCorr[w] == corr[w]
    ],
    {ww, words[h]}
  ],
  {h, 0, 10}
];

EO = {0, 1};
OE = {1, 0};
compressionCheck = And[
  cnt[EO] == cnt[OE] == {1, 1},
  affinePair[EO][[1]] == affinePair[OE][[1]] == 3/4,
  corr[EO] == traceCorr[EO] == 2,
  corr[OE] == traceCorr[OE] == 1,
  affinePair[EO][[2]] == 1/2,
  affinePair[OE][[2]] == 1/4
];

If[TrueQ[allWordChecks && compressionCheck],
  Print["DSD/Collatz layer-interface Wolfram audit: PASS"],
  Print["DSD/Collatz layer-interface Wolfram audit: FAIL"]
];

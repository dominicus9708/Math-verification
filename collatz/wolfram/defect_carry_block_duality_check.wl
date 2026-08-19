(* Exact finite cross-check for defect-carry block duality. *)

ClearAll[step, survQ, oddPos, corr, canon, futureSet, testCell, localCarryCheck];

step[n_Integer] := If[EvenQ[n], Quotient[n, 2], Quotient[3 n + 1, 2]];

survQ[word_List] := Module[{q = 0},
  And @@ Table[q += word[[j]]; 3^q >= 2^j, {j, 1, Length[word]}]
];

oddPos[word_List] := Flatten[Position[word, 1]] - 1;

corr[word_List] := Module[{d = oddPos[word], q = Total[word]},
  Sum[2^d[[i]] 3^(q - i), {i, 1, q}]
];

canon[word_List] := Module[{h = Length[word], q = Total[word], rR},
  rR = corr[word];
  Mod[-PowerMod[3^q, -1, 2^h] rR, 2^h]
];

futureSet[h_Integer, q0_Integer, m_Integer] := Module[{N = 2^m, vals},
  vals = Select[Range[0, N - 1], Function[rho,
    Module[{x = rho, q = q0, ok = True},
      Do[
        If[OddQ[x], q++];
        x = step[x];
        If[3^q < 2^(h + j), ok = False; Break[]],
        {j, 1, m}
      ];
      ok
    ]
  ]];
  Mod[PowerMod[3^q0, -1, N] vals, N]
];

testCell[h_Integer, q_Integer, m_Integer] := Module[
  {M = 2^h, N = 2^m, words, dstar, wstar, Rstar, P, rstar, ystar,
   xiStar, S, states},

  words = Select[Tuples[{0, 1}, h], Total[#] == q && survQ[#] &];
  If[words === {}, Return[True]];

  dstar = Table[Min[Floor[i Log[2, 3]], h - q + i], {i, 0, q - 1}];
  wstar = Table[Boole[MemberQ[dstar, j]], {j, 0, h - 1}];
  Rstar = corr[wstar];
  P = 3^q;
  rstar = Mod[-PowerMod[P, -1, M] Rstar, M];
  ystar = Quotient[P rstar + Rstar, M];
  xiStar = Mod[PowerMod[P, -1, N] ystar, N];
  S = futureSet[h, q, m];

  states = Table[
    Module[{R = corr[w], r = canon[w], y, C, U, Tc, wr, V, xi},
      y = Quotient[P r + R, M];
      C = Rstar - R;
      U = Mod[PowerMod[P, -1, M] C, M];
      Tc = Quotient[P U - C, M];
      wr = Quotient[rstar + U, M];
      V = Mod[PowerMod[P, -1, N] Tc, N];
      xi = Mod[PowerMod[P, -1, N] y, N];
      If[!(r == rstar + U - wr M &&
           y == ystar + Tc - wr P &&
           xi == Mod[xiStar + V - wr, N]),
        Return[False]
      ];
      {r, U, wr, xi}
    ],
    {w, words}
  ];

  And @@ Table[
    With[
      {
        direct = Count[states, s_ /; s[[1]] < X && MemberQ[S, s[[4]]]],
        criterion = Count[states, s_ /;
          MemberQ[Table[Mod[-rstar + j, M], {j, 0, X - 1}], s[[2]]] &&
          MemberQ[S, s[[4]]]
        ]
      },
      direct == criterion
    ],
    {X, 1, M}
  ]
];

localCarryCheck[h_Integer, q_Integer, m_Integer] := Module[
  {M = 2^h, N = 2^m, P = 3^q, words, dstar, wstar, Rstar, rstar,
   ystar, xiStar},

  words = Select[Tuples[{0, 1}, h], Total[#] == q && survQ[#] &];
  If[words === {}, Return[True]];

  dstar = Table[Min[Floor[i Log[2, 3]], h - q + i], {i, 0, q - 1}];
  wstar = Table[Boole[MemberQ[dstar, j]], {j, 0, h - 1}];
  Rstar = corr[wstar];
  rstar = canon[wstar];
  ystar = Quotient[P rstar + Rstar, M];
  xiStar = Mod[PowerMod[P, -1, N] ystar, N];

  And @@ Table[
    Module[{d = oddPos[w], U = 0, V = 0, Ci, ai, ti, bi, eps,
            R, C, Utot, Ttot, Vtot, r, wr, xi},
      Do[
        Ci = 3^(q - 1 - i) (2^dstar[[i + 1]] - 2^d[[i + 1]]);
        ai = Mod[PowerMod[P, -1, M] Ci, M];
        ti = Quotient[P ai - Ci, M];
        bi = Mod[PowerMod[P, -1, N] ti, N];
        eps = Boole[U + ai >= M];
        U = U + ai - eps M;
        V = Mod[V + bi - eps, N],
        {i, 0, q - 1}
      ];

      R = corr[w];
      C = Rstar - R;
      Utot = Mod[PowerMod[P, -1, M] C, M];
      Ttot = Quotient[P Utot - C, M];
      Vtot = Mod[PowerMod[P, -1, N] Ttot, N];
      r = canon[w];
      wr = Quotient[rstar + Utot, M];
      xi = Mod[PowerMod[P, -1, N] Quotient[P r + R, M], N];

      U == Utot && V == Vtot && xi == Mod[xiStar + V - wr, N]
    ],
    {w, words}
  ]
];

checks1 = Flatten@Table[
  If[3^q >= 2^h, testCell[h, q, m], Nothing],
  {h, 1, 7}, {q, 0, h}, {m, 1, 4}
];

checks2 = Flatten@Table[
  If[3^q >= 2^h, localCarryCheck[h, q, m], Nothing],
  {h, 1, 7}, {q, 0, h}, {m, 1, 4}
];

Print["global_identities_and_threshold_criterion=", And @@ checks1,
      ", cases=", Length[checks1]];
Print["local_two_coordinate_channel_recurrence=", And @@ checks2,
      ", cases=", Length[checks2]];

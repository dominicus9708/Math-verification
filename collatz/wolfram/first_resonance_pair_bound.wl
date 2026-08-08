(* First-resonance pair-bound check for the accelerated Collatz map.
   This is a reproducibility calculation, not a global Collatz proof. *)

q = 72057431991;
sigma = 114208327604;
L = 4*3^44 + 2;

prec = 100;
l2 = N[Log[2], prec];
l3 = N[Log[3], prec];

(* Conservative padding around the high-precision log values. *)
l2i = Interval[{l2 - 10^-90, l2 + 10^-90}];
l3i = Interval[{l3 - 10^-90, l3 + 10^-90}];

lambdaI = sigma*l2i - q*l3i;
deltaI = Exp[lambdaI] - 1;
rhsI = 24*L*deltaI;
marginI = rhsI - (7*q + 1);

Print["L = ", L];
Print["lambda interval = ", N[lambdaI, 50]];
Print["24 L (exp(lambda)-1) interval = ", N[rhsI, 50]];
Print["positive margin interval = ", N[marginI, 50]];

(* Equivalent high-precision diagnostic start bound. *)
aa = N[Log[2, 3], 180];
s = Ceiling[q*aa];
delta = Exp[(s - q*aa)*Log[2]] - 1;
Supper = (7*q + 1)/24;
Xupper = Supper/delta;
Print["sigma = ", s];
Print["delta = ", N[delta, 60]];
Print["pair-bound Xupper = ", N[Xupper, 50]];
Print["Xupper/L = ", N[Xupper/L, 40]];

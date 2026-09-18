# MATH-207 — phase-rotation conjugacy and boundary coefficient telescope

Date: 2026-09-19

Status: `EXACT STRUCTURAL REDUCTION / VARIABLE-r COMMON CLOCK / DEPTH-LOOP ELIMINATION / GLOBAL CLOSURE OPEN`

## 1. Purpose

The proof program must not return to a separate loop over paid-count layers or depth windows.

MATH-179 already gives a closed phase clock for each fixed paid count (r). This note strengthens it in two directions:

1. all paid counts are conjugate to one circle rotation law;
2. an arbitrary sequence (r_1,r_2,ldots) depends on the paid counts only through their cumulative sum.

A second consequence is an exact telescope for the affine coefficient of complete zero-cost-prefix + paid-cluster boundary blocks.

These identities are intended to replace repeated depth/r enumeration in the mainline.

## 2. Beatty notation

Let

[
	heta=log_2(3/2),
qquad
m(r)=lfloor r	hetafloor,
qquad
alpha_r={r	heta}=r	heta-m(r).
]

Because (2) and (3) are multiplicatively independent,

[
oxed{	heta
otinmathbb Q}
]

and therefore

[
oxed{alpha_r
otinmathbb Qquad(rge1).}
]

MATH-179 uses

[
	au_r=rac{3^r}{2^{r+m(r)+1}}.
]

Since (log_2 3=1+	heta),

[
oxed{	au_r=2^{alpha_r-1}.}
]

## 3. Log-phase coordinate

For normalized phase

[
arpiin(1/2,1],
]

define

[
oxed{x=-log_2arpiin[0,1).}
]

MATH-179 gives

[
E_r(arpi)
=
m(r)+mathbf1_{{arpile	au_r}}
]

and

[
arpi'
=
arpirac{2^{r+E_r(arpi)}}{3^r}.
]

The threshold condition becomes

[
arpile	au_r
iff
xge1-alpha_r.
]

Hence

[
x'
=
x+alpha_r
-
mathbf1_{{xge1-alpha_r}}.
]

Therefore

[
oxed{
x'={x+alpha_r}.
}
]

Every paid-count transition is the same circle rotation, with rotation amount equal to the fractional part of (r	heta).

## 4. Arbitrary paid-count sequence

Let

[
r_0,r_1,ldots,r_{n-1}ge1
]

be any sequence of completed paid first-return clusters, and put

[
R_n=sum_{i=0}^{n-1}r_i.
]

Repeated application of the rotation law gives

[
oxed{
x_n={x_0+	heta R_n}.
}
]

Thus the phase does not require a separate state evolution for every (r_i).

It depends only on

- the initial phase (x_0);
- the cumulative paid count (R_n).

In particular, if (R_n>0), then

[
x_n=x_0
]

would imply (R_n	hetainmathbb Z), impossible because (	heta) is irrational.

Hence

[
oxed{
	ext{no nontrivial finite paid-cluster sequence can return the phase exactly to its starting value.}
}
]

This is an exact aperiodicity statement for the phase coordinate only; it is not a Collatz aperiodicity theorem.

## 5. Cumulative paid-cluster length

For one cluster,

[
h_r
=
r+1+m(r)
+
mathbf1_{{xge1-alpha_r}}.
]

The rotation identity gives

[
m(r_i)+I_i
=
x_i+r_i	heta-x_{i+1}.
]

Summing,

[
sum_{i=0}^{n-1}igl(m(r_i)+I_iigr)
=
x_0+	heta R_n-x_n
=
lfloor x_0+	heta R_nfloor.
]

Therefore the total local paid-cluster shortcut length is

[
oxed{
sum_{i=0}^{n-1}h_{r_i}
=
R_n+n+lfloor x_0+	heta R_nfloor.
}
]

This is a single closed formula for an arbitrary mixture of paid counts.

For repeated fixed (r),

[
oxed{
H_n^{(r)}
=
nr+n+lfloor x_0+nr	hetafloor.
}
]

So neither the individual (arepsilon)-bits nor each intermediate cluster depth must be enumerated.

## 6. Paid-cluster coefficient cocycle

Let (arpi_i) be the entry phase and (arpi_{i+1}) the exit phase of an (r_i)-paid first-return cluster.

From

[
arpi_{i+1}
=
arpi_i
rac{2^{h_{r_i}-1}}{3^{r_i}},
]

we obtain

[
oxed{
rac{3^{r_i}}{2^{h_{r_i}}}
=
rac{arpi_i}{2arpi_{i+1}}.
}
]

Therefore for (n) consecutive paid clusters,

[
oxed{
prod_{i=0}^{n-1}
rac{3^{r_i}}{2^{h_{r_i}}}
=
rac{arpi_0}{2^narpi_n}.
}
]

This explains why the extra return-even step contributes exactly one factor (1/2) per paid cluster.

## 7. Complete boundary block telescope

A proof-facing boundary block consists of

1. a zero-cost mechanical prefix from boundary phase (omega) to paid-cluster entry phase (arpi);
2. one paid first-return cluster from (arpi) to the next boundary phase (omega').

Let the zero-cost prefix have length (L) and odd count (q).

At the paid exit its slack is exactly (u=1), so

[
arpi
=
omegarac{2^{L+1}}{3^q}.
]

Hence

[
oxed{
rac{3^q}{2^L}
=
rac{2omega}{arpi}.
}
]

For the following (r)-paid first-return cluster,

[
oxed{
rac{3^r}{2^{h_r}}
=
rac{arpi}{2omega'}.
}
]

Multiplication cancels both the intermediate phase and the two factors of (2):

[
oxed{
rac{3^{q+r}}{2^{L+h_r}}
=
rac{omega}{omega'}.
}
]

Thus a complete boundary factor with total odd count (Q=q+r) and total depth (H=L+h_r) satisfies

[
oxed{
rac{3^Q}{2^H}
=
rac{omega}{omega'}.
}
]

## 8. Arbitrary boundary-chain telescope

For boundary blocks (i=0,ldots,n-1),

[
rac{3^{Q_i}}{2^{H_i}}
=
rac{omega_i}{omega_{i+1}}.
]

Therefore

[
oxed{
rac{3^{Q_{m tot}}}{2^{H_{m tot}}}
=
rac{omega_0}{omega_n},
}
]

where

[
Q_{m tot}=sum_iQ_i,
qquad
H_{m tot}=sum_iH_i.
]

Since every normalized phase lies in ((1/2,1]),

[
oxed{
rac12
<
rac{3^{Q_{m tot}}}{2^{H_{m tot}}}
<
2.
}
]

Equivalently,

[
oxed{
|Q_{m tot}log_2 3-H_{m tot}|<1.
}
]

This is the desired depth-axis compression: across complete boundary blocks, total depth is determined by total odd count up to one phase bit of uncertainty.

## 9. No exact boundary-phase cycle

If a nonempty chain returned to the same boundary phase,

[
omega_n=omega_0,
]

then the telescope would give

[
3^{Q_{m tot}}=2^{H_{m tot}}.
]

For positive integers (Q_{m tot},H_{m tot}), this is impossible by unique prime factorization.

Hence

[
oxed{
	ext{no nonempty legal complete boundary chain can have an exact phase return.}
}
]

This does not by itself exclude an ordinary-integer aperiodic chain, but it removes exact phase cycles without any depth or (r)-layer enumeration.

## 10. Relation to the project goal

The mainline should now treat

[
(r,k)	ext{ grids}
]

as derived coordinates rather than outer loops.

The common proof state should advance the MATH-187 one-step recurrence, while

- paid count is emitted at first return;
- depth is derived from the common clock;
- phase is represented by one rotation coordinate;
- MATH-202 supplies (z_{min}(r)) as a function of the emitted paid count;
- MATH-205 transports the exact address carry.

MATH-206 remains a finite regression/support audit for the (r=10) tag, not the architecture of the final proof.

## 11. Claim boundary

Established:

- exact circle-rotation conjugacy for every (r);
- arbitrary variable-(r) phase composition by cumulative paid count;
- exact cumulative paid-cluster length formula;
- exact paid-cluster coefficient cocycle;
- exact complete-boundary coefficient telescope;
- depth/odd-count discrepancy below one bit across complete boundary chains;
- no exact nontrivial boundary-phase return.

Not established:

- exclusion of every aperiodic ordinary-integer carry path;
- closure of the (r=10) singleton carry kernel;
- first universal Farey-cell emptiness;
- the Collatz conjecture.

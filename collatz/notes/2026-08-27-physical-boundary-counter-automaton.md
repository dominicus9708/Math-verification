# Physical ordinary-boundary counter automaton for the repaired A0 branch

Date: 2026-08-27

Status: **SAFE exact boundary compression.** This is a finite ordinary-boundary representation theorem. It does not prove the Collatz conjecture and does not replace the long Hensel/ordering feasibility problem.

## 1. Exact first-global start counter

At the repaired first global resonance,

\[
2^{71}<N<\frac43\,2^{71},
\qquad N\equiv3\pmod4.
\]

Put

\[
N_0:=2^{71}+3.
\]

Then every physical start has the unique form

\[
\boxed{N=N_0+4s}
\]

with

\[
\boxed{0\le s<S},
\qquad
S=196765270119568550570.
\]

Exact comparison gives

\[
\boxed{3^{42}<S<3^{43}}.
\]

Hence the complete ordinary start band is a bounded **43-trit counter**.

Because 4 is a unit modulo every power of three, the residues

\[
N_0+4s\pmod{3^h},\qquad0\le s<S,
\]
cover every class modulo \(3^h\) for every

\[
\boxed{h\le42}.
\]

At \(h=43\) the counter becomes injective and the first genuine root-band residue selectivity appears.

The number of missing \(43\)-trit root classes is exactly

\[
\boxed{3^{43}-S=131491697274968527057}.
\]

This explains why a finite Hensel refinement of depth at most 42 cannot obtain a positive uniform tax merely from the absolute root interval: the ordinary root band still realizes every ternary residue at those depths.

## 2. Exact first-global gap counter

The first resonance gap satisfies

\[
0<g<2^{33},
\qquad4\mid g.
\]

Write

\[
\boxed{g=4r},
\qquad
1\le r<R,
\qquad
R=2^{31}.
\]

Since

\[
3^{19}<2^{31}<3^{20},
\]

the complete gap is a bounded **20-trit counter**.

Thus the exact physical first-global two-boundary family is parameterized by only

\[
\boxed{(s,r)}
\]

with

\[
N=N_0+4s,
\qquad
Y=N_0+4(s+r).
\]

The endpoint index

\[
k:=s+r
\]

runs through the complete interval

\[
\boxed{1\le k\le S+R-2}
\]
with

\[
S+R-2=196765270121716034216.
\]

The previously used coarse endpoint-only interval contains exactly two extra congruence points: the lower \(g=0\) endpoint and the unattainable simultaneous upper extreme. The two-counter parametrization removes both without using any Hensel or defect argument.

## 3. LSB-first bounded-counter automaton

The Hensel process exposes ternary information from low digits upward, so the ordinary bounds should be represented in the same direction.

Let

\[
0\le x\le B<3^m
\]
with ternary digits \(x_i,B_i\), read least-significant first.

Subtract \(x\) from \(B\) using the one-bit borrow state

\[
b_i\in\{0,1\}.
\]

At digit \(i\),

\[
T_i=B_i-x_i-b_i.
\]

Set

\[
b_{i+1}=
\begin{cases}
1,&T_i<0,\\
0,&T_i\ge0.
\end{cases}
\]

Then, after the fixed \(m\) digits,

\[
\boxed{x\le B\iff b_m=0}.
\]

Therefore the 43-trit root counter and 20-trit gap counter each require only a two-state comparison memory, plus a one-bit nonzero flag for \(r>0\).

The boundary family is huge as a set of integers, but its **ordinary-language state complexity is constant**.

## 4. Mechanical terminal zero ray: unique 44-trit physical lift

Let \(Y_m^{m mech}\) denote the last-\(m\)-odd mechanical terminal residue.

The exact certificate finds one unique physical endpoint compatible with the zero-displacement terminal ray through depth 44:

\[
\boxed{
Y_*=2729562462203742221059.
}

For

\[
h=42,43,44,
\]

\[
Y_h^{m mech}\equiv Y_*\pmod{3^h}.
\]

The complete 46-trit mechanical endpoint is

\[
Y_{m mech}=4699104266570964686821.
\]

The difference is exactly

\[
\boxed{
Y_{m mech}-Y_*=2\cdot3^{44}.
}
\]

Hence the zero-displacement terminal ray matches a physical ordinary endpoint through exactly 44 ternary digits and fails at the 45th digit.

This is stronger than a floating or interval statement: the first mismatch is one exact ternary digit.

It is still only a boundary mismatch theorem. A nonzero displacement can repair that digit, so this does not close the resonance.

## 5. Reset-strip counter representation

After the certified

\[
A_0,A_0,J_0
\]
reset,

\[
0\le d<0.478G,
\qquad G=2^{33}.
\]

For one subsequent A0 block,

\[
d'<d+a_A<0.9803G.
\]

The exact integer supersets are therefore

\[
0\le d<D_-,
\qquad
D_-=4105988735<3^{21},
\]

and

\[
0\le d'<D_+,
\qquad
D_+=8420712881<3^{21}.
\]

Thus the reset physical boundary can be represented by

\[
\boxed{(s,d,d',p_{m int})}
\]
with

\[
egin{aligned}
&0\le s<S<3^{43},\\
&0\le d<D_-<3^{21},\\
&0\le d'<D_+<3^{21},\\
&p_{m int}\in\{0,1\},
\end{aligned}
\]

and

\[
N=N_0+4s,
\qquad
X=N+d,
\qquad
Y=N+d'.
\]

The physical Hensel boundaries at any requested finite depth are then supplied by

\[
K_R=-Y,
\qquad
K_L=-2^{-A_0}X.
\]

This is an ordinary-input boundary oracle, not a fixed \(Kmod3^m\) quotient of the infinite Hensel dynamics.

## 6. DSD audit

### SAFE

\[
	ext{ordinary bounded counters}
	o
(X,Y)
	o
	ext{physical Hensel boundaries at requested depth}.
\]

The counter bounds are upstream arithmetic data. No Hensel lower cost or near-root defect lower estimate is used to create them.

### REJECTED

Do not replace the ordinary counters by a single fixed finite carry residue for an unbounded horizon.

Do not discard the common absolute root counter and keep only the local gap residue; the previously proved covariance theorem shows that gap-only compression admits abstract zero-cost lifts.

## 7. Next gate

The remaining state question is not the cardinality of the ordinary boundary set. That part is now finite-state.

The useful next question is whether the exact two-boundary Hensel operator itself admits a covariance-invariant representation in which these physical counters enter only through a smaller exact boundary invariant.

Companion certificate:

`collatz/src/physical_boundary_counter_automaton_certificate.py`

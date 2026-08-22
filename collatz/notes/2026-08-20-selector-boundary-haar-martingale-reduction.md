# Selector-boundary Haar martingale reduction

Date: 2026-08-20

Status: **exact martingale/Haar reformulation of the Stage-4 correlation term, with finite bulk/sparse diagnostics. This is not a proof of the Collatz conjecture.**

## 1. Selector density as a dyadic martingale

For the ternary selector

\[
S_m=3^m+\sum_{i=0}^{m-1}a_i3^i,
\qquad a_i\in\{0,1\},
\]

let \(\mu_{m,r}\) be its probability distribution modulo \(2^r\), and define the density relative to the uniform measure on \(\mathbb Z/2^r\mathbb Z\) by

\[
\boxed{g_{m,r}(x)=2^r\mu_{m,r}(x).}
\]

The family \(g_{m,r}\) is a dyadic martingale under projection from level \(r+1\) to level \(r\).

For

\[
p_r(m)=\sum_x\mu_{m,r}(x)^2,
\qquad
 e_r(m)=2p_{r+1}(m)-p_r(m),
\]

the level-r martingale increment satisfies the exact identity

\[
\boxed{\|\Delta_r g_m\|_2^2=2^r e_r(m).}
\]

The previously proved collision-halving identity is therefore precisely the Haar energy at one dyadic scale.

## 2. Exact energy telescope

Orthogonality of the dyadic martingale differences gives

\[
\boxed{
\sum_{s=0}^{R-1}2^s e_s(m)
=2^Rp_R(m)-1.
}
\]

This can also be checked directly by substituting
\(e_s=2p_{s+1}-p_s\): the sum telescopes.

Thus all selector sibling-imbalance energies through depth \(R\) are controlled by the single collision quantity \(2^Rp_R(m)-1\).

## 3. Beatty boundary as a Haar test function

Consider a coefficient-barrier rise from parent length \(L\) to child length \(L+1\). In the reduced coordinate \(N=4y+3\), the parent quotient has size

\[
M=2^{L-2}.
\]

Let \(\partial_L\) be the set of one-child coefficient-boundary parents and \(B_L=|\partial_L|\). For each boundary parent \(x\), let \(v_L(x)=+1\) if the lower child survives and \(-1\) if the upper child survives.

Define the child-level Haar function

\[
h_L(x)=v_L(x),
\qquad
h_L(x+M)=-v_L(x)
\]

on boundary sibling pairs and zero elsewhere. Then

\[
\boxed{
\|h_L\|_2^2=\frac{B_L}{2^{L-2}}.
}
\]

If \(K_L\) is the exact selector repair term in

\[
2C_{L+1}=2C_L-D_L+K_L,
\]

then the spatial mass-transport identity becomes the exact Haar pairing

\[
\boxed{
\frac{K_L}{2^m}
=\langle h_L,\Delta_{L-2}g_m\rangle.
}
\]

Consequently

\[
\boxed{
\frac{(K_L/2^m)^2}{B_L/2^{L-2}}
\le 2^{L-2}e_{L-2}(m).
}
\]

This is the same theorem as the previously derived boundary Cauchy estimate, now placed in its natural dyadic martingale space.

## 4. Global square-energy budget for all Beatty rises

Different rise depths occupy different Haar levels. Summing the preceding inequality therefore yields, for all rise levels with \(L-2<R\),

\[
\boxed{
\sum_{L\ {m rise}}
\frac{(K_L/2^m)^2}{B_L/2^{L-2}}
\le
2^Rp_R(m)-1.
}
\]

This removes the need to prove an independent correlation estimate at every rise.

The unweighted coefficient language has the exact lifetime boundary budget

\[
\boxed{
\sum_{L\ge2,\,L\to L+1\ {m rise}}
\frac{B_L}{2^{L-2}}=2.
}
\]

Indeed, writing \(C_L^{(0)}\) for the unweighted number of coefficient-surviving reduced residues and \(P_L=C_L^{(0)}/2^{L-2}\), a rise loses exactly \(B_L/2^{L-1}\) in normalized probability. The first two forced odd bits leave normalized reduced mass one and the later coefficient-survival probability tends to zero; telescoping gives the displayed total Haar support budget.

A second Cauchy inequality therefore gives the lifetime absolute-repair estimate

\[
\boxed{
\sum_{L\ {m rise}}\frac{|K_L|}{2^m}
\le
\sqrt{2\bigl(2^Rp_R(m)-1\bigr)}
}
\]

for the rises included below level \(R\), and analogously with the appropriate partial boundary budget for a finite range.

This is a genuine global reduction, but it is not yet an extinction theorem: one still needs either a subexponential bound on the selector collision energy or a deterministic treatment of the sparse tail.

## 5. Important negative result: small selector-only constants fail

The trial conjecture

\[
2^m e_r(m)\le\frac54
\]

is false. Exact middle-band calculations give

\[
\boxed{
2^{26}e_{16}(26)
=\frac{14419123}{8388608}
\approx1.7188934088,
}
\]

and

\[
\boxed{
2^{29}e_{17}(29)
=\frac{436843091}{134217728}
\approx3.2547346577.
}
\]

Thus Stage 4 should not be based on a small universal selector-only collision constant.

A second trial bound \(2^mp_m(m)\le2\) also fails in the finite scan: at \(m=23\), the exact value is approximately \(2.02641\). The useful target is therefore the much weaker growth statement

\[
\boxed{2^mp_m(m)=2^{o(m)}}
\]

or another bound whose exponential rate is below the formation entropy gap. No such theorem is claimed here.

## 6. Mixed correlation is much smaller than selector-only resonance

The selector-only resonance does not automatically produce a dangerous Stage-4 repair. At the exact resonance point \((m,r)=(29,17)\), corresponding to the Beatty boundary split at parent length \(L=19\), the direct mass transport gives

\[
C=61397829,
\qquad
D=10865114,
\qquad
U=1394379,
\qquad
K=5842.
\]

Hence

\[
\boxed{
\frac{|K|}{D}\approx5.37684\times10^{-4},
}
\]

whereas the orientation-free sibling imbalance is

\[
\frac UD\approx0.1283.
\]

This supports the mixed selector/Beatty-orientation route: a large selector Haar energy can remain nearly orthogonal to the coefficient-boundary orientation.

## 7. Exact finite bulk/sparse profiles

Directly propagating the full ternary selector candidates through their coefficient-survival lifetimes gives the following finite diagnostics.

### m=20, extinction depth 265

For nontrivial rises \(L\ge3\),

\[
\max |K|/\sqrt D\approx2.656.
\]

For \(D\ge1000\),

\[
\max |K|/D\approx0.05384.
\]

The first exact alignment \(|K|=D\) occurs only at \(L=187\), where \(C=20\) and \(D=3\).

### m=22, extinction depth 317

\[
\max |K|/\sqrt D\approx5.014,
\]

and for \(D\ge1000\),

\[
\max |K|/D\approx0.05179.
\]

The first exact alignment appears at \(L=196\) with \(C=62,D=4\).

### m=24, extinction depth 386

\[
\max |K|/\sqrt D\approx2.406,
\]

and for \(D\ge1000\),

\[
\max |K|/D\approx0.03419.
\]

The first exact alignment appears at \(L=239\) with \(C=39,D=2\).

These are finite exact profiles, not a uniform theorem. They consistently show a bulk/sparse dichotomy: square-root-sized discrepancy while boundary mass is large, followed by possible perfect alignment only after the candidate mass has become very small.

## 8. Revised Stage-4 target

The useful proof front is now

\[
\boxed{
\text{Haar-controlled bulk}
\longrightarrow
\text{sparse deterministic tail}.
}
\]

For the bulk it is enough to obtain a subexponential bound on the total selector martingale energy, or directly on the mixed Haar pairings. A small fixed selector-only constant is unnecessary and empirically false.

For the sparse tail the existing minimal-survivor / four-channel min-plus machinery is the natural complementary tool. The global theorem should therefore combine a cumulative Haar repair budget with a deterministic lower bound on the smallest surviving natural start once the active selector mass is small.

Certificate:

`collatz/src/selector_boundary_haar_martingale_certificate.py`.

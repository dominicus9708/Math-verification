# Delta-q=1 true first-merge two-channel system

Date: 2026-08-10

Status: **SUPERSEDED IN PART on 2026-08-11**.

The affine two-channel derivation, corrected lifted-predecessor definition, last-step Type A/Type B classification, merge-gap identity, congruence restriction, and 3-adic carry representation remain valid.

The stronger theorem target

\[
G=r_L-3r_H>0
\]

for every coefficient-surviving true first merge is **false** and must not be used.

The current corrected analysis is maintained in:

`collatz/notes/2026-08-11-deltaq1-carry-wrap-dominance.md`

The corresponding exact implementation is:

`collatz/src/deltaq1_carry_wrap_dominance.cpp`

## 1. Valid affine channel system

For

\[
F_p(x)=\frac{3^p x+p}{2},\qquad p\in\{0,1\},
\]

write

\[
T^j(r)=\frac{3^{q_j}r+R_j}{2^j}.
\]

Then

\[
q_{j+1}=q_j+p_j,
\qquad
R_{j+1}=3^{p_j}R_j+p_j2^j.
\]

With \(C_j=R_j/2^j\),

\[
C_{j+1}=F_{p_j}(C_j).
\]

For two channels H,L,

\[
\Delta x_j=x_{H,j}-x_{L,j},
\qquad
d_j=q_{H,j}-q_{L,j},
\]

and a parity pair \((p_H,p_L)\),

\[
\Delta x_{j+1}
=
\frac{
3^{p_H}\Delta x_j
+(3^{p_H}-3^{p_L})x_{L,j}
+(p_H-p_L)
}{2},
\]

\[
d_{j+1}=d_j+p_H-p_L.
\]

## 2. Valid true-first-merge definition

A depth-k canonical child obtained from a depth-(k-1) parent by a lift \(c2^{k-1}\) has actual predecessor

\[
\widetilde y=y+c3^q.
\]

Therefore a true first merge must compare the lifted predecessors, not the unlifted parent endpoints.

For a genuine first merge the final parities differ. With final \(\Delta q=1\), the two possible last-step types are:

### Type A

\[
(p_H,p_L)=(1,0),
\qquad
\Delta q_{k-1}=0.
\]

### Type B

\[
(p_H,p_L)=(0,1),
\qquad
\Delta q_{k-1}=2.
\]

## 3. Valid merge-gap and carry identities

At a common endpoint with

\[
q_H=q+1,\qquad q_L=q,
\]

we have

\[
2^k y=3^{q+1}r_H+R_H=3^qr_L+R_L,
\]

so

\[
\boxed{
G:=r_L-3r_H=\frac{R_H-R_L}{3^q}.
}
\]

Coefficient survival through depth at least two gives

\[
r_H\equiv r_L\equiv3\pmod4,
\]

hence

\[
G\equiv2\pmod4.
\]

For odd positions

\[
0=a_0<a_1<\cdots<a_q
\]

and

\[
0=b_0<b_1<\cdots<b_{q-1},
\]

the exact correction gap is

\[
G
=1+
\sum_{i=0}^{q-1}
\frac{2^{a_{i+1}}-2^{b_i}}{3^{i+1}}.
\]

Setting \(c_q=0\) and

\[
\boxed{
c_i=
\frac{2^{a_{i+1}}-2^{b_i}+c_{i+1}}{3}
}
\]

gives

\[
\boxed{G=1+c_0.}
\]

These identities remain part of the current method.

## 4. Counterexample to the discarded G>0 target

An exact coefficient-surviving Type-B true first merge occurs at depth

\[
\boxed{k=37}
\]

with

\[
r_H=11,828,881,407,
\qquad
r_L=35,486,644,219,
\]

\[
Q_H=25,
\qquad
Q_L=24,
\]

and

\[
T^{37}(r_H)=T^{37}(r_L)=72,923,114,054.
\]

Nevertheless,

\[
\boxed{G=-2.}
\]

Thus correction order \(R_H>R_L\), equivalently \(G>0\), is not a valid global first-merge theorem.

## 5. Corrected target

The endpoint Pareto quotient requires only

\[
\boxed{r_H<r_L.}
\]

Define

\[
J:=r_L-r_H.
\]

Since \(r_L=3r_H+G\),

\[
\boxed{J=2r_H+G=2r_H+1+c_0.}
\]

The depth-37 counterexample has \(G=-2\) but still satisfies

\[
J=23,657,762,812>0.
\]

The current problem is therefore to exclude

\[
\boxed{J\le0}
\]

at a coefficient-surviving true first merge, not to exclude all negative \(G\).

See the 2026-08-11 carry-wrap dominance note for the exact 3-adic carry / 2-adic wrap formulation and finite certificate through lower odd-count \(q\le33\).

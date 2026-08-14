# Epsilon-coordinate mod-19 selector for Collatz semiconvergents

Date: 2026-08-14

Status: **exact Euclidean-coordinate arithmetic theorem + exact identification of the current resonance**. It explains the uniqueness of the present R1 resonance inside its induced continued-fraction cell by a mod-19 integrality channel. It does not eliminate that resonance and does not prove Collatz.

Put

\[
\alpha:=\log_3 2,
\qquad
\varepsilon:=12-19\alpha.
\]

For an original coefficient pair `(A,H)`, define its epsilon-coordinate numerator

\[
\boxed{p:=12A-19H,\qquad r:=A.}
\]

Then

\[
\frac pr-\varepsilon
=19\left(\alpha-\frac HA\right).
\]

Thus the Diophantine approximation problem for `H/A` is carried exactly to the approximation problem for `epsilon`.

## 1. Return map from epsilon rationals to integer coefficient pairs

Conversely, given a rational approximation

\[
\frac pr
\]

to `epsilon`, the corresponding original coefficient pair would be

\[
\boxed{
A=r,
\qquad
H=\frac{12r-p}{19}.
}
\]

Therefore a rational in epsilon-space corresponds to an actual integer Collatz coefficient pair if and only if

\[
\boxed{
12r-p\equiv0\pmod{19}.
}
\]

This is an independent arithmetic channel on top of the continued-fraction approximation condition.

## 2. General semiconvergent selector

Let two adjacent epsilon-space convergent vectors be

\[
v_0=(p_0,r_0),
\qquad
v_1=(p_1,r_1).
\]

Inside the next continued-fraction cell, the semiconvergents are

\[
\boxed{
v_k=v_0+k v_1,
\qquad k=1,\ldots,a,}
\]

where `a` is the next partial quotient.

Define the linear mod-19 coordinate

\[
\chi(p,r):=12r-p\pmod{19}.
\]

Then

\[
\boxed{
\chi(v_k)=\chi(v_0)+k\chi(v_1)\pmod{19}.
}
\]

If

\[
\chi(v_1)\not\equiv0\pmod{19},
\]

there is exactly one solution class

\[
\boxed{
k\equiv
-\chi(v_0)\chi(v_1)^{-1}\pmod{19}.}
\]

Hence, whenever the cell width satisfies

\[
\boxed{a<19,}
\]

there is **at most one** semiconvergent in that cell that can map back to an integer `(A,H)` pair.

This is a deterministic arithmetic thinning of the Euclidean candidate family.

## 3. Current cell

For the cell containing the present R1 resonance, take

\[
\boxed{
v_0
=(235,984,999,
19,131,826,526),}
\]

\[
\boxed{
v_1
=(350,384,211,
28,406,424,013).}
\]

The next epsilon continued-fraction partial quotient is

\[
\boxed{a=13.}
\]

Their mod-19 coordinates are

\[
\boxed{
\chi(v_0)=8,
\qquad
\chi(v_1)=7.
}
\]

Therefore the integer-return condition is

\[
8+7k\equiv0\pmod{19}.
\]

Since

\[
7^{-1}\equiv11\pmod{19},
\]

we get

\[
\boxed{k\equiv7\pmod{19}.}
\]

Because `1<=k<=13`, the unique allowed value is

\[
\boxed{k=7.}
\]

## 4. Exact recovery of the current resonance

The selected epsilon semiconvergent is

\[
\begin{aligned}
(p,r)
&=v_0+7v_1\\
&=(2,688,674,476,
217,976,794,617).
\end{aligned}
\]

Transforming back gives

\[
A=r=217,976,794,617,
\]

and

\[
H=rac{12r-p}{19}
=137,528,045,312.
\]

Thus

\[
\boxed{
(A,H)
=(217,976,794,617,
137,528,045,312),
}
\]

exactly the unique resonance isolated independently by the global Worley/mechanical-envelope certificate.

## 5. Conceptual consequence

The current resonance is not merely an unexplained exceptional continued-fraction point.

In the induced gate coordinate it is the intersection

\[
\boxed{
\text{epsilon semiconvergent cell}
\cap
\text{mod-19 integer-return channel}.
}
\]

The two independent reductions agree:

1. the Archimedean first-crossing/Worley argument says only one coefficient pair survives below the current denominator ceiling;
2. the Euclidean gate coordinate says the relevant partial-quotient cell contains only one semiconvergent compatible with the original integer lattice, namely `k=7`.

This gives a structural reason for the isolation and suggests a reusable rule at later scales: each epsilon continued-fraction cell should first be thinned by the mod-19 selector before any expensive mixed-place analysis is performed.

If the next partial quotient is less than 19, at most one semiconvergent from that cell can return to an integer Collatz coefficient pair.

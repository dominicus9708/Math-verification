# Conditional next-bit balance on the A_30 coefficient-survivor tree

Date: 2026-08-12

Status: **exact finite cross-base transport diagnostic**. Through the current fixed class range, the ternary representative mass conditioned on coefficient-surviving parent cylinders is almost perfectly balanced between the two new binary lifts, even on the one-child boundary parents where the dynamics selects one lift. This is finite evidence for the correlation estimate required by the growing-resolution child-transport theorem; it is not an asymptotic theorem.

## 1. Setup

Use

\[
A_{30}=\left\{4\left(3^{44}+\sum_{i=0}^{29}a_i3^i\right)+3:\ a_i\in\{0,1\}\right\}.
\]

By the additive-free coefficient-barrier theorem, for every current `m=44` start and every `k<=44`, descent below the start is equivalent to

\[
3^{q_k}<2^k.
\]

Hence for the resolutions considered here the exact dangerous dyadic tree is the coefficient-survivor tree

\[
q_j\ge a_j,
\qquad
a_j:=\lceil j\log_3 2\rceil.
\]

At a transition `L -> L+1`, if

\[
a_{L+1}=a_L,
\]

all survivor parents have two children and there is no one-child pruning.

If

\[
a_{L+1}=a_L+1,
\]

the one-child parents are exactly the boundary paths

\[
q_L=a_L.
\]

## 2. Child-transport quantities

Use the notation of `2026-08-12-growing-resolution-child-transport-identity.md`:

\[
C_L=\sum_{r\in R_L}c(r),
\]

\[
D_L=\{r\in R_L:m(r)=1\},
\]

\[
M_D(L):=\sum_{r\in D_L}c(r),
\]

and the signed cross-correlation

\[
\boxed{
K_L:=\sum_{r\in D_L}v(r)u(r).
}
\]

Then

\[
\boxed{
C_{L+1}
=C_L-\frac12\left(M_D(L)-K_L\right)
}
\]

at the active coefficient-threshold steps, since there are no zero-child coefficient-survivor parents.

Define

\[
\eta_L:=\frac{M_D(L)}{C_L}
\]

and

\[
\varepsilon_L:=\frac{K_L}{M_D(L)}.
\]

The one-child mass is retained in the fraction

\[
\boxed{
\frac{1+\varepsilon_L}{2}.
}
\]

Perfect conditional next-bit balance corresponds to `epsilon_L=0`.

## 3. Exact active-transition table

The exact `A_30` calculation gives

\[
\boxed{
\begin{array}{c|r|r|r|r|c|c}
L&C_L&C_{L+1}&M_D(L)&K_L&\eta_L&\varepsilon_L\\\hline
4&805306368&536862784&536887296&128&0.6666870& 2.3841\times10^{-7}\\
6&536862784&436199473&201326620&-2&0.3750057&-9.9341\times10^{-9}\\
7&436199473&318759965&234879010&-6&0.5384670&-2.5545\times10^{-8}\\
9&318759965&268429113&100661783&79&0.3157918& 7.8481\times10^{-7}\\
11&268429113&236972326&62913083&-491&0.2343750&-7.8044\times10^{-6}\\
12&236972326&192409280&89126073&-19&0.3761033&-2.1318\times10^{-7}\\
14&192409280&169732552&45349421&-4035&0.2356925&-8.8976\times10^{-5}\\
15&169732552&138537664&62388740&-1036&0.3675709&-1.6606\times10^{-5}\\
17&138537664&122792235&31489378&-1480&0.2272983&-4.7000\times10^{-5}
\end{array}
}
\]

The plateau transitions

\[
L=5,8,10,13,16,18
\]

have

\[
M_D(L)=0
\]

because `a_(L+1)=a_L`.

## 4. Main observation

Across every active transition above, the signed conditional imbalance is tiny:

\[
\boxed{
|\varepsilon_L|<9\times10^{-5}.
}
\]

Thus, within the one-child coefficient-boundary parents, the ternary `A_30` mass is retained almost exactly at the ideal balanced rate

\[
\boxed{1/2.}
\]

The final active transition in the current public class range is especially illustrative:

\[
M_D(17)=31,489,378,
\]

but

\[
K_{17}=-1,480.
\]

Hence

\[
\boxed{
\varepsilon_{17}\approx-4.70\times10^{-5}.
}
\]

The global forward-class survivor count

\[
C_{18}=122,792,235
\]

is exactly the `A_30` forward-class fringe already certified in the bootstrap calculation.

## 5. Why this matters

The fixed-resolution mixing theorem only establishes unconditional equidistribution after many free ternary selectors.

The present calculation tests the stronger quantity actually needed by the growing-resolution transport theorem:

\[
\boxed{
\text{next binary bit of the ternary subset sum}
\mid
\text{already inside a dangerous coefficient parent}.
}
\]

The observed balance is therefore not merely a restatement of the overall residue histogram. It says that conditioning on the rare dynamical boundary has not produced a visible alignment with the surviving child direction at these resolutions.

## 6. Candidate theorem suggested by the data

A reusable growing-resolution theorem would follow from a bound of the form

\[
\boxed{
\left|
\sum_{r\in D_L}v(r)u(r)
\right|
\le\epsilon_L
\sum_{r\in D_L}c(r),
}
\]

with

\[
\epsilon_L\le1-2\delta
\]

for some fixed `delta>0` over a sufficiently long growing range, together with a lower bound on the cumulative one-child mass fractions `eta_L`.

The finite data are consistent with the much stronger heuristic regime

\[
\epsilon_L\approx0,
\]

but no asymptotic claim is made here.

## 7. Structural interpretation

This table separates three facts that had previously been mixed together:

1. the Beatty/Sturmian coefficient threshold decides **when** a pruning bit is required;
2. the one-child mass `eta_L` says **how much** current survivor mass lies on that dynamical boundary;
3. the cross-correlation `epsilon_L` says whether the ternary formation channel can systematically choose the unique surviving child.

Only item 3 is a genuinely cross-base obstruction.

The numerical near-zero values indicate that this is the right quantity to attack analytically rather than further scalar defect-density refinements.

## 8. Reproducibility

Exact verifier:

`collatz/src/m44_low30_coefficient_transport_certificate.cpp`

All counts are integer identities; the displayed decimal ratios are derived from those integers only.
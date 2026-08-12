# Coefficient-excess Sturmian transfer cocycle

Date: 2026-08-12

Status: **exact combinatorial reformulation** of the pure coefficient-survivor tree. The dynamical one-child mass is encoded by a one-dimensional half-line transfer cocycle driven by the Sturmian/Beatty increment word of `log_3 2`. This isolates the purely dynamical estimate needed by the growing-resolution transport theorem. This does not prove a uniform lower bound on the boundary fraction.

## 1. Coefficient barrier and excess

Put

\[
\beta:=\log_3 2,
\qquad
a_k:=\lceil k\beta\rceil.
\]

A length-`k` parity word survives the multiplicative coefficient barrier exactly when

\[
q_j\ge a_j
\qquad(1\le j\le k),
\]

where `q_j` is the cumulative number of odd steps.

At time `k` define the nonnegative excess

\[
\boxed{r:=q_k-a_k\ge0.}
\]

Let

\[
\boxed{
g_{k,r}}
\]

be the number of coefficient-surviving length-`k` parity words with excess `r`.

Let

\[
S_k:=\sum_{r\ge0}g_{k,r}
\]

be the total number of survivor parity words.

## 2. Sturmian boundary increment

Since `0<beta<1`,

\[
s_k:=a_{k+1}-a_k\in\{0,1\}.
\]

The binary sequence `(s_k)` is the mechanical/Sturmian increment word of slope `beta`.

There are therefore only two transfer operators.

## 3. Plateau operator

If

\[
s_k=0,
\]

the boundary does not rise.

From an old excess `r`:

- an even parity step leaves the excess `r`;
- an odd parity step raises it to `r+1`.

Hence, with `g_{k,-1}:=0`,

\[
\boxed{
g_{k+1,r}=g_{k,r}+g_{k,r-1}.}
\]

Define

\[
\boxed{(Pg)_r:=g_r+g_{r-1}.}
\]

Every parent has two surviving children, so

\[
\boxed{S_{k+1}=2S_k.}
\]

## 4. Rise operator

If

\[
s_k=1,
\]

the coefficient boundary rises by one.

From old excess `r`:

- an odd step increases `q` by one and therefore keeps the new excess equal to `r`;
- an even step leaves `q` fixed and lowers the new excess to `r-1`.

The even child of an old boundary state `r=0` is rejected.

Thus

\[
\boxed{
g_{k+1,r}=g_{k,r}+g_{k,r+1}.}
\]

Define

\[
\boxed{(Rg)_r:=g_r+g_{r+1}.}
\]

The total count satisfies

\[
\boxed{S_{k+1}=2S_k-g_{k,0}.}
\]

## 5. Exact one-child mass fraction

At a rise step the one-child parents are **exactly** the excess-zero boundary states.

Under the uniform dyadic parity-cylinder counting measure, their fraction among all current survivors is therefore

\[
\boxed{
\eta_k^{\rm dyn}:=rac{g_{k,0}}{S_k}.
}
\]

The pure coefficient-survivor contraction at that bit is

\[
\boxed{
\frac{S_{k+1}}{2S_k}
=1-\frac12\eta_k^{\rm dyn}.
}
\]

Thus the dynamical quantity called `eta` in the child-transport theorem has a completely explicit half-line combinatorial origin.

## 6. Generating-function form

Let

\[
G_k(z):=\sum_{r\ge0}g_{k,r}z^r.
\]

At a plateau,

\[
\boxed{G_{k+1}(z)=(1+z)G_k(z).}
\]

At a rise,

\[
\boxed{
G_{k+1}(z)
=(1+z^{-1})G_k(z)-z^{-1}g_{k,0}.
}
\]

The boundary subtraction is the only non-translation-invariant term.

Hence the entire coefficient-survivor tree is a positive operator cocycle on the half-line driven by one Sturmian word.

## 7. Separation from the ternary formation channel

For the actual ternary representative measure, the one-child **mass** need not equal the uniform dyadic count fraction `g_(k,0)/S_k` exactly.

However the roles are now cleanly separated:

1. `g_(k,0)/S_k` describes how large the one-child boundary is in the dyadic survivor language;
2. the ternary subset-sum distribution describes how much representative mass lands on that boundary;
3. `U_j(d)` bounds how unevenly that mass can choose the two child lifts.

The child-transport identity combines these only at the final step.

## 8. Finite diagnostic behavior

Exact dynamic programming of the cocycle shows that the boundary fraction at active rise steps remains visibly positive over long finite ranges. For example, through several hundred steps it is typically of order `10^-1`, with finite minima near `8*10^-2` in the first few hundred steps.

These values are diagnostic only and are **not** promoted to an asymptotic lower bound here.

The theorem target is now precise:

> prove an effective lower bound, or a sufficiently strong cumulative lower bound, for `g_(k,0)/S_k` along the Sturmian rise times.

A cumulative estimate is enough; a pointwise positive constant is not logically necessary.

## 9. Possible analytic routes

The reformulation exposes several standard tools that were obscured in the original Collatz notation:

- positive-operator cocycles;
- generating functions on the half-line;
- large-deviation / ballot-path estimates;
- renewal theory for a negative-drift walk conditioned to remain above a moving irrational boundary;
- transfer-matrix bounds grouped over continued-fraction/Sturmian blocks.

Any theorem obtained here is independent of the ternary recursive-sufficiency construction and can then be coupled to the formation imbalance theorem as a separate channel.
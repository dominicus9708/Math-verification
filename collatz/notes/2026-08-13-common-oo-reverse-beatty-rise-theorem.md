# Common-OO reverse-preimage Beatty-rise theorem

Date: 2026-08-13

Status: **exact structural theorem + exact finite depth-23 certificate**.  This concerns the aligned 3-adic alternate-preimage sieve inside the recursively sufficient ternary core.  It is not a proof of Collatz.

## 1. Common-OO reverse contraction budget

For a core start

\[
n=4S+3,
\]

the universal two-step descendant is

\[
y=T^2(n)=9S+8.
\]

Consider an alternate reverse path from `y` with total reverse odd count `q=d+2` and total extra inverse-even doublings `E`.

Its multiplicative factor relative to the original `n` is

\[
\lambda=\frac{2^{d+E}}{3^d}.
\]

Hence strict multiplicative contraction occurs exactly when

\[
2^{d+E}<3^d.
\]

Put

\[
\alpha=\log_2(3/2).
\]

Since `alpha` is irrational, the largest allowed integer `E` is exactly

\[
\boxed{B(d)=\lfloor d\alpha\rfloor.}
\]

Thus the reverse contraction budget is the same Beatty clock that appears in the odd-only mechanical/skew formulation.

## 2. Plateau theorem

Suppose

\[
\boxed{B(d)=B(d-1).}
\]

Then no prefix-minimal forbidden ternary cylinder can first appear at depth `d`.

### Proof

Assume a valid reverse path first gives a contracted alternate ancestor after `q=d+2` reverse odd steps.  Let `E_d` be its accumulated extra-doubling count.  Contraction gives

\[
E_d\le B(d).
\]

Truncate the final reverse-odd step of this path.  The resulting valid reverse prefix has `q-1=d+1` reverse odd steps and accumulated extra-doubling count `E_{d-1}` satisfying

\[
E_{d-1}\le E_d.
\]

On a budget plateau,

\[
E_{d-1}\le E_d\le B(d)=B(d-1).
\]

Therefore the truncated reverse path already satisfies

\[
2^{(d-1)+E_{d-1}}<3^{d-1},
\]

so the parent ternary prefix of depth `d-1` was already forbidden.  Hence the depth-`d` cylinder cannot be prefix-minimal.  QED.

For the current minimal-counterexample search the additive constant is harmless because all starts lie far above the finite threshold required in the common-OO alternate-preimage lemma.  The theorem above is fundamentally about the multiplicative/preimage budget; recursive elimination inherits the previously audited additive threshold.

## 3. Consequence: births occur only on Beatty rises

New prefix-minimal forbidden cylinders may occur only when

\[
\boxed{B(d)-B(d-1)=1.}
\]

Equivalently, the possible birth depths are the rises of

\[
\lfloor d\log_2(3/2)\rfloor.
\]

This removes every plateau depth from the reverse-sieve search before any 3-adic state calculation is performed.

## 4. Exact depth-23 extension

An OpenMP exact-integer verifier extends the common-OO alternate-preimage sieve to ternary depth 23.  The prefix-minimal forbidden-cylinder counts are

\[
\boxed{
\begin{array}{c|r}
d&\text{new minimal forbidden cylinders}\\\hline
7&2\\
9&2\\
11&5\\
12&24\\
14&42\\
16&104\\
18&224\\
19&802\\
21&1789\\
23&4296
\end{array}}
\]

There are no new minimal cylinders at the intervening depths through 23, exactly as forced by the plateau theorem.

At depth 23 the total number of removed 0/1 ternary cylinders is

\[
\boxed{299740}
\]

out of

\[
2^{23}=8388608,
\]

so the exact removed fraction is

\[
\boxed{
\frac{299740}{8388608}
=0.035731792449951171875.
}
\]

Thus the finite removed fraction rises from `3.28369140625%` at depth 18 and `3.4366607666%` at depth 20 to about `3.57318%` at depth 23.

## 5. Interpretation

The important result is not the modest percentage increase.  It is the synchronization

\[
\boxed{
\text{forward odd-only mechanical clock}
=\text{reverse 3-adic contraction-budget clock}
=\lfloor d\log_2(3/2)\rfloor.
}
\]

The same irrational rotation therefore controls:

1. Christoffel/mechanical displacement on the first-crossing side;
2. the number of extra inverse-even steps affordable by a smaller alternate ancestor on the 3-adic side.

This supplies a genuine common index for the two channels rather than merely comparing unrelated densities.

## 6. Limitation

The new forbidden-cylinder measure is still small and the data do not prove that the surviving ternary prefix tree has entropy strictly below one bit per trit.  In fact the decreasing incremental forbidden measure makes such a conclusion unsafe without an additional theorem.

Therefore the common-OO reverse sieve should be used as a synchronized arithmetic filter inside the dyadic late-lift / first-crossing analysis, not as a stand-alone entropy proof.

## 7. Verification

`collatz/src/common_oo_reverse_sieve_depth23.cpp` uses only exact integer arithmetic.  It checks the expected minimal-cylinder counts through depth 23, the total removed count `299740`, and that every observed new minimal depth lies on an exact contraction-budget rise.

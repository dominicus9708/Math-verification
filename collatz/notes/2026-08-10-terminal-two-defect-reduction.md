# Terminal two-defect reduction in the `1000` branch

Date: 2026-08-10

Status: **DERIVED FINITE EXCLUSIONS + ONE REMAINING TWO-AMPLITUDE CONGRUENCE**

This note continues `terminal-single-defect-exclusion.md` at the isolated resonance

\[
(q,\sigma)=(137,528,045,312,217,976,794,617).
\]

It concerns only the strongest `m=46`, high-four-trit `1000` branch.

## 1. Starting point

The previous certificate proves that among the final 20 odd-position coordinates there must be at least two defects.

Assume here that there are exactly two.

## 2. Two locally born terminal defects

First suppose the first of the final 20 coordinates has `z=0`, so both defects are born inside the remaining 19-coordinate window.

A new defect can begin from zero only across a mechanical gap of two, with initial amplitude `1`.  If the two defects are separated by at least one zero coordinate, both amplitudes are therefore `1`.  If they are adjacent, the second amplitude is restricted by the one-step transition and can only be `1` or `2` as allowed by the local mechanical gap.

There are exactly 65 such finite patterns.

Exact evaluation of the full terminal `3^48` endpoint for all 65 patterns shows that none lies in the branch near-return set

\[
\{y:\exists x\in\mathcal C_{1000},\;0\le y-x\le29,785,654\}.
\]

Hence two defects born wholly inside the terminal window are impossible.

## 3. First inherited defect, second separated isolated defect

Now let the first terminal coordinate carry an inherited amplitude `z>=1`, let at least one zero coordinate follow, and let the second defect be a later isolated defect.

The later defect must have amplitude `1` and can occur only at a mechanical gap of two.  There are 11 nominal positions.  Two of them are eliminated immediately by the lower-`3^19` near-return congruence, leaving nine one-parameter amplitude scans.

For each remaining position:

- `y mod 3^19` is fixed;
- the lower 19 ternary choices and their carry classes are finite and exact;
- the inherited amplitude satisfies
  \[
  1\le z\le167,265,511;
  \]
- the upper 21 ternary digits reduce to a Cantor-membership test.

The nine exact amplitude scans produce 64 modular/Cantor hits in total.

Instead of relying only on correction-budget pruning, every ordinary start represented by all 64 hits was reconstructed.  This gives exactly

\[
\boxed{1,113,680}
\]

distinct ordinary positive integers in the `1000` branch.

Their accelerated coefficient stopping times were computed exactly.  The maximum is

\[
\boxed{\max\tau_c=292.}
\]

Therefore none can realize the target first crossing

\[
\sigma=217,976,794,617.
\]

So the inherited-first / separated-second two-defect case is completely eliminated by ordinary-integer realization.

## 4. Only remaining exactly-two-defect geometry

The only remaining case with exactly two terminal defects is therefore an adjacent pair at the first two positions of the final-20 window:

\[
\boxed{(z_0,z_1)=(z,w),\qquad1\le w\le z.}
\]

The local mechanical gaps satisfy

\[
\kappa_{q-19}-\kappa_{q-20}=1,
\]

so the transition indeed gives `w<=z`.

All later 18 terminal coordinates are mechanical.

## 5. Lower `3^18` collapse

Both changed correction terms are multiples of `3^18`, so

\[
y\bmod3^{18}=350,996,365
\]

is fixed.

The near-return condition leaves exactly

\[
\boxed{13,824}
\]

choices among the lower 18 ternary `0/1` digits, and all of them lie in the same high-quotient carry class

\[
\boxed{h=1.}
\]

Thus the lower 18 ternary coordinates disappear from the remaining high-quotient equation except for this fixed carry.

## 6. Exact adjacent-pair congruence

Let

\[
M_{30}=3^{30}=205,891,132,094,649.
\]

At the first two terminal odd positions, the mechanical exponents differ by one.  Define the exact unit

\[
\boxed{
G=2^{\kappa_{q-20}-\sigma}\pmod{3^{30}}
=120,123,938,613,220.
}
\]

After subtracting the mechanical terminal endpoint and dividing the two changed terms by `3^18`, the adjacent amplitudes contribute

\[
\boxed{
G\left(3\,2^{-z}+2\,2^{-w}-5\right)
\pmod{3^{30}}.
}
\]

Let the remaining upper 22 ternary digits be

\[
S_{22}=\sum_{i=0}^{21}a_i3^i,
\qquad a_i\in\{0,1\}.
\]

The fixed start/endpoint constants reduce the target to

\[
\boxed{
G\left(3\,2^{-z}+2\,2^{-w}-5\right)
\equiv
4S_{22}+K
\pmod{3^{30}},
}
\]

with

\[
\boxed{K=197,151,077,055,918.}
\]

The remaining exactly-two-terminal-defect problem is therefore the bounded exponential-sum/Cantor congruence

\[
\boxed{
\begin{aligned}
&G(3\,2^{-z}+2\,2^{-w}-5)
\equiv4S_{22}+K\pmod{3^{30}},\\
&1\le w\le z\le167,265,511,\\
&S_{22}\in\mathcal C_{22}.
\end{aligned}
}
\]

This is substantially smaller than a raw two-dimensional scan over the original Collatz path, but it is still a genuine two-variable bounded exponential congruence.

## 7. Proof-program consequence

At terminal defect count two, every easy/local configuration has been eliminated.  The remaining obstruction is exactly one inherited adjacent defect run whose first two terminal amplitudes are `(z,w)`.

A useful next theorem or algorithm should exploit one of:

1. bounded discrete logarithms in the cyclic unit group modulo `3^30`;
2. meet-in-the-middle on the 22-bit Cantor target;
3. a correction-budget restriction coupling `z,w` to the run-level cost;
4. direct ordinary-integer reconstruction after reducing the exponential congruence to a small hit list.

Flat enumeration of all `(z,w)` is not an appropriate next step.
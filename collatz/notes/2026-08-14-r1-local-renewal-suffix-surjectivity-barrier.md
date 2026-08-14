# R1 local renewal-suffix surjectivity barrier

Date: 2026-08-14

Status: **exact local dynamical surjectivity / proof-strategy limitation**. It strengthens the earlier record-only suffix-address result: every finite 3-adic unit endpoint residue admits an actual positive odd-only suffix which is locally compatible not only with the R1 coefficient-record inequalities but also with the renewal-minimum condition. Therefore no bounded final-suffix filter using only local positivity, integrality, record, and minimum information can make the endpoint-residue family sparse. This does not construct a global Collatz counterexample.

## 1. Reverse odd step

For an odd endpoint state `y`, a reverse odd step with valuation `v>=1` is

\[
\boxed{
x=\frac{2^v y-1}{3}.}
\]

Integrality requires

\[
2^v y\equiv1\pmod3.
\]

For a 3-adic unit `y`, this fixes the parity of `v`.

Among the three exponents of that parity in `{1,2,3,4,5,6}`, exactly one exponent class modulo six satisfies the stronger congruence

\[
2^v y\equiv1\pmod9,
\]

which would make the predecessor divisible by three.

Choose instead the larger of the other two exponents. Then

\[
\boxed{3\le v\le6}
\]

and the new predecessor `x` is again a 3-adic unit.

## 2. Strict local height above the endpoint

Because the chosen valuation always satisfies `v>=3`, for every positive odd `y`,

\[
\boxed{
x=\frac{2^v y-1}{3}\ge\frac{8y-1}{3}>y.}
\]

Therefore iteration of the reverse construction produces

\[
\boxed{
x_0>x_1>\cdots>x_Q=Y}
\]

for any requested finite odd depth `Q`.

Equivalently, in the forward odd-only direction the constructed suffix is strictly decreasing toward its endpoint `Y`, but every earlier state in the suffix remains strictly above `Y`.

If `Y=N+g` is a renewal endpoint with `g>0`, then

\[
Y>N,
\]

so every state in this constructed final suffix is automatically above the original renewal floor `N`.

Thus the suffix satisfies the local renewal-minimum requirement exactly.

## 3. R1 record condition is also automatic

Let `S_j` be the accumulated binary valuation over the final `j` odd steps. Since every chosen valuation is at least three,

\[
\boxed{S_j\ge3j.}
\]

For the current R1 first-crossing pair, the backward record lower envelope `m_j` satisfies

\[
m_j\le2j+1\le3j.
\]

Hence

\[
\boxed{S_j\ge m_j}
\]

for every prefix of the constructed backward suffix.

So the same construction simultaneously satisfies

1. exact integer odd-only dynamics;
2. positivity;
3. preservation of 3-adic units;
4. the R1 backward coefficient-record inequalities;
5. the local renewal-minimum condition above `N`.

## 4. Arbitrary finite endpoint residue

Fix any finite depth `Q` and any unit residue

\[
Y\in(\mathbb Z/3^Q\mathbb Z)^\times.
\]

Starting from `Y` and applying the rule of Section 1 exactly `Q` times constructs a valid final-Q valuation suffix realizing that endpoint residue while satisfying all five local conditions above.

Therefore

\[
\boxed{
\text{the locally renewal-admissible endpoint-residue family mod }3^Q
\text{ is the full unit group for every finite }Q.
}
\]

This is stronger than record-only surjectivity.

## 5. Consequence for the gap44 mixed-fibre theorem

The gap44 theorem plus depth-27/28 Hensel correlation makes **one fixed final-44 suffix fibre** extremely small on the m44 selector core.

However the present theorem shows that the missing globalization cannot be obtained by making the bounded suffix test locally more faithful. Even the exact local dynamics and renewal-minimum condition still allow every unit endpoint residue.

Thus the obstruction is genuinely nonlocal:

\[
\boxed{
\text{bounded final suffix data}
\not\Rightarrow
\text{sparse endpoint-address family}.
}
\]

A terminal R1 state must preserve information coupling the suffix to the earlier part of the **same** orbit, such as

- the strengthened dyadic start/renewal address;
- accumulated skew/defect cost over growing scales;
- a same-integer canonical-lift condition;
- or an equivalent prefix--suffix direct-sum constraint.

This theorem justifies stopping further refinement of bounded suffix-only grammars or fixed-depth endpoint-residue sieves.

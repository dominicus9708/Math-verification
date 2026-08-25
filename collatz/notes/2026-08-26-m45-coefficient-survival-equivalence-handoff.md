# m=45 no-descent / coefficient-survival equivalence handoff

Date: 2026-08-26

Status: **exact finite equivalence through H=301,993, obtained by combining the existing coherent-ballot certificate with the positive affine correction.** This is a finite m=45 theorem, not a proof of the Collatz conjecture.

## 1. Existing certified direction

For the current m=45 recursively sufficient layer,

\[
N=4\left(3^{45}+\sum_{i=0}^{44}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

all starts satisfy

\[
N\ge4\cdot3^{45}+3.
\]

The exact coherent-ballot certificate proves through

\[
H\le301,993
\]

that coherent no-descent implies coefficient survival at every prefix:

\[
\boxed{
T^j(N)\ge N\ \forall j\le H
\Longrightarrow
3^{q_j}\ge2^j\ \forall j\le H.
}
\]

The certificate is

`collatz/src/m45_coherent_ballot_equivalence_depth301993_certificate.cpp`.

## 2. Converse is immediate

For every parity prefix,

\[
2^jT^j(N)=3^{q_j}N+R_j,
\]

where the affine correction satisfies

\[
R_j\ge0.
\]

Therefore if

\[
3^{q_j}\ge2^j,
\]

then

\[
T^j(N)
=\frac{3^{q_j}N+R_j}{2^j}
\ge N.
\]

Applying this at every prefix gives

\[
\boxed{
3^{q_j}\ge2^j\ \forall j\le H
\Longrightarrow
T^j(N)\ge N\ \forall j\le H.
}
\]

## 3. Exact equivalence for the current finite layer

Combining both directions,

\[
\boxed{
T^j(N)\ge N\ \forall j\le H
\iff
3^{q_j}\ge2^j\ \forall j\le H,
\qquad H\le301,993,
}
\]

for every current m=45 selector start.

Thus, inside this certified range, the finite m=45 no-descent problem is exactly a **same-integer ballot/coefficient-survival problem**. The additive correction no longer needs to be represented in the SAT search.

## 4. Computational consequence

The older direct Z3 encoding imposed the large unsigned constraints

\[
T^j(N)\ge N
\]

at every step. Those comparisons are unnecessary for m=45 through the certified horizon.

The exact replacement is:

1. build the 45-bit ternary selector integer;
2. follow only its deterministic parity evolution;
3. at each Beatty rise require the prefix odd count to satisfy
   \[
   q_j\ge\lceil j\log_3 2\rceil.
   \]

Because the required count is constant between Beatty rises while q_j is nondecreasing, constraints need only be inserted at the rises.

The corresponding solver is

`collatz/src/m45_coefficient_survival_z3.py`.

## 5. Relation to the Stage-4 handoff

This equivalence sharpens the post-address program.

At binary address exposure, K_addr(45)=74, the remaining fixed-layer task does not require estimating the additive correction or separately testing no-descent. One only needs to determine which ternary selector integers realize a coefficient-surviving binary address through the desired horizon.

Stage-4 L7/L14 and first-defect filters remain useful as **additional necessary minimal-counterexample filters**, but they are no longer needed to make no-descent itself mathematically testable.

Accordingly there are now two nested finite searches:

- **unconditional m45 finite search:** selector + exact coefficient survival;
- **minimal-counterexample-pruned search:** the same search plus the already justified Stage-4 maximality / first-defect conditions.

UNSAT in the unconditional search is strictly stronger. SAT only supplies a finite surviving witness and does not prove anything asymptotic.

# MATH-231 — relative-debt formulation of the r=10 layer

Date: 2026-09-19

Status: EXACT LOCAL BELLMAN FORMULATION / NO 89-RESET / r=10 OPEN

## 1. Why a relative formulation is required

The MATH-060 additive constant 89 belongs to the complete synchronized first-cell path and cannot be restarted at an interior r=10 boundary.

Therefore r=10 must be closed as a local composable segment:

either the segment reaches a certified descent terminal, or its total resolution-adjusted reduced cost is nonnegative.

Such a local statement composes with any inherited global Bellman value.

## 2. Initial r=10 debt

For one completed r=10 factor let

w_0 = P_10 - lambda H

be its raw local reduced cost, with lambda=19/503.

For the frozen negative-candidate source, w_0<0.

Define the exact initial debt

boxed: D_0 = -w_0 = lambda H - P_10 > 0.

Writing H=L+h_10 and

epsilon_10 = P_10 - lambda h_10,

gives

boxed: D_0 = lambda L - epsilon_10.

MATH-202 supplies the phase-uniform bound

epsilon_10 >= underline_epsilon_10

with

underline_epsilon_10 / lambda = 45390185 / 3545856 = 12.8009... .

Hence

boxed: D_0 <= lambda L - underline_epsilon_10 < lambda(L-12).

Since L<=72, every frozen r=10 local debt is finite and uniformly bounded.

## 3. Repayment credit

After the initial r=10 factor, let each later exact boundary transition have the MATH-074/197 resolution-adjusted reduced cost

w_i = p_i - lambda ell_i + lambda(R_(i-1)-R_i).

Define accumulated repayment credit

boxed: K_n = sum_{i=1}^n w_i.

No global additive constant appears.

If

K_n >= D_0,

then

w_0 + K_n >= 0.

So the whole segment from the r=10 entry through transition n is Bellman-nonnegative and can be contracted into the global proof state without any terminal descent certificate.

## 4. SAFE-prefix form

While every intervening edge is SAFE in the MATH-229 sense, w_i>=0 and therefore K_n is monotone nondecreasing.

The only unresolved event before repayment is:

a first edge with w_i<0 while K_(i-1)<D_0.

That edge is exactly where the MATH-192/193 singleton danger corridor and MATH-202 paid-count threshold must be applied.

Thus the r=10 layer closure target is

boxed:
initial r=10 debt
 -> SAFE*
 -> either repayment K>=D_0, or a terminally closed first negative edge.

## 5. Relation to existing branch closures

- MATH-221 closes regenerated r=10 zero carry.
- MATH-224 closes the high-L singleton paid-exit shell.
- MATH-226 closes every immediate next dangerous low-paid successor r=2..10 from the frozen r=10 output.
- MATH-229 supplies exact SAFE-prefix composition for the non-immediate case.

The remaining gap is therefore not a new r/depth grid. It is the reachability of an unpaid first-negative state under the common transducer.

## 6. Exact terminal predicate

At the first unpaid negative edge, MATH-193 gives the exact corridor

r_R < M,
r_R <= r_bad,
nu_2(C_R) >= z.

MATH-202 strengthens the last condition to

z >= z_min(r)

for the emitted paid tag r.

MATH-197 then supplies the synchronized integer terminal defect

J = C - N(2^k-3^q).

A state with J<0 is closed by strict self-descent.

Thus the exact surviving terminal kernel is

boxed:
K<D_0
 AND r_R<M
 AND r_R<=r_bad
 AND nu_2(C_R)>=z_min(r)
 AND J>=0.

## Claim boundary

Established:
- correct local debt/repayment formulation without reusing the global 89 allowance;
- exact debt identity D_0=lambda L-epsilon_10;
- safe-prefix repayment criterion K>=D_0;
- exact first-unpaid-negative terminal kernel.

Not established:
- emptiness of that kernel after arbitrary SAFE prefixes;
- full r=10 closure;
- first-cell emptiness;
- the Collatz conjecture.
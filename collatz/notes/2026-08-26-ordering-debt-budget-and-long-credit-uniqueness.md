# First resonance: ordering debt, displacement cap, and long-credit uniqueness

Date: 2026-08-26

Status: **exact structural theorem** inside the repaired first-global-resonance branch.  It does not prove the Collatz conjecture.

## 1. DSD state split

At the current proof frontier, a terminal reconstruction state has three logically distinct components:

1. **Hensel alignment state** — how many future mechanical ternary digits currently match;
2. **ordering debt** — the current displacement `p` from the mechanical odd position;
3. **correction cost** — the accumulated normalized defect.

The previous alignment-credit theorem controlled item 1.  This note controls item 2 and transfers it into item 3.

## 2. Global geometric displacement cap

For odd ordinal `j`, let

\[
b_j=\lfloor(j-1)\log_2 3\rfloor
\]

be the mechanical position and `a_j` the actual odd position.  Since actual odd positions are strictly increasing,

\[
a_j\ge j-1.
\]

Thus the displacement

\[
d_j=b_j-a_j
\]

obeys

\[
0\le d_j\le b_j-(j-1).
\]

Throughout the first Farey cell,

\[
b_j=\left\lfloor\frac{(j-1)A}{Q}\right\rfloor,
\qquad
A=Q+P,
\]

with

\[
P=42150895613,
\qquad
Q=72057431991.
\]

Therefore

\[
d_j\le\left\lfloor\frac{(j-1)P}{Q}\right\rfloor\le P-1,
\]

so

\[
\boxed{d_j\le42150895612.}
\]

## 3. Ordering debt can decay only across gap-2 steps

When reconstructing one earlier odd ordinal, let the old earliest displacement be `p`, the new displacement be `d`, and the mechanical gap be

\[
g\in\{1,2\}.
\]

Strict ordering of the actual odd positions gives

\[
\boxed{d\ge p-g+1.}
\]

Hence:

- if `g=1`, the displacement cannot decrease;
- if `g=2`, it can decrease by at most one.

At the start boundary, the first odd ordinal is at position zero and its mechanical position is also zero.  Therefore the final displacement debt is exactly zero.  Any positive displacement introduced anywhere in the terminal reconstruction must consequently be fully repaid before the start boundary.

## 4. Christoffel balance gives a repayment-time lower bound

The mechanical gap-2 indicator is the anchored lower Christoffel word

\[
m_n=
\left\lfloor\frac{(n+1)P}{Q}\right\rfloor
-
\left\lfloor\frac{nP}{Q}\right\rfloor.
\]

Any `h` consecutive letters contain at most

\[
\left\lceil\frac{hP}{Q}\right\rceil
\]

gap-2 symbols.

If the current displacement is `D`, returning to zero requires at least `D` one-unit decreases and therefore at least `D` gap-2 symbols.  Thus the positive-debt interval has length at least

\[
\boxed{
h(D)=
\left\lfloor\frac{(D-1)Q}{P}\right\rfloor+1.}
\]

## 5. Debt implies correction cost

At an odd ordinal whose displacement is `r>=1`, the exact normalized correction loss is

\[
2c_j(1-2^{-r}),
\qquad
c_j=\frac{2^{b_j-1}}{3^j}.
\]

Since

\[
c_j>\frac1{12},
\]

each such position costs strictly more than

\[
\frac16(1-2^{-r}).
\]

To lower-bound the cheapest possible repayment path from `D` to zero:

- the positive levels `D,D-1,...,1` must each occur at least once;
- any additional positive-debt positions cost at least the `r=1` amount.

Therefore

\[
\boxed{
\frac{E}{3^Q}
>
\frac{h(D)+D-2+2^{1-D}}{12}.}
\]

This inequality is independent of the Hensel steering choices.  It follows only from ordering, Christoffel balance, and the correction functional.

## 6. Exact first-resonance displacement cap

The previously certified total defect budget is

\[
\frac{E}{3^Q}<4314000000.
\]

The first integer `D` for which the debt lower bound already exceeds this entire budget is

\[
\boxed{D=19106028519.}
\]

Indeed

\[
h(D)=32661971485
\]

and

\[
h(D)+D-2=51768000002>12\cdot4314000000.
\]

Hence every surviving first-resonance path must satisfy

\[
\boxed{
\max_j d_j\le19106028518.}
\]

This improves the purely geometric cap `P-1=42150895612` by more than a factor of two.

## 7. Consequence for alignment-credit repairs

The alignment-credit theorem proved that buying `L` future mechanical ternary digits by a repair determines one odd displacement class

\[
d\pmod{2\cdot3^L}.
\]

Now

\[
2\cdot3^{20}=6973568802,
\]

but

\[
\boxed{
2\cdot3^{21}=20920706406
>
19106028518.}
\]

Therefore, inside the entire budget-feasible first-resonance state space,

\[
\boxed{
L\ge21
\quad\Longrightarrow\quad
\text{at most one ordinary displacement }d
\text{ can realize that repair class}.}
\]

So long-credit repairs do not form a many-valued branch.  All genuine branching caused by multiple ordinary representatives of the same repair residue is confined to alignment purchases of at most 20 ternary digits.

This does **not** yet prove that a long-credit repair exists or is impossible.  It proves that if one exists, it is a unique exceptional control at that state.

## 8. DSD proof-chain consequence

The repaired finite-crossing state now separates into

\[
\boxed{
\text{short-credit control }(L\le20)
\quad\text{or}\quad
\text{unique exceptional long-credit control }(L\ge21).
}
\]

Together with the symmetric boundary credits

\[
\mathfrak a_{\rm start},\mathfrak a_{\rm end}\le44,
\]

this suggests a finite-branch Bellman decomposition:

1. short-credit transitions have bounded memory depth;
2. every long-credit transition is deterministic once its state is fixed;
3. ordering debt supplies a state potential whose cost cannot be discarded at block boundaries.

The next target is to turn this dichotomy into a block potential on the 138-node Christoffel DAG.

Companion exact certificate:

`collatz/src/first_resonance_ordering_debt_budget_certificate.py`.

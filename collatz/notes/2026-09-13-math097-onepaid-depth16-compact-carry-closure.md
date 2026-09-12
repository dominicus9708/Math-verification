# MATH-097 — one-paid macro depth 16 closed by compact carry/address state

Date: 2026-09-13

Status: `EXACT FINITE t=16 BELLMAN CLOSURE / ONE-PAID FRONTIER 7<=t<=15`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This is a Bellman/reduced-cost closure for singleton handoffs at macro depth 16, not an ordinary descent theorem.

## 1. Compact state

MATH-096 permits each multi-source state to replace the full large integer pair `(B,Q)` by

\[
R=\lceil\log_2M\rceil,
\qquad P=73+R,
\]

\[
X=3^{-Q}B\pmod{2^P},
\qquad
G=3^{-Q}\pmod{2^P}.
\]

The exact phase interval and total source-modulus depth `H` are retained.

For a multi edge of resolution `h`, MATH-092 propagates the state by low-bit selection and right shift; because `R'<=R-h`, the child still possesses its complete required precision `73+R'`.

## 2. Phase-danger corridor

The address-forgotten MATH-086 lower envelope is used only to build a safe backward corridor of phase states that can reach a negative depth-16 terminal crossing.

The corridor sizes from macro depths 1 through 15 are

\[
\boxed{
26,101,169,206,233,280,314,361,399,421,472,504,554,589,588.
}
\]

Address information is then restored.  Because the corridor was produced after forgetting address and retaining minimum penalty on each phase cell, it is a superset of every actual negative same-integer path.  Discarding states outside it is therefore safe.

## 3. Exact compact-state workload

After exact address restoration and identical compact-state deduplication, the state counts are

\[
\begin{array}{c|r}
t&\text{compact multi-source states}\\\hline
1&61\\
2&285\\
3&1,112\\
4&3,045\\
5&6,766\\
6&17,673\\
7&37,189\\
8&85,681\\
9&167,405\\
10&270,430\\
11&566,240\\
12&1,004,752\\
13&1,971,140\\
14&3,412,980\\
15&2,460,473
\end{array}
\]

No approximate address matching is used.

## 4. Universal depth-16 terminal filter

MATH-086 proves that every one-paid macro pays strictly more than `1/9`.  A 16-macro chain therefore has

\[
\mathcal P>\frac{16}{9}.
\]

With

\[
\lambda=\frac{19}{503}
\]

and terminal resolution overshoot

\[
z=h-R,
\]

a negative reduced-cost terminal would require

\[
\frac{16}{9}-\lambda z<0.
\]

Since

\[
47<\frac{16/9}{19/503}=\frac{8048}{171}<48,
\]

any actual danger must satisfy

\[
\boxed{z\ge48.}
\]

## 5. Exact address audit

Across all 2,460,473 terminal-parent compact states, every canonical edge satisfying both

- exact phase compatibility;
- `h-R>=48`

is tested by the exact normalized dyadic residue.

The finite totals are

\[
\boxed{45,094,414\text{ danger-edge attempts}.}
\]

The number satisfying the actual source-family condition `r<M` is

\[
\boxed{0}.
\]

Indeed the smallest observed residue gap is

\[
\boxed{r-M=197,239,627>0.}
\]

Thus every phase-compatible edge that could possibly defeat the universal penalty lower bound is excluded by exact same-integer address compatibility.

## 6. Verdict

Therefore

\[
\boxed{t=16\text{ is Bellman-safe}.}
\]

Together with the earlier exact closures, the unresolved detailed one-paid macro-depth band becomes

\[
\boxed{7\le t\le15.}
\]

This result does not assert ordinary descent for all terminal integers and does not close the first universal cell by itself.

## Reproducibility

`collatz/src/2026_09_13_math097_onepaid_depth16_compact_carry_closure.py`

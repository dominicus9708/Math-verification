# Rational ternary-prefix defect budgets with the run-average bound

Date: 2026-08-10

Status: **DERIVED RATIONAL COROLLARY / CERTIFIED INTEGER BOUNDS**

This note strengthens `2026-08-09-ternary-prefix-defect-budget.md` using the run-average theorem

\[
\Delta S\ge\frac5{48}N_{\rm def}.
\]

No new floating-point assumption is introduced.

## 1. Conversion of the earlier exact bounds

The earlier rational certificate gives, for every ternary prefix block `p`, a rational correction-loss allowance `A(p)` and the integer bound

\[
N_{\rm old}(p)=\lfloor12A(p)\rfloor.
\]

The run-average theorem gives instead

\[
N_{\rm def}(p)\le\frac{48}{5}A(p)=9.6A(p).
\]

Since

\[
12A(p)<N_{\rm old}(p)+1,
\]

we obtain using only the already-certified integer `N_old(p)`

\[
N_{\rm def}(p)
<\frac45\bigl(N_{\rm old}(p)+1\bigr).
\]

Thus the certified integer replacement is

\[
\boxed{
N_{\rm run}(p)
=\left\lceil\frac45(N_{\rm old}(p)+1)\right\rceil-1.
}
\]

This avoids recomputing logarithm intervals and preserves the exact-rational status of the upstream certificate.

## 2. Updated high-four-prefix table

At

\[
q=137,528,045,312,
\]

the nine rationally allowed high-four prefixes in the `m=46` block receive the following strengthened bounds.

| high free trits | old `N_def` bound | run-aware `N_def` bound | required cap-match fraction |
|---|---:|---:|---:|
| 0000 | 14,516,878,922 | 11,613,503,138 | >= 91.555538% |
| 0001 | 13,992,454,808 | 11,193,963,847 | >= 91.860596% |
| 0010 | 12,943,606,581 | 10,354,885,265 | >= 92.470710% |
| 0011 | 12,419,182,467 | 9,935,345,974 | >= 92.775767% |
| 0100 | 9,797,061,898 | 7,837,649,519 | >= 94.301054% |
| 0101 | 9,272,637,784 | 7,418,110,227 | >= 94.606111% |
| 0110 | 8,223,789,556 | 6,579,031,645 | >= 95.216225% |
| 0111 | 7,699,365,442 | 6,159,492,354 | >= 95.521283% |
| 1000 | 357,427,848 | 285,942,279 | >= 99.792084% |

All percentages are computed from the certified integer upper bound divided by the exact integer `q`.

## 3. Interpretation

The recursive-sufficiency ternary prefix now controls a monotone hierarchy:

\[
\boxed{
\text{larger ternary prefix}
\Rightarrow
\text{larger minimum start}
\Rightarrow
\text{smaller correction-loss budget}
\Rightarrow
\text{sparser admissible defect process}.
}
\]

The `1000` branch is especially rigid: fewer than about `0.208%` of its odd-position coordinates may depart from the mechanical cap.

This is still only an upper-channel constraint. A proof-level exclusion needs a lower requirement on the number or placement of defects / late lifts forced by an ordinary integer in the same ternary block.

## 4. Next target

The natural next certificate is a branch-dependent lower function

\[
L_{\rm def}(p,K)
\]

or an equivalent late-lift obstruction such that every ordinary integer in ternary prefix block `p` surviving to the target resonance must satisfy

\[
N_{\rm def}\ge L_{\rm def}(p,K).
\]

Any block with

\[
L_{\rm def}(p,K)>N_{\rm run}(p)
\]

would then be eliminated exactly.
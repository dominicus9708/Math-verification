# MATH-064 — exact closure of the r=22 multi-paid layer

Date: 2026-09-11
Status: `EXACT r=22 CLOSURE / SYMBOLIC MULTI-PAID RANGE REDUCED TO r<=21 / FIRST-CELL OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This closes one paid-count layer of the MATH-063 symbolic/singleton split.  It does not close `r<=21`.

## 1. Why r=22 is the next critical layer

MATH-063 shows that every multi-source multi-paid cylinder with

\[
r\ge23
\]

is already nonnegative for the target slope

\[
\lambda_* = \frac{19}{503},
\]

except that the `r=22` layer still lies below the universal phase-sum threshold.

Rather than generating all endpoint parity histories, MATH-064 applies information gates in the order required by DSD:

1. exact phase cell;
2. exact source-window resolution;
3. only then endpoint parity / slack structure;
4. finally direct ordinary-integer continuation for the few remaining negative cylinders.

## 2. Phase refinement and source-resolution gate

For each paid-exit source cylinder, refine its source phase interval by the next 22 exact Beatty/Sturmian phase thresholds.

This gives exactly

\[
\boxed{1192}
\]

nonempty source phase cells.

For a fixed refined cell, the 22 future phase increments are fixed, so the total completed-cluster length is fixed before endpoint parity is known:

\[
h_{\rm cl}=22+1+\sum_{j=0}^{21}\varepsilon_j.
\]

Let

\[
H=L+h_{\rm cl}
\]

be the full macro length including the preceding zero-cost segment.

The baseline paid-cluster penalty, obtained by taking every paid odd at the minimum slack `u=1`, is

\[
\mathcal P_{\rm base}
=
\frac16\sum_{j=0}^{21}\Omega_j.
\]

Two exact pre-gates are then applied.

### Gate A — phase cost already sufficient

If

\[
\mathcal P_{\rm base}
\ge
\frac{19}{503}H,
\]

then every actual slack schedule in the cell is safe, because larger slack only increases penalty.

This removes

\[
\boxed{433}
\]

phase cells.

### Gate B — completed parity cylinders are automatically singleton

A complete cluster parity word of length `h_cl` fixes the source lift `t` modulo

\[
2^{h_{\rm cl}}.
\]

If the entire allowed source-lift interval has width smaller than that modulus, no parity cylinder can contain two ordinary source anchors.

This removes another

\[
\boxed{752}
\]

phase cells from the symbolic graph.

Thus only

\[
\boxed{7}
\]

phase/address cells require any endpoint-parity analysis at all.

## 3. Slack-deviation bound

Inside one of the seven critical cells, use the unique baseline schedule in which every paid odd occurs at

\[
u=1.
\]

For a paid event with phase value `Omega`, raising its slack changes the penalty by

\[
\Delta p(u)
=
\left(\frac12-2^{-u}\right)\frac{\Omega}{3}.
\]

Since every phase value satisfies

\[
\Omega>\frac12,
\]

we have

\[
u=2:\quad \Delta p>\frac1{24},
\]

\[
u=3:\quad \Delta p>\frac1{16},
\]

and

\[
u\ge4:\quad \Delta p>\frac7{96}.
\]

Two elevated paid events contribute more than

\[
\frac1{12}.
\]

The largest baseline deficit among all seven critical cells is strictly smaller than both

\[
\frac1{12}
\quad\text{and}\quad
\frac7{96}.
\]

Therefore every negative adjusted path must satisfy

\[
\boxed{
\text{at most one paid event has }u>1,
\qquad
u\le3.
}
\]

This collapses the potentially large slack-history family to exactly 13 legal low-deviation words per critical phase cell.

## 4. Exact congruence audit of the seven cells

The seven cells therefore require only

\[
7\times13
=
\boxed{91}
\]

slack/parity words.

Each complete word is converted directly into one exact congruence

\[
\boxed{t\equiv\tau\pmod{2^{h_{\rm cl}}}}
\]

and intersected with the exact source-lift interval.

The result is:

- `77` low-deviation words are already nonnegative at `19/503`;
- `12` negative cylinders are singleton;
- exactly `2` negative cylinders are multi-source.

The two negative multi-source cylinders are both the minimum-slack baseline words in the first two critical cells, and each contains exactly

\[
\boxed{3}
\]

ordinary sources.

Thus the complete negative ordinary-start workload is

\[
12+2\cdot3
=
\boxed{18}
\]

actual integer targets.

## 5. Same-integer closure

Every one of those 18 exact target anchors was continued under the shortcut Collatz map.

All 18 reach

\[
\le2^{71}
\]

within at most

\[
\boxed{7}
\]

additional shortcut steps.

For a hypothetical minimal counterexample above the frozen published floor, this is impossible: an iterate below the root is already convergent by minimality, and here the calculation reaches the verified floor itself.

Therefore

\[
\boxed{
\text{no }r=22\text{ multi-paid macro can belong to a first-cell minimal-counterexample path.}
}
\]

## 6. New frontier

Combining MATH-062, MATH-063, and MATH-064 gives

\[
\boxed{
\begin{array}{ll}
r\ge65
&\text{all multi-paid macros automatically safe},\\[1mm]
23\le r\le64
&\text{multi-source symbolic part automatically safe; singleton track only},\\[1mm]
r=22
&\text{exactly closed by MATH-064},\\[1mm]
2\le r\le21
&\text{detailed mixed Bellman/same-integer work remains}.
\end{array}
}
\]

The detailed paid-count frontier is therefore reduced from the original unbounded range to

\[
\boxed{2\le r\le21.}
\]

## 7. DSD audit

### SAFE

- phase refinement before endpoint branching;
- phase-cost lower-bound gate;
- exact dyadic source-resolution gate;
- exact low-deviation completeness from the slack penalty increments;
- exact congruence solving for every remaining parity word;
- same-integer continuation of all 18 negative ordinary targets;
- closure of the complete `r=22` layer.

### OPEN

- `2<=r<=21` multi-paid layers;
- mixed one-paid / multi-paid Bellman potential;
- arbitrary aperiodic same-integer continuation;
- first universal cell and later cells.

### PROHIBITED UPGRADES

- `r=22` closure `=>` all `r<=21` layers behave similarly;
- 18 finite target checks `=>` asymptotic density or universal descent;
- removal of the `r=22` layer `=>` first-cell closure.

## 8. Next target

Proceed downward to `r=21` with exactly the same hierarchy:

\[
\text{phase gate}
\to
\text{source-resolution gate}
\to
\text{small slack-deviation budget}
\to
\text{exact congruence}
\to
\text{same-integer continuation}.
\]

MATH-063 shows only 56 `r=21` phase/address cells survive the first two cheap gates, so no unrestricted endpoint-history enumeration is required.

## Reproducibility

`collatz/src/2026_09_11_math064_r22_exact_closure_certificate.py`

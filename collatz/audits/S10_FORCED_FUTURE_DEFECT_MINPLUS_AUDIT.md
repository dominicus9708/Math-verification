# S10 audit — finite-horizon forced future defect min-plus gate

Status: **theorem CLOSED / finite frontier execution PENDING / universal closure OPEN**

## Audited question

Can the active source state support a defect lower bound that is genuinely new relative to the already-realized prefix defect `N`?

Yes, at any fixed future one-event horizon, by minimizing the exact transported additional defect over all nonempty source-preserving pure-ballot descendants.

The resulting quantity is

\[
F_r^{min}(s)
=
\min_{d\in\mathcal D_r(s)}
\bigl(N(d)-3^rN(s)\bigr),
\]

when the depth-`r` descendant set is nonempty.

---

## D — Domain

The domain is one exact active source cylinder with the current S10 state

\[
(r,y,m_{lo},m_{hi},h,S)
\]

plus the exact defect scalar `N` used by the directed physical audit reconstruction.

Future transitions are only certified nonempty source-preserving valuation children that remain pure-ballot legal.

A branch that loses pure ballot is closed and removed from the future-survivor set; it is not assigned an artificial defect value.

**Status: EXACT.**

---

## R — Resolution

At one future one-event,

\[
\Delta=N'-3N=2^{t_q}-2^a\ge0.
\]

At horizon `r`,

\[
N_r=3^rN_0+F_r,
\]

with

\[
F_r=\sum_{k=0}^{r-1}3^{r-1-k}\Delta_k.
\]

Therefore all quantities are exact integers at one common descendant normalization.

No floating-point phase or asymptotic approximation is used.

**Status: EXACT / CLOSED.**

---

## S — State sufficiency

The current source state plus `N` is sufficient to enumerate each exact valuation child and to compute the next target-displacement atom.

No historical H/L label, formation rank, correction word, or checkpoint residue is needed for this finite-horizon calculation.

However source payload cannot be discarded: the positivity of `F_r^{min}` can depend on whether the live parameter interval intersects the unique all-zero-displacement dyadic residue class.

**Status: SUFFICIENT with source payload retained; control-only quotient REJECTED.**

---

## E — Equivalence

For a nonempty depth-`r` descendant set,

\[
F_r^{min}=0
\]

if and only if at least one exact descendant path realizes zero new displacement at every one-event in the horizon.

Hence

\[
F_r^{min}>0
\]

is equivalent to exclusion of every exact all-target-position continuation through the audited horizon, while at least one legal descendant remains.

This is stronger than merely observing that some branches incur displacement.

**Status: EXACT / CLOSED.**

---

## T — Transition

The min-plus recursion is

\[
F_r^{min}(s)
=
\min_c
\left(3^{r-1}\Delta(s,c)+F_{r-1}^{min}(c)\right),
\]

where the minimum ranges only over children that possess a surviving depth-`r-1` continuation.

This exactly transports defect to the final odd-count normalization.

**Status: EXACT / CLOSED.**

---

## C — Closure

The algebraic finite-horizon gate is closed.

The newly added certificate

- reconstructs the certified jump-8 parent set;
- expands four additional exact valuation jumps;
- asserts the previously reconstructed j9–j12 raw layer totals as regression targets;
- classifies each jump-8 parent at each horizon into ballot-dead, zero-floor, positive-floor, and whole-parent physical-closure states.

In the present chat environment that Python certificate has not been executed, and the branch has no automatic workflow run attached to the commit.

Therefore its printed future-floor counts are **not yet promoted to certified numerical results** in this audit.

**Status: theorem CLOSED; frontier execution PENDING.**

---

## N — Non-independence

`F_r` is independent of the already-realized prefix defect only in the precise additive sense

\[
N_r=3^rN_0+F_r.
\]

It must not be confused with historical prefix-defect bounds already contained in `N_0`.

It is also not an independent probability factor: it is deterministically derived from exact source descendants.

**Status: exact additive separation; probabilistic multiplication REJECTED.**

---

## O — Outstanding

1. execute the four-horizon certificate in a repository-capable Python environment;
2. record the exact counts/populations with `F_r^{min}>0`;
3. identify parents for which all horizon survivors are physically rejected;
4. if whole-parent closures occur, write them as exact finite source-fiber closures and update the canonical counts;
5. if no closures occur, inspect the minimum positive floors and determine whether a larger horizon or direct zero-path residue exclusion is the better next axis;
6. seek an analytic source-universal rule forcing zero-path exclusion without raw descendant expansion.

---

## Audit matrix

| Dimension | Result |
|---|---|
| D — domain | exact source-preserving pure-ballot descendants |
| R — resolution | exact integer descendant normalization |
| S — sufficiency | source state + N sufficient; source payload retained |
| E — equivalence | positive floor iff no zero-defect depth-r survivor |
| T — transition | exact min-plus transport |
| C — closure | theorem CLOSED; frontier execution PENDING |
| N — non-independence | separated from current N by exact transport; no probability factor |
| O — outstanding | execute, measure, then test physical whole-parent closure |

## Dependencies

- `../theorems/TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`
- `../theorems/FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`
- `../src/A0_s1_8jump_forced_future_defect_minplus_certificate.py`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`
- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`

## Final verdict

\[
\boxed{
\text{A genuinely future, source-sensitive additive defect is now defined exactly at finite horizon.}
}
\]

What remains is no longer a definition gap.  It is an execution/yield question and, beyond finite horizons, an analytic compression question.

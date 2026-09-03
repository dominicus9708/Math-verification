# S10 audit — finite-horizon forced future defect min-plus gate

Status: **theorem CLOSED / horizons 1–4 EXECUTED / zero-path extension to 41 EXECUTED / stronger cumulative floor OPEN**

## Audited question

Can the active exact source state support a defect lower bound that is genuinely new relative to the already-realized prefix defect `N`?

Yes.  For fixed future one-event horizon `r`, define

\[
F_r^{min}(s)
=
\min_{d\in\mathcal D_r(s)}
\bigl(N(d)-3^rN(s)\bigr)
\]

when the nonempty source-preserving pure-ballot descendant set `D_r(s)` exists.

Branches that lose pure ballot before the horizon are recorded as closed, not as zero-defect descendants.

---

## D — Domain

One exact active source cylinder with persistent payload

\[
(r,y,m_{lo},m_{hi},h,S)
\]

plus the exact directed-physical defect scalar `N`.

Transitions are exact source-preserving valuation children only.

**Status: EXACT.**

---

## R — Resolution

At one future one-event,

\[
\Delta=N'-3N=2^{t_q}-2^u\ge0.
\]

At horizon `r`,

\[
N_r=3^rN_0+F_r,
\qquad
F_r=
\sum_{k=0}^{r-1}3^{r-1-k}\Delta_k.
\]

Everything is an exact integer in descendant odd-count normalization.

**Status: EXACT / CLOSED.**

---

## S — State sufficiency

The source payload plus `N` determines every exact valuation child and every next defect atom.

No persistent H/L label, formation rank, checkpoint residue, or historical correction word is required.

Source payload may not be discarded because zero-floor versus positive-floor can depend on whether the live parameter interval meets one required dyadic residue.

**Status: SUFFICIENT with source payload retained.**

---

## E — Equivalence

For a nonempty horizon-r survivor set,

\[
F_r^{min}=0
\]

if and only if the unique target-exact future path is nonempty.

Thus target-exact residue exclusion gives the exact disjunction

\[
\boxed{
\text{ballot closure before horizon }r
\quad\text{or}\quad
F_r^{min}>0.
}
\]

**Status: EXACT / CLOSED.**

---

## T — Transition

The exact Bellman recursion is

\[
F_r^{min}(s)
=
\min_c
\left(
3^{r-1}\Delta(s,c)+F_{r-1}^{min}(c)
\right),
\]

where only children with a surviving depth-`r-1` continuation contribute.

The zero-floor case has a stronger shortcut: follow only the unique valuation that places each future one exactly at its target position.

**Status: EXACT / CLOSED.**

---

## C — Closure and finite execution

### Horizons 1–4

The current 14,224 jump-8 source cylinders were independently reconstructed from the exact GitHub certificates and executed in the chat Python environment.

The previously exploratory global layers are reproduced exactly:

| future one horizon | cylinders | population |
|---:|---:|---:|
| 1 | 34,318 | 23,697,743,382,405,825,230 |
| 2 | 93,000 | 21,589,704,816,219,050,321 |
| 3 | 209,784 | 18,423,678,262,570,974,925 |
| 4 | 609,808 | 16,690,807,021,040,991,694 |

For every one of the 14,224 parents and every horizon `r=1..4`, the unique target-exact source descendant is nonempty.
Therefore

\[
\boxed{F_r^{min}=0\quad(r=1,2,3,4)}
\]

for every parent.

The target-exact descendants themselves also fail the directed physical rejection gate, so no parent can have all horizon survivors physically rejected.

Hence:

- parent ballot closures through these horizons: `0`;
- positive future floors through these horizons: `0`;
- whole-parent physical closures: `0`.

### Zero-path extension through horizon 41

The target-exact path can be tested without positive-defect tree expansion.
The new certificate

- `../src/A0_s1_8jump_zero_future_defect_residue_exclusion_certificate.py`

follows that unique residue path through 41 future one-events.

Exact finite result:

- horizons 1–11: all 14,224 parents retain it;
- horizon 12: exclusions begin;
- horizon 40: one parent retains it;
- horizon 41: zero parents retain it.

Therefore every jump-8 parent is, by horizon 41, either already ballot-closed or forced to have positive future defect.

However the universal one-displacement lower floor obtained from this fact produces **zero** whole-parent physical closures.

At horizon 41, for every parent the additional future defect required by the parent-level physical barrier is more than `10^12` times the weak guaranteed one-displacement floor.  Exact quotient range:

\[
1{,}049{,}362{,}201{,}040
\le
\left\lfloor F_{required}/L_{41}\right\rfloor
\le
1{,}049{,}364{,}901{,}399.
\]

**Status: finite execution CLOSED; yield negative for the one-displacement floor.**

---

## N — Non-independence

`F_r` is separated from realized prefix defect only by the exact transport identity

\[
N_r=3^rN_0+F_r.
\]

It is not a probability factor and cannot be multiplied by an empirical survival rate.
Historical realized-prefix displacement bounds cannot be added to exact current `N`.

**Status: exact additive separation / probabilistic independence claim REJECTED.**

---

## O — Outstanding

The remaining useful problem is no longer to prove that **some** future displacement occurs; horizon 41 already does that for every current parent unless it ballot-closes earlier.

The open target is a source-sensitive lower bound on the **amount** of unavoidable future displacement, for example:

1. minimum number of displaced future one-events;
2. minimum weighted displacement sum;
3. exact or certified lower envelope for
   \[
   \sum_k3^{r-1-k}(2^{t_{q+k}}-2^{u_k});
   \]
4. a branch-and-bound/min-plus method that proves this floor without enumerating the full source tree.

Only such a cumulative floor has a realistic chance of strengthening the current directed physical gate.

---

## Audit matrix

| Dimension | Result |
|---|---|
| D | exact source-preserving pure-ballot descendants |
| R | exact integer descendant normalization |
| S | source payload + `N` sufficient |
| E | zero floor iff target-exact source path exists |
| T | exact min-plus transport; zero-path shortcut exact |
| C | r=1..4 executed; zero-path to r=41 executed; weak-floor closures 0 |
| N | no double count; no probability multiplication |
| O | cumulative/weighted unavoidable displacement floor |

## Dependencies

- `../theorems/TARGET_DISPLACEMENT_DEFECT_EXACT_DECOMPOSITION.md`
- `../theorems/FINITE_HORIZON_FORCED_FUTURE_DEFECT_MINPLUS.md`
- `../theorems/ZERO_FUTURE_DEFECT_RESIDUE_EXCLUSION.md`
- `../src/A0_s1_8jump_forced_future_defect_minplus_certificate.py`
- `../src/A0_s1_8jump_zero_future_defect_residue_exclusion_certificate.py`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`

## Final verdict

\[
\boxed{
\text{Existence of future defect is now finite-certified on every jump-8 parent by horizon 41,}
}
\]

but

\[
\boxed{
\text{the present lower bound on its magnitude is far too weak for physical whole-fiber closure.}
}
\]

The next frontier is therefore **cumulative source-sensitive displacement**, not deeper confirmation of mere positivity.

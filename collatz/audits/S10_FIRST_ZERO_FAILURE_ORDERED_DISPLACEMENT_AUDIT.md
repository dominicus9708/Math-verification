# S10 audit — exact ordered-displacement minimum at first zero-path failure

Status: **EXACT finite frontier CLOSED / physical yield zero / post-failure accumulation OPEN**

## Audited question

Once the target-exact future source path first becomes empty, can the minimum genuinely new future defect be computed exactly without expanding the unrestricted valuation tree?

Yes.

For every current jump-8 parent, at its individualized first zero-path failure horizon `r0`, the exact quantity

\[
F_{r_0}^{min}
\]

is certified by ordered-displacement enumeration plus a lower bound on all unenumerated higher-displacement classes.

---

## D — Domain

Domain:

- one of the 14,224 exact jump-8 source cylinders;
- its exact current defect scalar `N`;
- its first target-exact path failure horizon `r0` from 12 through 41;
- exact source-preserving valuation transitions only.

**Status: EXACT.**

---

## R — Resolution

Future one-events are represented by exact ordered positions

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0.
\]

The horizon defect is the exact integer

\[
F_r=
\sum_k3^{r-1-k}
\left(2^{t_{q+k}}-2^{t_{q+k}-d_k}\right).
\]

No floating approximation or averaged phase is used.

**Status: EXACT.**

---

## S — State sufficiency

A fixed displacement vector determines one finite future valuation word.
The existing source payload determines whether its parameter residue intersects the live source interval.

No extra persistent H/L, formation, checkpoint, or C4F label is needed.

**Status: SUFFICIENT with exact source payload retained.**

---

## E — Equivalence

For a fixed displacement-count class `c`, every strictly ordered vector with exactly `c` nonzero displacements is enumerated.
A vector is feasible exactly when its source-preserving valuation transitions remain nonempty.

Therefore the minimum feasible class cost `B_c` is exact.

For paths with at least `c` displaced ranks, the lower bound `L_c` is obtained from one unit-shift atom per displaced rank, with the earliest displaced rank restricted by strict ordering against the previous target-exact rank.

Thus the stopping rule

\[
B_{\le c}\le L_{c+1}
\]

is an exact certificate that no unenumerated higher-displacement path can improve the current best.

**Status: EXACT / CLOSED.**

---

## T — Transition

Every candidate vector is consumed through the already-certified valuation-cylinder source transition.
The resulting `F` is in the same descendant normalization as

\[
N_{desc}=3^rN_{parent}+F.
\]

No defect normalization is mixed across odd counts.

**Status: EXACT / CLOSED.**

---

## C — Finite closure result

All 14,224 parents are solved at their first zero-path failure horizon.
Every parent has at least one legal descendant there, hence

\[
\boxed{F_{r_0}^{min}>0}
\]

for every current parent.

Minimum-path displaced-rank distribution:

| ranks | parents | parent population |
|---:|---:|---:|
| 1 | 13,354 | 26,113,797,990,685,568,961 |
| 2 | 724 | 569,741,045,565,622,691 |
| 3 | 124 | 174,459,941,749,512,347 |
| 4 | 21 | 1,838,390,843,599,102 |
| 5 | 1 | 776,085 |

All exact minima are certified after checking no more than six displacement-count classes.
The one parent whose minimum uses five displaced ranks requires the sixth class only as a lower-cost exclusion check; no parent's minimum uses six ranks.

**Status: EXACT finite frontier CLOSED.**

---

## Physical whole-parent gate

Using

\[
N_{desc}\ge3^{r_0}N+F_{r_0}^{min}
\]

and the parent ordinary lower endpoint for the positive source term gives a SAFE physical whole-parent floor.

Exact result:

\[
\boxed{0\text{ whole-parent closures}.}
\]

The ratio between the additional future defect required by the present physical barrier and the exact first-failure minimum lies in

\[
145{,}742{,}202{,}315
\le
\left\lfloor F_{required}/F_{r_0}^{min}\right\rfloor
\le
920{,}214{,}076{,}930.
\]

Hence the first-failure floor is not merely slightly weak; it is many orders of magnitude below the current physical closure requirement.

**Status: SAFE finite negative yield.**

---

## N — Non-independence

The ordered-displacement representation is another exact representation of future correction loss.
It is not an independent probabilistic factor and must not be multiplied with ballot or other survival densities.

The exact first-failure minimum also cannot be added at current normalization; it enters only through

\[
3^{r_0}N+F_{r_0}^{min}.
\]

**Status: non-independence explicit.**

---

## O — Outstanding

The next useful object is post-first-failure accumulation.
A 41-horizon path truncated at `r0` obeys

\[
F_{41}
\ge
3^{41-r_0}F_{r_0}^{min},
\]

but this transport alone preserves the normalized strength and therefore cannot improve the physical result.

A new result must force **additional** displacement after the first failure.
Possible exact directions:

1. repeated zero-increment exclusion after conditioning on low-cost first-failure descendant classes;
2. a Pareto/min-plus frontier carrying `(source residue, accumulated defect)` rather than only the scalar minimum;
3. a lower bound on the minimum number of displaced ranks in successive windows;
4. an alternate source-sensitive predicate that uses displacement locations/2-adic pattern directly instead of collapsing everything into `P`.

The first-failure minimum itself should now be treated as CLOSED and not repeatedly refined.

---

## Audit matrix

| Dimension | Result |
|---|---|
| D | exact jump-8 source parents at individual first failure horizons |
| R | exact integer ordered-displacement cost |
| S | current source payload sufficient |
| E | exact class enumeration + rigorous higher-class lower bound |
| T | exact source-preserving valuation transition |
| C | all 14,224 exact minima CLOSED; physical closures 0 |
| N | deterministic defect representation, not independent pruning |
| O | repeated/cumulative post-failure displacement |

## Dependencies

- `../theorems/ZERO_FUTURE_DEFECT_RESIDUE_EXCLUSION.md`
- `../theorems/FIRST_ZERO_FAILURE_ORDERED_DISPLACEMENT_MINIMUM.md`
- `../src/A0_s1_8jump_zero_future_defect_residue_exclusion_certificate.py`
- `../src/A0_s1_8jump_first_zero_failure_ordered_displacement_minimum_certificate.py`
- `../src/A0_s1_14root_8jump_Pmin_recheck_certificate.py`

## Final verdict

\[
\boxed{\text{first zero-path failure future-defect minimum: EXACT/CLOSED on all current parents}}
\]

\[
\boxed{\text{directed physical whole-parent yield from that floor: 0}}
\]

The active S10 problem has moved to **repeated post-failure source-sensitive displacement accumulation**.

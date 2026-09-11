# MATH-067 — r=17 hybrid multiplicity cutoff

Date: 2026-09-11

Status: `PARTIAL EXACT r=17 REDUCTION / m<=64 CLOSED / m>=1024 CLOSED / 65..1023 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-065 closes all multi-paid layers `r>=18`.
- MATH-066 begins `r=17` with exact AP propagation.

## 1. Why a hybrid cutoff is better than one method

MATH-066 showed that very large arithmetic-progression cylinders are cheaper to continue as families, while singleton cylinders are cheaper to materialize and continue directly.

A trial lowering the AP threshold from `1024` toward `128` caused some medium-size families to generate very large parity trees.  Therefore multiplicity alone is not monotone with propagation cost.

The practical split is to attack the small and large ends separately.

## 2. Small multiplicity bands

Using the unchanged MATH-065 same-integer target construction followed by memoized ordinary shortcut continuation gives:

| multiplicity band | cylinders | target occurrences | maximum additional shortcut steps |
|---:|---:|---:|---:|
| `m=1` | 1,013,728 | 1,013,728 | 258 |
| `2<=m<=4` | 341,488 | 980,832 | 283 |
| `5<=m<=16` | 205,594 | 1,865,597 | 297 |
| `17<=m<=32` | 74,170 | 2,010,731 | 283 |
| `33<=m<=64` | 12,151 | 462,694 | 243 |

Every target in every listed band reaches

\[
\le2^{71}.
\]

Hence the complete small-multiplicity region

\[
\boxed{m\le64}
\]

is closed.

Together these bands contain

\[
\boxed{1,647,131}
\]

negative-candidate cylinders and

\[
\boxed{6,333,582}
\]

target occurrences.

## 3. Large multiplicity region

MATH-066 already proves that every cylinder with

\[
\boxed{m\ge1024}
\]

closes under exact arithmetic-progression propagation.

That region contains

\[
\boxed{4,086}
\]

cylinders representing

\[
\boxed{17,143,582}
\]

target occurrences.

## 4. Exact unresolved core

The full `r=17` negative-candidate workload is

\[
1,728,083\text{ cylinders}
\]

and

\[
38,457,239\text{ target occurrences}.
\]

Subtracting the proven small and large regions leaves exactly

\[
\boxed{76,866}
\]

cylinders representing

\[
\boxed{14,980,075}
\]

target occurrences.

Their multiplicities satisfy precisely

\[
\boxed{65\le m\le1023}.
\]

Therefore the correct status is

\[
\boxed{r=17\text{ remains OPEN, but only in the medium-multiplicity core}.}
\]

## 5. Computational observation that must not be over-promoted

Attempting direct ordinary continuation for the next band `65<=m<=127` exceeded the current execution budget.  This is a computational-cost observation only.

It does **not** mean that this band is mathematically harder, contains a counterexample, or fails to descend.

Likewise, the earlier AP propagation attempt at threshold `128` becoming expensive does not show that medium APs are dynamically exceptional.  It shows only that the present state representation branches inefficiently there.

## 6. DSD interpretation

The useful discriminator is no longer raw multiplicity.

The next state compression should account for at least

\[
(\text{AP residue information},\ b,\ m,\ \text{current affine height},\ \text{remaining reduced-cost budget}).
\]

Two states may be merged only if this preserves all future parity partitions and every proof-facing cost bound.

The current exact claim hierarchy remains:

1. `r>=18`: closed;
2. `r=17, m<=64`: closed;
3. `r=17, m>=1024`: closed;
4. `r=17, 65<=m<=1023`: open;
5. `r<=16`: not yet treated by this certificate family.

## 7. Next target

The next calculation should optimize the medium-multiplicity core rather than lower either threshold blindly.

Two promising routes are:

1. **residue-trie memoization** — share parity-prefix work between different AP cylinders when their affine states induce the same low-bit continuation;
2. **Bellman reduced-cost pruning during AP descent** — attach the remaining `19/503` budget to the family state and terminate subfamilies before ordinary descent materialization becomes necessary.

A successful medium-core compression would complete `r=17` without returning to a 38-million-target brute-force audit.

## Reproducibility

`collatz/src/2026_09_11_math067_r17_hybrid_cutoff_certificate.py`

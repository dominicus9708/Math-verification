# MATH-042 — depth-32 one-sided Hensel flat class-max audit

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / ONE-SIDED ROOT-HENSEL PRUNING / FINITE EXACT`
- Scope: coefficient-surviving parity prefixes under the frozen published-floor minimal-counterexample spine, compared against arbitrary parity-word competitors in the same Hensel class.

## 1. Selection asymmetry retained

The audited comparison is

\[
\text{candidate}\in\mathcal L_{\rm coeff},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

For fixed depth `k`, write

\[
C=h3^q+r,
\qquad0\le r<3^q.
\]

The class key is `(q,r)`, and the candidate survives the root-Hensel gate exactly when its correction equals the unrestricted maximum correction in that class.

MATH-013 downstream dominance is crucial: if a prefix is not class-maximal, appending the same suffix to a better competitor preserves the positive correction gap. Hence a current-depth class maximum could not have had a non-maximal earlier prefix. This lets MATH-042 audit all coefficient-surviving depth-32 words directly instead of replaying the nested filter from depth 1.

## 2. Exact depth-32 result

The coefficient-surviving language has

\[
\boxed{41{,}347{,}483}
\]

length-32 words.

The exact one-sided unrestricted class-max comparison leaves

\[
\boxed{33{,}880{,}411}
\]

survivors.

Thus the cumulative number removed by root-Hensel maximality through depth 32 is

\[
\boxed{7{,}467{,}072}.
\]

MATH-041 had `19,347,686` depth-31 nested survivors. After the depth-32 coefficient gate they generate exactly

\[
33{,}894{,}412
\]

children before the new depth-32 Hensel comparison. Therefore the genuinely new depth-32 Hensel pruning is

\[
\boxed{33{,}894{,}412-33{,}880{,}411=14{,}001}.
\]

## 3. Exact q-layer survivors

| q | coefficient candidates | Hensel-max survivors | removed |
|---:|---:|---:|---:|
| 21 | 13,472,296 | 10,924,522 | 2,547,774 |
| 22 | 13,049,303 | 10,653,576 | 2,395,727 |
| 23 | 8,422,120 | 6,934,804 | 1,487,316 |
| 24 | 4,118,103 | 3,427,766 | 690,337 |
| 25 | 1,613,495 | 1,360,759 | 252,736 |
| 26 | 511,496 | 438,144 | 73,352 |
| 27 | 130,169 | 113,563 | 16,606 |
| 28 | 26,070 | 23,221 | 2,849 |
| 29 | 3,968 | 3,620 | 348 |
| 30 | 432 | 405 | 27 |
| 31 | 30 | 30 | 0 |
| 32 | 1 | 1 | 0 |

The unrestricted competitor language examined across these q-layers contains exactly

\[
\boxed{236{,}618{,}693}
\]

length-32 words.

## 4. Calculation improvement

Because `q>=21` at depth 32, arbitrary competitors have at most 11 zero positions. Rather than materializing a global Hensel table, MATH-042:

1. generates only coefficient-surviving candidate corrections;
2. stores only candidate class residues in a flat hash table;
3. enumerates arbitrary words by their zero-position combinations;
4. updates only target class maxima;
5. compares candidate correction against the exact unrestricted maximum.

This avoids the large monolithic unrestricted class table used by the older DP route.

An independent depth-31 run of the same flat-class-max idea reproduced MATH-041 exactly:

\[
23{,}642{,}078\to19{,}347{,}686.
\]

## 5. DSD interpretation

- `D`: candidate/competitor selection is explicitly asymmetric.
- `R`: exact depth 32, exact q-layer, exact modulo `3^q` class residue.
- `S`: coefficient gate is applied only to the candidate side.
- `E`: candidate is excluded iff an arbitrary same-class word has larger correction.
- `T`: MATH-013 downstream dominance transfers current-depth non-maximality to all-prefix inadmissibility.
- `C`: independent depth-31 regression reproduces MATH-041.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.
- `O`: 7,467,072 depth-32 coefficient words are removed cumulatively; first-cell emptiness is not established.

## 6. Prohibited upgrades

- depth-32 prefix pruning ⇒ first universal cell empty — **PROHIBITED**;
- finite q-layer counts ⇒ asymptotic density statement — **PROHIBITED**;
- Hensel-max prefix ⇒ complete Collatz candidate validity — **PROHIBITED**;
- current finite calculation ⇒ arbitrary-depth root-Hensel theorem — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_depth32_one_sided_hensel_flat_classmax_certificate.cpp`

Certificate commit:

`e3592b987e065d376b260b3921919bce58869088`

The first universal cell and the Collatz conjecture remain `OPEN`.

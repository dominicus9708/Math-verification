# First universal cell: exact right-congruence audit of the 340-label survival masks

Date: 2026-09-07

Status: **SAFE negative/compression audit.** The 11-bit block-label transducer does admit substantial deterministic pruning for low-surplus states, but in exactly those strongest cases the endpoint residue `y mod 2048` cannot be coarsened at all if the exact 340-label survival set must be preserved.

No Collatz proof is claimed.

---

## 1. Object being compressed

For fixed depth-61 odd count `q` and endpoint residue

\[
y\pmod{2048},
\]

define the 340-bit mask

\[
M_{q,y}(a)
=1
\]

exactly when block label

\[
a\in\{1024,\ldots,1363\}
\]

produces an 11-bit continuation that remains coefficient-surviving through depth 72.

Two endpoint residues may be merged by an exact right-congruence for this local task only if their complete masks are identical:

\[
M_{q,y_1}=M_{q,y_2}.
\]

The certificate enumerates all 2048 endpoint residues and stores each exact 340-bit mask as an integer bitset.

---

## 2. Exact right-congruence class counts

| `q61` | distinct exact 340-label masks | min labels surviving | max labels surviving |
|---:|---:|---:|---:|
| 39 | 2048 | 36 | 47 |
| 40 | 2048 | 124 | 141 |
| 41 | 2048 | 221 | 235 |
| 42 | 2048 | 288 | 303 |
| 43 | 2048 | 320 | 333 |
| 44 | 1838 | 336 | 340 |
| 45 | 341 | 339 | 340 |
| 46–61 | 1 | 340 | 340 |

The decisive result is

\[
\boxed{
q_{61}=39,40,41,42,43
\Longrightarrow
\#\{M_{q,y}:y\bmod2048\}=2048.
}
\]

Thus every endpoint residue gives a different exact set of surviving top-address labels.

---

## 3. Consequence: no coarse endpoint quotient in the strongest sieve range

The previous transducer result was strongest at low surplus:

- `q61=39`: at most 47 of 340 labels survive;
- `q61=40`: at most 141;
- `q61=41`: at most 235.

However, precisely there,

\[
\boxed{
\text{no two }y\bmod2048\text{ residues have the same exact 340-label survival mask.}
}
\]

Therefore any descriptor that drops or coarsens the endpoint residue while trying to retain the exact label set is invalid in these ranges.

This rejects the tempting compression

\[
(q_{61},y\bmod2048)
\longrightarrow
q_{61}
\]

and also rejects every nontrivial quotient of `y mod2048` based solely on equality of the local 340-label coefficient-survival mask for `q61=39,...,43`.

---

## 4. The transition at q=44,45,46

At

\[
q_{61}=44
\]

the exact mask quotient has

\[
1838
\]

classes, so a small amount of endpoint compression appears.

At

\[
q_{61}=45
\]

only

\[
341
\]

exact masks remain.

At

\[
q_{61}\ge46,
\]

all 340 block labels satisfy coefficient survival through depth72, so the mask is identically all ones and there is one trivial class.

The last case is not useful pruning; it means this particular coefficient-only 11-bit sieve has exhausted its information.

---

## 5. Why q alone cannot eliminate a named block

For fixed `q` and fixed label `a`, varying `y mod2048` translates

\[
y+a3^q
\]

through every residue modulo2048.

Hence, unless additional information restricts which endpoint residues are actually realizable from lower-61 universal-spine prefixes, no individual block label can be declared globally impossible using `q61` alone.

The useful cap is pointwise in `y`, not uniform in the identity of the surviving labels.

This distinction prevents the invalid inference

\[
\text{at most 47 labels survive per }y
\not\Rightarrow
\text{there exist 293 globally bad labels}.
\]

---

## 6. DSD interpretation

The current 61+11 split separates three information layers:

1. `q61`: scalar surplus information;
2. `y mod2048`: exact local continuation phase;
3. block label `a`: 11-bit ordinary address choice.

The audit shows that layers 2 and 3 are strongly entangled in the low-surplus regime. The endpoint phase cannot be discarded before applying the address label.

This is precisely a **resolution barrier** rather than a failure of the 11-bit transducer itself.

---

## 7. DSD audit

### CLOSED / SAFE

1. every exact 340-label mask is evaluated for all 2048 endpoint residues;
2. distinct-mask counts are exact;
3. `q61=39,...,43` have no nontrivial mask-preserving endpoint quotient;
4. `q61=44` and `45` admit only the stated finite reductions;
5. `q61>=46` collapses to one mask because the local coefficient sieve becomes trivial.

### OPEN

1. characterize which `y mod2048` residues are actually reachable from lower-61 universal-spine states at each `q61`;
2. exploit correlations between the lower prefix and endpoint phase rather than quotienting the phase away;
3. combine endpoint phase with root-Hensel/endpoint eligibility;
4. turn conditional label caps into complete block exclusions.

### PROHIBITED UPGRADES

1. Do not replace `y mod2048` by `q61` alone in the low-surplus branch.
2. Do not infer globally excluded block labels from a pointwise cardinality cap.
3. Do not treat the 1838/341 class counts as probabilistic entropy rates.
4. Do not infer first-cell or Collatz closure.

---

## 8. Reproducibility

Certificate:

`collatz/src/first_cell_block_label_mask_right_congruence_certificate.py`

Commit:

`0ab28726a671b9c0e74ddaeded4e39cc6514ba19`

Expected key output:

```text
PASS
q61=39..43: all 2048 endpoint residues are pairwise distinguishable
q61=44: 1838 exact mask classes
q61=45: 341 exact mask classes
q61>=46: one trivial class because all 340 labels survive
```

---

## 9. Next target

The next useful calculation is no longer a generic quotient of endpoint residues. It is the **reachability relation**

\[
(q_{61},y\bmod2048)
\]

induced specifically by lower-61 universal-spine starts.

If that reachable subset is much smaller than all `2048` phases for low `q61`, the 47/141/235 label caps may become block-level eliminations. If it fills all phases, this route is correspondingly weakened and should be pruned.
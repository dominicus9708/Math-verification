# First universal cell: 11-bit block-label continuation transducer

Date: 2026-09-07

Status: **SAFE finite exact address-preserving sieve through depth 72.** The result uses the already-audited parity-vector bijection and does not assume independence, random parity, or ternary recursive-sufficiency coverage.

No Collatz proof is claimed.

---

## 1. Split the ordinary start at bit 61

For a surviving first-cell start write

\[
N=a2^{61}+x,
\qquad
1024\le a\le1363,
\qquad
0\le x<2^{61}.
\]

There are 340 possible top-11-bit block labels `a`.

Fix the first 61 binary start bits, equivalently fix `x`. Let

\[
q=q_{61}(x)
\]

be the odd count in its first 61 parity steps and let

\[
y=T^{61}(x)
\]

for the canonical lower residue `x`.

The affine parity-prefix identity gives

\[
\boxed{
T^{61}(a2^{61}+x)=y+a3^q.
}
\]

This is exact because adding `a2^61` to the start contributes `a3^q` after the already-fixed 61-step prefix.

---

## 2. The final 11 parity bits form an affine permutation

The next 11 parity bits depend only on the current endpoint modulo

\[
2^{11}=2048.
\]

Therefore the continuation selected by block label `a` is the parity vector of

\[
\boxed{
(y+a3^q)\bmod2048.
}
\]

Since `3^q` is odd,

\[
\gcd(3^q,2048)=1.
\]

Hence for fixed `(q,y)`, the map

\[
a\mapsto y+a3^q\pmod{2048}
\]

is a permutation of all 2048 residues when `a` ranges over `0,...,2047`.

By the exact parity-vector cylinder bijection, those 2048 residues correspond one-to-one with the 2048 possible 11-bit parity continuations.

Thus:

\[
\boxed{
\text{for a fixed lower-61 state, all 2048 top labels realize all 11-bit parity tails exactly once.}
}
\]

The current first-cell window merely selects the 340 labels

\[
1024,\ldots,1363
\]

from that affine permutation.

---

## 3. Uniform coefficient-survival audit over every endpoint residue

At depth 61 the least coefficient-surviving odd count is

\[
q_{61}^{\min}=39.
\]

For each possible `q=39,...,61`, the certificate enumerates

1. all `y mod 2048`;
2. all 340 surviving block labels;
3. the resulting exact 11-bit parity continuation;
4. whether every prefix through depths `62,...,72` remains coefficient-surviving.

Because every `y mod2048` is checked, the resulting minima and maxima are **uniform over all possible lower-61 prefix states**.

Exact results:

| `q61` | `3^q mod 2048` | minimum surviving labels | maximum surviving labels |
|---:|---:|---:|---:|
| 39 | 11 | 36 | 47 |
| 40 | 33 | 124 | 141 |
| 41 | 99 | 221 | 235 |
| 42 | 297 | 288 | 303 |
| 43 | 891 | 320 | 333 |
| 44 | 625 | 336 | 340 |
| 45 | 1875 | 339 | 340 |
| 46 | 1529 | 340 | 340 |
| 47 | 491 | 340 | 340 |
| 48 | 1473 | 340 | 340 |
| 49 | 323 | 340 | 340 |
| 50 | 969 | 340 | 340 |
| 51 | 859 | 340 | 340 |
| 52 | 529 | 340 | 340 |
| 53 | 1587 | 340 | 340 |
| 54 | 665 | 340 | 340 |
| 55 | 1995 | 340 | 340 |
| 56 | 1889 | 340 | 340 |
| 57 | 1571 | 340 | 340 |
| 58 | 617 | 340 | 340 |
| 59 | 1851 | 340 | 340 |
| 60 | 1457 | 340 | 340 |
| 61 | 275 | 340 | 340 |

---

## 4. New exact source-side pruning

The strongest cases are the low-surplus depth-61 states.

For every possible lower endpoint residue:

\[
\boxed{q_{61}=39\Longrightarrow\text{at most }47\text{ of the 340 block labels survive to depth 72}.}
\]

Thus at least

\[
340-47=293
\]

block labels are removed for every fixed lower-61 state with `q61=39`.

Likewise,

\[
\boxed{q_{61}=40\Longrightarrow\text{at most }141\text{ labels survive},}
\]

and

\[
\boxed{q_{61}=41\Longrightarrow\text{at most }235\text{ labels survive}.}
\]

These are genuine uniform caps, not averages.

Conditional removal counts:

| `q61` | maximum labels left | at least removed |
|---:|---:|---:|
| 39 | 47 | 293 |
| 40 | 141 | 199 |
| 41 | 235 | 105 |
| 42 | 303 | 37 |
| 43 | 333 | 7 |
| 44 | 340 | 0 uniformly |

For `q61>=46`, coefficient survival alone imposes no block-label loss over the final 11 start bits; stronger root/address or later terminal constraints are required there.

---

## 5. Why this is not a density argument

The calculation does not say that a random label survives with some probability.

For every fixed pair

\[
(q_{61},y\bmod2048)
\]

it explicitly checks all 340 actual labels.

The maximum over all endpoint residues is then used as a deterministic bound. Therefore, for example, the `47` cap at `q61=39` is a pointwise statement:

\[
\forall y\pmod{2048},
\quad
\#\{a\in[1024,1363]:\text{survives to depth72}\}\le47.
\]

---

## 6. External-literature role

No new external theorem was required in this step.

The only imported structural fact is the already-audited parity-vector residue bijection, recorded in the Tong Niu 2026 absorption audit as **A — SAFE EXTERNAL THEOREM**. The present affine block-label calculation is internal and finite-exact.

Relevant prior audit:

`collatz/notes/2026-09-07-external-niu-parity-paradoxical-audit.md`

---

## 7. DSD audit

### CLOSED / SAFE

1. the start split `N=a2^61+x` is exact;
2. after the fixed 61-step prefix, block label enters as `a3^q`;
3. reduction modulo `2^11` exactly determines the next 11 parity bits;
4. multiplication by `3^q` is a permutation modulo `2048`;
5. all `y mod2048` and all 340 labels are exhaustively checked;
6. the table of uniform min/max surviving labels is finite-exact;
7. low-surplus states receive deterministic block-label caps.

### OPEN

1. determine how the actual lower-61 universal-spine states distribute among `q61=39,...,61` and endpoint residues without brute-force enumeration;
2. combine the 11-bit label sieve with root-Hensel maximality and endpoint halos;
3. carry the address-specific survivors beyond depth72 toward the first crossing;
4. close individual top-address blocks.

### PROHIBITED UPGRADES

1. Do not multiply the uniform caps as if successive tails were independent.
2. Do not infer that every block is removed because each low-`q61` state loses many labels.
3. Do not ignore high-surplus `q61>=46` states, for which this particular coefficient sieve removes no labels.
4. Do not treat the 2048-label permutation as equidistribution over the restricted 340-label interval.
5. Do not infer first-cell or Collatz closure.

---

## 8. Reproducibility

Certificate:

`collatz/src/first_cell_block_label_11bit_transducer_certificate.py`

Commit:

`f208051d6992186507dafe0587bfd3315ae1c69a`

Expected output begins:

```text
PASS
q61_min = 39
q61 | 3^q mod 2048 | min surviving labels | max surviving labels
39 11 36 47
40 33 124 141
41 99 221 235
```

---

## 9. Next target

The remaining obstacle is now more sharply stated.

For a lower-61 prefix state, the top-address variable has been reduced to a 340-element finite affine orbit. The next compression target is therefore to derive enough information about the lower state to replace the unknown exact endpoint by a smaller descriptor than the full 61-bit history.

A natural next audit is to determine the **minimum endpoint modulus and odd-count information needed to propagate not merely coefficient survival through 72, but root-Hensel/endpoint eligibility into the post-72 continuation**.
# MATH-226 — common mechanical danger selector and exact successor closure from the frozen r=10 output

Date: 2026-09-19

Status: EXACT CROSS-r SUCCESSOR THEOREM / IMMEDIATE NEXT DANGEROUS LOW-PAID HANDOFF CLOSED / FULL r=10 OPEN

## 1. Purpose

MATH-186/202 say that a potentially nonpositive future multi-paid transfer with emitted paid count r must overshoot the current source resolution by at least z_min(r).

Starting from any exact affine child family

Y = B + 3^Q s,   0 <= s < M,

with boundary phase interval I and source resolution

R = ceil(log2 M),   R(1)=0,

a dangerous next transfer must begin with at least

L_min = R + z_min(r)

zero-cost mechanical shortcut bits.

This converts future Bellman danger into one exact dyadic selector on the current AP parameter. The formula is common to every emitted r; r only chooses z_min(r).

## 2. Common selector formula

Fix a mechanical word w of length L_min that is compatible with the current exact phase interval I.

Let A_w be its canonical ordinary source residue modulo 2^L_min.

Compatibility with the current affine child is

B + 3^Q s = A_w  (mod 2^L_min).

Since 3^Q is odd, the parameter is uniquely selected modulo 2^L_min:

s = (A_w-B) 3^(-Q)  (mod 2^L_min).

Because M <= 2^R < 2^L_min, the interval 0<=s<M contains at most one representative.

Hence every phase-compatible mechanical word contributes at most one ordinary boundary anchor

Y_* = B + 3^Q s.

No ordinary member of the AP is scanned.

## 3. Mechanical residue fanout

The exact number of distinct minimum-length mechanical source residues needed by each remaining paid tag is:

| emitted r | z_min(r) | distinct mechanical residues at that precision |
|---:|---:|---:|
| 2 | 1 | 1 |
| 3 | 2 | 2 |
| 4 | 3 | 2 |
| 5 | 6 | 4 |
| 6 | 7 | 5 |
| 7 | 8 | 6 |
| 8 | 10 | 7 |
| 9 | 11 | 7 |
| 10 | 13 | 9 |

For r=10 the nine residues are the MATH-220 catalogue.

Thus all open low-paid tags share one selector construction with fanout at most nine before the exact phase interval is used.

## 4. Frozen r=10 child reconstruction

The unchanged MATH-065/MATH-206 source is reproduced exactly:

- phase/address cells: 994 = 91 safe + 396 singleton + 507 critical;
- branch nodes: 1,994,258;
- negative-candidate leaf families: 278,725;
- represented occurrence mass: 27,557,263,803,397;
- maximum family multiplicity: 830,483,089,363.

For each frozen r=10 leaf, the exact output family is

Y = B + 3^Q s,   0<=s<count.

The child boundary phase interval is transported exactly from the cell through the r=10 paid-cluster epsilon sequence.

## 5. r=10 -> next r=10 danger

For the next emitted r=10 tag, use L_min=R+13.

Across all 278,725 frozen child families, the exact phase interval admits at most four length-L_min mechanical words per family.

Distribution of phase-compatible word counts:

- 201,409 families admit 1 word;
- 44,689 admit 2;
- 31,396 admit 3;
- 1,231 admit 4.

The raw symbolic selector upper bound is therefore 389,899.

After solving the exact parameter congruence and requiring 0<=s<count:

- only 22 frozen child families retain any selector;
- the 22 selector records collapse to 14 distinct ordinary boundary anchors.

All 14 anchors descend exactly to <=2^71; maximum additional shortcut descent is 53.

Therefore

initial r=10 output -> immediate next Bellman-dangerous r=10 handoff

is CLOSED.

## 6. Cross-r successor audit

The same selector formula was applied unchanged for every next emitted tag r=2..10.

| next emitted r | hit child families | selector records | unique boundary anchors | max extra descent |
|---:|---:|---:|---:|---:|
| 2 | 118,896 | 128,986 | 65,625 | 212 |
| 3 | 62,924 | 64,694 | 32,972 | 212 |
| 4 | 32,501 | 32,890 | 16,885 | 154 |
| 5 | 4,237 | 4,237 | 2,234 | 118 |
| 6 | 2,077 | 2,077 | 1,120 | 118 |
| 7 | 1,014 | 1,014 | 544 | 118 |
| 8 | 239 | 239 | 134 | 92 |
| 9 | 122 | 122 | 69 | 61 |
| 10 | 22 | 22 | 14 | 53 |

Every unique selector anchor in every row descends exactly to <=2^71.

Hence every immediate next Bellman-dangerous low-paid transfer from the frozen initial r=10 output is closed.

## 7. Why this is not an r-layer/depth enumeration

The outer computation is not a scan over ordinary source members or over possible depths.

The theorem is one selector law:

(B,Q,M,I,r) -> R -> L_min=R+z_min(r) -> mechanical residues -> one parameter congruence.

The emitted paid count only selects z_min(r).

The frozen r=10 audit is a regression/application of this common law to the already frozen source, not the architecture of the final proof.

## 8. Remaining logical gap

This theorem closes an immediate dangerous successor from a frozen r=10 child.

It does NOT yet prove that after an arbitrary finite sequence of Bellman-safe boundary transfers, the first later dangerous transfer is one of the selectors audited above. Safe transfers change B,Q,M and the boundary phase interval.

Therefore the remaining proof obligation is to propagate the same selector state through arbitrary Bellman-safe transfers with MATH-061/091/187, and apply the selector only when the first dangerous tag is emitted.

This future-complete safe-prefix transducer is the next mainline target.

## 9. Claim boundary

Established:
- exact common mechanical danger-selector theorem;
- exact reproduction of the frozen r=10 source invariants;
- exact closure of every immediate next dangerous r=2..10 successor from the frozen r=10 output;
- in particular, immediate r10->dangerous-r10 is closed.

Not established:
- closure after arbitrary intervening Bellman-safe boundary transfers;
- full r=10 layer closure;
- first-cell emptiness;
- the Collatz conjecture.
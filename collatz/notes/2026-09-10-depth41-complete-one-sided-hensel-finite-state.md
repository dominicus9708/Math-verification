# MATH-051 — complete depth-41 one-sided root-Hensel audit by fixed-d finite state

Date: 2026-09-10
Status: `CONFIRMED / FINITE EXACT / COMPLETE DEPTH-41 ONE-SIDED ROOT-HENSEL`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This is a finite exact prefix-language computation, not a universal proof.
- MATH-051 advances the complete audited frontier from depth 40 to depth 41.

## 1. Depth-41 coefficient boundary

At depth 41,

\[
q_{\min}(41)=26,
\]

because

\[
3^{25}<2^{41}<3^{26}.
\]

The threshold does not rise from depth 40, so every depth-40 coefficient-valid word has both coefficient-valid children. Therefore

\[
\boxed{L_{41}=2L_{40}=12,805,670,000},
\]

where `L_k` denotes the full all-prefix coefficient language at depth `k`.

Likewise every depth-40 nested Hensel survivor has both children in the depth-41 pre-Hensel nested prefilter, hence

\[
\boxed{P_{41}=2S_{40}=10,515,005,264}.
\]

## 2. Fixed-d exact signature used in MATH-051

Let the d even positions of a length-k parity word be

\[
E=(e_0<e_1<\cdots<e_{d-1}),\qquad q=k-d.
\]

Define

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}3^j\left(\frac23\right)^{e_j}.
}
\]

The correction satisfies

\[
\boxed{
\frac{C(E)}{3^{k-d}}
=1+\Sigma_d(E)-3^d\left(\frac23\right)^k.
}
\]

Thus for equal k,d,

\[
\boxed{
C(F)-C(E)=3^{k-d}\left(\Sigma_d(F)-\Sigma_d(E)\right).
}
\]

Consequently two fixed-d words are in the same exact Hensel class exactly when their Sigma difference is an integer; a positive integer difference is exactly the Hensel translation credit.

In cumulative odd-gap coordinates

\[
G_j=e_j-j,
\]

this becomes

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}2^j\left(\frac23\right)^{G_j}.
}
\]

Grouping equal gap levels gives the bounded carry recurrence

\[
\boxed{
h_{r-1}=\frac{2(h_r+\Delta a_r)}3},
\]

with divisibility by 3 required at each level.

## 3. New exact viability pruning

The first fixed-d subset implementation was exact but became memory-heavy at d=12--14. MATH-051 therefore adds an exact existential viability test for each primitive competitor state.

After the already processed high gap levels, let

- `rem` be the number/index of remaining gap levels,
- `na` be the number of unassigned candidate even ranks,
- `nb` be the number of unassigned competitor even ranks,
- `h` be the current carry.

Define `can(rem,na,nb,h)` to mean:

> there exists at least one completion of the remaining candidate and competitor gap blocks, respecting candidate coefficient deadlines and every carry divisibility condition, whose final exact Hensel credit is positive.

`can` is evaluated by an exact recursive search over the next candidate block length `la` and competitor block length `lb`, and memoized. If `can=false`, that primitive competitor state can never witness domination for any descendant candidate and is deleted from the subset without changing the accepted/dominated candidate language.

Before the recursive test, the safe necessary upper bound

\[
\boxed{
U=(h-(2^{n_A}-1))2^{r}+(2^{n_B}-1)3^{r}
}
\]

is used. If `U<=0`, even the optimistic completion in which the competitor puts all remaining ranks at gap 0 and the candidate puts all remaining ranks at the largest remaining gap cannot achieve positive Sigma difference, so the state is impossible and may be discarded exactly.

This is pruning of impossible witnesses, not probabilistic or heuristic pruning.

## 4. Terminal dominated count and primitive defect

Let

\[
D_{k,d}
\]

be the number of coefficient-valid length-k, fixed-d words that are terminally dominated in their exact Hensel class.

Downstream-stable class dominance implies

\[
\boxed{
R_{k,d}=D_{k,d}-D_{k-1,d}-D_{k-1,d-1},
}
\]

where `R_{k,d}` counts nested candidate prefixes that lose exact class-max for the first time at `(k,d)`.

This identity is used to recover the exact current-depth Hensel loss from the finite-state dominated counts.

## 5. Regression against MATH-050 central layers

Before accepting the new depth-41 central results, the viability-pruned solver was run backward against the canonical depth-40 central layers.

It reproduced exactly:

| depth 40 q | d | canonical new loss | finite-state derived loss |
|---:|---:|---:|---:|
| 29 | 11 | 26,875 | 26,875 |
| 28 | 12 | 102,635 | 102,635 |
| 27 | 13 | 371,134 | 371,134 |
| 26 | 14 | 1,064,057 | 1,064,057 |

Thus the new viability pruning preserves the previously audited MATH-050 central result.

The detailed dominated-count audit is stored in

`collatz/results/2026-09-10-depth41-fixed-d-viability-audit.tsv`.

## 6. Newly closed depth-41 central layers

The previously unresolved layers were q=29,28,27,26, equivalently d=12,13,14,15.

The exact dominated counts are:

\[
D_{41,12}=361,499,293,
\]

\[
D_{41,13}=586,723,760,
\]

\[
D_{41,14}=703,863,494,
\]

\[
D_{41,15}=355,002,462.
\]

Using the primitive-defect identity gives

\[
\boxed{R_{41,12}=114,061},
\]

\[
\boxed{R_{41,13}=422,198},
\]

\[
\boxed{R_{41,14}=1,282,478},
\]

\[
\boxed{R_{41,15}=2,016,600}.
\]

The corresponding q-layer survivor counts are

| q | d | pre-Hensel | newly pruned | survivors |
|---:|---:|---:|---:|---:|
| 26 | 15 | 1,546,488,816 | 2,016,600 | 1,544,472,216 |
| 27 | 14 | 3,120,974,892 | 1,282,478 | 3,119,692,414 |
| 28 | 13 | 2,676,589,480 | 422,198 | 2,676,167,282 |
| 29 | 12 | 1,707,170,114 | 114,061 | 1,707,056,053 |

Together with the already checked q>=30 tail, depth 41 is complete.

## 7. Complete depth-41 ledger

Canonical result:

`collatz/results/2026-09-10-depth41-complete-one-sided-hensel.tsv`

The final totals are

\[
\boxed{\text{coefficient language}=12,805,670,000},
\]

\[
\boxed{\text{nested prefilter}=10,515,005,264},
\]

\[
\boxed{\text{newly pruned at depth 41}=3,874,550},
\]

\[
\boxed{\text{survivors}=10,511,130,714}.
\]

Therefore cumulative Hensel removal through depth 41 is

\[
\boxed{
12,805,670,000-10,511,130,714
=2,294,539,286.
}
\]

Since q_min did not change from 40 to 41, this also cross-checks as

\[
\boxed{
2(1,145,332,368)+3,874,550=2,294,539,286.
}
\]

## 8. Complete depth-41 q table

| q | coefficient language | prefilter | survivors | newly pruned |
|---:|---:|---:|---:|---:|
| 26 | 1,899,474,678 | 1,546,488,816 | 1,544,472,216 | 2,016,600 |
| 27 | 3,823,555,908 | 3,120,974,892 | 3,119,692,414 | 1,282,478 |
| 28 | 3,262,891,042 | 2,676,589,480 | 2,676,167,282 | 422,198 |
| 29 | 2,068,555,346 | 1,707,170,114 | 1,707,056,053 | 114,061 |
| 30 | 1,059,690,721 | 880,982,971 | 880,953,629 | 29,342 |
| 31 | 455,820,107 | 382,235,624 | 382,228,154 | 7,470 |
| 32 | 166,571,780 | 141,092,144 | 141,090,446 | 1,698 |
| 33 | 51,809,775 | 44,393,684 | 44,393,177 | 507 |
| 34 | 13,649,879 | 11,850,117 | 11,849,974 | 143 |
| 35 | 3,013,145 | 2,654,671 | 2,654,619 | 52 |
| 36 | 547,841 | 490,672 | 490,672 | 0 |
| 37 | 79,980 | 72,943 | 72,943 | 0 |
| 38 | 9,020 | 8,393 | 8,393 | 0 |
| 39 | 738 | 703 | 702 | 1 |
| 40 | 39 | 39 | 39 | 0 |
| 41 | 1 | 1 | 1 | 0 |

## 9. State compression achieved

For depth 41, the exact viability-pruned subset-state peaks were:

| d | q | peak subset states | viability memo states |
|---:|---:|---:|---:|
| 8 | 33 | 56 | 20,896 |
| 9 | 32 | 136 | 45,560 |
| 10 | 31 | 337 | 93,166 |
| 11 | 30 | 1,049 | 184,710 |
| 12 | 29 | 3,227 | 339,746 |
| 13 | 28 | 9,835 | 594,017 |
| 14 | 27 | 28,455 | 1,000,342 |
| 15 | 26 | 44,095 | 1,352,979 |

This replaces the enormous parity-word populations with a finite exact witness-state computation for the entire depth-41 admissible range.

The reproducible solver is

`collatz/src/2026_09_10_depth41_fixed_d_viability_finite_state.cpp`.

## 10. DSD interpretation

The decisive change in MATH-051 is not a larger brute-force frontier. It is the change of description:

\[
\boxed{
\text{parity-word enumeration}
\longrightarrow
\text{fixed-d gap signature}
\longrightarrow
\text{bounded carry states}
\longrightarrow
\text{viable witness subsets}.
}
\]

For fixed d, the depth dependence of the Hensel collision test is removed from the Sigma difference, and impossible future competitor states are eliminated by an exact finite recursion.

This is the first complete depth in the branch whose difficult central layers were closed by the new finite-state description rather than by the earlier unrestricted tail-hash enumeration.

## 11. Next finite input, not yet executed

At depth 42,

\[
q_{\min}(42)=27,
\]

so the coefficient boundary rises by one.

Using the completed depth-41 values, the exact next pre-Hensel nested input would be

\[
\boxed{
P_{42}=2S_{41}-S_{41,q=26}=19,477,789,212.
}
\]

The full coefficient language would be

\[
\boxed{
L_{42}=2L_{41}-L_{41,q=26}=23,711,865,322.
}
\]

These are only next-input identities. MATH-052 has not been started in this checkpoint.

## 12. Audit boundaries

Do not upgrade this checkpoint to any of the following claims:

- finite exact depth 41 => Collatz proof;
- finite-state for d<=15 => a uniform finite state bound for arbitrary d;
- viability pruning => loss of arbitrary competitors;
- fixed-d Sigma signature => proof that all d admit a bounded-size closed form independent of d;
- MATH-051 complete => global convergence.

The global conjecture remains open. The new result is an exact finite-state replacement of the previous enumeration method through the complete admissible depth-41 range.

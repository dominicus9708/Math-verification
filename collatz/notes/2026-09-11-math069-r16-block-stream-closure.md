# MATH-069 — complete closure of the r=16 multi-paid layer

Date: 2026-09-11

Status: `EXACT r=16 CLOSURE / r>=16 CLOSED / 2<=r<=15 OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- MATH-068 closes `r=17`; MATH-065 closes every `r>=18`.

## 1. Exact r=16 workload

Applying the unchanged MATH-065 phase/address and dyadic branch-and-bound construction at paid count `r=16` gives

\[
\boxed{
1061
=229\text{ cost-safe}
+557\text{ singleton-resolution}
+275\text{ critical}
}
\]

phase/address cells.

The exact branch search visits

\[
\boxed{37,173,746}
\]

prefix nodes and leaves

\[
\boxed{2,417,129}
\]

negative-candidate completed cylinders representing

\[
\boxed{213,006,896}
\]

ordinary target occurrences.

The largest completed cylinder has multiplicity `767077`.

As in MATH-065 through MATH-068, multiplicity is only a representation property.  A cylinder is not declared closed merely because it is a singleton or because it is large.

## 2. Large arithmetic-progression branch

Every completed target cylinder is an exact arithmetic progression

\[
P=\{a+b k:0\le k<m\},
\qquad b=3^Q.
\]

For `m>=1024` the MATH-066 exact parity-splitting AP continuation is efficient enough to carry the complete family without ordinary-target materialization.

The exact band results are:

| multiplicity | cylinders | target occurrences | AP transition nodes | maximum shortcut depth |
|---:|---:|---:|---:|---:|
| `1024..4095` | 18,952 | 40,013,695 | 88,717,314 | 307 |
| `4096..16383` | 4,200 | 37,228,529 | 68,451,866 | 348 |
| `16384..65535` | 1,197 | 31,243,267 | 48,270,079 | 316 |
| `>=65536` | 454 | 52,065,578 | 66,651,246 | 335 |

Thus

\[
\boxed{24,803}
\]

large cylinders representing

\[
\boxed{160,551,069}
\]

target occurrences all reach the frozen floor `2^71`.

The maximum exact family depth in this branch is

\[
\boxed{348}.
\]

## 3. Small branch: m<=64

The small branch contains

\[
\boxed{2,238,071}
\]

cylinders representing

\[
\boxed{12,763,331}
\]

ordinary occurrences.

Use the universal exact 8-step shortcut block determined by `n mod 256`,

\[
T^8(n)=\frac{3^{q(r)}n+C(r)}{256}.
\]

Because every AP step `b` is odd, splitting the AP parameter by `k mod256` preserves exact ordinary-integer lineage.

After one block,

\[
\boxed{8,125,293}
\]

occurrences have already reached `<=2^71`.

The remaining

\[
\boxed{4,638,038}
\]

states are singleton ordinary integers and are passed to the streaming terminal verifier.

## 4. Medium branch: 65<=m<=1023

This branch contains

\[
\boxed{154,255}
\]

cylinders representing

\[
\boxed{39,692,496}
\]

occurrences.

The first exact 8-step block closes

\[
\boxed{25,273,451}
\]

occurrences.
Every surviving AP then has multiplicity at most

\[
\boxed{4}.
\]

The second 8-step block closes another

\[
\boxed{7,290,855}
\]

occurrences, leaving

\[
\boxed{7,128,190}
\]

singleton occurrences.

Thus the complete unresolved ordinary tail after the block handoff is

\[
4,638,038+7,128,190
=\boxed{11,766,228}
\]

singleton occurrences.

## 5. Constant-memory same-integer terminal audit

The Python generator writes the 11,766,228 singleton occurrences as unsigned 128-bit ordinary integers.  The companion verifier reads them sequentially and keeps no global duplicate table.

For each current residue modulo `256`, the verifier stores not only the affine 8-step block

\[
T^8(n)=\frac{A_r n+C_r}{256},
\]

but also the exact threshold for reaching `<=2^71` at any intermediate one of the next eight shortcut steps.  Therefore a descent hidden inside a block cannot be skipped.

The exact streaming result is

\[
\boxed{
11,766,228\text{ read}
=11,766,228\text{ closed},
}
\]

with

\[
\boxed{0\text{ failures},\qquad0\text{ arithmetic overflows}.}
\]

The maximum additional distance after the handoff is

\[
\boxed{331}
\]

shortcut steps.

A conservative bound from the original medium target is therefore

\[
16+331=347.
\]

The large-AP branch has maximum depth 348, so a single safe layer-wide bound is

\[
\boxed{348}
\]

additional shortcut steps from a completed negative-candidate `r=16` target to the frozen floor.

## 6. Verdict

All three exhaustive multiplicity regions are closed:

\[
\boxed{
\begin{array}{ll}
m\le64 & \text{one block + streaming singleton descent},\\
65\le m\le1023 & \text{two blocks + streaming singleton descent},\\
m\ge1024 & \text{exact AP-family descent}.
\end{array}
}
\]

Hence

\[
\boxed{r=16\text{ is completely closed}.}
\]

Combining MATH-065, MATH-068 and MATH-069,

\[
\boxed{r\ge16\text{ is closed}.}
\]

The detailed multi-paid frontier is now

\[
\boxed{2\le r\le15.}
\]

## 7. DSD audit

### SAFE

1. MATH-065 exact phase and source-address lineage is unchanged.
2. Every negative completed cylinder is assigned to exactly one of the three multiplicity regions.
3. Large AP continuation preserves every ordinary member under exact parity splitting.
4. The 8-step block is an exact affine identity on each residue modulo 256.
5. Floor trimming removes only ordinary values already `<=2^71`.
6. Small and medium block survivors are explicit singleton ordinary integers.
7. The terminal verifier is streaming only; lack of deduplication cannot remove a state.
8. Intermediate-step floor thresholds prevent an 8-step block from hiding a descent.

### OPEN

- `2<=r<=15` multi-paid layers;
- the mixed one-paid / remaining multi-paid Bellman problem;
- first universal Farey cell emptiness;
- later Farey cells;
- the full Collatz conjecture.

### PROHIBITED UPGRADES

- `r>=16` closure `=>` all multi-paid clusters are closed;
- the finite first-cell layer audit `=>` universal Collatz descent;
- streaming terminal verification `=>` a proof for integers not represented by the certified cylinders.

## 8. Methodological consequence

MATH-069 removes the memory bottleneck exposed while developing MATH-068.  The proof-facing state does not require a giant set of unique ordinary integers.  Once exact family resolution reaches singleton states, they may be verified as a stream because subsequent dynamics are a deterministic function of the integer alone.

The next layer should therefore start at

\[
\boxed{r=15}
\]

using the same three-stage architecture:

1. exact reduced-cost cylinder generation;
2. AP/block resolution by multiplicity and low-bit structure;
3. constant-memory terminal continuation.

## Reproducibility

Python generator:

`collatz/src/2026_09_11_math069_r16_block_stream_generator.py`

Constant-memory terminal verifier:

`collatz/src/2026_09_11_math069_u128_stream_descent.cpp`

# R1 G13 entrance E>=13 and 952-bit upgrade

Date: 2026-08-16

Status: **exact finite current-core upgrade**.  It closes the remaining `E=12` pre-gate layer, strengthens the present R1 theorem to `e_1539>=13`, and sharpens the internal G13 finite-natural entrance bound from `2^954` to `2^952`.  It does not eliminate R1 and does not prove Collatz.

## 1. Previous handoff

The preceding sparse-even theorem established for every unresolved current `m=44`, `V_33` R1 start

\[
\boxed{e_{1539}\ge12}
\]

and therefore

\[
\boxed{x_{1539}<2^{954}}.
\]

Its exact run-cover calculation also showed

\[
\boxed{e_{1539}=12\Longrightarrow e_{73}\le8.}
\]

The first-73 layers containing at most seven even positions had already been closed by exact enumeration, Cantor intersection, and first-descent certificates.  Consequently the only remaining `E=12` case was the first-73 layer with exactly eight zeros.

## 2. Reduction of the eight-zero layer

A current `m=44` start has

\[
N\equiv3\pmod4.
\]

Hence its first two accelerated Collatz parity bits are necessarily

\[
11.
\]

Therefore, in an eight-zero length-73 parity word, the first zero position is at least two.  The complete relevant layer has

\[
\boxed{10,639,125,640}
\]

parity vectors.

For each vector the certificate performs only exact integer operations:

1. compute the affine correction modulo `2^73`;
2. recover the unique canonical ordinary start modulo `2^73`;
3. test the current numerical interval;
4. test the exact `m=44` ternary-Cantor digit condition;
5. for every core intersection, follow the actual accelerated Collatz orbit and record first descent.

The computation was independently partitioned by first-zero position into three large shards:

\[
2\ldots5,\qquad6\ldots10,\qquad11\ldots65.
\]

Their exact counts are

\[
\begin{array}{c|r|r|r|r}
\text{first zero}&\text{parity vectors}&\text{numeric range}&\text{core matches}&\max\tau_<\\\hline
2\ldots5&4,116,764,080&858,474,402&22&284\\
6\ldots10&3,141,263,015&655,029,046&24&384\\
11\ldots65&3,381,098,545&705,045,932&27&279
\end{array}
\]

Summing gives

\[
\boxed{73\text{ current-core intersections}.}
\]

Every one of the 73 has an explicit first descent.  The global maximum is

\[
\boxed{\max\tau_<=384.}
\]

The minimum number of even steps among these 73 actual trajectories by time 1539 is

\[
\boxed{708,}
\]

far outside the sparse `E=12` sector.

Thus the eight-zero layer contains no unresolved R1 start.

## 3. Exact pre-gate even-count upgrade

The cases `e_73<=7` were already closed, and Section 2 closes the only remaining `e_73=8` possibility compatible with total `e_1539=12`.

Therefore

\[
\boxed{e_{1539}\ge13.}
\]

Equivalently,

\[
\boxed{q_{1539}\le1526.}
\]

With the upper mechanical count

\[
\lceil1539\log_3 2\rceil=972,
\]

the entrance surplus obeys

\[
\boxed{s_0=q_{1539}-972\le554.}
\]

This is a current-core finite theorem, not a universal statement about all positive starts.

## 4. Exact 952-bit G13 entrance bound

Use the same exact relaxed `U=x+1` run optimizer.

For fixed total even counts, the exact maximal relaxed endpoint has floor binary logarithm

\[
\begin{array}{c|rrrrrrrrr}
E&12&13&14&15&16&17&18&19&20\\\hline
\lfloor\log_2 U_{1539}^{\max}\rfloor
&953&951&950&948&947&945&944&942&940.
\end{array}
\]

The newly certified input `E>=13` therefore gives

\[
U_{1539}<2^{952}
\]

for `13<=E<=20`.  For `E>=21`, the coarser per-step product bound already lies below the same threshold and decreases with every additional even step.

Hence every unresolved current R1 start satisfies

\[
\boxed{x_{1539}<2^{952}.}
\]

## 5. Strengthened G13 natural cut

Since

\[
952=50\cdot19+2,
\]

the 19-bit canonical lift chunks at the G13 entrance satisfy

\[
\boxed{t_{50}<4,}
\]

and every later chunk must vanish:

\[
\boxed{t_b=0\qquad(b\ge51).}
\]

Thus the upper

\[
\boxed{20026-952=19074}
\]

bits of a realizable G13 canonical start address are forced to zero.

This supersedes the earlier `t_50<16` / `2^954` cut.

## 6. Diagnostic effect on the G13 relation search

Repeating the same finite beam diagnostic that had produced many bounded-credit ordinary G13 candidates under the `2^954` cut gives a qualitatively different picture after imposing `x<2^952`.

For a representative search with population 1200, sample width 80, and seed 20:

- only twelve natural prefix candidates survive the cut;
- none reaches a positive failure-time credit `<=397`.

This is **not** an exhaustive theorem because the forward candidate set is beam-generated.  It is recorded only as evidence that the two-bit entrance improvement materially reduces the surviving gate freedom.

## 7. Next exact sparse layer

The run-cover certificate now gives

\[
\boxed{e_{1539}=13\Longrightarrow e_{73}\le9.}
\]

Thus proving `e_1539>=14` by the same direct route would require closing the first-73 nine-zero layer.  Its raw size is

\[
\binom{73}{9}=97,082,021,465,
\]

which is no longer attractive for blind enumeration.

The more efficient next step is therefore to intersect the `E=13` pre-gate reverse envelope directly with the G13 finite-natural relation state, rather than enumerate all nine-zero parity vectors independently.

## Reproducibility

Eight-zero complete certificate:

`collatz/src/r1_first73_sparse_even_k8_parallel_certificate.cpp`

Upgraded exact run bound:

`collatz/src/r1_g13_entry_952bit_bound_certificate.py`

# R1 G13 entrance sparse-even bound and 954-bit natural cut

Date: 2026-08-16

Status: **exact current-core finite certificate + exact relaxed run-length bound**.  It strengthens the internal G13 entrance bound from `2^973` to `2^954` for the present `m=44`, `V_33` R1 branch.  It does not eliminate R1 and does not prove Collatz.

## 1. Current ordinary start range

The remaining recursively-sufficient `m=44` branch is

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\},
\]

above the certified floor

\[
V_{33}=4(3^{44}+3^{33})+2.
\]

Hence

\[
N_0=V_{33}+1
=3,939,105,844,976,711,153,619,
\]

and

\[
N\le N_{\max}=6\cdot3^{44}+1
=5,908,625,413,101,667,397,287<2^{73}.
\]

The internal G13 gate begins after

\[
\boxed{1539=81\cdot19}
\]

accelerated Collatz steps.

Write `e_1539` for the number of even steps in this pre-gate prefix.

## 2. Exact run-length relaxation

Put

\[
U=x+1.
\]

On an odd step,

\[
U\mapsto\frac32U
\]

exactly.  If `r` odd steps occur consecutively, integrality of each intermediate odd state requires

\[
\boxed{2^r\mid U,}
\]

so necessarily

\[
\boxed{r\le\lfloor\log_2U\rfloor.}
\]

An even step gives

\[
U\mapsto\frac{U+1}{2}.
\]

For the relaxed optimization in which only the run cap is retained, moving an allowed odd step to the left of an even step increases the resulting `U`:

\[
\boxed{O(E(U))-E(O(U))=\frac14>0.}
\]

Therefore, for fixed total time and fixed number of even steps, the maximal relaxed endpoint is obtained greedily: take the longest currently allowed odd run, then one even step, and repeat.

The exact `Fraction` certificate reproduces the endpoint floor-log table

\[
\begin{array}{c|rrrrrrrrrrrrrr}
E&5&6&7&8&9&10&11&12&13&14&15&16&17&18\\\hline
\lfloor\log_2U_{1539}^{\max}\rfloor
&964&963&961&959&958&956&955&953&951&950&948&947&945&944.
\end{array}
\]

For `E>=19`, the coarser stepwise bounds

\[
U_{\rm odd}=\frac32U,
\qquad
U_{\rm even}=\frac{U+1}{2}\le\frac34U
\]

already give an endpoint smaller than the `E=12` target bound and decrease with `E`.

## 3. Why very small total even counts force sparse first-73 prefixes

At time 73, after `k` even steps, the same coarse bound gives

\[
U_{73}\le (N_{\max}+1)\left(\frac32\right)^{73}2^{-k}.
\]

From this upper state, apply the greedy run-cover relaxation to the remaining 1466 steps.  Exact rational arithmetic gives

\[
\boxed{
\begin{array}{c|rrrrrrrr}
E_{1539}&5&6&7&8&9&10&11&12\\\hline
\max e_{73}&1&2&3&4&5&6&7&8.
\end{array}
}
\]

In particular,

\[
E_{1539}\le11\Longrightarrow e_{73}\le7.
\]

Thus total pre-gate even count at most eleven reduces to the finite first-73 layers with zero count at most seven.

## 4. Complete first-73 audit for zero count at most five

Every length-73 parity vector determines one exact ordinary residue modulo `2^73`.  Since the current starts already satisfy `N<2^73`, this is the ordinary start itself.

Enumerate every 73-bit parity vector containing at most five zeros:

\[
\boxed{
\sum_{k=0}^{5}\binom{73}{k}=16,173,662.
}
\]

For each vector the certificate reconstructs its exact canonical start, computes the exact state after the prescribed 73 bits, and follows the actual accelerated Collatz map.

Result:

\[
\boxed{0}
\]

starts retain at most twelve even events through time 1539.  Every one encounters its thirteenth even step by time 124.

This is stronger than required for the `E<=11` exclusion.

## 5. Exact zero-count-six Cantor intersection

The exact six-zero layer contains

\[
\binom{73}{6}=170,230,452
\]

parity vectors.

Intersecting their canonical starts with the current `m=44` Cantor core leaves exactly one integer:

\[
\boxed{N=5,738,710,870,301,394,599,935.}
\]

Its actual orbit has

\[
\boxed{\tau_<=311}
\]

and therefore cannot be a minimal counterexample.  It has 731 even steps by time 1539.

## 6. Exact zero-count-seven Cantor intersection

The seven-zero layer contains

\[
\binom{73}{7}=1,629,348,612
\]

parity vectors.

The full layer was partitioned by the first zero position.  Exact intersection with the current `m=44` core leaves twelve ordinary starts in total.  Every one has an explicit first descent; the largest depth is

\[
\boxed{\max\tau_<=462.}
\]

Their minimum even count by time 1539 is 715.

Hence no surviving current-core R1 start can belong to the seven-zero layer either.

## 7. Current-core pre-gate even theorem

Sections 3--6 exhaust every possibility with `e_1539<=11`.  Therefore every remaining current `m=44` R1 candidate obeys

\[
\boxed{e_{1539}\ge12.}
\]

Equivalently, if `q_1539` is the odd-step count,

\[
\boxed{q_{1539}\le1527.}
\]

Relative to the upper mechanical/Beatty boundary count

\[
\lceil1539\log_3 2\rceil=972,
\]

the G13 entrance surplus satisfies

\[
\boxed{s_0=q_{1539}-972\le555.}
\]

This is a theorem for the present current-core branch, not for arbitrary positive starts.

## 8. Strengthened G13 entrance size bound

Feed the certified input `e_1539>=12` into the exact relaxed run optimizer.

For `12<=E<=18`, every exact relaxed endpoint is below `2^954`; for `E>=19` the coarse product bound is already below the same threshold.  Hence

\[
\boxed{x_{1539}<2^{954}.}
\]

This supersedes the earlier universal `2^973` entrance bound.

## 9. Exact 19-bit natural-cut form

Write the G13 canonical ordinary start in 19-bit lift chunks

\[
\rho_{19m}=\sum_{b=0}^{m-1}t_b2^{19b},
\qquad 0\le t_b<2^{19}.
\]

Since

\[
954=50\cdot19+4,
\]

the finite-natural condition becomes

\[
\boxed{t_{50}<16,}
\]

and every later chunk must vanish:

\[
\boxed{t_b=0\qquad(b\ge51).}
\]

Equivalently, of the 20026 G13 dyadic address bits, the upper

\[
\boxed{20026-954=19072}
\]

bits must be zero.

After this cut, the G13 tail is no longer a free parity-word choice: it is the deterministic Collatz trajectory of one already-fixed ordinary integer.

## 10. Next finite layer

The same run-cover theorem gives

\[
e_{1539}=12\Longrightarrow e_{73}\le8.
\]

The layers through seven zeros are now closed.  Therefore an exact proof that `e_1539>=13` reduces to the single new eight-zero first-73 layer, together with the already closed lower layers.

The raw eight-zero layer has

\[
\binom{73}{8}=13,442,126,049
\]

vectors, so a new meet-in-the-middle or branch-bound intersection is preferable to another blind full enumeration.

## Reproducibility

- `collatz/src/r1_g13_entry_run_bound_certificate.py`
- `collatz/src/r1_first73_sparse_even_small_certificate.cpp`
- `collatz/src/r1_first73_sparse_even_cantor_layers.cpp`

Compile the last source with `-DSPARSE_K=6` or `-DSPARSE_K=7`; the first-zero range arguments permit independent shards of the seven-zero layer.

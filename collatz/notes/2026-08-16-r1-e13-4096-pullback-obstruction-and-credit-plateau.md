# R1 E=13: 4096 pullback obstruction and bounded-credit 3-adic plateau

Date: 2026-08-16

Status: **exact finite same-q pre-gate obstruction for the specific G13 entrance difference 4096 + exact labeled bounded-credit lift profile through `3^36`**.  The specific `4096` channel dies completely modulo `3^28`.  For the generic bounded set `1..397`, 150 credits are removed by `K=30`, but 247 credits persist through `K=36`; therefore terminal 3-adic refinement alone is not a universal proof mechanism.  This does not eliminate R1 and does not prove Collatz.

## 1. Direction correction

The previously constructed full G13 relation is

\[
\boxed{4096\longrightarrow1}
\]

when read forward from the G13 entrance to the G13 exit.

Therefore, if this **specific** relation is to be pulled farther left through the 1539-step pre-G13 segment, the right-boundary displacement entering the pre-gate pullback is

\[
\boxed{4096,}
\]

not a generic member of `1..397`.

The bounded-credit `1..397` calculations remain valid as a separate general relation-channel analysis, but they must not be substituted for the specific `4096` bridge without this distinction.

## 2. E=13 correction law

For one 1539-step path containing exactly 13 even events at positions

\[
0\le p_0<\cdots<p_{12}<1539,
\]

put

\[
\boxed{
C(P)=\sum_{j=0}^{12}2^{p_j}3^{1526-p_j+j}.
}
\]

Then, in `U=x+1` coordinates,

\[
\boxed{
2^{1539}U_T=3^{1526}U_0+C(P).
}
\]

For two same-`q` E=13 paths with original start difference `Delta` and G13 entrance difference `delta`, subtraction gives

\[
3^{1526}\Delta
=2^{1539}\delta+C(P')-C(P).
\]

Thus integrality requires

\[
\boxed{
C(P')-C(P)
\equiv-2^{1539}\delta
\pmod{3^{1526}}.
}
\]

Any contradiction modulo one finite power `3^K` is already sufficient to exclude that same-q pullback relation.

## 3. Terminal residue over-family

For the finite depths used here, exact run-cap upper bounds imply that the first five even-event ranks are too early to affect the low ternary digits.

The certified maxima are

\[
p_0\le72,\quad
p_1\le186,\quad
p_2\le365,\quad
p_3\le647,\quad
p_4\le1093.
\]

At `K=28`, the activation thresholds for those ranks are

\[
1499,1500,1501,1502,1503,
\]

so none can contribute modulo `3^K` for any `K<=28`.

Every possible low-`K` correction residue is therefore contained in a terminal active suffix beginning at some rank `j_0>=5`.  Write

\[
\boxed{
p_j=1526+j-(K-1)+b_j,}
\]

with

\[
0\le b_j\le K-1,
\qquad
b_j\le b_{j+1}.
\]

This is an exact over-family for the low-`K` correction residues: no ordinary E=13 correction residue is omitted.

## 4. Exact 4096 pullback collapse

Define `P_K(4096)` to be the set of ordered residue pairs in the terminal over-family satisfying

\[
c'-c\equiv-2^{1539}\cdot4096\pmod{3^K}.
\]

The complete `K=18` set has

\[
|S_{18}|=997,755
\]

residues and

\[
|P_{18}(4096)|=545.
\]

Instead of rebuilding the full residue set at each deeper `K`, lift only descendants of the previous pair endpoints.  Since every residue modulo `3^{K+1}` projects to one modulo `3^K`, this targeted Hensel lifting is exhaustive for the surviving pair set.

The exact counts are

\[
\boxed{
\begin{array}{c|r}
K&|P_K(4096)|\\\hline
18&545\\
19&204\\
20&158\\
21&83\\
22&42\\
23&20\\
24&4\\
25&2\\
26&2\\
27&2\\
28&0
\end{array}}
\]

Therefore

\[
\boxed{P_{28}(4096)=\varnothing.}
\]

Since a genuine same-q integer pullback would have to satisfy the congruence modulo every power up to `3^1526`, failure already modulo `3^28` proves:

\[
\boxed{
\text{No pair of ordinary E=13 pre-gate paths can have G13 entrance difference }4096.
}
\]

Equivalently, the specific G13 `4096 -> 1` relation cannot be pulled through the E=13 pre-gate segment as a same-q ordinary-integer predecessor relation.

## 5. Logical scope of the 4096 theorem

This result is strong but its role must be stated correctly.

The constructive G13 `4096 -> 1` witness proves that such a relation exists in the internal gate fibre.  It does **not** prove that every surviving R1 ordinary state is forced to possess that relation.

Therefore the new obstruction does **not** imply

\[
E=13\text{ is impossible}
\]

and does not eliminate R1 by itself.

It instead closes one proposed predecessor-construction channel:

\[
\boxed{
\text{G13 entrance credit }4096
\not\longleftarrow
\text{same-q E=13 ordinary pre-gate relation}.
}
\]

This also explains why the specific `4096` bridge should no longer be treated as the likely terminal route for transporting a smaller predecessor all the way back to the original start.

## 6. General bounded credits 1..397

Separately, label every same-q terminal residue pair by a credit

\[
1\le\delta\le397.
\]

At `K=18` all 397 credits are globally realizable somewhere in the terminal residue over-family.  The total number of labeled pair states is

\[
966,886.
\]

Targeted Hensel lifting gives the following exact profile:

\[
\boxed{
\begin{array}{c|r|r}
K&\text{labeled pair states}&\text{globally surviving credits}\\\hline
18&966,886&397\\
19&661,555&397\\
20&437,981&397\\
21&283,335&397\\
22&170,431&394\\
23&107,481&386\\
24&75,158&376\\
25&56,514&362\\
26&44,801&330\\
27&39,906&288\\
28&38,554&258\\
29&38,420&248\\
30&38,526&247\\
31&38,663&247\\
32&38,811&247\\
33&38,960&247\\
34&39,111&247\\
35&39,262&247\\
36&39,413&247
\end{array}}
\]

Thus by `K=30`, exactly

\[
\boxed{150}
\]

of the original 397 bounded credits are globally absent from the same-q terminal relation set.

## 7. Plateau is a negative strategic result

From `K=30` through `K=36`, the number of globally surviving credit labels remains

\[
\boxed{247.}
\]

Meanwhile the number of lifted pair states slowly increases:

\[
38,526,\ 38,663,\ 38,811,\ 38,960,\ 39,111,\ 39,262,\ 39,413.
\]

Therefore the naive extrapolation

> increasing the 3-adic resolution alone will automatically remove every bounded credit

is not supported and is structurally doubtful in this terminal quotient.

The terminal residue channel has performed a large exact subtraction, but the remaining 247 labels exhibit a stable lifting fibre over the tested range.

This is analogous to the earlier correction that scalar credit itself is recurrent rather than a well-founded proof rank: a stronger cross-channel condition is needed.

## 8. New intersection target

The correct next set is not all integers and not all 397 credits.  It is

\[
\boxed{
\mathcal C_{\mathrm{G13,entrance}}
\cap
\mathcal C_{\mathrm{pre},E=13}.
}
\]

Here

- `C_G13,entrance` is the set of entrance credits actually supplied or forced by the natural G13 same-state relation system;
- `C_pre,E=13` is the same-q pre-gate credit set that survives the exact 3-adic lift sieve.

The specific element `4096` is already known to lie outside the second set at depth 28.

Within the bounded test range `1..397`, 150 labels have also been removed globally, leaving a 247-label terminal plateau.

If the actual natural G13 entrance relation set can be shown to lie entirely in the removed side, then the E=13 relation channel closes.  If it intersects the 247 persistent labels, those intersection labels — rather than all parity words — become the only remaining proof obligations.

## 9. Relation to the natural 952-bit cut

The G13 ordinary entrance also satisfies

\[
X<2^{952}.
\]

After the first 51 19-bit lift chunks, the ordinary integer `X` is completely determined and all later lift chunks must vanish.

For every `K<=1526`, the actual pre-gate correction obeys

\[
\boxed{
C(P)\equiv2^{1539}(X+1)\pmod{3^K},
}
\]

because the original-root term `3^1526(N+1)` vanishes modulo `3^K`.

Thus the natural G13 transducer can be joined directly to the pre-gate 3-adic filter at the point where the 952-bit start has stabilized.  No reconstruction of the 13 event positions is required merely to obtain the actual correction residue.

This gives the next combined state:

\[
\boxed{
(\text{G13 natural lift state},
\ X\bmod3^K,
\ \text{entrance-credit relation label}).
}
\]

## Reproducibility

Specific `4096` obstruction:

`collatz/src/r1_e13_4096_pullback_obstruction.cpp`

General labeled bounded-credit lift sieve:

`collatz/src/r1_e13_bounded_credit_3adic_lift_sieve.cpp`

Earlier supporting files:

- `r1_e13_channel_formation_filter_certificate.py`;
- `r1_e13_high_prefix_attachment_oracle.py`;
- `r1_e13_terminal_3adic_sieve.cpp`;
- `g13_h1_4096_to_1_bridge_certificate.cpp`.

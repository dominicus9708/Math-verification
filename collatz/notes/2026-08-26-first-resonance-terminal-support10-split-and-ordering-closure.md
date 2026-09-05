# First global resonance: support-10 split and ordering closure at m=66

Date: 2026-08-26

Status: **exact finite theorem** in the repaired first-global-resonance branch. This note continues the compressed terminal Hensel ladder. It does not use the disputed ternary recursively-sufficient selector, repeated L7/L14 pullback, random sampling, floating point, or an independence assumption. It does **not** prove the Collatz conjecture.

## 1. Imported state

The previous certified ladder gives

\[
D_{\rm tail}(65)\ge10.
\]

Together with the independent early theorem

\[
D_{72}\ge11,
\]

this already implied \(r_*\ge21\).

The next task is to classify the equality layer

\[
D_{\rm tail}(65)=10.
\]

## 2. Exact 46/19 triangular split

For the final 65 odd ordinals, split the terminal coordinates into

- an early terminal block of 19 coordinates;
- the final 46 coordinates.

Because

\[
3^{65}=3^{46}3^{19}
\]

and every admissible ordinary endpoint satisfies \(y<3^{46}\), the last 46 coordinates determine the complete low block of the endpoint. The first 19 coordinates only have to cancel the high \(3^{19}\)-digit block.

Write

\[
p=\text{number of defects in the first 19 coordinates},
\qquad
s=10-p.
\]

The initial positive-run compression from the preceding note is applied in the first block. After normalizing its contribution, an initial run of length \(L\) occupies exactly two of the three residue classes modulo 3, with every lift in those classes represented.

The suffix is enumerated with the exact ordering recurrence and joined to the prefix through the high Hensel state.

The exact suffix leaf counts are

\[
\begin{array}{c|c|r|r}
p&s&\text{suffix leaves}&\text{join hits}\\\hline
0&10&234334166&0\\
1&9&88391047&0\\
2&8&28849080&0\\
3&7&8060208&1\\
4&6&1900479&0\\
5&5&370946&0\\
6&4&58342&0\\
7&3&7106&0\\
8&2&629&0
\end{array}
\]

Thus

\[
\boxed{361972003}
\]

exact suffix leaves reduce to exactly one compatible high/low Hensel join.

## 3. Unique compressed equality state

Reversing that one join gives a unique compressed support:

\[
\boxed{
\operatorname{supp}(\delta)
=(0,1,7,26,28,35,52,54,57,62).
}
\]

The unique high prefix state has

\[
L=2,
\qquad
h_{\rm initial}=7\pmod{3^2},
\]

one additional prefix defect

\[
\delta_7=1,
\]

and boundary displacement zero at the 19/46 split.

The suffix is uniquely

\[
(26,28,35,52,54,57,62),
\qquad
\delta=1
\]

at every listed coordinate.

The ordinary endpoint is

\[
\boxed{y=2556679481397564529951.}
\]

## 4. Exact triangular classes in the initial two-coordinate run

The initial run is visible through

\[
\delta_0\pmod2,
\qquad
\delta_1\pmod6.
\]

The unique compressed state \(h_{\rm initial}=7\pmod9\) has exactly two residue classes:

\[
\boxed{
(\delta_0\bmod2,\delta_1\bmod6)
=(0,3),\ (1,1).
}
\]

Hence the full support-10 equality layer at \(m=65\) consists of one compressed Hensel state and exactly two triangular residue classes.

## 5. Ordering closure at m=66

This is where the left-extension audit is stronger than endpoint congruence alone.

Suppose a support-10 state existed at \(m=66\). Since the final 65 coordinates already require at least ten defects,

\[
D_{\rm tail}(65)\ge10,
\]

the newly prepended coordinate must be mechanical, and the final-65 restriction must be one of the two equality classes above.

Both equality classes have the old \(t=0\) coordinate displaced. After prepending the new mechanical coordinate it becomes \(t=1\), preceded by

\[
\delta_0=0.
\]

But the exact new leading mechanical gap is

\[
\boxed{B_1-B_0=1.}
\]

The ordering recurrence therefore gives

\[
\delta_1
\le
\delta_0+(B_1-B_0)-1
=0.
\]

This contradicts the required positive displacement at the shifted old \(t=0\) coordinate.

Thus **neither support-10 equality class admits an ordered lift to \(m=66\)**, independently of any endpoint calculation.

Therefore

\[
\boxed{D_{\rm tail}(66)\ge11.}
\]

## 6. Combined first-resonance lower bound

The final-66 terminal support remains far beyond the first 72 positions, so it is disjoint from the independently certified early support

\[
D_{72}\ge11.
\]

Consequently every remaining hypothetical first-resonance candidate satisfies

\[
\boxed{r_*\ge11+11=22.}
\]

Using only the coarse correction charge greater than \(1/12\) per displaced ordinal,

\[
\boxed{
\frac{E}{3^{Q_0}}>\frac{22}{12}=\frac{11}{6}.
}
\]

The support statement is the primary result.

## 7. Audit correction to earlier left-extension wording

The same ordering check reveals that one earlier explanatory sentence was too weakly audited. The unique support-three class at \(m=50\) does **not** genuinely extend mechanically to \(m=51\): the new leading gap at \(m=51\) is also 1, so the shifted first positive displacement is immediately forbidden by ordering.

Therefore the stronger intermediate statement is already

\[
\boxed{D_{\rm tail}(51)\ge4.}
\]

The previously stated \(D_{\rm tail}(52)\ge4\) theorem remains valid; only the description of the intermediate extension mechanism needs correction.

All future left-extension steps should be audited in this order:

1. support restriction;
2. ordering at the newly exposed boundary;
3. only then endpoint/Hensel congruence.

## 8. DSD audit interpretation

The gain here is not a new independent descriptor. The same terminal transport state is being refined simultaneously in two channels:

\[
\text{support count}
\quad+\quad
\text{3-adic endpoint address}
\quad+\quad
\text{ordinal ordering}.
\]

The support-10 equality survives the endpoint address at \(m=65\) but is destroyed one step later by the ordering channel before any new endpoint computation is needed.

The current two-ended first-resonance state is therefore

\[
\boxed{
D_{72}\ge11
\;\big|\;
\text{Beatty transport bridge}
\;\big|\;
D_{\rm tail}(66)\ge11.
}
\]

Companion exact certificate:

`collatz/src/first_resonance_terminal_support10_split_certificate.cpp`.

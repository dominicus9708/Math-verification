# R1 E=13 channel-conditioned formation filter

Date: 2026-08-16

Status: **exact finite set-level strengthening of the pre-G13 formation bridge**.  It combines the `E=13` event-position composition law with the already certified six first-defect channels and the depth-27/Hensel necessary masses.  It reduces the possible high-prefix contact fraction to less than `1.93e-8` of the full `E=13` entrance band.  This is not yet an emptiness theorem for the complete natural G13 relation set and does not prove Collatz.

## 1. Inputs

The current isolated R1 branch has already been reduced to

\[
e_{1539}\ge13,
\qquad
x_{1539}<2^{952}.
\]

This note studies the next boundary layer

\[
\boxed{E=e_{1539}=13.}
\]

The surviving first-defect positions are exactly

\[
\boxed{p\in\{2,5,8,10,13,16\}.}
\]

The first mismatch is always mechanical `0 -> 1`, and before that mismatch the actual parity word equals the mechanical word.  Therefore the mechanical zero positions before the chosen defect are fixed actual even events.

The already-certified necessary current-core masses after the depth-27 Hensel intersection are

\[
\begin{array}{c|r}
p&\text{necessary Cantor mass}\\\hline
2&456,566,092,589\\
5&80,911,487,383\\
8&14,667,776,602\\
10&3,349,620,432\\
13&615,721,246\\
16&111,791,167
\end{array}
\]

where the `p=16` count includes the later targeted low-ternary reduction.

## 2. Exact future-cover condition

Use

\[
U=x+1.
\]

An odd accelerated step is

\[
U\mapsto\frac{3U}{2},
\]

and an even step is

\[
U\mapsto\frac{U+1}{2}.
\]

An odd run of length `r` requires

\[
\boxed{r\le\lfloor\log_2U\rfloor.}
\]

Moreover

\[
O(E(U))-E(O(U))=\frac14>0.
\]

Hence, for fixed step and even counts, moving odd steps as far left as the run cap permits maximizes the endpoint.  Repeating the longest admissible odd run before each remaining even event also maximizes the number of future steps that can be covered with that even budget.

This gives an exact relaxed necessary test: if even the endpoint-maximizing prefix followed by the maximal-cover suffix cannot reach step 1539, the proposed event position is impossible for every ordinary trajectory in the current numerical range.

## 3. Necessary positions of the 13 even events

Let

\[
0\le p_0<p_1<\cdots<p_{12}<1539
\]

be the ordered even-event positions.

The current core satisfies `N=3 mod 4`, so the first two accelerated bits are `11`.  Applying the exact prefix-max / suffix-cover test gives

\[
\boxed{
(p_0,\ldots,p_{12})
\ge
(2,3,4,5,6,7,8,9,66,164,317,558,938)
}
\]

coordinate-wise.

Thus the ninth even event cannot occur before position 66, the tenth before 164, the eleventh before 317, the twelfth before 558, and the thirteenth before 938.

This is substantially stronger than treating the 13 event positions as an arbitrary subset of 1539 time slots.

## 4. Generic correction improvement

The pre-G13 formation correction is

\[
\varepsilon_{13}
=
\sum_{j=0}^{12}
3^j\left(\frac23\right)^{p_j}.
\]

Using only `p_j>=j+2` gave the earlier bound

\[
\varepsilon_{13}\le\frac{32764}{9}>3640.
\]

Using the new coordinate-wise future-cover bounds gives instead

\[
\boxed{\varepsilon_{13}<114.}
\]

Therefore one fixed ordinary G13 entrance `X` has at most 114 compatible integer roots in the generic `E=13` layer, before the first-defect channel is used.

For the high-prefix factorization

\[
X+1=h2^{879}+\ell,
\qquad
\lambda=\frac{2^{2418}}{3^{1526}}<1,
\]

a single current-core root can touch at most

\[
\boxed{180}
\]

high-prefix values `h` under this generic strengthened bound, improving the previous cap 5725.

## 5. First-defect conditioning

Let the first mismatch be at one of the six surviving positions.

Before the mismatch the candidate equals the mechanical word.  At the mismatch itself a mechanical zero is changed to an actual odd bit.  Hence the early even-event positions are partly fixed.

Combining those fixed positions with the future-cover lower bounds gives the following exact correction and root-window caps:

\[
\boxed{
\begin{array}{c|c|c}
\text{first defect }p
&\text{integer roots per fixed }X
&\text{high prefixes per fixed root}\\\hline
2&76&120\\
5&34&55\\
8&16&26\\
10&11&19\\
13&6&11\\
16&4&7
\end{array}
}
\]

The last channel is especially rigid: if the first mismatch is delayed to bit 16, a fixed `E=13` G13 entrance has at most four possible ordinary roots.

## 6. Set-level aggregation

The exact `E=13` entrance calculation gives the 73-bit high-prefix band

\[
h_{\min}\le h\le h_{\max}
\]

with cardinality

\[
\boxed{
|\mathcal H_{13}|
=3,096,460,089,936,865,692,636.
}
\]

For each first-defect channel, multiply its necessary current-core mass by its channel-specific high-prefix cap.  Summing gives

\[
\boxed{
|\mathcal H_{13}^{\rm compatible}|
\le59,690,623,368,480.
}
\]

No disjointness assumption is used; this is a plain union bound, hence safe even when high-prefix intervals from different roots overlap.

Therefore

\[
\boxed{
\frac{|\mathcal H_{13}^{\rm compatible}|}{|\mathcal H_{13}|}
<\frac{193}{10^{10}}
<1.93\times10^{-8}.
}
\]

As a percentage,

\[
\boxed{<0.00000193\%}
\]

of the complete `E=13` high-prefix band can still touch the current necessary R1 core.

Equivalently the set-level subtraction already removes more than

\[
\boxed{99.99999807\%}
\]

of the 73-bit entrance-prefix band before the full natural G13 relation is imposed.

## 7. Integerized event-position address

The formation identity can also be written without rational corrections:

\[
\boxed{
2^{1539}(X+1)-3^{1526}(N+1)
=
\sum_{j=0}^{12}
2^{p_j}3^{1526-p_j+j}.
}
\]

Every exponent on the right is nonnegative because `p_j<=1538` and `j<=12`.

The smallest dyadic exponent occurs uniquely at `p_0`, so

\[
\boxed{
v_2\!\left(
2^{1539}(X+1)-3^{1526}(N+1)
\right)=p_0.
}
\]

After subtracting the first term, the next 2-adic valuation reveals `p_1`, and so on.  Thus the event-position set is not merely a bounded error term; it is an ordered 2-adic formation address encoded in the exact attachment difference.

This provides an additional route for future channel-wise congruence filtering.

## 8. Attachment-oracle consequence

The full 879 low entrance bits no longer have to be stored by a G13 search merely to test pre-gate compatibility.

A G13 natural-state generator can expose only

\[
\boxed{h=\lfloor(X+1)/2^{879}\rfloor.}
\]

For one proposed `h`, the strengthened formation bounds place every possible original start in an interval containing only on the order of tens of ordinary integers; channel-wise the exact caps are `76,34,16,11,6,4` per fixed entrance.

Each surviving integer can then be checked exactly for

1. current `m=44` ternary-core membership;
2. the six allowed first-defect channels;
3. total pre-gate even count `E=13`;
4. absence of first descent;
5. its actual time-1539 entrance `X` and high prefix `h`.

Thus the next computational proof object is

\[
\boxed{
\text{G13 relation state}
\longrightarrow
73\text{-bit }h
\longrightarrow
\text{tiny exact pre-gate attachment set}.
}
\]

The large first-73 nine-zero enumeration is no longer the primary route.

## 9. Remaining target

The unresolved intersection is now

\[
\boxed{
\mathcal G_{\rm nat}^{(952)}
\cap
\mathcal H_{13}^{\rm compatible}.
}
\]

The new theorem proves that the second set occupies less than `1.93e-8` of the full high-prefix band.  The next justified step is therefore to make the finite-natural G13 relation transducer emit the 73-bit high prefix and apply the attachment oracle immediately, instead of retaining a large unconstrained beam of ordinary G13 starts.

## Reproducibility

Companion exact certificate:

`collatz/src/r1_e13_channel_formation_filter_certificate.py`

Required prior certificates/notes:

- `r1_g13_entry_952bit_bound_certificate.py`;
- `r1_pregate_even_position_formation_bridge_certificate.py`;
- `2026-08-14-r1-first-defect-channel-reduction.md`.

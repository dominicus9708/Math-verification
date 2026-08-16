# R1 E=13 gate-pair rigidity

Date: 2026-08-16

Status: **exact conditional pair-attachment theorem**.  It applies to a `4096`-separated G13 entrance pair inside the current `E=13` entrance band.  It proves even-count rigidity and, if both entrances admit current `m=44` core preimages, collapses the pair difference to the low five ternary selectors.  It does not assert that the alternate entrance must admit such a preimage and does not prove Collatz.

## 1. Entrance band

The exact current `E=13` pre-G13 theorem places the ordinary G13 entrance in a 952-bit band

\[
X_{13}^{\min}\le X\le X_{13}^{\max}.
\]

The G13 credit relation naturally compares an entrance with

\[
X'=X-4096.
\]

Because `4096` is negligible on the normalized pre-gate scale, the pair may be treated inside the enlarged band

\[
X_{13}^{\min}-4096\le X'\le X\le X_{13}^{\max}.
\]

## 2. Even-count rigidity

For a fixed entrance `X` and total pre-gate even count `E`, put

\[
Y_E(X)=\frac{2^{1539}(X+1)}{3^{1539-E}}.
\]

A current-core root satisfies

\[
N+1=Y_E(X)-\varepsilon_E,
\qquad
\varepsilon_E>0.
\]

The mandatory first two odd accelerated bits give

\[
\varepsilon_E\le\frac49(2^E-1).
\]

At the largest pair entrance, the `E=12` coordinate already satisfies

\[
Y_{12}(X)-1<N_0.
\]

Hence every `E<=12` attachment lies below the current R1 numerical floor.

At the smallest pair entrance, even after subtracting the maximal correction,

\[
Y_{14}(X')-1-\frac49(2^{14}-1)>N_{\max}.
\]

The lower bound increases for all `E>14`, because multiplying the normalized coordinate by three dominates the doubling of the correction bound.

Therefore

\[
\boxed{
\text{any current-window preimage of }X\text{ or }X-4096
\text{ must have }E=13.
}
\]

This is stronger than treating the alternate G13 entrance as a separate unknown sparse-even layer.

## 3. Root displacement

For `E=13`, changing the entrance by 4096 changes the normalized root coordinate by

\[
\Delta_Y
=
4096\frac{2^{1539}}{3^{1526}}.
\]

Exact integer comparison gives

\[
\boxed{0<\Delta_Y<1.}
\]

The strengthened run-feasibility theorem gives, for every current-core `E=13` attachment,

\[
0<\varepsilon_{13}<114.
\]

Hence, if both members of the entrance pair have current-core roots `N,N'`, then

\[
N-N'
=
\Delta_Y-\varepsilon+\varepsilon'.
\]

Therefore

\[
\boxed{|N-N'|<115.}
\]

## 4. Ternary-fibre collapse

Current `m=44` roots have the form

\[
N=4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

Suppose two such roots first differ at the highest selector index `m`.  The smallest possible absolute difference is obtained by opposing all lower selectors:

\[
|N-N'|
\ge
4\left(3^m-\sum_{i=0}^{m-1}3^i\right)
=2(3^m+1).
\]

At `m=5`,

\[
2(3^5+1)=488.
\]

Thus the bound `|N-N'|<115` rules out every highest differing selector `m>=5`.

Consequently

\[
\boxed{
a_i=a_i'\qquad(5\le i\le43).
}
\]

Only

\[
\boxed{(a_0,\ldots,a_4)\in\{0,1\}^5}
\]

may differ.

So a hypothetical double attachment of the G13 `4096` pair is no longer a pair of arbitrary members of a `2^44` Cantor core.  It lies in one common high-39-trit fibre with only 32 low local states.

## 5. Relation to the high-prefix attachment oracle

The companion `h` oracle already reduces one proposed G13 high prefix to at most 115 ordinary integers and then verifies the exact 1539-step attachment.

The present theorem adds a second layer: if the G13 relation search ever requires both `X` and `X-4096` to attach to the current core, the two oracle roots must be searched only inside one common high selector fibre and 32 low-five-trit states.

This is a direct cross-place composition:

\[
\boxed{
4096\text{ G13 entrance difference}
\Longrightarrow
E=13\text{ on both attachments}
\Longrightarrow
|N-N'|<115
\Longrightarrow
\text{same }a_5,\ldots,a_{43}.
}
\]

## Reproducibility

Exact certificate:

`collatz/src/r1_e13_gate_pair_rigidity_certificate.py`

Related files:

- `r1_e13_channel_formation_filter_certificate.py`;
- `r1_e13_high_prefix_attachment_oracle.py`;
- `r1_pregate_even_position_formation_bridge_certificate.py`.

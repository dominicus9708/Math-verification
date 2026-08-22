# Depth-28 query-renewal fixed topology and phase cocycle

Date: 2026-08-20

Status: **exact corollary of the existing depth-28 renewal-syndrome graph plus the new cyclic-query conjugacy.** This is not a proof of the Collatz conjecture.

## 1. Existing exact renewal topology

The existing depth-28 hard-language certificate gives the ordinary first-defect sizes

\[
\begin{array}{c|rrrrrrrrrr}
p&2&5&8&10&13&16&18&21&24&27\\\hline
|S_p|&1623807&286895&51825&11763&2151&404&100&20&5&1.
\end{array}
\]

Under the fixed immediate-return normalization, all ordinary renewal translations are exact except the two finite enlargements

\[
8\to10:\quad 14443=11763+2680,
\]

and

\[
16\to18:\quad125=100+25.
\]

The recursively exceptional topology is only

\[
\boxed{E_{10}(2680)\to E_{18}(25),\ E_{21}(5),}
\]

with all finite returns from \(E_{18}\) and \(E_{21}\) normalizing back into ordinary later hard states. The remaining no-return states carry positive height through the right edge of the 28-bit window.

## 2. Scaling by the ternary exponent does not change the topology

For the current ternary progression exponent \(a\), the sparse-tail cyclic-query coordinate multiplies every canonical residue by

\[
3^{-a}\pmod{2^{28}}.
\]

Since \(3^{-a}\) is a unit modulo \(2^{28}\), this is a permutation of the entire residue group.

Therefore

\[
\boxed{
|3^{-a}S_p|=|S_p|,
\qquad
|3^{-a}E_j|=|E_j|,
}
\]

and every exact set equality, inclusion, exceptional difference and graph edge is preserved bijectively.

Hence the depth-28 query-renewal graph has **the same finite topology for every ternary exponent \(a\)**. The exponent does not create new graph nodes; it only changes the additive labels on translated edges.

## 3. Query edge labels

For an ordinary immediate-return defect at position \(p\), the canonical-residue translation is

\[
d_p
=
2^p3^{-(q_{<p}+1)}
\pmod{2^{28}}.
\]

After the ternary scaling, the corresponding cyclic-query translation is

\[
\boxed{
\delta_p(a)
=
3^{-a}d_p
=
2^p3^{-(a+q_{<p}+1)}
\pmod{2^{28}}.
}
\]

The topology is fixed and the arithmetic dependence on \(a\) is therefore a label cocycle over that fixed graph.

## 4. Exact triangular valuation

Because powers of three are 2-adic units,

\[
\boxed{v_2(\delta_p(a))=p.}
\]

Thus an edge generated at defect position \(p\) leaves the first \(p\) query bits unchanged and acts only on higher bits.

This makes the renewal graph triangular in the dyadic filtration.

## 5. Exact phase periods

The factor \(2^p\) means only the unit modulo

\[
2^{28-p}
\]

matters. For \(28-p\ge3\),

\[
\operatorname{ord}_{2^{28-p}}(3)=2^{26-p}.
\]

Therefore the dependence of \(\delta_p(a)\) on \(a\) has exact period

\[
\boxed{2^{26-p}}
\]

for the ordinary range, with the expected small-modulus exceptions at the very end.

For the first-defect positions in the certified depth-28 graph:

\[
\begin{array}{c|r|r}
p&q_{<p}&\text{period in }a\\\hline
2&2&2^{24}=16{,}777{,}216\\
5&4&2^{21}=2{,}097{,}152\\
8&6&2^{18}=262{,}144\\
10&7&2^{16}=65{,}536\\
13&9&2^{13}=8{,}192\\
16&11&2^{10}=1{,}024\\
18&12&2^8=256\\
21&14&2^5=32\\
24&16&2^2=4\\
27&18&1
\end{array}
\]

Thus the later the renewal occurs, the less phase information is needed to determine its exact query translation.

## 6. Fixed-topology skew product

The depth-28 sparse-tail renewal can now be written as a finite graph skew product:

\[
\boxed{
(\text{renewal node},\ \xi,\ a)
\longmapsto
(\text{next node},\ \xi-\delta_e(a),\ a'),
}
\]

where

- the node graph is the already certified finite ordinary/exceptional renewal graph;
- \(\xi\in\mathbb Z/2^{28}\mathbb Z\) is the cyclic-successor query;
- \(\delta_e(a)\) is the edge translation;
- the phase sensitivity of an edge is triangular and decreases with its defect depth.

The apparent growth of the ternary syndrome therefore does not enlarge the **depth-28 renewal topology**. It enters only through a phase-labelled query cocycle over a fixed graph.

## 7. Relation to the asymptotic bottleneck

This does not yet prove that repeated windows force the cyclic-successor cost to grow. The query still ranges over \(2^{28}\) residues and the exponent phase changes between windows.

However the remaining problem is now more specific:

> prove that the fixed finite renewal graph, with triangular phase-labelled query translations and the known exceptional nodes, cannot keep returning the query to uniformly small cyclic-successor gaps at a positive exponential rate.

This is a finite-topology cocycle problem rather than an unrestricted growing-syndrome problem.

The previous 3-adic contraction theorem supplies the complementary fact that low ternary memory is continuously forgotten while this dyadic query cocycle evolves.

## 8. Certificate

`collatz/src/depth28_query_renewal_phase_period_certificate.py` verifies the exact valuation and phase periods for all certified first-defect positions.

The underlying graph topology and exceptional counts remain independently certified by

`collatz/src/m45_depth28_renewal_syndrome_graph_certificate.cpp`.

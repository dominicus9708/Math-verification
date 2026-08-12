# Defect-address causality and the late-lift bridge

Date: 2026-08-12

Status: **exact coordinate collapse + 2-adic causality theorem for the primitive upper-CF first-crossing branch**. It identifies the high-resolution defect cylinder coordinate with the strengthened renewal-address shift and proves that later defects cannot repair lower-resolution address bits. Combined with the local square-jump theorem, this turns repeated mechanical-square obstruction into a growing-resolution late-defect forcing statement. This does not prove Collatz.

## 1. One defect coordinate in four formalisms

Let the primitive upper-CF reference word be the Christoffel/mechanical extremizer with correction numerator

\[
R_{\rm chr},
\]

and let an actual first-crossing word have

\[
R=R_{\rm chr}-\mathcal E,
\qquad
\mathcal E>0.
\]

Put

\[
\eta:=\frac{\mathcal E}{3^H}.
\]

The skew/displacement-collapse theorem gives

\[
\boxed{\eta=\frac13\mathfrak D_H.}
\]

For target binary resolution `M`, define the 2-adic realization of the same rational coordinate by

\[
\boxed{
A_M:=[3^{-H}\mathcal E]_{2^M}.
}
\]

This is exactly the high-resolution defect residue used in the draft cylinder formalism.

At the strengthened renewal scale

\[
M=A+2,
\]

the renewal-address theorem gives

\[
\boxed{
\widehat\rho-\widehat\rho_{\rm chr}
\equiv A_{A+2}
\pmod{2^{A+2}}.
}
\]

Thus the following are one object in different embeddings/coordinates:

1. the real Christoffel correction loss `eta`;
2. the rotation-weighted defect `mathfrak D_H=3 eta`;
3. the high-resolution cylinder defect `A_M`;
4. the strengthened renewal-address displacement.

The distinction is only that `eta` is viewed as a positive real rational in the Archimedean channel and as the 2-adic rational `3^{-H} E` in the dyadic channel.

## 2. Exact additive channel formula

Let the actual zero-based odd positions be

\[
d_i,
\qquad 0\le i<H,
\]

and the mechanical cap positions be

\[
\kappa_i:=\lfloor i\gamma\rfloor,
\qquad
\gamma=\log_2 3.
\]

Write

\[
h_i:=\kappa_i-d_i\ge0.
\]

The high-resolution defect formula is

\[
\boxed{
A_M
\equiv
\sum_{i=0}^{H-1}
3^{-(i+1)}
\left(2^{\kappa_i}-2^{d_i}\right)
\pmod{2^M}.
}
\]

At a positive defect,

\[
2^{\kappa_i}-2^{d_i}
=2^{d_i}(2^{h_i}-1).
\]

Because `3^{-(i+1)}` and `2^{h_i}-1` are odd 2-adic units,

\[
\boxed{
v_2\!\left(
3^{-(i+1)}(2^{\kappa_i}-2^{d_i})
\right)=d_i.}
\]

Therefore the binary depth at which one defect channel first becomes visible is exactly its actual parity-time position.

## 3. No-retroactive-repair theorem

Fix a binary resolution `M`.

Every defect with

\[
d_i\ge M
\]

contributes a multiple of `2^M`, hence vanishes modulo `2^M`.

Therefore

\[
\boxed{
A_M
\equiv
\sum_{d_i<M}
3^{-(i+1)}(2^{\kappa_i}-2^{d_i})
\pmod{2^M}.}
\]

In words:

> the defect address below bit `M` is determined completely by defects that have already occurred before parity time `M`.

No later defect can change it.

This is an exact causality statement, not a probabilistic or asymptotic one.

## 4. Triangular resolution intervals

List the positive-defect odd indices in increasing actual parity position:

\[
d_{i_1}<d_{i_2}<\cdots<d_{i_r}.
\]

Define the partial 2-adic defect coordinate

\[
\mathcal A^{(j)}
:=
\sum_{\ell=1}^{j}
3^{-(i_\ell+1)}
\left(2^{\kappa_{i_\ell}}-2^{d_{i_\ell}}\right)
\in\mathbb Z_2.
\]

Then for every resolution satisfying

\[
d_{i_j}<M\le d_{i_{j+1}},
\]

one has

\[
\boxed{
A_M=[\mathcal A^{(j)}]_{2^M}.}
\]

Thus between two successive defects the high-resolution address is not being actively changed by new channels: one is merely revealing more binary digits of the same fixed partial 2-adic rational.

This gives a triangular decomposition of the sparse-defect problem by parity-time depth.

## 5. Small ordinary starts across all resolutions

Suppose the actual ordinary renewal start satisfies

\[
N<2^B.
\]

For every prefix resolution

\[
M\ge B
\]

that lies inside the same realized parity word, the canonical residue of the actual prefix is the same ordinary integer:

\[
\boxed{r_M=N.}
\]

Let `r_M^{chr}` be the canonical residue of the corresponding mechanical/Christoffel reference prefix. The defect translation formula gives

\[
\boxed{
N
\equiv
r_M^{chr}+A_M
\pmod{2^M}.}
\]

Therefore, on a resolution interval containing no new defect, the newly exposed high bits of the critical reference address must be cancelled exactly by the newly exposed high bits of one already-fixed partial defect rational `A`.

A later defect cannot repair a failure at any lower resolution because of Section 3.

## 6. Relation to a zero-defect mechanical run

Suppose

\[
h_q=h_{q+1}=\cdots=h_{q+m-1}=0.
\]

Throughout the corresponding parity interval the actual word and the critical mechanical word coincide exactly.

At the same time no new nonzero defect channel is inserted at those odd-event coordinates. Hence the address compatibility in Section 5 is being prolonged using only the 2-adic tail of the already accumulated partial defect coordinate.

The local-square jump theorem shows that this cannot continue through a critical recurrence window containing a supercritical square `u^2` once

\[
2^{|u|}
>
2\left(N+\frac H3\right).
\]

Consequently every sufficiently large such mechanical recurrence window must contain a new positive defect before the window closes.

This is precisely a late-defect / growing-resolution statement:

\[
\boxed{
\text{new critical address bits cannot remain compatible indefinitely without a new defect channel.}
}
\]

## 7. Polylogarithmic late-defect forcing

The preceding local-square theorem and the Sturmian recurrence formula already imply effective constants `C,D` such that the gap between successive positive-defect odd-event coordinates is at most

\[
\boxed{C(\log H)^D}
\]

in every sufficiently large primitive upper-CF first-crossing candidate.

The present causality theorem sharpens the interpretation:

- this is not merely a lower bound on combinatorial defect density;
- each such forced defect is the next available channel capable of changing the high-resolution dyadic renewal address;
- defects occurring after a failed resolution cannot retroactively restore the same small ordinary start.

Thus the `H/polylog(H)` defect floor is simultaneously an `H/polylog(H)` sequence of forced high-resolution address interventions.

## 8. Exact relation to the draft cylinder split

At a split depth `B` and target depth `K=B+m`, write

\[
A_K=U+2^B W,
\]

with

\[
0\le U<2^B,
\qquad
0\le W<2^m.
\]

Then:

- `U` is fixed entirely by defects with actual parity positions below `B`;
- defects after `B` cannot change `U`;
- `W` records the later address information needed to remain compatible with the fixed ordinary start and the future admissible suffix.

This is the same low/high cylinder decomposition already verified independently in the draft branch.

The local-square theorem now provides a deterministic reason why, in a near-mechanical candidate, the later part cannot remain indefinitely on the reference cylinder without producing further defect channels.

## 9. What this does not yet prove

The theorem does **not** imply that every newly forced defect produces an independent unbiased binary bit. An early defect term is an odd rational multiple of a power of two and has an infinite 2-adic tail, so it can influence arbitrarily high bits even though its lowest affected bit is fixed.

Therefore one cannot simply multiply `1/2` probabilities or count forced defects as independent bit constraints.

The remaining theorem must be deterministic:

> show that the 2-adic tails of the successively forced sparse defect channels cannot keep cancelling the critical reference address while the real defect coordinate remains inside the first-crossing shadow budget.

This is now a coupled Archimedean/2-adic small-ball problem for one exact rational coordinate, not a separate formation-versus-gap problem.

## 10. Next target

A useful next lemma would be a **multi-scale defect-tail separation theorem**.

For logarithmically growing resolutions

\[
B_0<B_1<\cdots<B_J,
\]

chosen across consecutive forced-defect windows, prove a deterministic lower bound on the number or size of address blocks for which

\[
[r_{B_j}^{chr}+A_{B_j}]_{2^{B_j}}
\]

can remain equal to the same small ordinary integer `N`.

The direct-sum/difference-set theorem from the draft branch gives exact no-collision structure for prefix-defect and future-suffix coordinates. The missing strengthening is quantitative separation from the small ordinary interval near zero.

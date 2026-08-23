# Stage 4 two-state core strengthened by simultaneous L7 and L14 maximality

Date: 2026-08-23

Status: **exact deterministic-language strengthening of the remaining H=0,1 core. This is not a proof of the Collatz conjecture.**

## 1. Why L14 can be imposed

The existing L7 predecessor argument says that a sufficiently large hypothetical minimal counterexample must use a full-Hensel residue-maximal representative in each aligned seven-step block. The same finite predecessor replacement applies at length 14 once the finite maximum predecessor credit is bounded.

Exact enumeration of the complete length-14 parity cube gives

\[
\boxed{5425\text{ full-Hensel residue classes}}
\]

with odd-count class numbers

\[
(1,2,6,18,54,162,462,1011,1405,1215,708,287,79,14,1),
\]

and maximum ordinary predecessor credit

\[
\boxed{\Delta_{14,\max}=2730.}
\]

Thus in the present large-minimal-counterexample regime the L14 maximality condition is also available.

## 2. Intersection with the existing L7 language

There are 69 L7 residue-maximal words. Two independent L7 blocks would allow

\[
69^2=4761
\]

length-14 concatenations.

Requiring the same 14-step word itself to be L14 residue-maximal leaves exactly

\[
\boxed{3620}
\]

words.

Hence the deterministic 14-step symbolic language loses an additional

\[
1-\frac{3620}{4761}\approx23.9656\%
\]

relative to L7 alone.

## 3. Exact H=0,1 recurrent transition

Use two aligned strengthened 14-step words per 28-step mechanical window. As before, any transition reaching H>=2 exits the unresolved core because the companion phase-coupled certificates already control every incoming H>=2.

Across all 29 genuine length-28 mechanical factors, the minimum unresolved row masses are

\[
\boxed{
M_0^{\min}=317231,
\qquad
M_1^{\min}=1192543.
}
\]

The full 336-step calculation then enumerates all 337 genuine Sturmian/mechanical factors and multiplies their twelve exact 28-step two-state matrices.

For the entrywise phase maximum \(P_{\max}^{(12)}\), the simple positive potential

\[
v=(1,2)^T
\]

satisfies the exact integer inequality

\[
\boxed{
150^{12}P_{\max}^{(12)}v<2^{336}v
}
\]

componentwise.

Therefore the strengthened unresolved language admits the sufficient average per-window amplification scale

\[
\boxed{K=150.}
\]

## 4. Remaining selector-loss targets

A state is automatic if its dyadic admissible mass already exceeds \(2^{28}/K\). Neither state does:

\[
150\cdot317231=47584650<2^{28},
\]

\[
150\cdot1192543=178881450<2^{28}.
\]

Thus same-address control is still required.

The sufficient conditioned-selector losses are

\[
\boxed{
1-\frac{150\cdot1192543}{2^{28}}
\approx33.3615\%\quad(H=1),
}
\]

and

\[
\boxed{
1-\frac{150\cdot317231}{2^{28}}
\approx82.2733\%\quad(H=0).
}
\]

Compared with L7 alone at K=117, the H=1 target improves only from about 34.03% to about 33.36%. The L14 condition is therefore rigorous and useful, but its extra deterministic deletion is largely paid for by a corresponding reduction in the dyadic baseline mass.

## 5. Strategic consequence

This calculation is a useful stopping criterion for the current branch of the argument:

\[
\boxed{
\text{longer local residue-maximality alone is unlikely to remove the final two-state obstruction cheaply.}
}
\]

The next proof-level target should therefore be H=1 same-word address transport itself, not merely another independent local-language filter. The required contraction is weak: it is enough to lose one third of conditioned selector mass on average at the H=1 recurrent boundary.

Exact verifier:

`collatz/src/stage4_two_state_l7_l14_twelve_window_certificate.py`.

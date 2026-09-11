# MATH-074 — resolution-overshoot Bellman localization

Date: 2026-09-12

Status: `EXACT AUXILIARY LEMMA / SYMBOLIC MULTI-SOURCE EDGES SAFE / TERMINAL SINGLETON OVERSHOOT OPEN`

- Collatz conjecture: `OPEN`.
- First universal Farey cell: `OPEN`.
- This note combines the MATH-061 exact dyadic cylinder resolution with the MATH-060 Bellman target.

## 1. Resolution height

Let an exact same-integer source cylinder contain exactly `M>=1` ordinary source anchors and define

\[
R(M)=\lceil\log_2 M\rceil,
\qquad R(1)=0.
\]

Appending an exact parity/macro factor of shortcut length `ell` adds one residue condition modulo `2^ell` to the current cylinder parameter. Hence any compatible child contains at most

\[
M'\le\left\lceil\frac{M}{2^\ell}\right\rceil
\]

ordinary source anchors.

Since `M<=2^R`,

\[
\left\lceil\frac{M}{2^\ell}\right\rceil
\le 2^{\max(0,R-\ell)}.
\]

Therefore

\[
\boxed{R'\le\max(0,R-\ell).}
\]

This is exact dyadic resolution, not a density statement.

## 2. Bellman potential

Use the MATH-060 target

\[
\lambda=\frac{19}{503}
\]

and define

\[
\boxed{H_R=-\lambda R.}
\]

For a legal macro edge with penalty `p>=0`,

\[
p-\lambda\ell+H_R'-H_R
=p-\lambda\ell+\lambda(R-R').
\]

Using the resolution inequality,

\[
R-R'\ge \min(R,\ell),
\]

so

\[
\boxed{
p-\lambda\ell+H_R'-H_R
\ge
p-\lambda(\ell-R)_+.
}
\]

## 3. Consequence

If

\[
\ell\le R,
\]

then

\[
\boxed{
p-\lambda\ell+H_R'-H_R\ge p\ge0.
}
\]

Thus every exact symbolic refinement whose length does not exceed the remaining source-resolution height is automatically Bellman-safe, independently of how small the local penalty is.

If

\[
\ell>R,
\]

then the compatible child has at most one source anchor. The only possible negative reduced cost is localized to the terminal overshoot

\[
\boxed{\lambda(\ell-R).}
\]

So the unresolved Bellman problem is not a general low-cost-edge problem. It is a terminal singleton-handoff problem plus whatever direct same-integer closure or additional dominance certificate is needed after handoff.

## 4. Relation to the 73-bit handoff

MATH-061 gives a pre-first-cell source-anchor ceiling below `2^73`. Therefore every unresolved symbolic source has

\[
R\le73.
\]

The MATH-060 additive allowance is 89 shortcut steps. The resolution potential can consume at most 73 step-equivalents, leaving

\[
\boxed{89-73=16}
\]

step-equivalents of the old additive allowance unused.

This numerical slack does **not** by itself close terminal singleton states. It only confirms that the resolution potential fits inside the pre-existing additive budget.

## 5. State-factorization audit

Depth-41 bounded carry and MATH-061 dyadic compatibility do not encode the same information.

For future legality the address state must be split as

\[
\mathcal A=(\mathcal A_{\rm compat},\mathcal A_{\rm dom}).
\]

- `A_compat` determines exact compatibility with the next dyadic macro congruence.
- `A_dom` records Hensel dominance/translation information and may be represented by the MATH-051 bounded-carry subset state inside its audited fixed-d scope.

The carry state must not replace the exact compatibility address without an additional theorem.

## 6. Updated target

The next useful calculation is therefore:

1. enumerate/compress only macro compositions with accumulated source-resolution `<73`;
2. treat every edge with `ell<=R` as automatically Bellman-safe by the present lemma;
3. collect only edges with `ell>R`, which immediately create singleton source states;
4. classify those singleton handoffs by direct descent, Hensel dominance, or another exact terminal certificate;
5. add mixed multi-paid edges only where the one-paid terminal catalogue does not already close the state.

This is substantially smaller than solving a minimum-mean problem on every raw macro edge.

## Reproducibility

`collatz/src/2026_09_12_math074_resolution_overshoot_certificate.py`

# H19 transition-band birth of the d=5 Hensel channel

Date: 2026-08-15

Status: **exact finite phase-transition certificate + structural alignment with the first-return gate repair band**.  It identifies the first locally Hensel-eliminative length-19 phase as the opening of one specific `d=5` integerization channel under a single adjacent conjugacy swap.  This is a localization result, not a global minimal-counterexample exclusion and not a proof of Collatz.

## 1. Last hard phase and first eliminative phase

Along the current isolated-R1 mechanical phase corridor, the last length-19 factor with zero neutral same-state Hensel removal is

\[
\boxed{
H_{33}=1011011010110110101.
}
\]

The immediately following factor is

\[
\boxed{
H_{34}=1011010110110110101.
}
\]

They differ in exactly one adjacent pair, at local zero-based positions `6,7`:

\[
\boxed{10\longleftrightarrow01.}
\]

Both contain twelve odd symbols.

## 2. Neutral fibres

For a length-19 word `v`, compare cumulative odd count to the reference factor and impose

\[
\Sigma=0,
\qquad M=0,
\]

i.e. the relative count never goes below zero and returns to zero at the endpoint.

Exact combination enumeration gives

\[
\boxed{|\mathcal F(H_{33})|=8045,}
\]

\[
\boxed{|\mathcal F(H_{34})|=8640.}
\]

## 3. Exact sibling-max Hensel audit

Inside each neutral fibre use the exact same-length, same-odd-count Hensel sibling-max test.  For a pair with correction difference valuation

\[
s=v_3(R_u-R_w)<q,
\]

put

\[
d=q-s.
\]

The alternate can integerize contractively at its `d`-th odd event only if

\[
2^{t_d}>3^d.
\]

The exact results are

\[
\boxed{
H_{33}:\quad8045\text{ orientations},\quad0\text{ removals},
}
\]

and

\[
\boxed{
H_{34}:\quad8640\text{ orientations},\quad1608\text{ removals}.
}
\]

Moreover every one of the 1608 removals belongs to one and the same channel:

\[
\boxed{s=7,\qquad d=5.}
\]

No other Hensel valuation contributes to the onset.

## 4. Why the channel opens exactly here

The single conjugacy swap moves the fifth odd event by one time step:

\[
\boxed{
t_5:7\longrightarrow8.}
\]

The arithmetic threshold is exactly

\[
\boxed{2^7<3^5<2^8.}
\]

Thus before the swap the `d=5` alternate is noncontracting, while after the swap it becomes contracting.

The first local Hensel elimination in the hard phase corridor is therefore not the cumulative effect of many weak channels.  It is the discrete birth of the unique `d=5` channel at one Christoffel/Sturmian conjugacy exchange.

## 5. Alignment with the gate repair band

The following independently derived scales all lie in the same transition region:

1. the first-return gate systematic/syndrome split has front length
   \[
   F=402\text{--}409;
   \]
2. bounded-credit syndrome repair outside the explicit cube requires an additional correction degree of freedom at odd rank roughly
   \[
   398\text{--}403;
   \]
3. the mechanical odd count at time 646, where the first locally eliminative length-19 phase begins, is
   \[
   \boxed{408},
   \]
   because
   \[
   3^{407}<2^{646}<3^{408}.
   \]

Hence the local phase transition and the independent gate-syndrome repair threshold identify the same roughly 400th-odd-event band.

The present certificate further identifies the local mechanism at that boundary: the `d=5` Hensel channel opens when a single `10->01` conjugacy swap delays the fifth local odd event across the exact threshold `3^5` between `2^7` and `2^8`.

## 6. Limitation

A local smaller predecessor relative to an intermediate orbit state need not lie below the original global minimal start `N`.  Therefore the 1608 local eliminations are not themselves a closure of R1.

The significance is structural localization:

\[
\boxed{
\text{hard phase corridor}
\longrightarrow
\text{single }d=5\text{ channel birth}
\longrightarrow
\text{same band as gate late-repair freedom}.
}
\]

The next theorem should combine this local integerization threshold with the global headroom / renewal-gap inequality, rather than multiply local removal percentages.

## Reproducibility

Exact certificate:

`collatz/src/h19_transition_d5_hensel_birth_certificate.py`

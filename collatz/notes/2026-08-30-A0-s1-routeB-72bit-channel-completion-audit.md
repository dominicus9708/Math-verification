# A0 s=1 Route-B 72-bit physical channel completion audit — 2026-08-30

## Result

The physical A0 shell satisfies

\[
2^{71}<X\le X_{\max}<2^{72},
\]

with

\[
X_{\max}=3,295,414,002,074,039,191,016.
\]

For a prefix channel at depth \(h\le72\),

\[
X=r+2^hm,
\qquad
T^h(X)=y+3^qm,
\]

set

\[
\ell=72-h.
\]

Since \(0\le r<2^h\) and \(X<2^{72}\), every physical member satisfies

\[
0\le m<2^\ell.
\]

The exact block jump writes

\[
m=m_B+2^\ell n,
\qquad 0\le m_B<2^\ell.
\]

Hence at the 72-bit completion depth

\[
\boxed{n=0,\qquad m=m_B.}
\]

Thus every completed physical 72-bit parity address represents exactly one integer \(X\). There is no residual infinite arithmetic family inside a completed physical address.

## Certificate

`collatz/src/A0_s1_routeB_72bit_channel_completion_certificate.py`

The certificate checks the shell inequality at every prefix depth 0 through 72 and compares representative physical integers against the one-bit channel transducer at multiple prefix depths.

Results:

- representative physical integers: `5`;
- sampled prefix depths per integer: `11`;
- completion checks: `55`;
- failures: `0`.

This is consistent with the independent deterministic-formation bridge:

`collatz/src/A0_s1_72bit_deterministic_formation_bridge_certificate.py`

which establishes that, inside the physical A0 shell, the first 72 parity bits determine the source integer uniquely.

## Formation-Axiom audit

At 72 dyadic address bits the physical source coordinate is fully formed: the remaining affine parameter is forced to the singleton value \(n=0\).

## Axis-property audit

The dyadic source-address refinement axis terminates at the physical shell width. Further orbit evolution is temporal/dynamical evolution of that fixed integer, not further branching of the 72-bit source address.

## DSD audit / scope

Closed:

- finite source-address branching ends at 72 bits;
- every physical completed channel is a singleton source integer.

Not closed:

- the deterministic long orbit still has to satisfy the Route-B correction/ballot/first-passage/renewal membership conditions;
- a singleton source is not itself a proof of long-language membership;
- universal Route-B membership and global Collatz integration remain open.

The 14-root forest is not required for this result.

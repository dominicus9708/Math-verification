# First-resonance gap-modulus roughness audit

Date: 2026-08-27

Status: exact finite arithmetic audit; this closes a proposed small-prime CRT shortcut, not the Collatz conjecture.

For the repaired first global resonance

\[
(A,Q)=(114208327604,72057431991),
\]

define

\[
Z=2^A-3^Q.
\]

The near-return identity is

\[
ZN=R-2^A g,
\qquad 0<g<2^{33}.
\]

A tempting shortcut is to find several small prime divisors of `Z`.  If `M|Z` and `M>2^33`, then

\[
g\equiv 2^{-A}R\pmod M
\]

would expose the small integer gap `g` completely.

The companion certificate checks every prime

\[
p\le 50,000,000
\]

by the exact equivalence

\[
p\mid Z
\iff
2^A\equiv3^Q\pmod p.
\]

There are exactly

\[
3,001,134
\]

primes in that interval, and none divides `Z`:

\[
\boxed{
\forall p\le50,000,000\text{ prime},\quad p\nmid Z.
}
\]

Thus the proposed *small-prime product CRT* closure has no traction at this scale.  Scanning ever larger primes would merely replace the original structural problem by a factor search, so this route is demoted from the main proof line.

This does not mean the exact gap modulus is irrelevant.  The identity modulo the full `Z` remains valid, but using it requires a structural description of the correction residue `R`; that is precisely the two-boundary Hensel/formation problem already under study.

DSD audit conclusion:

\[
\boxed{
\text{small-prime factor shortcut}\;\text{closed as a main branch}
\quad\Rightarrow\quad
\text{return to boundary-preserving correction structure}.
}
\]

Companion certificate:

`collatz/src/first_resonance_gap_modulus_roughness_50m_certificate.cpp`.

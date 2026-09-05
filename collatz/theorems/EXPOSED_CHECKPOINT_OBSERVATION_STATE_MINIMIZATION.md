# Exposed-checkpoint observation state minimization

## Scope

This theorem applies **after one ordinary checkpoint integer `Z` has been
exposed with provenance**.  Before that exposure the directed observations
`z_2` and `z_H` remain useful synchronization coordinates and must not be
paired independently.

## 1. Dyadic observation is derived

The first 27 ordinary parity bits after the checkpoint have the unique dyadic
address

\[
\boxed{z_2=Z\bmod2^{27}.}
\]

Hence, once `Z` is known, neither `z_2` nor the raw 27-bit word is an
independent state coordinate.  The actual post-checkpoint prefix is obtained by
iterating the ordinary accelerated Collatz map from `Z`, and its address is
exactly `Z mod 2^27`.

## 2. Ternary/right-H observation is derived

At precision `ell=28`, the certified terminal/right-H transfer is

\[
\boxed{
z_H \equiv 2^s Z-C(H_s^*) \pmod{3^{28}},
}
\]

where

\[
s=630{,}138{,}897.
\]

The coefficient `2^s` is a unit modulo `3^28`, so the transfer is bijective:

\[
Z\bmod3^{28}
\longleftrightarrow
z_H\bmod3^{28}.
\]

Thus `z_H` is also derived after `Z` exposure.

## 3. Terminal target-dominance existence is one mod-3 test

For the current 28-gate right-H terminal window, the certified saturation
lemma gives

\[
\boxed{
\text{target-dominance terminal completion exists}
\iff
3\nmid Z.
}
\]

Consequently the right-H target-dominance existence predicate does not require
retaining the complete 28-gate slack tree after `Z` is exposed.

## 4. State-minimization consequence

After an ordinary checkpoint has been exposed **with source provenance**, the
checkpoint observation state may be reduced to

\[
\boxed{Z}
\]

plus only genuinely independent later predicates.  Specifically,

- `z_2` is derived from `Z mod 2^27`;
- `z_H` is derived by the affine transfer modulo `3^28`;
- the 27-bit post-prefix is deterministic from `Z`;
- target-dominance terminal existence is the derived test `Z mod 3 != 0`.

Therefore a source-preserving paired exporter should preferentially expose an
ordinary `Z` (or an equivalent provenance-preserving object from which `Z` is
uniquely reconstructed), rather than maintaining an independent Cartesian
product of `z_2` and `z_H` labels after the CRT seam.

## 5. Before exposure

This theorem does **not** say that `z_2` and `z_H` may be dropped before they
jointly expose `Z`.  Before synchronization,

\[
(z_2,z_H)
\]

are directed observations from different boundaries.  Their marginal sets may
not be Cartesian-multiplied or treated as independent probabilities.

## DSD audit

- **EXACT/CLOSED**: `Z -> z_2`.
- **EXACT/CLOSED**: `Z -> z_H` and inverse ternary transfer.
- **EXACT/CLOSED**: current terminal target-dominance existence reduces to
  `3 does not divide Z`.
- **EXACT/CLOSED**: after provenance-preserving exposure, `z_2` and `z_H` are
  derived rather than persistent coordinates.
- **REJECTED**: dropping both observations before a unique/provenanced `Z` has
  been exposed.
- **REJECTED**: independently Cartesian-pairing marginal `z_2` and `z_H` sets.
- **OPEN**: source-preserving construction of the actual ordinary checkpoint
  candidate(s) from the current 14,224 source families.
- **OPEN**: full right-H/H-L grammar and Route-B membership obligations beyond
  the certified target-dominance terminal existence predicate.

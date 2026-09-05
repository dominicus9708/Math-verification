# A0 s=1 Route-B channel/block parameter partition audit — 2026-08-30

## Result

For a fixed parent parity-prefix channel

\[
X=r+2^hm,
\qquad
T^h(X)=y+3^qm,
\]

and a fixed candidate block length \(\ell\), the exact block-jump rule assigns each length-\(\ell\) parity block \(B\) one parameter residue

\[
m\equiv m_B\pmod{2^\ell}.
\]

The map

\[
B\longmapsto m_B\pmod{2^\ell}
\]

is a bijection between the \(2^\ell\) parity blocks and the \(2^\ell\) parameter residues.

Therefore the full length-\(\ell\) block family partitions the parent parameter axis exactly: no two blocks claim the same residue class and no residue class is omitted.

## Exact reason

Each length-\(\ell\) parity cylinder has one canonical source residue

\[
\rho_B=-C_B(3^{q_B})^{-1}\pmod{2^\ell}.
\]

For the parent channel,

\[
m_B=(\rho_B-y)(3^q)^{-1}\pmod{2^\ell}.
\]

Because \(3^q\) is odd, multiplication by \((3^q)^{-1}\) modulo \(2^\ell\) is a bijection, and translation by \(-y\) is also a bijection. Thus parity-cylinder uniqueness transfers exactly to parent-parameter residue uniqueness.

## Certificate

`collatz/src/A0_s1_routeB_channel_block_partition_certificate.py`

Exhaustive audit domain:

- parent prefix depths through 5: 63 parent channels;
- block lengths 1 through 8;
- all parity blocks at each block length;
- direct endpoint lifts and finite-interval pullbacks.

Results:

- permutation checks: `504`;
- block-jump checks: `32,130`;
- endpoint-lift checks: `96,390`;
- interval-partition checks: `2,520`;
- failures: `0`.

## Formation-Axiom audit

A child block forms one and only one child residue coordinate. The complete block family forms the entire parent parameter coordinate without overlap or omission.

## Axis-property audit

At fixed block length \(\ell\), block choice and the residue coordinate \(m\bmod2^\ell\) are equivalent coordinates. Replacing block enumeration by residue-class pruning therefore does not change the represented set.

## DSD audit / scope

Closed:

- exact block-to-parameter bijection at fixed block length;
- exact transfer of block pruning into arithmetic residue-class pruning.

Open:

- which blocks satisfy the complete Route-B long admissibility predicate;
- compressed deterministic long-membership recognition;
- universal Route-B membership;
- global Collatz integration.

This certificate does not depend on the conditional 14-root reduction.

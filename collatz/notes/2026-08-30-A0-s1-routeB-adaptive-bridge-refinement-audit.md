# A0 s=1 Route-B adaptive bridge refinement audit — 2026-08-30

## Result

The fixed-resolution correction bridge has now been upgraded with an exact
adaptive refinement rule inside every collision class whose candidate words
share the same block length `h` and odd-count `q`.

For two such blocks `U,V`, write

\[
\Delta=C(U)-C(V).
\]

At resolution `(K,L)`,

\[
S_{K,L}(U)=S_{K,L}(V)
\iff 2^K3^L\mid\Delta.
\]

Therefore the exact first separating resolutions are

\[
K_*=v_2(\Delta)+1,
\qquad
L_*=v_3(\Delta)+1.
\]

If the pair currently collides at `(K,L)`, then either `(K_*,L)` or
`(K,L_*)` separates it.  A decoder can choose the smaller increment.

## Exhaustive audit

Certificate:

`collatz/src/A0_s1_routeB_adaptive_bridge_refinement_certificate.py`

Audit domain:

- all binary words through depth 11;
- pairs compared only inside equal `(h,q)` classes;
- resolutions `(1,1),(2,2),(3,2),(4,3),(5,4)`;
- exact phase-critical ballot summary crossed with every correction collision.

Results:

- pair/resolution checks: `2,380,725`;
- correction bridge collisions: `187,956`;
- exact adaptive separation checks: `375,912`;
- bridge collisions already split by ballot summary: `136,952`;
- bridge+ballot collisions remaining before adaptive refinement: `51,004`;
- all `51,004` remaining audited collisions separated by one exact
  valuation-guided refinement;
- maximum audited dyadic increment: `8`;
- maximum audited ternary increment: `8`.

Resolution breakdown is

| `(K,L)` | bridge collisions | ballot splits | bridge+ballot remain |
|---|---:|---:|---:|
| `(1,1)` | 138,048 | 103,391 | 34,657 |
| `(2,2)` | 31,196 | 21,157 | 10,039 |
| `(3,2)` | 15,848 | 10,479 | 5,369 |
| `(4,3)` | 2,704 | 1,801 | 903 |
| `(5,4)` | 160 | 124 | 36 |

Thus the ballot sector is not redundant: it removes many correction-sector
collisions without raising adic resolution.  Conversely, when ballot also
collides, the exact valuation rule supplies a deterministic refinement.

## Formation-Axiom audit

The refinement does not invent a new block coordinate.  It adds only the
missing dyadic or ternary resolution required to distinguish already formed
fixed-`(h,q)` candidate blocks.

The state formation order is therefore

1. intrinsic block metadata `(h,q)`;
2. correction coordinate at current resolution;
3. ballot response `(m,a)`;
4. only on collision, refine the required external adic resolution axis.

No expanded interior word is needed by the refinement theorem itself.

## Axis-property audit

Dyadic and ternary resolution are independent external refinement axes.
Raising one does not change the intrinsic block, its length, odd-count, or
ballot state.  Therefore choosing the cheaper of

\[
K_*-K,
\qquad
L_*-L
\]

is a legitimate decoder optimization, not a mathematical change of state.

## DSD audit / scope

Closed:

- exact collision criterion in equal-`(h,q)` classes;
- exact first dyadic and ternary separating resolutions;
- compatibility with the phase-critical ballot cross-filter on the exhaustive
  audit domain.

Still open:

- proof that every Route-B long survivor is always presented to this rule in
  an appropriate fixed-`(h,q)` candidate-block class;
- the full adaptive lazy language decoder;
- universal Route-B membership;
- global Collatz integration.

The 14-root forest remains a conditional/optimization checkpoint until its
upstream finite eliminations are independently re-certified in the proof
chain.  The present adaptive theorem does not depend on the 14-root reduction.

## Next exact primitive

For a parent channel

\[
X=r+2^hm,
\qquad
T^h(X)=y+3^qm,
\]

and candidate blocks of common `(ell,q_B)`, combine:

- the exact block-selected parameter residue `m_B mod 2^ell`;
- bridge+ballot collision filtering;
- adaptive adic refinement only on unresolved block pairs.

The next certificate should verify that distinct same-`(ell,q_B)` candidate
blocks induce distinct full parameter residues and that block refinement
partitions the parent channel exactly.  This is the direct bridge from the
state theory to the lazy Route-B decoder.

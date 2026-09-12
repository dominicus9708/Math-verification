# Collatz common-formula analysis data inventory

Date: 2026-09-12

Purpose: identify existing exact datasets that can be re-analyzed under the current common-state framework without prematurely using unclosed paid-count layers `2<=r<=13`.

## Priority A — directly compatible with the current common-state extraction

### A1. Depth 1--41 unified coefficient/Hensel chain

Status: re-audited 2026-09-12.

Useful coordinates:

\[
(k,q,r,S,\rho,\Sigma,\mathcal A_{dom}).
\]

Use: determine which quantities are exact state coordinates, which are redundant, and how near-boundary Hensel pruning depends on `rho`, q-distance from the coefficient boundary, and translation credit.

### A2. Closed paid-count layers r=14,15,16,17

Status: closed and separately DSD-audited.

Representations differ by layer:

- r=17: block -> singleton handoff;
- r=16: AP + block + streaming;
- r=15: multiplicity-banded AP union;
- r=14: adaptive AP union + arbitrary-precision source sharding.

Use: compare closure reasons against the same analytic coordinates

\[
S=1+\Sigma-\rho,
\qquad
\rho=2^{-u}\Omega,
\qquad
p=(\Omega-\rho)/3.
\]

### A3. One-paid macro catalogue and composition

Canonical one-paid cylinders: 910.

Two-macro nonempty compositions: 12,530.

Terminal singleton handoffs have now been checked through macro depth 4.

Use: extract future-compatibility quotient and test the resolution potential

\[
H_R=-\frac{19}{503}R_{res}.
\]

### A4. First-cell penalty / Bellman data

Includes MATH-053/054/059/060 and the exact first-cell slope target

\[
\lambda_*=19/503.
\]

Use: test whether the common state can yield a future-complete Bellman inequality without enumerating low-paid layers individually.

## Priority B — structural cross-check datasets

### B1. Integrated endpoint quotient and true-first-merge data through depth 32

Known exact depth-32 facts include:

- coefficient-surviving states: 41,347,483;
- endpoint classes: 38,890,504;
- exact true-first-merge count through depth 32: 6,996;
- Delta-Q sectors and exact G contrast values.

Use: rewrite endpoint/merge geometry in `(r,S,rho)` coordinates and test whether Hensel translation credit predicts merge channels.

### B2. First-descent interval-channel audit through depth 24

Use: connect ordinary descent events to normalized correction `S` and address resolution rather than only parity-word labels.

### B3. Exact first-crossing band audit through depth 26

Use: compare coefficient-boundary crossing with phase/slack `rho/Omega=2^{-u}`.

### B4. Reverse-preimage / Beatty-rise depth-23 certificate

Use: test whether the same mechanical boundary appears symmetrically in forward coefficient survival and reverse admissibility.

### B5. m44 coefficient-class sieve through depth 26

Use: audit which class descriptors are genuinely future-complete and which are only local filters.

### B6. root-11 no-00 Hensel-max audit through depth 28

Use: compare restricted-language Hensel maxima with the unrestricted fixed-d carry state.

### B7. no-27-mod-36 paradoxical first-crossing certificate through depth 38

Use: test whether arithmetic residue exclusions can be expressed as a compact address-side invariant independent of the analytic `(S,rho,Omega)` state.

## Priority C — long-depth validation datasets

These are valuable because they can test a formula extracted from depth <=41 without fitting it on the same depth range.

### C1. Exact Beatty-ballot survivor language through depth 191

Use: out-of-sample test of any proposed coefficient-boundary/mechanical-sequence formula.

### C2. First-cell root credit / root-safe / endpoint q-lock through depth 195

Use: test whether a common formula derived from shallow depths remains compatible with first-cell root/address restrictions at substantially greater depth.

### C3. Internal-boundary / collision exclusion datasets

Existing certificates extend various boundary/collision checks through depths 72, 75, 78, 79, 81 and beyond.

Use: stress-test any claim that `S` or Hensel state alone determines compatibility. These datasets are particularly useful for detecting hidden address dependence.

### C4. Linear collision-halo / large-depth bootstrap datasets

Existing DSD audits include linear collision-halo and rolling/block bootstrap calculations at depths far beyond 41.

Use: test whether a proposed finite quotient remains stable as depth grows without reusing the fitting sample.

## Priority D — alternative-coordinate datasets

### D1. 11-bit block-label transducer / right-congruence audits

Use: compare block symbolic state to the current dyadic compatibility coordinate.

### D2. 340-block endpoint-halo decomposition

Use: test aggregation invariance: whether the same common quantities survive a much coarser block description.

### D3. 3-adic and dyadic orthogonality certificates

Use: secondary test of whether residue channels can be factored or decorrelated exactly. These should not be used as independence assumptions unless an exact factorization theorem is established.

## Recommended analysis order

1. rewrite depth-32 endpoint/merge data in `(r,S,rho)`;
2. compare Hensel integer translation credit to actual merge/source translation;
3. attach the first-descent and first-crossing datasets;
4. compare against closed r=14--17 layers;
5. derive a candidate common potential/state reduction;
6. test it out-of-sample on depth 191/195 and boundary/collision datasets;
7. only after that, use r=13 as a new independent paid-layer test if desired.

This order avoids fitting a formula to `r=2..13`, which remain unclosed and intentionally excluded from the present extraction dataset.

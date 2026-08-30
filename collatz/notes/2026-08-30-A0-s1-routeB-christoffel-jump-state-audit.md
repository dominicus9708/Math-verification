# A0 s=1 Route-B Christoffel jump-state audit — 2026-08-30

## Scope

This note audits the next Route-B block-jump step after the exact correction-state reduction and phase-sensitive ballot-state certificate.

The goal is not to claim Collatz closure.  The goal is to determine which information can be propagated through the existing 129-node Stern-Brocot/Christoffel DAG without expanding the gigantic lower-mechanical word.

## 1. Existing DAG structure

The base block `L` is represented by a 129-node DAG for

- length `J0 = 10,439,860,591`,
- odd count `R0 = 6,586,818,670`.

Each internal node is exactly the concatenation of its stored left and right child.  There are 127 internal nodes and two leaves.

The existing normalized correction state is

\[
m(w)=\frac{3^{q(w)}}{2^{|w|}},\qquad c(w)=\frac{C(w)}{2^{|w|}},
\]

with

\[
c(uv)=m(v)c(u)+c(v).
\]

This is the normalized form of the already-certified exact integer law

\[
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
\]

## 2. Formation Axiom System lens

For an internal node `N = L R`, an intrinsic correction summary is admissible only if the parent summary is formed from the child summaries plus explicit composition metadata.

At dyadic resolution `K`, define

\[
C_K(w)=C(w)\pmod {2^K}.
\]

Then

\[
C_K(LR)=3^{q(R)}C_K(L)+2^{|L|}C_K(R)\pmod {2^K}.
\]

Therefore the parent correction projection is completely formed from

- the left child projection,
- the right child projection,
- `|L|`,
- `q(R)`.

No hidden expanded word is required.

This is an organizational use of the Formation Axiom System; the mathematical validity comes from the exact affine Collatz composition identity itself.

## 3. Axis-property lens

The previous exact state reduction showed that `(h,r,y,q)` contains redundant coordinates: for a realized parity prefix, `(h,q,C)` reconstructs `r,y` exactly.

At DAG level the useful distinction is now:

- intrinsic structural axes: block length and odd count,
- intrinsic arithmetic axis: correction projection `C mod 2^K`,
- external placement axis: absolute threshold phase/offset `h` used by the ballot margin.

The ballot phase must **not** be internalized naively into each reused DAG node.  Exact occurrence counting gives, for one base block `L`,

- leaf/bit placements: `10,439,860,591`,
- total binary parse-tree node placements: `20,879,721,181 = 2 J0 - 1`.

Thus replacing a 129-node DAG state by raw `(node, absolute h)` occurrences destroys the compression.

This does not prove that no compressed phase description exists.  It only rules out the naive absolute-offset lift.

## 4. Exact modular correction jump

For every `K` in

`1, 2, 4, 8, 16, 32, 64, 72, 74, 75, 128, 256, 512, 1024`,

the new certificate propagates `C mod 2^K` through every DAG node.

Results:

- DAG nodes: `129`,
- internal parent nodes: `127`,
- parent-composition checks: `1,778`,
- cross-resolution projection checks: `1,677`,
- mismatches: `0`.

## 5. Direct materialization regression

Every DAG node of length at most `100,000` was independently expanded and its exact correction was recomputed from the bit word.

Results:

- materialized nodes: `45`,
- total materialized bits across these node regressions: `457,063`,
- modular comparisons: `630`,
- mismatches: `0`.

For short nodes, canonical cylinder residues were also reconstructed from the exact correction and checked by directly running the accelerated Collatz map through the materialized parity word.

- low-residue checks: `177`,
- mismatches: `0`.

## 6. Target-aware residue jump

Because `3^q` is odd,

\[
r(w)\equiv -C(w)(3^{q(w)})^{-1}\pmod{2^{|w|}}.
\]

Therefore, at any `K <= |w|`,

\[
r(w)\bmod 2^K
=
-C_K(w)(3^{q(w)})^{-1}\bmod 2^K.
\]

This makes `C mod 2^K` an exact low-resolution target/cylinder discriminator.

For the existing threshold decomposition

\[
W_{\rm th}=U L^9,
\]

with

\[
|U|=|L|=J_0,\quad q(U)=R_0+1,\quad C(U)=C(L)+3^{R_0},
\]

the certificate computes the canonical residue of the entire gigantic threshold word without materializing it.

Against

`X_TH = 4,697,939,311,072,332,635,131`,

the modular residue agrees for every dyadic depth

\[
1\le K\le 74
\]

and first disagrees at

\[
K=75.
\]

An independent direct orbit check of the finite integer `X_TH` gives the same result: its parity word agrees with the threshold parity word for the first 74 symbols and first differs at zero-based position `74` (the 75th symbol).

This is an exact finite target projection, not a universal membership theorem.

## 7. DSD audit

### Closed

- ✅ exact intrinsic correction state can be projected modulo `2^K`;
- ✅ modular correction composition closes on all 129 DAG nodes;
- ✅ dyadic projections are mutually consistent;
- ✅ all directly materialized nodes agree with the recursive summaries;
- ✅ low-order canonical cylinder residues are recoverable from the modular state;
- ✅ the `X_TH`/threshold first-disagreement depth is recovered by the gigantic DAG jump without expanding the word;
- ✅ naive `(node, absolute phase)` state expansion is quantitatively rejected.

### Open

- ❌ compressed representation of phase-sensitive ballot margin `mu_h` on reused DAG nodes;
- ❌ proof of a finite or recursively closed right-congruence quotient;
- ❌ full `match_and_jump` decoder for arbitrary long candidate/target membership;
- ❌ universal Route-B correction-language membership verdict;
- ❌ Collatz conjecture proof.

## 8. Next gate

The next useful state should keep correction and placement separate:

\[
\text{intrinsic node state}
=(\ell,q,C\bmod 2^K),
\]

while the ballot part must receive a compressed description of the threshold location rather than a raw absolute offset for every occurrence.

The immediate task is therefore to test whether the Christoffel hierarchy itself supplies a recursive phase address sufficient to compose

\[
\Delta_h(B),\qquad \mu_h(B)
\]

without expanding all occurrences.

If such an address closes, it becomes the placement component of the Route-B jump decoder.  If it does not, that failure is itself a clean obstruction and the decoder must use a different target-aware/lazy decomposition.

## Reproducibility

Certificate:

`collatz/src/A0_s1_routeB_christoffel_jump_state_certificate.py`

Expected headline output:

```text
PASS A0 s=1 Route-B Christoffel modular jump-state certificate
dag_nodes 129
dag_internal_nodes 127
root_length 10439860591
root_ones 6586818670
parent_composition_checks 1778
projection_consistency_checks 1677
materialized_nodes 45
materialized_total_bits 457063
materialized_mod_checks 630
small_node_residue_checks 177
target_projection_checks 128
target_match_depth 74
target_first_mismatch_position_zero_based 74
base_block_leaf_phase_placements 10439860591
base_block_total_node_phase_placements 20879721181
status EXACT modular correction jump CLOSED; compressed phase-ballot/right-congruence decoder remains OPEN
```

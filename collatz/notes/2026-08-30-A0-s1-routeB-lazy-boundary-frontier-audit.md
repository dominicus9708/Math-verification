# A0 s=1 Route-B lazy boundary-frontier audit

Date: 2026-08-30

Status: **G4 lazy boundary descent primitive CLOSED; target-specific interior/right-congruence decoder remains OPEN**.

## 1. Input theorem

The preceding dual-adic audit established, for `W=UV`,

\[
D_K(W)=D_K(U)\quad(K\le h(U)),
\]

\[
E_L(W)=E_L(V)\quad(L\le q(V)).
\]

Here `D_K` is the start-facing residue modulo `2^K` and `E_L` is the end-facing residue modulo `3^L`.

The remaining implementation question is how far a compressed DAG decoder may descend without losing any requested boundary resolution.

## 2. Exact frontier rule

For a node `N` carrying a start condition of width `K`, descend to its left child only if that child has length at least `K`.

Stop at the first node `F_2` satisfying

\[
h(F_2)\ge K
\]

while its left child, if present, satisfies

\[
h(\operatorname{left}(F_2))<K.
\]

Then

\[
\boxed{D_K(N)=D_K(F_2)}.
\]

Likewise, for an end condition of ternary width `L`, descend to the right child only while that child contains at least `L` odd symbols.  Stop at `F_3` with

\[
q(F_3)\ge L,
\]

but

\[
q(\operatorname{right}(F_3))<L
\]

when a right child exists.  Then

\[
\boxed{E_L(N)=E_L(F_3)}.
\]

This stopping rule is important: the unresolved portion of a higher-resolution condition is retained at the parent frontier rather than silently discarded.

## 3. Certificate

New source:

`collatz/src/A0_s1_routeB_lazy_boundary_frontier_certificate.py`

Across the 129-node Christoffel DAG and the selected Route-B resolutions:

- left frontier checks: `1,228`;
- right frontier checks: `1,098`;
- left frontier minimality checks: `1,228`;
- right frontier minimality checks: `1,098`;
- explicit exact/mismatch gate checks on the left: `2,456`;
- explicit exact/mismatch gate checks on the right: `2,196`;
- maximum legal left descent: `43` DAG edges;
- maximum legal right descent: `85` DAG edges.

All passed.

## 4. Base-block L at the exposed resolutions

For the base Christoffel block

\[
|L|=10,439,860,591,
\qquad q(L)=6,586,818,670,
\]

the currently exposed checkpoint widths collapse to very small exact frontier nodes.

### 27-bit start frontier

At `K=27`, the root descends through 39 legal left edges to DAG node `8`:

\[
|F_2|=27,
\qquad q(F_2)=17.
\]

The exact shared residue is

\[
\boxed{D_{27}(L)=87,757,810}.
\]

The node's left child is too short to retain all 27 bits, so this is the exact minimal left frontier under the chosen DAG decomposition.

### 28-trit end frontier

At `L=28`, the root descends through 81 legal right edges to DAG node `11`:

\[
|F_3|=84,
\qquad q(F_3)=53.
\]

The exact shared residue is

\[
\boxed{E_{28}(L)=2,158,791,402,581}.
\]

Its right child has fewer than 28 odd symbols, so this is the exact minimal right frontier.

### Other existing exposure widths

- `K=39` reaches node `9`, with length `46` and `29` odd symbols;
- `L=24` reaches node `11`, with length `84` and `53` odd symbols.

Thus the already-certified 27/28 checkpoint exposure and 24/39 debit/credit widths are compatible with a very small boundary footprint inside the gigantic base block.

## 5. What this closes

A boundary mismatch can now be rejected at its exact minimal frontier without traversing the rest of the Christoffel block.

For a required dyadic residue `d`,

\[
D_K(N)\ne d
\iff
D_K(F_2)\ne d.
\]

For a required ternary residue `e`,

\[
E_L(N)\ne e
\iff
E_L(F_3)\ne e.
\]

The certificate checks both the matching and deliberately mismatching gate predicates so that an implementation cannot accidentally invert the pruning logic.

## 6. What this does not close

Matching both frontiers is only necessary boundary compatibility.

It does **not** prove that:

- the interior correction belongs to the admissible long correction language;
- the exposed start and end values are connected by the same Collatz bridge;
- the ballot/formation state is automatically preserved through the interior;
- a finite global right congruence has already been found.

The next target is therefore an **interior bridge state** that can be composed between the two frontiers and compared with the unique target correction without enumerating the intermediate parity word.

## 7. Formation / Axis / DSD audit

### Formation Axiom System

The decoder descends only when a child has enough formed coordinates to preserve the complete requested boundary datum.  A partial child coordinate is not promoted to a complete one.

### Axis Property

The dyadic condition propagates toward the left/start boundary and the ternary condition toward the right/end boundary.  Their directions are separate structural axes; absolute block placement is not added to the intrinsic node state.

### DSD

- dual-adic localization: ✅ CLOSED;
- resolution-preserving lazy frontier descent: ✅ CLOSED;
- mismatch pruning at the frontier: ✅ CLOSED;
- matching frontiers imply long correction membership: ❌ REJECTED;
- target-specific interior bridge decoder: OPEN;
- G5 universal membership verdict: OPEN;
- Collatz conjecture: OPEN.

## 8. Updated G4 decomposition

G4 can now be split into:

1. exact channel block jump — **CLOSED**;
2. exact dual-adic boundary localization — **CLOSED**;
3. exact lazy boundary frontier descent — **CLOSED**;
4. exact interior bridge/right-congruence state — **OPEN**;
5. target-aware full bridge decoder — **OPEN**.

The next useful calculation is step 4, not a larger shallow brute-force radius.

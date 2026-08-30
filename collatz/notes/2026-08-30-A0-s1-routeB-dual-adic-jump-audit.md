# A0 s=1 Route-B dual-adic jump audit

Date: 2026-08-30

Status: **exact dual-adic block localization CLOSED; target-aware lazy/right-congruence decoder remains OPEN**.

## 1. Purpose

The current Route-B gate is not an ordinary brute-force parity search.  The long correction word is unique when the relevant endpoints are fixed, so the useful next primitive is a compressed boundary decoder that can discard whole blocks without materializing their bits.

This note records an exact two-sided localization theorem for the correction state.

## 2. Exact block identity

For a parity block `W` of length `h(W)`, odd count `q(W)`, and correction `C(W)`,

\[
2^{h(W)}Y=3^{q(W)}X+C(W).
\]

For a concatenation `W=UV`,

\[
C(UV)=3^{q(V)}C(U)+2^{h(U)}C(V).
\]

Define the start-facing dyadic coordinate

\[
D_K(W):=-C(W)\,(3^{q(W)})^{-1}\pmod{2^K},
\qquad 1\le K\le h(W),
\]

and the end-facing ternary coordinate

\[
E_L(W):=C(W)\,(2^{h(W)})^{-1}\pmod{3^L},
\qquad 1\le L\le q(W).
\]

Then the composition law gives the exact localizations

\[
\boxed{D_K(UV)=D_K(U)\quad\text{when }K\le h(U)},
\]

and

\[
\boxed{E_L(UV)=E_L(V)\quad\text{when }L\le q(V)}.
\]

The dyadic start condition therefore belongs entirely to a sufficiently long left block, while the ternary endpoint condition belongs entirely to a sufficiently odd-rich right block.

The second identity does **not** require a canonical incoming value for `V`: when `q(V)>=L`, its incoming term is multiplied by `3^{q(V)}` and vanishes modulo `3^L`.

## 3. Independent certificate

New source:

`collatz/src/A0_s1_routeB_dual_adic_jump_certificate.py`

The certificate does not import the earlier jump-state certificate.  It reconstructs the correction summaries and checks the dual localization independently.

### Exhaustive arbitrary words

All nonempty binary parity words through depth 9 were checked.

- arbitrary words: `1,022`;
- summary composition checks: `7,172`;
- dyadic projection checks: `7,172`;
- ternary projection checks: `3,084`;
- left/dyadic localization checks: `29,692`;
- right/ternary localization checks: `14,846`;
- actual Collatz-orbit checks: `1,022`;
- actual dyadic lifted-value checks: `118,768`;
- actual ternary lifted-value checks: `59,384`.

The actual-value checks use representatives of the same `2^h` cylinder and verify the result against the ordinary Collatz map, rather than only reusing the symbolic composition identity.

### 129-node Christoffel DAG

The exact 129-node Stern-Brocot/Christoffel DAG for

\[
J_0=10,439,860,591,\qquad R_0=6,586,818,670
\]

was rebuilt independently in the certificate.

At the selected resolutions:

- dyadic parent composition checks: `1,270`;
- ternary parent composition checks: `1,143`;
- applicable left-localization checks: `1,216`;
- applicable right-localization checks: `1,080`.

All passed.

For every DAG node of length at most `100,000`, direct materialization was also used as a regression check:

- materialized nodes: `45`;
- total materialized bits: `457,063`;
- dyadic direct checks: `450`;
- ternary direct checks: `405`.

All passed.

## 4. Relation to existing Route-B exposure widths

The earlier closure-status audit independently records:

- checkpoint `Z`: `27` dyadic bits + `28` terminal ternary trits suffice for CRT singleton exposure;
- debit `L_-`: `24` terminal trits;
- credit `L_+`: `39` dyadic bits.

The present certificate includes the `K=27` and `L=28` resolutions and confirms that they are valid exact coordinates of the same compressed correction state.

This does **not** identify an exposed endpoint with a valid correction-language bridge.  Exposure and same-orbit/correction-language connectivity remain logically separate.

## 5. Decoder consequence

For a node split `W=UV`, an external start constraint `(K,d)` can be pushed entirely into `U` whenever `K<=h(U)`.  An external end constraint `(L,e)` can be pushed entirely into `V` whenever `L<=q(V)`.

Thus a target-aware decoder can use the rule

\[
\Sigma_{K,L}(UV)=\bigl(D_K(U),E_L(V)\bigr)
\]

whenever both localization conditions hold.

If either exposed residue disagrees with the required boundary residue, the whole parent block is rejected without descending to individual bits.

If the child is too short to absorb the requested resolution, the decoder must descend or transform the unresolved boundary condition exactly; it may not silently truncate the condition.

This last recursive control rule is the next G4 task.

## 6. Formation / Axis / DSD audit

### Formation Axiom System

The parent dual-boundary state is formed only from exact child correction summaries and explicit concatenation metadata.  No expanded giant word or undefined hidden state is required.

### Axis Property

The two adic coordinates have opposite boundary orientation:

- `D_K`: start/left-facing coordinate;
- `E_L`: end/right-facing coordinate.

They are not absolute placement coordinates.  This avoids the earlier state explosion caused by internalizing every placement `h` in a reused DAG node.

### DSD

- exact algebraic dual localization: ✅ CLOSED;
- Christoffel-DAG compatibility: ✅ CLOSED;
- existing 27x28 exposure interpreted only as boundary resolution: ✅;
- exposed endpoint implies same correction-language bridge: ❌ REJECTED;
- target-aware recursive lazy decoder: OPEN;
- universal Route-B membership/nonmembership: OPEN;
- Collatz conjecture: OPEN.

## 7. Updated G status

- `G1` exact correction state: **CLOSED**;
- `G2` exact correction + ballot two-block state: **CLOSED**;
- `G3` recursive block-state composition: **CLOSED as a compositional mechanism**, but target-relevant finite/right-congruence closure remains **OPEN**;
- `G4` target-aware decoder: **IN PROGRESS**; block jump and dual-adic localization primitives are now CLOSED;
- `G5` universal Route-B membership verdict: **OPEN**.

The next certificate should implement the exact lazy descent rule and prove that pruning by a localized boundary mismatch is equivalent to the corresponding direct block residue test, while preserving unresolved higher-resolution constraints instead of discarding them.

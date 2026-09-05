# A0 s=1 Route-B adaptive bridge + ballot refinement audit

Date: 2026-08-31
Branch: `collatz-stage4-window-threshold`
Status: finite-domain G4 decoder primitive closed; universal long-language membership remains open.

## 1. Scope

This audit combines two exact Route-B block summaries already established on this branch:

1. the fixed-resolution dual-adic correction bridge
   \[
   S_{K,L}(W)=\left(3^{q(W)},2^{h(W)},C(W)\right)\pmod{2^K3^L},
   \]
2. the phase-critical ballot summary
   \[
   B(W)=(h(W),q(W),m_W,a_W).
   \]

The combined state is
\[
\mathcal S_{K,L}(W)=\bigl(S_{K,L}(W),B(W)\bigr).
\]
Both sectors have exact two-block composition laws, so the combined state is compositionally closed.

This is not yet a universal recognizer for the Route-B correction language. In particular, first-passage, renewal, same-orbit and the remaining long-membership gate are not inferred merely from equality of \(\mathcal S_{K,L}\).

## 2. Exact pairwise refinement rule

Suppose distinct blocks \(U,V\) have the same length and one-count:
\[
h(U)=h(V),\qquad q(U)=q(V).
\]
Set
\[
\Delta=C(U)-C(V)\ne0.
\]
Then equality of their correction bridge states at resolution \((K,L)\) is exactly equivalent to
\[
2^K3^L\mid\Delta.
\]
Therefore the first dyadic resolution that can separate the pair is
\[
K_*=v_2(\Delta)+1,
\]
and the first ternary resolution is
\[
L_*=v_3(\Delta)+1.
\]

The ballot coordinates may separate a correction-bridge collision before either resolution axis is raised.

## 3. Finite exhaustive audit

Audit domain: all binary words of length 12, hence 4096 words.
Initial resolution:
\[
(K,L)=(2,2).
\]

Exact counts:

- pure bridge collision pairs: `246489`
- bridge collision pairs after additionally fixing the same \((h,q)\): `89684`
- combined bridge+ballot collision pairs: `27792`
- pairs separated by adding the ballot summary to the pure bridge state: `218697`
- same-\((h,q)\) bridge pairs separated by ballot: `61892`
- valuation theorem pair checks: `27792`

The earlier provisional figure `89684` is therefore not the number of collisions of the pure bridge state. It is the count after imposing the additional same-\((h,q)\) condition. The corrected pure-bridge count is `246489`.

For the 27792 remaining combined-state collision pairs, the cheaper of dyadic or ternary extra refinement required:

- 1 step: `20980`
- 2 steps: `5742`
- 3 steps: `1024`
- 4 steps: `46`

Axis comparison:

- dyadic cheaper: `7512`
- ternary cheaper: `11295`
- equal cost: `8985`

## 4. Adaptive decoder audit

At each non-singleton combined-state bucket, compare one-step refinement \((K+1,L)\) with \((K,L+1)\). Choose the axis that creates more immediate child buckets; break the next tie by the smaller largest child bucket, then deterministically prefer the dyadic axis.

At the initial \((2,2)\) resolution:

- singleton words: `171`
- collision groups: `457`
- words inside collision groups: `3925`

The adaptive recursion separated all 3925 collision words.

Exact run statistics:

- adaptive internal nodes: `2960`
- adaptive leaves: `3925`
- maximum refinement steps on one path: `7`
- maximum dyadic resolution reached: `K=9`
- maximum ternary resolution reached: `L=8`
- dyadic refinement nodes: `2503`
- ternary refinement nodes: `457`

The enclosing fixed rectangle \((K,L)=(9,8)\) also gives unique combined states for all 4096 audited words.

These numbers are finite-domain evidence only. They do not justify extrapolating a uniform resolution bound to arbitrary Route-B words.

## 5. Formation Axiom System audit

The combined state is formed only from already-defined child summaries plus explicit concatenation/resolution metadata. No hidden materialization of the full parity word is required.

Adaptive refinement does not change the underlying block. It requests one additional coordinate of resolution only when a current quotient class still contains multiple candidates.

Result: structurally admissible as a compositional summary mechanism.

## 6. Axis Property audit

The dyadic and ternary resolutions \(K,L\) are external resolution axes, not intrinsic identities of the block.

The ballot coordinates \(m_W,a_W\) are intrinsic response coordinates of the block. In particular, the critical prefix can distinguish correction-bridge collisions before either external resolution axis grows.

This preserves the earlier separation between intrinsic block structure and external evaluation/resolution coordinates. The rejected raw `(node,h)` phase lift should not be reintroduced.

## 7. DSD cross-audit

Confirmed:

- exact correction bridge composition;
- exact phase-critical ballot composition;
- exact same-\((h,q)\) valuation threshold for correction-state collisions;
- finite exhaustive adaptive separation on the 12-bit audit domain.

Not confirmed:

- a universal finite upper bound for \(K,L\);
- recognition of the full Route-B admissible/correction language;
- first-passage, renewal or same-orbit closure from this state alone;
- the final universal Route-B membership theorem;
- the Collatz conjecture.

## 8. Next proof obligation

The next task is not a larger generic finite enumeration. It is to attach this exact adaptive state to the actual Route-B long-membership representation and its channel constraints.

The intended next state is a relative/target-aware decoder carrying, as needed,
\[
(\text{channel},\;K,L,\;S_{K,L},\;m,a,\;\text{target/hierarchy locator},\;\text{defect data}).
\]
A whole block should be rejected or jumped whenever the channel-block residue condition or the combined state decides it; only unresolved blocks should descend recursively.

The 14-root forest remains a conditional optimization checkpoint until the upstream \(f\ge40\) first-defect closure is independently re-certified.

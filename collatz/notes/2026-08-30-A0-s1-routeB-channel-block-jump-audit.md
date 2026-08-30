# A0 s=1 Route-B exact channel-block jump audit — 2026-08-30

## Purpose

Close the exact arithmetic primitive required by a target-aware lazy block decoder.

The existing prefix-channel transducer refines one parity bit at a time. This audit asks whether an already summarized parity block can refine the same channel in one exact jump without materializing or replaying its bits.

This is a structural/computational certificate only. It does **not** prove universal Route-B membership and does **not** prove the Collatz conjecture.

## Parent channel

For an already certified prefix of depth `h`, write

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m.
\]

The exact channel state is `(h,r,y,q)`.

## Intrinsic block state

For a parity block `B` of length `ell`, odd count `q_B`, and correction `C_B`,

\[
T^{\ell}(Z)=\frac{3^{q_B}Z+C_B}{2^{\ell}}.
\]

Its canonical input residue is

\[
\rho_B\equiv-C_B(3^{q_B})^{-1}\pmod{2^{\ell}}.
\]

The block itself therefore needs only the intrinsic correction summary

\[
(\ell,q_B,C_B)
\]

for this jump arithmetic.

## Exact parameter selection

At the block entrance the current channel value is

\[
Z=y+3^q m.
\]

It follows `B` exactly when

\[
y+3^q m\equiv\rho_B\pmod{2^{\ell}}.
\]

Since `3^q` is invertible modulo `2^ell`, there is exactly one residue class

\[
\boxed{
m_B\equiv(\rho_B-y)(3^q)^{-1}\pmod{2^{\ell}}
}
\]

with `0 <= m_B < 2^ell`.

Writing

\[
m=m_B+2^{\ell}n
\]

selects precisely the subchannel that follows the block.

## Exact jumped channel

Substitution gives

\[
X=r+2^h m_B+2^{h+\ell}n,
\]

so

\[
\boxed{r'=r+2^h m_B},
\qquad
\boxed{h'=h+\ell}.
\]

The endpoint after the block is

\[
T^{h+\ell}(X)
=
\frac{3^{q_B}(y+3^q m_B)+C_B}{2^{\ell}}
+
3^{q+q_B}n.
\]

Therefore

\[
\boxed{
q'=q+q_B
}
\]

and

\[
\boxed{
y'=\frac{3^{q_B}(y+3^q m_B)+C_B}{2^{\ell}}}.
\]

Thus the exact jump is

\[
\boxed{
(h,r,y,q)+(\ell,q_B,C_B)
\longrightarrow
(h+\ell,r',y',q+q_B)
}
\]

with one exact dyadic parameter residue `m_B`.

## Exact interval pullback

If the old parameter is restricted by

\[
L\le m\le U,
\]

then `m=m_B+2^ell n` gives

\[
\boxed{
\left\lceil\frac{L-m_B}{2^{\ell}}\right\rceil
\le n\le
\left\lfloor\frac{U-m_B}{2^{\ell}}\right\rfloor
}.
\]

If the lower bound exceeds the upper bound, the entire block branch is empty and can be rejected without bitwise refinement.

## Certificate

Source:

`collatz/src/A0_s1_routeB_channel_block_jump_certificate.py`

Local exact run:

```text
PASS A0 s=1 Route-B exact channel-block jump certificate
parent_channel X=r+2^h*m; T^h(X)=y+3^q*m
block T^ell(Z)=(3^qB*Z+C_B)/2^ell
selected_parameter mB=(rho_B-y)*(3^q)^(-1) mod 2^ell
jump r'=r+2^h*mB; q'=q+qB
jump_endpoint y'=[3^qB*(y+3^q*mB)+C_B]/2^ell
parent_max_depth 7
block_max_depth 7
jump_checks 65025
lift_checks 260100
interval_checks 260100
composition_checks 48447
formation_audit parent + intrinsic block summary + explicit boundary
axis_audit parameter resolution changes m=mB+2^ell*n; block remains intrinsic
dsd_audit jump equals repeated one-bit refinement on exhaustive audit domain
status EXACT channel-block jump CLOSED; target-aware lazy decoder remains OPEN
```

The finite regression checks every parent/block pair through depth 7, verifies several lifted integers in each selected subchannel, verifies interval pullback, and verifies that sequential jumps over two blocks equal one jump over the composed block.

## Formation Axiom System audit

The parent jump state is formed only from:

- the already formed parent channel;
- the intrinsic block summary `(ell,q_B,C_B)`;
- the explicit concatenation boundary.

No expanded parity word is implicitly required by the jump theorem.

This is an organizational audit. The mathematical validity comes from the exact Collatz affine identities above.

## Axis Property audit

The intrinsic block does not contain the parent's absolute placement coordinate.

Instead, the channel parameter changes resolution by

\[
m=m_B+2^{\ell}n.
\]

So the old coordinate `m` and new coordinate `n` describe the same cylinder family at different dyadic scales. This avoids reintroducing the phase/state explosion previously seen when external placement was internalized into DAG nodes.

## DSD cross-audit

- ✅ exact parent channel is defined;
- ✅ exact intrinsic block correction state is defined;
- ✅ block entrance congruence has one dyadic residue solution;
- ✅ jump agrees with repeated bit refinement on the exhaustive audit domain;
- ✅ finite parameter intervals pull back exactly;
- ✅ two-block sequential jump equals composed-block jump;
- ❌ universal Route-B correction-language membership is not proved;
- ❌ target-aware recursive decoder is not yet certified;
- ❌ Collatz is not proved.

## Updated gate status

- **G1 — CLOSED:** exact correction state.
- **G2 — CLOSED:** correction + phase-critical ballot block composition.
- **G3 — PARTIAL:** recursive block composition exists; target-relevant right-congruence/decoder closure remains open.
- **G4 — IN PROGRESS:** exact channel-block jump primitive is now closed. The remaining work is to connect it to the Christoffel hierarchy and target-aware lazy descent.
- **G5 — OPEN:** universal Route-B membership verdict.

## Next implementation target

Build a target-aware lazy decoder with state conceptually of the form

\[
(\text{channel},\text{hierarchy locator},\text{ballot response},\text{target/boundary constraints}).
\]

At each hierarchy node:

1. test whether the whole summarized block is admissible for the current channel and interval;
2. if yes, apply the exact channel-block jump;
3. if the branch is empty, reject it immediately;
4. if a whole-block decision is insufficient, descend only into the child containing the unresolved critical/mismatch location;
5. retain the 129-node compressed hierarchy instead of materializing the giant threshold word.

The 14-root reduction remains a conditional/optimization checkpoint until its upstream provenance is independently re-certified; it is not needed to validate this jump theorem.

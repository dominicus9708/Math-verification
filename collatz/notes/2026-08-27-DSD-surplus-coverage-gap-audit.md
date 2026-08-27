# DSD surplus formation-domain coverage gap audit

Date: 2026-08-27

Status: **OPEN FORMATION-DOMAIN GAP / NO CONTRADICTION TO SAFE LEMMAS / COLLATZ NOT PROVED**

## 1. Audit target

The current `A0` first-crossing structural lemma carries the checkpoint surplus

\[
s=q_{10J_0}-10R_0\ge1.
\]

Thus its formation domain is the union

\[
\mathcal F_{\ge1}
=\bigcup_{s\ge1}\mathcal F_s.
\]

The active Hensel/Bellman terminal-recovery program has so far concentrated on the minimal-surplus sector

\[
\mathcal F_1.
\]

The DSD formation-domain audit asks whether the edge

\[
\mathcal F_{\ge1}\longrightarrow\mathcal F_1
\]

is actually a theorem.

It is not presently established.

Therefore the global terminal-recovery node must not be identified with the `s=1` calculation.

---

## 2. Exact reason the reduction is nontrivial

For

\[
(A_0,Q_0)=10(J_0,R_0)+(U,P),
\]

with

\[
(U,P)=(9809721694,6189245291),
\]

the tenth-checkpoint surplus satisfies

\[
s\ge1,
\]

and the terminal block has odd count

\[
q_{\mathrm{tail}}=P-s.
\]

The homogeneous factors are

\[
C_{\mathrm{pre}}(s)=3^s e^{-10\delta_J},
\]

\[
C_{\mathrm{tail}}(s)=\frac{e^{\delta_U}}{3^s},
\]

while

\[
C_{\mathrm{pre}}(s)C_{\mathrm{tail}}(s)
=e^{-\delta_A}
\]

is independent of `s`.

That cancellation is not enough to prove `s=1` extremality, because the affine composition is

\[
S_{\mathrm{full}}
=S_{\mathrm{pre}}
+\frac{S_{\mathrm{tail}}}{C_{\mathrm{pre}}(s)}.
\]

Changing `s` changes at least all of the following simultaneously:

1. the prefix homogeneous excursion;
2. the terminal homogeneous contraction;
3. the terminal odd count `P-s`;
4. the admissible parity words;
5. the Hensel congruence/displacement classes;
6. the prefix and tail affine corrections.

Hence

\[
C_{\mathrm{pre}}C_{\mathrm{tail}}\text{ independent of }s
\]

does **not** imply

\[
\mathcal T_s^{\mathrm{Hensel}}
\ge
\mathcal T_1^{\mathrm{Hensel}}
\qquad(s\ge2).
\]

---

## 3. Missing theorem

To use the `s=1` Hensel calculation as a theorem about all `A0` first crossings, at least one of the following must be proved independently.

### Route A — extremality

\[
\boxed{
\inf_{s\ge1}\mathcal T_s^{\mathrm{Hensel}}
=
\inf\mathcal T_1^{\mathrm{Hensel}}.
}
\]

### Route B — uniform lower bound

Find `L` such that

\[
\boxed{
\mathcal T_s^{\mathrm{Hensel}}\ge L
\quad\text{for every admissible }s\ge1.
}
\]

The bound need not prove that `s=1` is extremal.

### Route C — audited surplus partition

Partition

\[
\{s\ge1\}=S_1\sqcup S_2\sqcup\cdots
\]

into finitely or recursively controlled sectors and prove the required Hensel/recovery bound separately in each sector.

No one of these three routes is presently SAFE.

---

## 4. Basic range observation does not close the gap

Since the terminal odd count is nonnegative,

\[
P-s\ge0,
\]

so algebraically

\[
1\le s\le P.
\]

This only makes the surplus range finite in a vacuous astronomical sense. It does not justify a scan and does not supply an extension theorem or a monotonicity theorem.

No stronger upper bound on `s` is asserted here unless independently proved from the prefix-survival and Hensel constraints.

---

## 5. Circularity lock

The downstream near-root recovery budget must **not** be used to discard `s\ge2` while constructing the Hensel lower bound that will later be compared with that same budget.

Forbidden proof loop:

\[
D_{\mathrm{allowed}}
\Longrightarrow
\text{only }s=1\text{ matters}
\Longrightarrow
L_{\mathrm{Hensel}}
\Longrightarrow
L_{\mathrm{Hensel}}>D_{\mathrm{allowed}}.
\]

The surplus-coverage theorem must be proved using upstream/local information only.

Allowed direction:

\[
\boxed{
\text{ordering/Hensel structure}
\longrightarrow
\text{uniform surplus coverage}
\longrightarrow
\text{independent budget comparison}.
}
\]

---

## 6. DSD classification

The canonical proof-control graph must be split as follows.

### `C6A` — minimal-surplus Hensel sector

Formation domain:

\[
\mathcal F_1.
\]

Status: **OPEN**.

Target: a monotone finite-depth-to-full Hensel lower bound for `s=1`.

### `C6B` — surplus coverage bridge

Formation domain:

\[
\mathcal F_{\ge1}.
\]

Status: **OPEN**.

Target: prove Route A, B, or C above so that every `s\ge1` terminal-recovery sector is routed.

### `C7` — recovery-budget comparison

`C7` may consume a full-domain result only after `C6B` is available.

A theorem in `C6A` alone cannot close the complete `A0` terminal-recovery language.

---

## 7. Audit verdict

\[
\boxed{
\mathcal F_1\subsetneq_{\text{proof coverage}}\mathcal F_{\ge1}
}
\]

means: the currently proved/targeted `s=1` module is only a subdomain of the formation domain emitted by the `A0` structural lemma. This is a proof-control coverage gap, not a counterexample to any existing SAFE lemma.

The DSD audit therefore blocks the promotion

\[
\text{`s=1` Hensel closure}
\Longrightarrow
\text{all `A0` terminal recoveries closed}
\]

until a separate surplus-coverage theorem is proved.

This is precisely the kind of silent domain loss that the DSD algorithm audit is intended to expose.

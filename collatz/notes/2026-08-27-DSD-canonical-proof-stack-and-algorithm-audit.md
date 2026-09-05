# DSD canonical proof stack and adversarial algorithm audit — Collatz

Date: 2026-08-27

Status: **AUDIT FRAMEWORK / COLLATZ CONJECTURE NOT PROVED**

This file is the canonical proof-control ledger for the active Collatz program. It imports the DSD-style algorithm audit used in the Navier–Stokes project: formation-domain declaration, state preservation, explicit escape routing, acyclic dependencies, adversarial anti-proof checks, and strict separation of `SAFE`, `CONDITIONAL`, `OPEN`, and `REJECTED` claims.

\[
\boxed{\text{THE COLLATZ CONJECTURE REMAINS UNPROVED.}}
\]

---

# 1. DSD audit semantics

Every live module must declare:

1. **formation domain** — exactly which integers / parity words / residue classes enter it;
2. **state** — every datum needed downstream;
3. **transition** — the proved local implication;
4. **exit set** — every branch left alive by the implication;
5. **claim type** — `SAFE`, `CONDITIONAL`, `OPEN`, or `REJECTED`;
6. **dependencies** — upstream modules only.

The governing rules are

\[
\boxed{
\text{downstream exact algebra may survive a broken entry edge only as CONDITIONAL},
}
\]

and

\[
\boxed{
\text{a consumer may not silently cover a larger formation domain than it proves}.}
\]

---

# 2. Canonical proof/control DAG

## `C0` — external finite base + minimal-counterexample normalization

**Status:** SAFE given the retained published external verification input.

For a hypothetical minimal counterexample,

\[
N>2^{71},
\qquad
N\equiv3\pmod4.
\]

A stronger live computation may not silently replace the published threshold used by an existing certificate.

---

## `C1` — first global resonance / near-return

**Status:** SAFE on `C0`.

\[
(A_0,Q_0)=(114208327604,72057431991).
\]

With

\[
y=T^{A_0}(N)=N+g,
\]

one has

\[
\boxed{
g\in4\mathbb Z_{>0},\qquad0<g<2^{33}.}
\]

This line does not use the broken ternary-selector entry theorem.

---

## `C2` — phase-renewal splitter at `K1`

**Status:** SAFE splitter.

\[
(K_1,P_1)=(103768467013,65470613321),
\]

\[
(J_0,R_0)=(10439860591,6586818670),
\]

\[
(A_2,Q_2)=(217976794617,137528045312).
\]

The branch split is

\[
q_{K_1}(y)=P_1
\]

or

\[
q_{K_1}(y)\ge P_1+1.
\]

The two children must remain separate.

---

## `C2E` — exact second lower resonance

**Status:** SAFE branch theorem.

On

\[
q_{K_1}(y)=P_1,
\]

write

\[
z=T^{A_2}(N)=N+h.
\]

Then

\[
\boxed{
h\in4\mathbb Z_{>0},\qquad2^{33}<h<7\cdot2^{33}.}
\]

This is the branch consumed by the present `J0/A0` near-root line.

---

## `E2S` — `K1` surplus-recovery escape

**Status:** OPEN.

Formation domain:

\[
q_{K_1}(y)\ge P_1+1.
\]

The exact-resonance analysis does not eliminate this complement. It remains an explicit global escape until independently routed.

---

## `C3` — repaired local resonance/gap corridor

**Status:** SAFE on `C2E`.

Let

\[
G=2^{33}.
\]

The current exact finite-scale structure includes:

\[
\Delta_J>2.527G,
\]

at an actual primitive `J0` crossing; two consecutive `J0` debits reduce the root-relative gap below `2G`; after those two debits the complete sub-`A0` Worley–Dujella audit promotes the next possible scale to `A0`.

For the `A0/J0` activation budget,

\[
a_A/G\approx0.5022073893714335,
\]

\[
a_J/G\approx2.5270212947568598,
\]

and

\[
\boxed{5a_A<a_J}.
\]

For `1\le m\le10`, the activation index is

\[
\boxed{k_m=5m-3}.
\]

These are deterministic weighted-transition facts. They do not prove that a `J0` resonance must eventually be chosen.

---

# 3. Critical local/global split at `A0`

## `C4F` — local `A0` formation grammar

**Status:** SAFE on its stated local formation domain.

**Formation domain:** any parity word satisfying the `A0` first-crossing conditions.

This node intentionally does **not** know the global near-root recovery budget or whether a hypothetical counterexample actually reaches this word.

The exact decomposition is

\[
\boxed{(A_0,Q_0)=10(J_0,R_0)+(U,P)},
\]

\[
(U,P)=(9809721694,6189245291).
\]

At the tenth `J0` checkpoint,

\[
s=q_{10J_0}-10R_0\ge1,
\]

and the terminal `U` block has

\[
q_{\rm tail}=P-s.
\]

The homogeneous factors are

\[
C_{\rm pre}(s)=3^s e^{-10\delta_J},
\qquad
C_{\rm tail}(s)=e^{\delta_U}3^{-s},
\]

with

\[
C_{\rm pre}(s)C_{\rm tail}(s)=e^{-\delta_A}<1.
\]

At minimal surplus `s=1`, the forced prefix coefficient excursion exceeds `2.99` times the local start.

The full normalized affine correction composes as

\[
\boxed{
S_{\rm full}
=S_{\rm pre}
+\frac{S_{\rm tail}}{C_{\rm pre}(s)}.
}
\]

The cancellation of the homogeneous `s` factors does not imply affine/Hensel monotonicity in `s`.

---

## `C4R` — global route into the `A0` grammar

**Status:** SAFE routing/reduction node on the branch where an actual `A0` first crossing is reached.

Dependencies:

\[
(C3,C4F)\to C4R.
\]

This node carries the global state

\[
(N,\text{root-relative gap},\text{active resonance scale})
\]

and instantiates a local `C4F` word only after the `A0` event is established.

Its exits are:

1. finite terminal recovery;
2. `E4C` — infinite consecutive `A0` returns, classified as a nontrivial positive cycle;
3. `E4L` — leave the present `A0` language toward later finite/infinite coefficient-survivor behavior.

---

# 4. Independent Hensel channel

## `C5` — ordering-only Bellman relaxation

**Status:** SAFE local lemma / exact finite certificate.

For a binary gap word

\[
w=(g_1,\ldots,g_n),\qquad g_i\in\{1,2\},
\]

the ordering-only cost has exact closed form

\[
\boxed{
B_w(p)
=
2A_{m_w(p)}
-6\,2^{-p}
\left[\left(\frac32\right)^{m_w(p)}-1\right].
}
\]

The exact Hensel problem only satisfies the relaxation inequality

\[
\boxed{\mathcal T_w^{\rm Hensel}\ge B_w(p).}
\]

`C5` is independent of the global near-root `A0/J0` gap channel.

---

## `C6A` — minimal-surplus Hensel sector

**Status:** OPEN.

Formation domain:

\[
s=1.
\]

Dependencies:

\[
(C4F,C5)\to C6A.
\]

Target a monotone hierarchy

\[
\mathcal T_{w,1}^{\rm Hensel}
\ge B_{w,1}^{(h+1)}
\ge B_{w,1}^{(h)}
\ge B_w.
\]

Finite-depth computation is only a finite-depth theorem unless an explicit extension/stabilization theorem upgrades it.

---

## `C6B` — all-surplus Hensel coverage

**Status:** OPEN and logically separate from `C6A`.

Formation domain:

\[
s\ge1.
\]

Dependencies:

\[
(C4F,C5)\to C6B.
\]

At least one of the following must be proved:

1. `s=1` extremality,
   \[
   \inf_{s\ge1}\mathcal T_s^{\rm Hensel}
   =\inf\mathcal T_1^{\rm Hensel};
   \]
2. a uniform all-surplus lower bound;
3. an audited partition of every admissible surplus sector.

No current theorem establishes the promotion

\[
C6A\Longrightarrow C6B.
\]

---

# 5. First legal meeting of the two channels

## `C7` — independent recovery-budget comparison

**Status:** OPEN.

The local Hensel channel and global near-root channel are kept separate until

\[
\boxed{(C4R,C6B)\to C7.}
\]

The desired comparison has the form

\[
\boxed{
\inf\mathcal T^{\rm Hensel}>D_{\rm allowed}.
}
\]

Forbidden circular pattern:

\[
D_{\rm allowed}
\to\text{discard surplus/residue states}
\to L_{\rm Hensel}
\to L_{\rm Hensel}>D_{\rm allowed}.
\]

The Hensel lower bound must be obtained without reading `C4R`'s downstream budget data.

---

# 6. Global escape ledger

## `E4C` — nontrivial-cycle escape

The implication

\[
\text{infinite consecutive A0-only endpoint language}
\Longrightarrow
\text{nontrivial positive Collatz cycle}
\]

is SAFE.

Exclusion of every resulting cycle is OPEN unless an independently applicable theorem closes it.

## `E4L` — later-scale / infinite-survivor escape

**Status:** OPEN.

This includes leaving the present `A0` language, a later finite coefficient crossing, or an infinite coefficient-survivor state not already closed by the current resonance grammar.

## `C8` — global branch completeness

**Status:** OPEN.

A global closure node must consume at least

\[
\boxed{C7,\ E2S,\ E4C,\ E4L.}
\]

Closing the terminal-recovery branch alone cannot prove Collatz.

---

# 7. Quarantined selector branch

## `Q1` — Ansari recursive-sufficiency entry

**Status:** CONDITIONAL / published entry argument broken as used.

The induction equality fails already at `n=1`.

\[
F_1\setminus F_2
=(36\mathbb N_0+27)\cup(36\mathbb N_0+31).
\]

The `36k+31` progression has a smaller recursive predecessor, while `36k+27` remains unrepaired.

Thus

\[
\boxed{
\text{minimal counterexample}
\not\Rightarrow_{\rm currently\ proved}
\text{ternary }\{0,1\}\text{ selector family}.
}
\]

## `Q2` — downstream selector/Fourier/carry/same-address calculations

**Status:** CONDITIONAL.

These calculations may remain exact inside the fixed selector family, but they cannot feed the SAFE spine until `Q1` is repaired or made unnecessary.

---

# 8. Adversarial anti-proof attacks

Every future module is attacked with all of the following.

### A1 — formation-domain attack

Does every object emitted upstream actually enter the claimed downstream module?

Current detected example:

\[
C4F:\ s\ge1
\]

was wider than the original Hensel target

\[
C6A:\ s=1.
\]

This forced creation of `C6B`.

### A2 — state-loss attack

A compressed state may not reconstruct discarded coordinates later without a theorem.

The current live state channels include at least:

\[
\text{global}: (N,d,\text{scale},\text{active resonances}),
\]

\[
\text{local word}: (j,q_j,s,\text{parity prefix}),
\]

\[
\text{Hensel}: (p,\text{congruence/displacement state}).
\]

### A3 — reverse-dependency / circularity attack

The near-root budget may not construct the Hensel lower bound that is later compared against that same budget.

### A4 — quantifier attack

Distinguish exactly:

- one word vs all admissible words;
- one surplus sector vs all `s\ge1`;
- one residue class vs every integer in the domain;
- finite depth vs arbitrary depth;
- finite scan vs infinite language;
- density/almost-all vs every hypothetical counterexample;
- local endpoint return vs global first descent.

### A5 — extension attack

\[
\boxed{\text{finite Hensel search}\not\Rightarrow\text{infinite Hensel closure}.}
\]

\[
\boxed{\text{finite resonance table}\not\Rightarrow\text{no later resonance}.}
\]

### A6 — branch-completeness attack

Every split creates explicit complements. Consuming one child never erases the others.

### A7 — external-theorem hypothesis attack

Record exact map convention, domain, threshold, strictness, cycle-length convention, publication status, and exact invocation point.

### A8 — numerical-to-exactness attack

Decisive strict inequalities must reduce to exact integer/rational arithmetic or directed certified bounds. Resonance near-equalities receive mandatory exact checking.

---

# 9. Audit locks

Do not use without a new theorem:

1. repeated local `L7/L14/L19` residue-maximality as a root-predecessor theorem;
2. Ansari recursive sufficiency as unconditional selector entry;
3. m44/m45 selector results as unconditional facts about all counterexamples;
4. finite Hensel scans as infinite closure;
5. local same-address coincidence as global descent;
6. `A0`-only cycle classification as exclusion of all nontrivial cycles;
7. `5a_A<a_J` as proof that a `J0` debit must eventually occur;
8. activation of `mJ0` as proof that the orbit chooses that resonance;
9. `s=1` Hensel results as all-`s` closure;
10. `C4R` near-root budget data as an input to `C6A/C6B`;
11. one phase-renewal child as closure of its complementary child;
12. computational verification below a threshold as a theorem about all larger integers.

---

# 10. Algorithmic audit protocol

Every new lemma/certificate follows:

1. `P0 DECLARE` — formation domain, state, target, dependencies, external inputs;
2. `P1 PROVE LOCALLY` — no downstream contradiction/budget may be used;
3. `P2 REPRODUCE` — exact or directed-bound certificate and explicit scope;
4. `P3 ATTACK` — run A1–A8 and deliberately search at least one complement/escape;
5. `P4 CLASSIFY` — assign `SAFE`, `CONDITIONAL`, `OPEN`, or `REJECTED`;
6. `P5 ROUTE EXITS` — no branch silently disappears;
7. `P6 UPDATE DAG` — add forward dependencies only; a cycle is an audit failure;
8. `P7 PROMOTE CAUTIOUSLY` — only an all-SAFE upstream path may enter the SAFE spine.

The executable companion is

`collatz/src/dsd_dependency_dag_audit.py`.

The dedicated surplus scope certificate is

`collatz/src/dsd_surplus_scope_gap_certificate.py`.

---

# 11. Current DSD verdict

### SAFE / structurally clean

- first-resonance near-return line on its stated inputs;
- exact second-resonance child and near-root annulus;
- finite-scale `J0/A0` debit/activation lemmas;
- local `A0` ten-checkpoint surplus grammar `C4F`;
- ordering-only Bellman relaxation `C5`;
- selector branch quarantine;
- local/global `A0` state split;
- explicit escape ledger and acyclic proof-control graph.

### OPEN live gates

\[
\boxed{C6A:\ s=1\text{ finite-depth/full-Hensel refinement}}
\]

\[
\boxed{C6B:\ \text{all-surplus Hensel coverage}}
\]

\[
\boxed{C7:\ \text{independent recovery-budget comparison}}
\]

\[
\boxed{E2S:\ K_1\text{ surplus-recovery branch}}
\]

\[
\boxed{E4C:\ \text{nontrivial-cycle exclusion}}
\]

\[
\boxed{E4L:\ \text{later/infinite coefficient-survivor routing}}
\]

\[
\boxed{C8:\ \text{global branch completeness}}
\]

The important new audit result is not a proof of Collatz but a stricter proof architecture: the `s=1` scope leak and the coarse local/global `A0` dependency have been isolated before they could be used as hidden assumptions.

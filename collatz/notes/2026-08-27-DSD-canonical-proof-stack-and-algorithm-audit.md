# DSD canonical proof stack and adversarial algorithm audit — Collatz

Date: 2026-08-27

Status: **AUDIT FRAMEWORK / COLLATZ CONJECTURE NOT PROVED**

Purpose: import the DSD-style algorithm audit used in the Navier–Stokes project into the Collatz proof program. The objective is not to create a new axiom or to promote computational evidence into proof. It is to compress the live argument into a directed theorem stack, preserve rejected/conditional branches as audit evidence, and actively search for missing formation-domain edges, hidden reverse dependencies, and un-routed escape branches.

\[
\boxed{\text{THE COLLATZ CONJECTURE REMAINS UNPROVED.}}
\]

---

## 0. DSD audit semantics

Every live module is represented by five fields:

1. **formation domain** — exactly which integers / parity words / residue classes the module applies to;
2. **state** — the mathematical data carried into the module;
3. **transition** — the proved map from input state to output state;
4. **exit set** — every branch that may leave the module;
5. **claim type** — `SAFE`, `CONDITIONAL`, `OPEN`, or `REJECTED`.

The governing rule is:

\[
\boxed{
\text{a downstream calculation may survive even when its upstream entry edge fails,}
}
\]

but it must then be downgraded to a conditional calculation on its explicitly stated formation domain.

This is exactly the correction applied to the Ansari / ternary-selector branch.

---

# Canonical proof stack

## C0. External finite base and minimal-counterexample normalization

**Claim type:** SAFE GIVEN EXTERNAL THEOREM INPUTS / EXTERNAL HYPOTHESES MUST BE REAUDITED.

Use only the published finite verification threshold retained by the certificates:

\[
N>2^{71}
\]

for a hypothetical minimal counterexample.

Elementary minimality gives

\[
N\equiv3\pmod4.
\]

This module is an entry normalization, not a global proof step.

**State:** `N`, its parity orbit, and the first-descent prohibition below `N`.

**Audit lock:** a larger live computational verification threshold may strengthen numerics, but must not silently replace the published input used in an existing certificate.

---

## C1. First global coefficient resonance and near-return gap

**Claim type:** SAFE DERIVED REDUCTION, CONDITIONAL ONLY ON C0 EXTERNAL INPUTS.

The first global coefficient crossing is

\[
(A_0,Q_0)
=(114208327604,72057431991).
\]

If

\[
y=T^{A_0}(N)=N+g,
\]

then the repaired first-crossing / correction argument gives

\[
\boxed{
g\in4\mathbb Z_{>0},\qquad0<g<2^{33}.}
\]

This branch uses no ternary-selector entry theorem and no repeated local pullback.

**State:**

\[
(N;A_0,Q_0;g).
\]

**Exit set:** finite second crossing, coefficient survival beyond the current scale, or a cycle branch where separately justified.

---

## C2. Phase renewal and repaired second-resonance annulus

**Claim type:** SAFE BRANCH REDUCTION.

Let

\[
(K_1,P_1)=(103768467013,65470613321),
\]

\[
(J_0,R_0)=(10439860591,6586818670),
\]

and

\[
(A_2,Q_2)=(217976794617,137528045312).
\]

The phase-renewal bridge gives a two-way branch at `K1` from the first endpoint:

1. coefficient-surplus recovery;
2. exact second lower resonance `q_{K1}=P1`.

On the exact second-resonance branch, with

\[
z=T^{A_2}(N)=N+h,
\]

one has

\[
\boxed{h\in4\mathbb Z_{>0},\qquad2^{33}<h<7\cdot2^{33}.}
\]

**Audit requirement:** the surplus-recovery branch and the exact-resonance branch remain separate until a theorem reconnects them.

---

## C3. Local resonance/gap transition system

**Claim type:** SAFE FINITE-SCALE TRANSITION LEMMAS.

The local state is not merely a residue class. The DSD state is

\[
\boxed{
(\text{gap band},\text{active resonance multiplicities},\text{current scale}).
}
\]

The proved transition structure includes:

- a local `J0` debit satisfying
  \[
  \Delta_J>2.527\,G,\qquad G=2^{33};
  \]
- two `J0` debits promote the next possible subcritical scale to `A0`;
- one promoted `A0` return preserves the immediate `J0` exclusion;
- `A0` maximum credit `a_A` and `J0` minimum debit `a_J` satisfy
  \[
  \boxed{5a_A<a_J};
  \]
- the activation ladder for `mJ0`, `1\le m\le10`, is
  \[
  \boxed{k_m=5m-3}.
  \]

This is a weighted deterministic transition system, not a probabilistic density argument.

**Audit lock:** local residue-maximality is not a root-predecessor theorem. Any local-to-global pullback must separately discharge the `3^p` divisibility / Hensel compatibility requirement.

---

## C4. Internal structure of an `A0` first crossing

**Claim type:** SAFE LOCAL STRUCTURAL LEMMA.

The exact Euclidean decomposition is

\[
\boxed{(A_0,Q_0)=10(J_0,R_0)+(U,P)}
\]

with

\[
(U,P)=(9809721694,6189245291).
\]

For an `A0` first-crossing word, the ten `J0` checkpoints force surplus

\[
s=q_{10J_0}-10R_0\ge1,
\]

and the terminal `U` block has odd count

\[
q_{\rm tail}=P-s.
\]

The ten-`J0` prefix must make an internal excursion satisfying at least

\[
\boxed{T^{10J_0}(X)>2.99X}
\]

at minimal surplus `s=1`, while the terminal block must recover to the near-root endpoint.

An infinite sequence of consecutive `A0` endpoint returns remains in a finite affine interval and therefore repeats; hence

\[
\boxed{
\text{infinite A0-only endpoint language}
\Longrightarrow
\text{nontrivial positive Collatz cycle}.
}
\]

**Audit lock:** this classifies the infinite `A0`-only escape. It does not exclude every nontrivial cycle and must not be used as though it did.

---

## C5. Acyclic ordering-only Bellman lower-bound layer

**Claim type:** SAFE LOCAL LEMMA / EXACT FINITE CERTIFICATE.

For a gap word

\[
w=(g_1,\ldots,g_n),\qquad g_i\in\{1,2\},
\]

remove Hensel congruence conditions but retain ordering. With

\[
p_i=\max(0,p-N_2(i)),
\]

the ordering-only defect cost has exact closed form

\[
\boxed{
B_w(p)
=
2A_{m_w(p)}
-6\,2^{-p}
\left[\left(\frac32\right)^{m_w(p)}-1\right].
}
\]

The exact Hensel problem satisfies only the relaxation inequality

\[
\boxed{\mathcal T_w^{\rm Hensel}\ge B_w(p).}
\]

No near-root budget and no `A0/J0` contraction is used to derive `B_w`.

**Dependency direction is locked:**

\[
\boxed{
\text{ordering}
\to
\text{finite-depth Hensel}
\to
\text{full Hensel lower bound}
\to
\text{independent near-root budget comparison}.
}
\]

---

## C6. Finite-depth Hensel refinement hierarchy

**Claim type:** OPEN.

Construct certified lower bounds

\[
\boxed{
\mathcal T_w^{\rm Hensel}
\ge B_w^{(h+1)}
\ge B_w^{(h)}
\ge B_w.
}
\]

The first `h` congruence decisions must be enforced exactly, while only the suffix is relaxed.

A finite computation is admissible only as a finite-depth theorem unless an explicit extension / stabilization theorem upgrades it.

**Current gate:** derive a nontrivial monotone Hensel lower-bound sequence for the `s=1` terminal-recovery sector.

---

## C7. Independent recovery-budget comparison

**Claim type:** OPEN MAIN GAP FOR THE CURRENT `A0`-DOMINANT BRANCH.

Only after C6 has been independently derived may one compare it with the near-root defect budget.

The desired form is

\[
\boxed{
\inf\mathcal T^{\rm Hensel}>D_{\rm allowed}.
}
\]

If established with independent inputs, the corresponding terminal-recovery language closes.

If the inequality fails or is not proved, the branch remains OPEN. Numerical proximity is not a proof substitute.

---

## C8. Global escape completeness

**Claim type:** OPEN GLOBAL BRANCH-COMPLETENESS AUDIT.

Even closing C7 would not by itself prove Collatz. The proof tree must still account for every escape from the current resonance language, including at least:

1. coefficient survival through `A0` to later finite scales;
2. an infinite coefficient-survivor branch;
3. nontrivial cycle branches not eliminated by an independently applicable cycle theorem;
4. any Hensel-compatible local branch not represented by the current `J0/A0` macro language;
5. the conditional ternary-selector family, unless its upstream entry theorem is repaired or rendered unnecessary.

The global conjecture can be promoted only after this exit set is exhaustive and every member is closed.

---

# Dependency graph

The current allowed main direction is

\[
\boxed{
C0
\to C1
\to C2
\to C3
\to C4
\to C5
\stackrel{\mathbf{C6\ OPEN}}{\longrightarrow}
C7
\stackrel{\mathbf{C8\ OPEN}}{\longrightarrow}
\text{global closure}.
}
\]

Some arrows are structural organization rather than logical implication between every lemma; any actual theorem invocation must cite its exact prerequisites.

The ternary-selector branch is not on this unconditional spine.

---

# Conditional / quarantined branch

## Q1. Ansari recursive-sufficiency → ternary selector

**Claim type:** CONDITIONAL / ENTRY EDGE BROKEN AS PUBLISHED.

The equality used in the published recursive-sufficiency induction fails already at `n=1`. The progression

\[
36\mathbb N_0+31
\]

has been repaired as recursive, while

\[
36\mathbb N_0+27
\]

remains the first unrepaired class.

Therefore

\[
\boxed{
\text{minimal counterexample}
\not\Rightarrow_{\rm currently\ proved}
\text{ternary }\{0,1\}\text{ selector family}.
}
\]

Downstream m44/m45 selector, Fourier, carry, same-address and related finite calculations may remain algebraically correct on that family, but are quarantined from the unconditional spine.

---

# Adversarial anti-proof audit

The audit must actively try to falsify each reduction rather than merely rerun its certificate.

## A1. Formation-domain attack

For every edge `X -> Y`, ask:

> Is every object admitted by X actually shown to enter Y?

Failure mode already observed: global minimal counterexample → ternary selector family.

Required output: either a proof of the entry edge, or downgrade Y to CONDITIONAL.

## A2. State-loss attack

Ask whether a compression discards data needed later.

For the present resonance line, the retained state must include at least

\[
(\text{scale},\text{gap},\text{odd-count surplus},\text{active resonance set},\text{Hensel displacement}).
\]

A transition proved only after forgetting one of these coordinates cannot later reconstruct it for free.

## A3. Reverse-dependency / circularity attack

Forbidden cycles include:

- near-root budget `->` Hensel lower bound `->` near-root contradiction;
- `A0/J0` macro contraction `->` local Hensel bound used to justify the same contraction;
- local residue survival `->` global predecessor theorem `->` local residue survival;
- assuming absence of a later-scale escape in order to prove that no later-scale escape exists.

Every new proof note must provide an acyclic dependency list.

## A4. Quantifier attack

Explicitly distinguish:

- one word vs all admissible words;
- one residue class vs every integer in the formation domain;
- finite depth vs arbitrary depth;
- finite search vs an infinite language;
- density-one / almost-all results vs every hypothetical counterexample;
- local endpoint return vs global first descent.

Changing one quantifier requires a theorem, not a notation change.

## A5. Extension attack

A finite certificate establishes only what it enumerates unless a proved extension theorem is attached.

In particular:

\[
\boxed{
\text{finite Hensel search}
\not\Rightarrow
\text{infinite Hensel closure}
}
\]

and

\[
\boxed{
\text{finite resonance table}
\not\Rightarrow
\text{no later resonance}.
}
\]

## A6. Branch-completeness attack

Whenever a branch is eliminated, construct its complement explicitly and ask whether the complement was routed.

Example:

\[
\text{A0-only forever}
\to
\text{cycle}
\]

leaves the divergent branch with the complement

\[
\text{activated lower resonance}
\lor
\text{survival beyond A0}
\lor
\text{later crossing / other language}.
\]

These exits must remain visible until individually closed.

## A7. External-theorem hypothesis attack

Every external result must be recorded with:

- exact map convention;
- domain (`positive integers`, shortcut map, etc.);
- threshold and whether strict/non-strict;
- cycle-length convention (total steps, odd members, local minima, ...);
- publication status;
- exact place where the theorem is invoked.

A stronger recent computational claim does not automatically inherit the hypotheses of an older certificate.

## A8. Numerical-to-exactness attack

Decimal values may guide search, but every decisive strict inequality must be reducible to exact integer/rational arithmetic or directed certified bounds.

Near-equality at a resonance is especially high risk and receives mandatory exact auditing.

---

# Audit locks

Do not use the following without a new theorem:

1. repeated local `L7/L14/L19` residue-maximality as a root-predecessor theorem;
2. Ansari recursive sufficiency as an unconditional global selector-entry theorem;
3. m44/m45 selector conclusions as unconditional facts about all Collatz counterexamples;
4. finite Hensel scans as infinite closure;
5. local same-address coincidence as global descent;
6. an `A0`-only cycle classification as exclusion of all nontrivial cycles;
7. `5a_A<a_J` as proof that a `J0` debit must eventually occur;
8. activation of `mJ0` as proof that the orbit actually chooses that resonance;
9. near-root gap bounds as input to the Hensel lower bound they are later compared against;
10. computational verification below a threshold as a theorem about all larger integers.

---

# Algorithmic audit protocol for every future module

Each new lemma/certificate must be processed in this order:

### P0 — Declare

Record formation domain, exact hypotheses, state variables, target conclusion, external inputs.

### P1 — Prove locally

Derive the claimed transition without using any downstream budget or desired contradiction.

### P2 — Reproduce

Provide exact or directed-bound certificate where computation is involved. The certificate must print its scope.

### P3 — Attack

Run the eight anti-proof attacks above. At least one deliberate complement / escape search is required.

### P4 — Classify

Assign exactly one status:

- `SAFE`: theorem/certificate proved on its stated domain and all invoked prerequisites are available;
- `CONDITIONAL`: local result is valid but one or more upstream entry edges are unproved;
- `OPEN`: target implication is not proved;
- `REJECTED`: a claimed implication or computation is false / invalid as stated.

### P5 — Route exits

List every surviving branch. No branch is silently discarded.

### P6 — Update DAG

Add only forward dependencies. A dependency cycle is an audit failure requiring refactoring before the result is used.

### P7 — Promote cautiously

A result enters the unconditional spine only if every upstream edge is SAFE. Otherwise it remains quarantined even if its internal computation is exact.

---

# Current DSD audit verdict

The present unconditional work has made genuine structural progress:

- the false/unsupported ternary selector entry has been quarantined instead of contaminating downstream algebra;
- the global first resonance and near-return channel are independent of that selector;
- the `J0/A0` gap system is now a finite-state weighted transition language at the audited scales;
- the `A0` block has a forced internal surplus/recovery structure;
- the ordering-only Bellman layer is deliberately acyclic.

But the canonical stack exposes two principal live gates:

\[
\boxed{C6:\ \text{finite-depth Hensel lower-bound refinement}}
\]

and

\[
\boxed{C8:\ \text{global escape / branch completeness}.}
\]

Closing only the first without the second would still not prove the conjecture.

This file is therefore a proof-control ledger and adversarial audit specification, not a Collatz proof claim.

# DSD dependency refinement — split local `A0` grammar from global near-root routing

Date: 2026-08-27

Status: **SAFE PROOF-CONTROL REFACTOR / MATHEMATICAL CLAIMS UNCHANGED / COLLATZ NOT PROVED**

## 1. Audit finding

The first DSD dependency DAG used a single node `C4` for two logically distinct kinds of information:

1. the local combinatorial/arithmetic structure of an `A0` first-crossing parity word;
2. the fact that the current global minimal-counterexample branch has actually reached an `A0` sector from the repaired near-root `J0/A0` corridor.

Those facts must be separated before the Hensel lower-bound layer is compared with the near-root recovery budget.

Otherwise a future calculation could silently read a downstream gap bound through the coarse `C4` dependency and later compare its result with the same bound.

---

## 2. Local node `C4F` — formation grammar

Formation domain:

> any parity word satisfying the stated `A0` first-crossing conditions.

This is a local theorem on a word, not a theorem that every global counterexample reaches such a word.

Its exact data include

\[
(A_0,Q_0)=10(J_0,R_0)+(U,P),
\]

\[
(U,P)=(9809721694,6189245291),
\]

and the checkpoint surplus

\[
s=q_{10J_0}-10R_0\ge1,
\]

with terminal odd count

\[
q_{\mathrm{tail}}=P-s.
\]

It also contains the purely local coefficient factorization

\[
C_{\mathrm{pre}}(s)=3^s e^{-10\delta_J},
\qquad
C_{\mathrm{tail}}(s)=e^{\delta_U}3^{-s},
\]

\[
C_{\mathrm{pre}}(s)C_{\mathrm{tail}}(s)=e^{-\delta_A},
\]

and the forced internal excursion bound at minimal surplus.

**Status:** SAFE on its stated local formation domain.

**Forbidden input:** the downstream near-root recovery budget `D_allowed`.

---

## 3. Global node `C4R` — route into the local grammar

Formation domain:

> the repaired exact-second-resonance / `J0/A0` global branch that has reached an actual `A0` first crossing.

This node consumes the earlier near-root resonance/gap analysis and invokes `C4F` only after the `A0` event is established.

It carries global information such as the root-relative endpoint gap and the current resonance/activation state.

Its exits include:

1. finite terminal recovery;
2. infinite consecutive `A0` returns, classified into a nontrivial-cycle exit;
3. leaving the present `A0` language toward later finite/infinite coefficient-survivor states.

**Status:** SAFE as a routing/reduction node on the actual branch where its hypotheses hold.

---

## 4. Correct noncircular Hensel dependency

The Hensel lower-bound modules must read the local grammar, not the global recovery budget:

\[
\boxed{
(C4F,C5)
\longrightarrow
C6A,C6B.
}
\]

Here `C5` is the independent ordering-only Bellman relaxation.

In particular,

\[
\boxed{
C4R\not\longrightarrow C6A,C6B
}
\]

is an audit lock unless a future proof explicitly identifies which upstream datum is imported and proves that doing so does not reuse the downstream comparison budget.

The budget comparison occurs only after an all-surplus Hensel theorem exists:

\[
\boxed{
(C4R,C6B)
\longrightarrow C7.
}
\]

Thus the intended causal order is

\[
\text{local A0 grammar}
\to
\text{Hensel lower bound}
\]

in parallel with

\[
\text{global resonance route}
\to
\text{near-root admissible budget},
\]

followed by one first meeting at `C7`.

---

## 5. DSD interpretation

This is a state-separation correction.

The local state

\[
(\text{parity word},s,\text{Hensel displacement})
\]

and the global state

\[
(N,\text{root-relative gap},\text{active resonance scale})
\]

are different channels.

They may be paired when a global orbit is proved to instantiate the local word, but information from the global gap channel must not be smuggled backward into the local Hensel lower-bound theorem.

---

## 6. Audit verdict

No existing SAFE numerical lemma is rejected by this split.

The correction strengthens proof hygiene by replacing the coarse dependency

\[
C4\to C6\to C7
\]

with two independent upstream channels:

\[
\boxed{
C4F\to C6B\to C7
\quad\text{and}\quad
C3\to C4R\to C7.
}
\]

This makes the forbidden circular pattern

\[
D_{\mathrm{allowed}}
\to L_{\mathrm{Hensel}}
\to D_{\mathrm{allowed}}
\]

structurally visible and therefore machine-auditable.

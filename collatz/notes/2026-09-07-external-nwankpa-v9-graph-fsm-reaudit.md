# Nwankpa v9 graph-theoretic FSM claim — current-version DSD re-audit

Date: 2026-09-07

Source: Amarachukwu Nwankpa, *The Collatz Conjecture: A Graph-Theoretic Structural Proof*, Preprints.org `202503.0929`, **Version 9**, posted 22 October 2025.

Status: **D — CURRENT VERSION RE-AUDITED; CORE QUOTIENT/LIVENESS HINGE STILL FAILS.** The revision changes the presentation to a strongly-connected-component / unique-exit argument, but it does not repair the distinction between existence of a state-graph exit path and inevitability of the actual integer trajectory taking that exit.

This note supersedes the version-specific scope of the 2026-09-06 v6 audit while preserving that audit as historical evidence.

---

## 1. What v9 claims

Version 9 partitions positive integers into a 17-state system and claims:

1. all nonterminal transient states form one strongly connected component (SCC);
2. the only transient state with a direct terminal transition is `S11`;
3. therefore every infinite trajectory must eventually use that exit and reach `{1,2,4}`.

The global conclusion depends on the implication

\[
\boxed{
\text{one transient SCC + an available exit}
\Longrightarrow
\text{every actual trajectory eventually takes the exit}.
}
\]

That implication is false for directed graphs in general and is not repaired by the arithmetic state partition.

---

## 2. The paper's own transition table is not a deterministic quotient map

Lemma 4.4 describes branches such as

\[
S_1\to\{S_7,S_8\}
\]

depending on the hidden parameter `m` in the integer representative. Similar state-level branching occurs elsewhere.

Thus determinism of the integer Collatz map

\[
x\mapsto C(x)
\]

does not induce a function

\[
S_i\mapsto S_j
\]

unless all representatives of each coarse state have successor representatives in one common state.

The correct quotient object is a transition **relation** that forgets arithmetic information.

This is the same well-definedness defect identified in the earlier v6 audit.

**DSD failure: quotient determinism / hidden representative.**

---

## 3. The v9 `unique exit` is representative-specific

Version 9 explicitly states that

\[
S_{11}: x=18k+8
\]

has possible transitions to `S5`, `S6`, and terminal `SC4`, and that the terminal transition occurs only for

\[
k=0,
\qquad x=8,
\qquad C(8)=4.
\]

For every other `S11` representative (`k>0`), the next state returns to the transient SCC.

Therefore

\[
\boxed{
\text{trajectory reaches coarse state }S_{11}
\not\Rightarrow
\text{trajectory reaches }x=8.
}
\]

The graph exit is not an exit that every visit to `S11` must take.

This directly invalidates the phrase `unique exit` as a universal liveness certificate for the represented integer trajectories.

---

## 4. Lemma 4.6 establishes reachability, not inevitability

The backward construction `A_k` in Lemma 4.6 proves that every transient state has **a directed path** to `S11`.

Its logical form is

\[
\forall S\in\mathcal T\;\exists P_S:
P_S\text{ is a graph path from }S\text{ to }S_{11}.
\]

The Collatz theorem would require, at minimum,

\[
\forall x\in\mathbb N\;\exists t:
C^t(x)=8
\]

or a faithful quotient theorem forcing every realizable successor path to the exit representative.

The first statement does not imply the second.

**DSD failure: existential reachability promoted to universal liveness.**

---

## 5. Lemma 4.7's sink-component argument is not valid for a coarse quotient

Version 9 argues that a hypothetical nontrivial integer cycle would form an internal sink component of the finite state graph; since every state has a path to `S11` and `S11` has a terminal exit, such a sink cannot exist.

This conflates recurrence in the integer space with recurrence in a many-to-one quotient.

A cycle of integer representatives need not contain every outgoing edge attached to their coarse state labels. An outgoing graph edge may be realized only by another integer in the same state.

Conversely, a state cycle need not be an integer cycle because distinct integers can share the same state label.

Hence

\[
\boxed{
\text{integer cycle}
\not\equiv
\text{sink SCC of the coarse transition relation}.
}
\]

The existence of an exit edge from a coarse state cannot rule out a trajectory whose hidden representatives always realize internal successors.

---

## 6. Pure graph-theoretic countermodel to the claimed principle

Even abstractly, an SCC with an exit does not force all infinite walks to leave it.

Take vertices `a,b,t` and edges

\[
a\to b,
\qquad
b\to a,
\qquad
b\to t,
\qquad
t\to t.
\]

Then `{a,b}` is strongly connected and has an exit to absorbing `t`, but

\[
a,b,a,b,\ldots
\]

is an infinite internal walk that never takes the exit.

To deduce inevitable absorption one needs an additional property such as:

- a deterministic faithful quotient whose unique successor graph has no nonterminal cycle;
- a rank/Lyapunov function decreasing on every realizable internal transition;
- or an arithmetic theorem showing that hidden representatives cannot keep selecting internal branches forever.

Version 9 supplies none of these bridges.

---

## 7. Finite computation does not repair the universal hinge

The paper reports computational checks through `10^7` starts. Those calculations can verify finite state assignments and observed transitions, but cannot establish the missing universal implication

\[
\text{available exit path}\Rightarrow\text{eventual use of that exit}
\]

for every positive integer.

They are therefore **FINITE EVIDENCE**, not a closure theorem.

---

## 8. What survives and may still be cited

The v9 paper can still be cited for:

1. its explicit modular partition as a coarse descriptive classification;
2. valid case-by-case modular transition relations where the arithmetic derivation is correct;
3. the graph as a diagnostic summary of possible state transitions;
4. finite computational observations within the tested range.

These do not establish the claimed convergence theorem.

---

## 9. Anti-patterns retained for the internal proof program

### FSM-1 — quotient well-definedness

Before a finite partition is called a deterministic dynamical quotient, prove

\[
x\sim y\Longrightarrow C(x)\sim C(y).
\]

### FSM-2 — existential path is not forced path

\[
\forall S\;\exists\text{ path to exit}
\not\Rightarrow
\forall\text{ actual trajectories eventually exit}.
\]

### FSM-3 — exit edge availability is not fairness

A strongly connected directed component may possess an exit while admitting infinite internal walks.

### FSM-4 — coarse state recurrence is not integer recurrence

Repeated finite-state labels do not imply repeated ordinary integers.

---

## 10. Final verdict

\[
\boxed{
\text{Nwankpa v9 global Collatz proof: NOT ESTABLISHED.}
}
\]

The current version still lacks the information-preserving / liveness bridge from the coarse nondeterministic transition relation to every deterministic integer trajectory.

Citation use in this repository is therefore **anti-pattern / negative-control citation**, with the failure restricted to the stated quotient and graph-theoretic closure mechanism rather than a blanket claim about every local lemma in the paper.
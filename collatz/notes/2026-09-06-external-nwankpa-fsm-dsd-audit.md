# DSD audit — Nwankpa 17-state finite-state proof of Collatz

Date: 2026-09-06

Source: Amarachukwu Nwankpa, *A Proof of the Collatz Conjecture via Finite State Machine Analysis and Structural Confinement*, Preprints.org `202503.0929`, v6 (posted 4 April 2025).

Status: **D — CORE QUOTIENT/QUANTIFIER HINGE FAIL.**  The state partition is a finite coarse classification of integers, but the quotient does not define a deterministic state map and the reachability argument proves existential paths rather than inevitability of the actual Collatz path.  The global proof therefore does not follow as written.

---

## 1. State space being audited

The transient-state function is

\[
s(x)=(x\bmod9,\ S(x),\ p(x)),
\]

where `S(x)` records membership in `I` or `X` and `p(x)` records parity.  This yields twelve transient states `S1,...,S12`.

The paper then claims that these states form a deterministic finite-state machine whose graph forces every integer trajectory through gateway `S11` and into `{1,2,4}`.

The distinction that must be audited is:

\[
\boxed{
\text{determinism of }x\mapsto C(x)
\quad\text{vs}\quad
\text{determinism of }s(x)\mapsto s(C(x)).
}
\]

The former does not imply the latter unless all integers in a state have successors in one common next state.

---

## 2. Explicit failure of quotient determinism

Lemma 30 itself lists branched state transitions, for example

\[
S_3\to S_1\text{ or }S_2.
\]

The paper parametrizes

\[
S_3:\quad x=18m+2,\qquad m\ge1.
\]

Take

\[
x_1=20=18\cdot1+2,
\qquad
x_2=38=18\cdot2+2.
\]

Both are in the same state `S3`.

But

\[
C(20)=10,
\]

and `10` belongs to `S1`, whereas

\[
C(38)=19,
\]

and `19` belongs to `S2`.

Therefore

\[
\boxed{
s(20)=s(38)=S_3,
\qquad
s(C(20))\ne s(C(38)).}
\]

Hence there is no function

\[
\bar C:\{S_1,\ldots,S_{12}\}\to\{S_1,\ldots,S_{12},S_C\}
\]

satisfying

\[
\bar C(s(x))=s(C(x))
\]

for every integer `x`.

The quotient is a **nondeterministic transition relation**, not a deterministic finite-state dynamical system.

### DSD verdict

\[
\boxed{
\text{integer-map determinism}
\not\Rightarrow
\text{coarse-state determinism}.}
\]

---

## 3. Lemma 31 proves only trajectory determinism before quotienting

Lemma 31 argues that for each fixed integer `x`, `C(x)` is unique and therefore `getState(C(x))` is unique.

That statement is true but weaker than required.

It has quantifier form

\[
\forall x\ \exists! S'\quad s(C(x))=S'.
\]

A deterministic quotient transition would require

\[
\forall S\ \exists!S'\ \forall x\in S:\ s(C(x))=S'.
\]

The explicit `20/38` example shows that the latter formula is false.

Thus Lemma 31 changes the order of quantifiers when it interprets pointwise determinism as finite-state determinism.

DSD failure type: **QUOTIENT WELL-DEFINEDNESS / QUANTIFIER ORDER**.

---

## 4. Lemma 33 proves existential reachability, not inevitable hitting

The paper defines

\[
A_0=\{S_{11}\},
\]

\[
A_{k+1}=A_k\cup
\left\{S_i:\exists S_j\in A_k
\text{ such that }S_i\to S_j\text{ is a possible transition}\right\}.
\]

For a branching state the paper explicitly assigns the state according to the **shortest path** to `S11`.

Consequently `A_4=S_{1-12}` proves

\[
\boxed{
\forall S\ \exists\text{ a permitted state path from }S\text{ to }S_{11}.}
\]

What Theorem 34 needs is

\[
\boxed{
\forall x\ \exists t:\ s(C^t(x))=S_{11},}
\]

or, at the quotient-relation level, the even stronger statement that **every realizable infinite successor path** from every state reaches the gateway.

Existential graph reachability is insufficient:

\[
\boxed{
\forall S\ \exists\text{ good path}
\not\Rightarrow
\forall\text{ actual trajectories from }S\ \text{good path is taken}.}
\]

This is the central global hinge failure.

---

## 5. State cycles are not integer cycles

Theorem 34 further states that indefinite looping inside the transient subsystem would require a nontrivial Collatz cycle.

That implication is false for a coarse quotient.

A direct integer example is

\[
34\to17\to52.
\]

Using the paper's state definitions,

\[
34\in S_9,
\qquad
17\in S_{12},
\qquad
52\in S_9.
\]

Thus the quotient path contains the state loop

\[
\boxed{S_9\to S_{12}\to S_9}
\]

while

\[
34\ne52.
\]

Therefore a repeated state need not imply a repeated integer.

A trajectory can traverse a cycle in a finite quotient while drifting among infinitely many representatives of those states.

DSD failure type: **QUOTIENT RECURRENCE PROMOTED TO ORIGINAL-SPACE RECURRENCE**.

---

## 6. Strong connectivity does not imply absorption

A strongly connected transient component containing a state that has an exit edge does not force every path to take the exit.

Even in a genuinely finite nondeterministic directed graph, an infinite path may stay inside a strongly connected component forever by repeatedly choosing internal edges.

To prove inevitable absorption one needs an additional structure such as:

- a strict ranking/Lyapunov function decreasing on every internal transition;
- absence of all realizable infinite internal paths;
- a deterministic quotient with no internal directed cycle;
- sufficient memory so that hidden arithmetic choices are represented in the state.

None follows merely from strong connectivity plus existence of an exit path.

The paper's own transition table contains branching, so the hidden representative matters.

---

## 7. Relation to the internal fixed-memory barrier

The present internal DSD program independently found a stronger limitation on a related mixed `2`-adic/`3`-adic finite-state architecture.

For depth `h`, if reverse compatibility is represented only by

\[
(\sigma_h,R_h\bmod3^{Q(h)}),
\]

there exist infinite witness families that are indistinguishable modulo `3^(h-4)` but have opposite compatibility. Hence exact classification requires at least

\[
\boxed{Q(h)\ge h-3.}
\]

This theorem does **not** formally refute every conceivable finite-state representation of Collatz.  But it gives the correct methodological comparison:

- Nwankpa's fixed mod-9/parity quotient visibly forgets information already at one step;
- the internal audit shows that for one precise mixed deterministic gate, required arithmetic memory actually grows linearly with depth.

Thus the external failure and internal barrier point in the same direction:

\[
\boxed{
\text{a coarse fixed residue state cannot be assumed to preserve long-horizon carry/history.}
}
\]

---

## 8. What survives from the paper

The following parts are not invalidated by this audit:

1. the listed sets can form a useful coarse partition;
2. Lemma 30's case-by-case transition **relation** contains valid modular observations where correctly derived;
3. gateway/residue graphs may be useful diagnostics or routing summaries;
4. computational checks up to a finite bound can validate that observed transitions belong to the relation.

What fails is the promotion

\[
\text{finite coarse relation + reachability}
\Longrightarrow
\text{universal Collatz convergence}.
\]

---

## 9. DSD anti-patterns extracted

### FSM-1 — Pointwise determinism is not quotient determinism

Before calling a partition an FSM, verify

\[
x\sim y\Rightarrow C(x)\sim C(y).
\]

Without this congruence property the quotient transition is multivalued.

### FSM-2 — Existential reachability is not universal liveness

Forbidden upgrade:

\[
\forall S\ \exists\text{ path to sink}
\Rightarrow
\forall\text{ trajectories hit sink}.
\]

### FSM-3 — State loop is not integer cycle

Forbidden upgrade:

\[
s(C^a(x))=s(C^b(x))
\Rightarrow
C^a(x)=C^b(x).
\]

The quotient may identify different integers.

### FSM-4 — Finite computation validates only tested representatives/horizons

Checking many integers confirms compatibility with the transition relation but cannot prove the missing quotient congruence or universal liveness theorem.

---

## 10. Executable regression

`collatz/src/external_nwankpa_fsm_quotient_counterexample.py`

checks the exact examples

\[
20,38\in S_3,
\quad C(20)=10\in S_1,
\quad C(38)=19\in S_2,
\]

and

\[
34\to17\to52,
\qquad
S_9\to S_{12}\to S_9,
\qquad34\ne52.
\]

---

## 11. Final verdict

\[
\boxed{
\text{The 17-state quotient does not define the deterministic finite-state dynamics required by the proof.}
}
\]

The paper provides a finite modular transition relation, but Lemma 33 establishes only existential gateway reachability and Theorem 34 upgrades this to inevitability without controlling the hidden integer representative.  Therefore the claimed complete proof does not follow as written.

For the internal program this is a valuable negative result: every proposed finite-state closure must now pass explicit quotient-well-definedness, memory-sufficiency, and universal-path tests before it can enter the SAFE proof chain.

# DSD escape-ledger audit — Collatz live proof tree

Date: 2026-08-27

Status: **OPEN BRANCH-COMPLETENESS LEDGER / COLLATZ NOT PROVED**

## Purpose

The DSD audit treats every theorem that splits a formation domain as a producer of explicit exits. A later theorem may consume one exit without erasing the others.

The current resonance program contains at least two such split points that must remain visible in the canonical proof DAG.

---

## Split S2 — phase-renewal bridge at `K1`

From the first global resonance endpoint `y`, the audited phase-renewal theorem yields the disjoint alternatives

\[
q_{K_1}(y)=P_1
\]

or

\[
q_{K_1}(y)\ge P_1+1.
\]

### S2-E — exact second lower resonance

Formation domain:

\[
q_{K_1}(y)=P_1.
\]

Status: **SAFE branch theorem**.

This branch yields

\[
z=T^{A_2}(N)=N+h,
\]

with

\[
2^{33}<h<7\cdot2^{33},
\qquad h\in4\mathbb Z_{>0},
\]

and feeds the current local `J0/A0` gap analysis.

### S2-S — surplus-recovery branch

Formation domain:

\[
q_{K_1}(y)\ge P_1+1.
\]

Status: **OPEN as a global exit**.

The existence of the exact-resonance analysis does not eliminate this complementary branch. Until a separate theorem routes or closes it, it remains an explicit escape from the present main line.

Therefore

\[
\boxed{
\text{S2-E closed or reduced further}
\not\Rightarrow
\text{all K1 branches closed}.
}
\]

---

## Split S4 — `A0` local return language

The audited `A0` structure separates at least three logical exits.

### S4-T — finite terminal recovery

Status: **OPEN**, currently routed toward Hensel/Bellman analysis.

Its full formation domain contains every admissible checkpoint surplus

\[
s\ge1.
\]

The separate surplus-coverage audit shows that an `s=1` computation alone does not cover this exit.

### S4-C — infinite consecutive `A0` returns

The bounded affine endpoint argument proves

\[
\text{infinite A0-only endpoint language}
\Longrightarrow
\text{nontrivial positive Collatz cycle}.
\]

Status of the implication: **SAFE**.

Status of the resulting cycle exit: **OPEN globally** unless an independently applicable cycle theorem excludes every such cycle.

Thus the implication classifies the escape; it does not delete it.

### S4-L — leave the present `A0` language

This includes later finite coefficient crossings, coefficient survival through the current scale, and any other Hensel-compatible later-scale language not already represented by the present `J0/A0` macro system.

Status: **OPEN**.

---

## Escape ledger

| Exit | Formation condition | Current status | Consumed by |
|---|---|---|---|
| `E2-exact` | `q_K1=P1` | SAFE reduction | `J0/A0` gap line |
| `E2-surplus` | `q_K1>=P1+1` | OPEN | no complete global consumer yet |
| `E4-terminal` | finite `A0` terminal recovery, all `s>=1` | OPEN | `C6B` target |
| `E4-cycle` | infinite consecutive `A0` returns | SAFE classification, OPEN exclusion | global cycle branch |
| `E4-later` | leave present `A0` language / later survivor | OPEN | later-scale analysis |
| `Q-selector` | ternary selector family | CONDITIONAL | quarantined family only |

---

## DSD branch-completeness rule

A proposed global closure must supply a consumer for every nonempty exit in the ledger.

Formally, if a split theorem gives

\[
\mathcal F
=\mathcal F_1\sqcup\cdots\sqcup\mathcal F_r,
\]

then proving impossibility only on an index subset `I` establishes at most

\[
\mathcal F\setminus\bigcup_{i\in I}\mathcal F_i
\subseteq
\bigcup_{i\notin I}\mathcal F_i.
\]

It does not establish `\mathcal F=\varnothing`.

This rule is now an audit lock for the Collatz project.

---

## Current verdict

The active exact-resonance / `J0/A0` line remains mathematically usable on its stated formation domain, but it is not yet an exhaustive global proof tree.

The two most immediate branch-completeness obligations are

\[
\boxed{E2\text{-surplus}}
\]

and

\[
\boxed{E4\text{-later / cycle exits}}.
\]

Together with the separate all-surplus Hensel coverage gate `C6B`, these must remain OPEN until independently routed.

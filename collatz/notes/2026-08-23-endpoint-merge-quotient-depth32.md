# Endpoint-merge quotient extended through depth 32

Date: 2026-08-23

Status: **exact finite extension of the same-depth endpoint dominance diagnostic. The one-Pareto-state-per-endpoint phenomenon now holds through depth 32, but no asymptotic exponent improvement is claimed. This does not prove Collatz.**

## 1. Verified dominance lemma retained

At one fixed prefix depth, two coefficient-surviving states with the same canonical endpoint satisfy the previously proved dominance rule:

\[
(r_1,q_1,y),\ (r_2,q_2,y),
\qquad
r_1\le r_2,\ q_1\ge q_2
\]

implies that state 1 dominates state 2 for every common future continuation in the minimal-survivor dynamic program.

The open structural question was whether each endpoint group continues to have only one Pareto state beyond the previously tested depth 28.

## 2. Exact extension

The optimized exact verifier gives

\[
\boxed{
\begin{array}{c|r|r|r|r|r}
k&\text{survivors}&\text{endpoints}&\text{collision groups}&\text{Pareto kept}&\max|G|\\\hline
28&3,524,586&3,312,992&210,107&3,312,992&4\\
29&6,385,637&6,003,575&379,327&6,003,575&4\\
30&12,771,274&12,006,840&758,572&12,006,840&4\\
31&23,642,078&22,229,766&1,401,286&22,229,766&4\\
32&41,347,483&38,890,504&2,437,971&38,890,504&4
\end{array}
}
\]

At every one of these depths,

\[
\boxed{\text{Pareto kept}=\text{distinct endpoints}.}
\]

Thus every endpoint collision group has exactly one Pareto survivor through depth 32.

Certificate:

`collatz/src/endpoint_merge_quotient_depth32_certificate.cpp`.

## 3. Reduction size

At depth 32 the quotient removes

\[
41,347,483-38,890,504=2,456,979
\]

coefficient-surviving states, about

\[
\boxed{5.94\%}
\]

of the raw survivor set.

The removal fraction remains close to the depth-28 value of about 6%. Therefore the current finite data do **not** indicate a new exponential exclusion rate; they indicate a stable finite quotient.

## 4. Structural candidate

The finite evidence supports the candidate statement:

> **One-Pareto endpoint theorem.** At every depth, among coefficient-surviving canonical preimages of a fixed endpoint, ordering by increasing start residue produces a nonincreasing odd-count profile, so the smallest start residue dominates every other member of the endpoint group.

This theorem is not proved here.

A proof would nevertheless be useful even if the quotient ratio stays asymptotically constant, because it removes endpoint multiplicity as an independent state coordinate and can simplify the remaining cross-base transfer.

## 5. Relation to the residue-maximality audit

The endpoint quotient does not depend on repeated local residue-maximality. It therefore remains an unconditional branch after the local-pullback dependency correction.

The present valid Stage-4 objects are now separated cleanly:

1. coefficient-survivor/formation entropy;
2. exact first-window m=45 selector transversality;
3. finite renewal/Hensel normalization results not using repeated local maximality;
4. same-endpoint Pareto quotient, verified through depth 32;
5. the still-open cross-base/global-pullback theorem.

The conditional L7/L14 low-height automata remain useful diagnostics, but they are not counted as unconditional proof closure until the global Hensel-compatible predecessor pullback is established.

# S10 audit — pure-ballot macroblock non-contraction

Date: 2026-09-03

Status: **SAFE negative/compression result / principal S10 gate remains OPEN**

## Object under audit

The current eight-jump A0, s=1, Route-B frontier admits an exact finite-horizon pure-ballot control quotient and an exact valuation-macroblock compiler.

The question is whether compiling four future valuation jumps into one macroblock contracts the mathematical source-family state space, or merely reduces transition overhead.

## D — Domain

The result applies to the already-certified A0, s=1, Route-B pure-ballot source-family frontier.

The active exact source state remains

\[
(r,y,m_{lo},m_{hi},h,S).
\]

No claim is made for Route-A, s>=2, other formation sectors, or global Collatz.

## R — Resolution

The theorem compares two representations of the same finite depth-d legal valuation language:

- sequential valuation jumps;
- direct macroblocks \(0^{a_1}1\cdots0^{a_d}1\).

The comparison is exact at the parity-prefix/source-cylinder resolution.  The current numerical counts are finite control-frontier calculations at horizon four.

## S — State sufficiency

`(h,S)` is sufficient only for the pure-ballot control skeleton.

It is not sufficient for source identity.  Therefore the 13 horizon-four control signatures may share transition programs, but source payload coordinates `(r,y,m_lo,m_hi)` must remain attached to each source family.

## E — Equivalence

The legal equivalence is

\[
\text{sequential tuple }(a_1,\ldots,a_d)
\equiv
\text{one macroblock }0^{a_1}1\cdots0^{a_d}1
\]

for the same parent source channel.

It is not legal to infer

\[
(h_1,S_1)\sim(h_2,S_2)
\Rightarrow
\text{source-family merge}.
\]

Equal control signature means equal reusable control skeleton only.

## T — Transition

The depth-d leaf blocks are prefix-free because each terminates at its d-th one.

The exact multibit source transition gives the same child as sequential valuation refinement for each leaf.

Thus direct compilation bypasses internal nodes but preserves the terminal parity/source partition selected by the same predicate.

## C — Closure

CLOSED:

1. pure-ballot depth-d macroblock is an exact representation of sequential legal valuation tuples;
2. depth-d leaf language is prefix-free;
3. direct macroblock evaluation cannot by itself produce additional mathematical pruning relative to the same pure-ballot predicate;
4. on the current horizon-four control frontier, intermediate transition construction can be reduced.

OPEN:

1. a stronger admissible block language that rejects additional source residue classes;
2. a proved source-to-formation-run parameter map/quotient;
3. deterministic Route-B formation-rank renewal/globalization;
4. S11 checkpoint/debit/tail realization;
5. A0 s=1 Route-B closure.

## N — Non-independence

The 13 control signatures are not 13 source equivalence classes.

Macroblock compilation and sequential valuation pruning are not independent filters; they are two implementations of the same pure-ballot language.  Their survival factors must not be multiplied.

Likewise, the 35.6% reduction reported below is an execution-attempt reduction, not a 35.6% mathematical pruning of source candidates.

## O — Outstanding

The next principal question is no longer whether pure-ballot macroblocks can reduce source cardinality.  That route is closed negatively.

The next high-value interface is:

\[
\boxed{
\text{exact source family}
\longrightarrow
\text{formation rank/run parameter family}
}
\]

because the bounded-drop/run and formation-cylinder theorems already compress a fixed formation path strongly, but their deterministic renewal from the active source family remains OPEN.

## Current finite calculation

From the certified 14,224-path / 90-control eight-jump frontier, four further pure-ballot control levels contain

\[
34{,}318,\quad93{,}000,\quad209{,}784,\quad609{,}808
\]

control-path leaf attempts.

Sequential evaluation therefore constructs

\[
946{,}910
\]

child attempts across the four levels, whereas a direct four-jump macroblock compiler emits only the

\[
609{,}808
\]

terminal leaf attempts.

The skipped intermediate attempts are

\[
337{,}102,
\]

or approximately

\[
35.6002154376\%.
\]

This is implementation compression only.

## Forbidden inferences

- 13 control signatures -> 13 source families;
- macroblock speedup -> membership pruning;
- equal macroblock control -> equal source cylinder;
- block-to-residue bijection -> universal Route-B admissibility;
- fixed formation-path macrostate -> deterministic formation-path selection;
- finite horizon-four counts -> horizon-independent quotient theorem;
- this negative result -> Route-B impossibility;
- A0 s=1 Route-B progress -> global Collatz proof.

## Verdict

**SAFE.**

The finite-horizon macroblock route is retained as an execution optimization and reusable control compiler, but it is removed as a candidate standalone S10 source-cardinality contraction mechanism.

# S10 audit — source-to-formation entry state

Status: **local entry CLOSED / persistent formation label REJECTED / global rank bridge OPEN**

## Audited question

At the current A0 `s=1` Route-B frontier, the persistent exact source state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S)}.
\]

The audit asks whether this state must be enlarged before exact maximal-macroblock formation information can be used.

The answer is **no for local entry partitioning**, but **yes if one tries to replace the source cylinder by one formation label or one global formation-rank path**.

---

## D — Domain

The theorem applies to positive endpoint families

\[
Y(m)=y+3^{Q(h)+S}m
\]

on a finite integer parameter interval.

The local formation object is the exact maximal accelerated continuation

\[
0^b1^H0^D,
\]

where

\[
b=v_2(Y),
\quad
H=v_2(Y/2^b+1),
\quad
D=v_2\!\left(3^H\frac{Y/2^b+1}{2^H}-1\right).
\]

This domain must not be conflated with the separate suffix-slack / formation-subtraction automaton.

**Status: EXACT.**

---

## R — Resolution

For a prescribed local descriptor \((b,H,D)\), let

\[
K=b+H+D+1.
\]

The exact parameter preimage is one class modulo \(2^K\):

\[
m\equiv\rho_{b,H,D}\pmod{2^K}.
\]

Therefore the required resolution is explicit and finite for every fixed local type.

The `+1` is essential: it certifies exact maximality of the terminal zero run by fixing the following odd parity.

**Status: EXACT / CLOSED.**

---

## S — State sufficiency

From the persistent state,

\[
q=Q(h)+S,
\qquad
A=3^q
\]

are derived.

Then

\[
\rho_{b,H,D}
\equiv
(2^b x_{H,D}-y)A^{-1}
\pmod{2^{b+H+D+1}}
\]

is computable with no additional historical coordinate.

Hence

\[
\boxed{
(r,y,m_{lo},m_{hi},h,S)
}
\]

is sufficient to construct the exact local formation-entry partition.

However it does not imply that the whole live interval has one common \((b,H,D)\).  Whenever two consecutive parameters survive, the odd coefficient \(A\) makes their endpoints opposite in parity, hence their `b` values differ.

Therefore a persistent single formation label is not a sufficient replacement for the source payload.

**Status: source state SUFFICIENT; single-label replacement REJECTED.**

---

## E — Equivalence

For a fixed descriptor \((b,H,D)\), membership in its parameter residue class is equivalent to realizing that exact local maximal block.

Thus the local residue partition is exact.

But equality of local descriptors for two different subcylinders does **not** imply equality of their source residues, endpoint offsets, future checkpoint observations, physical scores, or any other unresolved source-sensitive predicate.

No right-congruence merge theorem is supplied.

**Status: local equivalence CLOSED; source merge OPEN.**

---

## T — Transition

The local descriptor is a compiled future parity grammar

\[
0^b1^H0^D
\]

with one terminal look-ahead bit used for exact maximality.

It can therefore be consumed through the certified multibit source transducer after the corresponding residue subcylinder is selected.

This is a transition interface, not a new dynamical law.

**Status: CLOSED as transient grammar interface.**

---

## C — Closure

The following question is now closed:

> Must S10 carry an additional formation-rank/H/L coordinate merely to recover the next exact maximal macroblock?

No.

The existing minimized source state already determines the exact type partition.

The following stronger question remains open:

> Can the resulting partition be contracted, rejected, or mapped into the bounded-rank formation automaton in a source-safe way?

No theorem presently closes that step.

**Status: local entry CLOSED; proof-level contraction OPEN.**

---

## N — Non-independence

The local formation-entry residue is determined by dyadic future parity information already accessible to the valuation/multibit transducers.

Therefore it must not be counted as an independent pruning factor on top of the same parity refinement.

Likewise, the established local slack/formation recurrence conjugacy does not turn these maximal blocks into one global formation-subtraction rank path.  The direct stitching condition and obstruction remain separate and binding.

**Status: NON-INDEPENDENT / direct-globalization shortcut REJECTED.**

---

## O — Outstanding

The useful next theorem must add information not already present in the parity partition.  Candidate forms are:

1. a source-sensitive inequality that rejects an entire formation-entry residue subcylinder;
2. a right-congruence allowing exact safe merging of different source payloads;
3. an explicit carry/rank bridge into the bounded-rank formation automaton, including all boundary transitions;
4. a future unavoidable defect floor that can be composed with the exact physical `P` predicate.

Merely enumerating deeper \((b,H,D)\) labels is not a proof-level contraction strategy.

---

## Audit matrix

| Dimension | Result |
|---|---|
| D — domain | EXACT |
| R — resolution | EXACT / CLOSED |
| S — state sufficiency | CLOSED for local partition; single-label replacement REJECTED |
| E — equivalence | CLOSED locally; source merge OPEN |
| T — transition | CLOSED as transient grammar |
| C — closure | local entry CLOSED; contraction OPEN |
| N — non-independence | formation entry is not independent of parity refinement |
| O — outstanding | source-sensitive rejection/quotient or explicit global bridge |

## Canonical dependencies

- `../theorems/SOURCE_TO_MACROBLOCK_FORMATION_ENTRY_PARTITION.md`
- `../src/A0_s1_source_to_macroblock_formation_entry_partition_certificate.py`
- `../theorems/SLACK_FORMATION_LOCAL_CONJUGACY_STITCHING_OBSTRUCTION.md`
- `../theorems/SOURCE_PAYLOAD_CONTROL_FACTORIZATION.md`
- `../theorems/VALUATION_MACROBLOCK_COMPILATION.md`

## Final audit verdict

\[
\boxed{
\text{state insufficiency was not the formation-entry obstruction.}
}
\]

The exact obstruction is instead

\[
\boxed{
\text{one live source cylinder generally partitions into multiple formation types,}
}
\]

and no certified theorem yet converts that partition into source-sensitive contraction or into one global bounded-rank formation path.

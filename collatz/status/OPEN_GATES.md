# Open gates

This register contains unresolved obligations only. Closed lemmas belong in the proof map / theorem index rather than being mixed into this list.

## G1 — 14-root forward family execution

**Module:** C4

Run the exact forward family state on all 14 source roots with the smallest currently sufficient active state

`source/control × interval payload × P_min`

and quantify where whole-family physical closure occurs before singleton expansion.

Required output:

- exact node state definition;
- exact merge/dominance rule;
- reproducible root-level certificate;
- closed/unresolved counts without probability language.

Terminal ternary state is not carried while it is dormant.

Status: **ACTIVE**.

## G2 — Backward right-H projective residue filter

**Module:** C4/C5

The minimal forward ternary observation problem for a final `N_J mod 3^L` predicate is now closed:

\[
m(q)=\max(0,L-(J-q)).
\]

Critical-cut shielding also proves that the current 24-, 28-, and 47-trit terminal correction/defect residue predicates are entirely right-local at the existing critical cut.

The remaining gate is therefore to construct the compressed backward filter inside the right H/projective factor.

Required output:

- actual required right-block terminal residue(s);
- exact backward branch/cylinder transition;
- compressed state representation without flat carry-residue enumeration;
- state counts by terminal precision;
- exact cut-boundary export state.

Known structural help:

- each fixed one-event predecessor residue is empty or singleton;
- projective exponent cylinders have period `2*3^(m-1)`;
- for `m>=23`, every specified exponent cylinder is empty or singleton inside the entire legal dominance interval;
- the rejected local-carry greedy rule remains forbidden.

Status: **ACTIVE — principal new structural gate**.

## G3 — Exact forward/backward cut join

**Module:** C4/C5

Join the forward 14-root source/physical Bellman families to the backward right-H projective filter at an exact block boundary.

The join must preserve every boundary/control coordinate queried by either side.

Do not multiply marginal counts or assume left/right independence.

Status: **OPEN after G1/G2 export states are explicit**.

## G4 — Full pre-bridge correction-language membership

**Module:** C5

For every remaining joined family, prove membership or nonmembership in the exact long pre-bridge formation/correction language.

Boundary exposure alone is insufficient.

Status: **OPEN — principal local membership gate after the two-front join**.

## G5 — Checkpoint and debit coherence

**Module:** C5

Join coherent checkpoint residues to an ordinary checkpoint and compatible debit without circularly using X and L_- to define one another.

Existing exposure theorems may be used only through the synchronized interface already audited in the chronological notes.

The new lazy-residue and shielding theorems may be applied only after the relevant checkpoint/debit condition is explicitly reduced to a correction/defect residue congruence.

Status: **OPEN after structural exposure lemmas**.

## G6 — Tail first-passage / post-checkpoint compatibility

**Module:** C5

Close the exact tail language and physical first-passage obligations for every pre-bridge survivor.

Status: **OPEN**.

## G7 — C4F / renewal / global formation compatibility

**Module:** C5

Provide an explicit invariant/state theorem if these predicates are needed. Do not assume a local pure-ballot/projective quotient preserves a complete C4F Boolean state.

Status: **OPEN**.

## G8 — Route-A completion

**Module:** C6

Complete the independent Route-A lower-bound/closure obligation.

Status: **OPEN**.

## G9 — All-surplus `s>=2`

**Module:** C6

Generalize or separately close the surplus sectors not covered by the current `s=1` factorization.

Status: **OPEN**.

## G10 — Global branch completeness

**Module:** C0/C6

Prove that all counterexample classes are covered by the final branch partition and that closure of every module implies the ordinary Collatz conjecture.

Status: **OPEN**.

---

# Priority order

Current priority is

`G1 || G2 -> G3 -> G4/G5/G6/G7 -> G8/G9 -> G10`.

`G1` and `G2` may proceed independently until their exact boundary/export states are ready for `G3`.

The order may change only when a new exact theorem makes an earlier gate redundant. Such a change should be recorded in `DEPENDENCY_LEDGER.md`.

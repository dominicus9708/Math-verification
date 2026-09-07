# External literature audit-before-calculation protocol

Date: 2026-09-07

Status: **ACTIVE OPERATING RULE FOR FUTURE COLLATZ WORK.**

This protocol records the standing rule for external literature discovered during future Collatz calculations.

The purpose is to prevent two opposite failures:

1. importing an external theorem more strongly than its hypotheses allow;
2. discarding an entire paper because one global hinge fails even when useful local results survive.

---

## 1. Trigger

Whenever an external paper, preprint, computational project, theorem, conjecture, or claimed proof becomes materially relevant to the next Collatz calculation, it must be audited **before** it is used as a proof input.

A source is materially relevant when it may:

- provide a lemma, bound, reduction, verification floor, state representation, congruence fact, density theorem, Fourier/spectral estimate, 2-adic/3-adic structure, cycle result, or computational certificate used by the current calculation;
- contradict or weaken a current internal lemma;
- suggest a shortcut that would replace an existing open gate;
- provide a known failure mode that matches a proposed internal transition.

External browsing/search may occur during calculation when necessary, but theorem-level use is suspended until the audit classification is recorded.

---

## 2. Mandatory audit sequence

For every newly relevant source, perform the following sequence.

```text
DISCOVER SOURCE
-> LOCK SOURCE VERSION
-> IDENTIFY EXACT CLAIM UNIT
-> REPRODUCE OR CHECK THE NECESSARY HINGE
-> ASSIGN A / B / C / D / FINITE_ONLY
-> RECORD POSITIVE USE
-> RECORD FAILED OR OPEN HINGE
-> RECORD PROHIBITED UPGRADE
-> MAP TO CURRENT INTERNAL GATE
-> COMMIT AUDIT RECORD
-> ONLY THEN USE IT IN THE NEXT CALCULATION
```

The source is never classified only from its title, abstract, reputation, publication status, or claimed conclusion.

---

## 3. Classification

### A — POSITIVE PRIOR ART

The exact theorem/result required by the calculation survives the audit with its hypotheses intact.

Use: cite normally and import only the stated scope.

### B — CONDITIONAL / OPEN PRIOR ART

A useful implication, architecture, or conjecture is valid only under an unproved hypothesis.

Use: keep the hypothesis visible in every downstream dependency.

### C — SPLIT / PARTIAL ABSORPTION

Some definitions, identities, local lemmas, or finite results survive, while a separate global hinge is missing or fails.

Use: cite the surviving result positively and cite the failed/open hinge separately as a boundary condition or anti-pattern.

### D — REJECTED PROOF MECHANISM / NEGATIVE CONTROL

The global closure mechanism needed from the source fails under an explicit counterexample, state defect, quantifier error, invalid globalization, or missing bridge.

Use: do not import the failed implication. Retain the source as a methodological negative control when it illuminates how the present proof avoids the same error.

### FINITE_ONLY

The source provides bounded computation or finite-range evidence only.

Use: finite certificate only. Never promote it to an infinite theorem without a separate bridge.

---

## 4. Citation rule

A paper is not assigned one blanket moral verdict when its claims have different statuses.

The correct citation pattern is claim-level:

\[
\boxed{
\text{surviving theorem}
+\text{conditional theorem}
+\text{failed hinge as anti-pattern}
}
\]

For a failed proof mechanism, use the structure

```text
external claim
-> exact failed hinge
-> DSD diagnosis / prohibited transition
-> additional information preserved by the current proof
```

Avoid rhetorical language such as `the entire paper is false` unless every material claim has actually been audited and refuted.

---

## 5. Mandatory DSD safeguards before import

Every newly relevant source must be checked against at least the applicable safeguards below.

```text
finite computation != universal theorem
almost all != all
measure zero != empty set
same coarse state != same integer future
existential good path != inevitable actual path
average / spectral contraction != pathwise deterministic contraction
symbolic or 2-adic survivor != positive ordinary integer
cycle exclusion != divergence exclusion
root minimality != arbitrary later-block minimality
auxiliary decomposition != literal universal coverage
residue representative != actual-integer quantity unless invariant/bounded
forall L exists witness_L != exists one witness for all L
```

If a proposed external result would cross one of these boundaries, the missing bridge becomes an explicit audit target.

---

## 6. Integration with calculation

After the audit is committed, the next calculation must state which external result is being used and at what status.

Examples:

```text
SAFE EXTERNAL INPUT: theorem X under hypotheses H.
CONDITIONAL EXTERNAL INPUT: implication H -> C; H remains OPEN.
FINITE ONLY INPUT: verified through bound B; no claim above B.
ANTI-PATTERN CHECK: proposed transition does not repeat AP-n failure.
```

If an external source invalidates or weakens an internal dependency, the internal status must be downgraded before further calculation.

If an external source supplies a stronger valid theorem, downstream calculations may be updated only after the hypothesis/interface compatibility is checked.

---

## 7. Recording requirements

Every new literature audit should record:

```text
SOURCE_VERSION
BIBLIOGRAPHIC_ID / DOI / URL
CLAIM_UNIT
AUDIT_CLASS: A / B / C / D / FINITE_ONLY
POSITIVE_CITATION_USE
FAILED_OR_OPEN_HINGE
PROHIBITED_UPGRADE
INTERNAL_GATE_MAPPING
REPRODUCIBILITY_STATUS
MATCHING_COMMIT
DATE_AUDITED
```

The result must be written to the Collatz GitHub audit/notes structure and mirrored into the Notion Collatz external-literature audit ledger.

Material new proof bridges should additionally receive a formal DSD Audit record or revision in `DSD_Method_Family/DSD_Audit/audits/mathematics/`.

---

## 8. Search policy during future work

External literature search is **need-driven, not mandatory at every arithmetic step**.

Search again when:

- the next proof gate requires a theorem not already in the ledger;
- a current result resembles a known field where stronger literature may exist;
- a newly proposed bridge is vulnerable to one of the recorded anti-patterns;
- a cited preprint has a newer version whose theorem statement may have changed;
- a new claimed proof/result materially overlaps the current bottleneck.

If no new external input is needed, continue the internal exact calculation without interrupting it merely to expand the bibliography.

---

## 9. Standing workflow

The future default workflow is therefore

\[
\boxed{
\text{calculate}
\to
\text{detect literature need}
\to
\text{search}
\to
\text{DSD analyze + audit}
\to
\text{classify/cite}
\to
\text{record in GitHub + Notion}
\to
\text{resume calculation}.
}
\]

This protocol is subordinate to the current authoritative literature ledger:

`collatz/notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md`

and extends its `Current repository rule` into the operational order for all future calculations.

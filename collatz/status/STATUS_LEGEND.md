# Status legend

Every Collatz document/certificate should use these labels with the meanings below.

## EXACT / CLOSED

A mathematical implication has been proved within its explicitly stated domain.

Requirements:

- hypotheses and domain are stated;
- the conclusion follows algebraically/logically from those hypotheses;
- finite regression may support implementation but is not the proof.

`CLOSED` is local unless a global module explicitly says otherwise.

## CERTIFIED ARITHMETIC

A finite numerical/combinatorial claim is established by an exact reproducible certificate.

Examples:

- exact finite counts;
- exhaustive finite-radius closure;
- exact rational/fixed-point interval arithmetic;
- independent implementation cross-checks.

This label does not automatically generalize beyond the certified finite domain.

## SAFE NECESSARY PRUNING

A condition is necessary for every survivor in the stated upstream domain.

It may remove candidates safely, but a candidate that survives the condition is not thereby proved to satisfy full membership.

## REGRESSION ONLY

A small-horizon or finite test guards implementation/index conventions.

It must never be cited as the proof of the general theorem unless the theorem itself is finite and exactly exhausted by that regression.

## DIAGNOSTIC

A numerical scale estimate, complexity indication, strategy comparison, or exploratory statistic used to decide what to try next.

Diagnostic values are not proof obligations and cannot close a branch.

## REJECTED

A proof implication, abstraction, or search strategy has been shown invalid, over-strong, circular, or practically unsuitable.

Rejected material is retained for audit so the same error is not reintroduced.

Distinguish:

- **REJECTED AS MATHEMATICS** — the implication itself is false/unsupported;
- **REJECTED AS SEARCH ENGINE** — the mathematics may be valid but the implementation strategy is unsuitable for the long problem.

## SUPERSEDED

A statement/file is historically valid but a stronger or cleaner canonical object has replaced it.

Do not delete it solely for being superseded; keep it linked from the archive/migration index until references are audited.

## OPEN

A necessary mathematical or computational obligation has not been closed.

An OPEN gate remains open even if many adjacent lemmas are closed.

## ACTIVE

An OPEN gate is the current computation/proof frontier.

There should be as few ACTIVE objects as possible; all other open obligations belong in `OPEN_GATES.md` rather than the current frontier.

---

# Promotion rules

Allowed promotions require explicit evidence:

- `REGRESSION ONLY` + algebraic proof → `EXACT`;
- exact finite exhaustive computation → `CERTIFIED ARITHMETIC`;
- exact theorem + certified upstream bounds → `SAFE NECESSARY PRUNING`;
- a SAFE pruning bound does **not** promote survivors to membership;
- local `CLOSED` does **not** imply module/global `CLOSED`.

Whenever a status changes, record the dependency that justified the change in `DEPENDENCY_LEDGER.md` or the relevant audit note.

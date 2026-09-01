# Dependency ledger

This file records dependency order that must not be silently reversed.

## D1 — Radius-seven closure before refined X bound

Required order:

`old X bound`
→ `finite radius 0..7 closure`
→ `d75 >= 8`
→ `first-75 defect floor`
→ `Christoffel real-envelope conversion`
→ `refined X upper bound`.

Rule: the refined X bound is not used retroactively to justify the finite radius-seven closure unless a separate certificate reruns that closure under the new hypothesis.

## D2 — Refined X bound before shell-conditioned pruning

The first-defect shell cardinalities / shell-specific physical restrictions depend on the upstream refined physical interval.

Rule: any later stronger shell bound must declare whether it is independent of, or downstream from, the existing refined X bound.

## D3 — 14-root forest after late-shell elimination

The 14-root forest is the retained family only after the late first-defect shells have been eliminated by certified pruning.

Rule: do not present the 14 roots as the complete unconditioned set of all threshold deviations.

## D4 — H/L grammar before target Christoffel specialization

Universal dual H/L grammar is defined/proved for the ballot languages first.

Only then may the already certified target word be aligned with its Stern-Brocot/continued-fraction hierarchy.

Rule: arbitrary H/L candidates are not promoted to Christoffel words.

## D5 — Target-collision state before membership use

Adic/projective target-collision coordinates may localize candidate positions or force displacement cylinders.

Only the resulting ordinary correction defect / explicit membership predicate may be used for physical rejection.

Required interface:

`projective observation`
→ `formation/order restriction`
→ `ordinary displacement/defect`
→ `normalized eta floor`
→ `physical X pruning`.

Rejected shortcut:

`adic mismatch -> membership rejection`.

## D6 — Local defect floors before global accumulation

A local `1/12`, `1/8`, or exact cylinder floor is not automatically additive with another floor unless their supports/ranks or semiring block composition are certified to avoid double counting.

Rule: use ranked atoms, fixed-cylinder ordering minimum, or the normalized-defect semiring.

## D7 — Fixed-cylinder greedy after cylinder sequence is fixed

The right-to-left maximal-position greedy is exact for an already fixed sequence of admissible position cylinders.

Rule: it is not used to choose the ternary carry/cylinder sequence itself.  A counterexample to local carry-greedy selection is retained in the audit record.

## D8 — Physical-risk merge inside an exact future-control class

Min-plus/Bellman merging of histories is legal only when the merged histories share the exact future transition/predicate class required by the active state theorem.

Rule: a smaller defect/risk label does not permit merging source controls that can emit different future parity/predicate behavior.

## D9 — Checkpoint residue exposure before ordinary checkpoint reconstruction

Checkpoint dyadic and ternary residues must be coherent residues of the same checkpoint.

Only after the CRT/corridor singleton condition is satisfied may an ordinary checkpoint be reconstructed.

Rule: do not multiply marginal residue densities and do not infer checkpoint membership from one boundary channel alone.

## D10 — Debit reconstruction without circularity

`L_- = 3X - Z` couples X, Z, and debit.

Rule: terminal correction data plus the required X residue determine the debit residue; terminal debit trits are not treated as an X-independent ordinary debit oracle.

## D11 — Local Route-B closure before global claims

Even complete closure of all 14 A0 `s=1` Route-B roots would close only that module.

Required later dependencies:

`Route-B local closure`
→ `Route-A + s>=2 + remaining branches`
→ `global branch completeness`
→ `Collatz conclusion`.

## Change-control rule

Whenever a new theorem shortens the dependency chain:

1. state exactly which previous dependency becomes redundant;
2. keep the old record as historical evidence;
3. update `PROOF_MAP.md`, `CANONICAL_PROOF_STACK.md`, and `OPEN_GATES.md` in the same maintenance cycle;
4. do not silently reinterpret old finite results under the new assumptions.

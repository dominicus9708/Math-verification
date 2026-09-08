# MATH-041 — targeted reverse-Hensel nested survivor engine

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / EXACT TARGETED HENSEL ORACLE / NESTED ONE-SIDED PRUNING THROUGH DEPTH 31 / COMPUTATIONAL ACCELERATION`

## 1. Why the calculation direction changed

MATH-040 corrected the root-Hensel selection rule to

\[
\text{candidate}\in\mathcal L_{\rm coeff},
\qquad
\text{competitor}\in\mathcal L_{\rm arbitrary}.
\]

A direct unrestricted class-max table grows rapidly.  The global class-max DP already contains

\[
154{,}390{,}110
\]

classes at depth 30.

The actual candidate side is much smaller, so MATH-041 computes an unrestricted maximum **only for the classes that are actually queried by surviving candidates**.

## 2. Reverse-Hensel class reconstruction

For odd positions

\[
p_1<\cdots<p_q<k,
\]

the correction satisfies

\[
C=3C_{q-1}+2^{p_q}.
\]

Given a queried Hensel residue

\[
r=C\bmod3^q,
\]

a possible last odd position must satisfy

\[
2^{p_q}\equiv r\pmod3.
\]

For each such `p_q`, the previous residue is uniquely

\[
\boxed{
r_{q-1}\equiv\frac{r-2^{p_q}}3\pmod{3^{q-1}}.
}
\]

Recursing with the new upper-position bound `p_{q-1}<p_q` enumerates every arbitrary parity word in the queried class exactly once.  Taking the largest reconstructed correction gives the exact unrestricted class maximum.

Thus no unrelated Hensel class has to be materialized.

## 3. Downstream dominance makes the filter nested

MATH-013 proved that if two prefixes are in the same Hensel class with

\[
h_1<h_2,
\]

then after either common next parity bit the inequality remains strict in the child class.

Therefore

\[
\boxed{
\text{a non-maximal prefix can never recover under a common suffix}.
}
\]

This means a prefix may be deleted immediately.  Its descendants never need to be generated.

Equivalently, at depth `k`, being unrestricted-class-max is consistent with all earlier all-prefix Hensel-max requirements.

## 4. Exact nested counts

The targeted engine was extended through depth 31.

Selected rows:

| depth | full coefficient language | candidates generated from previous Hensel survivors | final Hensel survivors | newly pruned at this depth |
|---:|---:|---:|---:|---:|
| 6 | 8 | 8 | 7 | 1 |
| 10 | 64 | 53 | 52 | 1 |
| 16 | 2,114 | 1,721 | 1,720 | 1 |
| 20 | 27,328 | 22,272 | 22,244 | 28 |
| 24 | 286,581 | 234,332 | 234,156 | 176 |
| 26 | 1,037,374 | 848,189 | 847,493 | 696 |
| 27 | 1,762,293 | 1,443,156 | 1,442,349 | 807 |
| 28 | 3,524,586 | 2,884,698 | 2,882,872 | 1,826 |
| 29 | 6,385,637 | 5,230,056 | 5,226,985 | 3,071 |
| 30 | 12,771,274 | 10,453,970 | 10,446,423 | 7,547 |
| 31 | **23,642,078** | **19,359,254** | **19,347,686** | **11,568** |

At depth 31 the cumulative number of coefficient-surviving residue classes removed by root-Hensel maximality is therefore

\[
\boxed{
23{,}642{,}078-19{,}347{,}686
=4{,}294{,}392.
}
\]

## 5. Exact first-cell ordinary-start count at depth 31

Every surviving depth-31 prefix has nonzero residue modulo `2^31`, since coefficient survival requires many odd steps.

In the current 340-block first-cell window, each nonzero residue modulo `2^31` occurs exactly

\[
340\cdot2^{30}=365{,}072{,}220{,}160
\]

times.

Therefore coefficient survival alone through depth 31 leaves

\[
23{,}642{,}078\cdot340\cdot2^{30}
=8{,}631{,}065{,}904{,}655{,}892{,}480
\]

ordinary starts, while coefficient survival plus all-prefix one-sided Hensel maximality leaves

\[
\boxed{
19{,}347{,}686\cdot340\cdot2^{30}
=7{,}063{,}302{,}682{,}978{,}549{,}760.
}
\]

Thus within this finite depth-31 prefix audit, Hensel maximality removes an additional

\[
\boxed{
1{,}567{,}763{,}221{,}677{,}342{,}720
}
\]

ordinary starts beyond coefficient survival alone.

These are exact finite counts of residue classes in the current window, not probabilities or a global Collatz density statement.

## 6. Computational consequence

At depth 30 a full unrestricted class-max table has `154,390,110` classes.  The targeted nested engine queries only `10,453,970` candidate classes before filtering at that depth.

The reverse oracle therefore changes the computational problem from

\[
\text{construct every arbitrary Hensel class}
\]

to

\[
\boxed{
\text{reconstruct only the arbitrary members of candidate-requested classes}.
}
\]

In the session implementation this also reduced memory dramatically.  Wall-clock and RSS values are environment-dependent diagnostics only; the theorem-facing claim is the exact class-query reduction and equality of the resulting survivor counts.

## 7. Current frontier

Depth 31 succeeds with the targeted engine.  A monolithic depth-32 run exceeds the current single-run execution budget because the number of candidate class queries and reverse-search nodes grows rapidly.

The next exact step is therefore to partition depth-32 candidate queries by `q` and/or Hensel residue bucket.  Such partitioning changes only evaluation order and can be independently merged by exact counts.

## 8. DSD interpretation

- `D`: candidate prefixes and arbitrary competitor class are separate objects.
- `R`: exact `(k,q,C mod3^q)` resolution.
- `S`: only current coefficient+Hensel survivors generate descendants; arbitrary competitors are reconstructed on demand.
- `E`: non-maximal prefixes are deleted immediately.
- `T`: MATH-013 downstream dominance proves deleted states cannot recover.
- `C`: targeted oracle reproduces all MATH-040 counts through 26 and extends nested counts through 31.
- `N`: `ESTABLISHED_WITHIN_SCOPE / FINITE EXACT`.
- `O`: unrestricted global class-table construction is no longer the preferred Hensel computation.

## 9. Prohibited upgrades

- depth-31 survivor count ⇒ first-cell candidate count at the terminal crossing — **PROHIBITED**;
- finite nested pruning ⇒ asymptotic density — **PROHIBITED**;
- targeted oracle through 31 ⇒ root-Hensel maximality through 195 — **PROHIBITED**;
- environment benchmark ⇒ theorem strength — **PROHIBITED**.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_targeted_reverse_hensel_nested_survivor_certificate.cpp`

Certificate commit:

`4c3a914c00efdb394866c9242a0d32f7272e5f08`

Controlling selection correction:

MATH-040, `collatz/notes/2026-09-08-one-sided-root-hensel-selection-correction.md`.

The first universal cell and Collatz conjecture remain `OPEN`.

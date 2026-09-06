# Collatz external literature vs current DSD proof program — comparative audit

Date: 2026-09-06

Status: **COMPARATIVE FRONTIER AUDIT / GLOBAL COLLATZ CONJECTURE REMAINS OPEN.**

This note separates three classes of external work:

1. established rigorous partial results used as a baseline;
2. results directly overlapping the present recursive-sufficiency / 2-adic / 3-adic program;
3. recent manuscripts claiming or approaching a complete resolution.

The comparison is about theorem strength, scope, exception handling, and reproducibility. It is not a priority claim for any internal lemma unless prior-art has been separately exhausted.

---

## 1. Established rigorous baselines

### 1.1 Tao — almost-all first-passage control

Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12.

Tao proves that for every function `f(N)->infinity`,

\[
\operatorname{Col}_{\min}(N)<f(N)
\]

for almost all positive integers in logarithmic density. The proof uses Syracuse first-passage variables, `3`-adic cyclic groups, high-frequency Fourier decay, a skew random walk, and a renewal-process geometry.

DSD comparison:

- **EXTERNAL AHEAD in theorem breadth / density strength.** The present project does not match Tao's almost-all theorem.
- **INTERNAL DIFFERENT TARGET:** the current program focuses on the exceptional / hypothetical minimal-counterexample branch where logarithmic-density conclusions do not imply emptiness.
- Tao's method itself does not upgrade an almost-all statement to every integer; his paper explicitly notes that even an absolute bounded minimum for almost all orbits appears close to full Collatz difficulty.

Thus it is invalid to describe the present project as globally ahead of Tao. The potentially new contribution is the exact treatment of the exceptional same-integer branch, not a stronger density theorem.

### 1.2 Barina — computational verification baseline

David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), article 810.

Published baseline:

\[
N<2^{71}
\]

is fully verified computationally.

DSD comparison:

- **EXTERNAL AHEAD in raw verified range and distributed verification engineering.**
- **INTERNAL USE:** the present universal minimality/Farey argument takes `B0=2^71` only as an external input and derives restrictions above the verified floor.
- The present project must not present its symbolic certificates as a replacement for Barina's exhaustive verification infrastructure.

### 1.3 Monks — every arithmetic progression is sufficient

Kenneth M. Monks, *The sufficiency of arithmetic progressions for the 3x+1 conjecture*, Proc. AMS 134 (2006), 2861--2872.

Monks proves every nonconstant arithmetic progression is sufficient in the standard merge/hitting sense.

DSD comparison:

\[
\boxed{
\text{sufficient / merge-sufficient}
\neq
\text{recursive smaller-merge sufficient}.
}
\]

The current repaired coverage gate needs an order condition

\[
m<n,
\qquad m\leftrightarrow n.
\]

Therefore Monks' theorem does **not** close

\[
36\mathbb N_0+27
\]

as a recursively eliminable progression.

- **EXTERNAL AHEAD in broad orbit-intersection theory.**
- **INTERNAL MORE REFINED on the order-sensitive smaller-merge gate.**

### 1.4 Simons--de Weger — nontrivial cycle exclusion

John Simons and Benne de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51--70; later online updates extend the exclusion.

Published result excludes nontrivial `m`-cycles for `m<=68`; later author versions extend this to `m<=75`.

Methods include linear forms in logarithms and computational Diophantine approximation.

DSD comparison:

- **EXTERNAL AHEAD on rigorous cycle exclusion.**
- The present project is primarily attacking divergent/minimal-counterexample first-crossing and recursive coverage, not trying to beat the cycle record.
- Cycle exclusion alone cannot prove Collatz because a nonperiodic divergent orbit remains a separate branch.

---

## 2. Ansari (2025) — exact DSD core-hinge failure

Reference:

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3) (2025), 471--480.

The paper introduces a useful order-sensitive notion of recursive sufficiency and proves several valid generic implications from that definition. The decisive problem lies in the Section 3 induction claiming all ternary sieve sets `F_n` are recursively sufficient.

### 2.1 Printed sets

The paper defines

\[
F_n=
\bigcup_{a_0,\ldots,a_{n-1}\in\{0,1\}}
\left(
4\cdot3^n\mathbb N_0
+4\sum_{i=0}^{n-1}a_i3^i+3
\right).
\]

In the inductive step it introduces an enlarged `F'_n`, removes a recursive set `A'`, and states

\[
\boxed{F_{n+1}=F'_n\setminus A'.}
\]

### 2.2 Exact n=1 regression

Direct specialization modulo `36` gives

\[
F_1\equiv\{3,7,15,19,27,31\},
\]

and from the original definition

\[
F_2\equiv\{3,7,15,19\}.
\]

Hence

\[
\boxed{F_1\setminus F_2=\{27,31\}\pmod{36}.}
\]

But the printed auxiliary construction gives

\[
F'_1
\equiv
\{3,7,11,15,19,23,27,31,35\},
\]

and

\[
A'_1\equiv\{35\},
\]

so

\[
F'_1\setminus A'_1
\equiv
\{3,7,11,15,19,23,27,31\},
\]

which is not `F_2`.

Thus

\[
\boxed{
F_2\ne F'_1\setminus A'_1.
}
\]

Status: **SAFE CORE_HINGE_FAIL of the printed induction.**

This is not a numerical approximation or interpretive disagreement; it is a direct residue counterexample to the equality consumed by Lemma 3.1.

Regression source:

`collatz/src/ansari_recursive_sufficiency_induction_audit.py`.

### 2.3 Corrected removed layer

The exact identity from the definitions is

\[
A_n:=F_n\setminus F_{n+1}
=
\left\{
4\left(
3^{n+1}p+2\cdot3^n+\sum_{i<n}a_i3^i
\right)+3
\right\}.
\]

There are exactly `2^n` residue classes modulo `4*3^(n+1)`.

For `n=1`,

\[
A_1=(36\mathbb N_0+27)\dot\cup(36\mathbb N_0+31).
\]

The `31 mod 36` class is recursive by the exact affine merge

\[
32k+27\to48k+41\to72k+62\to36k+31,
\]

with `32k+27<36k+31`.

The first unresolved layer is

\[
\boxed{36\mathbb N_0+27.}
\]

### 2.4 What survives Ansari audit

Do **not** classify the whole paper as false.

Potentially surviving pieces include:

- the definition of recursive sufficiency;
- the induction principle that a genuinely recursively sufficient sieve reduces finite verification;
- early examples such as `F0`, `F1` where smaller merges are independently established;
- order-sensitive computational-sieve philosophy.

What fails is the printed general ternary induction and downstream conclusions that specifically require every `F_n` to be recursively sufficient.

---

## 3. Current project: strongest universal branch obtained after removing Ansari dependence

The current universal route no longer uses the disputed ternary coverage.

Use the externally verified floor

\[
B_0=2^{71}.
\]

For a hypothetical minimal positive counterexample `N>B0`, if `s_j` is the number of odd shortcut steps in the first `j` steps, minimality gives

\[
(3+1/B_0)^{s_j}>2^j
\]

for every prefix.

Thus

\[
\frac{s_j}{j}>
\beta(B_0)
:=
\frac{\ln2}{\ln(3+1/B_0)}.
\]

At the first coefficient crossing `(A,q)`,

\[
\boxed{
\beta(B_0)<\frac qA<\alpha,
\qquad
\alpha=\log_3 2.
}
\]

Exact Farey/rational-log arithmetic isolates the earliest possible cell:

\[
\boxed{
(A_0,q_0)
=(114{,}208{,}327{,}604,
72{,}057{,}431{,}991).
}
\]

The buffered co-order theorem gives

\[
\boxed{2^{71}<N<2^{72}}
\]

for any paradoxical start in that cell.

Root-safe full-Hensel maximality is valid for every prefix through depth

\[
\boxed{195}.
\]

Since `N<2^72<2^195`, the depth-195 canonical residue is the ordinary start itself. The current exact finite target is therefore

\[
\boxed{
\mathcal R_{195}^{\rm coeff+nested\ root\text{-}Hensel\ max}
\cap(2^{71},2^{72}).
}
\]

Status: **SAFE relative to the external `2^71` verification floor; GLOBAL CLOSURE OPEN.**

This is the most concrete place where the present project is ahead of the published Ansari ternary program: it supplies a coverage-independent minimal-counterexample restriction rather than assuming the flawed `F_n` induction.

No claim is made that this is stronger than Tao's almost-all theorem in its own scope.

---

## 4. Kawasaki (2025) — proof claim withdrawn by its own application audit

Toshiharu Kawasaki, arXiv:2502.20642.

Version 1 was titled *A proof of the Collatz conjecture* and claimed the new fixed-point theorem proves Collatz.

In version 2 the title is changed to *Fixed point theorem in metric spaces and its application to the Collatz conjecture*. The revised text states that the conditions needed for the relevant fixed-point theorems are not satisfied in the remaining cases.

DSD verdict:

\[
\boxed{
\text{SELF-ACKNOWLEDGED APPLICATION-GATE FAILURE.}
}
\]

This should not be described as a counterexample to the abstract fixed-point theorem itself. The issue is that the Collatz map does not satisfy the hypotheses needed to consume the theorem globally.

Compared with the present project:

- Kawasaki's route does not presently produce an exceptional minimal-counterexample core.
- The current parity/Farey/Hensel chain is materially further along on Collatz-specific arithmetic constraints.

---

## 5. Nwanozie (2026) — shallow rigorous sieve, not a proof

Kevin Nwanozie, *A Rigorous Framework for the Collatz Conjecture: Structure, Constraints, and Markov Analysis*, Cambridge Open Engage, 2026.

The manuscript explicitly says it is **not a formal proof**.

It studies

\[
A=\{N\text{ odd}:v_2(3N+1)\le6\},
\]

which contains `63/64` of odd integers, and characterizes the complementary congruence class. For the complement, `v_2(3N+1)>=7` gives immediate strong descent under the accelerated odd map.

DSD verdict:

- the one-step valuation sieve is a plausible/standard **SAFE shallow reduction**;
- the Markov-chain layer is heuristic unless a deterministic trajectory-uniform bridge is proved;
- no global theorem is claimed by the author, so there is no global-proof error to refute.

Comparison:

- **EXTERNAL useful simple reduction**;
- **INTERNAL ahead in depth/adaptivity:** the prefix-dependent `485s_j>306j` spine and exact Farey crossing isolation constrain an entire hypothetical minimal-counterexample history rather than one valuation event.

---

## 6. Kawanishi weak-cover certificate — reproducibility benchmark

Recent public versions of *Machine-Checkable Weak Covering for the Collatz (3x+1) Problem* package a finite Weak Covering target with a strict verifier, checksums, and independent implementation/cross-check philosophy.

DSD comparison:

- classify as **FINITE MACHINE-CHECKABLE STRUCTURE**, not global proof unless the finite certificate has a proved universal handoff theorem;
- the public artifact discipline is a useful benchmark for this repository: exact certificates, hashes, and independent verifiers are stronger reproducibility practice than prose-only computational claims;
- the present project is currently stronger in minimal-counterexample symbolic reductions, while Kawanishi's public packaging is a useful external standard for certificate distribution.

No mathematical error is asserted here.

---

## 7. Recent complete-proof claims: mandatory DSD gates before acceptance

Several 2025--2026 preprints/Zenodo packages claim complete resolution using combinations of probabilistic mixing, finite automata, `2`-adic carries, spectral gaps, or finite certificates.

Unless full text and artifacts are checked, status is

\[
\boxed{\text{OPEN_DEEP_AUDIT, not FALSE.}}
\]

The current project's negative/barrier lemmas provide concrete regression tests for such claims.

### Gate A — average contraction is not pathwise contraction

The present project has exact counterexamples showing that a full-child average contraction cannot be upgraded to arbitrary occupied-subset contraction. Any external proof using a Markov/Doeblin/average drift theorem must prove that the **actual deterministic exceptional trajectory distribution** inherits the needed mixing.

### Gate B — finite-Q state closure

The present mixed-state audit constructs explicit families for which any fixed `3`-adic truncation `Q` loses information, and within the tested architecture complete compatibility requires at least linear memory

\[
Q(h)\ge h-3.
\]

Thus an external finite automaton with a fixed residue depth must prove a separate universal quotient theorem. A finite automaton that only models truncated residues cannot be silently identified with every actual integer trajectory.

### Gate C — Fourier decay scope

Low-frequency Fourier decay or an `L^2` mixing estimate does not automatically control the full `ell^1` tail or an arbitrary sparse survivor subset. The present selector audit identified a stronger incomplete powers-of-3 exponential-sum statement close to the Moore--Schulman open regime; that conjectural strength cannot be imported as known.

### Gate D — cycle vs divergence

Eliminating all nontrivial cycles is only one half of Collatz. Any "complete proof" built from cycle-mean or S-unit cycle exclusion must separately exclude nonperiodic divergent trajectories.

### Gate E — finite certificate handoff

A finite computation is decisive only after a theorem proves that every positive integer/counterexample maps into one of the certified finite states with all required order/same-integer information preserved.

These gates should be applied to every new complete-proof claim before attempting detailed constants verification.

---

## 8. Taha Muhammad (2026) — induction route requires full dependency audit

The public Version 7 abstract of *Collatz Sequence Proof (2nd Way)* uses an induction-like split into even and odd numbers and claims global convergence.

From the abstract alone, the key risk is whether the proof of the odd step consumes convergence of a number that has not been established to be smaller in the induction order. Collatz ordinary steps often increase an odd input, so a strong-induction proof needs an explicit decreasing measure or a proved smaller merge.

DSD status:

\[
\boxed{\text{HIGH-RISK INDUCTION GATE / FULL-TEXT AUDIT REQUIRED}.}
\]

No final mathematical-error verdict should be issued from the abstract alone.

---

## 9. Where the external literature is ahead

The present project is **not** ahead everywhere.

### Clearly external-ahead

1. Tao: rigorous almost-all theorem and deep `3`-adic/Fourier/renewal analysis.
2. Barina: exhaustive verification range and computational infrastructure.
3. Simons--de Weger: rigorous nontrivial-cycle exclusion.
4. Monks: broad sufficient-set theory for arbitrary arithmetic progressions.
5. Formalization/certificate projects: in some cases stronger public independent-verifier packaging.

The project should cite/reuse these results rather than recreate weaker versions.

---

## 10. Where the current project is genuinely more advanced or more resolved

Relative to the specific external routes audited above, the current project has stronger resolution in the following narrow senses.

### 10.1 Ansari repair / order-sensitive coverage

It has identified and regression-certified the exact published induction error, derived the correct `F_n\\F_(n+1)` layer, and isolated the first real open progression `36k+27`.

### 10.2 Coverage-independent universal minimality spine

It no longer needs the disputed ternary sieve to obtain

\[
\frac{s_j}{j}>\beta(2^{71})
\]

for every prefix of a hypothetical minimal counterexample.

### 10.3 Exact Farey first-crossing isolation

It turns the verified floor into the exact first possible coefficient-crossing cell

\[
(114208327604,72057431991),
\]

rather than a density or heuristic drift statement.

### 10.4 Same-integer / Hensel constraints

Root-safe Hensel correction maximality through depth `195` is an exact order-sensitive same-integer constraint on the first universal cell.

### 10.5 Barrier ledger

The project has explicitly rejected several attractive but invalid upgrades:

- finite selector ratios -> asymptotic theorem;
- average child contraction -> arbitrary occupied-subset contraction;
- finite-Q reverse potential -> universal pathwise elimination;
- fixed low-frequency Fourier control -> full selector mixing;
- density/mass decay -> emptiness without atom floor;
- later-block Hensel maximality without a valid root pullback;
- finite mixed coverage -> global COV-1.

This barrier ledger is a substantive advantage when auditing new proof claims.

---

## 11. Current comparative frontier

A fair hierarchy is

\[
\boxed{
\begin{array}{l|l}
\text{Question}&\text{strongest side at present}\\\hline
\text{almost-all orbit descent}&\text{Tao / external}\\
\text{verified finite range}&\text{Barina / external}\\
\text{finite-cycle exclusion}&\text{Simons--de Weger / external}\\
\text{arithmetic-progression sufficiency}&\text{Monks / external}\\
\text{Ansari ternary induction audit/repair}&\text{current DSD project}\\
\text{order-sensitive }36k+27\text{ coverage}&\text{OPEN; current project has deepest active audit}\\
\text{minimal-counterexample first-crossing cell}&\text{current DSD project, conditional only on external verified floor}\\
\text{full Collatz conjecture}&\textbf{OPEN}
\end{array}}
}
\]

The phrase "current project ahead" should therefore always be qualified by **which subproblem** is being compared.

---

## 12. Next external-audit queue

Priority order for the next full-text audits:

1. complete-resolution packages claiming deterministic small-ball / finite-automaton closure;
2. hybrid probabilistic--deterministic proofs claiming Doeblin/spectral-gap contraction;
3. machine-checkable weak-cover proofs, to inspect the universal handoff theorem rather than only the verifier;
4. recent induction-based complete-proof manuscripts;
5. any proof using a fixed-residue automaton, checked against the current linear-memory and ghost-path barriers.

For each manuscript, record:

`CLAIM -> HINGE -> DOMAIN/QUANTIFIER -> EXACT COUNTERTEST -> SURVIVOR -> STATUS`.

No proof claim is rejected merely because it differs from the present approach.

---

\[
\boxed{\text{GLOBAL COLLATZ CONJECTURE REMAINS OPEN.}}
\]

# External Collatz literature — completed DSD audit and citation ledger

Date: 2026-09-07

Status: **CURRENT AUTHORITATIVE LITERATURE LEDGER FOR THE REPOSITORY CORPUS.**

Scope: this ledger completes the audit of the external papers, preprints, and proof mechanisms that have actually been imported, compared, or used as proof-design inputs by `Math-verification/collatz` through 2026-09-07. It is **not** a claim to have audited every Collatz publication ever written.

The citation rule is deliberately non-binary:

\[
\boxed{
\text{keep valid prior art}
+\text{keep conditional reductions with hypotheses}
+\text{keep failed hinges as named anti-patterns}.
}
\]

A failed global proof does not erase valid local lemmas. A surviving local lemma does not rescue an unsupported global bridge.

---

## 1. Citation classes

### A — POSITIVE PRIOR ART

A theorem/result whose stated hypotheses and conclusion are safe to import unchanged.

Citation style: ordinary positive citation, with scope retained.

### B — CONDITIONAL / OPEN PRIOR ART

A rigorous implication or useful architecture whose required hypothesis is open, or an explicitly stated conjecture.

Citation style: cite as conditional or conjectural; never as a proved bridge.

### C — SPLIT / PARTIAL ABSORPTION

Some definitions, local lemmas, or finite theorems survive, but a distinct global hinge is missing or fails.

Citation style: cite the surviving theorem positively and the failed hinge separately as a boundary/anti-pattern.

### D — REJECTED PROOF MECHANISM / NEGATIVE CONTROL

The audited global closure mechanism has an explicit counterexample, quotient defect, quantifier failure, or invalid upgrade.

Citation style: retain the paper/project in the bibliography as a negative control, identify the exact failed claim, and state how the present proof avoids the same transition. Do **not** write a blanket `the whole paper is false` unless every material claim has actually been refuted.

### FINITE ONLY

Exact computation or bounded-range observation.

Citation style: computational evidence/certificate only; no finite-to-infinite promotion.

---

## 2. Established literature that survives audit

| Source | Current DSD class | What may be cited positively | Main boundary | Matching repository audit/commit | Completion |
|---|---|---|---|---|---|
| Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values* (2019/2022) | A | logarithmic-density almost-all theorem; 3-adic/renewal/Fourier transport framework | almost-all is not all; exceptional set may remain | `887fba789d43fa16d702c14528398cc07632cd71`, `006b095fb5259c985930094aa823d9a0af54b91a` | COMPLETE FOR REPOSITORY USE |
| David Barina, published exhaustive verification through `2^71` | A / FINITE COMPUTATIONAL THEOREM | universal verification below the stated finite floor | no statement above the floor | `006b095fb5259c985930094aa823d9a0af54b91a`; downstream first-cell commits `54aea7e4...`, `494de650...` | COMPLETE FOR REPOSITORY USE |
| Hercher / cycle-lower-bound literature | A | rigorous exclusion/lower bounds for nontrivial cycles in the stated cycle class | cycle exclusion is not divergence exclusion | `006b095fb5259c985930094aa823d9a0af54b91a` | COMPLETE FOR REPOSITORY USE |
| López–Stoll, 2-adic conjugacy / Sturmian boundary | A | parity-vector/2-adic conjugacy structure and critical-density boundary results | symbolic `Z_2` path is not automatically a positive ordinary integer | `887fba789d43fa16d702c14528398cc07632cd71`, `006b095fb5259c985930094aa823d9a0af54b91a` | COMPLETE FOR REPOSITORY USE |
| Rozier–Terracol, paradoxical Collatz sequences | A + FINITE layer | affine remainder bounds; paradoxical-sequence framework; rigorous reductions stated in the paper | reported bounded searches are finite; no universal absence theorem | `887fba789d43fa16d702c14528398cc07632cd71`, R1 downstream notes | COMPLETE FOR REPOSITORY USE |
| Tong Niu (2026), parity vectors and paradoxical sequences | A + FINITE/CONJECTURAL layer | exact parity cylinder count; analytic fixed-length paradoxical criterion/count; bounded-length density-zero theorem | CST and all-length approximation structure remain open | `1bafc5d5d2d6b6d91bc523311c9d4768ab0be95f` | COMPLETE, ADDED 2026-09-07 |
| Kenneth Monks / Monks et al., sufficient and strongly sufficient sets | A | sufficiency/strong-sufficiency routing theorems | merge sufficiency does not imply recursive sufficiency or smaller merge | `887fba789d43fa16d702c14528398cc07632cd71` | COMPLETE FOR REPOSITORY USE |

---

## 3. Conditional/open literature

| Source | Class | Safe use | Forbidden use | Matching commit | Completion |
|---|---|---|---|---|---|
| Moore–Schulman incomplete powers-of-three exponential-sum conjecture | B | motivation/conditional Fourier gate | cite as if the needed near-linear orbit cancellation were proved | `887fba789d43fa16d702c14528398cc07632cd71` | COMPLETE AS OPEN INPUT |
| conditional entropy/transport completion programs | B | architecture of what additional deterministic gates would suffice | conditional theorem -> unconditional Collatz proof | `887fba789d43fa16d702c14528398cc07632cd71` | COMPLETE AT CLAIM-SCOPE LEVEL |
| current Cerdà rigid-regime / return-map program | B/C | structural 2-adic reduction and explicitly retained entry-map/invariance/arithmetic criterion | treat the remaining criterion as already closed | `17c1aa8988f034c02c029dc6ff2954007f81a12a`, `2ac8fc96c597ede92ccb95c7f192e05fe1bbba40` | CURRENT STATUS INTEGRATED |

---

## 4. Split verdicts: valid pieces retained, failed/open hinge retained too

### 4.1 Ansari (2025), recursive sufficiency

**Positive citation:** definitions of recursive integers/recursively sufficient sets and the elementary finite-interval strong-induction reduction.

**Failed/open hinge:** the printed ternary `F_n` coverage induction does not reproduce the literal removed layer already at `F_1 -> F_2`.

Exact internal replacement:

\[
A_n=F_n\setminus F_{n+1},
\]

with first unresolved coverage progression

\[
36\mathbb N_0+27.
\]

Citation role: **C — split citation**.

Matching commits:

- `887fba789d43fa16d702c14528398cc07632cd71` — literature absorption matrix;
- `df0a6550e5a1ec2e1cdd67feae8c0f0128e325dd` — downstream dependency audit and `V_33` downgrade;
- `ffd41e25645058d2858ca973b0042b49e9cbfb27` — exact COV-1 first-crossing handoff.

Status: **COMPLETE FOR THE IMPORTED CLAIM.** The missing theorem remains a mathematical open target, not an audit task.

### 4.2 Cerdà 2-adic survival series

**Positive citation now fully reproduced:**

1. exact valuation cylinders;
2. affine branch form;
3. exact finite-itinerary noncollision;
4. exact restricted-survival mass decay by `1/2` per required `k>=2` step;
5. Haar-null infinite restricted survivor.

Independent reproduction gives, conditional on initial exact class,

\[
\frac{\mu(S_N^*)}{\mu(C_{k_0})}
=\sum_{k_1,\ldots,k_N\ge2}2^{-(k_1+\cdots+k_N)}
=2^{-N}.
\]

**Boundary / anti-upgrade:**

\[
\mu(S_\infty^*)=0
\not\Rightarrow
S_\infty^*=\varnothing,
\]

and escape from a restricted `k>=2` survivor is not by itself ordinary-integer convergence.

The author's later rigid-regime papers themselves retain an invariance/entry-map/arithmetic criterion, so the current repository treats the full program as a structural reduction with a remaining bridge rather than importing it as a complete Collatz proof.

Citation role: **C for the series as a whole; A for the reproduced cylinder/measure theorem.**

Matching commits:

- `17c1aa8988f034c02c029dc6ff2954007f81a12a` — original partial absorption / terminal-hinge audit;
- `2ac8fc96c597ede92ccb95c7f192e05fe1bbba40` — independent completion of the previously pending multi-step measure reproduction.

Status: **REPRODUCTION PENDING ITEM CLOSED.**

---

## 5. Rejected proof mechanisms retained as anti-pattern citations

### 5.1 Nwankpa finite-state / graph-theoretic proof claim

Current version audited: Preprints.org v9, *The Collatz Conjecture: A Graph-Theoretic Structural Proof*.

Failure retained:

- coarse transition table is a relation with branches depending on hidden representatives;
- all states having **a path** to `S11` is existential reachability, not inevitability of the actual trajectory;
- terminal transition from `S11` is realized specifically by `x=8`, while other `S11` representatives return internally;
- an SCC having an exit does not force every infinite internal walk to take it;
- coarse state recurrence/sink arguments do not preserve integer identity.

Citation role: **D — negative control for quotient well-definedness and liveness.**

Matching commits:

- `173b62cd3bf37886989e8399fef53a6346c7b30b` — v6 theorem-level audit;
- `096dd1fd634621c5faada4c7ffbe40fd64d32431` — exact FSM quotient regression;
- `fa404b6b3265cec6e40881220b7891e599e0af93` — v9 current-version re-audit.

Status: **CURRENT VERSION RE-AUDITED / COMPLETE FOR THE GLOBAL PROOF HINGE.**

### 5.2 Moon 2025 mod-64 LP claim

Exact witness:

\[
21\equiv85\equiv149\pmod{64}
\]

but their accelerated valuations/successors differ. Therefore exact successor data are not a function of the mod-64 state alone. A drift expression using the small residue representative in place of the actual integer also requires a separate invariance/uniform-bound argument.

Citation role: **D — state-aliasing / representative-substitution negative control.**

Matching commits:

- `422e9048f8253e29b25aaf4b2cda6582cb4aaec1` — exact aliasing certificate;
- `006b095fb5259c985930094aa823d9a0af54b91a` — literature comparison and theorem-level audit.

Status: **COMPLETE FOR THE AUDITED MOD-64 LP HINGE.**

### 5.3 Fixed universal single-halving block contraction

Exact family

\[
n_0=2^r-1
\]

has exactly `r-1` consecutive accelerated odd steps with `v_2(3n+1)=1`. Hence no fixed universal block length can force a higher valuation.

Citation role: **D — negative control for fixed-window/globalization claims.**

Matching commits:

- `4359ac9214824b18c3ad4a8d5d516182e8eab1bf` — exact counterexample regression;
- `0b2122a1bd81175ab6be5bc7ecf372aa714317e4` — mechanism audit.

Status: **COMPLETE FOR THE CLAIM CLASS.** This is intentionally not a blanket verdict on every manuscript containing a block argument.

### 5.4 Spectral-gap / annealed-to-deterministic cycle claim

The audited project established a spectral/averaged contraction statement but later withdrew the claimed deterministic cycle consequence after a `3x-1` control showed the same kind of certificate can coexist with known nontrivial cycles.

Citation role: **A for the operator/spectral result in its actual scope; D for the withdrawn deterministic-cycle upgrade.**

Matching commit:

- `4f8614fe2dabd4f22d577a10d39a05fce4b86e3a` — annealed-vs-deterministic external audit.

Status: **COMPLETE SPLIT VERDICT.**

---

## 6. Permanent anti-pattern index

The failed literature is retained because each failure supplies a regression test.

### AP-1 — ALMOST-ALL / DENSITY UPGRADE

\[
\text{almost all / measure zero exception}
\not\Rightarrow
\text{universal pointwise closure}.
\]

### AP-2 — FINITE-STATE ALIASING

\[
\text{same coarse state}
\not\Rightarrow
\text{same successor information}.
\]

### AP-3 — EXISTENTIAL REACHABILITY

\[
\forall S\;\exists\text{ good path}
\not\Rightarrow
\forall\text{ actual paths are good}.
\]

### AP-4 — FINITE WINDOW TO UNIVERSAL WINDOW

A depth bound depending on quotient resolution is not a fixed resolution-independent orbit bound.

### AP-5 — ANNEALED TO PATHWISE

Average/spectral contraction is not deterministic contraction of every realized orbit.

### AP-6 — SYMBOLIC / 2-ADIC TO ORDINARY INTEGER

An infinite symbolic survivor or nested 2-adic cylinder is not automatically a positive natural-number counterexample, nor is Haar-nullity emptiness.

### AP-7 — AUXILIARY DECOMPOSITION TO COVERAGE

A symbolic set identity used by induction must reproduce the literal removed layer before it can support universal coverage.

### AP-8 — REPRESENTATIVE SUBSTITUTION

A coarse residue representative may replace the actual integer only for quantities proved invariant or uniformly controlled on that residue class.

---

## 7. How these citations should appear in a future paper

### Positive source

State the theorem and its exact scope, then explain where it enters the present proof.

Example structure:

> Prior work establishes exact parity-cylinder uniqueness modulo `2^k`; we retain that theorem and add the present same-integer prefix constraints.

### Split source

Cite both the retained theorem and the audited boundary.

Example structure:

> The 2-adic cylinder calculation gives exact geometric decay of a restricted survivor. This does not imply emptiness; the present argument therefore keeps a separate ordinary-integer terminal gate.

### Failed proof mechanism

Do not use polemical language. Record the logical hinge and the correction.

Example structure:

> A finite-state approach can establish reachability in a coarse transition relation, but reachability does not imply that every deterministic integer trajectory realizes the exit path. We therefore require quotient well-definedness and same-integer lineage before finite-state closure.

This makes the failed source a reproducible methodological comparison rather than a rhetorical dismissal.

---

## 8. Completion audit

The 2026-09-06 master matrix left three material literature tasks unfinished or stale:

1. Cerdà multi-step survival measure — **was reproduction-pending; now CLOSED/SAFE in restricted scope** (`2ac8fc96...`).
2. Nwankpa — **old audit was v6; current v9 is now re-audited and remains D at the global hinge** (`fa404b6b...`).
3. Niu 2026 — **was absent from the formal ledger; now audited and absorbed as A + finite/conjectural split** (`1bafc5d5...`).

After these updates, no paper/result already used as an input by the current Collatz repository remains silently labeled `SAFE` while awaiting a known reproduction audit.

Items that remain mathematically OPEN are now explicitly open **research hypotheses/gates**, not unfinished audit bookkeeping.

---

## 9. Current repository rule

For future literature additions, every source must enter with

```text
SOURCE_VERSION
CLAIM_UNIT
AUDIT_CLASS: A / B / C / D / FINITE_ONLY
POSITIVE_CITATION_USE
FAILED_OR_OPEN_HINGE
PROHIBITED_UPGRADE
MATCHING_COMMIT
REPRODUCIBILITY_STATUS
```

A literature audit is complete only when both the usable theorem and the non-usable upgrade boundary are recorded.

---

## 10. Final verdict

\[
\boxed{
\text{CURRENT IMPORTED LITERATURE CORPUS: AUDIT BOOKKEEPING COMPLETE AS OF 2026-09-07.}
}
\]

This means the citation status of the literature already used by the project is explicit and traceable. It does **not** mean the Collatz conjecture is solved, and it does not mean every external Collatz manuscript has been exhaustively reviewed.
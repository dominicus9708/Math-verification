# Collatz proof architecture — full analysis and status audit

Date: 2026-09-07

Status: **CURRENT STATUS AUTHORITY / PARTIALLY CONFIRMED ARCHITECTURE / COMPLETE PROOF OPEN.**

This note is the current synthesis layer for the repository as of the 2026-09-07 full audit.  Historical notes are preserved, but where an older note gives a stronger unconditional status than this document, the newer dependency audit and this status note control the current interpretation.

Korean summary / 한글 요약:

> 현재 저장소의 핵심 계산들 가운데 published-floor Farey reduction, first universal cell localization, root-safe Hensel depth 195, first-cell 1024-block start cap, COV-1 inverse-limit criterion, and eventually-periodic negative-ghost theorem은 각각의 명시된 범위 안에서 살아남았습니다. 그러나 이 결과들은 아직 하나의 완전한 보편 증명으로 연결되지 않았습니다. 가장 중요한 미해결 브리지는 **동일한 양의 정수의 dyadic root address와 giant first-crossing correction을 끝까지 함께 보존하는 same-integer transfer**, **첫 보편 셀 이후의 무한한 later strip cells**, **genuinely aperiodic coefficient-survival branch**, 그리고 **Ansari ternary recursive-sufficiency coverage의 복구**입니다.

---

## 1. Audit lock

### Repository lock

- repository: `dominicus9708/Math-verification`
- audited main head before this report: `14db14f4a3f3546f3d3051c9ea7555a3d3866edd`
- audit regression added during this audit: `collatz/src/2026_09_07_full_core_audit_regression.py`

### DSD audit framework lock

The structural audit follows the separated DSD Audit framework in

- `dominicus9708/DSD_Method_Family/DSD_Audit/README.md`
- `DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`
- `DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md`

The domain norm remains ordinary mathematical proof validity. DSD Analysis/Audit is used to expose selections, bridges, resolution changes, lineage, and information loss; it does not replace mathematical proof.

### External floor lock

For paper-facing unconditional calculations, retain the published 2025 Barina floor

\[
\boxed{B_{\rm pub}=2^{71}.}
\]

Primary published source:

- David Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81, 810 (2025), DOI `10.1007/s11227-025-07337-0`.

The official project page, retrieved during this audit on 2026-09-07, reports a newer operational frontier

\[
\boxed{B_{\rm live}=2075\cdot2^{60}\approx2^{71.02}.}
\]

This live frontier is recorded as a **time-stamped operational input**, not silently substituted for the frozen published baseline.

---

## 2. Global verdict first

### External mathematical verdict

\[
\boxed{\text{The Collatz conjecture remains open.}}
\]

No current repository theorem closes every positive integer.

### Internal repository verdict

\[
\boxed{\textbf{PARTIALLY CONFIRMED}.}
\]

A large set of exact intermediate lemmas, reductions, counterexample regressions, and finite certificates survive.  The repository has also successfully identified and downgraded several formerly over-strong routes.

The maximum supported claim is:

> Any hypothetical minimal positive counterexample above the frozen published floor is subject to a strong collection of exact parity-prefix, first-crossing, dyadic-address, root-Hensel, and renewal constraints.  In the earliest universal first-crossing cell, its ordinary start is localized to a strict subinterval of `(2^71,2^72)` occupying only 341 of the original 1024 top-11-bit address blocks.  This does not exclude all starts in that interval, all later first-crossing cells, or the genuinely aperiodic coefficient-survival branch.

---

## 3. Base algebra and parity lineage

Use the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

For a length-`k` parity word `w`, odd count `q`, and correction `R(w)`,

\[
\boxed{
T^k(N)=\frac{3^qN+R(w)}{2^k}.
}
\]

A parity word determines one canonical starting residue modulo `2^k`.

Audit status:

\[
\boxed{\textbf{SAFE / FOUNDATIONAL}.}
\]

This exact affine identity is the lineage carrier connecting word, correction, endpoint, and dyadic address.

---

## 4. Minimal-counterexample published-floor spine

Assume a hypothetical minimal positive counterexample `N`.

Published verification gives

\[
N>2^{71}.
\]

By minimality, every positive iterate on its orbit is at least `N`; otherwise the smaller iterate converges and pulls `N` into the same convergent orbit.

If `s_j` is the number of odd shortcut steps among the first `j` steps, then

\[
\boxed{(3+1/B_{\rm pub})^{s_j}>2^j}
\]

for every prefix.

Equivalently,

\[
\frac{s_j}{j}>
\beta(B_{\rm pub})
:=
\frac{\ln2}{\ln(3+1/B_{\rm pub})}.
\]

Audit status:

\[
\boxed{\textbf{SAFE relative to the published computational floor}.}
\]

Important scope rule:

- this is a pointwise minimal-counterexample prefix theorem;
- it is not a density statement;
- it must not be transferred to arbitrary ordinary starts without the minimality/suffix-minimum premise.

---

## 5. First coefficient crossing and Farey isolation

Define the first coefficient crossing by

\[
3^{q_i}\ge2^i\quad(i<A),
\qquad
3^q<2^A.
\]

At such a crossing, the minimal-counterexample inequality implies

\[
\boxed{
\beta(B_{\rm pub})<\frac qA<\alpha,
\qquad
\alpha:=\log_3 2.
}
\]

The exact rational-log/Farey certificate gives the earliest possible strip cell

\[
\boxed{
(A_0,q_0)
=(114,208,327,604,
72,057,431,991).
}
\]

Through the previously studied second resonance the only strip cells are

\[
(A_0,q_0)
\]

and

\[
\boxed{
(217,976,794,617,
137,528,045,312).
}
\]

Audit status:

\[
\boxed{\textbf{SAFE}.}
\]

### Critical audit distinction

The theorem proves

\[
\boxed{A\ge A_0,}
\]

not

\[
A=A_0.
\]

Therefore eliminating the first universal cell does **not** eliminate all finite first-crossing possibilities.  Later strip cells remain a separate universal obligation.

Any statement of the form

> “only the first universal cell remains globally”

would be an overclaim unless an additional complete strip-coverage theorem is supplied.

---

## 6. First universal cell: buffered start localization

For the first cell, exact dangerous-axis / buffered co-order calculations give

\[
h=23,
\qquad
B=72.
\]

Thus a paradoxical start in this exact cell must satisfy

\[
N<2^{72}.
\]

Together with the published floor,

\[
\boxed{2^{71}<N<2^{72}.}
\]

Audit status:

\[
\boxed{\textbf{SAFE CONDITIONAL ON BEING IN THE FIRST CELL}.}
\]

The condition “being in the first cell” is essential lineage information.

---

## 7. Root-safe full-Hensel maximality

For another length-`k`, weight-`q` word `u` in the same full-Hensel correction class,

\[
R(u)\equiv R(w)\pmod{3^q},
\]

if `R(u)>R(w)` then

\[
\Delta=rac{R(u)-R(w)}{3^q}\in\mathbb Z_{>0}
\]

and

\[
T_u^k(N-\Delta)=T_w^k(N).
\]

If `0<\Delta<N`, root minimality gives a contradiction.  Hence the actual root prefix must maximize correction inside its full-Hensel class whenever every possible positive credit is below `N`.

Using coefficient survival,

\[
q_k\ge b(k):=\min\{q:3^q\ge2^k\},
\]

and the fixed-`q` credit envelope

\[
\Delta
<
2^{k-q}
\left(1-\left(\frac23\right)^q\right),
\]

the exact published-floor transition is

\[
\boxed{
K_{\rm root-safe}=195,
}
\]

with first envelope failure

\[
\boxed{(k,q)=(196,124).}
\]

Independent exact arithmetic in the 2026-09-07 audit reproduced this transition.

Audit status:

\[
\boxed{\textbf{SAFE ROOT-MINIMALITY OBLIGATION}.}
\]

### What is and is not established

Established:

> A hypothetical original minimal counterexample in the first cell must satisfy nested full-Hensel root maximality at every prefix through depth 195.

Not established:

> The complete depth-195 survivor intersection has already been enumerated or proved empty.

The latter remains open.

### Same-integer advantage

Since

\[
N<2^{72}<2^{195},
\]

the canonical residue modulo `2^195` is the ordinary start itself.

Thus the first-cell problem becomes an exact ordinary-integer intersection problem, not merely a residue-density problem.

---

## 8. Correction-only barrier

For the latest mechanical first-crossing word,

\[
p_r=\lfloor(r-1)\log_2 3\rfloor,
\]

the normalized correction is

\[
S_*
=
\frac13
\sum_{n=0}^{q_0-1}
2^{-\{n\log_2 3\}}.
\]

The exact two-term rotation pairing gives

\[
\boxed{
S_*>rac{7q_0-1}{36}.
}
\]

Exact rational logarithm bounds then certify

\[
\boxed{
S_*>1.07\,B_{\rm pub}\varepsilon,
}
\]

where

\[
\varepsilon=rac{2^{A_0}-3^{q_0}}{3^{q_0}}.
\]

Audit status:

\[
\boxed{\textbf{SAFE NEGATIVE / PRUNING RESULT}.}
\]

Interpretation:

- correction capacity alone is not too small;
- therefore a proof that only upper-bounds scalar correction and compares it to `B_pub*epsilon` cannot close the whole first cell;
- the missing obstruction must retain the same word's dyadic address.

This is not an existence theorem for a positive counterexample.

---

## 9. Exact 1024-block correction cap

Define

\[
H_m(x)
=
\sum_{j=0}^{m-1}
2^{-\{x+j\theta\}},
\qquad
\theta=\log_2(3/2).
\]

At `m=1024`, every phase power

\[
2^{\{j\theta\}}
\]

is represented exactly as a rational ratio of `3^j` and a power of `2`.  Between wrap thresholds, `H_m(x)` is a positive constant times `2^{-x}`, so its global maximum occurs at a finite set of exact threshold candidates.

Independent 2026-09-07 reconstruction found

\[
\frac{\max_x H_{1024}(x)}{1024}
\approx0.7219603657483404
<0.722
=
\frac{361}{500}.
\]

The repository certificate then proves the universal first-cell correction bound strong enough to exclude every start

\[
N\ge
\frac{1365}{1024}2^{71}.
\]

Hence

\[
\boxed{
2^{71}<N<
\frac{1365}{1024}2^{71}
=1365\cdot2^{61}.
}
\]

The old one-bit source interval loses exactly

\[
\boxed{
\frac{683}{1024}
}
\]

of its width, leaving

\[
\boxed{341}
\]

top-11-bit address blocks,

\[
1024,1025,\ldots,1364.
\]

Audit status:

\[
\boxed{\textbf{SAFE POSITIVE REDUCTION}.}
\]

### Information-loss audit

The 1024-block estimate is intentionally non-injective: it aggregates away the exact dyadic address.  Therefore it may safely produce a scalar **upper start cap**, but it cannot prove emptiness of the remaining address blocks by itself.

This is the exact place where the proof must change resolution from aggregate correction back to same-integer address lineage.

---

## 10. Current first-cell same-integer target

The current high-priority universal target is the intersection of

1. the 341 remaining root-address blocks;
2. coefficient survival through every prefix before `A_0`;
3. nested root-Hensel maximality through depth 195;
4. extension to the exact terminal first-crossing cell `(A_0,q_0)`;
5. enough terminal correction to keep the endpoint at least the same start.

For a fixed ordinary start `N`, let `E(N)` be its first-cell admissible extension language.  The desired pointwise inequality is

\[
\boxed{
\sup_{w\in E(N)}S(w)<\varepsilon N
}
\]

for every surviving ordinary start.

Audit status:

\[
\boxed{\textbf{OPEN}.}
\]

This is currently the cleanest same-integer bridge for the first universal cell.

---

## 11. Recursive-sufficiency / COV route

### 11.1 What survives from Ansari

The definitions of recursive integers and recursively sufficient sets, and the finite-interval strong-induction principle, are sound and usable.

Status:

\[
\boxed{\textbf{SAFE PARTIAL ABSORPTION}.}
\]

### 11.2 What failed

The asserted ternary `F_n` recursive-sufficiency induction does not reproduce the literal removed layer already at

\[
F_1\to F_2.
\]

The exact difference includes

\[
36\mathbb N_0+27
\]

and

\[
36\mathbb N_0+31.
\]

The `31 mod 36` branch has an explicit smaller merge, while

\[
\boxed{36\mathbb N_0+27}
\]

remains the first unresolved branch `COV_1`.

Status of the old global ternary coverage:

\[
\boxed{\textbf{OPEN / CONDITIONAL}.}
\]

### 11.3 Consequence for `V_33`

The exact finite `m=44` selector computations remain valid for the enumerated selector families.

However the promotion of their endpoint to a continuous global floor

\[
V_{33}
\]

requires the reopened ternary coverage theorem.

Therefore:

\[
\boxed{\text{finite selector calculations: SAFE},}
\]

but

\[
\boxed{V_{33}\text{ as universal minimal-counterexample floor: CONDITIONAL}.}
\]

Any historical note that uses `V_33` unconditionally must be read through the 2026-09-06 dependency correction.

### 11.4 COV-1 finite first-crossing audit

The exact word-level certificate checks every root-`11` first crossing through binary depth 38 in the progression

\[
36k+27.
\]

Recorded count:

\[
150,456,308
\]

first-crossing words, with zero paradoxical cases in that finite range.

Status:

\[
\boxed{\textbf{FINITE ONLY}.}
\]

No arbitrary-depth conclusion follows.

### 11.5 COV-1 inverse-limit terminal criterion

Nested parity prefixes define a compatible sequence of `k mod 2^{L-2}` residues and hence a unique

\[
k_\infty\in\mathbb Z_2.
\]

Taking least nonnegative representatives `c_L`, one has

\[
\boxed{
k_\infty\in\mathbb N_0
\iff
c_L\text{ is eventually constant}.
}
\]

Therefore an infinite open symbolic branch is harmless if its parameter sequence never stabilizes to an ordinary nonnegative integer.

Status:

\[
\boxed{\textbf{SAFE TERMINAL REDUCTION}.}
\]

Open:

\[
\boxed{
\text{genuinely aperiodic open branch}
\Longrightarrow
c_L\text{ nonstabilizing}.
}
\]

### 11.6 COV hierarchy completeness

Even a future proof of `COV_1` would repair only the first removed layer.  A full recursive-sufficiency proof still requires a general theorem covering the higher removed layers `COV_n`, or another argument that bypasses them.

Thus

\[
\boxed{\text{COV}_1\text{ closure alone }\not\Rightarrow\text{ Collatz}.}
\]

---

## 12. R1/R2 renewal route

For a hypothetical nonperiodic first-descent survivor, the renewal-floor coefficient-stopping architecture splits into two exact cases.

### R1 — infinitely many finite coefficient crossings

Infinitely many renewal floors generate paradoxical first-crossing prefixes.

Status:

\[
\boxed{\textbf{STRUCTURAL DICHOTOMY SAFE; UNIVERSAL ELIMINATION OPEN}.}
\]

The first-crossing/Farey machinery strongly constrains this branch, but does not yet exclude every possible later strip cell.

### R2 — eventual coefficient survival

Eventually every renewal floor has infinite coefficient stopping time, producing a dual-record critical meander.

Status:

\[
\boxed{\textbf{STRUCTURAL DICHOTOMY SAFE; APERIODIC ELIMINATION OPEN}.}
\]

### Eventually periodic R2 tail

For a periodic tail of length `H`, odd count `S`, and correction `C>0`, the periodic 2-adic state is

\[
x=rac{C}{2^H-3^S}.
\]

Persistent coefficient survival forces

\[
3^S>2^H,
\]

so

\[
x<0.
\]

A finite preperiod cannot restore positivity.

Hence

\[
\boxed{
\text{eventually periodic coefficient survivor}
\Longrightarrow
\text{negative rational 2-adic ghost}.
}
\]

Status:

\[
\boxed{\textbf{SAFE / CLOSED FOR THE PERIODIC SUBBRANCH}.}
\]

The genuinely aperiodic R2 boundary remains open.

---

## 13. External literature audit status

### Safe external inputs / comparisons

- Barina published computational floor `2^71`.
- Tao almost-all / logarithmic-density result: statistical benchmark only.
- parity-vector / 2-adic conjugacy results used with their exact symbolic-vs-natural distinction.
- Monks-style sufficiency results: routing/merge constraints, not recursive minimality.
- valid local arithmetic and one-step cylinder facts from later 2-adic survival-set work.

### Partial or conditional inputs

- Ansari recursive-sufficiency definitions survive, but ternary global coverage is reopened.
- Rozier–Terracol paradoxical-sequence results may support R1 bounds exactly as cited, but finite reported frontiers remain finite evidence.
- any current live computational frontier beyond `2^71` is time-sensitive operational evidence unless separately frozen and archived.

### Rejected universal proof mechanisms retained as regressions

The repository now has explicit counterexamples or audits against:

- finite-state quotient closure that aliases distinct integer states;
- fixed single-halving window claims;
- annealed/spectral contraction silently upgraded to deterministic pointwise contraction;
- finite or measure-zero survivor decay upgraded to emptiness;
- arbitrary later-block Hensel maximality;
- restricted survivor-set escape upgraded to convergence without terminal branch closure.

These failures strengthen the present architecture by defining prohibited transitions.

---

## 14. Current official computational frontier sensitivity

The official Barina project page retrieved in this audit reports

\[
B_{\rm live}=2075\cdot2^{60}>2^{71}.
\]

A separate exact sensitivity check in the audit regression shows:

1. the first Farey cell `(A_0,q_0)` remains inside the narrower live-floor strip;
2. the root-safe Hensel transition remains exactly depth 195 with first envelope failure `(196,124)`.

If one were to use the live frontier operationally while retaining the already proved absolute first-cell upper cap `1365*2^61`, the surviving source interval would touch 328 top-11-bit blocks rather than 341, with the lowest of those only partially occupied.

Status:

\[
\boxed{\textbf{CURRENT OPERATIONAL SENSITIVITY ONLY}.}
\]

Do not silently replace the published baseline in paper-facing claims.

---

## 15. DSD eight-axis analysis

| Axis | Current result |
|---|---|
| D — Describability | Strong. The principal states, words, residues, corrections, floors, and branch assumptions are explicit. |
| R — Resolution | Mixed but now better controlled. Exact integer/residue statements, aggregate correction bounds, and density results are explicitly separated. |
| S — Selection | First cell, COV-1, and periodic R2 are legitimate subproblems, but none is exhaustive by itself. |
| E — Exclusion | Exact start-cap and negative-ghost exclusions are justified. Density/finite-state/finite-depth exclusions are prohibited from universal upgrade. |
| T — Transition | Main remaining risk. The critical open bridges are correction→same address, finite witnesses→same natural integer, and repaired ternary coverage. |
| C — Consistency | Improved after the V33/Ansari audit. Historical files still contain stronger legacy language, so dependency precedence must be respected. |
| N — Norm | Ordinary universal mathematical proof is the standard. DSD labels do not replace theorem proof. |
| O — Outcome | Strong partial structure and pruning; no complete Collatz proof. |

---

## 16. Transition and lineage audit

| Step | Transition | Identity preserved? | Status |
|---|---|---:|---|
| published verification → `N>2^71` | minimal counterexample floor | yes | JUSTIFIED |
| minimality → every iterate `>=N` | smaller iterate would converge | yes | JUSTIFIED |
| prefix inequality → Farey strip | exact logs / rationals | yes | JUSTIFIED |
| Farey strip → `A>=A0` | neighbor denominator theorem | yes | JUSTIFIED |
| `A>=A0` → `A=A0` | not available | no | UNSUPPORTED |
| first cell → `N<2^72` | buffered co-order | yes | JUSTIFIED |
| first cell → 1024-block cap | exact rotation max | partially aggregated | JUSTIFIED for cap only |
| scalar correction → cell emptiness | address discarded | no | UNSUPPORTED |
| minimal root → Hensel max through 195 | exact merge credit | yes | JUSTIFIED |
| later orbit block → same Hensel rule | root minimality lost | no | CONTRADICTED by prior regression |
| finite COV witnesses → one natural `k` | quantifier swap | no | UNSUPPORTED |
| nested COV residues → `Z_2` limit | inverse-limit compatibility | yes | JUSTIFIED |
| eventual stabilization → natural `k` | least representative theorem | yes | JUSTIFIED |
| measure zero → emptiness | atom identity lost | no | UNSUPPORTED |
| finite m44 layers → global `V33` | requires Ansari coverage | conditional | CONDITIONALLY_JUSTIFIED |
| periodic coefficient survivor → positive integer | sign theorem blocks it | no | CONTRADICTED |

---

## 17. Contradiction / overclaim audit

### No new substantive contradiction found in the current safe core

Independent reconstruction during this audit reproduced:

- the first Farey cell and the two-cell list through the second resonance;
- root-safe depth 195 and first failure `(196,124)`;
- the exact 1024-block maximum inequality;
- the `1365*2^61` first-cell upper start cap.

### Historical scope conflicts remain

Older notes predating the 2026-09-06 coverage audit may still describe

- `V33` as unconditional;
- the second/current resonance as the sole universal R1 obstruction;
- arbitrary later-block Hensel/L7 maximality more strongly than now allowed.

These are **legacy scope conflicts**, not current accepted conclusions.

This document and the explicit dependency-correction notes supersede those universal readings without deleting historical records.

---

## 18. Reproducibility audit

### Positive

The repository contains exact integer/rational certificates for the principal modern reductions.

The 2026-09-07 audit adds

`collatz/src/2026_09_07_full_core_audit_regression.py`

as a lightweight cross-check of:

- Farey isolation;
- first two strip cells;
- root-safe depth 195;
- exact 1024-block phase maximum bound;
- first-cell source cap;
- time-stamped live-frontier sensitivity.

No random seed or floating-point assertion is required.

### Remaining reproducibility weakness

The audited latest repository head has no attached GitHub combined-status checks.  Certificates exist, but their execution is not currently enforced by repository CI at every revision.

Status:

\[
\boxed{\textbf{REPRODUCIBLE BY SCRIPT, CI ENFORCEMENT OPEN}.}
\]

---

## 19. Current proof-obligation hierarchy

### Priority U1 — same-integer first-cell transfer

Intersect the 341 root-address blocks with nested root-Hensel constraints through 195 and first-cell terminal correction.

This is the most concrete current universal finite-address target.

### Priority U2 — later Farey strip cells

Develop a uniform theorem or state compression that does not require treating infinitely many later coefficient-crossing cells individually.

Closing only `(A_0,q_0)` is not sufficient.

### Priority U3 — genuinely aperiodic coefficient survival

Prove that every genuinely aperiodic infinite survivor corresponds to a non-natural 2-adic state, or otherwise force descent/merge.

The eventually-periodic portion is already closed.

### Priority C1 — repaired ternary recursive sufficiency

Close `COV_1` and then prove a general removed-layer theorem for `COV_n`, if the ternary route is to recover its former global-floor role.

### Priority R — automated dependency/status regression

Keep historical calculations but add machine-readable/current status checks so that conditional floors cannot be accidentally imported as unconditional assumptions.

---

## 20. Final status matrix

| Component | Current verdict |
|---|---|
| Shortcut affine parity identity | SAFE |
| Published floor `2^71` | SAFE EXTERNAL COMPUTATIONAL INPUT |
| Minimal-counterexample prefix spine | SAFE |
| Earliest Farey first-crossing cell | SAFE |
| Claim that first crossing must equal earliest cell | NOT ESTABLISHED |
| First-cell `N<2^72` | SAFE IN FIRST CELL |
| Root-Hensel necessity through depth 195 | SAFE |
| Depth-195 intersection emptiness | OPEN |
| Correction-only full-cell closure | CLOSED AS INSUFFICIENT STRATEGY |
| 1024-block cap / 341 address blocks | SAFE |
| Same-integer 341-block terminal transfer | OPEN |
| Exact finite m44 selector computations | SAFE FINITE |
| `V33` as universal floor | CONDITIONAL |
| Ansari ternary global coverage | OPEN / PARTIAL ABSORPTION |
| COV-1 finite depth-38 audit | FINITE ONLY |
| COV-1 inverse-limit criterion | SAFE REDUCTION |
| COV-1 universal closure | OPEN |
| Higher `COV_n` coverage | OPEN |
| R1/R2 dichotomy | SAFE STRUCTURAL REDUCTION |
| Eventually periodic coefficient-survival branch | CLOSED AS NEGATIVE GHOST |
| Genuinely aperiodic coefficient-survival branch | OPEN |
| Full Collatz conjecture | OPEN |

---

## 21. Audit conclusion

The current project is **not** in a state where one remaining numerical calculation would automatically produce a proof.

It is, however, substantially cleaner than before the September 6 dependency audits:

1. old selector-dependent global claims are separated from universal claims;
2. measure/density/finite-state proof shortcuts are explicitly blocked;
3. root-minimality is restricted to the original start where it is valid;
4. symbolic 2-adic survivors are separated from ordinary positive integers;
5. the earliest universal first-crossing cell has been reduced from a one-bit interval to 341 exact top-address blocks;
6. the remaining first-cell obstruction is now a concrete same-integer bridge rather than a vague correction-size problem.

The strongest next move is therefore **not** to deepen scalar correction estimates indiscriminately.  It is to build an address-preserving transfer that compresses the 341 root blocks while preserving the exact nested parity/Hensel lineage to the terminal cell.

That target should be treated as the next universal proof experiment, while later strip cells and the genuinely aperiodic R2 boundary remain explicitly visible as separate global obligations.

# Collatz verification / current index

이 문서는 `collatz/`의 **현재 정본 진입점**입니다.

과거 계산·실패 경로·조건부 경로는 기존 파일과 커밋에 그대로 보존합니다. 이 README는 현재 살아 있는 계산선과 감사 경계를 빠르게 찾기 위한 인덱스입니다.

## Current global status

- **Collatz conjecture:** `OPEN`
- **First universal Farey cell:** `OPEN`
- **Proof architecture:** `PARTIALLY_CONFIRMED`
- finite computation은 universal proof로 승격하지 않음

## Frozen external verification baseline

Theorem-facing baseline:

\[
B_{\rm pub}=2^{71}.
\]

더 최근 live verification 값은 operational sensitivity로만 관리하며 published baseline을 조용히 대체하지 않습니다.

## Current first universal cell

Earliest first-coefficient-crossing cell:

\[
(A_0,q_0)=(114{,}208{,}327{,}604,\;72{,}057{,}431{,}991).
\]

Current exact start window:

\[
2^{71}<N<\frac{1364}{1024}2^{71}=1364\cdot2^{61}.
\]

Thus the current top-address labels are

\[
a=1024,\ldots,1363,
\]

exactly **340 blocks**.

The scalar correction-only route stops at this 340-block frontier; later work must preserve same-integer information.

## Current exact chain

### MATH-004 — endpoint q-lock

For candidate-language universal-spine prefixes through the first crossing,

\[
S=R/3^q\le q/3<2^{71}.
\]

Thus same endpoint implies same `q` within the audited candidate scope. With equal q,

\[
R_1-R_2=3^q(N_2-N_1),
\qquad
N_1<N_2\iff R_1>R_2.
\]

This does not automatically extend arbitrary-word full-Hensel maximality beyond its separately audited scope.

### MATH-005 — 340-block endpoint locality

Same-endpoint candidate starts satisfy

\[
|N_1-N_2|\le24{,}019{,}143{,}996<2^{35}.
\]

One endpoint fiber can therefore couple at most two adjacent `2^61` address blocks. The small halo ratio is locality information, not an emptiness theorem.

### MATH-006 — exact 61+11 address transducer

Write

\[
N=a2^{61}+x,
\qquad1024\le a\le1363.
\]

If the lower-61 state is `(q,y)` with `y=T^61(x)`, then

\[
T^{61}(N)=y+a3^q,
\]

and the final 11 parity bits depend on

\[
(y+a3^q)\bmod2048.
\]

Exact surviving-label ranges:

| `q61` | min | max |
|---:|---:|---:|
| 39 | 36 | 47 |
| 40 | 124 | 141 |
| 41 | 221 | 235 |
| 42 | 288 | 303 |
| 43 | 320 | 333 |
| 44 | 336 | 340 |
| 45 | 339 | 340 |
| 46–61 | 340 | 340 |

In particular,

\[
q_{61}=39\Longrightarrow\text{at most }47/340\text{ labels survive}
\]

for every base endpoint phase. This is exact and pointwise, not probabilistic.

### MATH-007 — right-congruence barrier

Distinct exact 340-label masks as `y mod 2048` varies:

| `q61` | distinct masks |
|---:|---:|
| 39–43 | 2048 |
| 44 | 1838 |
| 45 | 341 |
| 46–61 | 1 |

Hence the strong low-surplus range cannot discard endpoint phase through a nontrivial exact coarse quotient.

### MATH-008 — actual lower-61 phase reachability

\[
\#\operatorname{Reach}_{61}(q)=
\begin{cases}
2048,&39\le q\le58,\\
1166,&q=59,\\
58,&q=60,\\
1,&q=61.
\end{cases}
\]

All 2048 phases really occur wherever MATH-006 can reject any labels (`q61=39..45`). Therefore phase-sparsity refinement is `STRATEGY SATURATION`; it cannot turn per-phase caps into fixed global block exclusions.

### MATH-009 — Hensel/endpoint ordering redundancy

Inside one fixed `(k,q,E)` endpoint fiber,

\[
R_1-R_2=3^q(N_2-N_1).
\]

Minimum-start ordering and correction-max ordering are therefore the same affine order in opposite coordinates.

Status:

`CONFIRMED / REDUNDANT / NO NEW PRUNING`.

### MATH-010 — DSD-native representation gate

The calculation now distinguishes

- `BASE_ENDPOINT`: `y mod 2048`;
- `ADDRESS_LIFTED`: `(y+a3^q) mod 2048`.

The transition

\[
\texttt{BASE\_ENDPOINT}\to\texttt{ADDRESS\_LIFTED}
\]

is permitted exactly once. A second lift is rejected. This caught the attempted double-counting of the affine address term while preserving all MATH-006 arithmetic exactly.

The state also records first-failure depth and coefficient margin.

### MATH-011 — complete descriptor + cyclic-window acceleration

For lifted residue `r mod 2048`, let `s_j(r)` be the number of odd tail steps through `j`. Define

\[
H(r)=\max_{1\le j\le11}\bigl(q_{\min}(61+j)-s_j(r)\bigr).
\]

Then

\[
r\text{ survives through depth72}\iff q_{61}\ge H(r).
\]

Exact distribution:

`39:247, 40:554, 41:570, 42:406, 43:195, 44:63, 45:12, 46:1`.

With `m=3^q mod 2048` and `z=m^{-1}y`, the 340-address arithmetic progression becomes a cyclic contiguous window. The full legacy 2048-count vector is reproduced for every `q61=39..61`.

The expensive address-predicate evaluation layer drops from

\[
23\cdot2048\cdot340=16{,}015{,}360
\]

to

\[
23\cdot2048=47{,}104
\]

threshold evaluations, an exact factor-340 reduction at that layer.

Status:

`CONFIRMED WITHIN SCOPE / COMPUTATIONAL ACCELERATION / NO NEW BLOCK EXCLUSION`.

### MATH-012 — Hensel even-budget complete descriptor

The existing root-Hensel arithmetic-credit predicate at the frozen floor is

\[
2^{k-q}\left(1-\left(\frac23\right)^q\right)<2^{71}.
\]

For `q>=2` this is exactly equivalent to

\[
\boxed{k-q\le71.}
\]

Thus

\[
d=k-q
\]

—the number of even shortcut steps in the prefix—is a complete descriptor for **this arithmetic-credit predicate only**.

Combining coefficient survival and the credit gate gives

\[
\boxed{Q_*(k)=\max\{q_{\min}(k),k-71\}.}
\]

The historical uniform boundary is refined as

\[
(195,124):\text{ credit safe},
\]

\[
(196,124):\text{ coefficient-safe / credit-unsafe},
\]

\[
(196,125):\text{ credit safe}.
\]

So depth 196 is the first point where the **lowest coefficient-surviving branch** loses this credit; higher-q branches may remain arithmetically eligible. This does not automatically validate every other condition needed for full arbitrary-word Hensel maximality.

The certificate regresses all `130,816` states with

\[
2\le q\le k\le512
\]

against the original exact large-integer inequality with zero mismatches.

Status:

`CONFIRMED / EXACT ARITHMETIC-CREDIT DESCRIPTOR / COMPUTATIONAL ACCELERATION / NO NEW COLLATZ EXCLUSION`.

## Current frontier

Use DSD complete descriptors as **calculation gates**, not as decorative metadata.

The next target is the part of depth-72+ Hensel/endpoint eligibility that remains after the cheap gate

\[
k-q\le71.
\]

The question is whether the remaining non-redundant correction/word/endpoint conditions admit another small exact descriptor. If they do, use it for safe state merging or early rejection of the **proof mechanism**; if they do not, retain the full state instead of forcing an unsafe quotient.

A failed Hensel-credit gate is not a failed Collatz candidate.

## Canonical current documents

- [`notes/2026-09-07-full-proof-architecture-analysis-and-status.md`](notes/2026-09-07-full-proof-architecture-analysis-and-status.md)
- [`notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md`](notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md)
- [`notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md`](notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md)
- [`notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md`](notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md)
- [`notes/2026-09-08-root-hensel-endpoint-ordering-redundancy.md`](notes/2026-09-08-root-hensel-endpoint-ordering-redundancy.md)
- [`notes/2026-09-08-dsd-native-61plus11-computation-pilot.md`](notes/2026-09-08-dsd-native-61plus11-computation-pilot.md)
- [`notes/2026-09-08-dsd-complete-descriptor-and-cyclic-window-acceleration.md`](notes/2026-09-08-dsd-complete-descriptor-and-cyclic-window-acceleration.md)
- [`notes/2026-09-08-hensel-even-budget-complete-descriptor.md`](notes/2026-09-08-hensel-even-budget-complete-descriptor.md)
- [`src/2026_09_08_dsd_complete_descriptor_cyclic_window_acceleration.py`](src/2026_09_08_dsd_complete_descriptor_cyclic_window_acceleration.py)
- [`src/2026_09_08_dsd_hensel_even_budget_descriptor.py`](src/2026_09_08_dsd_hensel_even_budget_descriptor.py)

DSD formal audits are indexed at:

`dominicus9708/DSD_Method_Family/DSD_Audit/audits/mathematics/README.md`.

## Directory roles

```text
collatz/
├─ README.md
├─ notes/
├─ src/
├─ results/
└─ wolfram/
```

Historical files remain in place for traceability.

## External literature audit policy

Any new external theorem used as a calculation input is audited before use.

- `A` — positive prior art / safe in exact scope
- `B` — conditional prior art
- `C` — partial absorption
- `D` — audited anti-pattern / negative methodological example
- `FINITE ONLY` — finite evidence only

## Prohibited upgrades

- finite verification `⇒` universal proof
- almost all / density one / measure zero `⇒` all / emptiness
- coarse FSM reachability `⇒` inevitable ordinary-integer trajectory
- endpoint quotient + root-Hensel maximality as independent filters
- local endpoint q-lock `⇒` arbitrary later-block Hensel maximality
- per-phase surviving-label cap `⇒` fixed globally excluded labels
- full phase reachability at depth61 `⇒` arbitrary deeper-state reachability
- `ADDRESS_LIFTED` `⇒` valid input for another address lift
- finite complete descriptor `⇒` arbitrary-depth completeness
- `k-q>71` `⇒` Collatz candidate excluded
- same `k-q` `⇒` same full Collatz/Hensel state
- arithmetic-credit safe `⇒` all Hensel assumptions safe
- computational acceleration `⇒` stronger Collatz theorem
- route saturation `⇒` first-cell or Collatz closure

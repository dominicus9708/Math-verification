# Collatz verification / current index

이 문서는 `collatz/`의 **현재 정본 진입점**입니다.

과거 계산·실패 경로·조건부 경로는 추적성을 위해 기존 파일에 그대로 보존합니다. 이 README는 현재 살아 있는 증명선과 감사 상태를 가리키는 인덱스입니다.

## Current global status

- **Collatz conjecture:** `OPEN`
- **First universal Farey cell:** `OPEN`
- **Current proof-architecture audit:** `PARTIALLY_CONFIRMED`
- **Finite computation:** universal proof로 승격하지 않음

## External verification baseline

Paper-facing frozen baseline:

\[
B_{\rm pub}=2^{71}.
\]

최소반례 논증의 공개 정리에는 이 값을 사용합니다. 더 최근 live verification 값은 operational sensitivity로만 관리하며 published baseline을 조용히 대체하지 않습니다.

## Current first universal cell

Earliest first-coefficient-crossing cell:

\[
(A_0,q_0)=(114{,}208{,}327{,}604,\;72{,}057{,}431{,}991).
\]

Current exact start window:

\[
2^{71}<N<\frac{1364}{1024}2^{71}=1364\cdot2^{61}.
\]

Surviving top-11-bit address labels:

\[
a=1024,\ldots,1363,
\]

즉 **340개 block**입니다.

Denjoy–Koksma/Ostrowski bound 이후 scalar correction-only route는 block `1363`부터 whole-block elimination을 제공하지 못합니다. 이후 계산은 same-integer address coupling을 보존해야 합니다.

## Current same-integer structure

### Endpoint q-lock across the first cell

Candidate-language universal-spine prefixes satisfy

\[
S=R/3^q\le q/3<2^{71}
\]

through the first universal crossing. Hence within the current candidate window,

\[
T^k(N_1)=T^k(N_2)\Longrightarrow q_1=q_2.
\]

With equal `q`,

\[
R_1-R_2=3^q(N_2-N_1),
\qquad
N_1<N_2\iff R_1>R_2.
\]

This is address-faithful. It does **not** extend arbitrary-word full-Hensel maximality to the whole first crossing.

### MATH-009: Hensel/endpoint ordering redundancy

Inside one fixed `(k,q,E)` endpoint fiber,

\[
2^kE=3^qN_i+R_i
\]

implies

\[
R_1-R_2=3^q(N_2-N_1).
\]

Therefore minimum-start ordering and correction-maximum ordering are the same affine ordering in opposite coordinates. They must not be counted as independent pruning filters.

Status: `CONFIRMED / REDUNDANT / NO NEW PRUNING`.

### 340-block locality

Same-endpoint candidate starts satisfy

\[
|N_1-N_2|\le24{,}019{,}143{,}996<2^{35}.
\]

Each top-address block has width `2^61`, so one endpoint fiber can couple at most two adjacent blocks. Cross-block dependence is confined to thin halos around the 339 internal boundaries.

This is a locality theorem, not an emptiness or density argument.

## 61+11 exact address transducer

Write

\[
N=a2^{61}+x,
\qquad1024\le a\le1363.
\]

If the lower-61 state is `(q,y)` with `y=T^61(x)`, then

\[
T^{61}(N)=y+a3^q,
\]

so the final 11 parity bits are determined by

\[
(y+a3^q)\bmod2048.
\]

For the current 340 labels, exact pointwise surviving-label ranges are:

| `q61` | min survivors | max survivors |
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

for every base endpoint residue. This is an exact pointwise cap, not a probability statement.

### Right-congruence barrier

Number of distinct exact 340-label survival masks as `y mod 2048` varies:

| `q61` | distinct masks |
|---:|---:|
| 39–43 | 2048 |
| 44 | 1838 |
| 45 | 341 |
| 46–61 | 1 |

Thus in the strongest low-surplus range, endpoint phase cannot be discarded by a nontrivial exact coarse quotient.

### Lower-61 endpoint-phase reachability saturation — MATH-008

\[
\#\operatorname{Reach}_{61}(q)=
\begin{cases}
2048,&39\le q\le58,\\
1166,&q=59,\\
58,&q=60,\\
1,&q=61.
\end{cases}
\]

For `q61=39..58`, every phase has an explicit ordinary-integer witness. For `q61=59..61`, the valid universal-spine parity-word languages were exhaustively enumerated.

Every range where MATH-006 rejects any labels (`39..45`) already reaches all 2048 phases. Reachability sparsity therefore cannot convert the pointwise masks into a fixed global block exclusion. This strategy branch is `SATURATED`.

## MATH-010: DSD-native computation pilot

DSD has now been inserted into the calculation state itself while leaving the exact Collatz arithmetic unchanged.

The phase representation is split into two stages:

- `BASE_ENDPOINT`: `y mod 2048`;
- `ADDRESS_LIFTED`: `(y+a3^q) mod 2048`.

The DSD transition gate permits the address lift exactly once:

\[
\texttt{BASE\_ENDPOINT}\to\texttt{ADDRESS\_LIFTED}.
\]

A second lift is rejected by a negative control.

This caught a concrete semantic problem in the proposed post-MATH-008 refinement: **MATH-006 already computes**

\[
r=(y+a3^q)\bmod2048.
\]

Therefore feeding `y+a3^q` back into the existing MATH-006 predicate as though it were a new base endpoint would double-count the same address contribution. That proposed extra affine-coupling filter is not independent pruning.

The DSD-native implementation regression-reproduces all MATH-006 min/max label counts exactly.

### First-failure / margin diagnostics

Each lifted tail residue now carries:

- `first_fail_depth`;
- `minimum_coefficient_margin` over depths 62..72;
- `SURVIVE/EXCLUDED` outcome;
- explicit representation stage and resolution.

For `q61=39`, the 2048 lifted residues decompose exactly as:

| first outcome | residue count |
|---|---:|
| fail at 62 | 1024 |
| fail at 64 | 256 |
| fail at 65 | 256 |
| fail at 67 | 96 |
| fail at 69 | 56 |
| fail at 70 | 76 |
| fail at 72 | 37 |
| survive through 72 | 247 |

All 247 surviving `q61=39` residues attain minimum coefficient margin `0` somewhere in depths 62..72.

These are finite exact residue counts, not probability or density claims.

MATH-010 status:

`CONFIRMED WITHIN FINITE 61+11 SCOPE / REPRESENTATION ERROR BLOCKED / NO NEW GLOBAL PRUNING`.

## Current next frontier

The `(q61,y mod2048)` + 11-bit coefficient-transducer information is now audited both arithmetically and at the representation stage. Further manipulation of the same phase/address lift is not a new observable.

The next refinement must add genuinely new same-integer information. Priority targets are:

1. couple DSD-native `first_fail_depth` / `minimum_coefficient_margin` to a depth-72+ same-integer Hensel eligibility condition;
2. seek an exact address-local invariant inside the `<2^35` adjacent-block halos;
3. test whether correction information beyond the already-audited endpoint ordering yields a non-redundant observable.

The next calculation should reject any proposed feature that is only a relabeling of information already present in MATH-004/006/009.

## Canonical current documents

- [`notes/2026-09-07-full-proof-architecture-analysis-and-status.md`](notes/2026-09-07-full-proof-architecture-analysis-and-status.md) — proof architecture/status baseline
- [`notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md`](notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md) — external literature citation ledger
- [`notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md`](notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md) — endpoint/Hensel address theorem
- [`notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md`](notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md) — MATH-008 phase reachability / route saturation
- [`notes/2026-09-08-root-hensel-endpoint-ordering-redundancy.md`](notes/2026-09-08-root-hensel-endpoint-ordering-redundancy.md) — MATH-009 redundancy result
- [`notes/2026-09-08-dsd-native-61plus11-computation-pilot.md`](notes/2026-09-08-dsd-native-61plus11-computation-pilot.md) — MATH-010 DSD-native pilot
- [`src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py`](src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py) — MATH-008 certificate
- [`src/2026_09_08_dsd_native_61plus11_computation_certificate.py`](src/2026_09_08_dsd_native_61plus11_computation_certificate.py) — MATH-010 certificate

DSD formal audits are indexed separately at:

`dominicus9708/DSD_Method_Family/DSD_Audit/audits/mathematics/README.md`.

## Directory roles

```text
collatz/
├─ README.md   # current canonical index
├─ notes/      # theorem candidates, derivations, revisions, failed/conditional routes
├─ src/        # exact/reproducible certificates and scans
├─ results/    # generated finite results
└─ wolfram/    # Wolfram-side exact/symbolic diagnostics
```

## External literature audit policy

Any new external paper needed as a calculation input is audited **before** it is used.

- `A` — positive prior art / safe within exact scope
- `B` — conditional prior art
- `C` — surviving result and failed/open hinge separated
- `D` — audited anti-pattern / negative methodological example; not proof support
- `FINITE ONLY` — finite evidence only

## Prohibited upgrades

- finite verification `⇒` universal proof
- almost all / density one / measure zero `⇒` all / emptiness
- coarse FSM reachability `⇒` inevitable ordinary-integer trajectory
- endpoint quotient and root-Hensel maximality as independent filters
- local/candidate-language endpoint q-lock `⇒` arbitrary later-block Hensel maximality
- per-phase surviving-label cap `⇒` fixed globally excluded labels
- full phase reachability at depth61 `⇒` arbitrary deeper-state reachability
- `ADDRESS_LIFTED` phase `⇒` valid input for another address lift
- DSD-native representation safety `⇒` new mathematical pruning
- route saturation `⇒` first-cell or Collatz closure

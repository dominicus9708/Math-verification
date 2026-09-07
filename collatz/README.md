# Collatz verification / current index

이 문서는 `collatz/`의 **현재 정본 진입점**입니다.

과거 계산·실패 경로·조건부 경로는 추적성을 위해 기존 파일에 그대로 보존합니다. 이 README는 그 기록을 삭제하거나 재작성하지 않고, 현재 살아 있는 증명선과 감사 상태를 가리키는 인덱스 역할만 합니다.

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

최소반례 논증의 공개 정리에는 이 값을 사용합니다.

Barina 프로젝트의 더 최근 live verification 값은 operational sensitivity로만 관리하며, published frozen baseline을 조용히 대체하지 않습니다.

## Current first universal cell

Earliest first-coefficient-crossing cell:

\[
(A_0,q_0)=(114{,}208{,}327{,}604,\;72{,}057{,}431{,}991).
\]

Current exact start window:

\[
2^{71}<N<\frac{1364}{1024}2^{71}=1364\cdot2^{61}.
\]

따라서 surviving top-11-bit address labels are

\[
a=1024,\ldots,1363,
\]

즉 **340개 block**입니다.

Denjoy–Koksma/Ostrowski bound 이후 scalar correction-only route는 block `1363`부터 더 이상 whole-block elimination을 제공하지 못합니다. 이후 계산은 same-integer address coupling을 보존해야 합니다.

## Current same-integer structure

### Endpoint q-lock across the first cell

Candidate-language universal-spine prefixes satisfy

\[
S=R/3^q\le q/3<2^{71}
\]

through the first universal crossing. Hence within the current candidate window,

\[
T^k(N_1)=T^k(N_2)\Longrightarrow q_1=q_2
\]

through that crossing.

With equal `q`,

\[
R_1-R_2=3^q(N_2-N_1),
\qquad
N_1<N_2\iff R_1>R_2.
\]

This is an address-faithful form of the same root-minimality/Hensel mechanism. **Do not count endpoint quotienting and root-Hensel maximality as independent pruning factors.**

This does **not** extend arbitrary-word full-Hensel maximality to the whole first crossing.

### 340-block locality

Same-endpoint candidate starts satisfy an integer displacement bound

\[
|N_1-N_2|\le 24{,}019{,}143{,}996<2^{35}.
\]

Each top-address block has width `2^61`, so one endpoint fiber can couple at most two adjacent blocks. Cross-block dependence is confined to thin halos around the 339 internal boundaries.

This is a locality theorem, not an emptiness or density-to-emptiness argument.

### 61+11 address transducer

Write

\[
N=a2^{61}+x,
\qquad 1024\le a\le1363.
\]

If the lower-61 state is `(q,y)`, then

\[
T^{61}(N)=y+a3^q,
\]

so the final 11 parity bits are determined by

\[
(y+a3^q)\bmod2048.
\]

For the current 340 labels, the exact pointwise surviving-label ranges are:

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
q_{61}=39\Longrightarrow \text{at most }47/340\text{ labels survive}
\]

for every endpoint residue. This is an exact pointwise cap, not a probability statement.

### Right-congruence barrier

Number of distinct exact 340-label survival masks as `y mod 2048` varies:

| `q61` | distinct masks |
|---:|---:|
| 39–43 | 2048 |
| 44 | 1838 |
| 45 | 341 |
| 46–61 | 1 |

Thus in the strongest low-surplus range `q61=39..43`, the endpoint phase `y mod 2048` cannot be discarded by a nontrivial exact coarse quotient.

### Lower-61 endpoint-phase reachability saturation

The actual universal-spine candidate language has exact reachable-phase cardinalities

\[
\#\operatorname{Reach}_{61}(q)=
\begin{cases}
2048,&39\le q\le58,\\
1166,&q=59,\\
58,&q=60,\\
1,&q=61.
\end{cases}
\]

For `q61=39,...,58`, every phase has an explicit ordinary-integer witness. For `q61=59,60,61`, the valid parity-word languages were exhaustively enumerated.

This closes the proposed reachable-phase refinement of MATH-006/007 as **SATURATED**. In every range where the coefficient-only 11-bit sieve actually rejects labels (`q61=39,...,45`), all 2048 phases occur in the real candidate language. Therefore reachability sparsity cannot turn the pointwise masks into a fixed global block exclusion.

The restricted high-`q` phase sets do not help this sieve because `q61>=46` already has the trivial all-340-survive coefficient mask through depth72.

## Current next frontier

The 61+11 coefficient-only phase route is now audited to saturation. The next refinement must add a **new same-integer observable**, rather than further coarsening or restricting `(q61,y mod2048)`.

Priority targets:

1. correction/address order information within one endpoint phase;
2. endpoint/Hensel eligibility beyond depth72 while preserving the audited non-independence rule;
3. an exact address-local invariant inside the `<2^35` adjacent-block halos.

The next calculation should test the cheapest of these refinements for exact deterministic pruning before a deeper state space is adopted.

## Canonical current documents

- [`notes/2026-09-07-full-proof-architecture-analysis-and-status.md`](notes/2026-09-07-full-proof-architecture-analysis-and-status.md) — proof architecture/status baseline
- [`notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md`](notes/2026-09-07-external-literature-complete-audit-and-citation-ledger.md) — external literature citation ledger
- [`notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md`](notes/2026-09-07-first-cell-endpoint-q-lock-and-hensel-equivalence.md) — endpoint/Hensel address theorem
- [`notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md`](notes/2026-09-08-lower61-endpoint-phase-reachability-and-route-saturation.md) — current phase-reachability result and route saturation
- [`src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py`](src/2026_09_08_lower61_endpoint_phase_reachability_certificate.py) — exact constructive/exhaustive MATH-008 certificate

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

Historical notes are not automatically current merely because they remain in `notes/`. Prefer this README and the latest canonical status/audit documents when resolving conflicts.

## External literature audit policy

Any new external paper needed as a calculation input is audited **before** it is used.

- `A` — positive prior art / safe within exact scope
- `B` — conditional prior art
- `C` — surviving result and failed/open hinge separated
- `D` — audited anti-pattern / negative methodological example; not proof support
- `FINITE ONLY` — finite evidence only

Failed proof mechanisms remain citable as methodological counterexamples:

```text
claim
→ exact failure locus
→ prohibited transition
→ information retained by the current architecture
```

## Prohibited upgrades

- finite verification `⇒` universal proof
- almost all / density one / measure zero `⇒` all / emptiness
- coarse FSM reachability `⇒` inevitable ordinary-integer trajectory
- endpoint quotient and root-Hensel maximality as independent filters
- local/candidate-language endpoint q-lock `⇒` arbitrary later-block Hensel maximality
- per-phase surviving-label cap `⇒` fixed globally excluded labels
- full phase reachability at depth61 `⇒` arbitrary deeper-state reachability
- route saturation `⇒` first-cell or Collatz closure

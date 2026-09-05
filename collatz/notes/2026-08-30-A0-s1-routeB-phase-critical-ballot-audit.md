# A0 s=1 Route-B phase-critical ballot audit — 2026-08-30

## Result

The previously open problem “a ballot summary depends on the absolute threshold phase `h`, so does a reused Christoffel node require a separate `(node,h)` state for every occurrence?” is resolved negatively.

A raw absolute phase is **not** needed inside the node state.

For every finite parity block `B`, its complete lower-ballot response to every placement `h` is determined by two intrinsic ballot coordinates, in addition to length/odd-count metadata:

\[
S_{\rm bal}(B)=(m_B,a_B).
\]

Here

\[
\alpha=\log_3 2,\qquad F(n)=\lfloor n\alpha\rfloor,
\]

\[
d_B(u)=Q_B(u)-F(u),\qquad
m_B=\min_{0\le u\le |B|} d_B(u),
\]

and `a_B` is the positive prefix attaining `m_B` whose fractional phase

\[
\{u\alpha\}
\]

is maximal.  If no positive prefix attains `m_B`, `a_B` is absent.

This is exact, not an empirical finite-state guess.

## 1. Exact phase formula

For `n>0`, irrationality of `alpha` gives

\[
REQ(n)=F(n)+1.
\]

Therefore for `h>=1`,

\[
REQ(h+u)-REQ(h)=F(h+u)-F(h).
\]

Define the floor carry

\[
\kappa(h,u)=F(h+u)-F(h)-F(u)\in\{0,1\}.
\]

Then

\[
\mu_h(B)
=\min_u\left(d_B(u)-\kappa(h,u)\right).
\]

Every prefix with `d_B(u)>=m_B+1` remains at least `m_B` after subtracting a carry of at most one.  Hence the minimum can only be `m_B` or `m_B-1`, and it falls to `m_B-1` exactly when a prefix attaining the base minimum carries.

Because

\[
\kappa(h,u)=1
\iff
\{h\alpha\}+\{u\alpha\}\ge1,
\]

it is enough to retain the minimum prefix with the largest fractional phase.  Thus

\[
\boxed{
\mu_h(B)=m_B-\kappa(h,a_B),\qquad h\ge1,
}
\]

with the carry term omitted when `a_B` is absent.

At `h=0`,

\[
\boxed{
\mu_0(B)=
\begin{cases}
m_B-1,&a_B\text{ exists},\\
0,&a_B\text{ absent}.
\end{cases}
}
\]

So the infinitely many possible absolute phases are handled parametrically rather than stored as distinct node states.

## 2. Exact two-block composition

Let `B=UV` and

\[
e_U=q(U)-F(|U|).
\]

For a prefix entering `V`,

\[
d_{UV}(|U|+v)
=e_U+d_V(v)-\kappa(|U|,v).
\]

Therefore the right-side minimum is

\[
r=e_U+m_V-\kappa(|U|,a_V),
\]

again with the carry omitted when `a_V` is absent, and

\[
\boxed{m_{UV}=\min(m_U,r).}
\]

The critical prefix of the parent is obtained by comparing at most two candidates:

- the left critical prefix `a_U` if the left side attains `m_{UV}`;
- the shifted right critical prefix `|U|+a_V` if the right side attains `m_{UV}`;
- if `a_V` is absent, the right candidate is the boundary `|U|` itself.

The candidate with larger fractional phase `{u alpha}` becomes `a_{UV}`.

Fractional-phase ordering is performed exactly using `F`, not floating point.  For `a>b`,

\[
\{a\alpha\}>\{b\alpha\}
\iff
F(a)-F(b)\le F(a-b).
\]

## 3. Exact arithmetic certification

The certificate uses the same rigorous rational logarithm bounds already used by the Route-B Christoffel real-envelope certificate:

- `ln 2 = 2 atanh(1/3)`,
- `ln 3 = 2 atanh(1/2)`,
- positive geometric tail bounds,
- rational lower/upper bounds for `alpha=ln2/ln3`.

Every queried `floor(n alpha)` is accepted only when the rational lower and upper bounds have the same floor.

No floating-point value participates in an assertion.

## 4. Regression results

### Arbitrary words

All binary words through length 11 were summarized directly.

- split/composition checks: `36,868`;
- placement/phase checks: `33,726`;
- mismatches: `0`.

### Existing 129-node Christoffel DAG

- DAG nodes: `129`;
- parent compositions: `127`;
- direct materialized-node summary checks: `45`;
- additional direct phase-response checks: `1,628`;
- mismatches: `0`.

For the base block `L`,

\[
\boxed{
S_{\rm bal}(L)
=(|L|,q(L),m_L,a_L)
=(10{,}439{,}860{,}591,
6{,}586{,}818{,}670,
0,
9{,}809{,}721{,}694).
}
\]

Examples:

\[
\mu_0(L)=-1,\qquad
\mu_1(L)=-1,\qquad
\mu_{J_0}(L)=0.
\]

## 5. Formation Axiom System audit

The Formation Axiom System is used here only as a structural audit lens; it does not establish the Collatz identity.

The parent ballot-response state is formed entirely from

- the left child summary,
- the right child summary,
- the explicit concatenation boundary `|U|`.

No hidden materialized word and no unrecorded absolute phase are required.

Result:

- ✅ child-to-parent formation is explicit;
- ✅ boundary dependence is explicit;
- ✅ no undefined hidden coordinate is used in the composition rule.

## 6. Axis-property audit

The previous `(node,h)` attempt treated absolute placement as though it were an intrinsic node axis.  That would expand one `L` block to `20,879,721,181` parse-tree placements.

The new summary separates the roles:

- intrinsic block axes/metadata: `length`, `ones`;
- intrinsic ballot-response coordinates: `m`, `critical_prefix`;
- external evaluation coordinate: `h`.

Thus `h` is supplied only when evaluating a node, rather than copied into every node occurrence.

Result:

- ✅ raw phase is removed from the intrinsic state;
- ✅ the phase dependence survives exactly through one critical-prefix coordinate;
- ✅ the 129-node DAG compression is preserved.

## 7. Combined Route-B block state

Together with the previously closed modular correction state, a useful exact jump state at dyadic resolution `K` is now

\[
\boxed{
S_K(B)=
\bigl(
|B|,q(B),C(B)\bmod2^K,m_B,a_B
\bigr).
}
\]

The two arithmetic sectors compose independently but share the same block concatenation:

- correction sector: affine/dyadic composition;
- ballot sector: minimum-plus-carry composition.

This closes the main G2 compositional-state problem without materializing the gigantic Christoffel word.

## 8. Updated DSD status

### Closed

- ✅ exact correction state reduction `(h,r,y,q) -> (h,q,C)`;
- ✅ exact correction block composition;
- ✅ exact modular correction jump on all 129 Christoffel nodes;
- ✅ exact phase-sensitive ballot criterion;
- ✅ exact phase-critical compression `(m,a)`;
- ✅ exact two-block ballot-summary composition;
- ✅ direct arbitrary-word and materialized-DAG regressions;
- ✅ naive absolute-phase state explosion avoided.

### Open

- ❌ proof that target-relevant states have a finite right-congruence quotient;
- ❌ full target-aware `match_and_jump` decoder for arbitrary long candidates;
- ❌ universal Route-B correction-language membership verdict;
- ❌ Collatz conjecture proof.

The correct next step is G3/G4: use the combined state to perform target-aware recursive discrimination and determine whether the target decoder closes recursively without introducing a new unbounded coordinate.

## Reproducibility

Certificate:

`collatz/src/A0_s1_routeB_phase_critical_ballot_certificate.py`

Expected headline output:

```text
PASS A0 s=1 Route-B exact phase-critical ballot certificate
arbitrary_word_max_depth 11
arbitrary_word_composition_checks 36868
arbitrary_word_phase_checks 33726
dag_nodes 129
dag_parent_composition_checks 127
materialized_nodes 45
materialized_direct_summary_checks 45
dag_phase_response_checks 1628
root_length 10439860591
root_ones 6586818670
root_base_min 0
root_critical_prefix 9809721694
root_mu_h0 -1
root_mu_h1 -1
root_mu_hJ0 0
status EXACT parametric ballot phase compression CLOSED; universal membership remains OPEN
```

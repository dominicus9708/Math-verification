# A0 s=1 Route-B Christoffel run-hierarchy audit — 2026-08-30

## Result

The previous two-sided residue audit established two facts:

1. fixed dyadic/ternary boundary projections are exact recursive invariants;
2. at the Route-B exposure depths they do not separate the large Christoffel nodes.

The next G3 calculation shows that this is not a dead end.  The missing coordinate is naturally the **Stern-Brocot/continued-fraction hierarchy**.

For the present threshold slope, 126 one-step Stern-Brocot decisions compress to only 20 alternating runs.  The already-certified exact correction+ballot state can be propagated over those runs by block powering, and the resulting root state is exactly the same as the state obtained from the full 129-node DAG.

At the same time, the final Christoffel run gives a sharp lower bound showing why a fixed boundary resolution cannot replace this hierarchy.

## 1. Continued-fraction address

For

\[
\frac{R_0}{J_0}
=
\frac{6{,}586{,}818{,}670}{10{,}439{,}860{,}591},
\]

the exact continued fraction is

\[
[0;
1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,16].
\]

There are 22 coefficients in this convention.

The corresponding 126 nonterminal Stern-Brocot decisions have only 20 alternating runs:

```text
L^1 R^1 L^2 R^2 L^3 R^1 L^5 R^2 L^23 R^2
L^2 R^1 L^1 R^55 L^1 R^4 L^3 R^1 L^1 R^15
```

The final exact mediant supplies the last unit corresponding to the terminal continued-fraction coefficient `16`.

Thus the hierarchy is much smaller than either

- the `10,439,860,591`-bit word itself, or
- a raw absolute-position state, or
- the 127 one-mediant-at-a-time internal nodes.

## 2. Exact run-level state propagation

At dyadic correction resolution `K=128`, use the combined state

\[
S(B)=
\bigl(
|B|,
q(B),
C(B)\bmod2^{128},
m_B,
a_B
\bigr).
\]

Both previously certified sectors are associative under concatenation:

- correction sector: affine composition;
- ballot sector: phase-critical min/carry composition.

Therefore repeated copies of one block can be evaluated by exact block powering.

For a repeated Stern-Brocot direction:

- a left-bound run updates `left -> left · right^n`;
- a right-bound run updates `right -> left^n · right`.

The certificate compares the run-compressed state after every one of the 20 run endpoints with the corresponding state in the full 129-node DAG.

Results:

- run endpoint comparisons: `20`;
- mismatches: `0`;
- block-power internal compositions: `36`;
- final root state: exact match.

The reconstructed root is

\[
|L|=10{,}439{,}860{,}591,
\]

\[
q(L)=6{,}586{,}818{,}670,
\]

\[
C(L)\bmod2^{128}
=236625333412151970821400857998262175134,
\]

\[
m_L=0,
\qquad
a_L=9{,}809{,}721{,}694.
\]

This establishes **recursive run-level generation** of the current Christoffel state without materializing the word.

## 3. Exact compressed LCP calculation

To measure the boundary resolution required to distinguish neighboring hierarchy states, the certificate includes an exact longest-common-prefix calculation directly on the straight-line grammar.

It never expands the giant nodes.  Equal reused DAG nodes are skipped by their exact stored lengths; differing nodes are recursively split only as needed.

The compressed LCP algorithm was independently compared with direct bit materialization for every ordered pair among the 45 DAG nodes of length at most `100,000`:

- regression comparisons: `2,025`;
- mismatches: `0`.

## 4. Final Christoffel ray

Let

- `A = node 112`,
- `B = node 111`.

Their exact metadata are

\[
|A|=630{,}138{,}897,
\qquad q(A)=397{,}573{,}379,
\]

\[
|B|=357{,}638{,}239,
\qquad q(B)=225{,}644{,}606.
\]

They are Farey neighbors:

\[
q(A)\,|B|-q(B)\,|A|=-1.
\]

The final sixteen nodes have the exact formation

\[
\boxed{W_n=A^nB,\qquad 1\le n\le16.}
\]

In particular,

\[
W_{16}=L,
\qquad
W_{15}=\text{node 127}.
\]

The base words satisfy

\[
\operatorname{LCP}(A,B)=|B|-1
=357{,}638{,}238.
\]

Hence, since

\[
W_n=A W_{n-1},
\]

one obtains recursively

\[
\boxed{
\operatorname{LCP}(W_n,W_{n-1})
=|W_{n-1}|-1.
}
\]

All 16 instances in the actual final run were checked exactly on the compressed grammar.

## 5. Linear source-resolution obstruction

For root versus its predecessor,

\[
|W_{15}|=9{,}809{,}721{,}694,
\]

and

\[
\operatorname{LCP}(W_{16},W_{15})
=9{,}809{,}721{,}693.
\]

Therefore their canonical source cylinders are identical for every

\[
K<9{,}809{,}721{,}694,
\]

and the first possible dyadic distinction occurs only at

\[
\boxed{K=9{,}809{,}721{,}694.}
\]

This is not merely “large”; it grows linearly with the shorter Christoffel block on this ray.

Consequently a constant source-resolution quotient cannot distinguish the ray as its run exponent grows.

## 6. Endpoint obstruction is even stronger

Because

\[
W_n=A W_{n-1},
\]

`W_{n-1}` is an exact suffix of `W_n`.

The exact rear-screening identity therefore gives

\[
y_R(W_n)=y_R(W_{n-1})
\]

for every endpoint resolution available to the shorter block:

\[
R\le q(W_{n-1}).
\]

For the root/predecessor pair this means equality through

\[
\boxed{R=6{,}189{,}245{,}291.}
\]

Thus increasing only the terminal ternary resolution does not separate this nested suffix pair at all within the shorter block's full odd-count depth.

## 7. Ballot critical prefix meets hierarchy

A notable independent consistency appears in the phase-critical ballot state.

For every actual final-run node `W_n`, `1<=n<=16`, the already-derived ballot critical prefix satisfies

\[
\boxed{a_{W_n}=|W_{n-1}|.}
\]

All 16 identities were verified by the exact ballot composition state.

For the root,

\[
a_L
=9{,}809{,}721{,}694
=|W_{15}|
=\operatorname{LCP}(W_{16},W_{15})+1.
\]

So the ballot critical-prefix coordinate is not merely a legality statistic on this run: it points exactly to the hierarchy scale at which the root first separates from its immediate predecessor on the source side.

This does not yet prove that `a_B` is a complete decoder coordinate for arbitrary Christoffel blocks, but it makes it a particularly relevant G4 checkpoint.

## 8. Formation Axiom System audit

The previous fixed-boundary candidate failed because equal projections did not determine equal formation.

The run hierarchy repairs that specific defect:

- each run explicitly records which boundary block is repeated;
- the integer exponent records how many formations occur in that run;
- block powering reconstructs the exact child-to-parent state;
- all 20 run endpoints agree with the original DAG.

Therefore:

- ✅ the hierarchy preserves formation information lost by the fixed boundary quotient;
- ✅ repeated formation is represented recursively rather than by billions of positions;
- ❌ this alone does not establish target-language membership or right-congruence sufficiency.

## 9. Axis-property audit

The calculations separate three roles:

1. dyadic source boundary axis;
2. ternary endpoint boundary axis;
3. hierarchical scale/run axis.

The first two are exact but non-separating at fixed resolution.  The third distinguishes formation compactly.

The final run demonstrates why raw resolution is the wrong coordinate:

\[
K_{\rm distinguish}\sim |W_{n-1}|,
\]

while the same structural change is described by the small run counter

\[
n\mapsto n+1.
\]

Thus the hierarchy/run exponent is a better structural coordinate than copying an absolute bit position into the state.

## 10. Updated G3/G4 status

### Closed / established

- ✅ fixed low-resolution boundary state is insufficient;
- ✅ one internal fixed-resolution CRT cut is insufficient;
- ✅ the present Christoffel word has an exact continued-fraction/run hierarchy;
- ✅ the complete correction+ballot block state propagates through that hierarchy;
- ✅ 20 run endpoints reconstruct the exact 129-node DAG state;
- ✅ final-ray boundary resolution must grow linearly;
- ✅ ballot critical prefix coincides with the exact final-ray separating cut.

### Interpretation

G3 should no longer be phrased as “find a small fixed set of boundary residues.”

The surviving formulation is:

> determine whether the target-relevant language is recursively closed under a hierarchy-aware state whose unbounded information is carried by compact run/continued-fraction coordinates.

This is weaker than a finite-state quotient but still compatible with the original G3 alternative “finite **or recursive** closure.”

### Open

- ❌ proof that the hierarchy-aware state is sufficient for all future target continuations;
- ❌ target-aware lazy `match_and_jump` using the run hierarchy;
- ❌ Route-B universal membership verdict;
- ❌ Collatz conjecture proof.

## 11. Next G4 calculation

The next decoder should descend at **hierarchical critical cuts**, not at fixed bit/trit depths.

For the current root, the first natural cut is already supplied by

\[
a_L=|W_{15}|.
\]

At a generic hierarchy node, the decoder should therefore test whether the stored ballot critical prefix identifies one of the two run/DAG child boundaries.  If it does, target matching can jump directly to that child boundary.  If not, the critical prefix can be recursively located inside one child without expanding the word.

This is the next concrete G4 gate.

## Reproducibility

Certificate:

`collatz/src/A0_s1_routeB_christoffel_run_hierarchy_certificate.py`

Expected headline output:

```text
PASS A0 s=1 Route-B Christoffel run-hierarchy certificate
continued_fraction_terms 22
stern_brocot_one_step_decisions 126
run_groups 20
run_endpoint_state_checks 20
state_power_compositions 36
root_length 10439860591
root_ones 6586818670
root_ballot_base_min 0
root_ballot_critical_prefix 9809721694
lcp_materialized_regression_checks 2025
final_ray_pair_checks 16
final_ray_ballot_checks 16
root_predecessor_length 9809721694
root_predecessor_ones 6189245291
root_predecessor_lcp 9809721693
first_distinguishing_dyadic_K 9809721694
endpoint_indistinguishable_through_R 6189245291
status FIXED boundary quotient REJECTED on final ray; recursive run hierarchy CLOSED for current target; universal membership OPEN
```

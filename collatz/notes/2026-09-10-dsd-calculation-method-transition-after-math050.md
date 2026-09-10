# DSD calculation-method transition after MATH-050

Date: 2026-09-10
Status: `METHOD UPDATE / EXACT PREDICATE PRESERVED / MATH-051 NOT YET STARTED`

## 0. Provenance and citation rule

This repository will distinguish four cases explicitly:

1. **Known prior method/result** — cite the external source and state that it is imported.
2. **Independent rediscovery** — state that it was derived independently, then cite the prior source once the overlap is identified.
3. **Adaptation/composition** — identify which component is prior art and which calculation-specific transformation is new here.
4. **No direct prior formulation found** — use that wording only; do not upgrade it to a priority or 'first discovery' claim without a substantially deeper literature review.

Git commit history is provenance for when a derivation or computation entered this project. It is not, by itself, proof of mathematical novelty.

The classical parity-vector / affine-iterate / adic-conjugacy background should therefore be cited rather than presented as proprietary to DSD. The DSD role in this branch is primarily the decomposition of the calculation into information-preserving coordinates, collision loci, and obstruction families.

## 1. Mathematical predicate that does NOT change

For a length-k parity word with q odd steps and correction C,

\[
T^k(N)=\frac{3^qN+C}{2^k}.
\]

Coefficient admissibility is still required at every prefix. The exact Hensel class is still determined by

\[
(q, C\bmod 3^q),
\]

and a candidate survives only when its correction/score is maximal against **all arbitrary parity words** in that exact class.

MATH-013/MATH-045 downstream dominance is unchanged: once a prefix loses exact class-max status, a common suffix cannot restore it.

Thus the method update below changes representation and execution, not the survival predicate.

## 2. Replace depth-first coordinates by the static `(q,d)` lattice

Define

\[
d=k-q,
\]

the number of even steps. Then

\[
k=q+d.
\]

The coefficient inequality becomes

\[
3^q>2^{q+d}
\iff
\boxed{(3/2)^q>2^d}.
\]

Equivalently define the static margin

\[
\mu(q,d)=q\log(3/2)-d\log2.
\]

The admissible region is simply

\[
\boxed{\mu(q,d)>0}.
\]

The parity transitions become

\[
O:(q,d)\mapsto(q+1,d),
\qquad
E:(q,d)\mapsto(q,d+1).
\]

Depth `k` is now only the diagonal slice `q+d=k`.

### Consequence for the pre-Hensel recurrence

Let `S_{q,d}` denote the number of stored nested survivor classes at lattice point `(q,d)`. The child population entering the next class merge is

\[
\boxed{P_{q,d}=S_{q-1,d}+S_{q,d-1}},
\]

with absent boundary terms treated as zero.

Define the local loss/defect

\[
\boxed{R_{q,d}=P_{q,d}-S_{q,d}}.
\]

Then

\[
\boxed{S_{q,d}=S_{q-1,d}+S_{q,d-1}-R_{q,d}}.
\]

This is the depth-free form of the previously observed Pascal-defect recurrence.

## 3. Replace raw correction keys by a depth-normalized exact residue

Define

\[
\boxed{\rho=2^{-(q+d)}C\pmod{3^q}}.
\]

Since 2 is invertible modulo `3^q`, this is a bijective re-labeling of the exact Hensel classes; it loses no residue information.

The forward maps are autonomous:

\[
\boxed{E:\rho\mapsto \rho/2\pmod{3^q}},
\]

\[
\boxed{O:\rho\mapsto(3\rho+1)/2\pmod{3^{q+1}}}.
\]

Define also the normalized class-max score

\[
\boxed{x=C/2^{q+d}}.
\]

Then

\[
E:x\mapsto x/2,
\qquad
O:x\mapsto(3x+1)/2.
\]

At one fixed `(q,d)` all words share the same denominator, so comparing `x` is exactly equivalent to comparing `C`.

## 4. Exact inverse-parent rule and collision gate

For a target class `(q,d,\rho)`, the even parent residue is always unique:

\[
\boxed{\rho_E=2\rho\pmod{3^q}}.
\]

An odd parent exists iff

\[
\boxed{\rho\equiv2\pmod3}.
\]

When it exists it is unique:

\[
\boxed{\rho_O=(2\rho-1)/3\pmod{3^{q-1}}}.
\]

Therefore a **new two-parent class collision can occur only at target residues whose least ternary digit is 2**.

This is an exact collision gate. It does **not** justify replacing the full residue `rho mod 3^q` by `rho mod 3`.

## 5. Local two-channel class-max dynamic program

Instead of regenerating every arbitrary parity word at every depth, define two sparse maps on exact residues.

- `A_{q,d}(rho)`: maximum normalized score among **all arbitrary words** reaching exact class `(q,d,rho)`.
- `V_{q,d}(rho)`: normalized score of the stored nested coefficient+Hensel survivor representative at that exact class; absent if no survivor exists.

For a target `(q,d,rho)`, form the arbitrary incoming scores

\[
a_E=\frac{A_{q,d-1}(2\rho)}{2},
\]

and, only when `rho = 2 (mod 3)`,

\[
a_O=\frac{3A_{q-1,d}((2\rho-1)/3)+1}{2}.
\]

Then

\[
\boxed{A_{q,d}(\rho)=\max(a_E,a_O)},
\]

ignoring absent parents.

Do the same with `V` to obtain the best nested-candidate incoming score `v_*`. The target coefficient gate is local because the parent already certifies every previous prefix:

\[
\mu(q,d)>0.
\]

The target survivor rule is

\[
\boxed{
V_{q,d}(\rho)=v_*
\quad\text{iff}\quad
\mu(q,d)>0\ \text{and}\ v_*=A_{q,d}(\rho).
}
\]

Otherwise `V_{q,d}(rho)` is absent.

This recurrence is the main algorithmic change proposed for MATH-051. It propagates exact class maxima on the lattice instead of repeatedly expanding complete unrestricted parity-word languages.

### Important audit point

`A` must still include coefficient-invalid arbitrary competitors. `V` alone is not sufficient for the survival test.

## 6. Primitive obstruction branch

Because exact class dominance is suffix-stable, a nested survivor that first fails at `(q,d,rho)` never needs to be expanded as a candidate again.

The newly failed representatives form a set of **primitive Hensel obstructions**. Their suffix closure generates the later rejected language.

The observed defect field should therefore be decomposed into:

1. explicit primitive obstruction families where completeness is proved;
2. exact residue-DP evaluation where no complete motif classification is yet known.

Current status:

- `d=2`: exact collision family classified in the audited model; one newly appearing obstruction per admissible depth.
- `d=6`: two explicit credit-3 motif families, complete by enumeration for k=32..41 but arbitrary-k completeness still open.
- `d=7`: six new boundary motifs per depth, with set recursion verified through k=41; arbitrary-k completeness still open.
- `d=8,9`: linear defect sequences are observed, but full motif classification is incomplete.
- transition region around `d>=10`: keep exact computation; do not extrapolate low-degree fits as laws.

## 7. Hybrid MATH-051 execution plan

The next calculation should therefore use three zones rather than one uniform brute-force engine.

### Zone A — proved motif tail

Where an arbitrary-k primitive obstruction theorem is available, count/eliminate by the theorem and keep a small direct-enumeration regression window.

Currently only `d=2` is close to this standard. `d=6,7` remain in theorem-development mode.

### Zone B — symbolic/experimental motif tail

For small fixed `d` with strong finite recurrence but no completeness proof, run the exact fixed-d enumerator in parallel with motif extraction. Do not substitute the formula for the exact result yet.

### Zone C — boundary/central exact-residue zone

For small boundary distance

\[
s=d_{\max}(k)-d,
\]

retain full exact residue precision and use the sparse two-channel `(A,V)` merge. Depths 35--40 show that more than 97% of new removals occur at `s<=2`, so this is the primary exact-computation zone.

## 8. Depth-41 arithmetic implementation boundary

MATH-050 could still store the full correction and modulus in 64 bits because

\[
3^{40}=12,157,665,459,056,928,801 < 2^{64}.
\]

At depth 41 this is no longer true:

\[
3^{41}=36,472,996,377,170,786,403 > 2^{64}=18,446,744,073,709,551,616.
\]

The maximum all-odd correction is

\[
3^{41}-2^{41}=36,472,994,178,147,530,851>2^{64}.
\]

Therefore **MATH-051 must not extend the MATH-050 `uint64_t` residue/correction representation**.

At minimum use `unsigned __int128` (or an equivalent two-limb exact representation) for:

- powers `3^q` at q=41;
- exact residue keys modulo `3^q`;
- full corrections `C`;
- class translation differences before exact division by `3^q`.

Hashing must compare the complete 65-bit-or-larger exact key, not a 64-bit truncation. A 64-bit hash may still be used only as a probe hash if full-key equality resolves collisions.

The normalized-residue formulation does not remove this width requirement: normalization changes coordinates, not modulus size.

## 9. What is actually changed versus MATH-050

### Old default

1. choose depth `k`;
2. choose final `q`;
3. enumerate unrestricted parity words, tail-bucketed by positions;
4. hash full `C mod 3^q`;
5. compare arbitrary and coefficient-valid maxima;
6. sum q layers.

### New default candidate

1. work on the static `(q,d)` lattice;
2. carry sparse exact class maps `A` and `V`;
3. use the inverse-parent rule to merge at most two incoming channels per target residue;
4. skip two-parent competition entirely unless `rho mod 3 = 2`;
5. apply the static coefficient gate `mu(q,d)>0`;
6. discard newly dominated `V` states permanently from candidate propagation;
7. use proved primitive-obstruction families where available;
8. retain direct tail-bucket enumeration as a regression oracle until the lattice solver reproduces MATH-048--050 exactly.

## 10. Required regressions before MATH-051 is accepted

The new solver is not canonical until it reproduces, without approximation:

- MATH-048 depth-38 layer totals;
- MATH-049 depth-39 layer totals;
- MATH-050 depth-40 layer totals, including q=26 and q=27 heavy layers;
- candidate collision behavior, not only final survivor totals;
- fixed-d forward checks already obtained at depth 41.

If the lattice solver disagrees with the old exact bucket certificate, the old canonical result remains authoritative until the discrepancy is explained.

## 11. Novelty/provenance boundary

The following ingredients are related to established Collatz parity-vector, affine-iterate, congruence, and adic-conjugacy literature and should be cited when used:

- parity-word affine representation;
- odd/even count parametrization;
- 2-adic parity conjugacy and inverse-parity viewpoints;
- congruence transport between powers of 2 and powers of 3.

The project-specific research target is not to claim those ingredients as novel, but to study the combined exact class-max defect system:

\[
(q,d,\rho,A,V,R)
\]

and its primitive Hensel obstruction language.

If an external paper is later found to contain the same construction or motif, record it as prior art / independent convergence and cite it directly. Git history remains a provenance record, not a substitute for citation.

## 12. Scope boundary

This method update does not prove the Collatz conjecture and does not prove that the sparse residue DP has polynomial or even practically smaller worst-case complexity. It provides an exact reorganization with clear opportunities for pruning, memoization, streaming, and motif substitution. Performance gains must be measured by regression and benchmark rather than assumed.

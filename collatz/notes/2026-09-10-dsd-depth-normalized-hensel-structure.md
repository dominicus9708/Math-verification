# DSD structural checkpoint — depth-normalized Hensel dynamics and fixed-even-budget defect field

Date: 2026-09-10
Status: `CONFIRMED EXACT REPARAMETRIZATION / FINITE PATTERN EXTRACTION / GENERAL LAW OPEN`

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- MATH-050 remains the latest completed full depth audit.
- This note is a structural side analysis before MATH-051, not a new proof-depth claim.

## 1. Why revisit the calculation with DSD

Depths 32--40 now provide a long exact one-sided root-Hensel ledger.  Recent work used DSD mainly as an audit boundary and safe partitioning discipline.  The accumulated exact data are now sufficient to ask a different question: can the calculation itself be re-described in coordinates that expose invariant structure and reduce future work?

The answer is partly yes.  Two exact coordinate changes remove much of the artificial depth dependence, and the remaining pruning can be organized as a sparse defect field on a fixed `(q,d)` lattice.

## 2. `(q,d)` lattice: depth is a diagonal, not a fundamental state variable

For a length-k parity prefix let

\[
q=\#\{\text{odd steps}\},\qquad d=k-q=\#\{\text{even steps}\}.
\]

Then

\[
k=q+d.
\]

The coefficient admissibility condition at every prefix is

\[
3^q>2^k.
\]

Using `k=q+d`, this is exactly

\[
\boxed{(3/2)^q>2^d}.
\]

Equivalently, with logarithmic margin

\[
\mu(q,d)=q\log(3/2)-d\log2,
\]

coefficient admissibility is the fixed half-lattice condition

\[
\boxed{\mu(q,d)>0}.
\]

Thus the moving threshold seen in `(k,q)` coordinates is a coordinate artifact.  In `(q,d)` coordinates the admissible region is static.

The two parity transitions are simply

\[
\text{odd}: (q,d)\mapsto(q+1,d),
\]

\[
\text{even}: (q,d)\mapsto(q,d+1).
\]

Depth-k computations are diagonal slices `q+d=k` through this fixed lattice.

For comparison with the historical depth notation,

\[
q_{\min}(k)=\lceil k\log_3 2\rceil,
\]

\[
d_{\max}(k)=k-q_{\min}(k)=\lfloor k\log_3(3/2)\rfloor,
\]

and the boundary-distance coordinate is

\[
\boxed{s=q-q_{\min}(k)=d_{\max}(k)-d}.
\]

## 3. Exact Pascal-defect recurrence

Let `S_{k,d}` be the number of nested coefficient+Hensel survivors at depth k with exactly d even steps.

A depth-k word with d evens has exactly two possible parent types:

1. last bit odd: parent `(k-1,d)`;
2. last bit even: parent `(k-1,d-1)`.

Therefore the exact pre-Hensel population in that layer is

\[
\boxed{P_{k,d}=S_{k-1,d}+S_{k-1,d-1}},
\]

with out-of-domain/boundary terms interpreted as zero.

Define the current-depth Hensel loss/defect

\[
\boxed{R_{k,d}=P_{k,d}-S_{k,d}}.
\]

Then

\[
\boxed{S_{k,d}=S_{k-1,d}+S_{k-1,d-1}-R_{k,d}}.
\]

This is an exact Pascal-type growth law with a sparse Hensel defect field `R`.

The large depth-by-depth ledgers are therefore better viewed as measurements of `R_{k,d}`, rather than as unrelated q-layer enumerations.

## 4. Depth-normalized exact Hensel residue

The correction satisfies

\[
T^k(N)=\frac{3^qN+C_k}{2^k}.
\]

The historical exact Hensel class key is

\[
(q,\ C_k\bmod3^q).
\]

Since 2 is invertible modulo every power of 3, define the normalized residue

\[
\boxed{\rho_k\equiv2^{-k}C_k\pmod{3^q}}.
\]

Multiplication by `2^{-k}` is a bijection modulo `3^q`, so this loses no class information:

\[
C_1\equiv C_2\pmod{3^q}
\iff
\rho_1\equiv\rho_2\pmod{3^q}.
\]

The important gain is that the explicit depth term disappears from the transitions.

For an even next bit,

\[
C_{k+1}=C_k,
\]

so

\[
\boxed{\rho_{k+1}\equiv\rho_k/2\pmod{3^q}}.
\]

For an odd next bit,

\[
C_{k+1}=3C_k+2^k,
\]

and therefore

\[
\boxed{\rho_{k+1}\equiv(3\rho_k+1)/2\pmod{3^{q+1}}}.
\]

These maps contain no explicit k.

This is an exact reparametrization, not a coarse quotient.  The full `3^q` residue precision remains present.

## 5. Depth-normalized score and autonomous class-max dynamics

At fixed depth, maximizing `C_k` is equivalent to maximizing

\[
\boxed{x_k=C_k/2^k},
\]

because `2^k>0` is common to the layer.

The score evolves by the same affine maps:

\[
\text{even}: x\mapsto x/2,
\]

\[
\text{odd}: x\mapsto(3x+1)/2.
\]

Both maps are strictly increasing.  Thus class dominance is preserved under a common suffix, reproducing the MATH-013/MATH-045 downstream-stable class-max rule in depth-normalized coordinates.

An exact state may therefore be written schematically as

\[
\boxed{(q,d,\rho,x)},
\]

with the coefficient gate `mu(q,d)>0` and exact `3^q` residue precision.

Absolute depth k is redundant because `k=q+d`.

## 6. Exact two-channel merge structure

At lattice point `(q,d)`, an exact class can be reached from only two channel types:

- odd image of a class at `(q-1,d)`;
- even image of a class at `(q,d-1)`.

The odd residue map is injective from modulo `3^(q-1)` classes into modulo `3^q` classes, and the even residue map is bijective modulo `3^q`.

Therefore new class collisions arise only where the odd and even images meet.  In normalized coordinates the collision condition is

\[
\boxed{\rho_E\equiv3\rho_O+1\pmod{3^q}}.
\]

At such a collision the child scores are

\[
x_O'=(3x_O+1)/2,
\qquad
x_E'=x_E/2,
\]

so the class winner is decided by the local comparison

\[
\boxed{3x_O+1\ \gtrless\ x_E}.
\]

This shows that the Hensel quotient evolution is a local two-channel max merge, not an unconstrained all-to-all comparison.

It does not by itself make the central state space small, but it identifies the exact interaction locus that a future symbolic or streamed implementation should target.

## 7. Boundary concentration in the MATH-045--MATH-050 data

For depths 35--40, regrouping the exact new-removal counts by

\[
s=d_{\max}(k)-d=q-q_{\min}(k)
\]

gives:

| s | prefilter sum | newly pruned | share of all new pruning | pruning rate |
|---:|---:|---:|---:|---:|
| 0 | 2,777,546,167 | 2,750,297 | 63.9883% | 0.0990% |
| 1 | 3,368,921,573 | 1,115,309 | 25.9488% | 0.0331% |
| 2 | 2,547,732,131 | 317,008 | 7.3755% | 0.0124% |
| 3 | 1,466,042,887 | 85,242 | 1.9832% | 0.0058% |
| 4 | 692,920,487 | 22,472 | 0.5228% | 0.0032% |

Across these six depths,

\[
\boxed{89.9371\%}
\]

of all new pruning occurs at `s<=1`, and

\[
\boxed{97.3126\%}
\]

occurs at `s<=2`.

This is finite evidence, not an asymptotic theorem.  It nevertheless gives a strong computational partition: the heavy exact-residue work is concentrated near the coefficient boundary.

## 8. Fixed-d defect sequences

Regrouping the same canonical ledgers by fixed even count d reveals a different regularity.  Using depths 32--40:

- `d=0`: `R=0`;
- `d=1`: `R=0`;
- `d=2`: `R=1`;
- `d=3,4,5`: `R=0`;
- `d=6`: `R=2k-30`;
- `d=7`: `R=6k-103`;
- `d=8`: `R=23k-436`;
- `d=9`: `R=83k-1705`.

All four displayed linear laws agree exactly at every audited depth 32--40.

For `d=10`, depths 33--40 obey

\[
R_{k,10}=4k^2+174k-6388,
\]

while depth 32 is `3278`, six above the polynomial value `3272`.  This is therefore only an eventual-polynomial candidate, not a law.

`d>=11` already shows more complicated finite differences and is left unresolved.

## 9. Forward falsification at depth 41

Before beginning the full MATH-051 computation, the fixed-d laws were tested on a new depth by direct exhaustive fixed-d enumeration.

Observed depth-41 new removals:

| d | prediction from depth32--40 | exact depth41 result |
|---:|---:|---:|
| 2 | 1 | 1 |
| 3 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 0 | 0 |
| 6 | 52 | 52 |
| 7 | 143 | 143 |

Thus the d=2--7 patterns now hold over ten consecutive depths 32--41 and passed a one-step forward falsification test.

This is still finite evidence.  In particular, d=8 and d=9 have not yet received the depth-41 forward test in this checkpoint.

## 10. Extracted d=2 motif

For `d=2`, the observed unique newly pruned word has even positions

\[
E=\{k-2,k-1\}.
\]

An unrestricted competitor with even positions

\[
E'=\{0,k-2\}
\]

has the same q=`k-2` and corrections satisfying

\[
\boxed{C(E')-C(E)=3^{k-2}}.
\]

Hence it lies in the same exact Hensel class and dominates with translation credit 1.

This algebraically explains the existence of the persistent one-removal family.  General uniqueness of this family for arbitrary k is not established here; uniqueness is finite-checked through k=41.

## 11. Extracted d=6 motif families

For every audited `k=32..41`, the complete newly pruned set at d=6 is exactly the union of two families indexed by

\[
10\le n\le k-6.
\]

Candidate even-position sets:

\[
A_{k,n}=\{n-2,n,n+1,n+2,n+3,k-2\},
\]

\[
B_{k,n}=\{n-3,n,n+1,n+2,n+3,k-2\}.
\]

Corresponding unrestricted competitors:

\[
A'_{k,n}=\{0,1,n-2,n,k-2,k-1\},
\]

\[
B'_{k,n}=\{0,1,n-3,n+1,k-2,k-1\}.
\]

Using the exact correction formula for a consecutive odd block,

\[
C_{\rm out}=3^L C_{\rm in}+2^a(3^L-2^L),
\]

both families give

\[
\boxed{C(A'_{k,n})-C(A_{k,n})=3^{k-5}},
\]

\[
\boxed{C(B'_{k,n})-C(B_{k,n})=3^{k-5}}.
\]

Since q=`k-6`, the difference is

\[
3^{k-5}=3\cdot3^{k-6},
\]

so each competitor is in the same exact Hensel class with credit 3.

The number of candidates is

\[
2\bigl((k-6)-10+1\bigr)=\boxed{2k-30},
\]

exactly matching the observed defect law throughout k=32..41.

What is established here is:

1. the two explicit families are genuine exact same-class domination motifs;
2. over k=32..41, exhaustive enumeration shows that they are exactly the complete newly pruned d=6 set.

What is not yet established is arbitrary-k completeness of these two families.

## 12. DSD interpretation and proposed hybrid calculation

The state space now separates naturally into three structural zones.

### A. Boundary defect zone

Small `s=d_max-d`, especially `s<=2`.

This zone accounts for more than 97% of the observed new pruning at depths 35--40 and remains the main exact-residue computational burden.  No unsafe residue compression is justified here yet.

### B. Stable low-d motif zone

Small fixed d.

Here the defect field is zero, constant, or low-degree over long exact depth intervals, and explicit collision motifs are already extractable at d=2 and d=6.

The next objective is to replace brute-force high-q tail enumeration by proved motif-count formulas wherever arbitrary-k completeness can be established.

### C. Transition zone

Intermediate d, currently around d=10--12 in the available data.

Simple linear laws begin to break or acquire activation thresholds.  This zone should be treated as a separate symbolic-search problem rather than being forced into either boundary or stable-tail assumptions.

## 13. Next structural tasks before/alongside MATH-051

1. Prove or refute arbitrary-k uniqueness of the d=2 motif.
2. Prove or refute arbitrary-k completeness of the two d=6 motif families.
3. Extract d=7, d=8 and d=9 collision motifs and determine why their finite defect counts are linear.
4. Test the d=8 and d=9 linear predictions at depth 41 using an exact bucket implementation.
5. Determine whether d=10 is eventually polynomial or only locally polynomial/quasi-polynomial.
6. Implement an incremental two-channel class-max merge using the normalized residue maps instead of re-enumerating all unrestricted words at each depth.
7. Keep the boundary zone exact until a genuine exact quotient is proved.

## 14. Audit boundaries

The following upgrades are prohibited:

- fixed-d finite linearity => arbitrary-k theorem;
- depth-normalized residue => loss of ternary residue precision;
- sparse defect counts => negligible or ignorable collisions;
- boundary concentration => central layers alone determine all future pruning;
- motif witness => completeness of the motif family without proof;
- autonomous coordinate dynamics => Collatz proof.

The present result is a change in calculation representation and a finite structural discovery.  It materially supports a DSD-guided hybrid algorithm, but does not close the global conjecture.

## Reproducibility

- canonical depth ledgers: depth32 through depth40 one-sided Hensel result files;
- fixed-d pattern ledger: `collatz/results/2026-09-10-dsd-fixed-d-defect-patterns.tsv`;
- direct fixed-d certificate: `collatz/src/2026_09_10_dsd_fixed_d_forward_motif_certificate.cpp`.

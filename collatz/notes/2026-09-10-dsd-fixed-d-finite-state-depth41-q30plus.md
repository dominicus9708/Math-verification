# DSD fixed-d finite-state checkpoint — depth 41 q>=30

Date: 2026-09-10
Status: `PARTIAL MATH-051 / EXACT q>=30 / CENTRAL q=26..29 OPEN`

- Collatz conjecture: `OPEN`.
- MATH-050 remains the latest completed full-depth audit.
- This checkpoint advances depth 41 only for `q=30..41`, equivalently `d=k-q=0..11`.
- The result is exact within the audited fixed-d / finite-state calculation; it is not a full depth-41 closure.

## 1. Fixed-d correction signature

For a length-k parity word, let the d even positions be

\[
E=(e_0<e_1<\cdots<e_{d-1}),
\qquad q=k-d.
\]

The correction C in

\[
T^k(N)=\frac{3^{k-d}N+C(E)}{2^k}
\]

obeys the exact identity

\[
\boxed{
\frac{C(E)}{3^{k-d}}
=1+\sum_{j=0}^{d-1}3^j\left(\frac23\right)^{e_j}
-3^d\left(\frac23\right)^k
}.
\]

Define

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}3^j\left(\frac23\right)^{e_j}
}.
\]

For two words E,F of the same k,d, the common k-dependent terms cancel:

\[
\boxed{
C(F)-C(E)=3^{k-d}\bigl(\Sigma_d(F)-\Sigma_d(E)\bigr).
}
\]

Therefore

\[
\boxed{
E\equiv F\pmod{\text{exact Hensel class}}
\iff
\Sigma_d(F)-\Sigma_d(E)\in\mathbb Z.
}
\]

If that integer is positive, it is exactly the Hensel translation credit of F over E.

This removes explicit depth dependence from same-d collision and dominance comparisons.

## 2. Gap-coordinate reduction

Define cumulative odd-gap coordinates

\[
G_j=e_j-j.
\]

Then

\[
\boxed{
\Sigma_d(E)=\sum_{j=0}^{d-1}2^j\left(\frac23\right)^{G_j}.
}
\]

Because the even positions are strictly increasing,

\[
0\le G_0\le G_1\le\cdots\le G_{d-1}.
\]

At fixed d, trailing odd steps after the final even do not appear in `Sigma_d`; they change depth but not the same-d collision signature.

Grouping equal gap levels gives

\[
\Sigma_d=\sum_{r\ge0}a_r\left(\frac23\right)^r,
\]

where each integer `a_r` is a sum of powers `2^j` from the even ranks assigned to gap level r.

## 3. Bounded carry criterion

For two fixed-d words let

\[
\Delta a_r=a_r(F)-a_r(E).
\]

Initialize the high-level carry by `h_M=0`, where M is the largest occupied gap level. Descending from r=M to r=1, require

\[
\boxed{h_r+\Delta a_r\equiv0\pmod3}
\]

and update

\[
\boxed{
h_{r-1}=\frac{2(h_r+\Delta a_r)}3.
}
\]

If any divisibility condition fails, the two words are not in the same exact Hensel class. If all steps pass, the exact translation credit is

\[
\boxed{\Delta a_0+h_0}.
\]

Since

\[
|\Delta a_r|\le2^d-1
\]

and the update contracts by the factor `2/3`, the carry is bounded for fixed d. Thus fixed-d exact Hensel collision testing is representable by a finite carry-state system.

The algebraic certificate is stored at

`collatz/src/2026_09_10_fixed_d_signature_bounded_carry_certificate.py`.

Its self-test checks the general signature identity against the original correction recurrence, the carry criterion against direct `mod 3^(k-d)` equality, the d=2 credit-1 family, and the two extracted d=6 credit-3 families.

## 4. Finite-state dominated-count formulation

Let

\[
D_{k,d}
\]

denote the number of coefficient-valid length-k words with d even steps that are terminally dominated in their exact Hensel class.

Instead of enumerating all `C(k,d)` parity words, the finite-state prototype reads candidate gap levels while propagating only the bounded set of competitor/carry possibilities. Candidate prefixes with the same future competitor-state set are merged into one subset state.

Downstream-stable class dominance gives the primitive defect relation

\[
\boxed{
R_{k,d}=D_{k,d}-D_{k-1,d}-D_{k-1,d-1}.
}
\]

Here `R_{k,d}` is the number of nested candidate prefixes that lose exact class-max for the first time at `(k,d)`.

This relation was regression-checked against the stored depth-32 fixed-d exact data for `d=2..9`, reproducing

\[
1,0,0,0,34,89,300,951
\]

without parity-word enumeration at that depth.

## 5. Depth-41 exact q>=30 result

At depth 41, `q=41-d`. The exact partial ledger is

`collatz/results/2026-09-10-depth41-q30plus-finite-state-dsd.tsv`.

| q | d | pre-Hensel | new defect R(41,d) | survivors |
|---:|---:|---:|---:|---:|
| 41 | 0 | 1 | 0 | 1 |
| 40 | 1 | 39 | 0 | 39 |
| 39 | 2 | 703 | 1 | 702 |
| 38 | 3 | 8,393 | 0 | 8,393 |
| 37 | 4 | 72,943 | 0 | 72,943 |
| 36 | 5 | 490,672 | 0 | 490,672 |
| 35 | 6 | 2,654,671 | 52 | 2,654,619 |
| 34 | 7 | 11,850,117 | 143 | 11,849,974 |
| 33 | 8 | 44,393,684 | 507 | 44,393,177 |
| 32 | 9 | 141,092,144 | 1,698 | 141,090,446 |
| 31 | 10 | 382,235,624 | 7,470 | 382,228,154 |
| 30 | 11 | 880,982,971 | 29,342 | 880,953,629 |

Hence the audited q>=30 partial totals are

\[
\boxed{1,463,781,962\to1,463,742,749}
\]

with

\[
\boxed{39,213}
\]

new primitive defects.

## 6. Newly forward-checked fixed-d laws

The depth-41 exact finite-state results give

\[
R_{41,8}=507,
\qquad
R_{41,9}=1698,
\qquad
R_{41,10}=7470,
\qquad
R_{41,11}=29342.
\]

The first three continue the previously observed finite laws:

\[
R_{k,8}=23k-436,
\]

\[
R_{k,9}=83k-1705,
\]

and, for the observed interval beginning at k=33,

\[
R_{k,10}=4k^2+174k-6388.
\]

At k=41 these give exactly 507, 1698, and 7470. These agreements are forward checks, not arbitrary-k proofs.

For d=11, the new exact value 29342 is recorded without imposing a low-degree closed form.

## 7. Motif-transport interpretation

The fixed-d signature explains why extracted same-class witness pairs survive depth transport: if their `Sigma_d` difference is a fixed positive integer, the correction difference is automatically

\[
\Delta C = m\,3^{k-d}
\]

at every depth where the motif is geometrically realizable.

This algebraically supports the previously extracted d=2 and d=6 families and the finite d=8/d=9 transport observations. It does not by itself prove that those motif families exhaust every primitive obstruction at arbitrary depth.

## 8. Computational consequence

The main change is

\[
\boxed{
\text{enumerate parity words}
\longrightarrow
\text{propagate fixed-d finite carry/subset states}.
}
\]

For the depth-41 high-q tail, the observed subset-state scales were approximately

- d=8: 3,445 states;
- d=9: 15,590 states;
- d=10: 72,037 states;
- d=11: 338,690 states.

Thus the q>=30 depth-41 tail was closed without constructing the corresponding enormous parity-word populations individually.

This is the first checkpoint in this branch where the DSD structural reduction materially replaces a large fixed-depth enumeration rather than only auditing it.

## 9. Remaining MATH-051 work

Depth 41 is not complete. The unresolved central layers are

\[
q=29,28,27,26,
\]

equivalently

\[
d=12,13,14,15.
\]

The current Python/prototype state representation grows sharply at d=12. The next task is therefore to minimize/canonicalize the finite subset states and/or combine the fixed-d carry automaton with the exact normalized-residue two-parent DP before attempting the central layers.

No unfinished d=12 run is used as a result.

## 10. Audit boundaries

The following upgrades are prohibited:

- finite-state representation at fixed d => uniform finite state bound independent of d;
- depth-41 forward agreement => arbitrary-k polynomial law;
- same-class transported witness => completeness of an obstruction family;
- q>=30 exact partial closure => full MATH-051 completion;
- finite exact high-q result => Collatz proof.

## 11. Provenance and prior-work policy

Classical parity-vector, affine-iterate and adic/congruence background is to be cited as prior work when used. If a structure is independently rediscovered and later matched to prior literature, both facts should be stated. Git history records when this project derived or imported a method; it is not by itself a mathematical priority claim.

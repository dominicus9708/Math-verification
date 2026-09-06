# COV-1 inverse-limit ghost terminal criterion

Date: 2026-09-06

Status: **SAFE EXACT TERMINAL REDUCTION.**  The unresolved progression

\[
36\mathbb N_0+27
\]

need not be covered by a finite certificate tree.  Infinite open symbolic paths are harmless provided their compatible dyadic parameter limit is not a nonnegative ordinary integer.

This note formalizes that quantifier structure.  It does not prove COV-1.

---

## 1. One parity prefix gives one `k` cylinder

Let `w` be a shortcut parity prefix of length `L>=2`, odd count `q`, and correction

\[
C(w).
\]

Its canonical starting residue is

\[
\boxed{
n_L(w)
\equiv
-C(w)3^{-q}
\pmod{2^L},
\qquad
0\le n_L(w)<2^L.
}
\]

For a prefix beginning with `11`,

\[
n_L(w)\equiv3\pmod4.
\]

The COV-1 progression is

\[
N=36k+27.
\]

Therefore

\[
\frac{N-27}{4}=9k.
\]

Since `9` is a unit modulo every power of `2`, define

\[
\boxed{
c_L(w)
\equiv
9^{-1}\frac{n_L(w)-27}{4}
\pmod{2^{L-2}},
}
\]

where division by `4` is performed on the integer difference before reduction.

Then exactly

\[
\boxed{
N=36k+27\text{ has parity prefix }w
\iff
k\equiv c_L(w)\pmod{2^{L-2}}.
}
\]

This is the nested form of the previously proved full-dyadic-suffix theorem.

---

## 2. Nested prefixes give a unique `2`-adic parameter

Let

\[
w^{(2)}\prec w^{(3)}\prec w^{(4)}\prec\cdots
\]

be nested parity prefixes of one infinite path.

Parity-vector compatibility gives

\[
n_{L+1}\equiv n_L\pmod{2^L}.
\]

Hence

\[
\boxed{
c_{L+1}\equiv c_L\pmod{2^{L-2}}.}
\]

The residues therefore define a unique inverse-limit point

\[
\boxed{k_\infty\in\mathbb Z_2.}
\]

Equivalently,

\[
k_\infty\equiv c_L\pmod{2^{L-2}}
\]

for every `L`.

Thus every infinite symbolic branch exists perfectly well in the `2`-adic parameter space, whether or not it corresponds to an ordinary nonnegative `k`.

---

## 3. Ordinary-integer criterion

Take `c_L` to be the least nonnegative representative modulo `2^(L-2)`.

### If `k_infty` is a nonnegative ordinary integer

For every sufficiently large `L`,

\[
2^{L-2}>k_\infty.
\]

Hence the least representative is exactly

\[
\boxed{c_L=k_\infty}
\]

for all sufficiently large `L`.

### Conversely, if the representatives stabilize

Suppose there is `L_0` and `k>=0` such that

\[
c_L=k
\]

for every `L>=L_0`.

Then

\[
N=36k+27
\]

lies in every nested parity cylinder, and therefore its actual infinite parity vector is the given infinite path.

Thus

\[
\boxed{
 k_\infty\in\mathbb N_0
\iff
(c_L)\text{ is eventually constant as least nonnegative representatives}.
}
\]

Equivalently, the binary lift digits of `k_infty` are eventually zero.

---

## 4. Certificate-tree terminal theorem

Consider any sound prefix-certificate tree for `36k+27` in which a branch is closed only after a verified smaller merge/descent certificate has been obtained for the whole arithmetic cylinder represented by that prefix.

Assume every `k\in\mathbb N_0` follows its unique nested parity branch.

Then the following condition is sufficient for COV-1:

> Every infinite open branch has a non-eventually-constant parameter sequence `c_L`.

Indeed, if some ordinary `k` remained open forever, then its nested residues would satisfy

\[
c_L=k
\]

for every sufficiently large `L`, producing an infinite open branch with eventually constant representatives, contrary to the condition.

Therefore

\[
\boxed{
\text{all infinite open branches are `2`-adic ghosts}
\Longrightarrow
36\mathbb N_0+27\text{ is recursive},
}
\]

provided all finite leaf certificates are themselves sound.

This is a **terminal criterion**, not a claim that the premise has been proved.

---

## 5. Why finite-level emptiness is unnecessarily strong

The previously proved dyadic-suffix theorem gives, for every finite `L`, every possible suffix after the fixed `11` head.

Thus statements of the form

\[
\forall L\;\exists k_L:\text{a hard prefix of length }L
\]

are unavoidable and do not imply an ordinary counterexample.

The dangerous quantifier order is instead

\[
\exists k\in\mathbb N_0\;\forall L:\text{the same }k\text{ remains hard}.
\]

The inverse-limit formulation separates these correctly:

\[
\boxed{
\forall L\exists k_L
\quad\not\Rightarrow\quad
\exists k\forall L.
}
\]

A sequence of finite witnesses may simply converge to a non-natural `2`-adic ghost.

---

## 6. Periodic examples

### All-odd path

The all-odd path has

\[
N_\infty=-1.
\]

Since

\[
36k+27=-1,
\]

its parameter is

\[
\boxed{k_\infty=-\frac79.}
\]

This is a valid `2`-adic integer because `9` is a `2`-adic unit, but it is not in `N_0`.

### `110` periodic path

The periodic survivor

\[
(110)^\infty
\]

has

\[
N_\infty=-5,
\]

hence

\[
\boxed{k_\infty=-\frac89.}
\]

Again the nested finite parity cylinders are all nonempty, but their inverse-limit parameter is not an ordinary nonnegative integer.

The general coefficient-surviving eventually-periodic branch is already closed as a negative rational ghost in

`2026-09-06-coefficient-surviving-eventually-periodic-negative-ghost-theorem.md`.

---

## 7. Relation to canonical lift bits

Write

\[
c_{L+1}=c_L+\eta_L2^{L-2},
\qquad
\eta_L\in\{0,1\}.
\]

Changing `k` by `2^(L-2)` changes

\[
N=36k+27
\]

by

\[
36\cdot2^{L-2}=9\cdot2^L
\equiv2^L\pmod{2^{L+1}}.
\]

Therefore `eta_L` is exactly the ordinary canonical-start lift bit at binary position `L`.

Consequently

\[
\boxed{
(c_L)\text{ eventually stabilizes}
\iff
\eta_L=0\text{ eventually}.
}
\]

This identifies the COV-1 inverse-limit condition with the existing Gate-C finite-support/canonical-lift condition.

It does **not** solve that condition: once the lift tail is zero, its dynamics become the actual Collatz orbit, as already audited.

---

## 8. DSD status

### CLOSED / SAFE

1. parity prefix `w` ↔ one exact `k mod 2^(L-2)` cylinder;
2. nested prefixes ↔ one exact `k_infty in Z_2`;
3. ordinary nonnegative `k` ↔ eventual stabilization of least representatives;
4. finite-level nonemptiness does not imply a common ordinary integer;
5. eventual periodic coefficient-survivors are negative ghosts.

### OPEN

1. proving that every genuinely aperiodic infinite open branch has nonstabilizing `c_L`;
2. COV-1 itself;
3. the full repaired ternary-core coverage chain.

### PROHIBITED UPGRADES

1. Do not demand finite-depth emptiness as if it were necessary.
2. Do not infer a counterexample from an infinite `2`-adic branch.
3. Do not infer a common natural `k` from finite witnesses `k_L` that vary with depth.
4. Do not call canonical-lift stabilization solved; zero-tail is the real Collatz dynamics.

---

## 9. Next target

After removing eventually-periodic ghosts, the exact surviving terminal obligation is

\[
\boxed{
\text{genuinely aperiodic infinite open branch}
\Longrightarrow
c_L\text{ does not eventually stabilize}.
}
\]

Any future aggregate/Fourier/Hensel argument should be judged by whether it supplies information about this **same nested branch**, not merely about the number or density of finite hard prefixes.

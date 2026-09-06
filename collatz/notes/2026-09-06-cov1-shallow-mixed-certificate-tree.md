# COV-1: shallow mixed `2`-adic / `3`-adic certificate tree

Date: 2026-09-06

Status: **EXACT FINITE SYMBOLIC CERTIFICATE / GLOBAL COV-1 OPEN.**  After two architecture barriers were established—no finite pure binary one-turn cover and a strict `<8%` ceiling for the single `T(x)`-anchored inverse language—the next admissible architecture is a mixed tree.  This note combines exact forward-descent dyadic cylinders with shifted inverse-anchor triadic cylinders.

The finite tree improves certified natural-density coverage of

\[
x=36k+27
\]

from

\[
45/64=70.3125\%
\]

using forward descent alone through depth `8`, to

\[
\boxed{
\frac{6011273}{8503056}
\approx0.7069544173294872
}
\]

when exact inverse cylinders from anchors `h=1,2,3` through `q<=16` are added by CRT.  The gain is real but small.  No limit is inferred.

---

## 1. Shifted forward anchors

Let

\[
x=36k+27.
\]

The first two shortcut states are uniformly odd:

\[
T(x)=54k+41,
\qquad
T^2(x)=81k+62.
\]

For `h>=2`, split

\[
k=2^{h-2}u+c,
\qquad
0\le c<2^{h-2}.
\]

The length-`h` parity prefix is then fixed on each `c` cylinder.  If it contains `s` odd shortcut states, direct calculation gives

\[
\boxed{
T^h(x)=3^{s+2}u+B_{h,c}
}
\]

for an integer intercept `B_(h,c)`.

The starting value on the same cylinder is

\[
x=36\cdot2^{h-2}u+36c+27
=9\cdot2^h u+36c+27.
\]

Thus the endpoint coefficient comparison is controlled exactly by

\[
3^s\quad\text{versus}\quad2^h,
\]

while the intercept comparison remains a separate gate.

Status: **SAFE AFFINE BRANCH FORMULA.**

---

## 2. Exact forward-descent cylinders through `h<=8`

Applying the uniform affine criterion

\[
A'\le A,
\qquad
B'<B
\]

to every parity cylinder through `h=8` gives the following prefix-free `k` cylinders, written as residues modulo `2^a`:

\[
\begin{aligned}
&a=2:\quad 2,\\
&a=3:\quad 4,7,\\
&a=5:\quad 3,8,21,\\
&a=6:\quad 9,19,24,37,43,48,61.
\end{aligned}
\]

Their exact density is

\[
\boxed{
\frac14+rac28+rac3{32}+rac7{64}
=\frac{45}{64}.
}
\]

Therefore `45` of the `64` residue classes modulo `64` already have a uniform forward iterate below the start by depth at most `8`.

The `19` surviving classes modulo `64` are

\[
\boxed{
0,1,5,11,13,16,17,25,27,29,32,33,41,45,49,51,56,57,59.
}
\]

They split by the parity of `k` into

\[
\boxed{4\text{ even survivors},\qquad15\text{ odd survivors}.}
\]

Status: **EXACT FINITE FORWARD CERTIFICATE.**

This is not a universal stopping-time theorem.

---

## 3. General shifted inverse-anchor cylinder

For a fixed forward branch

\[
z_h=T^h(x)=A_hu+B_h,
\]

write

\[
v=v_3(A_h).
\]

A reverse word with `q` inverse-odd letters at positions

\[
p_0<\cdots<p_{q-1}
\]

has the normalized congruence

\[
A_hu+B_h
\equiv
\sum_{j=0}^{q-1}
3^j2^{-p_j-1}
\pmod{3^q}.
\]

The first `v` positions must satisfy the intercept congruence modulo `3^v`.  Once that holds, the word determines at most one cylinder

\[
\boxed{u\pmod{3^{q-v}}.}
\]

The full affine endpoint is reconstructed and checked for

\[
0<m<x
\]

before a cylinder is accepted.

Thus every accepted certificate has a mixed address

\[
\boxed{
k=2^{h-2}u+c,
\qquad
u\equiv r\pmod{3^b}.}
\]

By CRT it is a single arithmetic progression modulo

\[
2^{h-2}3^b.
\]

Status: **SAFE MIXED-CYLINDER CALCULUS.**

---

## 4. Reverse anchor families used in the finite tree

The exact prefix-free inverse cylinders through `q<=16` are:

\[
\begin{array}{c|c|c}
\text{anchor}&\text{dyadic branch}&\text{prefix-free triadic cylinders}\\\hline
h=1&T(x)=54k+41&742\\
h=2&T^2(x)=81k+62&994\\
h=3&k\equiv0\pmod2&994\\
h=3&k\equiv1\pmod2&213
\end{array}
\]

The largest retained triadic depth is `12`, so all these cylinders can be compared exactly on

\[
\mathbb Z/3^{12}\mathbb Z,
\qquad
3^{12}=531441.
\]

The union from anchors `h=1,2` contains

\[
6848
\]

residues modulo `3^12`.

After adding the `h=3` branch:

\[
\boxed{
\begin{array}{c|c}
k\text{ parity}&\text{covered triadic residues mod }3^{12}\\\hline
0&6848\\
1&6857
\end{array}
}
\]

Thus, at this depth, the even `h=3` shifted anchor contributes no residue outside the already covered `h=1,2` triadic union, while the odd branch contributes only nine additional depth-12 residues.

Status: **FINITE ONLY.**

No permanent containment theorem is inferred from the zero addition on the even branch.

---

## 5. CRT combination

Because powers of `2` and powers of `3` are coprime, the dyadic and triadic cylinder conditions combine independently by CRT.

The direct-descent part contributes

\[
\frac{45}{64}.
\]

Among the `19/64` dyadic survivors, the reverse-anchor contribution is

\[
\frac4{64}\frac{6848}{531441}
+
\frac{15}{64}\frac{6857}{531441}.
\]

Therefore the full finite mixed certificate has density

\[
\begin{aligned}
\delta_{\rm mixed}
&=
\frac{45}{64}
+
\frac4{64}\frac{6848}{531441}
+
\frac{15}{64}\frac{6857}{531441}\\
&=
\boxed{
\frac{6011273}{8503056}
}\\
&\approx
\boxed{0.7069544173294872}.
\end{aligned}
\]

The incremental gain over the forward-only depth-8 tree is therefore about

\[
0.0038294173,
\]

i.e. roughly `0.383` percentage points.

---

## 6. What this finite tree teaches

The calculation answers an architectural question.

The mixed `2`/`3` mechanism is **not empty**: exact shifted inverse certificates do remove additional classes that shallow forward descent does not.

However, shallow anchor proliferation is inefficient.  At the tested levels, the main coverage comes from forward descent, while the first three inverse anchors only lightly erode the difficult forward-survivor set.

Therefore the next proof target should not be

> add many shallow anchors and hope the finite density approaches one.

Instead it should compress the state of the surviving branches themselves.

Natural state variables are:

1. forward depth `h`;
2. odd count `s_h` / Beatty slack;
3. affine intercept of the forward branch;
4. `3`-adic valuation capacity of the turning coefficient;
5. the normalized inverse congruence defect.

This is precisely where a nonstationary mixed automaton may be useful—but unlike the rejected single-anchor complement automaton, its states must include **forward-anchor changes**.

---

## 7. DSD audit

### SAFE

1. The affine branch formula `T^h(x)=3^(s+2)u+B` after splitting `k mod 2^(h-2)`.
2. Exact forward-descent criterion on each cylinder.
3. Exact `45/64` forward coverage through `h<=8`.
4. Exact shifted inverse-cylinder construction.
5. Exact CRT composition.
6. Exact finite mixed density `6011273/8503056`.

### FINITE ONLY

- `45/64` as a depth-8 coverage fraction;
- the counts `742,994,994,213` through `q<=16`;
- the depth-12 residue counts `6848,6848,6857`;
- the `70.6954%` mixed coverage value.

### OPEN

1. Any asymptotic mixed-tree coverage theorem.
2. Whether a recursively structured mixed tree certifies every ordinary `k`.
3. Whether the difficult branches admit a finite-state quotient.
4. Full `36N_0+27` recursion.

### PROHIBITED UPGRADES

1. Do not infer density-one coverage from the finite increase.
2. Do not infer that shifted anchors are useless from their small shallow gain.
3. Do not treat an uncovered mixed cylinder as a counterexample.
4. Do not replace universal recursion with a density statement.

---

## 8. Regression certificate

`collatz/src/cov1_mixed_2adic_3adic_shallow_tree_certificate.py`

reconstructs all forward branches, all accepted inverse cylinders in the declared finite domain, performs the CRT union, and asserts

\[
\boxed{
\delta_{\rm mixed}
=
\frac{6011273}{8503056}.
}
\]

---

## 9. Next target

The next step is to derive a **state recurrence** for the mixed survivor branch rather than extending raw residue lists.

For a forward branch with depth `h`, odd count `s`, and affine state

\[
z=3^{s+2}u+B,
\]

we should normalize the intercept by its available `3`-adic capacity and track how one additional forward parity bit changes:

\[
(h,s,B)
\longmapsto
(h+1,s',B').
\]

At selected turns, the inverse congruence should be written as a defect state rather than a full residue list.

A successful quotient would turn the current mixed CRT tree into a small nonstationary automaton driven by the same Beatty word already present in the coefficient-survivor analysis.

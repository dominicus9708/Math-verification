# COV-1: companion-word merge calculus and an infinite recursive dyadic seed family

Date: 2026-09-06

Status: **SAFE EXACT COMPANION CALCULUS + SAFE INFINITE SUBCOVER / GLOBAL COV-1 OPEN.**  The growing `3`-adic mixed state can be replaced, for one important class of certificates, by a pair of finite binary words whose affine constants differ by an exact multiple of `3^(s+2)`.  A companion seed with defect `D=1` or `D=2` yields a universal smaller merge on its whole dyadic cylinder, and the defect is invariant under arbitrary common suffix extension.  This produces an explicit infinite prefix-free recursive family of total `k`-density `1/8` inside the unresolved progression `36k+27`.

This is not a proof that every `36k+27` is recursive and not a proof of the Collatz conjecture.

---

## 1. Forward affine constant

For a binary shortcut parity word `w` of length `h`, let

\[
s=|w|_1
\]

and write

\[
\boxed{
T^h(n)=\frac{3^s n+C(w)}{2^h}.
}
\]

If the odd positions are

\[
0\le d_0<\cdots<d_{s-1}<h,
\]

then

\[
\boxed{
C(w)=
\sum_{a=0}^{s-1}
3^{s-1-a}2^{d_a}.
}
\]

Thus the mixed-state constant `C_h` introduced in the previous note is exactly the additive correction channel already used throughout the first-crossing calculations.

Status: **SAFE / CLASSICAL.**

---

## 2. Reverse word as a binary companion

At the dyadic branch represented by `w`, write

\[
k=2^{h-2}u+c,
\qquad
0\le c<2^{h-2},
\]

so that

\[
x=36k+27
=9\cdot2^h u+36c+27.
\]

The turning value has form

\[
T^h(x)=3^{s+2}u+B_h,
\]

and the previously proved compression identity is

\[
\boxed{
2^hB_h\equiv C(w)\pmod{3^{s+2}}.
}
\]

Take a reverse word of total length

\[
K=h+3
\]

with exactly

\[
q=s+2
\]

inverse-odd letters.  If its inverse-odd positions are

\[
p_0<\cdots<p_{q-1},
\]

pad trailing inverse-even letters if necessary so that the total length is exactly `h+3`.

Now reverse this binary reverse-word indicator in time and call the resulting binary word `z`.  Then

\[
|z|=h+3,
\qquad
|z|_1=s+2.
\]

The exact reverse-word correction is

\[
\sum_{a=0}^{q-1}
3^a2^{K-1-p_a}.
\]

But this is precisely

\[
\boxed{C(z).}
\]

Hence reverse compatibility is equivalent to

\[
\boxed{
C(z)\equiv8C(w)\pmod{3^{s+2}}.
}
\]

The factor `8` comes from the fixed length difference

\[
K-h=3.
\]

Status: **SAFE EXACT FORWARD/REVERSE IDENTIFICATION.**

---

## 3. Companion defect

Whenever the congruence holds, define

\[
\boxed{
D(w,z)
:=
\frac{C(z)-8C(w)}{3^{s+2}}
\in\mathbb Z.
}
\]

This integer contains exactly the intercept information that is lost if one records only the congruence class.

Let `m` be the endpoint obtained by following the reversed companion word from the turning value.  Using

\[
2^hB_h
=
3^s(36c+27)+C(w),
\]

we obtain

\[
\begin{aligned}
m
&=
\frac{2^{h+3}(3^{s+2}u+B_h)-C(z)}{3^{s+2}}\\
&=
2^{h+3}u
+
\frac{8\,3^s(36c+27)+8C(w)-C(z)}{3^{s+2}}\\
&=
\boxed{
2^{h+3}u+32c+24-D(w,z).
}
\end{aligned}
\]

The start is

\[
\boxed{
x=9\cdot2^hu+36c+27.}
\]

Therefore

\[
\boxed{
x-m
=2^h u+4c+3+D(w,z).}
\]

Status: **SAFE EXACT ENDPOINT FORMULA.**

---

## 4. Exact positivity/descent gate

A companion pair gives a positive smaller endpoint for every

\[
u\ge0
\]

on the dyadic branch iff

\[
32c+24-D>0
\]

and

\[
4c+3+D>0.
\]

Equivalently, for integer `D`,

\[
\boxed{
-4c-2\le D\le32c+23.
}
\]

In particular, because `c>=0`, both

\[
\boxed{D=1}
\]

and

\[
\boxed{D=2}
\]

automatically satisfy positivity and strict descent on every branch.

Thus

\[
\boxed{
D\in\{1,2\}
\Longrightarrow
\text{uniform smaller merge on the whole dyadic cylinder}.
}
\]

This is stronger than the previous congruence-only compatibility test.

---

## 5. Defect invariance under common suffix extension

Let the current pair be `(w,z)` with

\[
|z|=|w|+3,
\qquad
|z|_1=|w|_1+2.
\]

Append the same bit

\[
e\in\{0,1\}
\]

to both words.

### Even suffix bit

If `e=0`, both affine constants are unchanged and the odd counts are unchanged.  Therefore

\[
D(w0,z0)=D(w,z).
\]

### Odd suffix bit

If `e=1`, then

\[
C(w1)=3C(w)+2^h,
\]

while

\[
C(z1)=3C(z)+2^{h+3}.
\]

Hence

\[
C(z1)-8C(w1)
=3\bigl(C(z)-8C(w)\bigr),
\]

and the new denominator is

\[
3^{s+3}=3\cdot3^{s+2}.
\]

Thus again

\[
\boxed{D(w1,z1)=D(w,z).}
\]

By induction, for every finite common suffix `u`,

\[
\boxed{
D(wu,zu)=D(w,z).
}
\]

Status: **SAFE COMPANION-INHERITANCE THEOREM.**

Therefore a single companion seed certifies its entire dyadic descendant cylinder.

---

## 6. Infinite seed family

For every

\[
r\ge4,
\]

define

\[
\boxed{w_r=1^r00.}
\]

It has length

\[
h=r+2
\]

and odd count

\[
s=r.
\]

Its affine constant is

\[
\boxed{
C(w_r)=3^r-2^r.
}
\]

Define two companion words:

\[
\boxed{
z_r^{(1)}=11100\,1^{r-2}\,01,}
\]

\[
\boxed{
z_r^{(2)}=0110\,1^{r-1}\,01.}
\]

Both have length

\[
r+5=h+3
\]

and odd count

\[
r+2=s+2.
\]

Direct recurrence gives

\[
\boxed{
C(z_r^{(1)})
=17\cdot3^r-8\cdot2^r,
}
\]

and

\[
\boxed{
C(z_r^{(2)})
=26\cdot3^r-8\cdot2^r.
}
\]

Since

\[
8C(w_r)=8\cdot3^r-8\cdot2^r,
\]

we obtain

\[
C(z_r^{(1)})-8C(w_r)
=9\cdot3^r
=3^{r+2},
\]

and

\[
C(z_r^{(2)})-8C(w_r)
=18\cdot3^r
=2\cdot3^{r+2}.
\]

Therefore

\[
\boxed{
D(w_r,z_r^{(1)})=1,
\qquad
D(w_r,z_r^{(2)})=2.
}
\]

Both are universal smaller-merge seeds.

Status: **SAFE INFINITE FAMILY.**

---

## 7. Why these are actual `36k+27` cylinders

The progression

\[
36k+27=4(9k+6)+3
\]

has full dyadic suffix entropy after the forced first two parity bits `11`, because multiplication by `9` is invertible modulo every `2^r`.

Every word

\[
w_r=1^r00,
\qquad r\ge4,
\]

starts with `11`, so each is realized by exactly one residue class

\[
k\pmod{2^r}.
\]

The family is prefix-free: if `r'<r`, then `w_(r')` has its first zero where `w_r` still has a one.

Therefore the corresponding dyadic cylinders are pairwise disjoint and have total natural density in the free parameter `k`

\[
\sum_{r=4}^{\infty}\frac1{2^r}
=
\boxed{\frac18}.
\]

Hence

\[
\boxed{
\text{at least }12.5\%\text{ of the }36k+27\text{ parameter space is recursively certified by this one infinite companion family.}
}
\]

This is an exact infinite-family theorem, not a finite extrapolation.

---

## 8. Combination with the existing shallow forward-descent cover

The existing exact direct-descent prefix family through `h<=8` has density

\[
\frac{45}{64}.
\]

Three of those finite direct cylinders lie inside the companion family:

- two descendants of `w_4=111100`;
- one descendant of `w_5=1111100`.

Their total overlap density is

\[
\frac1{32}+\frac1{64}+\frac1{64}
=
\frac1{16}.
\]

Thus the exact union of

1. the old direct-descent cover through `h<=8`, and
2. the infinite companion seed family `w_r=1^r00`,

has density

\[
\boxed{
\frac{45}{64}+rac18-rac1{16}
=
\frac{49}{64}
=0.765625.
}
\]

Again, density below one does not imply an obstruction and density tending to one would not by itself prove full coverage.  This figure is only the exact size of the displayed certified union.

---

## 9. Relation to the linear-memory lower bound

The previous note proved that no state of the form

\[
(\sigma_h,R_h\bmod3^{Q(h)})
\]

can decide mixed reverse compatibility when

\[
Q(h)<h-3.
\]

The companion calculus does not contradict that lower bound.  It changes representation instead of truncating the growing residue.

Rather than storing almost all ternary digits of one state, it carries two finite binary words with an invariant integer defect:

\[
\boxed{
(w,z,D).
}
\]

This is precisely the kind of DSD transformation that can evade a coordinate-memory barrier without falsely claiming that the underlying information disappeared.

---

## 10. Finite diagnostic beyond the explicit family

Exact enumeration through depth `h=18` shows additional companion seeds beyond `1^r00`.  In the coefficient-surviving language, the first-hit compatible prefixes are one new `1^(h-2)00` seed at each depth `6<=h<=17`, followed at depth `18` by that expected seed plus six additional prefix-free seeds.

For every compatible coefficient-surviving prefix tested through `h=18`, there are exactly two length-`h+3` companions, with defects

\[
D=1
\quad\text{and}\quad
D=2.
\]

This is **FINITE DIAGNOSTIC ONLY**.  No theorem is presently claimed that every future compatible survivor has exactly these two defects.

---

## 11. DSD audit

### SAFE

1. `C(w)` is exactly the previous correction channel.
2. Reverse compatibility is exactly a binary companion congruence.
3. The companion defect gives the exact affine endpoint.
4. `D=1,2` imply positive strict smaller merges on every branch.
5. `D` is invariant under arbitrary common suffix extension.
6. The infinite family `w_r=1^r00`, `r>=4`, is recursively certified.
7. Its exact parameter density is `1/8`.
8. Its union with the previous direct `h<=8` cover has exact density `49/64`.

### FINITE ONLY

- the observation of exactly two companions for every tested compatible coefficient-survivor prefix through `h=18`;
- the six additional first-hit seeds at depth `18`;
- any empirical trend in the companion-hit density.

### OPEN

1. A classification of all minimal companion seeds.
2. Whether every ordinary `k>=0` eventually enters either a direct-descent or a companion-certified cylinder.
3. Whether the surviving infinite binary paths reduce only to non-natural `2`-adic ghosts or contain other arithmetic obstructions.
4. Full `COV_1`.

### PROHIBITED UPGRADES

1. Do not infer full `COV_1` from the `1/8` infinite-family density.
2. Do not infer that all compatible states have only `D=1,2` from the finite scan.
3. Do not identify an infinite surviving `2`-adic path automatically with a natural-number counterexample.
4. Do not discard the earlier linear-memory theorem; the companion representation bypasses truncation rather than refuting it.

---

## 12. Regression certificate

`collatz/src/cov1_companion_seed_family_certificate.py`

checks the exact closed forms, defect invariance on finite suffix regressions, endpoint inequalities, and the prefix-free `1/8` density identity.

---

## 13. Next target

The highest-value next target is now a **companion-seed survivor tree**.

At every dyadic prefix `w` of the `36k+27` progression:

1. remove the node if a uniform forward descent is already proved;
2. remove it if there exists a companion `z` with `D=1` or `D=2`;
3. otherwise retain its two parity children.

Because both kinds of certificate are inherited by descendants, the retained nodes form a genuine prefix tree.

The key question is no longer density alone.  It is the structure of the inverse limit of this tree:

\[
\boxed{
\bigcap_h\text{ surviving dyadic cylinders}.
}
\]

If every infinite path in that tree can be proved non-natural (for example a finite collection of `2`-adic ghost points), `COV_1` closes even though no finite level need become empty.

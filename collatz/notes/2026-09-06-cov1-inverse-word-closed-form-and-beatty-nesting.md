# COV-1: closed-form inverse words and Beatty nesting of new cylinders

Date: 2026-09-06

Status: **SAFE ALGEBRAIC COMPRESSION + EXACT FINITE CERTIFICATE THROUGH `q=23`; GLOBAL `36k+27` RECURSION OPEN.**

This note compresses the reverse-word search for the unresolved coverage branch

\[
x=36k+27
\]

into one explicit congruence and proves that genuinely new recursive cylinders can arise only at a second Beatty/Sturmian boundary, namely when the available reverse-position budget jumps by two.

---

## 1. Reverse-word closed form

Let

\[
y=T(x)=54k+41.
\]

Use reverse shortcut letters

\[
E(z)=2z,
\qquad
O(z)=\frac{2z-1}{3}
\]

when the latter is integral.

Let a reverse word have total length `K` and `q` letters `O`, occurring at zero-indexed positions

\[
0\le p_0<p_1<\cdots<p_{q-1}<K.
\]

Then after the whole word,

\[
\boxed{
m=\frac{2^K y-C_w}{3^q},}
\]

where

\[
\boxed{
C_w=
\sum_{a=0}^{q-1}
3^a\,2^{K-1-p_a}.
}
\]

Proof: start from `C=0`.  Appending `E` sends

\[
(K,q,C)\mapsto(K+1,q,2C),
\]

while appending `O` sends

\[
(K,q,C)\mapsto(K+1,q+1,2C+3^q).
\]

Iterating gives the displayed sum.

Status: **SAFE EXACT FORMULA.**

---

## 2. Final integrality is equivalent to stepwise admissibility

Suppose all reverse steps before some `O` are integral and that this `O` is invalid.  Then its output has denominator exactly `3` with numerator not divisible by `3`.

From that point onward:

- `E` multiplies the numerator by `2`, so the denominator factor `3` cannot cancel;
- `O` sends `a/3^d` to
  \[
  \frac{2a-3^d}{3^{d+1}},
  \]
  and if `3\nmid a`, then `3\nmid(2a-3^d)`.

Thus once a denominator `3` appears it persists forever.

Therefore

\[
\boxed{
\text{the final value }m\text{ is an integer}
\iff
\text{every }O\text{ step is admissible}.}
\]

This licenses replacing repeated divisibility checks by the final congruence

\[
\boxed{
2^K(54k+41)\equiv C_w\pmod{3^q}.}
\]

Status: **SAFE.**

---

## 3. Trailing `E` letters are never needed

Suppose

\[
w=w'E^t,
\qquad t\ge1,
\]

where `w'` ends in `O`.  The two words have the same `O`-integrality conditions and hence the same `3`-adic `k` cylinder.

If `w'` produces predecessor `m'`, then `w` produces

\[
m=2^t m'.
\]

Consequently, if the longer word already satisfies

\[
m<x,
\]

then

\[
m'=m/2^t<m<x.
\]

Thus trailing `E` letters can only worsen contraction and never create a new coverage cylinder.

Hence every minimal coverage word may be assumed to end in `O`:

\[
\boxed{K=p_{q-1}+1.}
\]

Status: **SAFE PRUNING LEMMA.**

---

## 4. Exact contraction position budget

Since

\[
y=\frac{3x+1}{2},
\]

the leading multiplier of `m` relative to `x` is

\[
\frac{2^{K-1}}{3^{q-1}}.
\]

For a word ending in `O`, `K-1=p_(q-1)`.  Strict asymptotic contraction therefore requires

\[
2^{p_{q-1}}<3^{q-1}.
\]

Because `log_2 3` is irrational, define exactly

\[
\boxed{
P_q:=\left\lfloor(q-1)\log_2 3\right\rfloor.
}
\]

Then every canonical contracting word satisfies

\[
\boxed{p_{q-1}\le P_q.}
\]

Also

\[
P_{q+1}-P_q\in\{1,2\}.
\]

---

## 5. Normalized cylinder congruence

Divide the final congruence by the unit `2^K` modulo `3^q`:

\[
54k+41
\equiv
\sum_{a=0}^{q-1}
3^a2^{-p_a-1}
\pmod{3^q}.
\]

Thus

\[
\boxed{
54k+41
\equiv S_w
:=
\sum_{a=0}^{q-1}3^a2^{-p_a-1}
\pmod{3^q}.}
\]

For `q>=3`, since `54=2\cdot3^3`, this has a solution in `k` iff

\[
S_w\equiv41\pmod{27}.
\]

Only the first three `O` positions matter for this test:

\[
\boxed{
2^{-p_0-1}
+3\,2^{-p_1-1}
+9\,2^{-p_2-1}
\equiv41\pmod{27}.}
\]

If it holds, there is exactly one `k` residue modulo

\[
\boxed{3^{q-3}.}
\]

Explicitly,

\[
\boxed{
k
\equiv
\frac12\,rac{S_w-41}{27}
\pmod{3^{q-3}},}
\]

where division by `2` means multiplication by its inverse modulo `3^(q-3)`.

This reduces the search dramatically: the `mod 27` admissibility filter is determined before the later `O` positions are chosen.

Status: **SAFE EXACT CYLINDER FORMULA.**

---

## 6. Beatty nesting theorem for new cylinders

Consider a canonical contracting word with `q+1` letters `O` and positions

\[
p_0<\cdots<p_q\le P_{q+1}.
\]

Delete its final `O`.  The prefix has `q` letters `O` and final position `p_(q-1)`.

### Case 1: `P_(q+1)=P_q+1`

Then

\[
p_{q-1}\le P_{q+1}-1=P_q.
\]

Therefore the prefix is already a contracting `q`-word.  Since final integrality implies prefix integrality, the `q+1` cylinder is a child of an already certified `q` cylinder.

Hence

\[
\boxed{
P_{q+1}-P_q=1
\Longrightarrow
\text{no genuinely new prefix-free coverage cylinder at level }q+1.}
\]

### Case 2: `P_(q+1)=P_q+2`

A new cylinder can avoid having a contracting `q` prefix only if

\[
p_{q-1}>P_q.
\]

Since positions are integral and increasing,

\[
p_{q-1}=P_q+1,
\qquad
p_q=P_q+2.
\]

Thus every potentially new cylinder at a growth event must end with the two newly opened positions:

\[
\boxed{
(p_{q-1},p_q)=(P_q+1,P_q+2).}
\]

This is an exact structural restriction, not an observed pattern.

Status: **SAFE BEATTY NESTING THEOREM.**

---

## 7. Interpretation

The reverse-merge coverage growth is itself controlled by the mechanical word of slope

\[
\gamma=\log_2 3.
\]

The available position budget grows according to

\[
P_q=\lfloor(q-1)\gamma\rfloor,
\]

and genuinely new `3`-adic cylinders are possible only on the `2`-increment letters of this Beatty word.

This is a second, independent appearance of the same powers-of-two/powers-of-three boundary that already controls the coefficient-survival side.

It does **not** imply that the two languages are identical or that their intersection is empty.

---

## 8. Exact extension through `q=23`

Using the closed-form congruence and the pruning lemmas, every canonical contracting word was exhausted for

\[
8\le q\le23.
\]

For each solvable cylinder, the exact affine predecessor was reconstructed and checked to satisfy

\[
0<m<x
\]

already at the least nonnegative representative; the strict leading contraction then preserves the inequality on the whole cylinder.

After removing cylinders contained in earlier certified cylinders, the new prefix-free cylinders are:

\[
\begin{array}{c|c|r}
q&r=q-3&\text{new cylinders}\\\hline
8&5&1\\
10&7&5\\
12&9&25\\
13&10&131\\
15&12&580\\
17&14&2,982\\
19&16&16,176\\
20&17&90,550\\
22&19&428,103
\end{array}
\]

At

\[
q=9,11,14,16,18,21,23
\]

there are exactly zero new prefix-free cylinders, as forced by Section 6.

The total number of disjoint certified cylinders is

\[
\boxed{538,553.}
\]

Their exact natural density in the free `k` parameter is

\[
\boxed{
\delta_{23}
=
\frac{561769}{43046721}
\approx0.01305021583409338.}
\]

Thus the finite symbolic coverage rises from the earlier `q<=16` value about `1.098%` to about

\[
\boxed{1.305\%}
\]

through `q<=23`.

Status: **FINITE ONLY.**

No density-one or convergence claim is licensed by this increase.

---

## 9. DSD audit

### SAFE

1. Closed form for `C_w` and `m`.
2. Final integrality iff every reverse `O` is valid.
3. Trailing-`E` pruning.
4. Exact normalized congruence and unique `3^(q-3)` cylinder.
5. `P_q` contraction budget.
6. Beatty nesting theorem: `P_(q+1)-P_q=1` produces no new prefix-free cylinders.
7. At a jump by `2`, a genuinely new word must occupy both newly opened final positions.

### FINITE ONLY

- `538,553` disjoint cylinders through `q=23`;
- density `561769/43046721`;
- the apparent rate at which new-cylinder density changes.

### OPEN

1. Whether the union over all `q` covers every `k`.
2. Whether its density tends to `1`, to a smaller positive limit, or otherwise.
3. Whether every uncovered `k` can be eliminated by a different merge mechanism.
4. Full `COV_1`, and hence global ternary-core coverage.

### PROHIBITED UPGRADES

1. Do not extrapolate the `1.305%` finite coverage.
2. Do not infer that zero-new levels imply stagnation; new cylinders can reappear at the next Beatty jump-by-two.
3. Do not identify this reverse-word Beatty process with the coefficient-survivor Beatty process without an explicit map.
4. Do not restore universal minimal-counterexample coverage from these finite cylinders.

---

## 10. Regression certificate

`collatz/src/cov1_inverse_word_closed_form_q23_certificate.py`

implements the closed-form search and asserts the exact prefix-free counts and density through `q=23`.

---

## 11. Next target

The nesting theorem suggests the next analytic compression:

1. ignore all `q` for which `P_q-P_(q-1)=1` when searching for new coverage;
2. at each jump-by-two level, fix the forced final two `O` positions;
3. derive the induced map from the earlier prefix's normalized defect to the two newly determined base-3 digits of `k`;
4. analyze the complement as a nonstationary `3`-adic automaton driven by the Beatty word of slope `log_2 3`.

If that automaton has no infinite path, `COV_1` closes.  If it has infinite paths, their arithmetic meaning must be audited rather than treated as counterexamples automatically.

# COV-1: eventually-all-odd ghost terminal lemma

Date: 2026-09-06

Status: **SAFE EXACT TERMINAL LEMMA / GLOBAL COV-1 OPEN.**  The companion/direct prefix tree need not become empty at any finite depth: it contains genuine infinite `2`-adic ghost paths.  However, every parity path that is eventually all odd corresponds to a negative rational initial value and therefore cannot represent a positive ordinary integer.  Consequently COV-1 would close if every infinite survivor path could be proved eventually all odd.

---

## 1. Unique all-odd tail

Under the shortcut map

\[
T(n)=\frac{3n+1}{2}
\]

on an odd state, an infinite all-odd tail in `Z_2` must satisfy

\[
x\equiv-1\pmod{2^L}
\]

for every `L`, hence

\[
\boxed{x=-1\in\mathbb Z_2.}
\]

Equivalently, `-1` is the fixed point

\[
\frac{3(-1)+1}{2}=-1.
\]

No positive ordinary integer has this value.

---

## 2. Arbitrary finite prefix followed by an all-odd tail

Let a finite parity prefix `p` have length

\[
H,
\]

odd count

\[
s,
\]

and standard affine constant

\[
C(p),
\]

so that

\[
T^H(N)
=
\frac{3^sN+C(p)}{2^H}.
\]

If every parity bit after this prefix is `1`, then the state at time `H` must be the unique all-odd `2`-adic point `-1`.  Therefore

\[
\frac{3^sN+C(p)}{2^H}=-1,
\]

and hence

\[
\boxed{
N
=-\frac{2^H+C(p)}{3^s}.
}
\]

Because

\[
2^H+C(p)>0,
\]
we have

\[
\boxed{N<0.}
\]

Thus no positive natural number can have an eventually-all-odd infinite shortcut parity sequence.

Status: **SAFE EXACT TERMINAL EXCLUSION.**

---

## 3. The pure all-ones path in `36k+27`

For the unresolved progression

\[
N=36k+27,
\]

the pure all-ones parity path gives

\[
N=-1.
\]

Therefore

\[
36k+27=-1
\]

and

\[
\boxed{
k=-\frac79.}
\]

Since `9` is odd, this is a valid element of `Z_2`, but

\[
\boxed{k\notin\mathbb N_0.}
\]

This is exactly the ghost point already visible from the congruences

\[
36k+27\equiv-1\pmod{2^L}
\]

at every finite depth.

---

## 4. Why the all-ones ray is never companion-compatible

Take

\[
w=1^h.
\]

Then

\[
s=h,
\qquad
C(w)=3^h-2^h.
\]

A companion has length

\[
h+3
\]

and must contain

\[
h+2
\]

ones, so it has exactly one zero.  Let that zero occur at position

\[
j\in\{0,\ldots,h+2\}.
\]

The companion constant is

\[
\boxed{
C(z)
=3^{h+2}
+2^j3^{h+2-j}
-2^{h+3}.
}
\]

Hence its would-be defect is

\[
\begin{aligned}
D
&=
\frac{C(z)-8C(w)}{3^{h+2}}\\
&=
\boxed{
\frac19+\left(\frac23\right)^j.
}
\end{aligned}
\]

For every integer `j>=0`, this is not an integer.  Therefore

\[
\boxed{
1^h\text{ has no companion at any depth }h.
}
\]

So the companion-prefix tree necessarily has at least this one infinite path; finite-level emptiness is not an appropriate terminal objective.

---

## 5. Correct terminal objective

Let

\[
\mathcal T_h
\]

be the dyadic prefix tree remaining after all currently proved hereditary certificates are removed, for example:

1. uniform forward descent;
2. companion-word smaller merges;
3. any later safe hereditary certificate.

The desired conclusion is **not**

\[
\mathcal T_h=\varnothing
\]

for some finite `h`.

The correct inverse-limit target is

\[
\boxed{
\text{every infinite path in }
\varprojlim\mathcal T_h
\text{ is eventually all odd}.
}
\]

By Section 2, every such path is a negative rational `2`-adic point, so it cannot correspond to any positive natural start.

Therefore the implication

\[
\boxed{
\text{all infinite survivor paths eventually }1
\Longrightarrow
36\mathbb N_0+27\text{ is recursive}
}
\]

is safe.

---

## 6. Known nontrivial ghost rays

The earlier linear-memory audit constructed eventually-one witness families such as

\[
11011011\,1^t
\]

that remain incompatible with the tested reverse-congruence condition for every finite `t`.  This is consistent with the present theorem: an eventually-one infinite ray can survive every finite congruence sieve while still representing only a negative rational `2`-adic value.

Thus such rays must not be mistaken for natural-number counterexamples.

---

## 7. DSD audit

### SAFE

1. `-1` is the unique all-odd infinite `2`-adic tail.
2. A finite prefix followed by all ones has initial value
   \[
   -(2^H+C(p))/3^s<0.
   \]
3. The pure ghost in the `36k+27` parameter is `k=-7/9`.
4. The all-ones ray has no companion at any finite depth.
5. Eventual-all-ones inverse-limit paths can be discarded from positive-natural coverage.

### OPEN

1. Whether every infinite path surviving direct descent and companion certificates is eventually all odd.
2. Whether additional non-eventually-periodic `2`-adic survivor paths exist.
3. Whether such paths, if they exist, can intersect the ordinary natural numbers.
4. Full COV-1.

### PROHIBITED UPGRADES

1. Do not infer COV-1 merely because the obvious all-ones survivor is non-natural.
2. Do not infer that every infinite `2`-adic survivor is eventually periodic.
3. Do not infer emptiness of the natural survivor set from dyadic density decay alone.
4. Do not treat a finite prefix compatible with a ghost ray as evidence for a Collatz counterexample.

---

## 8. Regression certificate

`collatz/src/cov1_eventually_odd_ghost_certificate.py`

checks the all-ones companion obstruction and the negative-rational terminal formula on representative finite prefixes.

---

## 9. Next target

The next structural question is now sharply stated:

> Can the infinite direct/companion survivor tree contain a path with infinitely many zero parity bits?

A useful approach is to classify **minimal companion seeds**.  Since companion certificates are inherited by every common suffix, any path with infinitely many zeroes can survive only if it avoids every minimal seed forever.

If the minimal-seed language can be shown unavoidable for every non-eventually-one binary sequence beginning with `11`, then COV-1 closes without any finite-depth exhaustion.

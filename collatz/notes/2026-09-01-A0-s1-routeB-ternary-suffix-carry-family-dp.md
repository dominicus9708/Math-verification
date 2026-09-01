# A0 s=1 Route-B ternary suffix-carry family DP

## Purpose

The remaining target-family bottleneck after the surplus/dominance reduction is the ternary right-front collision condition.

This note gives an exact family-level recurrence for that condition.  It replaces full parity-word enumeration at fixed bridge resolution `(K,L)` by a right-to-left carry DP on ranked one positions.

It does **not** prove a horizon-independent finite quotient and does **not** prove the Collatz conjecture.

---

## 1. Target-dominance language

Fix a target parity word of length `h` and one-count `q`.

Write its one positions as

\[
a_1<a_2<\cdots<a_q.
\]

For the strict-ballot target class already derived, every candidate has one positions

\[
b_1<b_2<\cdots<b_q,
\qquad
b_r\le a_r.
\]

The ordinary Collatz correction is

\[
C(W)=\sum_{r=1}^q3^{q-r}2^{b_r}.
\]

For target `A` and candidate `B`, define

\[
\Delta=C(A)-C(B)
=\sum_{r=1}^q3^{q-r}\left(2^{a_r}-2^{b_r}\right).
\]

---

## 2. Exact suffix locality

Process ranked one positions from right to left.

For `0 <= t <= q`, define

\[
F_t
=
\sum_{j=0}^{t-1}
3^j\left(2^{a_{q-j}}-2^{b_{q-j}}\right),
\qquad F_0=0.
\]

All unprocessed terms in `Delta` contain at least a factor `3^t`.
Therefore

\[
\boxed{\Delta\equiv F_t\pmod{3^t}}.
\]

Hence

\[
\boxed{3^t\mid\Delta\iff3^t\mid F_t}.
\]

In particular, for `L <= q`, the condition

\[
3^L\mid\Delta
\]

depends only on the last `L` ranked one positions.
The entire earlier prefix family can be counted without expansion.

---

## 3. Carry recurrence

Assume `3^t | F_t` and define

\[
Z_t=F_t/3^t.
\]

Let

\[
A_t=2^{a_{q-t}}-2^{b_{q-t}}.
\]

Then

\[
F_{t+1}
=F_t+3^tA_t
=3^t(Z_t+A_t).
\]

Therefore the next ternary lift is exact:

\[
\boxed{
3^{t+1}\mid\Delta
\iff
Z_t+A_t\equiv0\pmod3
}.
\]

When that condition holds,

\[
\boxed{
Z_{t+1}=(Z_t+A_t)/3
}.
\]

This is the ternary suffix-carry recurrence.

---

## 4. Finite carry quotient at requested resolution

Suppose the final requested ternary resolution is `L`.

At stage `t`, future acceptance depends only on

\[
\boxed{
\bar Z_t=Z_t\pmod{3^{L-t}}.
}
\]

Indeed, if

\[
Z_t\equiv Z'_t\pmod{3^{L-t}},
\]

then after adding the same next atom `A_t`, divisibility by `3` agrees, and after division by `3` the successor carries agree modulo

\[
3^{L-t-1}.
\]

Thus the exact observation state is triangular:

\[
\bar Z_0\in\mathbf Z/3^L\mathbf Z,
\quad
\bar Z_1\in\mathbf Z/3^{L-1}\mathbf Z,
\quad\ldots\quad,
\bar Z_L\in\mathbf Z/1\mathbf Z.
\]

The initial state is always

\[
\bar Z_0=0.
\]

This is a finite quotient for every fixed `L`.
It is not yet a horizon-independent quotient because the initial modulus grows with `L`.

---

## 5. Case `L > q`

After all `q` ranked one positions have been processed,

\[
F_q=\Delta.
\]

If `3^q | Delta`, then

\[
Z_q=\Delta/3^q.
\]

The remaining condition is simply

\[
\boxed{
3^{L-q}\mid Z_q.
}
\]

Thus the same recurrence handles arbitrary `L`, not only `L <= q`.

---

## 6. Dyadic coordinate becomes a fixed target prefix

Inside the same target-dominance language, the previously derived identity gives, for a non-target candidate,

\[
v_2(\Delta)=b_{r_0},
\]

where `r_0` is the first ranked one moved left from the target.

Therefore

\[
\boxed{
2^K\mid\Delta
\iff
W_{[0,K)}=TH_{[0,K)}.
}
\]

At fixed `(K,L)`, the combined family DP can therefore enforce:

1. exact target-prefix equality through position `K-1`;
2. target dominance for the remaining candidate positions;
3. the ternary suffix-carry recurrence through resolution `L`.

No exact full correction integer is required in the DP state.

---

## 7. Length-18 exact regression

For the threshold target of length 18,

\[
(a_1,\ldots,a_{12})
=(0,1,3,4,6,7,9,11,12,14,15,17).
\]

The target-dominance language contains exactly

\[
\boxed{2652}
\]

candidates, including the target.

At `K=1`, the new family DP gives the numbers of **other** ternary colliders:

```text
L=1   1498
L=2    960
L=3    476
L=4    180
L=5     85
L=6     30
L=7     12
L=8      6
L=9      2
L=10     1
L=11     0
```

These are exactly the survivor counts of the earlier adaptive-decoder regression.

The implementation additionally compares the family DP with direct correction congruence for

\[
1\le K\le7,
\qquad
1\le L\le12,
\]

for 84 `(K,L)` pairs.
All agree.

Source:

`collatz/src/A0_s1_routeB_ternary_suffix_carry_dp_certificate.py`

---

## 8. Family-level consequence

Before this recurrence, a ternary collision query appeared to require the exact correction of every candidate word.

It now factors as

\[
\boxed{
\text{left fixed prefix}
\;\times\;
\text{unexpanded dominance prefix family}
\;\times\;
\text{right ternary carry frontier}.
}
\]

For `L <= q`, only the last `L` ranked one positions participate in the ternary carry.
All earlier positions are counted as one prefix family.

This is an exact family-cover mechanism at fixed observation resolution.

---

## 9. DSD audit

✅ candidate language is defined independently of observation resolution;

✅ dyadic and ternary observation axes remain separate;

✅ right-tail locality is an exact divisibility theorem;

✅ carry transition is exact;

✅ `Z_t mod 3^(L-t)` is sufficient for all remaining ternary decisions;

✅ length-18 survivor counts are reproduced without `2^18` word enumeration;

✅ 84 direct `(K,L)` finite regressions agree;

❌ the number of possible carry states is not yet bounded independently of `L`;

❌ this does not yet close the huge Christoffel/Route-B target family;

❌ no global Collatz claim is made.

---

## 10. Next task

The next reduction is to analyze a single carry transition at remaining precision

\[
m=L-t.
\]

Because `2` generates the unit group modulo `3^m`, the exponent `b` enters the carry only through

\[
b\pmod{2\cdot3^{m-1}}.
\]

The intended next audit is to determine whether the allowed exponent residues and successor carry residues form a bijection, and then combine that structure with the interval/order constraints on candidate one positions.

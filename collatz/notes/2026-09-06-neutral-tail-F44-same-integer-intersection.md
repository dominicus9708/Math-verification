# Neutral Beatty tail intersected with the actual `F_44` same-integer selector family

Date: 2026-09-06

## Status

- **SAFE REDUCTION:** a fixed parity prefix determines one start residue modulo `2^K`, hence one reduced selector residue modulo `2^(K-2)` on the `N=4X+3` core.
- **FINITE EXACT CERTIFICATE:** the canonical neutral Beatty prefix has exactly one `F_44` selector realization through `K=46` and none through `K=47`.
- **SCOPE:** this excludes the particular neutral tail beginning with the canonical six-one entry used in the Gate-B barrier inside `F_44`; it is not yet a theorem excluding every neutral segment entered later after an arbitrary admissible root prefix.

No Collatz proof is claimed.

---

## 1. Why this intersection is different from the bare Sturmian problem

The preceding literature audit showed that the infinite critical Sturmian parity word by itself lies on a known difficult boundary of the 3x+1 conjugacy/periodicity problem.

The DSD program has extra same-integer information.  In the recursively sufficient depth-44 layer,

\[
F_{44}
=
\left\{
4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\}.
\]

Thus one should not ask whether the critical Sturmian word is impossible for an arbitrary 2-adic start.  One can ask the strictly narrower question whether its canonical start residue is represented by the same finite ternary-selector family.

---

## 2. Canonical start residue of a parity prefix

For a length-`K` parity word with `q` odd entries and correction `R_K`,

\[
T^K(N)=\frac{3^qN+R_K}{2^K}.
\]

The word determines a unique starting residue modulo `2^K`:

\[
\boxed{
N_K\equiv -R_K\,3^{-q}\pmod{2^K}.
}
\]

For the neutral word used here,

\[
e_0=\cdots=e_5=1,
\qquad
e_j=b(j+1)-b(j)\quad(j\ge6),
\]

and

\[
q_K=b(K)+2\qquad(K\ge6).
\]

Every member of `F_44` is `3 mod 4`, so write

\[
N=4X+3.
\]

A length-`K` match is therefore equivalent to

\[
X
\equiv
\frac{N_K-3}{4}
\pmod{2^{K-2}}.
\]

Substituting

\[
X=3^{44}+\sum_{i=0}^{43}a_i3^i
\]

gives one exact subset-sum congruence:

\[
\boxed{
\sum_{i=0}^{43}a_i3^i
\equiv
\frac{N_K-3}{4}-3^{44}
\pmod{2^{K-2}}.
}
\]

Status: **SAFE REDUCTION**.

---

## 3. Exact `22+22` meet-in-the-middle

Split the 44 selector digits into

\[
\{0,\ldots,21\}
\quad\text{and}\quad
\{22,\ldots,43\}.
\]

Each half has `2^22=4,194,304` subset sums.

The first half satisfies

\[
\sum_{i=0}^{21}3^i
=
\frac{3^{22}-1}{2}
<2^{34}.
\]

Hence for every certified depth

\[
K\ge36,
\]

the low-half sums are strictly smaller than the modulus

\[
2^{K-2}
\]

and need no modular folding.  Sort these exact low-half sums once.  For every high-half assignment, reduce its sum modulo `2^(K-2)` and binary-search the unique required low-half complement.

This counts selector assignments exactly without enumerating all `2^44` full assignments.

---

## 4. Exact intersection counts

The certified counts are

\[
\boxed{
\begin{array}{c|rrrrrrrrrrrr}
K&36&37&38&39&40&41&42&43&44&45&46&47\\\hline
\#(F_{44}\cap\text{neutral prefix})
&1076&555&277&136&73&30&13&6&4&2&1&0.
\end{array}
}
\]

In particular,

\[
\boxed{
\#I_{46}=1,
\qquad
\#I_{47}=0.
}
\]

Because the prefix cylinders are nested, this proves that no member of the exact `F_44` layer can follow this neutral critical parity tail for 47 steps from the root.

Status: **FINITE EXACT CERTIFICATE**.

---

## 5. The unique depth-46 realization

The unique selector assignment at depth 46 has selector mask

\[
\boxed{11375966551508}
\]

under the convention that bit `i` is the digit `a_i`.

It gives

\[
\boxed{N=5,404,210,161,480,071,189,247.}
\]

The neutral target's canonical residue at depth 46 is

\[
\boxed{N_{46}=32,032,672,256,767\pmod{2^{46}}.}
\]

Direct iteration of the recovered `F_44` integer confirms:

- parity positions `0,...,45` agree with the neutral target;
- the first disagreement is position `46`;
- the neutral target has a Beatty plateau there, so it demands `e_{46}=0`;
- the actual `F_44` integer has `e_{46}=1`.

Thus the unique same-integer realization is forced out of the neutral `d=2` channel at the next bit and moves upward in surplus rather than continuing the critical tail.

---

## 6. DSD interpretation

This is exactly the type of extra cross-channel information that the bare Sturmian conjugacy problem lacks:

\[
\boxed{
\text{critical parity word}
+
\text{same }F_{44}\text{ ternary selector}
\Longrightarrow
\text{finite disappearance at }K=47.
}
\]

So the neutral exceptional channel is **not** an obstruction inside the particular root-aligned `F_44` layer indefinitely.

This materially improves the terminal picture:

1. the bare neutral Sturmian word cannot be dismissed by known conjugacy theory at the critical density;
2. fixed-Q7 reverse potential also cannot kill it pathwise;
3. root-Hensel maximality does not kill it, and its Hensel class is singleton through depth 95;
4. nevertheless, adding the actual `F_44` same-integer selector constraint kills the root-aligned neutral tail by depth 47.

The useful mechanism is therefore **cross-base same-integer incompatibility**, not generic parity-word impossibility.

---

## 7. Scope barrier

The result must not be overextended.

It treats the specific root-aligned neutral word

\[
111111\,\delta_6\delta_7\cdots
\]

which reaches `d=2` at depth 6 and then follows the Beatty boundary exactly.

An arbitrary surviving candidate could in principle enter

\[
d=2
\]

at a later depth after a different root prefix and then begin following `e_j=delta_j`.

Therefore the next theorem target is not

> the neutral channel is closed.

The correct target is:

\[
\boxed{
\text{uniform shifted-neutral incompatibility:}
\quad
\exists L<\infty
\text{ such that every admissible }F_m\text{ root prefix entering }d=2
\text{ loses }e=\delta\text{ within }L\text{ further steps},
}
\]

or a weaker weighted version sufficient for the tail-budget/atom-floor closure.

This is **OPEN**.

---

## 8. Reproducibility

Source:

`collatz/src/neutral_tail_f44_mitm_certificate.cpp`

Build:

```text
g++ -O3 -std=c++17 neutral_tail_f44_mitm_certificate.cpp -o neutral_f44
```

Expected terminal line:

```text
PASS
```

The program verifies the exact count vector `K=36..47`, reconstructs the unique `K=46` selector assignment, verifies its `F_44` value, and directly checks that its first neutral mismatch is parity position 46.

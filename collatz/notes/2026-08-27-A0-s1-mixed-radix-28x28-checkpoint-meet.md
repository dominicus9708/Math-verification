# A0 s=1: shallow 28×28 mixed-radix checkpoint meet

Date: 2026-08-27

Status: **SAFE exact boundary-interface reduction.** This is a finite-address pruning theorem inside the repaired binary `s=1` branch. It does not prove the Collatz conjecture.

## 1. Starting point

The hard renewal checkpoint is an ordinary integer

\[
\boxed{2^{72}<Z<2^{73}}.
\]

The full two-ended exposure theorem used:

- up to 73 dyadic start bits on the tail side;
- up to 47 ternary endpoint digits on the prefix side.

For a meet-in-the-middle test, that much information is not needed before the two sides are joined.

## 2. Twenty-eight dyadic digits from the tail

The first 28 parity symbols of the tail determine the accelerated-Collatz start residue

\[
\boxed{Z\pmod{2^{28}}}.
\]

Because `s=1` is an exact renewal point, the tail is a first-passage ballot path. Exact directed log bounds give the required minimum tail odd counts after steps `k=1,...,28` as

```text
0,1,1,2,3,3,4,5,5,6,6,7,8,8,
9,10,10,11,11,12,13,13,14,15,15,16,17,17.
```

A dynamic count of all binary words satisfying these necessary prefix inequalities gives exactly

\[
\boxed{16,956,950}
\]

28-bit words/residues.

Since

\[
15\cdot16,956,950<2^{28},
\]

this necessary tail prefix family occupies less than

\[
\boxed{\frac1{15}}
\]

of all 28-bit residues.

This is only a necessary 28-step prefix language. It is deliberately **not** promoted to the claim that every such prefix extends to the complete `U`-step first-passage tail.

## 3. Twenty-eight ternary digits from the prefix

The last 28 odd ordinals of the prefix affine correction determine

\[
\boxed{Z\pmod{3^{28}}}.
\]

This is the same endpoint-exposure mechanism used by the 47-trit complete checkpoint theorem, truncated to a shallow exact residue.

No fixed `K mod 3^28` unbounded-Hensel quotient is being introduced. The residue is requested only as a boundary digit of the bounded ordinary checkpoint `Z`.

## 4. CRT singleton theorem

The two moduli are coprime and

\[
2^{28}3^{28}=6^{28}
=6140942214464815497216,
\]

while the allowed checkpoint interval has width

\[
2^{73}-2^{72}=2^{72}
=4722366482869645213696.
\]

Hence

\[
\boxed{2^{28}3^{28}>2^{72}}.
\]

Therefore every pair

\[
\left(Z\bmod2^{28},\ Z\bmod3^{28}\right)
\]

determines one CRT class modulo a modulus larger than the entire checkpoint interval.

Consequently:

\[
\boxed{
\text{each 28-bit/28-trit residue pair has at most one }Z\in(2^{72},2^{73}).
}
\]

The remaining 45 dyadic bits and 19 ternary digits are no longer needed to *identify* a checkpoint candidate. They become exact validation filters on the singleton candidate.

## 5. DSD state interpretation

The state chain is

\[
\boxed{
\begin{aligned}
&\text{tail ballot prefix}
\to Z\bmod2^{28},\\
&\text{prefix endpoint suffix}
\to Z\bmod3^{28},\\
&\text{CRT + ordinary interval}
\to \text{zero or one checkpoint }Z.
\end{aligned}}
\]

This preserves both independently generated boundary descriptions until a mathematically exact join operation.

### SAFE

- finite tail ballot prefix constraints;
- finite ordinary boundary residues;
- CRT composition;
- bounded interval representative test.

### REJECTED

- interpreting a surviving shallow CRT candidate as a full A0 path;
- discarding the remaining ballot/first-passage conditions after the shallow join;
- promoting the 28-trit prefix boundary residue to a global Hensel state quotient.

## 6. Interaction with the 40-bit debit/credit corridor

The companion renewal reduction gives

\[
L_-=3X-Z<2^{40},
\qquad
L_+=3Y-Z<2^{40},
\]

and

\[
|L_+-L_-|<2^{34}.
\]

Thus there are now two exact finite meet coordinates for the same branch:

1. **checkpoint meet** — 28 dyadic + 28 ternary boundary digits identify at most one `Z`;
2. **renewal debit/credit meet** — two `<40`-bit local observables must agree within the physical `<2^34` shift.

The next algorithm should intersect these descriptors rather than choose one and discard the other.

## 7. Next gate

Build a compact digital trie / DAG for

\[
Z\bmod3^{28}
\]

on the prefix `0->0` ballot bridge, join it against the certified 28-bit tail ballot residue set by CRT, and then validate any singleton `Z` with deeper prefix/tail conditions and the 40-bit renewal corridor.

Companion exact certificate:

`collatz/src/A0_s1_mixed_radix_28x28_checkpoint_certificate.py`.

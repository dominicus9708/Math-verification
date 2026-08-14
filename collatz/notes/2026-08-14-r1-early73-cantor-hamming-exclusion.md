# R1 early-73 dyadic/Cantor boundary exclusion

Date: 2026-08-14

Status: **exact finite boundary-intersection certificate + exact first-descent audit**. This uses the current `V_33` verified floor and the isolated R1 mechanical phase. It proves that any remaining minimal-counterexample candidate in the current `m=44` R1 branch must differ from the mechanical first 73 parity bits in at least ten positions. It does not prove Collatz.

## 1. Mechanical early boundary

For the isolated upper-CF R1 resonance, the time-expanded mechanical word begins with four copies of

\[
H_{19}=1101101101011011010.
\]

The first 73 bits are therefore

\[
\boxed{
H_{73}=(H_{19}^4)_{0:73}.
}
\]

They contain 47 odd symbols.

Every remaining member of the `m=44` recursively-sufficient block satisfies

\[
N<2^{73}.
\]

Hence a realized 73-bit parity prefix determines the ordinary start itself:

\[
N=[-3^{-q}R_w]_{2^{73}}.
\]

## 2. Zero-deformation residue

For `w=H_73`, exact affine arithmetic gives

\[
\boxed{
N_{\rm mech,73}
=4,697,939,311,072,332,635,131.
}
\]

Writing

\[
Y=(N_{\rm mech,73}-3)/4
\]

in base three produces multiple digits equal to `2`. Therefore

\[
\boxed{N_{\rm mech,73}\notin F}
\]

for Ansari's recursively-sufficient Cantor core

\[
F=\left\{4\left(3^{44}+\sum_{i=0}^{43}a_i3^i\right)+3:a_i\in\{0,1\}\right\}
\]

in the current layer.

Thus a remaining R1 minimal counterexample must already deform the mechanical parity word before bit 73.

## 3. Exact search space

For time depths `t<=73`, the current large-start first-crossing theorem makes coefficient survival equivalent to the exact Beatty ballot inequalities

\[
q_t\ge\lceil t\log_3 2\rceil.
\]

The mechanical word `H_73` realizes the boundary sequence itself. For an integer `K`, enumerate **every** length-73 parity word satisfying

1. all Beatty ballot inequalities;
2. Hamming distance
   \[
   d_H(w,H_{73})\le K.
   \]

For every leaf compute the exact canonical residue modulo `2^73`, then retain it only if

- it is above the already certified floor
  \[
  V_{33}=4(3^{44}+3^{33})+2;
  \]
- it is at most the maximum `m=44` core member;
- `(N-3)/4` has ternary leading digit 1 at position 44 and all lower digits in `{0,1}`.

All arithmetic is integer/modular; no floating-point test is used in the certificate.

## 4. Exact boundary counts

The complete ballot-prefix counts are

\[
\boxed{
\begin{array}{c|r|r}
K&\#\{\text{ballot prefixes}\}&\#\{\text{Cantor-core starts}\}\\\hline
4&235,873&0\\
6&25,000,400&0\\
7&176,477,240&1\\
8&1,425,446,750&11\\
9&7,900,490,816&57
\end{array}
}
\]

The `K=7` intersection is the single integer

\[
5,851,919,334,513,169,412,511.
\]

At `K=8` there are ten additional starts, and at exact Hamming distance 9 there are 46 additional starts.

Hence the full `K<=9` boundary intersection contains exactly

\[
\boxed{57}
\]

ordinary integers.

## 5. Exact first-descent audit

Every one of the 57 ordinary starts was iterated under

\[
T(n)=\begin{cases}
(3n+1)/2,&n\text{ odd},\\
n/2,&n\text{ even}.
\end{cases}
\]

until it first fell below its own start.

All 57 succeed. The largest first-descent depth among them is

\[
\boxed{211}.
\]

Therefore none of the Cantor-core starts whose first 73 parity bits lie within Hamming distance 9 of the isolated R1 mechanical prefix can be a minimal counterexample.

Thus the remaining R1 branch obeys the exact finite condition

\[
\boxed{
d_H(w_{0:73},H_{73})\ge10.
}
\]

## 6. Immediate defect consequence

Let

- `A` be the number of positions among the first 73 bits where the mechanical bit is `0` and the actual bit is `1`;
- `B` be the number where mechanical is `1` and actual is `0`.

Coefficient survival at time 73 gives

\[
A-B=q_{73}(w)-q_{73}(H_{73})\ge0.
\]

Since

\[
A+B=d_H(w,H_{73})\ge10,
\]

we obtain

\[
\boxed{A\ge5.}
\]

Every such `0->1` position is an odd event occurring strictly earlier than in the mechanical reference; distinct added odd positions correspond to distinct displaced odd ranks. Hence the first-73 boundary contains at least five early displaced/defect odd events.

This is only a local finite defect floor; it is not the global `r_*` theorem. Its significance is that it is forced by the **same ordinary-start address plus Cantor-core condition**, not by an average defect-density estimate.

## 7. Proof-program consequence

The early boundary of the isolated R1 resonance is now constrained simultaneously by

\[
\boxed{
\text{ordinary }73\text{-bit dyadic address}
\cap
\text{Cantor }m=44\text{ address}
\cap
\text{Beatty first-crossing ballot language}.
}
\]

The locally Hensel-resistant mechanical hard phase itself is excluded, as are all deformations through Hamming radius 9.

The next useful target is not a much larger blind Hamming enumeration. It is to convert the forced early deformation into the existing two-ended variables:

1. earliest-defect dyadic valuation;
2. Christoffel displacement/weighted defect;
3. primitive `k=7` gate phase;
4. late Hensel boundary freedom;
5. renewal/headroom inequality.

That conversion may allow whole deformation families beyond radius 9 to be eliminated without enumerating the rapidly growing ballot Hamming ball.
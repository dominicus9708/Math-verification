# A0 s=1: local exposure of the renewal debit/credit addresses

Date: 2026-08-27

Status: **SAFE exact modular-truncation theorem + finite ballot certificate.** This further localizes the repaired `s=1` direct-intersection problem. It does not prove the Collatz conjecture.

## 1. Inputs from the renewal corridor

For

\[
X\xrightarrow{(t_0,j_0)}Z\xrightarrow{(U,P-1)}Y
\]

define

\[
L_-=3X-Z,
\qquad
L_+=3Y-Z.
\]

The companion corridor theorem gives the safe outer bounds

\[
0<L_-<112G<3^{26},
\]

\[
0<L_+<108G<2^{40}.
\]

Thus it is enough to determine `L_- mod 3^26` and `L_+ mod 2^40`; each residue is already the complete ordinary integer.

## 2. Prefix debit needs only the last 26 odd ordinals

Write the exact prefix affine identity

\[
2^{t_0}Z=3^{j_0}X+R_-,
\]

with

\[
R_-=
\sum_{r=1}^{j_0}
3^{j_0-r}2^{a_r}.
\]

Since

\[
L_-=3X-Z,
\]

multiplication by `2^t0` gives

\[
2^{t_0}L_-
=(3\cdot2^{t_0}-3^{j_0})X-R_-.
\]

Reduce modulo `3^26`. Because `j0>26`, the term `3^j0 X` vanishes. Since `2` is a unit modulo `3^26`,

\[
\boxed{
L_-
\equiv
3X-2^{-t_0}R_-
\pmod{3^{26}}.
}
\]

But in `R_- mod 3^26`, every term with

\[
j_0-r\ge26
\]

vanishes. Therefore only

\[
\boxed{
\text{the last 26 prefix odd ordinals}
}
\]

remain.

Since `0<L_-<3^26`, their 26-trit endpoint address together with `X mod 3^26` determines the complete ordinary debit `L_-`.

This is a boundary-exposure theorem, not a fixed-depth Hensel quotient for the full prefix.

## 3. Tail credit needs only the first 40 parity steps

Let

\[
q=P-1
\]

and write

\[
2^U Y=3^qZ+R_+,
\]

\[
R_+=
\sum_{r=1}^{q}
3^{q-r}2^{b_r},
\]

where `b_r` are the local odd time positions of the tail.

Substitute

\[
Z=3Y-L_+.
\]

Then

\[
3^qL_+
=(3^{q+1}-2^U)Y+R_+.
\]

Reduce modulo `2^40`. Since `U>>40`, the `2^U Y` term vanishes, and `3^q` is invertible:

\[
\boxed{
L_+
\equiv
3Y+3^{-q}R_+
\pmod{2^{40}}.
}
\]

Every correction term with

\[
b_r\ge40
\]

is divisible by `2^40` and vanishes. Hence only odd events occurring in

\[
\boxed{
\text{the first 40 tail parity positions}
}
\]

remain.

Since `0<L_+<2^40`, this 40-bit residue is the complete ordinary tail credit.

## 4. Exact necessary tail language at depth 40

The renewal first-passage barrier gives, for `k=1,...,40`, the exact minimum tail odd counts

```text
0,1,1,2,3,3,4,5,5,6,
6,7,8,8,9,10,10,11,11,12,
13,13,14,15,15,16,17,17,18,18,
19,20,20,21,22,22,23,23,24,25.
```

Directed rational logarithm bounds certify every entry.

The number of 40-bit parity words satisfying all these necessary prefix conditions is exactly

\[
\boxed{31,654,570,714}.
\]

Moreover

\[
32\cdot31,654,570,714<2^{40},
\]

so the necessary 40-bit tail boundary language occupies less than

\[
\boxed{\frac1{32}}
\]

of the complete dyadic boundary space.

Again, this is an outer necessary prefix language; no claim is made that every such prefix extends through the full `U`-step first-passage block.

## 5. Revised finite meet

The exact direct-intersection problem can now be represented by two local boundary descriptors:

\[
\boxed{
\begin{aligned}
L_- &= F_-(X\bmod3^{26},\ \text{last 26 prefix odd ordinals}),\\
L_+ &= F_+(Y\bmod2^{40},\ \text{first 40 tail parity bits}),
\end{aligned}}
\]

subject to

\[
\boxed{L_+-L_-=3(Y-X)}.
\]

Thus the long `104`-billion / `9.8`-billion step interiors do not enter the *boundary-value exposure* of the renewal observables. They still enter the proof through the requirement that the short boundary descriptors extend to the complete pre-ballot and tail-first-passage languages.

## 6. DSD audit

### SAFE information reduction

\[
\text{complete physical block}
\to
\text{bounded ordinary }L_\pm
\to
\text{minimal modulus exposing each }L_\pm.
\]

The discarded interior correction terms vanish exactly in the chosen modulus; they are not approximated.

### REJECTED promotion

Do not infer

\[
\text{valid 26-trit / 40-bit local address}
\Longrightarrow
\text{valid full pre/tail block}.
\]

The long ballot-extension condition remains an explicit verification layer.

Do not reinterpret the 26-trit prefix residue as an exact unbounded-horizon Hensel state.

## 7. Next gate

The next exact algorithm should generate the **prefix terminal-26-odd address language** under the `0->0` ballot bridge and meet it against the tail 40-bit ballot address language through the ordinary corridor

\[
L_+-L_-=3(Y-X).
\]

Because the tail language has a small ballot-state automaton but a large raw residue set, the useful target is a digital trie / BDD / Christoffel-DAG representation, not flat enumeration.

Companion certificate:

`collatz/src/A0_s1_local_boundary_address_exposure_certificate.py`.

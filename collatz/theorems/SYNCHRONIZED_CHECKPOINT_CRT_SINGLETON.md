# Synchronized checkpoint CRT singleton

Status: **EXACT / CLOSED for checkpoint exposure**

## Inputs

Use only the independently certified pre-defect corridor inputs

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33},
\]

\[
75\,2^{33}<L_-<112\,2^{33},
\qquad L_-=3X-Z.
\]

No later defect-derived refinement of the `X` bound is used.

Therefore

\[
3\cdot2^{71}-112\cdot2^{33}<Z
<3\left(\frac43 2^{71}+0.478\,2^{33}\right)-75\cdot2^{33}.
\]

Since `Z` is an integer, a SAFE integer corridor is

\[
\boxed{Z_{\min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241},
\]

\[
\boxed{Z_{\max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196}.
\]

Its span is

\[
\boxed{Z_{\max}-Z_{\min}
=2{,}361{,}183{,}241{,}764{,}968{,}152{,}955}.
\]

## Ternary observation from the right-H factor

For the current right factor

\[
s=630{,}138{,}897,
\qquad q_H=397{,}573{,}380,
\]

and modulo `3^28`,

\[
2^s\equiv12{,}596{,}342{,}295{,}887,
\]

\[
C(H_s^*)\equiv2{,}677{,}095{,}985{,}033.
\]

The exact right-H carry observation is

\[
z_H\equiv2^s Z-C(H_s^*)\pmod{3^{28}}.
\]

Because

\[
(2^s)^{-1}\equiv17{,}062{,}811{,}582{,}066\pmod{3^{28}},
\]

this is equivalent to one ternary checkpoint residue

\[
\boxed{
Z\equiv
17{,}062{,}811{,}582{,}066
\left(z_H+2{,}677{,}095{,}985{,}033\right)
\pmod{3^{28}}.
}
\]

The characteristic-word correction uses 0-based bit positions. For ranked one `r>=2`,

\[
a_r=\left\lceil\frac{(r-1)J_0}{R_0}\right\rceil-1.
\]

The `-1` is part of the exact indexing and is audited in the certificate.

## Dyadic observation and CRT

Let the 27-bit dyadic checkpoint observation be

\[
Z\equiv z_2\pmod{2^{27}}.
\]

Since `gcd(2^27,3^28)=1`, the pair `(z_2,z_H)` determines exactly one residue class modulo

\[
M=2^{27}3^{28}
=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608.
\]

Moreover

\[
Z_{\max}-Z_{\min}<M,
\]

with exact margin

\[
M-(Z_{\max}-Z_{\min})
=709{,}287{,}865{,}467{,}439{,}595{,}653>0.
\]

Hence:

\[
\boxed{
\text{each synchronized pair }(z_2,z_H)
\text{ admits at most one integer }Z\in[Z_{\min},Z_{\max}].
}
\]

## Explicit CRT representative

Let

\[
z_3=(2^s)^{-1}(z_H+C(H_s^*))\pmod{3^{28}}.
\]

With

\[
(2^{27})^{-1}\equiv664{,}903{,}189{,}592\pmod{3^{28}},
\]

one representative is

\[
Z_0=z_2+2^{27}
\left((z_3-z_2)\,664{,}903{,}189{,}592\bmod3^{28}\right),
\]

chosen in `[0,M)`.

The SAFE corridor contains either no number congruent to `Z_0 mod M` or exactly one.

## DSD audit

### EXACT / CLOSED

- pre-defect `X`/`L_-` bounds imply the stated SAFE `Z` corridor;
- right-H carry is an affine observation of the same ordinary checkpoint `Z` modulo `3^28`;
- the 27-bit dyadic observation and 28-trit ternary observation combine by ordinary coprime CRT;
- corridor span smaller than the CRT modulus gives singleton exposure.

### REJECTED

Do not reinterpret the result as multiplication of two marginal survival fractions such as

\[
2^{-27}3^{-28}.
\]

The observations are synchronized constraints on the same integer `Z`; no independence assumption appears.

### Scope

This theorem exposes the checkpoint once an admissible synchronized observation pair is supplied. It does **not** prove that a given 14-root source family supplies such a pair, nor does it close Route-B membership.

## Certificate

- `../src/A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`

The finite sample checks in the certificate are implementation guards only.

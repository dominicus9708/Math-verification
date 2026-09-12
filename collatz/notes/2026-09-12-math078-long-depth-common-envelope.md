# MATH-078 — long-depth out-of-sample common-envelope bridge

Date: 2026-09-12

Status: `EXACT REPARAMETRIZATION / DEPTH-191 AND 195 REGRESSION PASS / GLOBAL PROOF OPEN`

## 1. Purpose

MATH-072 and MATH-077 extracted `(S,rho)` from depth `<=41` and first-crossing calculations. MATH-078 tests those coordinates against older results that were derived independently and reach much deeper:

1. the forced-OO Beatty-ballot uniform safety certificate through depth 191;
2. the normalized root-credit and first-cell endpoint-q-lock envelope through depth 195.

These older results were not used to derive the common-coordinate identities, so they serve as out-of-sample validation.

The Collatz conjecture and the first universal Farey cell remain `OPEN`.

## 2. Universal fixed-(k,q) correction envelope

The historical normalized root-credit envelope is

\[
E(k,q)
=2^{k-q}\left(1-\left(\frac23\right)^q\right).
\]

Put `d=k-q` and

\[
\rho=\frac{2^k}{3^q}.
\]

Then exactly

\[
\boxed{
E(k,q)=2^d-\rho.
}
\]

MATH-072 gives

\[
S=1+\Sigma_d-\rho.
\]

Using the elementary fixed-`d` root envelope

\[
\Sigma_d\le2^d-1,
\]

gives

\[
\boxed{
S\le2^d-\rho=E(k,q).
}
\]

Thus the quantity historically called the normalized root Hensel-credit envelope is exactly a fixed-`(k,q)` upper envelope for the same normalized correction `S`.

## 3. Depth-195 root-safe transition

The earlier certificate checked the least coefficient-surviving `q` at each depth and proved

\[
E(k,q)<2^{71}
\]

through

\[
\boxed{k=195}.
\]

The first failure of that simple envelope is

\[
\boxed{(k,q)=(196,124)}.
\]

MATH-078 reproduces the same transition using only

\[
S_{\max}=2^d-\rho.
\]

Therefore the old root-credit depth bound and the present common-coordinate envelope are the same inequality.

## 4. Forced-OO Beatty-ballot envelope through depth 191

For starts

\[
N\ge V_0=4\cdot3^{44}+2
\]

with the forced initial `OO` parity, the older depth-191 certificate constructed an exact fixed-`(j,q)` maximum correction numerator

\[
R_{\max}(j,q).
\]

For a subcritical coefficient prefix,

\[
3^q<2^j,
\]

its uniform safety condition was

\[
R_{\max}(j,q)<V_0(2^j-3^q).
\]

Divide by `3^q` and put

\[
S_{\max}^{OO}=R_{\max}/3^q,
\qquad
\rho=2^j/3^q.
\]

Then the condition is exactly

\[
\boxed{
S_{\max}^{OO}<V_0(\rho-1).
}
\]

This is MATH-077's orbit-gap descent condition applied uniformly to the maximum `S` in the whole fixed-`(j,q)` forced-OO family.

The historical certificate proved this through depth 191. At depth 192 its simple worst-case envelope first loses uniformity, with the same exceptional `q=121` reproduced by MATH-078.

The loss at 192 is therefore **not** a failure of the orbit-gap identity. It is a failure of this particular coarse `S_max` envelope to force the inequality uniformly.

## 5. First-cell endpoint q-lock through depth 195

Let

\[
B_0=2^{71},
\qquad
N\in(B_0,\tfrac{1364}{1024}B_0).
\]

The depth-195 envelope gives

\[
S<B_0.
\]

Hence

\[
N+S<\left(\frac{1364}{1024}+1\right)B_0<3B_0.
\]

Suppose two same-depth candidate prefixes have the same endpoint and

\[
q_H=q_L+d,
\qquad d\ge1.
\]

The common-coordinate endpoint relation gives

\[
N_L+S_L=3^d(N_H+S_H).
\]

Since `N_H>B0`, the right side is at least `>3B0`, contradicting the upper bound on the left side. Therefore

\[
\boxed{d=0}
\]

for equal endpoints in the audited candidate window through depth 195.

The general MATH-076 merge credit therefore collapses there to

\[
\boxed{
N_L-N_H=S_H-S_L.
}
\]

This is precisely the old conclusion that, after `q` is locked, the smaller candidate start is the larger normalized-correction representative of its endpoint class.

## 6. Structural consequence

Three historically separate long-depth objects now have one description:

\[
\boxed{
\text{root Hensel-credit envelope}
=\text{an }S\text{-envelope},
}
\]

\[
\boxed{
\text{Beatty-ballot uniform safety}
= S_{\max}<N(\rho-1),
}
\]

\[
\boxed{
\text{endpoint q-lock}
=\text{range separation of }N+S\text{ under multiplication by }3^d.
}
\]

Thus the common `(S,rho)` coordinates survive a substantial out-of-sample extension beyond the depth-41 derivation range.

## 7. Claim boundary

Established:

- exact identity `E(k,q)=2^(k-q)-rho`;
- exact interpretation of `E` as a fixed-layer `S` envelope;
- exact translation of the depth-191 forced-OO test into the orbit-gap inequality;
- exact reproduction of the depth-195 / 196 root-envelope transition;
- exact common-coordinate derivation of the existing endpoint q-lock through depth 195.

Not established:

- a uniformly sufficient `S_max` envelope beyond depth 191;
- global endpoint q-lock;
- global positivity of generalized merge credit;
- first-cell emptiness;
- the Collatz conjecture.

## Reproducibility

`collatz/src/2026_09_12_math078_long_depth_common_envelope_certificate.py`

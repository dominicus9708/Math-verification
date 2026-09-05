# A0 s=1 Route-B — synchronized checkpoint CRT singleton closure

Date: 2026-09-01

## Purpose

Close the remaining checkpoint-exposure seam before applying the two-front machinery to the 14-root family.

The target is not an independent dyadic/ternary density estimate. The target is an exact synchronized arithmetic interface on one ordinary checkpoint integer `Z`.

## Independent upstream corridor

Use only the pre-defect debit/credit corridor chain:

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33},
\]

\[
75\,2^{33}<L_-<112\,2^{33},
\qquad L_-=3X-Z.
\]

Therefore a SAFE integer checkpoint corridor is

\[
Z_{\min}=7{,}083{,}549{,}723{,}342{,}395{,}146{,}241,
\]

\[
Z_{\max}=9{,}444{,}732{,}965{,}107{,}363{,}299{,}196.
\]

The exact span is

\[
2{,}361{,}183{,}241{,}764{,}968{,}152{,}955.
\]

This derivation intentionally does not use the later defect-derived refined `X` bound.

## Right-H ternary synchronization

For the current right H factor,

\[
s=630{,}138{,}897,
\qquad q_H=397{,}573{,}380,
\]

and

\[
z_H\equiv2^sZ-C(H_s^*)\pmod{3^{28}}.
\]

The characteristic correction is recomputed with the exact 0-based ranked-one position

\[
a_r=\left\lceil\frac{(r-1)J_0}{R_0}\right\rceil-1
\]

for `r>=2`. This gives

\[
2^s\bmod3^{28}=12{,}596{,}342{,}295{,}887,
\]

\[
C(H_s^*)\bmod3^{28}=2{,}677{,}095{,}985{,}033,
\]

and

\[
(2^s)^{-1}\bmod3^{28}=17{,}062{,}811{,}582{,}066.
\]

Hence `z_H` determines `Z mod 3^28` exactly.

## Synchronized CRT

Combine this ternary observation with

\[
Z\equiv z_2\pmod{2^{27}}.
\]

The joint modulus is

\[
M=2^{27}3^{28}
=3{,}070{,}471{,}107{,}232{,}407{,}748{,}608.
\]

The corridor span is strictly smaller:

\[
M-(Z_{\max}-Z_{\min})
=709{,}287{,}865{,}467{,}439{,}595{,}653>0.
\]

Therefore each synchronized observation pair `(z2,z_H)` admits **at most one** ordinary checkpoint `Z` in the SAFE corridor.

## DSD audit

### EXACT / CLOSED

- SAFE checkpoint corridor derived from independent pre-defect inputs;
- exact right-H affine observation of `Z mod 3^28`;
- exact 27-bit/28-trit coprime CRT;
- singleton exposure from corridor span `< 2^27*3^28`.

### CERTIFIED ARITHMETIC

The certificate fixes the exact integer endpoints, joint modulus, margin, characteristic correction, and modular inverses.

### REGRESSION ONLY

The finite constructed-Z and generic observation-pair checks are implementation guards only.

### REJECTED

- multiplying marginal dyadic/ternary densities;
- assuming independence between the two observations;
- using the later defect-derived refined `X` bound retroactively to certify this interface;
- interpreting checkpoint singleton exposure as proof that a 14-root family actually reaches that checkpoint.

### OPEN after this closure

The checkpoint-exposure seam is no longer the immediate blocker.

The next active calculation is:

\[
\text{14-root forward }P_{\min}\text{ state}
\quad\Join\quad
\text{right-H synchronized observation/export state}
\]

followed by exact ordinary-checkpoint and remaining membership/tail compatibility tests.

No 14-root family is closed by the CRT theorem alone. Route-B and the Collatz conjecture remain open.

## Files

- `../src/A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`
- `../theorems/SYNCHRONIZED_CHECKPOINT_CRT_SINGLETON.md`

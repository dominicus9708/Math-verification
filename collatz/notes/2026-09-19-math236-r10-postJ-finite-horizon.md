# MATH-236 — sharpened post-J finite horizon for the surviving r=10 branch

Date: 2026-09-19

Status: EXACT HORIZON SHARPENING / 127-BIT ADDRESS / 24 FUTURE ODDS / r=10 OPEN

## 1. Starting point

MATH-235 leaves only coefficient-expanding frozen r=10 factors and proves

R_0<=38.

## 2. Address precision

MATH-228 proves that all future low-paid r=2..10 address decisions are future-complete at precision

P_10(R)=89+R.

Therefore on the MATH-235 survivor set

boxed: P_10<=127 bits.

## 3. Multi-source dyadic horizon

MATH-074/232 imply that every parity/factor refinement that remains multi-source consumes source resolution.

Hence the total future dyadic depth while multiplicity remains unresolved is at most

boxed: H_fut<=38.

## 4. Complete-boundary odd-count horizon

MATH-233 gives for every complete future boundary chain

1/2 < 3^Q_fut / 2^H_fut < 2.

If Q_fut>=25 while H_fut<=38, then

3^Q_fut / 2^H_fut >= 3^25/2^38 > 2

because exactly

3^25 > 2^39.

Contradiction.

Therefore

boxed: Q_fut<=24.

Thus at most 24 complete factors / paid events can occur while the surviving r=10 continuation is still multi-source.

## 5. Updated finite transducer box

After MATH-235 the proof-facing symbolic continuation lies inside

- source resolution 0<=R<=38;
- future total odd count 0<=Q_fut<=24;
- normalized dyadic address precision <=127 bits;
- exact synchronized correction / defect channel;
- emitted r as a first-return tag, not an outer loop.

## Claim boundary

This sharpens the finite state box only. The number of reachable synchronized states and the coefficient-expanding singleton tail remain open.

## MATH-246 SCOPE CORRECTION

MATH-246 SCOPE CORRECTION: this horizon is exact only for the diagnostic subset selected by the local MATH-235 J cut. Because that cut is not a valid original-source closure, this note is not a proof-facing reduction of the full r=10 branch.

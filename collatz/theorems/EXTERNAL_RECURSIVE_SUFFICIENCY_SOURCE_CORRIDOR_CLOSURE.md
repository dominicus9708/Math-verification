# External recursive-sufficiency closure of the current source corridor

Status: **EXACT conditional on published finite-verification dependencies / closes the current source corridor as an external theorem dependency**

Date checked: **2026-09-05**

## Scope

This note compares the independently certified physical source corridor used by
`A0, s=1, Route-B` with the published finite-range Collatz verification bound
obtained by combining:

1. David Bařina's computational verification through `2^71`;
2. Mohammad Ansari's 2025 recursive-sufficiency Proposition 3.2.

The result is a finite-range closure of every ordinary positive source integer
`X` in the current Route-B source corridor.

This is an **external dependency closure**.  It is not counted as an internal
self-contained derivation of the DSD/Route-B bridge.

## 1. Current certified source corridor

The current Route-B physical source satisfies the independently certified SAFE
bounds

\[
2^{71}<X<\frac43 2^{71}+0.478\,2^{33}.
\]

Write the decimal coefficient exactly as

\[
0.478=\frac{239}{500}.
\]

Hence the exact rational upper endpoint is

\[
U_X
=\frac43 2^{71}+\frac{239}{500}2^{33}
=\frac{1180591620718951049199616}{375}.
\]

Since `X` is an integer,

\[
\boxed{X\le 3{,}148{,}244{,}321{,}917{,}202{,}797{,}865.}
\]

The source corridor is inherited from the independently certified pre-defect
physical chain already used by the synchronized-checkpoint theorem.

## 2. Published recursive-sufficiency proposition

Ansari (2025), *Recursive sufficiency for the Collatz conjecture and
computational verification*, Notes on Number Theory and Discrete Mathematics
31(3), 471--480, DOI `10.7546/nntdm.2025.31.3.471-480`, proves the following
finite-range extension mechanism.

For

\[
N_n=2\,3^n+1,
\]

if all integers in `[1,N_n]` satisfy the Collatz conjecture, then all integers
in

\[
(N_n,2N_n]
\]

also satisfy it.

The proof uses a recursively sufficient set `F` for which

\[
(N_n,2N_n]\cap F=\varnothing.
\]

Corollary 2.2 of that paper then propagates verified convergence from `[1,N_n]`
to `[1,2N_n]`.

The phrase "largest known integer" in the published statement is not needed by
the proof kernel for a chosen `N_n`: what is used is that `[1,N_n]` has already
been verified and that the recursively sufficient set has no member in the
interval `(N_n,2N_n]`.

## 3. Specialization to `n=44`

Set

\[
N_{44}=2\,3^{44}+1.
\]

Exactly,

\[
\boxed{N_{44}=1{,}969{,}541{,}804{,}367{,}222{,}465{,}763.}
\]

Bařina's published/project verification includes every positive integer below

\[
2^{71}=2{,}361{,}183{,}241{,}434{,}822{,}606{,}848.
\]

The exact gap is

\[
2^{71}-N_{44}
=391{,}641{,}437{,}067{,}600{,}141{,}085>0.
\]

Therefore `[1,N_44]` is contained in the already verified range.

Ansari's finite-range extension then gives convergence for every positive
integer through

\[
2N_{44}=4\,3^{44}+2.
\]

Exactly,

\[
\boxed{
L_{RS}=4\,3^{44}+2
=3{,}939{,}083{,}608{,}734{,}444{,}931{,}526.
}
\]

Equivalently,

\[
\frac{L_{RS}}{2^{71}}\approx1.66826679929.
\]

## 4. Comparison with the Route-B source upper bound

The exact margin between the recursive-sufficiency finite bound and the current
source upper endpoint is

\[
L_{RS}-U_X
=\frac{296564732556465800122634}{375}>0.
\]

Numerically this margin is approximately

\[
7.90839\times10^{20}.
\]

Therefore

\[
\boxed{U_X<L_{RS}.}
\]

Combining with the current lower bound,

\[
\boxed{
2^{71}<X<U_X<L_{RS}.
}
\]

Hence every ordinary positive source integer `X` represented by the current
`A0,s=1,Route-B` source corridor lies inside the externally established finite
verification range.

## 5. Orbit consequence

If an ordinary positive source integer `X` satisfies the Collatz conjecture,
then its deterministic forward orbit reaches `1`.

Consequently no actual nonconvergent Collatz orbit can contain such an `X` as a
state.  In particular, no current Route-B candidate whose same-orbit provenance
ultimately reduces to an ordinary source integer inside this corridor can be a
genuine counterexample branch.

Therefore, **conditional on accepting the two external published verification
dependencies**, the current physical source corridor is closed without carrying
its source cylinders to the `q=j_0-28` late-activation seam.

## 6. DSD interpretation

This result activates a previously external observable at a much coarser
resolution than the internal source bridge:

- internal route: preserve exact source payload over a very long hypothetical
  Route-B continuation;
- external finite-range route: observe only the ordinary source integer `X` and
  apply an already certified convergence property over the complete containing
  interval.

Once the external finite-range predicate is accepted, every finer internal
Route-B descriptor attached to those same source integers is downstream of a
closed source condition and is no longer required for branch rejection.

This is predicate-relative state elimination, not a claim that the internal
bridge theorem has been constructed.

## 7. Audit classification

### EXACT arithmetic / CLOSED

- `N_44=2*3^44+1`;
- `N_44<2^71`;
- `L_RS=2*N_44=4*3^44+2`;
- exact current source upper endpoint `U_X`;
- `U_X<L_RS` with the stated positive exact margin.

### EXTERNAL THEOREM DEPENDENCY

- Bařina: computational convergence verification through `2^71`;
- Ansari 2025: recursive sufficiency and the interval-extension proposition.

### CONSEQUENCE IF EXTERNAL DEPENDENCIES ARE ACCEPTED

- every current ordinary source `X` satisfies Collatz;
- the current `A0,s=1,Route-B` counterexample source corridor is empty of true
  counterexample sources;
- late-activation/terminal-descriptor/right-H work is unnecessary for rejecting
  this finite Route-B source corridor.

### STILL OPEN INTERNALLY

- a self-contained DSD/source-preserving proof of the late-activation bridge;
- an internally generated terminal-descriptor closure independent of the
  published finite-range result;
- Route-A, `s>=2`, remaining branches, and global branch completeness;
- the global Collatz conjecture.

### REJECTED OVERCLAIMS

- external closure of this finite source corridor -> global Collatz proof;
- Ansari's finite verification extension -> proof for arbitrary integers;
- replacing all internal research with numerical evidence;
- treating an external finite verification theorem as an internally derived DSD
  result.

## References

- D. Bařina, *Improved verification limit for the convergence of the Collatz
  conjecture*, Journal of Supercomputing 81 (2025), Article 810.
- M. Ansari, *Recursive sufficiency for the Collatz conjecture and computational
  verification*, Notes on Number Theory and Discrete Mathematics 31(3) (2025),
  471--480, DOI 10.7546/nntdm.2025.31.3.471-480.

## Certificate

- `../src/A0_s1_external_recursive_sufficiency_source_corridor_closure_certificate.py`

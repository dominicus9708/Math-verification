# G13 height-one full credit bridge and finite-natural zero-lift obstruction

Date: 2026-08-16

Status: **exact constructive full-gate relation + exact phase alignment + exact finite-natural obstruction for the constructed witness**.  This note shows that the G13 same-state arithmetic channel is flexible enough to carry credit `4096 -> 1` while accumulated block-boundary height stays in `{0,1}`.  The constructed relation is nevertheless not attachable to the current R1 ordinary orbit because its canonical G13 start representative has 20024 bits, whereas every actual R1 state at the G13 entrance has fewer than 1612 bits.  This is not a Collatz proof and does not exclude all G13 relations satisfying the finite-natural start condition.

## 1. Exact phase alignment inside the current R1 reference

The isolated R1 mechanical reference begins at time zero with the standard upper mechanical word

\[
m_t=\lceil (t+1)\alpha\rceil-\lceil t\alpha\rceil,
\qquad \alpha=\log_3 2.
\]

Its first length-19 factor is

\[
H_{19}=1101101101011011010.
\]

The first 11-odd type-0 length-19 block begins at block index `81`, hence at

\[
\boxed{t_0=81\cdot19=1539.}
\]

Using the exact rational enclosure

\[
\frac{15601}{24727}<\alpha<\frac{31867}{50508},
\]

the 20026 mechanical bits beginning at time `1539` agree bit-for-bit with the unique G13 factor used in the second-return analysis.  Thus the G13 gate considered here is an internal macro-gate of the current R1 mechanical reference beginning at time 1539; it is not the original time-zero R1 boundary.

## 2. Height-aware block relation state

Split G13 into

\[
20026/19=1054
\]

length-19 blocks.

For a compared pair of local orientations `w,u`, require the same local odd count `q` in each block.  Relative to the mechanical block let the shared accumulated block-boundary height be `H`.  Each local word is admissible when

\[
H+M(w)\ge0,
\qquad
H+M(u)\ge0.
\]

If the mechanical block has odd count `q_*`, then

\[
H'=H+q-q_*.
\]

For an incoming ordinary state difference / predecessor credit `delta`, exact affine concatenation gives the right-boundary difference

\[
\boxed{
\delta'
=\frac{3^q\delta-(R_u-R_w)}{2^{19}}
}
\]

whenever the numerator is a positive multiple of `2^19`.

The finite section studied here imposes

\[
\boxed{H\in\{0,1\}}
\]

at every length-19 block boundary.

## 3. Exact full-G13 witness

Starting from the first open transition-layer parent credit

\[
\boxed{\delta_0=4096,}
\]

a deterministic finite search retaining only low-credit states finds a complete 1054-block witness ending at

\[
\boxed{\delta_{1054}=1.}
\]

The witness is then independently verified without using the beam pruning.

Both global orientations satisfy

\[
\boxed{q=12635}
\]

and their relative mechanical prefix heights never become negative.  At block boundaries the shared height stays in `{0,1}` and returns to zero at the end.

Their full corrections satisfy the exact integer identity

\[
\boxed{
3^{12635}\,4096-(R_u-R_w)=2^{20026}.
}
\]

Equivalently, if the two gate-start integers differ by 4096, then after the whole G13 gate their endpoint integers differ by exactly 1.

The two parity words first differ at zero-based time position `12`, as forced by the 2-adic valuation of the left credit, and their difference persists to the far end of the gate.  The witness therefore realizes the anticipated two-ended mixed-place geometry rather than a short local swap.

## 4. This defeats a purely low-height gate-arithmetic obstruction

The existence of the witness proves that neither

- same local odd count in every 19-bit block,
- global mechanical-prefix survival,
- accumulated block-boundary height at most one,
- nor the integer-credit channel itself

is sufficient to block the G13 repair.

In particular, the earlier transition-band barriers must not be extrapolated into a theorem that all large transition repairs fail.  The full same-state gate fibre contains enough distributed freedom to realize an exact

\[
4096\to1
\]
relation.

This is a negative result for the attempted obstruction strategy, not evidence for a Collatz counterexample.

## 5. Finite-natural start bound at the G13 entrance

Every current R1 candidate satisfies

\[
N<2^{73}.
\]

For the accelerated Collatz map

\[
T(x)=x/2\quad(x\text{ even}),
\qquad
T(x)=(3x+1)/2\quad(x\text{ odd}),
\]
we have for every positive integer

\[
T(x)\le2x.
\]

Therefore the actual R1 orbit state at the G13 entrance obeys the universal bound

\[
\boxed{
x_{1539}<2^{1539}N<2^{1612}.}
\]

Since `1612 < 20026`, any 20026-bit G13 parity word realized by that ordinary state must have canonical start representative

\[
\rho(w)=[-3^{-12635}R_w]_{2^{20026}}
\]
with

\[
\boxed{\rho(w)<2^{1612}.}
\]

This is the exact finite-natural high-dyadic zero-lift condition relevant to the internal G13 gate.

## 6. The constructed witness fails the zero-lift condition

For the explicit `4096 -> 1` witness, exact big-integer evaluation gives

\[
\boxed{\operatorname{bitlen}(\rho(w))=20024,}
\]

and likewise the alternate representative has bit length 20024.

Moreover

\[
\boxed{
\rho(u)-\rho(w)\equiv-4096\pmod{2^{20026}},
}
\]

as required by the exact credit relation.

But

\[
20024>1612,
\]

so this witness cannot be the actual G13 segment of any current R1 ordinary orbit.

Thus the arithmetic relation exists in the 2-adic gate fibre but fails finite-natural stabilization by an enormous margin.

## 7. Correction to a tempting low-73 comparison

Because this G13 gate begins at R1 time 1539 rather than at time zero, its local canonical start representative must **not** be compared directly with the original `m=44` Cantor start `N`.

The correct comparison is

\[
\rho_{G13}=x_{1539},
\]

where `x_1539` is the ordinary orbit state transported from the original start.  The universal bound above supplies a safe necessary condition without conflating the two time origins.

## 8. Revised terminal finite problem

Inside the present height-one/blockwise-same-q section, the next exact question is:

> Does there exist a pair of G13 orientations satisfying global mechanical survival and
> \[
> 3^{12635}\,4096-(R_u-R_w)=2^{20026}\delta,
> \qquad 1\le\delta\le397,
> \]
> while simultaneously
> \[
> [-3^{-12635}R_w]_{2^{20026}}<2^{1612}?
> \]

The unrestricted arithmetic answer is yes (`delta=1`), but the explicit witness fails the finite-natural condition.

This identifies the active channel much more sharply:

\[
\boxed{
\text{G13 same-state relation}
\cap
\text{finite-natural high dyadic zero-lift}
}
\]

rather than another marginal Hensel or transition-magnitude bound.

A stronger R1-specific version should replace the crude `2^1612` headroom by the exact set of ordinary states reachable at time 1539 from the surviving `m=44` start core.

## Reproducibility

Companion constructive search / verifier:

`collatz/src/g13_h1_4096_to_1_bridge_certificate.cpp`

The certificate reconstructs the exact G13 mechanical factor, produces a full relation witness, and verifies the blockwise survival and affine credit identities.  An accompanying zero-lift verifier evaluates the canonical start representative and the R1 time-1539 size bound.
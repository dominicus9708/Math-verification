# MATH-195 — exact phase-gap extension of first-crossing descent through q=67

Date: 2026-09-18

Status: `FINITE EXACT PHASE ENVELOPE / DIRECT r<=21 POST-CLUSTER CROSSINGS CLOSED / GLOBAL CLOSURE OPEN`

## 1. Purpose

MATH-194 gives a purely analytic first-crossing descent theorem for `q<=42` using only the integer gap `2^k-3^q>=1`.

For the current paid-macro target range `r<=21`, the relevant direct post-cluster odd counts extend modestly beyond 42. The phase clock is exact and one-dimensional, so this range can be enlarged without ordinary-source enumeration by auditing only the finite Beatty phase values.

## 2. Exact first-crossing gap

At first coefficient failure,

\[
u=0\xrightarrow{E}-1.
\]

Immediately before the failing even step,

\[
\rho_-=\Omega_q,
\]

and after it

\[
\boxed{\rho_+=2\Omega_q.}
\]

Therefore

\[
\boxed{
\rho_+-1
=2\Omega_q-1
=\frac{2^{q+m(q)+1}-3^q}{3^q}.
}
\]

## 3. Exact phase audit through q=67

For

\[
1\le q\le67,
\]

the exact minimum of `2 Omega_q - 1` occurs at

\[
\boxed{q=41}
\]

and equals

\[
\boxed{
\delta_{67}
:=
\frac{420491770248316829}{36472996377170786403}
>0.
}
\]

This is an audit of 67 exact rational phase values, not an ordinary-start enumeration.

Hence every first coefficient failure with `q<=67` satisfies

\[
\boxed{\rho-1\ge\delta_{67}.}
\]

## 4. Correction envelope

MATH-053 gives

\[
S<\frac q3.
\]

Thus throughout the same range,

\[
\boxed{S<\frac{67}{3}.}
\]

For every unresolved first-cell source above the frozen floor,

\[
N\ge2^{71}.
\]

Therefore MATH-080 gives

\[
\mathfrak D
=S-N(\rho-1)
<
\frac{67}{3}-2^{71}\delta_{67}.
\]

The exact positive margin in the opposite direction is

\[
2^{71}\delta_{67}-\frac{67}{3}
=
\frac{
992858121071587431976002615113194815325
}{
36472996377170786403
}
>0.
\]

Consequently

\[
\boxed{
q\le67
\quad\Longrightarrow\quad
\mathfrak D<0
}
\]

at first coefficient failure.

## 5. Relation to the r=1..21 paid range

The canonical MATH-058R paid-exit source generator over prefix lengths `1..72` has

\[
\boxed{q_0\le46.}
\]

A paid cluster with target count

\[
1\le r\le21
\]

adds exactly `r` odd events. Hence immediately after one such cluster,

\[
q\le q_0+r\le46+21=67.
\]

Therefore, if the next coefficient-boundary event is the first global coefficient failure, it is automatically a strict descent:

\[
\boxed{
\text{canonical paid exit}
+\text{one }r\le21\text{ cluster}
+\text{direct first failure}
\Longrightarrow
\text{strict descent}.
}
\]

In particular this covers the analogous direct post-cluster crossing for `r=10`, where `q<=56`.

## 6. Structural consequence

Any still-open low-paid path after MATH-195 cannot be difficult merely because one `r<=21` cluster ends near the coefficient boundary and immediately crosses it.

The remaining obstruction must include additional boundary-surviving structure before the first failure, such as another legal handoff / phase segment / carried-address transition.

This aligns with MATH-193: the hard core is a transported carry/address chain, not an isolated paid cluster.

## 7. Audit boundary

Established:

- exact first-crossing phase gap through `q=67`;
- exact minimum at `q=41`;
- source-independent strict descent at every first coefficient failure with `q<=67` above `2^71`;
- direct post-cluster first crossings for the canonical `r<=21` paid-exit range are closed.

Not established:

- that every `r<=21` branch crosses immediately after one cluster;
- closure of chains containing additional boundary-surviving handoffs;
- arbitrary-q first-crossing descent;
- any new paid-count layer closure by itself;
- first-cell emptiness;
- the Collatz conjecture.

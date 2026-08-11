# Nonperiodic hard core and critical-balance reduction

Date: 2026-08-11

Status: **exact internal reduction plus external comparison**. The internal theorem below is proved from the survivor-ceiling identities. The final section notes agreement with known 2-adic parity-density work but does not make that external theorem a hidden assumption of the internal derivation.

## 1. Odd-event state

For an odd-event trajectory define

\[
\lambda_q:=\frac{2^{A_q}}{3^q},
\]

where `A_q` is the total number of accelerated Collatz steps used in the first `q` odd-to-odd events.

Let

\[
c_q:=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}}.
\]

Since

\[
\lambda_i=\frac{2^{A_i}}{3^i},
\]

we have the exact cumulative identity

\[
\boxed{
c_q=\frac13\sum_{i=0}^{q-1}\lambda_i.}
\]

Write

\[
\boxed{
S_q:=\sum_{i=0}^{q-1}\lambda_i,
}
\]

so `c_q=S_q/3`.

At a contracting event endpoint `lambda_q>1`, the current survival ceiling is

\[
\boxed{
C_q=\frac{c_q}{\lambda_q-1}
=\frac{S_q}{3(\lambda_q-1)}.
}
\]

---

## 2. Nonperiodic survivor with infinitely many contracting endpoints

Assume a fixed positive integer `n>=2` has an infinite no-first-descent orbit and is nonperiodic.

Suppose

\[
\lambda_q>1
\]

for infinitely many event indices `q`.

The ceiling-gap stabilization theorem shows that along those contracting event indices,

\[
\boxed{C_q\to+\infty.}
\]

Therefore

\[
\frac{\lambda_q-1}{S_q}
=
\frac{1}{3C_q}
\longrightarrow0
\]

along every contracting subsequence.

Since there are infinitely many terms with `lambda_q>1`, the positive partial sums satisfy

\[
\boxed{S_q\to+\infty.}
\]

For noncontracting event indices, `lambda_q<=1`, so

\[
0<\frac{\lambda_q}{S_q}\le\frac1{S_q}\to0.
\]

For contracting indices,

\[
\frac{\lambda_q}{S_q}
=
\frac{\lambda_q-1}{S_q}+\frac1{S_q}
\to0.
\]

Hence over the full event sequence,

\[
\boxed{
\frac{\lambda_q}{S_q}\to0.
}
\]

---

## 3. Subexponential cumulative multiplicative scale

Because

\[
S_{q+1}=S_q+\lambda_q,
\]

we obtain

\[
\boxed{
\frac{S_{q+1}}{S_q}
=1+\frac{\lambda_q}{S_q}
\to1.
}
\]

Therefore

\[
\log\frac{S_{q+1}}{S_q}\to0.
\]

By Cesaro averaging of the telescoping logarithms,

\[
\boxed{
\frac{\log S_q}{q}\to0.
}
\]

Since `lambda_q/S_q->0`, eventually `lambda_q<=S_q`, so

\[
\limsup_{q\to\infty}
\frac{\log\lambda_q}{q}
\le0.
\]

On the other hand, `lambda_q>1` for infinitely many `q`, so along that subsequence

\[
\frac{\log\lambda_q}{q}>0.
\]

Consequently

\[
\boxed{
\limsup_{q\to\infty}
\frac{\log\lambda_q}{q}
=0.
}
\]

---

## 4. Critical event-density boundary

Using

\[
\log\lambda_q
=A_q\log2-q\log3,
\]

we obtain

\[
\boxed{
\limsup_{q\to\infty}
\frac{A_q}{q}
=
\frac{\log3}{\log2}
=
\log_2 3.
}
\]

Equivalently, since `A_q/q>0`,

\[
\boxed{
\liminf_{q\to\infty}
\frac{q}{A_q}
=
\frac{\log2}{\log3}.
}
\]

Thus a nonperiodic infinite survivor that returns to the contracting side infinitely often is forced asymptotically onto the exact powers-of-two/powers-of-three balance boundary.

This conclusion is not a finite computation.

---

## 5. Two nonperiodic hard cores

A hypothetical nonperiodic positive-integer counterexample must therefore lie in one of two classes.

### Hard core I: eventual coefficient survival

There are only finitely many event indices with

\[
\lambda_q>1.
\]

Equivalently, from some point onward

\[
\boxed{\lambda_q\le1}
\]

at every odd-event checkpoint. In accelerated-prefix language the multiplicative coefficient `3^q/2^{A_q}` stays at least one thereafter.

This sector cannot be removed by survival ceilings alone because no new finite contracting ceiling is created at those checkpoints.

### Hard core II: recurrent contraction with critical asymptotic balance

There are infinitely many event indices with

\[
\lambda_q>1,
\]

and necessarily

\[
\boxed{
\limsup A_q/q=\log_2 3.
}
\]

This sector repeatedly crosses the multiplicative boundary but can do so only with asymptotically zero exponential drift.

---

## 6. Formation condition common to both hard cores

A finite positive-integer counterexample also has an eventually constant formation floor. Equivalently, its formation-increment bits satisfy

\[
\boxed{
\beta_k=0
\quad\text{for all sufficiently large accelerated depths }k.
}
\]

Thus the remaining global task can be stated as exclusion of

\[
\boxed{
\text{eventually-zero formation increments}
+
\text{Hard core I or Hard core II}.
}
\]

This is substantially narrower than arbitrary parity or macroblock enumeration.

---

## 7. Macroblock discrepancy form

For maximal macroblocks write `(h_i,d_i)` and define

\[
\alpha:=\log_2\frac32.
\]

The block multiplier of `lambda` is

\[
M_i
=\frac{2^{h_i+d_i}}{3^{h_i}}
=2^{d_i-\alpha h_i}.
\]

Define the signed block discrepancy

\[
\boxed{
e_i:=d_i-\alpha h_i.}
\]

Then

\[
\boxed{
\log_2\frac{\lambda_m}{\lambda_0}
=\sum_{i<m}e_i.
}
\]

The critical debit

\[
d_i=\lceil\alpha h_i\rceil
\]

has `0<e_i<1`; subcritical blocks have `e_i<0`; supercritical blocks have `e_i>1`.

Hence Hard core II is equivalently a zero-asymptotic-drift regime for this irrational-slope discrepancy walk, together with the exact headroom and formation constraints.

---

## 8. External comparison

López and Stoll, *The 3x+1 Periodicity Conjecture in R* (arXiv:2101.12747), Theorem 1, state a stronger global boundary restriction for divergent rational 2-adic trajectories: the lower limiting proportion of odd entries in the accelerated parity vector must equal

\[
\frac{\log2}{\log3}.
\]

A positive integer is a rational 2-adic integer, so their theorem points to the same critical density for any noncyclic positive-integer counterexample.

The internal theorem in Sections 2--4 is narrower in hypothesis (it assumes infinitely many contracting odd-event checkpoints) but is derived directly from the present ceiling identities. The external result is therefore best used as corroboration or, after independent proof audit, as an optional stronger filter.

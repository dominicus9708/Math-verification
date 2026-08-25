# DSD coefficient-ratio bridge: signed skew, Beatty surplus, and adaptive reverse scale

Date: 2026-08-25

## Status

Exact structural bridge plus an exact audit on the current coefficient-record integer.

No Collatz proof is claimed.

## 1. One scalar behind the two coordinates

For the accelerated odd-event map

\[
x_{q+1}=\frac{3x_q+1}{2^{v_q}},
\qquad
A_q=\sum_{j<q}v_j,
\]

define the coefficient ratio

\[
\boxed{
\Theta_q=\frac{3^q}{2^{A_q}}.
}
\]

The signed-skew coordinate already used in the aperiodic hard core is

\[
s_q=\lfloor q\log_2 3\rfloor-A_q.
\]

Since

\[
\lfloor q\log_2 3\rfloor=\lfloor\log_2 3^q\rfloor,
\]

we have the exact identity

\[
\boxed{
s_q=\lfloor\log_2\Theta_q\rfloor.
}
\]

Thus `s_q` is simply the base-2 integer scale of the coefficient ratio.

## 2. Beatty surplus is the base-3 scale of the same ratio

For ordinary binary-step depth `B`, define

\[
b(B)=\min\{r:3^r\ge2^B\}
=\lceil B\log_3 2\rceil.
\]

At the completed odd-event time `B=A_q`, the Beatty surplus is

\[
d_{A_q}=q-b(A_q).
\]

Because `q` is an integer,

\[
q-\lceil A_q\log_3 2\rceil
=
\lfloor q-A_q\log_3 2\rfloor.
\]

Therefore

\[
\boxed{
d_{A_q}=\lfloor\log_3\Theta_q\rfloor.
}
\]

The two DSD coordinates are not independent obstacles.  They are the same coefficient ratio viewed at two logarithmic resolutions:

\[
\boxed{
\Theta_q
\longrightarrow
\begin{cases}
s_q=\lfloor\log_2\Theta_q\rfloor,\\[3pt]
d_{A_q}=\lfloor\log_3\Theta_q\rfloor.
\end{cases}
}
\]

## 3. Exact audit on the current record integer

For

\[
N=12,235,060,455,
\]

the coefficient stopping time is

\[
\tau_c(N)=547.
\]

The canonical formation/lift reconstruction gives:

- the last nonzero lift digit is `t_26`;
- after 27 completed odd events, at `A=34`, the canonical representative becomes exactly

\[
\rho=N;
\]

- every audited later lift digit is zero.

Thus this integer is already in the `eventual-zero lift` regime very early in the long coefficient-surviving excursion.

Nevertheless, before the coefficient crossing the completed-event bridge reaches

\[
\boxed{
(q,A,s,d)=(227,345,14,9).
}
\]

So eventual-zero lift digits do **not** force the coefficient ratio to stay in a bounded low-surplus strip by any immediate local argument.

At the crossing event,

\[
(q,A)=(345,547),
\]

and the bridge gives

\[
\boxed{s=d=-1},
\]

matching the failure of coefficient survival.

## 4. Exact adaptive reverse scale

A reverse code at ternary depth `Q` has coefficient potential at most

\[
\Lambda_{Q,\max}=\left(\frac32\right)^Q.
\]

For a completed forward event with coefficient ratio `Theta_q`, define the least resolution at which reverse contraction is even coefficient-wise possible:

\[
\boxed{
Q_{\rm need}(q)
=
\min\left\{Q:\left(\frac32\right)^Q>\Theta_q\right\}.
}
\]

The accompanying certificate evaluates this with exact integer arithmetic through the current record crossing.

In the eventual-zero-lift region it reaches

\[
\boxed{Q_{\rm need}=26}
\]

at the same high excursion

\[
(q,A,s,d)=(227,345,14,9).
\]

This is consistent with the earlier asymptotic scaling

\[
Q\gtrsim\frac{\log3}{\log(3/2)}d
\approx2.70951129135d,
\]

but the exact `Q_need` is sharper because it uses the full Beatty phase contained in `Theta_q`, not only the integer surplus `d`.

## 5. Consequence for the aperiodic hard core

The previous finite-support lift-digit target and the newer Beatty-surplus target can now be written on one chain:

\[
\boxed{
\text{eventual-zero lift}
\longrightarrow
\Theta_q
\longrightarrow
(s_q,d_{A_q})
\longrightarrow
Q_{\rm need}(q).
}
\]

The remaining problem is no longer to relate the two coordinates.  That relation is exact.

The remaining arithmetic question is whether the **actual endpoint residue** at a usable adaptive resolution admits a reverse code whose potential exceeds `Theta_q`.

Equivalently, the unresolved step is transversality between

1. the coefficient scale `Theta_q`, and
2. the ternary endpoint residue controlling the available reverse codes.

## 6. Scope

This bridge does not exclude an aperiodic positive integer path.

In particular, the current record example proves that one must not infer

> eventual zero lift digits imply bounded signed skew / bounded Beatty surplus.

The bridge instead removes a duplicated coordinate from the proof architecture and turns the next question into a single coefficient-ratio versus residue problem.

## 7. Reproducibility

Source:

`collatz/src/dsd_theta_skew_surplus_bridge_certificate.py`

Expected final line:

`PASS`

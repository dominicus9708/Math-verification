# A0 packed-suffix surplus envelope

Date: 2026-08-27

Status: **SAFE STRUCTURAL LEMMA + exact arithmetic certificate.** This note continues the DSD parallel audit. It does not prove the Collatz conjecture.

## 1. Ordered-position formulation

For a first coefficient crossing at

\[
(A_0,Q_0)=(114208327604,72057431991),
\]

let

\[
\tau_1<\tau_2<\cdots<\tau_{Q_0}
\]

be the one-indexed odd-event positions.

With

\[
\alpha=\log_3 2,
\]

the global mechanical envelope positions are

\[
\boxed{
n_j=\left\lfloor\frac{j-1}{\alpha}\right\rfloor+1.}
\]

Global coefficient survival through every proper prefix is equivalent to

\[
\boxed{\tau_j\le n_j\quad(1\le j\le Q_0).}
\]

Because the normalized correction

\[
S=\sum_{j=1}^{Q_0}\frac{2^{\tau_j-1}}{3^j}
\]

is strictly increasing in every ordered position, maximizing `S` under any additional checkpoint constraint is a coordinatewise latest-position problem.

## 2. Checkpoint surplus as a capacity constraint

Put

\[
t_0=10J_0,
\qquad
j_0=10R_0+1.
\]

The mechanical word has exactly `j0` odd events by `t0`.

Suppose instead the actual word has

\[
q_{t_0}=10R_0+s=j_0+r,
\qquad r=s-1\ge0.
\]

Define

\[
K=j_0+r.
\]

The condition `q_(t0)=K` means

\[
\tau_K\le t_0.
\]

Strict ordering then forces, for every `j<=K`,

\[
\tau_j\le t_0-(K-j).
\]

Combining this with the global deadline `tau_j<=n_j` gives

\[
\boxed{
\tau_j\le p_j(r):=
\min\{n_j,\ t_0-K+j\}
\qquad(j\le K).
}
\]

For `j>K` there is no additional checkpoint restriction, so only `tau_j<=n_j` remains.

## 3. Exact constrained mechanical envelope

Both sequences

\[
n_j
\quad\text{and}\quad
t_0-K+j
\]

increase by at least one per ordinal.  Hence `p_j(r)` is itself strictly increasing.

Also `n_(K+1)>t0`, so the sequence

\[
\boxed{
\tau_j^*(r)=
\begin{cases}
p_j(r),&j\le K,\\
n_j,&j>K
\end{cases}
}
\]

is globally strictly increasing and is feasible.

Since every feasible word is coordinatewise bounded by this sequence, it is the unique correction-maximizing word at fixed checkpoint surplus.

Therefore the huge shifted-tail optimization collapses to the explicit ordered-position envelope

\[
\boxed{
S_r^*=\sum_{j\le K}\frac{2^{p_j(r)-1}}{3^j}
+\sum_{j>K}\frac{2^{n_j-1}}{3^j}.
}
\]

No `O(U)` tail DP is required.

## 4. The shifted U tail is not a new independent word

For `j>K`, the constrained envelope uses exactly the original global mechanical position `n_j`.

Thus the phase-shifted `(U,P-s)` tail is simply the continuation of the global mechanical envelope after ordinal `K`.

All correction loss caused by the checkpoint surplus is localized in a **packed suffix before the checkpoint**.

This sharpens the previous DSD chain:

\[
\boxed{
\text{surplus formation}
\to
\text{checkpoint capacity constraint}
\to
\text{packed pre-checkpoint suffix}
\to
\text{unchanged mechanical tail continuation}.
}
\]

The `U` tail does not introduce a second independent combinatorial state.

## 5. Which odd ordinals are packed?

Set

\[
\beta:=\frac1\alpha-1
=\log_2(3/2).
\]

The mechanical deadline satisfies the exact identity

\[
\boxed{
n_j-j=\lfloor (j-1)\beta\rfloor.}
\]

Write

\[
c=t_0-j_0.
\]

An ordinal `j<=K` is shifted by the surplus constraint exactly when

\[
n_j>t_0-K+j,
\]

i.e.

\[
\boxed{
\lfloor(j-1)\beta\rfloor>c-r.
}
\]

Because `n_j-j` is nondecreasing, the shifted ordinals form one contiguous suffix

\[
\boxed{
j_*(r),j_*(r)+1,\ldots,K.}
\]

Let its length be

\[
m(r)=K-j_*(r)+1.
\]

This is the exact **packed-suffix length**.

## 6. Lower bound for the packed-suffix length

From the baseline relation at `j0` and the threshold shift by `r`, one obtains

\[
\boxed{
m(r)\ge r+\left\lfloor\frac{r-1}{\beta}\right\rfloor
\qquad(r\ge1).}
\]

Exact logarithmic bounds certify

\[
\beta<\frac{117}{200}.
\]

Therefore

\[
\boxed{
 m(r)
\ge
 r+\left\lfloor\frac{200(r-1)}{117}\right\rfloor.
}
\]

Asymptotically this is approximately

\[
m(r)\gtrsim2.7094r.
\]

So one additional checkpoint odd event does not move only one mechanical odd ordinal.  The finite capacity of the checkpoint forces a longer suffix of previously placed odd events to pack leftward as well.

## 7. Stronger correction-budget tax

Every original mechanical contribution obeys

\[
\frac{2^{n_j-1}}{3^j}>\frac16.
\]

For a shifted ordinal in the packed suffix, its new deadline position is

\[
p_j=j+c-r.
\]

At the first shifted ordinal the defining inequality for `j_*` gives its new contribution strictly below `1/6`.

Each subsequent packed contribution is exactly `2/3` times the preceding one, so the total new contribution of the entire packed suffix is less than

\[
\frac{1/6}{1-2/3}=\frac12.
\]

The original contribution of the `m(r)` shifted ordinals is greater than `m(r)/6`.

Hence the exact constrained envelope loses at least

\[
\boxed{
L(r):=S_{\rm mech}-S_r^*
>
\frac{m(r)}6-\frac12.
}
\]

Combining with the explicit count bound gives

\[
\boxed{
L(r)
>
\frac16\left(
 r+\left\lfloor\frac{200(r-1)}{117}\right\rfloor
\right)-\frac12.
}
\]

This improves the previous coarse tax slope from approximately `r/6` to approximately

\[
0.4516r.
\]

## 8. Endpoint consequence

Let

\[
G=2^{33}.
\]

The unrestricted mechanical A0 gap-credit ceiling remains

\[
a_A/G\approx0.50220738937.
\]

For checkpoint surplus `r=s-1>=1`, the stronger envelope gives

\[
\boxed{
 d'-d
<
a_A-C_A L(r),
\qquad
C_A=3^{Q_0}/2^{A_0}<1.
}
\]

At the maximal coefficient-wise surplus

\[
s=P,
\qquad r=P-1,
\]

the exact arithmetic certificate gives

\[
m(r)>1.67\times10^{10},
\]

\[
L(r)>0.325G,
\]

and therefore

\[
\boxed{
 d'-d<0.177G.
}
\]

So the largest-surplus A0 envelope has less than 36% of the unrestricted A0 gap-credit allowance.

## 9. DSD audit result

The structural state can now be compressed further:

\[
\boxed{
(\text{gap band},\text{resonance scale},r)
}
\]

with deterministic derived quantities

\[
K(r),\quad j_*(r),\quad m(r),\quad L(r).
\]

No separate high-dimensional `U`-tail state is needed at the envelope level.

### SAFE

- exact checkpoint-capacity envelope `p_j(r)`;
- unique correction-maximizing ordered-position word at fixed surplus;
- shifted U-tail continuation equals the original global mechanical continuation after ordinal `K`;
- shifted ordinals form one contiguous packed suffix;
- exact identity `n_j-j=floor((j-1) beta)`;
- packed-count and packed-loss lower bounds;
- strengthened surplus-dependent A0 credit ceiling.

### OPEN

- the envelope still permits positive A0 gap credit for all coefficient-wise possible surplus classes;
- therefore surplus packing alone does not close the A0 branch;
- the next step is to combine `L(r)` with the resonance activation ladder and ask which surplus classes can coexist with repeated avoidance of each activated `mJ0` first-crossing gate.

Companion certificate:

`collatz/src/A0_packed_suffix_surplus_envelope_certificate.py`

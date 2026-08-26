# A0 as ten J0 blocks plus an upper recovery tail

Date: 2026-08-27

Status: **SAFE STRUCTURAL LEMMA + exact rational certificate.** No ternary selector entry theorem and no repeated-local pullback is used. This does not prove Collatz.

## 1. Exact Euclidean decomposition of the promoted resonance

The promoted lower resonance is

\[
(A_0,Q_0)
=(114208327604,72057431991),
\]

and the previous lower convergent is

\[
(J_0,R_0)
=(10439860591,6586818670).
\]

The continued-fraction coefficient `10` appears arithmetically as

\[
\boxed{
(A_0,Q_0)=10(J_0,R_0)+(U,P),
}
\]

where

\[
\boxed{
(U,P)=(9809721694,6189245291).
}
\]

The residual pair lies on the opposite side of

\[
\alpha=\log_3 2.
\]

More precisely,

\[
R_0/J_0<\alpha<P/U,
\]

and the exact logarithmic phase defects are

\[
\delta_J:=J_0\ln2-R_0\ln3>0,
\]

\[
\delta_U:=P\ln3-U\ln2>0,
\]

\[
\delta_A:=A_0\ln2-Q_0\ln3>0.
\]

They satisfy the exact identity

\[
\boxed{
\delta_A=10\delta_J-\delta_U.
}
\]

Thus the exceptionally small `A0` lower defect is literally the remainder after ten copies of the earlier lower defect are almost cancelled by one opposite-sided upper block.

## 2. Every A0 first crossing carries a surplus token through the ten J0 checkpoints

Let a parity trajectory have its first coefficient crossing at `A0/Q0`.
Then every proper prefix is coefficient-surviving.

For each

\[
1\le m\le10,
\]

we have

\[
0<m(\alpha J_0-R_0)<1,
\]

so

\[
\left\lceil\alpha mJ_0\right\rceil=mR_0+1.
\]

Therefore the odd count at every checkpoint obeys

\[
\boxed{
q_{mJ_0}\ge mR_0+1.
}
\]

Define the checkpoint surplus

\[
s_m:=q_{mJ_0}-mR_0.
\]

Then

\[
\boxed{s_m\ge1\qquad(1\le m\le10).}
\]

In particular put

\[
s:=s_{10}\ge1.
\]

Since the full `A0` block contains exactly `Q0` odd events, the terminal `U`-block contains exactly

\[
\boxed{
q_{\rm tail}=P-s.
}
\]

odd events.

The integer `s` is therefore transported from a positive prefix surplus into an equal terminal deficit.

## 3. The terminal U-block is necessarily coefficient-subcritical

The opposite-sided residual pair satisfies

\[
P-1<\alpha U<P.
\]

Since `s>=1`,

\[
q_{\rm tail}=P-s\le P-1<\alpha U.
\]

Hence

\[
\boxed{
3^{q_{\rm tail}}<2^U.
}
\]

So every `A0` first-crossing word contains a terminal block of length

\[
U=9.81\times10^9
\]

whose aggregate coefficient is strictly contracting.

Consequently, when the terminal block is viewed from its own local start, it contains a local first coefficient crossing at some depth at most `U`, and

\[
U<J_0.
\]

This local crossing is not yet a contradiction, because its local start can lie far above the global minimal root `N`.  Its role is structural: an `A0` return cannot be an undifferentiated 114-billion-step object; it necessarily factors into a large supercritical excursion followed by a shorter subcritical recovery channel.

## 4. Exact coefficient cancellation of the transported surplus

At the tenth checkpoint the prefix aggregate coefficient has logarithm

\[
\log C_{\rm pre}
=s\ln3-10\delta_J.
\]

The terminal block has logarithm

\[
\log C_{\rm tail}
=\delta_U-s\ln3.
\]

Since

\[
10\delta_J<\ln3,
\qquad
0<\delta_U<\ln3,
\]

we obtain for every `s>=1`

\[
\boxed{C_{\rm pre}>1,}
\]

\[
\boxed{C_{\rm tail}<1.}
\]

and their product is independent of `s`:

\[
\begin{aligned}
\log(C_{\rm pre}C_{\rm tail})
&=\delta_U-10\delta_J\\
&=-\delta_A.
\end{aligned}
\]

Thus

\[
\boxed{
C_{\rm pre}C_{\rm tail}
=\frac{3^{Q_0}}{2^{A_0}}<1.
}
\]

The surplus token cancels exactly in the aggregate coefficient.

This is a genuine conserved-channel description:

\[
\boxed{
+s\text{ prefix surplus}
\longleftrightarrow
-s\text{ terminal deficit}.
}
\]

## 5. The internal excursion is macroscopically large

For the smallest possible surplus `s=1`,

\[
C_{\rm pre}
=3e^{-10\delta_J}
>2.99.
\]

For larger `s`, the prefix factor is larger by an additional factor of `3` per surplus unit.

Therefore, ignoring the positive affine correction only strengthens the lower bound:

\[
\boxed{
T^{10J_0}(X)>2.99X
}
\]

for every local start `X` whose first coefficient crossing is at `A0`.

So an `A0` near-return necessarily contains an internal excursion to almost three times its local starting magnitude before the upper-tail recovery brings the coefficient backbone back toward the root scale.

This is important for the current branch: repeated `A0` returns cannot remain uniformly near `N` throughout their interior even when their endpoints remain in a narrow gap strip.

## 6. Relation to the activation ladder

The previous activation theorem found

\[
k_m=5m-3
\]

for the first coarse gap level at which the lower multiple `mJ0` can cease to be automatically forbidden.

The present decomposition explains why `J0` is the natural repeated lower clock inside `A0`: the promoted resonance itself contains ten exact `J0` denominator blocks before the opposite-sided recovery tail.

The two structures should therefore be treated together:

\[
\boxed{
\text{gap activation ladder}
\quad+\quad
\text{ten-checkpoint surplus transport}.
}
\]

The remaining A0-dominant branch is no longer just “many A0 returns”.  Each such return must:

1. survive all ten internal `mJ0` coefficient checkpoints;
2. carry a positive integer surplus `s` through the tenth checkpoint;
3. create an amplification by at least `2.99` in the coefficient backbone;
4. place exactly `P-s` odd events in the terminal upper block;
5. use that terminal block to absorb the same surplus and end with the tiny global lower defect `delta_A`.

## 7. Next exact target

The natural next target is now the terminal recovery channel:

> bound the affine correction available to the `U,P-s` terminal block as a function of the transported surplus `s`, and compare it with the amount required to return from the `>2.99X` checkpoint excursion to an endpoint `N+d'` in the certified gap strip.

If the required recovery correction exceeds the mechanical/unconstrained maximum for every `s`, the A0-dominant branch closes.  If not, the surviving `s` values give a much smaller finite/macro-state language for the next audit.

Companion certificate:

`collatz/src/A0_ten_J0_upper_tail_surplus_certificate.py`

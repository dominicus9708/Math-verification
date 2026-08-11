# Subcritical-block 3-adic core address

Date: 2026-08-11

Status: **exact local arithmetic theorem for maximal subcritical blocks**. It supplies a genuine 3-adic endpoint/core attribute, but finite concatenations remain locally realizable by CRT; therefore it is not by itself a global exclusion theorem.

## 1. Block recurrence

For one maximal block write

\[
X=2^hK-1,
\qquad
X'=2^{h'}K'-1,
\]

with `K,K'` odd and

\[
X'=\frac{3^hK-1}{2^d}.
\]

Equivalently,

\[
\boxed{
2^{d+h'}K'
=3^hK+2^d-1.
}
\]

Assume the block is subcritical:

\[
\boxed{d<h\log_2(3/2).}
\]

Since `log_2(3/2)<1`,

\[
\boxed{d<h.}
\]

## 2. Exact 3-adic valuation of the next odd core

Taking `v_3` of the recurrence, the term `3^hK` has 3-adic valuation at least `h`.

For `d` odd,

\[
2^d-1\not\equiv0\pmod3,
\]

so

\[
\boxed{v_3(2^d-1)=0.}
\]

For `d` even, LTE gives

\[
\boxed{
v_3(2^d-1)=1+v_3(d).
}
\]

In either case

\[
v_3(2^d-1)\le d<h.
\]

Therefore the two summands on the right have unequal 3-adic valuations, and the lower one is exactly the valuation of the sum. Since powers of two are 3-adic units,

\[
\boxed{
v_3(K')
=v_3(2^d-1).
}
\]

Thus

\[
\boxed{
v_3(K')
=
\begin{cases}
0,&d\text{ odd},\\[1mm]
1+v_3(d),&d\text{ even}.
\end{cases}
}
\]

The 3-adic valuation of the next odd core is completely determined by the current debit depth `d`; it is independent of `K`, `h'`, and the magnitude of the orbit state.

## 3. Full 3-adic residue modulo `3^h`

Reduce the exact recurrence modulo `3^h`:

\[
2^{d+h'}K'
\equiv
2^d-1
\pmod{3^h}.
\]

Because `2` is invertible modulo powers of `3`,

\[
\boxed{
K'
\equiv
2^{-(d+h')}(2^d-1)
\pmod{3^h}.
}
\]

Hence a subcritical block of credit depth `h` fixes the next odd core to one exact residue class modulo `3^h`.

This is a genuine endpoint/core condition in the 3-adic direction, distinct from the 2-adic start-formation condition.

## 4. Next-block 2-adic condition

If the following maximal block has parameters `(h',d')`, exact debit valuation gives

\[
v_2(3^{h'}K'-1)=d'.
\]

Equivalently,

\[
\boxed{
K'
\equiv
3^{-h'}(1+2^{d'})
\pmod{2^{d'+1}}.
}
\]

Therefore a two-block concatenation places `K'` simultaneously in

\[
\boxed{
\begin{cases}
K'\equiv2^{-(d+h')}(2^d-1)\pmod{3^h},\\[1mm]
K'\equiv3^{-h'}(1+2^{d'})\pmod{2^{d'+1}}.
\end{cases}
}
\]

## 5. Why finite local concatenation is not enough

The moduli

\[
3^h
\quad\text{and}\quad
2^{d'+1}
\]

are coprime. Hence the Chinese remainder theorem combines the two conditions into one residue class modulo

\[
\boxed{3^h2^{d'+1}.}
\]

Thus the mixed 2-adic/3-adic condition does not generally make a finite block pair impossible.

This is consistent with the global parity-prefix principle: finite exact local patterns typically remain realizable by an arithmetic progression, even when their formation class becomes very thin.

Therefore repeatedly adding finite congruence conditions would return to the growing-prefix dilemma.

## 6. Global role in Mode I

The useful content is not finite impossibility but **formation-floor growth**.

In the diffuse long-block Mode I hard core, `h` becomes large in odd-event-weighted density. Therefore the next odd core is repeatedly forced into residue classes modulo increasingly large powers `3^h`, while simultaneously satisfying the next block's dyadic valuation class.

A complete Mode I theorem must exploit this mixed-place thinning to prove that the least positive ordinary-integer representative of the nested exact block state cannot remain bounded.

Equivalently, the target is still

\[
\boxed{
\mu_I(R)\to\infty,
}
\]

but the state available for proving this now includes an exact 3-adic core address in addition to the 2-adic formation address and the Archimedean block-product bounds.

# MATH-219 — local 73-bit source-recovery register after singletonization

Date: 2026-09-19

Status: EXACT AUXILIARY REGRESSION / REDUNDANT AFTER MATH-091 SINGLETON CHILD / NOT MAINLINE

## 1. Purpose

MATH-218 proves that every remaining low-paid singleton hard path accumulates enough parity bits to identify its current boundary anchor after at most 15 dangerous macros, and after at most 3 dangerous r=10 macros.

The proof-facing executor must do this without violating the synchronized-origin rule of MATH-188.

Therefore two source coordinates are kept distinct:

1. the global synchronized source state, rooted at the original first-cell integer \(N\);
2. a temporary local parity register rooted at the boundary anchor \(Y\) where singletonization occurs.

The local register is used only to recover \(Y\) exactly. It does not replace the global correction/defect/Hensel origin.

## 2. Local parity correction recurrence

At the singleton boundary initialize

\[
\widehat K=0,\qquad
\widehat Q=0,\qquad
\widehat C=0.
\]

For each actual shortcut parity bit \(b\in\{0,1\}\), update

\[
\boxed{
\widehat K'=\widehat K+1,
\qquad
\widehat Q'=\widehat Q+b,
}
\]

and

\[
\boxed{
\widehat C'
=
3^b\widehat C+b2^{\widehat K}.
}
\]

Then after \(\widehat K\) local steps,

\[
\boxed{
T^{\widehat K}(Y)
=
\frac{3^{\widehat Q}Y+\widehat C}{2^{\widehat K}}.
}
\]

This is exactly the standard MATH-187 correction recurrence, but in an explicitly auxiliary local coordinate.

## 3. Canonical local source residue

The local parity prefix determines

\[
\boxed{
\widehat A_{\widehat K}
=
\left(
-\widehat C\,3^{-\widehat Q}
\right)
\bmod2^{\widehat K}.
}
\]

Every ordinary integer realizing the local parity prefix satisfies

\[
Y\equiv\widehat A_{\widehat K}\pmod{2^{\widehat K}}.
\]

## 4. Exact recovery at 73 bits

MATH-057 gives

\[
0<Y<2^{73}.
\]

Therefore at

\[
\widehat K=73
\]

we have

\[
\boxed{
Y=\widehat A_{73}
}
\]

for every realizable positive boundary state.

If

\[
\widehat A_{73}=0,
\]

there is no positive \(Y<2^{73}\) realizing the prefix.

Thus the local source register never needs more than 73 source-address bits.

## 5. Stronger hard-window gate

Let

\[
B_{\rm ext}
\]

be the externally certified convergence floor used by the project. At minimum,

\[
B_{\rm ext}\ge2^{71}.
\]

Let

\[
Y_{\max}
=
\left\lfloor
2\left(1364\cdot2^{61}+\frac{q_0}{3}\right)
\right\rfloor
\]

with the strict endpoint convention inherited from MATH-057/058.

At source recovery, a still-hard state must satisfy

\[
\boxed{
B_{\rm ext}<\widehat A_{73}\le Y_{\max}.
}
\]

Otherwise:

- \(\widehat A_{73}\le B_{\rm ext}\): the boundary anchor is already in the verified convergence region;
- \(\widehat A_{73}>Y_{\max}\): the local symbolic prefix is incompatible with the first-cell boundary-anchor bound.

This is one integer interval test.

## 6. Relation to emitted paid counts

The register advances one bit per actual shortcut step and does not care which paid count is eventually emitted.

MATH-218 supplies only a lower bound on how quickly dangerous macros fill it:

\[
\sum_i W(r_i)\ge73
\Longrightarrow
\text{recovery}.
\]

Therefore the same register handles every mixture of \(r=2,\ldots,10\).

For r=10 alone:

\[
3W(10)=87>73,
\]

so no symbolic lineage can pass three dangerous r=10 macros without triggering exact local-source recovery.

## 7. State separation audit

The following coordinates must not be identified:

\[
(\widehat K,\widehat Q,\widehat C)
\ne
(k,q,C)_{\rm global}.
\]

The local register may be reset at singletonization because it answers only the question

> which boundary integer \(Y\) realizes this local parity prefix?

The global synchronized coordinates answer different questions:

- first-cell source identity;
- global correction penalty;
- Hensel translation;
- terminal defect relative to the original source.

No proof credit is double-counted between the two channels.

## 8. Executor consequence

After MATH-217, the remaining theorem-facing path may be implemented as

\[
\boxed{
\text{global MATH-187/209 state}
\times
\text{local 73-bit recovery register}
\times
\text{MATH-215 carry/regeneration state}.
}
\]

The local register has only three outcomes:

1. not yet saturated;
2. saturated to an exact boundary integer inside the hard window;
3. closed/incompatible at saturation.

There is no AP-source index after singletonization.

## 9. Claim boundary

Established:

- exact auxiliary local correction recurrence;
- exact source residue formula;
- exact boundary integer recovery at 73 bits;
- exact separation from the synchronized global source channel;
- one hard-window test at saturation.

Not established:

- that no recovered boundary integer lies in the hard window;
- that every recovered hard integer descends without direct continuation;
- closure of r=10;
- first-cell emptiness;
- the Collatz conjecture.


## Mainline disposition

This register remains a valid parity-vector reconstruction identity, but it is redundant in the current r=10 mainline. After MATH-186 singletonization, MATH-091 already stores the exact child intercept B' and M'=1, so the ordinary boundary integer is known immediately as Y=B'. The global synchronized state should therefore use that exact singleton anchor rather than wait for a 73-bit local reconstruction.

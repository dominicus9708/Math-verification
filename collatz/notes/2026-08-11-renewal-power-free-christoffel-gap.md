# Renewal power-free theorem and quantitative Christoffel gap

Date: 2026-08-11

Status: **exact renewal structural theorem + quantitative consequence of Fernández–Ibáñez transposition monotonicity**. This narrows the continued-fraction multiple branch but does not yet exclude it.

## 1. Renewal words are primitive

Let a renewal-floor segment have exact parity word `w` and send an odd renewal floor `N` to the next renewal floor `N'>N`.

Assume for contradiction that

\[
\boxed{w=u^s,\qquad s>1.}
\]

Let the affine map induced by the shorter word `u` be

\[
G(x)=a x+b,
\qquad a>0,
\qquad b>0.
\]

Then the full renewal map is `G^s`, and

\[
G^s(N)=N'>N.
\]

If `a>=1`, then `G(x)>x` for every positive `x`, so

\[
N<G(N)<G^2(N)<\cdots<G^s(N)=N'.
\]

If `0<a<1`, let `C=b/(1-a)` be the positive fixed point. The inequality `G^s(N)>N` forces `N<C`; hence again

\[
N<G(N)<G^2(N)<\cdots<G^s(N)=N'.
\]

Because `w=u^s` and the renewal word starts at an odd state, every copy boundary begins the same parity word `u`; therefore each `G^k(N)`, `1<=k<s`, is an odd exact block-start state.

But a renewal-floor segment has the defining property that every interior block start is strictly larger than the next renewal floor `N'`.

Thus `G^k(N)<N'` is impossible.

Therefore

\[
\boxed{\text{every renewal-floor parity word is primitive under concatenation}.}
\]

## 2. Consequence for non-coprime Christoffel parameters

Let the aggregate accelerated length be `A` and the odd count be `H`. If

\[
\gcd(A,H)=s>1,
\]

write

\[
A=sA_0,
\qquad H=sH_0.
\]

The Christoffel definition

\[
d_i=\left\lceil\frac{iH}{A}\right\rceil-\left\lceil\frac{(i-1)H}{A}\right\rceil
\]

depends only on the reduced slope `H_0/A_0`, and satisfies

\[
d_{i+A_0}=d_i.
\]

Hence

\[
\boxed{
w_{A,H}^{\rm chr}=(w_{A_0,H_0}^{\rm chr})^s.}
\]

Thus the Christoffel extremal equality word is forbidden as a renewal word whenever `s>1`.

This applies in particular to a continued-fraction multiple layer

\[
(H,D)=(sq,sp),
\qquad A=s(p+q),
\qquad s>1.
\]

## 3. Exact transposition increment

Fernández–Ibáñez prove that a local transposition `10 -> 01` strictly increases their correction functional `C`.

If the swapped `1` occurs at position `j` and there are `r` ones strictly to the right of the swapped pair, the exact increment is

\[
\boxed{\Delta C=2^{j-1}3^r.}
\]

Their construction transforms a suitable minimum-position rotation `d^c` of any word into the Christoffel word by such transpositions.

Suppose the rotation class is not Christoffel. Then at least one one, say the `k`th one, must move to its Christoffel position

\[
i_k^{\rm chr}=\left\lfloor\frac{(k-1)A}{H}\right\rfloor+1.
\]

During its final transposition into that position, `j=i_k^{chr}-1` and exactly `H-k` ones lie to the right. Hence that one transposition contributes

\[
\Delta C
=2^{i_k^{\rm chr}-2}3^{H-k}.
\]

Assume the aggregate word is supercritical,

\[
\rho:=\frac AH>\log_2 3.
\]

Using

\[
\left\lfloor(k-1)\rho\right\rfloor-1
\ge (k-1)\rho-2,
\]

we obtain

\[
\begin{aligned}
\Delta C
&\ge 2^{(k-1)\rho-2}3^{H-k}\\
&>\frac14\,3^{k-1}3^{H-k}\\
&=\frac{3^H}{12}.
\end{aligned}
\]

Therefore every non-Christoffel rotation class in the supercritical regime obeys

\[
\boxed{
C_{\min}^{\rm chr}-C_{\min}(w)
\ge\frac{3^H}{12}.
}
\]

## 4. Renewal-shadow consequence

For a supercritical renewal word set

\[
Z:=2^A-3^H>0,
\qquad
\Delta:=A-H\log_2 3>0.
\]

Its positive rational shadow minimum is

\[
C=\frac{C_{\min}(w)}{Z}.
\]

The Christoffel extremal bound gives

\[
\frac{C_{\min}^{\rm chr}}{Z}
\le
\frac{1}{2^{A/H}-3}.
\]

If the renewal word is not Christoffel, the quantitative gap yields

\[
\boxed{
C
\le
\frac{1}{2^{A/H}-3}
-
\frac{1}{12(2^\Delta-1)}.
}
\]

Since a renewal shadow also satisfies

\[
C=N'+\frac{g}{2^\Delta-1},
\qquad g=N'-N,
\]

we obtain the strengthened non-Christoffel renewal inequality

\[
\boxed{
N'
+
\frac{g+1/12}{2^\Delta-1}
\le
\frac{1}{2^{A/H}-3}.
}
\]

For every continued-fraction multiple layer with `s>1`, this strict form applies automatically because the Christoffel equality word is a forbidden power.

## 5. Scope

The additional `1/12` in the normalized shadow-distance term is not by itself an exclusion theorem. Its structural value is that the full Christoffel extremum is unavailable on every nonprimitive continued-fraction multiple layer.

Thus the residual economical renewal language splits into:

1. primitive (`s=1`) Christoffel-compatible layers, where equality may still be possible;
2. multiple (`s>1`) layers, where every renewal word is quantitatively separated from the Christoffel extremum.

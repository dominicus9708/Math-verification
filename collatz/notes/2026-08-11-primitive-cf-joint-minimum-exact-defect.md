# Primitive upper-CF renewal words are joint minima with exact Christoffel defect

Date: 2026-08-11

Status: **exact refinement of the primitive-CF renewal branch**. It combines the first-coefficient-crossing theorem with the continued-fraction best-approximation property to show that the genuine renewal rotation is simultaneously the rational-shadow `C_min` rotation and a minimum-position (`mu`) rotation. Consequently the Fernández–Ibáñez transposition defect becomes an exact identity in the actual renewal coordinates.

## 1. Setup

Let a genuine aggregate-supercritical renewal word have primitive upper-convergent counts `(A,H)` for

\[
\gamma:=\log_2 3.
\]

Put

\[
\delta:=A-\gamma H>0.
\]

Let the actual renewal rotation be

\[
w=(d_1,\ldots,d_A).
\]

The earlier renewal-shadow theorem implies that this rotation realizes the minimum positive rational shadow state, hence

\[
\boxed{C(w)=C_{\min}(w).}
\]

## 2. Proper suffix slope is strictly larger than the total slope

Let a proper suffix have length `A_s` and odd count `H_s`.

If `H_s>0`, the suffix maps a larger rational shadow state down to the minimum shadow state, so its affine coefficient is less than `1`:

\[
\frac{3^{H_s}}{2^{A_s}}<1.
\]

Thus

\[
\delta_s:=A_s-\gamma H_s>0.
\]

Because `A/H` is a continued-fraction convergent of `gamma` and `0<H_s<H`, the best-approximation-of-the-second-kind property gives

\[
\boxed{\delta_s>\delta.}
\]

Therefore

\[
\frac{A_s}{H_s}-\gamma
=\frac{\delta_s}{H_s}
>
\frac{\delta}{H}
=
\frac AH-\gamma,
\]

so

\[
\boxed{
\frac{A_s}{H_s}>\frac AH
}
\]

and equivalently

\[
\boxed{
\frac{H_s}{A_s}<\frac HA.
}
\]

If `H_s=0`, this density inequality is automatic.

Hence every proper suffix has one-density strictly below the global one-density.

## 3. Tail-density condition is equivalent to minimum position among rotations

Let

\[
S(w):=\sum_{i=1}^A i\,d_i
\]

be the unnormalized one-position sum.

Rotate the first `k` symbols to the end. Let `H_s` be the number of ones in the suffix of length `A-k`. Then the number of ones in the first `k` positions is `H-H_s`, and the position-sum change under the rotation is

\[
\begin{aligned}
S(\tau^k w)-S(w)
&=(A-k)(H-H_s)-kH_s\\
&=A(H-H_s)-kH.
\end{aligned}
\]

The suffix-density inequality

\[
\frac{H_s}{A-k}\le\frac HA
\]

is exactly

\[
A(H-H_s)-kH\ge0.
\]

Therefore

\[
\boxed{
S(\tau^k w)\ge S(w)
\qquad\forall k.
}
\]

Thus the actual renewal rotation is a minimum-position rotation in the sense used by Fernández–Ibáñez:

\[
\boxed{w=d^c.}
\]

For the primitive upper-CF renewal branch, the renewal start is therefore simultaneously

\[
\boxed{
C\text{-minimal and }\mu\text{-minimal in its rotation class}.
}
\]

## 4. Direct Christoffel position comparison in renewal coordinates

Let the actual one positions be

\[
i_1<\cdots<i_H,
\]

and the Christoffel positions at the same `(A,H)` be

\[
\boxed{
i_k^{\rm chr}
=
\left\lfloor\frac{(k-1)A}{H}\right\rfloor+1.}
\]

Fernández–Ibáñez's position comparison now applies directly to the actual renewal word:

\[
\boxed{i_k\le i_k^{\rm chr}\qquad(1\le k\le H).}
\]

Define the exact left-displacement vector

\[
\boxed{s_k:=i_k^{\rm chr}-i_k\ge0.}
\]

Thus every primitive upper-CF renewal word is obtained from the Christoffel extremizer by moving some of its ones to the left while preserving their order.

## 5. Exact defect identity

Moving the `k`th one from `i_k` to `i_k^{chr}` by adjacent `10 -> 01` transpositions increases the Collatz correction by

\[
3^{H-k}2^{i_k-1}(2^{s_k}-1).
\]

Because the actual renewal rotation is itself the `C_min` rotation, no inequality through a different mean-minimizing rotation is needed. Hence

\[
\boxed{
\mathcal E(w)
:=C_{\min}^{\rm chr}-C_{\min}(w)
=
\sum_{k=1}^H
3^{H-k}2^{i_k-1}(2^{s_k}-1).
}
\]

Equivalently,

\[
\boxed{
\mathcal E(w)
=
\sum_{k:s_k>0}
3^{H-k}2^{i_k^{\rm chr}-1}(1-2^{-s_k}).
}
\]

Since `A/H>log_2 3`,

\[
2^{i_k^{\rm chr}-1}>\frac12 3^{k-1},
\]

and therefore the normalized exact defect obeys

\[
\boxed{
\frac{\mathcal E(w)}{3^H}
>
\frac16
\sum_{k=1}^H(1-2^{-s_k}).
}
\]

## 6. Exact residual parameterization

The primitive upper-CF supercritical renewal hard core may now be parameterized by the integer vector

\[
\boxed{(s_1,\ldots,s_H),\qquad s_k\ge0,}
\]

subject simultaneously to:

1. strict ordering of actual positions `i_k=i_k^{chr}-s_k`;
2. the exact renewal parity word;
3. the exact defect identity above;
4. the renewal defect upper budget;
5. the tiny gap channel
   \[
   g\equiv g_w\pmod{2^A-3^H},
   \qquad
   0<g<H/3,
   \qquad
   g\equiv0\pmod4;
   \]
6. the fixed-word integer shadow window;
7. nonperiodicity.

This is materially smaller than the unrestricted binary-word search space.

## 7. Relation to the square-prefix theorem

The exact Christoffel vector is

\[
(s_1,\ldots,s_H)=(0,\ldots,0),
\]

and that branch has already been reduced to a finite initial audit by the square-prefix formation theorem.

Therefore any infinite residual primitive-CF branch must have at least one positive displacement `s_k` at every sufficiently large convergent. The next target is to show that any such nonzero displacement vector is incompatible with the tiny renewal gap residue/window conditions for all sufficiently large convergents.

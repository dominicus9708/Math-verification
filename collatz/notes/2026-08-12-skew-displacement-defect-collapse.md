# Exact collapse of signed skew, Christoffel displacement, and weighted defect

Date: 2026-08-12

Status: **exact coordinate-identification theorem for the primitive upper-CF first-crossing branch**. It proves that the odd-event signed-skew path, the Christoffel one-position displacement staircase, and the newly introduced weighted defect mass are the same arithmetic object in three coordinate systems. It reduces the remaining near-Christoffel problem to a sparse-support tri-place problem. This does not prove Collatz.

## 1. Setup

Put

\[
\gamma:=\log_2 3,
\qquad
\alpha:=\gamma-1=\log_2(3/2).
\]

Let `(A,H)` be a primitive upper continued-fraction convergent in the `A/H` coordinate:

\[
\frac AH>\gamma.
\]

Consider a genuine renewal segment whose full parity word is the first coefficient crossing and has total parity length `A` and odd count `H`.

At odd-event resolution define

\[
a_q:=\sum_{j<q}v_j,
\qquad 0\le q\le H,
\]

so `a_H=A`. For every proper odd-event prefix first-coefficient survival gives

\[
q\gamma-a_q>0,
\qquad 1\le q<H.
\]

Define the nonnegative signed-skew height

\[
\boxed{
h_q:=\lfloor q\gamma\rfloor-a_q
=\lfloor q\alpha\rfloor-(a_q-q),
\qquad 0\le q<H.
}
\]

At the full upper crossing,

\[
A=\lceil H\gamma\rceil,
\]

so it is convenient to set

\[
\boxed{h_H=-1.}
\]

## 2. Convergent floor-lock lemma

For every integer

\[
0\le q<H,
\]

one has

\[
\boxed{
\left\lfloor\frac{qA}{H}\right\rfloor
=
\lfloor q\gamma\rfloor.
}
\]

Proof. Suppose for some `0<q<H` the left side were larger. Then there would be an integer `m` satisfying

\[
q\gamma<m\le\frac{qA}{H}.
\]

Hence

\[
0<m-q\gamma
\le q\left(\frac AH-\gamma\right)
< H\left(\frac AH-\gamma\right)
=A-H\gamma.
\]

But `A/H` is a convergent of `gamma`, so the best-approximation-of-the-second-kind property forbids a denominator `q<H` with

\[
|m-q\gamma|<|A-H\gamma|.
\]

Contradiction.

Thus the Christoffel and irrational Beatty floors are exactly locked throughout every proper odd-event index.

## 3. Position displacement equals signed skew

Let the actual one positions in the parity word be

\[
i_1<i_2<\cdots<i_H.
\]

Because the first odd symbol is at position `1` and `a_q` parity steps have elapsed before the `(q+1)`st odd symbol,

\[
\boxed{i_{q+1}=a_q+1.}
\]

The ceiling Christoffel positions at the same `(A,H)` are

\[
\boxed{
i_{q+1}^{\rm chr}
=
\left\lfloor\frac{qA}{H}\right\rfloor+1.
}
\]

By the floor-lock lemma,

\[
i_{q+1}^{\rm chr}
=\lfloor q\gamma\rfloor+1.
\]

Therefore the Christoffel left-displacement coordinate is exactly

\[
\boxed{
s_{q+1}
:=i_{q+1}^{\rm chr}-i_{q+1}
=h_q,
\qquad 0\le q<H.
}
\]

Thus the previously separate coordinates are identical after the index shift

\[
\boxed{s_{q+1}=h_q.}
\]

## 4. Exact reference correction

The normalized affine correction of the actual word is

\[
\boxed{
c
=
\sum_{q=0}^{H-1}
\frac{2^{a_q}}{3^{q+1}}.
}
\]

For the exact Christoffel reference, `a_q^{chr}=floor(q gamma)` for every proper prefix, so

\[
\begin{aligned}
c_{\rm chr}
&=
\sum_{q=0}^{H-1}
\frac{2^{\lfloor q\gamma\rfloor}}{3^{q+1}}\\
&=
\frac13
\sum_{q=0}^{H-1}
2^{-\{q\gamma\}}\\
&=
\boxed{
\frac13
\sum_{q=0}^{H-1}
2^{-\{q\alpha\}}.
}
\end{aligned}
\]

For the actual path, since

\[
a_q=\lfloor q\gamma\rfloor-h_q,
\]

we have

\[
\boxed{
c
=
\frac13
\sum_{q=0}^{H-1}
2^{-\{q\alpha\}}2^{-h_q}.
}
\]

## 5. Weighted skew defect is exactly the Christoffel defect

Define the weighted skew-defect mass

\[
\boxed{
\mathfrak D_H
:=
\sum_{q=0}^{H-1}
2^{-\{q\alpha\}}
\left(1-2^{-h_q}\right).
}
\]

Subtracting the two exact correction formulas gives

\[
\boxed{
c_{\rm chr}-c
=\frac13\mathfrak D_H.
}
\]

Let

\[
\mathcal E:=R_{\rm chr}-R
\]

be the integer Christoffel correction defect, and let

\[
\eta:=\frac{\mathcal E}{3^H}
\]

be the normalized tri-place defect coordinate. Since `c=R/3^H`,

\[
\boxed{
\eta
=c_{\rm chr}-c
=\frac13\mathfrak D_H.
}
\]

Equivalently,

\[
\boxed{
\mathfrak D_H=3\eta.
}
\]

So the rotation-weighted defect introduced from the odd-event correction budget is not merely comparable to the Christoffel defect: it is exactly three times the same tri-place coordinate.

## 6. Sparse-support equivalence

Let

\[
\boxed{
r_*:=\#\{q:0\le q<H,\ h_q>0\}.}
\]

By the coordinate identification this is exactly the number of displaced Christoffel one-positions:

\[
r_*=\#\{k:s_k>0\}.
\]

For every positive `h_q`,

\[
\frac12<2^{-\{q\alpha\}}<1
\]

and

\[
\frac12\le1-2^{-h_q}<1.
\]

(The `q=0` term has `h_0=0` and never belongs to the support.) Hence

\[
\boxed{
\frac14 r_*
<
\mathfrak D_H
<
r_*.
}
\]

Therefore

\[
\boxed{
\mathfrak D_H=o(H)
\iff
r_*=o(H).
}
\]

Likewise, `mathfrak D_H` has positive linear density if and only if the displaced-one set has positive linear density, up to absolute constants.

Thus the previous weighted-defect target is exactly a sparse-support question.

## 7. Valuation-word sparsity

Let

\[
r_q:=\lfloor(q+1)\gamma\rfloor-\lfloor q\gamma\rfloor\in\{1,2\}.
\]

Since

\[
a_q=\lfloor q\gamma\rfloor-h_q,
\]

the actual odd-event valuation is

\[
\boxed{
v_q
=r_q+h_q-h_{q+1}.
}
\]

For the exact upper-Christoffel first-crossing reference, use

\[
h_q^{chr}=0\quad(0\le q<H),
\qquad
h_H^{chr}=-1.
\]

Hence the reference valuation word is

\[
v_q^{chr}=r_q
\quad(0\le q<H-1),
\]

and

\[
v_{H-1}^{chr}=r_{H-1}+1.
\]

If both adjacent skew heights equal their reference values, then the actual valuation equals the Christoffel valuation. Therefore

\[
\boxed{
\#\{q:v_q\ne v_q^{chr}\}
\le2r_*.
}
\]

Consequently

\[
\boxed{
\mathfrak D_H=o(H)
\Longrightarrow
\text{the valuation word differs from the critical Beatty/Christoffel word on only }o(H)\text{ indices}.
}
\]

This is substantially stronger than saying only that the aggregate ratio is near critical.

## 8. Direct tri-place rewrite in the new coordinate

The earlier tri-place identities may now be written directly in terms of `mathfrak D_H`:

### Real correction

\[
\boxed{
c=c_{\rm chr}-\frac13\mathfrak D_H.}
\]

### 2-adic formation address

\[
\boxed{
\rho_s
\equiv
\rho_{\rm chr}+\frac13\mathfrak D_H
\pmod{2^{A+1}}.
}
\]

### Renewal-gap address

With

\[
Z=2^A-3^H,
\]

\[
\boxed{
g_s
\equiv
 g_{\rm chr}-\frac13\mathfrak D_H
\pmod Z.
}
\]

The factor `1/3` is a unit in both relevant odd/dyadic modular settings.

Thus one and the same weighted sparse-support quantity controls the Archimedean correction loss, the 2-adic formation shift, and the gap-residue shift.

## 9. Earliest defect and 2-adic depth

Let

\[
q_*:=\min\{q:h_q>0\},
\qquad
k_*=q_*+1.
\]

The earlier exact earliest-displacement theorem gives

\[
v_2(\eta)=i_{k_*}-1.
\]

Since `mathfrak D_H=3 eta` and `3` is odd,

\[
\boxed{
v_2(\mathfrak D_H)=i_{k_*}-1=a_{q_*}.}
\]

So the first nonzero skew event is exactly the 2-adic depth at which the weighted defect begins to alter the formation address.

## 10. Square-prefix localization

For every sufficiently indexed upper-Christoffel standard word, the established square-prefix theorem supplies a prefix

\[
u^2
\]

of parity length `2L`, with formation barrier

\[
\rho(u^2)>2^{L+1}.
\]

The strengthened first-crossing ceiling from the rotation-mean/Denjoy--Koksma bound is polynomial in the current convergent size. By the same effective Baker/Matveev comparison already used for the Christoffel equality branch, for all sufficiently large convergents this polynomial ceiling is below `2^{L+1}`.

Therefore any surviving non-Christoffel first-crossing word must differ from the Christoffel word before the end of that square prefix. Equivalently its earliest displaced one satisfies

\[
\boxed{i_{k_*}\le2L.}
\]

Hence

\[
\boxed{v_2(\mathfrak D_H)\le2L-1.}
\]

So a residual candidate cannot postpone its first defect arbitrarily far into the word while keeping a polynomial-size ordinary starting integer.

## 11. Refined residual hard core

The primitive upper-CF first-crossing branch is now reduced to the following form.

For sufficiently large convergents, any surviving non-Christoffel word must have:

1. an exact skew/displacement path `h_q=s_{q+1}`;
2. a nonzero weighted defect `mathfrak D_H=3 eta`;
3. exact tri-place compatibility in the real, 2-adic, and gap coordinates;
4. a defect occurring inside the forced Christoffel square-prefix scale;
5. and, if it evades every positive-density defect bound,

\[
\boxed{r_*=o(H),}
\]

so its valuation sequence differs from the critical Beatty/Christoffel sequence on only `o(H)` positions.

Thus the remaining R1 asymptotic branch is no longer an unrestricted near-Christoffel family. It is a **sparse, early-anchored perturbation of the critical mechanical word subject to one exact tri-place residue constraint**.

## 12. Next theorem target

The next useful terminal statement is a sparse-perturbation exclusion theorem:

> Show that no sequence of primitive upper-CF first-crossing words can simultaneously have `r_*=o(H)`, an earliest defect inside the forced square-prefix scale, a polynomial-size ordinary formation representative, and a gap residue in `4 Z cap (0,H/3)`.

The López--Stoll analysis of the 3x+1 conjugacy map over exact mechanical/Sturmian words is relevant background for the zero-defect critical word, but the remaining problem is strictly sharper: it concerns sparse perturbations of that mechanical word together with ordinary-integer naturalness and renewal-gap arithmetic.

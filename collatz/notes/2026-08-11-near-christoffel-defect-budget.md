# Near-Christoffel defect budget for supercritical renewal words

Date: 2026-08-11

Status: **exact defect lower bound from the Fernández–Ibáñez transposition construction + exact renewal-shadow upper budget**. This quantifies how far a residual supercritical renewal word may lie from the Christoffel extremizer. It does not yet prove defect zero.

## 1. Setup

Fix aggregate parameters

\[
A>0,\qquad H>0,\qquad 2^A>3^H.
\]

Put

\[
\gamma:=\log_2 3,
\qquad
P:=\frac{2^A}{3^H}>1,
\qquad
Z:=2^A-3^H=3^H(P-1).
\]

Let `w` be a finite word occurring as an aggregate-supercritical renewal segment, in the rotation whose positive rational periodic shadow has its minimum at the renewal start. Since within every maximal block the intermediate odd states rise and the trailing even states decrease to the next block start, the minimum over all parity rotations is attained at a block start. Thus the renewal rotation realizes the rotation-invariant value

\[
C_{\min}(w).
\]

Let

\[
C_{\min}^{\rm chr}
\]

be the Christoffel maximum at the same `(A,H)`, and define the correction defect

\[
\boxed{
\mathcal E(w)
:=C_{\min}^{\rm chr}-C_{\min}(w)
\ge0.
}
\]

The defect is zero exactly for the Christoffel rotation class.

## 2. Position-displacement coordinates

Fernández–Ibáñez choose a rotation `d^c` minimizing the mean position of its ones and prove that its one-positions satisfy

\[
i_k^c\le i_k^{\rm chr},
\qquad k=1,\ldots,H,
\]

where

\[
\boxed{
i_k^{\rm chr}
=
\left\lfloor\frac{(k-1)A}{H}\right\rfloor+1.}
\]

Define the right-displacements needed to reach the Christoffel positions:

\[
\boxed{s_k:=i_k^{\rm chr}-i_k^c\ge0.}
\]

Their construction moves the ones, from right to left, by adjacent transpositions `10 -> 01`.

## 3. Exact transposition defect for the mean-minimizing rotation

Moving the `k`th one one place to the right when it currently occupies position `j` changes the Collatz correction functional by

\[
\boxed{2^{j-1}3^{H-k}.}
\]

Hence moving the `k`th one from `i_k^c` to `i_k^{chr}` contributes exactly

\[
3^{H-k}
\sum_{j=i_k^c}^{i_k^{\rm chr}-1}2^{j-1}
=
3^{H-k}2^{i_k^c-1}(2^{s_k}-1).
\]

Therefore

\[
\boxed{
C_{\min}^{\rm chr}-C(d^c)
=
\sum_{k=1}^H
3^{H-k}2^{i_k^c-1}(2^{s_k}-1).
}
\]

Since

\[
C_{\min}(w)\le C(d^c),
\]

we obtain the rigorous lower bound

\[
\boxed{
\mathcal E(w)
\ge
\sum_{k=1}^H
3^{H-k}2^{i_k^c-1}(2^{s_k}-1).
}
\]

## 4. Normalized displacement-charge bound

For `s_k>0`, rewrite one summand as

\[
3^{H-k}2^{i_k^{\rm chr}-1}(1-2^{-s_k}).
\]

Because

\[
\frac AH>\log_2 3,
\]

and

\[
i_k^{\rm chr}-1
=
\left\lfloor\frac{(k-1)A}{H}\right\rfloor,
\]

we have

\[
2^{i_k^{\rm chr}-1}
>
\frac12\,3^{k-1}.
\]

Thus

\[
3^{H-k}2^{i_k^{\rm chr}-1}(1-2^{-s_k})
>
\frac{3^H}{6}(1-2^{-s_k}).
\]

Define the Christoffel displacement charge

\[
\boxed{
\mathscr D(w)
:=
\sum_{k=1}^H(1-2^{-s_k}).
}
\]

Then

\[
\boxed{
\frac{\mathcal E(w)}{3^H}
>
\frac16\,\mathscr D(w).
}
\]

If

\[
r_*(w):=\#\{k:s_k>0\}
\]

is the number of displaced ones, then every nonzero term in `mathscr D` is at least `1/2`, so

\[
\boxed{
r_*(w)<12\,\frac{\mathcal E(w)}{3^H}.}
\]

The functional therefore controls the number of one-positions that differ from the Christoffel extremal placement, although it does not linearly control arbitrarily large displacement distances because `1-2^{-s}` saturates.

## 5. Exact renewal-shadow defect budget

Let the renewal segment send the integer floor

\[
N\mapsto N'=N+g,
\qquad g>0.
\]

Its rational shadow minimum is

\[
C_w
=
N+\frac{P}{P-1}g.
\]

Since

\[
C_w
=
\frac{C_{\min}(w)}{Z},
\qquad
C_{\rm chr}
=
\frac{C_{\min}^{\rm chr}}{Z},
\]

we have the exact identity

\[
\boxed{
\frac{\mathcal E(w)}{3^H}
=(P-1)(C_{\rm chr}-C_w).
}
\]

The Fernández–Ibáñez Christoffel extremal estimate gives

\[
C_{\rm chr}
\le
\frac1{3(P^{1/H}-1)}.
\]

Therefore every supercritical renewal word satisfies

\[
\boxed{
\frac{\mathcal E(w)}{3^H}
\le
\frac{P-1}{3(P^{1/H}-1)}
-(P-1)N
-Pg.
}
\]

Combining with the displacement lower bound yields

\[
\boxed{
\mathscr D(w)
<
6\left[
\frac{P-1}{3(P^{1/H}-1)}
-(P-1)N
-Pg
\right].
}
\]

and

\[
\boxed{
r_*(w)
<
12\left[
\frac{P-1}{3(P^{1/H}-1)}
-(P-1)N
-Pg
\right].}
\]

The bracket must be positive for any renewal candidate.

For a non-Christoffel word at least one one is displaced, so the normalized defect is strictly larger than `1/12`. Hence a necessary condition is

\[
\boxed{
Pg+(P-1)N+\frac1{12}
<
\frac{P-1}{3(P^{1/H}-1)}.
}
\]

This recovers and strengthens the earlier single-transposition strict-gap correction in a position-resolved form.

## 6. Valid restoration of the `H > 3g` renewal cost

An earlier event-level argument for `H>3g` was retracted because it incorrectly treated all odd states inside a maximal block as larger than the next renewal floor.

The same conclusion is, however, valid by the Christoffel-shadow route.

Dropping the positive terms `(P-1)N` and `mathcal E/3^H` from the exact budget gives

\[
Pg
<
\frac{P-1}{3(P^{1/H}-1)}.
\]

Let

\[
x:=P^{1/H}>1.
\]

Then

\[
\frac{P-1}{P(P^{1/H}-1)}
=
\frac{x^H-1}{x^H(x-1)}
=
\sum_{j=1}^{H}x^{-j}
<H.
\]

Therefore

\[
\boxed{g<\frac H3,}
\]

or equivalently

\[
\boxed{H>3g.}
\]

This proof is independent of the invalid interior-odd-state estimate.

Since genuine renewal floors satisfy `g≡0 mod 4`, every aggregate-supercritical genuine renewal has

\[
\boxed{g\ge4,\qquad H\ge13.}
\]

## 7. Stronger floor-sensitive form

Using

\[
P^{1/H}-1\ge\frac{\ln P}{H}
\]

in the Christoffel-shadow budget gives

\[
H
\ge
3N\ln P
+
3g\,\frac{P\ln P}{P-1}.
\]

Because

\[
\frac{P\ln P}{P-1}>1,
\]

we obtain

\[
\boxed{
H>3g+3N\ln P.
}
\]

In discrepancy notation `P=2^Delta`,

\[
\boxed{
H>3g+3N\Delta\ln2.
}
\]

Thus a supercritical renewal simultaneously pays for its integer floor gap and for its coefficient distance above the critical line.

## 8. Gap-channel combination

The exact gap-channel theorem gives

\[
g\equiv g_w\pmod Z,
\qquad
Z=2^A-3^H.
\]

The block-count theorem gives `g<m`, and every maximal block contains at least one odd event, so `m<=H`. The stronger Christoffel argument now yields

\[
\boxed{0<g<\frac H3.}
\]

Consequently, whenever

\[
Z>H/3,
\]

the only possible positive gap is the least positive residue itself:

\[
\boxed{
g=g_w<\frac H3.}
\]

For a genuine renewal it must additionally satisfy

\[
\boxed{g_w\equiv0\pmod4.}
\]

Thus the residual arithmetic problem is extremely sharp: an exponentially large modulus must place the exact correction residue into the tiny set

\[
\boxed{
\{4,8,12,\ldots\}\cap(0,H/3).
}
\]

## 9. Current role

The exact Christoffel equality branch has already been reduced to a finite initial audit by the square-prefix formation theorem.

For non-Christoffel CF-resonant words, the present theorem supplies two complementary constraints:

1. a **combinatorial defect budget** through `mathscr D(w)` and `r_*(w)`;
2. a **tiny arithmetic gap channel** `g_w in (0,H/3)` with `g_w=0 mod 4`.

A complete residual exclusion theorem should connect these two facts: show that moving any positive set of ones away from the Christoffel placement cannot move the enormous gap residue into the required tiny interval without exceeding the renewal defect budget or violating exact formation.

# Defect-carry block duality for finite-horizon Collatz pruning

Date: 2026-08-09

Status: **DERIVED EXACT REFORMULATION + BLOCK PRUNING LEMMA + INDEPENDENT SMALL CHECK**

This note connects the fixed-cell defect transfer to the backward cyclic-successor / interval-count machinery. It is an exact finite-horizon reduction, not a proof of the Collatz conjecture.

## 1. Fixed surviving prefix cell

Use the accelerated map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Fix a coefficient-surviving cell of length `h` with `q` odd positions. Put

\[
M=2^h,\qquad P=3^q.
\]

For an admissible odd-position vector `d`, let

\[
R(d)=\sum_{i=0}^{q-1}2^{d_i}3^{q-1-i}.
\]

Let `d*` be the prefix-constrained cell maximizer from `slack-cell-correction-envelope.md`, with correction `R*`, canonical start `r*`, and endpoint `y*`:

\[
r^*\equiv-P^{-1}R^*\pmod M,
\qquad
My^*=Pr^*+R^*.
\]

For another word in the same cell define the correction defect

\[
\boxed{C=R^*-R\ge0.}
\]

## 2. Forward wrap coordinate

Define

\[
\boxed{U=[P^{-1}C]_M,\qquad 0\le U<M.}
\]

Then

\[
r\equiv r^*+U\pmod M,
\]

so, with

\[
\boxed{w=\left\lfloor\frac{r^*+U}{M}\right\rfloor\in\{0,1\},}
\]

we have the exact representative identity

\[
\boxed{r=r^*+U-wM.}
\]

Thus the many additive defect channels affect the canonical start only through one cyclic coordinate `U` and one final wrap bit `w`.

For any threshold

\[
1\le X\le M,
\]

we obtain

\[
\boxed{
r<X
\iff
U\in I_M(-r^*,X),
}
\]

where

\[
I_M(a,L)=\{a,a+1,\ldots,a+L-1\}\pmod M.
\]

Hence a small canonical start is exactly a short cyclic-interval hit by the defect-transfer coordinate `U`.

If `X<=r*`, this forward interval has constant `w=1`. If `X>r*`, it splits into at most two ordinary intervals, one with `w=1` and one with `w=0`.

## 3. Carry quotient and endpoint coordinate

Because

\[
PU\equiv C\pmod M,
\]

the integer

\[
\boxed{T_c=\frac{PU-C}{M}}
\]

is well-defined. Substituting the start identity into

\[
My=Pr+R
\]

gives

\[
\boxed{y=y^*+T_c-wP.}
\]

Now fix a target depth

\[
K=h+m,
\]

put

\[
N=2^m,
\]

and define the transformed backward query coordinates

\[
\xi=[P^{-1}y]_N,
\qquad
\xi^*=[P^{-1}y^*]_N.
\]

Define the second defect coordinate

\[
\boxed{V=[P^{-1}T_c]_N.}
\]

Then the endpoint query becomes the simple translation

\[
\boxed{\xi=[\xi^*+V-w]_N.}
\]

This is the key duality: the forward small-start condition is a short interval in `U`, while the backward zero-lift condition is a translated condition in `V`.

## 4. Local two-coordinate defect transfer

Write the total correction defect as the sum of the exact defect channels from `slack-defect-channel-transfer.md`:

\[
C=\sum_i C_i,
\]

\[
C_i=3^{q-1-i}\left(2^{d_i^*}-2^{d_i}\right).
\]

For one channel define

\[
\boxed{a_i=[P^{-1}C_i]_M,}
\]

\[
\boxed{t_i=\frac{Pa_i-C_i}{M}\in\mathbb Z,}
\]

and

\[
\boxed{b_i=[P^{-1}t_i]_N.}
\]

Starting from

\[
U_0=0,\qquad V_0=0,
\]

add the channels in odd-position order. The modular-addition carry is

\[
\boxed{\varepsilon_i=\mathbf 1_{\,U_i+a_i\ge M}.}
\]

Then

\[
\boxed{U_{i+1}=U_i+a_i-\varepsilon_iM,}
\]

\[
\boxed{V_{i+1}=[V_i+b_i-\varepsilon_i]_N.}
\]

At the end these equal the global coordinates defined above.

For fixed channel choice and fixed carry value, this is a piecewise-affine matrix update on the product group:

\[
\begin{pmatrix}
U'\\V'\\1
\end{pmatrix}
=
\begin{pmatrix}
1&0&a_i-\varepsilon_iM\\
0&1&b_i-\varepsilon_i\\
0&0&1
\end{pmatrix}
\begin{pmatrix}
U\\V\\1
\end{pmatrix},
\]

with the first coordinate interpreted modulo `M` and the second modulo `N`. The carry gate is determined only by whether `U` crosses the single threshold `M-a_i`.

Together with the nearest-neighbor admissibility rule for the defect state `z_i`, this gives a sparse two-coordinate channel transfer.

## 5. Exact target-depth small-start criterion

Let

\[
S_{h,q,m}\subset\mathbb Z/N\mathbb Z
\]

be the transformed admissible suffix set from `two-channel-successor-bellman.md` / `interval-count-certificate.md`. For the current prefix word,

\[
J=0
\iff
\xi\in S_{h,q,m}.
\]

A target-depth canonical descendant has the form

\[
n=r+MJ,\qquad J\ge0.
\]

Therefore, for

\[
1\le X\le M,
\]

we have the exact equivalence

\[
\boxed{
\exists\ n<X\text{ represented by this cell and surviving through }K
}
\]

iff there exists an admissible defect state `(U,V)` such that

\[
\boxed{U\in I_M(-r^*,X)}
\]

and

\[
\boxed{[\xi^*+V-w(U)]_N\in S_{h,q,m}.}
\]

The reason is that `J>=1` would already give

\[
n\ge M\ge X.
\]

Thus, below a bit threshold, the entire finite-horizon problem inside one `(h,q)` cell is a two-coordinate intersection problem.

## 6. Rectangle pruning theorem

Consider any block of reachable defect states for which

- the `U` projection lies inside the forward small-start interval;
- the final wrap bit is constant, `w=w_0`;
- the `V` projection is contained in a cyclic interval

\[
I_N(v_0,L).
\]

Then every transformed endpoint query in the block lies in

\[
I_N(\xi^*+v_0-w_0,L).
\]

Let

\[
N_{h,q,m}(a,L)
=|S_{h,q,m}\cap I_N(a,L)|
\]

be the exact backward interval count. If

\[
\boxed{
N_{h,q,m}(\xi^*+v_0-w_0,L)=0,
}
\]

then no defect state in the whole block has `J=0`. Since the block was already restricted to `r<X<=M`, no state in the block can produce a target-depth start below `X`.

Therefore the whole rectangle may be removed safely.

This remains safe if the `V` interval is merely an over-approximation of the true reachable `V` values: emptiness of the larger interval implies emptiness of the exact support.

This is the direct block-level bridge between the forward defect matrix and the backward exact interval certificate.

## 7. Relation to formation/complement pruning

The exact removal sequence is now:

1. fix an E/O cell `(h,q)`;
2. use the defect transfer to form certified `(U,V)` blocks;
3. intersect `U` with the short forward interval required by `r<X`;
4. split once if necessary so that `w` is fixed;
5. translate the corresponding `V` block to a backward-query interval;
6. call the exact E/O interval count;
7. prune the block only when that count is zero.

No average-density, independence, or Fourier assumption is needed for the final removal.

## 8. Independent finite checks

Wolfram exact-integer enumeration was performed for all coefficient-admissible fixed cells with

\[
1\le h\le7,
\qquad
1\le m\le4.
\]

Across 56 `(h,q,m)` cases it verified simultaneously:

- `r=r*+U-wM`;
- `y=y*+T_c-wP`;
- `xi=xi*+V-w`;
- the local channel recurrence for `(U,V)` equals the global definitions;
- for every threshold `1<=X<=M`, direct counting of target-depth survivors below `X` agrees with the two-coordinate block criterion.

These are finite computational cross-checks, not ingredients of the algebraic proof.

## 9. Next target

The immediate proof-relevant target is no longer a new state equivalence. It is to find a controlled rectangle cover of the reachable defect support

\[
\mathcal C_{h,q,m}\subset
(\mathbb Z/M\mathbb Z)\times(\mathbb Z/N\mathbb Z)
\]

inside the short forward interval `U in I_M(-r*,X)`.

If that cover uses few rectangles, the exact backward count can eliminate each rectangle in one call. A uniform subexponential or polynomial rectangle-cover bound at the logarithmic bit scale would directly strengthen the current anti-alignment / late-lift program.
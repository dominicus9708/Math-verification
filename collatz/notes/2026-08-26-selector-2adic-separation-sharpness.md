# Sharp 2-adic separation depth of the ternary selector layer

Date: 2026-08-26

Status: **exact finite arithmetic theorem.** This note determines the least dyadic modulus that separates all members of one recursively sufficient selector layer. It slightly sharpens the fixed-layer handoff depth but proves that the asymptotic address slope cannot be improved by selector 2-adic injectivity alone. It is not a Collatz proof.

## 1. Selector differences

For fixed `m`, write

\[
N(a)
=4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3,
\qquad a_i\in\{0,1\}.
\]

For two selectors `a,b`,

\[
N(a)-N(b)
=4\sum_{i=0}^{m-1}(a_i-b_i)3^i.
\]

Put

\[
\varepsilon_i:=a_i-b_i\in\{-1,0,1\}.
\]

Then every selector difference is `4S`, where

\[
S=\sum_{i=0}^{m-1}\varepsilon_i3^i.
\]

## 2. Balanced-ternary completeness

The signed digits `{-1,0,1}` are the ordinary balanced-ternary digits. Therefore the map

\[
(\varepsilon_0,\ldots,\varepsilon_{m-1})
\mapsto
\sum_i\varepsilon_i3^i
\]

is a bijection onto the complete integer interval

\[
\boxed{
-A_m,-A_m+1,\ldots,A_m,
\qquad
A_m:=\frac{3^m-1}{2}.
}
\]

Every signed digit vector is realizable as the difference of two `0/1` selector digit vectors: choose `(a_i,b_i)=(1,0)` for `epsilon_i=1`, `(0,1)` for `-1`, and equal digits for zero.

Hence the nonzero selector differences are exactly

\[
\boxed{
4S,
\qquad
0<|S|\le A_m.
}
\]

## 3. Exact maximum 2-adic valuation

Because every integer up to `A_m` occurs, the largest possible 2-adic valuation is attained by the largest power of two not exceeding `A_m`:

\[
\max_{a\ne b}v_2(N(a)-N(b))
=2+\lfloor\log_2A_m\rfloor.
\]

Equivalently,

\[
\boxed{
V_m
:=
\max_{a\ne b}v_2(N(a)-N(b))
=
\left\lfloor\log_2\bigl(2(3^m-1)\bigr)\right\rfloor.
}
\]

Therefore the least dyadic resolution at which the selector residues are pairwise distinct is

\[
\boxed{
K_{\rm sep}(m)
=V_m+1
=\operatorname{bitlength}\bigl(2(3^m-1)\bigr).
}
\]

This is sharp: at resolution `K_sep-1`, choose the balanced-ternary representation of

\[
2^{\lfloor\log_2A_m\rfloor};
\]

the corresponding two selectors differ by a nonzero multiple of `2^(K_sep-1)`.

## 4. Comparison with the full-value address bound

The earlier full-value handoff used

\[
K_{\rm addr}(m)
=\operatorname{bitlength}(6\cdot3^m+1).
\]

The exact selector-separation depth is slightly smaller:

- `m=44`: `K_addr=73`, `K_sep=71`;
- `m=45`: `K_addr=74`, `K_sep=73`.

Thus arguments that need only **identity within the selector layer modulo a dyadic power**, rather than recovery of the absolute integer from an arbitrary residue, may hand off at `K_sep`.

In particular, in a plateau orientation cube, two vertices whose first differing swap coordinate has index

\[
j\ge K_{\rm sep}(m)
\]

have canonical residues congruent modulo `2^K_sep`. They therefore cannot both be members of the same selector layer.

## 5. Asymptotic sharpness of the address slope

Since

\[
K_{\rm sep}(m)
=m\log_2 3+O(1),
\]

the selector's own 2-adic separation has the same asymptotic slope

\[
\boxed{\log_2 3\approx1.584962500721156}
\]

as the earlier full-address exposure.

Therefore there is no asymptotic gain available from the hypothesis

> `the ternary 0/1 selector might become dyadically injective much earlier than its numeric bit length`.

Balanced-ternary completeness supplies actual power-of-two selector differences all the way to the natural magnitude scale, so this route can save only `O(1)` bits.

## 6. DSD audit verdict

This is a useful negative/pruning result.

- **state layer:** one fixed ternary selector layer;
- **difference channel:** balanced ternary `{-1,0,1}`;
- **dyadic descriptor:** valuation of selector differences;
- **exact conclusion:** modular selector identity is available at `K_sep`;
- **closed branch:** no smaller asymptotic address slope can be obtained from pure 2-adic injectivity of selector differences.

The post-address plateau-cube route remains useful, but any exponential improvement must come from additional dynamical/survivor constraints rather than from selector separation alone.

Certificate: `collatz/src/selector_2adic_separation_sharpness_certificate.py`.

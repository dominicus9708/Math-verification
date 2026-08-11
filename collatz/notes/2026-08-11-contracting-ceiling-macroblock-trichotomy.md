# Contracting-ceiling macroblock trichotomy

Date: 2026-08-11

Status: **exact auxiliary theorem**. This note links the formation-floor/survival-ceiling formulation to the earlier odd-event headroom formulation. It does **not** prove the remaining global boundary-crossing theorem.

## 1. Odd-event coordinates

For an odd starting integer `n`, let

\[
x_{q+1}=\frac{3x_q+1}{2^{v_q}},\qquad v_q:=v_2(3x_q+1)\ge 1.
\]

Let

\[
A_q:=\sum_{i=0}^{q-1}v_i,
\qquad
\lambda_q:=\frac{2^{A_q}}{3^q},
\]

and let the normalized affine correction be

\[
c_q:=\sum_{i=0}^{q-1}\frac{2^{A_i}}{3^{i+1}}.
\]

Then

\[
\boxed{
x_q=\frac{n+c_q}{\lambda_q}.
}
\]

Equivalently, in the accelerated-prefix notation `a=3^q/2^{A_q}`, one has `a=1/lambda` and the same correction coordinate `c`.

The event update is

\[
\boxed{
\lambda_{q+1}=\lambda_q\frac{2^{v_q}}{3},
\qquad
c_{q+1}=c_q+\frac{\lambda_q}{3}.
}
\]

---

## 2. Contracting endpoint ceiling and headroom are the same boundary

At an event with

\[
\lambda_q>1
\]

(the corresponding affine coefficient is below one), define the current endpoint survival ceiling

\[
\boxed{
C_q:=\frac{c_q}{\lambda_q-1}.
}
\]

Indeed,

\[
x_q\ge n
\iff
\frac{n+c_q}{\lambda_q}\ge n
\iff
c_q\ge n(\lambda_q-1)
\iff
\boxed{n\le C_q.}
\]

Define the headroom

\[
\boxed{
H_q:=1+\frac{c_q}{n}-\lambda_q.
}
\]

Then

\[
\boxed{
H_q\ge0\iff C_q\ge n
}
\]

whenever `lambda_q>1`.

Thus `H` and `C` are two coordinate descriptions of the same survival boundary: `H` is additive and start-dependent, while `C` is an absolute ceiling on admissible starts.

---

## 3. Single-event ceiling update

Assume `lambda>1`, write

\[
c=C(\lambda-1),
\]

and let the next odd-event valuation be `v>=1`. If the new endpoint is still contracting,

\[
\lambda' = \lambda\frac{2^v}{3}>1,
\]

then

\[
\boxed{
C'
=
\frac{3C(\lambda-1)+\lambda}{2^v\lambda-3}.
}
\]

Subtracting `C` gives

\[
\boxed{
C'-C
=
\frac{\lambda\,[1+C(3-2^v)]}{2^v\lambda-3}.
}
\]

Hence for a surviving positive start `n>=2`, so that `C>=n>=2`:

- `v=1` implies `C'>C` whenever both endpoints are contracting;
- every `v>=2` implies `C'<C` whenever both endpoints are contracting.

Moreover a transition from a noncontracting endpoint `lambda<=1` to a contracting one `lambda'>1` is impossible for `v=1`, because multiplication by `2/3` decreases `lambda`. Therefore:

\[
\boxed{
\text{a finite endpoint survival ceiling can be created or tightened only at }v_2\ge2\text{ events.}
}
\]

Credit events `v=1` never create a new finite contracting ceiling.

---

## 4. Maximal macroblock

Consider a maximal macroblock consisting of `ell>=0` consecutive credit events `v=1`, followed by one debit event `b>=2`.

Set

\[
\boxed{h:=\ell+1,\qquad d:=b-1\ge1}
\]

and define

\[
\boxed{
r_h:=\left(\frac23\right)^h,
\qquad
M_{h,d}:=\frac{2^{h+d}}{3^h}.
}
\]

Here `M_{h,d}` is the exact multiplier of `lambda` across the whole macroblock.

Starting from `(lambda,c)`, the block update is

\[
\boxed{
\lambda'=\lambda M_{h,d},
}
\]

\[
\boxed{
c'=c+\lambda(1-r_h).
}
\]

For the headroom relative to a fixed initial `n`, this gives the particularly simple exact identity

\[
\boxed{
H'-H
=
\lambda\left[
\frac{1-r_h}{n}-(M_{h,d}-1)
\right].
}
\]

Thus a macroblock credits headroom exactly when its multiplicative excess above one is smaller than the affine correction credit `(1-r_h)/n`.

---

## 5. Contracting-ceiling macroblock recurrence

Suppose the block begins at a contracting endpoint with ceiling `C`, and the block ends at another contracting endpoint:

\[
\lambda>1,
\qquad
\lambda M_{h,d}>1.
\]

Then

\[
\boxed{
C'-C
=
\frac{
\lambda\left[
1-r_h-C(M_{h,d}-1)
\right]
}{
\lambda M_{h,d}-1
}.
}
\]

Therefore, when `M_{h,d}>1`, failure to lower the endpoint ceiling requires

\[
\boxed{
0<M_{h,d}-1
\le
\frac{1-r_h}{C}.
}
\]

If a particular start `n>=2` survives, then `C>=n`, hence

\[
\boxed{
1<M_{h,d}
\le
1+\frac{1-r_h}{C}
\le
1+\frac{1-r_h}{n}
<
1+\frac1n.
}
\]

This recovers the earlier critical-resonance window directly as a **ceiling-stall condition**.

---

## 6. Exact debit threshold

Define

\[
\boxed{
d_*(h):=\left\lceil h\log_2\frac32\right\rceil.}
\]

Because `log_2(3/2)` is irrational,

\[
d_*(h)-1
<
h\log_2\frac32
<
d_*(h).
\]

Hence:

### Subcritical debit

If

\[
d<d_*(h),
\]

then

\[
\boxed{M_{h,d}<1.}
\]

Consequently

\[
\boxed{
\lambda'<\lambda,
\qquad
H'-H>0.
}
\]

A subcritical block gains headroom but spends multiplicative `lambda`.

### Critical debit

If

\[
d=d_*(h),
\]

then

\[
\boxed{1<M_{h,d}<2.}
\]

Write

\[
\epsilon_h
:=
d_*(h)-h\log_2\frac32
\in(0,1),
\]

so

\[
\boxed{M_{h,d_*}=2^{\epsilon_h}.}
\]

The exact headroom increment is

\[
\boxed{
H'-H
=
\lambda\left[
\frac{1-(2/3)^h}{n}
-
(2^{\epsilon_h}-1)
\right].
}
\]

Thus critical headroom nonloss is equivalent to

\[
\boxed{
2^{\epsilon_h}-1
\le
\frac{1-(2/3)^h}{n}.
}
\]

This is the sole debit layer in which `lambda` can increase without automatically producing a large headroom debit.

### Supercritical debit

If

\[
d>d_*(h),
\]

then, since increasing `d` by one doubles `M`,

\[
\boxed{M_{h,d}>2.}
\]

For every `n>=2`,

\[
\frac{1-r_h}{n}<\frac12,
\qquad
M_{h,d}-1>1,
\]

so

\[
\boxed{
H'-H< -\frac{\lambda}{2}.
}
\]

A supercritical block therefore spends headroom by a uniform amount proportional to the incoming `lambda`.

---

## 7. Resource trichotomy

Every maximal odd-event macroblock belongs to exactly one of three classes:

\[
\boxed{
\begin{array}{c|c|c}
\text{class}&\lambda& H\\
\hline
 d<d_*(h)&\text{strictly decreases}&\text{strictly increases}\\
 d=d_*(h)&\text{increases by factor }(1,2)&\text{sign depends on resonance}\\
 d>d_*(h)&\text{increases by factor }>2&\text{decreases by more than }\lambda/2
\end{array}
}
\]

Thus every **noncritical** block makes a definite trade in one of the two resource coordinates. The only layer where both resources can avoid a strong loss is the critical debit

\[
\boxed{d=d_*(h).}
\]

This does not by itself prove termination, because subcritical and supercritical blocks can alternate and exchange the two resources. The remaining proof task is to show that a finite positive integer cannot realize an infinite exchange sequence while maintaining the exact formation constraints and `H>=0` at every prefix.

---

## 8. Relation to the floor/ceiling framework

The earlier formation/survival framework gives, for each parity prefix,

\[
\rho_k\le \Theta_k
\]

as the exact survival condition for a nonempty class.

The present macroblock theorem identifies the mechanism by which the Archimedean side can tighten:

- finite ceilings arise only at debit events `v_2>=2`;
- ordinary supercritical debit blocks strongly consume headroom;
- subcritical blocks replenish headroom only by contracting `lambda`;
- failure of an expanding block to lower the endpoint ceiling is confined to the critical near-resonant layer.

Therefore the next refinement should not enumerate all `(h,d)`. It should attach arithmetic realization data only to the critical layer and prove that indefinite resource exchange is incompatible with formation by one fixed finite natural number.

---

## 9. Scope warning

A decrease `x'<x` across one macroblock, or a decrease of the current endpoint ceiling `C`, is **not** by itself a first descent below the original initial integer `n`. Such local decreases are resource statements only. Any final pruning theorem must still be stated against the original first-descent boundary or the cumulative survival ceiling `Theta`.

# Renewal gap-depth transfer theorem

Date: 2026-08-11

Status: **exact integer theorem for consecutive renewal floors**. It couples the renewal-floor gap to the credit depth of the first maximal block at the next floor.

## 1. Setup

Let consecutive renewal floors be odd positive integers

\[
N<N',
\qquad
g:=N'-N.
\]

Write

\[
N+1=2^hK,
\qquad K\text{ odd},
\]

so

\[
\boxed{h=v_2(N+1)}
\]

is the credit depth of the first maximal block leaving `N`.

Similarly define

\[
\boxed{h':=v_2(N'+1).}
\]

Let

\[
t:=v_2(g).
\]

Because both renewal floors are odd, `g` is a positive even integer.

## 2. Exact valuation transfer

We have

\[
N'+1=2^hK+g.
\]

### Case `t<h`

Write `g=2^t u` with `u` odd. Then

\[
N'+1
=2^t(2^{h-t}K+u),
\]

and the bracket is even-plus-odd, hence odd. Therefore

\[
\boxed{h'=t.}
\]

### Case `t>h`

Then

\[
N'+1
=2^h(K+2^{t-h}u),
\]

and the bracket is odd-plus-even, hence odd. Therefore

\[
\boxed{h'=h.}
\]

### Case `t=h`

Now

\[
N'+1=2^h(K+u),
\]

and `K+u` is even. Therefore

\[
\boxed{h'>h.}
\]

Combining the three cases,

\[
\boxed{
h'=
\begin{cases}
t,&t<h,\\
h,&t>h,\\
>h,&t=h.
\end{cases}}
\]

## 3. Immediate corollaries

### Depth preservation/growth costs a large gap

If

\[
h'\ge h,
\]

then `t>=h`, so

\[
\boxed{2^h\mid g}
\]

and in particular

\[
\boxed{g\ge2^h.}
\]

### A small gap forces a depth drop

If

\[
g<2^h,
\]

then `t<h` and hence

\[
\boxed{h'=v_2(g)<h.}
\]

Thus a renewal floor cannot retain a long first-block credit depth across a small floor increment.

## 4. Combination with supercritical renewal cost

For an aggregate-supercritical renewal segment the exact block-count theorem gives

\[
\boxed{m>g,}
\]

where `m` is the number of maximal blocks in the segment.

Therefore

\[
\boxed{
P>1\text{ and }h'\ge h
\Longrightarrow
m>g\ge2^h.
}
\]

A supercritical renewal leaving a floor with large credit depth must therefore choose one of two outcomes:

1. **depth drop:** `h'<h`; or
2. **exponential block overload:** `m>2^h`.

This is a new discrete progress alternative independent of the continued-fraction/Christoffel resonance bounds.

## 5. Role

The theorem does not exclude an infinite renewal chain. Its value is that the first-block credit depth is now a transported discrete attribute with an exact transition law.

In particular, a hypothetical hard core cannot simultaneously keep large renewal-floor depths, use aggregate-supercritical transitions, and keep the number of blocks moderate.

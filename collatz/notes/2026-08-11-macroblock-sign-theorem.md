# Macroblock sign theorem

Date: 2026-08-11

Status: **exact theorem for maximal odd-event/debit blocks**. It shows that coefficient direction and actual integer direction coincide at macroblock resolution, except for exact block-fixed cycles.

## 1. Maximal block state

Let an odd block start be

\[
\boxed{X=2^hK-1,}
\]

where

\[
h=v_2(X+1)\ge1,
\qquad K\text{ is odd}.
\]

After `h-1` odd events with valuation `v=1`, the block ends with a debit event of valuation `d+1>=2`. The next odd block start is

\[
\boxed{
X'=\frac{3^hK-1}{2^d}.
}
\]

Define

\[
\boxed{
M:=\frac{2^{h+d}}{3^h}.
}
\]

Then

\[
\boxed{
M\frac{X'}{X}
=1+\frac{1-(2/3)^h}{X}>1.
}
\]

---

## 2. Subcritical blocks strictly increase

If

\[
M<1,
\]

then the block identity gives

\[
\frac{X'}{X}>\frac1M>1.
\]

Therefore

\[
\boxed{M<1\Longrightarrow X'>X.}
\]

---

## 3. Supercritical nondecrease forces exact return

Assume

\[
M>1.
\]

Put

\[
\Delta:=2^{h+d}-3^h>0.
\]

A direct subtraction gives

\[
\boxed{
X'-X
=\frac{2^d-1-\Delta K}{2^d}.
}
\]

Suppose also that

\[
X'\ge X.
\]

Then the numerator is nonnegative. Since `Delta K>=1`,

\[
0\le2^d-1-\Delta K\le2^d-2<2^d.
\]

But `X'-X` is an integer, so the numerator must be divisible by `2^d`. The only multiple of `2^d` in the displayed interval is zero. Hence

\[
\boxed{X'=X.}
\]

Therefore

\[
\boxed{
M>1\text{ and }X'\ge X
\Longrightarrow X'=X.
}
\]

Equivalently, if the block is not an exact return,

\[
\boxed{M>1\Longrightarrow X'<X.}
\]

---

## 4. Exact sign law on nonperiodic orbits

Equality `M=1` is impossible because positive powers of 2 and 3 cannot coincide.

On a nonperiodic orbit, `X'=X` is impossible because the deterministic map would then repeat the same odd state after one maximal block.

Hence every maximal block of a nonperiodic orbit satisfies the exact sign equivalence

\[
\boxed{
M<1\iff X'>X,
\qquad
M>1\iff X'<X.
}
\]

Since

\[
\log_2 M=d-h\log_2\frac32,
\]

this may be written as

\[
\boxed{
\operatorname{sgn}(X'-X)
=-\operatorname{sgn}\!\left(d-h\log_2\frac32\right)
}
\]

for every nonperiodic maximal block.

---

## 5. Consequences

### No macroblock-level paradoxical growth

At accelerated-step resolution, a prefix may have contracting multiplicative coefficient while its endpoint still exceeds the initial value; this is the source of coefficient-stopping/paradoxical complications.

At **maximal debit-block resolution**, this cannot occur strictly. A supercritical block either decreases the odd block state or closes exactly on the same state.

Thus local paradoxical behavior disappears after this exact coarse-graining.

### Tail minima

If `X` is a tail minimum of a nonperiodic divergent orbit, then `X'>=X`. The theorem therefore forces

\[
\boxed{M<1.}
\]

This recovers the tail-minimum strict-expansion lemma as an immediate corollary.

### Turning points

For a nonperiodic block orbit:

- consecutive `M<1` blocks form a strictly increasing run of block states;
- consecutive `M>1` blocks form a strictly decreasing run of block states.

Hence all local extrema of the odd-event orbit can be represented exactly by sign changes of the scalar block discrepancy

\[
\boxed{d-h\log_2(3/2).}
\]

This reduces the qualitative block dynamics to a one-dimensional signed lattice path coupled to the exact odd-core recurrence

\[
3^hK+2^d-1=2^{d+h'}K'.
\]

---

## 6. Scope

The theorem is local to one maximal block and does **not** imply global first descent. A sequence can contain many increasing and decreasing maximal blocks while remaining above its original starting value.

Its role is structural: it removes the need for a separate block-level paradoxical sector and permits future arguments to work directly with monotone runs and their turning points.
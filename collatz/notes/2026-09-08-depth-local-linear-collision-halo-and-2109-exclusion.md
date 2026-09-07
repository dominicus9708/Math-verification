# Depth-local linear collision halo and depth-2109 internal-boundary exclusion — MATH-021

Date: 2026-09-08

Status: `CONFIRMED / EXACT STRUCTURAL REDUCTION + FINITE-PREFIX OBSTRUCTION`

Global status remains:

- Collatz conjecture: `OPEN`
- first universal Farey cell: `OPEN`

## 1. Why the previous halo was unnecessarily large

MATH-015 through MATH-020 used a depth-dependent arithmetic-credit halo such as

\[
D_k=2^{k-q_{\min}(k)}-1.
\]

Those calculations were valid, but this is much larger than what is actually required for a **same-endpoint collision**.

MATH-004 already supplies a stronger relation inside a candidate-language endpoint fiber.

Write

\[
T^k(N)=\frac{3^Q N+R}{2^k},
\qquad
S=\frac{R}{3^Q}.
\]

For a universal-spine candidate prefix, if the odd positions are `p_r`, then

\[
2^{p_r}\le 3^{r-1},
\]

so

\[
0<S=\sum_{r=1}^{Q}\frac{2^{p_r}}{3^r}\le \frac Q3.
\]

Now take adjacent-block starts

\[
N_L<N_R,
\qquad d=N_R-N_L>0,
\]

that have the same depth-`k` endpoint.  The audited endpoint q-lock gives the same final odd-count `Q`.  Therefore

\[
3^Q(N_R-N_L)=R_L-R_R,
\]

hence

\[
\boxed{d=S_L-S_R}.
\]

Because `Q>0`, every such correction is positive, so

\[
0<S_R,
\qquad S_L\le Q/3.
\]

Thus

\[
\boxed{0<d<Q/3\le k/3}.
\]

Since `d` is a positive integer,

\[
\boxed{
d\le \left\lfloor\frac{Q-1}{3}\right\rfloor
\le
\left\lfloor\frac{k-1}{3}\right\rfloor.
}
\]

This is the correct **collision-complete depth-local halo**.

It is linear in `k`, not exponential in `k-q_min(k)`.

## 2. Consequence for an internal block boundary

Let an internal boundary be

\[
B=b2^{61},
\qquad b=1025,\ldots,1363,
\]

and write

\[
N_L=B-\ell,
\qquad
N_R=B+r,
\]

with

\[
\ell\ge1,
\qquad r\ge0.
\]

Then

\[
d=N_R-N_L=\ell+r.
\]

Any cross-boundary endpoint collision at depth `k` must therefore satisfy

\[
\boxed{
\ell+r\le\left\lfloor\frac{k-1}{3}\right\rfloor.
}
\]

In particular each side separately obeys

\[
r\le d,
\qquad \ell\le d.
\]

The large halos used in MATH-015–020 are therefore safe supersets, but not minimal collision search regions.

## 3. A depth-61 right-side obstruction

For the right start

\[
N_R=b2^{61}+r,
\]

the first 61 shortcut parity bits depend only on

\[
N_R\pmod{2^{61}}=r.
\]

Therefore the candidate-language coefficient-survival prefix through depth 61 can be audited using the canonical nonnegative residue `r` itself; the boundary number `b` is irrelevant for these first 61 parity decisions.

At the frozen published floor

\[
B_{\rm pub}=2^{71},
\]

the exact minimal-counterexample coefficient threshold is

\[
\left(3+\frac1{B_{\rm pub}}\right)^q>2^k.
\]

The certificate checks by exact integer arithmetic that, for every

\[
1\le k\le61,
\]

its minimum integer `q` agrees with

\[
q_{\min}(k)=\min\{q:3^q\ge2^k\}.
\]

An exhaustive exact scan of

\[
r=0,1,\ldots,703
\]

then gives

\[
\boxed{
\text{no }0\le r\le702\text{ survives every coefficient prefix through depth61},
}
\]

while

\[
\boxed{r=703}
\]

is the first surviving right offset.

Thus

\[
\boxed{r_{\min}^{(61)}=703}.
\]

This is a small finite-prefix fact, not a density or probabilistic statement.

## 4. Depth-2109 exclusion

Suppose an internal cross-boundary endpoint collision existed at some depth

\[
61\le k\le2109.
\]

The linear halo theorem would force

\[
r\le d<k/3\le703.
\]

At `k=2109` the final inequality is strict, hence

\[
\boxed{r\le702}.
\]

But every right offset `0..702` has already failed the required candidate prefix by depth 61.

Such a state cannot re-enter the universal-spine candidate language at a later depth.

Therefore

\[
\boxed{
\text{there is no internal adjacent-block same-endpoint candidate pair}
\text{ at any depth }61\le k\le2109.
}
\]

Depth 2110 is the first depth at which the linear halo permits

\[
r=703,
\]

so the present obstruction stops exactly before that new right-offset shell becomes admissible.

## 5. Relation to MATH-015–020

This result does not invalidate the previous exhaustive halos.

Rather, it explains that they audited much larger supersets than necessary.

For example at depth 81:

- MATH-020 used the exact arithmetic-credit halo with width `2^29-1`;
- MATH-021 proves that a same-endpoint collision could only have displacement at most

\[
\left\lfloor\frac{80}{3}\right\rfloor=26.
\]

The large finite scan found strict endpoint ordering; the new theorem shows that **inside the only region where equality could possibly occur**, the right candidate set is already empty.

Thus DSD cause classification becomes sharper:

1. `Q` support mismatch — not the cause in the large halo;
2. large-halo ordered separation — true but stronger than needed computationally;
3. **collision-local right-prefix extinction** — earliest complete exclusion gate through depth 2109.

## 6. Computational significance

The collision search radius changes from a potentially exponential-looking quantity

\[
2^{k-q_{\min}(k)}
\]

to the linear bound

\[
\boxed{\lfloor(k-1)/3\rfloor}.
\]

For the present first-cell internal-boundary endpoint problem, this is not merely an implementation optimization.  It is an exact theorem about where a collision could exist.

The finite anchor `r_min=703` then converts this local theorem into a whole interval of excluded depths without separately scanning depths 82,83,...,2109.

## 7. DSD interpretation

- `D`: the target is specifically **same-endpoint internal adjacent-block coupling**, not all candidate behavior.
- `R`: the collision-relevant resolution is reduced from the arithmetic-credit halo to the exact displacement variable `d`.
- `S`: only offsets satisfying `d<Q/3` can remain collision candidates.
- `E`: right offsets `0..702` are excluded by an exact depth-61 prefix failure.
- `T`: prefix failure is irreversible; an excluded universal-spine state cannot re-enter later.
- `C`: the algebraic displacement bound and the finite `r_min=703` certificate are independently checkable and compose without a density argument.
- `N`: `ESTABLISHED_WITHIN_SCOPE` for internal adjacent-block endpoint coupling through depth 2109.
- `O`: the next genuinely new shell begins at depth 2110 with right offset `r=703`.

## 8. Prohibited upgrades

Do not infer:

- no internal endpoint collision through 2109 `=>` no candidates through 2109;
- block-local endpoint independence `=>` first-cell closure;
- internal-boundary result `=>` outer-window competitor exclusion;
- the depth-2109 interval `=>` arbitrary-depth exclusion;
- linear collision halo `=>` every other Hensel/proof constraint is local in the same radius.

The Collatz conjecture remains open.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_depth_local_linear_collision_halo_certificate.py`

Certificate commit:

`66f5773946be912f6e238fce29c50ddd33c9667a`

Upstream theorem input:

MATH-004 full-first-cell endpoint q-lock and correction bound.

## Next target

Depth 2110 is the first newly admissible collision shell because `r=703` can enter the linear halo.

The next efficient calculation is therefore **not** depth 82.

It is to continue the actual right-offset `r=703` (and then subsequent depth-61-surviving offsets) across the 339 internal boundaries and determine:

1. at which deeper depths each offset remains in the candidate language;
2. whether it can ever share `(Q,E)` with a left offset satisfying the same linear displacement bound;
3. whether another finite-prefix extinction threshold bootstraps the 2109 bound much farther.

# Hensel class-max dominance quotient — MATH-013

## Status

- Collatz conjecture: `OPEN`
- First universal Farey cell: `OPEN`
- Result: `CONFIRMED / EXACT DOMINANCE QUOTIENT / COMPUTATIONAL ACCELERATION`
- New universal Collatz exclusion: **none**

## 1. Question after MATH-012

MATH-012 reduced the root-Hensel arithmetic-credit envelope to the exact scalar gate

\[
d=k-q\le71.
\]

The next question was whether the **remaining** full-Hensel class/maximality information could also be represented by `(k,q,d)` or another very small scalar.

The answer splits in two parts:

1. `(k,q,d)` is **not sufficient**;
2. there is nevertheless an exact downstream-stable dominance quotient that reduces the competitor state space.

## 2. Correction-class coordinates

For a length-`k` parity word `w` with `q` odd bits, write

\[
T^k(N)=\frac{3^qN+C(w)}{2^k}.
\]

Euclidean-divide the correction by `3^q`:

\[
\boxed{C(w)=h(w)3^q+r(w)},
\qquad 0\le r(w)<3^q.
\]

Define the root-Hensel translation-class key

\[
\boxed{\kappa(w)=(q,r(w))=(q,C(w)\bmod3^q)}.
\]

If two words have the same `q` and `r`, then

\[
C(u)-C(w)=(h(u)-h(w))3^q.
\]

Thus the integer difference in `h` is exactly the ordinary-start translation credit within that class.

Whenever that positive credit is separately known to be smaller than the candidate start — uniformly, for example, under the MATH-012 credit-safe gate — a hypothetical minimal counterexample can only use the **maximum `h` representative** of its class.

## 3. Exact information-loss witness for `(k,q,d)`

The previously audited first root-11/no-00 singleton collision at length 24 gives

```text
w = 110110110101010110110101
u = 111111111101011000100100
```

Both have

\[
(k,q,d)=(24,15,9).
\]

But

\[
3^{15}=14{,}348{,}907,
\]

and

\[
C(w)=74{,}913{,}815
=5\cdot3^{15}+3{,}169{,}280,
\]

\[
C(u)=17{,}518{,}187
=1\cdot3^{15}+3{,}169{,}280.
\]

Hence

\[
\kappa(w)=\kappa(u)=(15,3{,}169{,}280),
\]

but

\[
h(w)-h(u)=4.
\]

So `(k,q,d)` cannot determine residual Hensel class/maximality information. The missing information is genuinely correction/ternary-class information, not another relabeling of the even-step budget.

The existing finite root audit establishes the displayed target `w` as the class-maximum representative at this length, while `u` is dominated inside the same class.

## 4. Downstream-stable dominance

The important computational fact is that dominated states never need to return.

Suppose at depth `k`

\[
C=h3^q+r.
\]

### Even next bit

For next parity bit `0`, `C`, `q`, `r`, and `h` are unchanged.

### Odd next bit

For next parity bit `1` at position `k`,

\[
C'=3C+2^k
=h3^{q+1}+(3r+2^k).
\]

Write

\[
3r+2^k=t3^{q+1}+r',
\qquad0\le r'<3^{q+1}.
\]

Then

\[
\boxed{r'=(3r+2^k)\bmod3^{q+1}},
\]

\[
\boxed{h'=h+t}.
\]

Crucially, the child class key `(q+1,r')` depends on `(q,r,k)` but **not** on `h`, while the child score is `h` plus a class-dependent constant.

Therefore if

\[
h_1<h_2
\]

inside one parent class, then after either child transition

\[
h'_1<h'_2
\]

inside the same child class.

Hence a non-maximal class representative can never become maximal at any later depth.

This proves the exact pruning rule:

\[
\boxed{
\text{retain only one maximum }h\text{ per }(q,r)\text{ class before expansion.}
}
\]

This is a true dominance quotient, not a heuristic merge.

## 5. Exact state-space reduction

A quotient dynamic program was run with one class-maximum representative per `(q,r)`.

Counts below exclude the all-zero `q=0` word when comparing with the ordinary nonzero binary word space.

| depth L | nonzero words | class-max states | final-state reduction |
|---:|---:|---:|---:|
| 24 | 16,777,215 | 3,213,594 | 5.220701495× |
| 25 | 33,554,431 | 6,116,463 | 5.485920703× |
| 26 | 67,108,863 | 11,650,325 | 5.760256731× |

The cumulative child-transition counts also fall:

| depth L | full binary child transitions | quotient transitions | reduction |
|---:|---:|---:|---:|
| 24 | 33,554,430 | 7,141,552 | 4.698478706× |
| 25 | 67,108,862 | 13,568,742 | 4.945842584× |
| 26 | 134,217,726 | 25,801,670 | 5.201900730× |

These are exact operation/state counts for the stated finite symbolic computation.

A session-local optimized C++ comparison also showed the quotient construction materially faster than raw all-word class construction at depths 24 and 26, but wall-clock ratios are implementation- and machine-dependent and are not theorem-facing claims.

## 6. What this does and does not accelerate

The quotient avoids expanding correction states that are already permanently dominated with respect to root-Hensel class maximum.

It is useful when the downstream calculation needs the best correction representative per translation class.

However:

- the ternary residue `r=C mod 3^q` is still required;
- `r` grows with `q`, so this is not yet a fixed-size descriptor for the depth-196 regime;
- the quotient does not imply that two states in different classes are equivalent;
- outside a separately valid positive-credit bound, a lower class representative is computationally non-maximal but cannot automatically be converted into a minimal-counterexample contradiction.

Thus MATH-013 gives **real computational pruning**, while also identifying the remaining large-state obstruction: exact ternary-class information.

## 7. DSD interpretation

- `D`: root-Hensel translation class and class-maximum score are explicitly separated.
- `R`: exact finite symbolic words through the audited depth; no coarse phase substitution.
- `S`: one maximum `h` retained per exact `(q,r)` class.
- `E`: lower-`h` representatives are permanently dominated for class-max computation.
- `T`: dominance is proved invariant under both next-bit transitions.
- `C`: known L=24 collision plus exact DP state-count regressions through L=26.
- `N`: `ESTABLISHED_WITHIN_SCOPE`.
- `O`: safe state-space/transition reduction; no global Collatz closure.

## 8. Prohibited upgrades

Do not infer

\[
(k,q,d)\text{ equal}\Longrightarrow\text{same Hensel state}.
\]

Do not infer

\[
(q,r)\text{ equal}\Longrightarrow\text{same full Collatz trajectory}.
\]

Do not infer that a dominated correction representative is a contradictory ordinary start unless the positive integer credit is separately legal for the actual candidate.

Do not extrapolate the finite 24–26 reduction ratios as an asymptotic exponent.

## Reproducibility

Certificate:

`collatz/src/2026_09_08_dsd_hensel_classmax_dominance_quotient.cpp`

Certificate commit:

`098fddb5565b0a9849ce51c50a9c4660c81855be`

Historical singleton/collision audit used as regression anchor:

`collatz/src/no00_root_hensel_max_audit.cpp`

Historical commit:

`414169e3fa272265b08850dbd447eb70fb9a482e`

## Next target

MATH-013 shows that the residual Hensel state cannot collapse to the MATH-012 scalar `d`; exact ternary class residue survives as necessary information.

The next step should test whether, **under the bounded-credit/current-first-cell restrictions actually needed downstream**, the full ternary residue can be replaced by a smaller exact address-local descriptor. If no such bounded quotient exists, the Hensel compression branch should be stopped and the `<2^35` adjacent-block halo invariant should become the primary line.

# Certified lookahead dominance from lower/upper lift bounds

Date: 2026-08-09

Status: **DERIVED SAFE PRUNING RULE + COMPUTATIONAL DIAGNOSTIC**

This note turns the backward Bellman channel into a certified branch-and-bound rule.  It does not assume an unproved state dominance relation.

## 1. Full backward value

Fix target depth `K`, split depth `k`, and `m=K-k`.
For a surviving split state `(r,q,y)`, let

\[
J_m=J_{k,q,m}(3^{-q}y\bmod2^m)
\]

be its exact minimum future lift.
The exact final minimum from this state is

\[
\boxed{V=r+2^kJ_m.}
\]

## 2. Short-lookahead lower bound

For `0<=ell<=m`, let

\[
L_\ell
\]

be the minimum lift integer modulo `2^ell` that preserves the coefficient barrier through only the next `ell` steps.
Equivalently,

\[
L_\ell
=J_{k,q,\ell}(3^{-q}y\bmod2^\ell)
\]

for the truncated target `k+ell`.

Every full feasible lift `C` has a low-`ell` residue

\[
c=C\bmod2^\ell
\]

that is feasible for the truncated problem.  Therefore

\[
c\ge L_\ell
\]

and, since `C>=c`,

\[
\boxed{J_m\ge L_\ell.}
\]

The truncated minima are monotone:

\[
\boxed{
0=L_0\le L_1\le\cdots\le L_m=J_m.
}
\]

Thus even a shallow exact lookahead gives a rigorous lower bound on the full future lift.

## 3. Safe-cylinder upper bound

From `safe-cylinder-gap-bound.md`, let

\[
d=\max(0,a_K-q),
\qquad a_K=\lceil K\log_3 2\rceil.
\]

The explicit all-odd-to-safe completion gives

\[
\boxed{
U=C_*
=
\left[3^{-q}(2^d-1-y)\right]_{2^d},
}
\]

with

\[
J_m\le U<2^d.
\]

Therefore each split state has a certified final interval

\[
\boxed{
 r+2^kL_\ell
\le V
\le
 r+2^kU.
}
\]

## 4. Global safe pruning rule

Let

\[
B=\min_i\left(r_i+2^kU_i\right)
\]

be the best explicit feasible upper bound among the split states.
Since `B` is realized by an actual admissible completion, it is a certified incumbent.

A state `i` satisfying

\[
\boxed{
r_i+2^kL_{\ell,i}>B}
\]

cannot attain the global minimum and may be deleted.

If

\[
r_i+2^kL_{\ell,i}=B,
\]

it cannot improve the incumbent; it may also be removed after one witness attaining `B` is retained.

This pruning is proof-safe because it compares a rigorous lower bound with a rigorous feasible upper bound.  No future-language equivalence is assumed.

## 5. Independent diagnostic

Wolfram exact-integer calculations used the state-specific safe-cylinder upper bound and a shallow lookahead lower bound.  The following counts use strict `<B` to display only states still capable of improving the incumbent:

| K | split k | lookahead ell | split survivors | capable of improving B | certified B |
|---:|---:|---:|---:|---:|---:|
| 20 | 10 | 4 | 64 | 31 | 703 |
| 24 | 12 | 4 | 226 | 159 | 6,471 |
| 28 | 14 | 4 | 734 | 358 | 12,447 |
| 30 | 15 | 5 | 1,295 | 296 | 11,931 |

Thus the deliberately crude incumbent already prunes about 52%, 30%, 51%, and 77% of the split states respectively in these small tests.

These are computational diagnostics, not asymptotic estimates.  The certified incumbents are much weaker than the true value `mu(K)=27` in this range; the purpose is to verify that the bound mechanism is safe and nontrivial even without using the known answer.

## 6. Matrix / channel interpretation

The lower and upper certificates add an interval-valued evaluation to the same E/O transition skeleton:

- lower channel: truncated exact min-plus value `L_ell`;
- upper channel: explicit safe-cylinder witness `U`;
- objective channel: `r + 2^k J`.

A block can be removed whenever its lower envelope lies above the best upper witness.
This is the current rigorous meaning of **certified dominance compression**.

## 7. Next target

The safe-cylinder upper bound is elementary; the main room for improvement is the lower bound.
Useful next steps are:

1. obtain lower bounds on `J` for entire blocks of transformed endpoint residues rather than one state at a time;
2. exploit the exact two-channel set recursion to propagate interval exclusions of small lift values;
3. combine arithmetic residue restrictions with the shallow Bellman lower bound;
4. use any Fourier estimate only as a block exclusion aid, with the final prune certified by the exact min-plus lower bound.

# Exact E/O skew-product state and a compression obstruction

Date: 2026-08-09

Status: **DERIVED REFORMULATION + EXACT COUNTEREXAMPLE TO AN OVER-COMPRESSION**

This note connects the temporary E/O count plane to the exact canonical-residue state already used by `minimal_survivor_branch_bound.cpp`.

## 1. Base plane and fiber state

At depth `k`, let

\[
q=q_k
\]

be the odd-step count, and let `r` be the canonical start residue for the parity prefix, represented in `[0,2^k)`.  Let

\[
y=T^k(r)
\]

be the canonical endpoint of that representative.  Then the exact affine identity is

\[
\boxed{2^k y=3^q r+R.}
\]

Thus the correction channel is reconstructible as

\[
\boxed{R=2^k y-3^q r.}
\]

For step-by-step exact work, the state

\[
\boxed{(k,q;r,y)}
\]

is therefore sufficient and avoids storing `R` independently.

Interpretation:

- `(k,q)` is the coarse E/O count-plane coordinate (`e=k-q`);
- `r` is the canonical-start / min-plus cost channel;
- `y` is the endpoint / carry channel.

The slack is derived from the base plane:

\[
s=q-\lceil k\log_3 2\rceil.
\]

## 2. Exact lift bit

Suppose the next desired parity is

\[
b\in\{0,1\}.
\]

The two lifts of the canonical start modulo `2^(k+1)` are

\[
r\quad\text{and}\quad r+2^k.
\]

Write the chosen lift as

\[
r'=r+c2^k,
\qquad c\in\{0,1\}.
\]

Because

\[
T^k(r+c2^k)=y+c3^q
\]

and `3^q` is odd, the parity toggles when `c` toggles.  Hence the unique carry/lift bit is

\[
\boxed{c=b\oplus(y\bmod2).}
\]

This is exactly the rule implemented in `minimal_survivor_branch_bound.cpp`.

## 3. Exact transition equations

First form

\[
\widetilde y=y+c3^q,
\qquad
r'=r+c2^k.
\]

If the next channel is even (`b=0`),

\[
\boxed{
(k,q;r,y)
\mapsto
(k+1,q;\ r+c2^k,\ (y+c3^q)/2).
}
\]

If the next channel is odd (`b=1`),

\[
\boxed{
(k,q;r,y)
\mapsto
(k+1,q+1;\ r+c2^k,\ (3(y+c3^q)+1)/2).
}
\]

The coefficient-survival barrier is then applied to the new base coordinate `(k+1,q')`.

## 4. Conditional affine matrices on the fiber

For fixed base `(k,q)` and fixed lift bit `c`, use homogeneous fiber coordinates

\[
\mathbf v=(r,y,1)^T.
\]

The even branch is

\[
A_{E,c}^{(k,q)}=
\begin{pmatrix}
1&0&c2^k\\
0&1/2&c3^q/2\\
0&0&1
\end{pmatrix},
\]

and the odd branch is

\[
A_{O,c}^{(k,q)}=
\begin{pmatrix}
1&0&c2^k\\
0&3/2&(3c3^q+1)/2\\
0&0&1
\end{pmatrix}.
\]

The lift bit is not free: it is gated by

\[
c=b\oplus(y\bmod2).
\]

Therefore the exact dynamics is a **skew-product affine system**:

1. the E/O count plane updates `(k,q)`;
2. endpoint parity selects the lift/carry;
3. the selected affine matrix updates the fiber `(r,y)`.

This is a more faithful matrix model than a single 2x2 count matrix because it preserves the arithmetic realization of each parity prefix.

## 5. Why one minimum per slack layer is not enough

A tempting compression is to retain only the smallest canonical residue `r` in each slack layer.  This is not safe.

At depth 5, both parity prefixes

\[
w_7=11101,
\qquad
w_{27}=11011
\]

survive the coefficient barrier and have the same odd count `q=4`, hence the same slack `s=0`.

Their canonical starts and endpoints are

\[
(r,y)=(7,20)
\]

for `11101`, and

\[
(r,y)=(27,71)
\]

for `11011`.

Thus at depth 5,

\[
7<27.
\]

Now require the next parity to be odd.

For the `7` state, `y=20` is even, so

\[
c=1,
\qquad
r'=7+32=39.
\]

For the `27` state, `y=71` is odd, so

\[
c=0,
\qquad
r'=27.
\]

Therefore the ordering reverses:

\[
\boxed{39>27.}
\]

Both children are coefficient-surviving depth-6 prefixes with slack `s=1`.

Hence the rule

> keep only the minimum canonical residue in each `(k,s)` layer

can discard the future minimizer and is invalid as an exact dynamic program.

This exact counterexample was independently checked by direct integer enumeration and by Wolfram evaluation of the trajectories.

## 6. What state may be safely contracted

The example shows that slack alone does not determine the lift cost.  At minimum, a future-sensitive contraction must preserve enough information to recover the carry sequence.

The current exact solver retains the full endpoint `y`, which is sufficient.  A reduced matrix/transfer construction must therefore justify any replacement of `y` by a smaller carry state; it cannot assume such a reduction.

This also explains why the cross-base residue/carry bridge remains a genuine source of complexity in the existing notes.

## 7. Recommended next matrix target

The next safe target is not a scalar recurrence for one boundary path.  It is a block operator over

\[
\boxed{(s;\ r,y)}
\]

or an equivalent rigorously sufficient quotient, with:

- sparse E/O slack transitions;
- nonnegative min-plus cost increments `c 2^k` on `r`;
- endpoint/carry gating through `y mod 2`;
- exact coefficient-barrier pruning;
- optional interval/Fourier contraction only after a proof that the quotient preserves the target extremum.

Any proposed state merge should first be tested against exact small-depth equivalence: two states may be merged only if their allowed future channel languages and future min-plus costs are provably interchangeable for the target theorem.

# Exact-count Bellman formula for first-crossing prefix minima

Date: 2026-08-09

Status: **DERIVED EXACT RECURRENCE + FINITE CROSS-CHECK**

This note specializes the existing two-channel cyclic-successor Bellman recurrence to one fixed first-coefficient-crossing layer. It determines the least canonical start in a fixed prefix class without scanning all parity completions. It is an exact reformulation, not a global Collatz/CST proof.

## 1. Fixed first-crossing layer

Fix total odd count `Q` and

\[
\sigma=\lceil Q\log_2 3\rceil,
\qquad 3^Q<2^\sigma.
\]

A first-crossing word of length `sigma` must satisfy

\[
3^{q_j}\ge2^j\qquad(1\le j<\sigma)
\]

and contain exactly `Q` odd steps at depth `sigma`.

Suppose a fixed parity/odd-position prefix has been realized through depth `k`, with exact canonical state

\[
(k,q;r,y).
\]

Put

\[
m=\sigma-k,
\qquad u=Q-q.
\]

Here `u` is the exact number of odd channels that must still occur.

## 2. Exact-count transformed suffix set

Let

\[
S^{(u)}_{k,q,m}\subset \mathbb Z/2^m\mathbb Z
\]

be the transformed suffix residues producing exactly `u` future odd steps, preserving the coefficient barrier at every intermediate depth, and reaching the prescribed first crossing at the terminal depth.

At `m=0`,

\[
S^{(u)}_{k,q,0}=\begin{cases}\{0\},&u=0,\\\varnothing,&u\ne0.\end{cases}
\]

For `m>=1`, retain only branches whose remaining odd count is feasible. For an intermediate step (`m>1`) the E branch requires

\[
3^q\ge2^{k+1},
\]

and the O branch requires

\[
3^{q+1}\ge2^{k+1}.
\]

At the final step (`m=1`) the intermediate-barrier test is omitted; terminal exact count `u=0` after the branch and the fixed pair `(Q,sigma)` supply the crossing condition.

With modulus `M=2^m`, the transformed channel recursion is

\[
S_E=2S^{(u)}_{k+1,q,m-1}\pmod M,
\]

\[
S_O=2S^{(u-1)}_{k+1,q+1,m-1}-3^{-(q+1)}\pmod M.
\]

Thus

\[
\boxed{S^{(u)}_{k,q,m}=S_E\cup S_O}
\]

with only feasible/admissible channels included. The two images have opposite parity and are disjoint.

## 3. Exact-count cyclic successor

For

\[
\xi=3^{-q}y\pmod{2^m},
\]

define

\[
\boxed{
J^{(u)}_{k,q,m}(\xi)
=
\min_{s\in S^{(u)}_{k,q,m}}[s-\xi]_{2^m}.
}
\]

This is the least future canonical lift integer among completions with the required final odd count.

The scalar E/O recurrence is the previous Bellman recurrence with the extra count coordinate `u`:

- E keeps `u` unchanged;
- O replaces `u` by `u-1`;
- impossible count states return `+infinity`.

For E, writing

\[
b_E=\xi\bmod2,
\qquad
h_E=\left\lceil\xi/2\right\rceil\pmod{2^{m-1}},
\]

we have

\[
J_E=2J^{(u)}_{k+1,q,m-1}(h_E)+b_E.
\]

For O, put

\[
g=[3^{-(q+1)}]_{2^m},
\qquad t=(\xi+g)\bmod2^m,
\]

\[
b_O=t\bmod2,
\qquad h_O=\left\lceil t/2\right\rceil\pmod{2^{m-1}},
\]

and

\[
J_O=2J^{(u-1)}_{k+1,q+1,m-1}(h_O)+b_O.
\]

Hence

\[
\boxed{
J^{(u)}_{k,q,m}(\xi)=\min\{J_E,J_O\}_{\rm admissible}.
}
\]

## 4. Least canonical start in a fixed prefix class

All completions of the fixed depth-`k` prefix have starts

\[
x=r+2^k j.
\]

Therefore the class minimum is exactly

\[
\boxed{
x_*(Q,\pi)=r+2^kJ^{(Q-q)}_{k,q,\sigma-k}(3^{-q}y).
}
\]

This is the exact quantity required by `correction-gap-common-minimizer.md`.

## 5. q=29 check

At `Q=29`, `sigma=46`:

### dangerous prefix `(0,1,2)`

The prefix state after depth `k=3` is

\[
(k,q;r,y)=(3,3;7,26).
\]

The exact-count recurrence gives

\[
J=428,
\]

and hence

\[
\boxed{x_*=7+2^3\cdot428=3431}.
\]

### dangerous prefix `(0,1,3)`

The prefix state after depth `k=4` is

\[
(k,q;r,y)=(4,3;11,20).
\]

The recurrence gives

\[
J=305,
\]

and

\[
\boxed{x_*=11+2^4\cdot305=4891}.
\]

These match the independently scanned first-crossing minima and the independent Wolfram trajectory check stored in the correction-gap note.

A straightforward memoized Python evaluation visited about 5.56 million states for the first class and 2.44 million for the second. This is a finite diagnostic only: exactness is achieved, but no asymptotic state contraction follows from this recurrence alone.

## 6. Proof-program consequence

The unresolved `x_*` quantity is no longer undefined: it is one exact constrained cyclic-successor value. The remaining problem is structural complexity.

Two complementary reductions are therefore available:

1. compute `x_*` exactly by this final-count Bellman recurrence;
2. for proof/pruning, avoid full `J` whenever a threshold/interval certificate already proves that no low-lift completion can be paradoxical.

The latter remains the preferred asymptotic direction.
# First resonance: anchored Christoffel/Farey DAG compression

Date: 2026-08-26

Status: **exact word-structure theorem + finite certificate.** This compresses the first-resonance mechanical gap word but does not yet compress the Hensel boundary state space. It does not prove the Collatz conjecture.

## 1. Anchored mechanical word

Set

\[
P=A-Q=42150895613,
\qquad
Q=72057431991.
\]

Because

\[
{A\over Q}=1+{P\over Q},
\]

the first-resonance mechanical gap sequence is

\[
g_{n+1}=1+m_n,
\]

where

\[
\boxed{
m_n=\left\lfloor{(n+1)P\over Q}\right\rfloor
-\left\lfloor{nP\over Q}\right\rfloor,
\qquad0\le n<Q.}
\]

The binary word `m_0...m_{Q-1}` is the anchored lower mechanical/Christoffel word of slope `P/Q`.  No conjugacy or cyclic rotation is introduced; the intercept is exactly zero.

## 2. Exact Farey-parent factorization

Let `0<p<q` and `gcd(p,q)=1`.  Define the lower Farey parent by

\[
q_-:=p^{-1}\pmod q,
\qquad1\le q_-<q,
\]

\[
\boxed{p_-:={pq_- -1\over q}.}
\]

Then

\[
pq_- -p_-q=1,
\]

so

\[
{p_-\over q_-}<{p\over q}.
\]

Define the other parent by

\[
p_+=p-p_-,
\qquad
q_+=q-q_-.
\]

Then

\[
p_+q-pq_+=1,
\]

and hence

\[
{p\over q}<{p_+\over q_+}.
\]

Thus

\[
{p\over q}={p_-+p_+\over q_-+q_+}
\]

is the Farey mediant of its two parents.

Let

\[
C_{p,q}(n)
=
\left\lfloor{(n+1)p\over q}\right\rfloor
-
\left\lfloor{np\over q}\right\rfloor.
\]

Then the **anchored** word factors exactly as

\[
\boxed{C_{p,q}=C_{p_-,q_-}\,C_{p_+,q_+}.}
\]

## 3. Elementary proof of the anchored factorization

The determinant relation gives

\[
pq_- -p_-q=1.
\]

For `0<=x<=q_-`,

\[
{px\over q}-{p_-x\over q_-}
={x\over qq_-}.
\]

For `0<x<q_-`, the fractional part of `p_-x/q_-` is either zero or at least `1/q_-`; the perturbation above is strictly less than `1/q_-`. Therefore

\[
\left\lfloor{px\over q}\right\rfloor
=
\left\lfloor{p_-x\over q_-}\right\rfloor
\qquad(0\le x\le q_-).
\]

At the splitting point,

\[
\left\lfloor{pq_-\over q}\right\rfloor=p_-.
\]

Now write `x=q_-+s`, `0<=s<=q_+`.  Using

\[
p_+q-pq_+=1,
\]

one obtains

\[
{p(q_-+s)\over q}-p_-
-
{p_+s\over q_+}
={q_+-s\over qq_+}.
\]

Again this perturbation is too small to cross an integer grid point for `0<s<q_+`, and the endpoints agree. Hence

\[
\left\lfloor{p(q_-+s)\over q}\right\rfloor-p_-
=
\left\lfloor{p_+s\over q_+}\right\rfloor.
\]

Taking consecutive differences proves the concatenation formula.

Thus the factorization is internal arithmetic; no external Christoffel convention is needed for the proof.

## 4. First-resonance root split

For

\[
(P,Q)=(42150895613,72057431991),
\]

the exact lower and upper Farey parents are

\[
\boxed{
(P_-,Q_-)
=(38297853692,65470613321)
}
\]

and

\[
\boxed{
(P_+,Q_+)
=(3853041921,6586818670).
}
\]

Therefore the entire anchored root word factors as

\[
\boxed{
C_{42150895613,72057431991}
=
C_{38297853692,65470613321}
\,
C_{3853041921,6586818670}.
}
\]

The first factor corresponds to the lower semiconvergent adjacent to the repaired first resonance; the second is the previous convergent block.

## 5. Full memoized Farey DAG

Apply the same parent factorization recursively until reaching the one-letter bases

\[
C_{0,1}=0,
\qquad
C_{1,1}=1.
\]

If repeated rational blocks are memoized, the entire 72-billion-letter word uses exactly

\[
\boxed{138}
\]

distinct block nodes.

The expanded root has exactly

\[
\boxed{72057431991}
\]
letters and

\[
\boxed{42150895613}
\]
ones, while the memoized DAG depth is only

\[
\boxed{136}.
\]

Thus the **word-length problem is solved structurally**: every block transfer needed by the first-resonance mechanical word can in principle be computed from 138 distinct lower-level block transfers rather than 72 billion individual letters.

## 6. Connection to the min-plus operator

Relabel

\[
0\mapsto1,
\qquad
1\mapsto2
\]

to recover the Collatz mechanical gaps.

For every DAG node `C_{p,q}=UV`, the exact two-boundary operator obeys

\[
\mathcal T_{C_{p,q}}
=
\mathcal T_U
\star_{\lambda(U)}
\mathcal T_V,
\]

where

\[
\lambda(U)={3^{|U|}\over2^{G(U)}}
\]

and `star` is the weighted min-plus convolution from

`2026-08-26-two-boundary-minplus-block-composition.md`.

This removes the `Q`-step iteration from the intended proof computation.

## 7. What remains

The remaining obstruction is **not word length**. It is the interface state space:

\[
(K\bmod3^r,\ p,\ C).
\]

The finite-horizon quotient and Pareto dominance are exact, but a macroscopic block still has exponentially many possible carry residues in principle.

The next proof-level target is therefore sharply stated:

> Find a DAG-compatible interface compression or Bellman dual potential that bounds the minimum two-boundary cost without enumerating all `3^r` carry classes.

Any proposed compression can be tested against the exact terminal low-support certificates before being used on the 138-node root DAG.

## 8. DSD audit interpretation

The reduction now separates two independent complexity sources:

\[
\boxed{
\text{word complexity}=138\text{ exact DAG nodes}
}
\]

versus

\[
\boxed{
\text{state complexity}=\text{still open}.
}
\]

This prevents the proof program from confusing a solved combinatorial-length problem with the remaining arithmetic boundary-state problem.

Companion certificate:

`collatz/src/first_resonance_anchored_christoffel_dag_certificate.py`.

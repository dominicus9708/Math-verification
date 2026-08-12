# Aperiodic terminal checkpoint: signed-skew input and finite-support lift output

Date: 2026-08-12

Status: **current most compressed aperiodic proof target**. This checkpoint supersedes `Phi(s) in N` as the preferred operational naturalness condition by using exact canonical formation lift digits. It also records the negative control that dynamic resets do not necessarily consume new lift bits.

## 1. Signed-skew input

Put

\[
\gamma:=\log_2 3,
\qquad
r_q:=\lfloor(q+1)\gamma\rfloor-\lfloor q\gamma\rfloor\in\{1,2\}.
\]

For an odd-event exponent code define

\[
A_q:=\sum_{i<q}v_i,
\qquad
s_q:=\lfloor q\gamma\rfloor-A_q.
\]

Then

\[
\boxed{v_q=s_q+r_q-s_{q+1}}
\]

and local admissibility is exactly

\[
\boxed{s_{q+1}\le s_q+r_q-1.}
\]

Any nonperiodic positive-integer no-first-descent counterexample must also satisfy

\[
\boxed{\sum_{i<q}2^{-s_i}=O_N(q^{1/9})}
\]

and the critical-density recurrence

\[
\boxed{\liminf_{q\to\infty}\frac{s_q}{q}=0.}
\]

## 2. Canonical formation transducer

For the completed first `q` odd events let

\[
\rho_q\in\{1,3,\ldots,2^{A_q+1}-1\}
\]

be the least positive start representative.

Appending valuation `v_q` produces the unique lift output

\[
\boxed{t_q\in\{0,1,\ldots,2^{v_q}-1\}}
\]

with

\[
\boxed{\rho_{q+1}=\rho_q+t_q2^{A_q+1}.}
\]

The carry state

\[
y_q=\frac{3^q\rho_q+B_q}{2^{A_q}}
\]

obeys

\[
\boxed{2^{v_q}y_{q+1}=3y_q+1+2t_q3^{q+1}.}
\]

The digit itself is

\[
\boxed{
t_q\equiv
3^{-(q+1)}
\left(2^{v_q-1}-\frac{3y_q+1}{2}\right)
\pmod{2^{v_q}}.
}
\]

Thus the full object is a deterministic transducer

\[
\boxed{
(s_q;\ r_q)
\longmapsto
(v_q,y_q,t_q).
}
\]

## 3. Ordinary-integer naturalness is finite-support output

The exact binary decomposition is

\[
\boxed{
\frac{\rho_q-1}{2}
=\sum_{i<q}t_i2^{A_i}.
}
\]

The bit blocks of distinct `t_i` are disjoint. Hence an infinite signed-skew code comes from one finite positive odd integer iff

\[
\boxed{t_q=0\text{ for all sufficiently large }q.}
\]

Equivalently, if the stabilized start is `N`,

\[
\boxed{
\frac{N-1}{2}=\sum_{q\ge0}t_q2^{A_q}
}
\]

is its finite ordinary binary expansion.

If `B=floor(log_2 N)+1` is the bit length, then

\[
\boxed{t_q=0\quad\forall q\ge B-1.}
\]

## 4. Finite information budget

Because the lift blocks are disjoint,

\[
\boxed{
\sum_q\operatorname{popcount}(t_q)
=
\operatorname{popcount}\left(\frac{N-1}{2}\right).
}
\]

This is a true finite **formation** information budget.

However it is not a dynamical excursion budget.

After the floor has stabilized, `y_q` is the actual orbit state and therefore every subsequent actual valuation satisfies

\[
\boxed{t_q=0}
\]

by definition, including arbitrarily deep valuations if such events occur.

Concrete finite examples such as `N=63` and `N=703` exhibit valuation-4 events after formation stabilization with zero lift output.

Hence

\[
\boxed{
\text{deep reset/crossing}\not\Rightarrow\text{new formation bit}.
}
\]

Any proof that charges each future excursion to a fresh bit of the original integer is invalid without a separate forcing lemma.

## 5. Refined terminal theorem

The preferred aperiodic closure statement is now:

### Finite-Support Lift-Output Exclusion

There is no infinite integer sequence `s_q` such that

\[
\boxed{s_{q+1}\le s_q+r_q-1,}
\]

\[
\boxed{\sum_{i<q}2^{-s_i}=O(q^{1/9}),}
\]

\[
\boxed{\liminf s_q/q=0,}
\]

and whose canonical formation transducer satisfies

\[
\boxed{t_q=0\text{ eventually}.}
\]

This is equivalent to the earlier signed-skew ordinary-integer naturalness target, but it exposes the exact missing arithmetic condition as finite binary support.

## 6. What remains after output stabilization

Once `t_q=0` permanently, the carry recurrence is simply the actual Syracuse recurrence

\[
\boxed{2^{v_q}y_{q+1}=3y_q+1.}
\]

Therefore the hard part cannot be solved by further formation bookkeeping alone. At that point one fixed positive integer has already been fully formed, and the remaining task is to prove that its deterministic orbit cannot realize the signed-skew harmonic/critical regime.

This is the precise boundary between the solved formation problem and the still-open orbit-dynamics problem.

## 7. Final proof architecture

The full Collatz proof remains reduced to two terminal exclusions:

\[
\boxed{
\begin{array}{ll}
\textbf{Periodic:}&\text{exclude nontrivial positive exact-return cycles},\\[1mm]
\textbf{Aperiodic:}&\text{prove Finite-Support Lift-Output Exclusion}.
\end{array}
}
\]

The second statement is the current preferred operational form of the aperiodic hard core.

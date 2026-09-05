# A0 s=1 sector is an exact ballot renewal point

Date: 2026-08-27

Status: **SAFE exact combinatorial/Diophantine theorem** inside the repaired first-crossing line. It does not prove the Collatz conjecture.

## 1. Threshold height

Let

\[
\alpha=\log_3 2,
\qquad
b(n)=\lceil\alpha n\rceil.
\]

For an A0 first-crossing word, let `q_n` be the number of odd steps in the first `n` accelerated time steps and define

\[
\boxed{h(n):=q_n-b(n).}
\]

Because `A0` is the first coefficient-subcritical time,

\[
h(n)\ge0
\qquad(0\le n<A_0).
\]

At the crossing,

\[
q_{A_0}=Q_0,
\qquad
b(A_0)=Q_0+1,
\]
so

\[
\boxed{h(A_0)=-1.}
\]

## 2. Ten-J0 threshold is exact

Put

\[
t_0=10J_0,
\qquad
j_0=10R_0+1.
\]

Since

\[
\delta_J=J_0\ln2-R_0\ln3>0,
\]
we have

\[
10R_0<\alpha t_0.
\]

The exact rational logarithmic enclosure also gives

\[
\alpha t_0<10R_0+1.
\]

Therefore

\[
\boxed{b(t_0)=j_0.}
\]

In the `s=1` sector,

\[
q_{t_0}=j_0,
\]
so

\[
\boxed{h(t_0)=0.}
\]

Thus the hard surplus sector is exactly the sector in which the first-crossing ballot path returns to the threshold boundary at the tenth-J0 checkpoint.

## 3. Exact language factorization

The global height path has

\[
h(0)=0,
\qquad
h(n)\ge0\ (n<A_0),
\qquad
h(A_0)=-1.
\]

In the `s=1` sector it additionally satisfies

\[
h(t_0)=0.
\]

Hence the word decomposes exactly into two ballot objects:

### Pre block

\[
\boxed{
0\to0
\text{ nonnegative ballot bridge on }[0,t_0].
}
\]

### Tail block

Starting from the renewed height zero at `t0`,

\[
\boxed{
0\to-1
\text{ first-passage bridge on }[t_0,A_0],
}
\]

which remains nonnegative at every proper intermediate time and crosses below zero only at the final A0 step.

This is stronger than merely saying `s=1` means low surplus. It gives an exact renewal decomposition of the coefficient-survival language.

## 4. Relation to the displacement factorization

The previous ordered-position audit proved that `s=1` also gives

\[
d_{j_0+1}\in\{0,1\}
\]

and makes the cross-checkpoint ordering inequality automatic.

Therefore the same checkpoint simultaneously factorizes:

1. the time/odd-count ballot language;
2. the ordered displacement language;
3. the raw reachable-Xi invariant sum;
4. the physical orbit into the ordinary state `Z=T^{t0}(X)`.

The hard branch now has a genuine renewal node rather than an artificial proof split.

## 5. DSD interpretation

The checkpoint is supported by four independent descriptions of the same structural event:

\[
\boxed{
\begin{aligned}
&s=1,\\
&h(t_0)=0,\\
&\text{no odd-event transport across }t_0,\\
&X\to Z\to Y\text{ ordinary-state factorization}.
\end{aligned}}
\]

This is exactly the kind of descriptor coincidence that is safe to promote: the arrows are proved independently from the definitions and arithmetic, rather than inferred from a desired contradiction.

## 6. Next gate

The pre and tail reachable sets should now be built as **ballot-constrained boundary maps** rather than unrestricted ordered-control sets:

\[
\mathcal Z_{\rm pre}^{\rm ballot},
\qquad
\mathcal Z_{\rm tail}^{\rm first-pass}.
\]

The next proof target is the ordinary checkpoint same-address intersection

\[
\boxed{
\mathcal Z_{\rm pre}^{\rm ballot}
\cap
\mathcal Z_{\rm tail}^{\rm first-pass}
\cap(2^{72},2^{73}).
}
\]

If this set is empty, the `s=1` branch closes without invoking the defect ceiling. If it is nonempty, only the surviving ordinary checkpoint classes need the final physical gap/defect audit.

Companion exact certificate:

`collatz/src/A0_s1_exact_ballot_renewal_certificate.py`.

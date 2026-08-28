# A0 s=1 long-membership frontier

Date: 2026-08-28

Status: **current Route-B continuation point after the first-defect shell closure**. This note separates exact search representation from finite pruning and from the still-open long correction-language membership problem.

## 1. Starting gate

The unresolved Route-B question remains

\[
C_{\rm req}(X,Z)\in\mathcal C_{\rm pre}\ ?
\]

with

\[
t_0=104398605910,
\qquad
j_0=65868186701.
\]

Correction injectivity means that for a fixed physical target there is at most one full parity word. The problem is therefore not to estimate the size of the correction language, but to decide whether the unique target word exists and satisfies every required bridge predicate.

## 2. Exact prefix-channel transducer

For a parity prefix of depth `h`, let

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m.
\]

Here `r` is the canonical residue, `q` is the prefix odd count, and `y=T^h(r)`.

For desired next parity bit `b`, parity of `y+3^q m` fixes one bit of `m`:

\[
m=m_0+2k,
\qquad
m_0\equiv b-y\pmod2.
\]

The exact child is

\[
r'=r+2^h m_0.
\]

If `b=0`,

\[
q'=q,
\qquad
y'=\frac{y+3^q m_0}{2}.
\]

If `b=1`,

\[
q'=q+1,
\qquad
y'=\frac{3y+3^{q+1}m_0+1}{2}.
\]

Thus

\[
X=r'+2^{h+1}k,
\qquad
T^{h+1}(X)=y'+3^{q'}k.
\]

This is an exact lossless channel refinement, not a statistical approximation.

Certificate:

- `collatz/src/A0_s1_prefix_channel_transducer_certificate.py`

## 3. Monotone irreversible correction defect

Let `t_r` be the threshold position of odd rank `r`, and `a_r` the actual position. Pure ballot gives

\[
a_r\le t_r.
\]

Define the accumulated normalized defect

\[
\eta_h
=
\sum_{a_r<h}
3^{-r}\left(2^{t_r}-2^{a_r}\right).
\]

Every term is nonnegative. Therefore no suffix can repair defect already accumulated by a prefix:

\[
\boxed{\eta_{h'}\ge\eta_h\quad(h'\ge h).}
\]

At fixed total odd count,

\[
\frac{C_{\rm th}-C}{2^{t_0}}
=
\lambda\eta,
\qquad
\lambda=\frac{3^{j_0}}{2^{t_0}}.
\]

The existing directed Christoffel real envelope converts every prefix defect lower bound into a SAFE physical upper bound on `X`. Therefore a whole prefix cylinder may be rejected when its least physical `X` already exceeds the upper bound implied by its irreversible defect.

Certificate:

- `collatz/src/A0_s1_prefix_defect_membership_pruning_certificate.py`

The shell-conditioned first-75 version removes an additional `40,854,445` ordinary integers from the previously retained dyadic-shell union. No whole shell is removed by the defect magnitude alone.

## 4. Direct closure of the high first-defect shells

The shell-conditioned upper bounds make the high-valuation shells small enough for exact ordinary-orbit exhaustion.

The ten shells

\[
\boxed{
40,43,46,48,51,54,56,59,62,65
}
\]

contain exactly

\[
455010884
\]

ordinary integers under their respective SAFE shell bounds.

Among them,

\[
22346636
\]

survive pure ballot through depth 75 with `d_75>=8`.

Every one of those candidates subsequently loses pure ballot, with the latest first failure at prefix

\[
\boxed{454}.
\]

Hence all ten shells are closed.

Certificate:

- `collatz/src/A0_s1_first_defect_f40plus_closure_certificate.cpp`

This is a finite necessary-condition closure. It does not use C4F and does not promote any finite survivor elsewhere to membership.

## 5. Remaining first-defect theorem

The first-defect condition is now strengthened from 24 possibilities to

\[
\boxed{
F_{\rm rem}
=
\{2,5,8,10,13,16,18,21,24,27,29,32,35,37\}.
}
\]

Thus every remaining physical candidate satisfies

\[
\boxed{
v_2(X-X_{\rm th})\in F_{\rm rem}}
\]

and in particular

\[
\boxed{v_2(X-X_{\rm th})\le37.}
\]

This means the candidate parity word must disagree with the threshold by zero-based position 37 at the latest.

## 6. Exact 14-root search forest

For each `f in F_rem`, the parity prefix is forced to agree with the threshold before `f` and to make the first `0->1` disagreement at `f`.

Consequently every remaining shell is represented by one exact root channel

\[
\boxed{
X=r_f+2^{f+1}m,
\qquad
m_{\min,f}\le m\le m_{\max,f}.
}
\]

The corresponding endpoint is

\[
T^{f+1}(X)=y_f+3^{q_f}m.
\]

The 14 root cylinders are pairwise disjoint. Refinement by the next parity bit chooses one parity of `m`, writes `m=m_0+2k`, and exactly partitions the parent integer interval into two child intervals.

Certificate:

- `collatz/src/A0_s1_14root_long_membership_forest_certificate.py`

The total ordinary integer parameter count across these SAFE-pruned roots is

\[
125072439875999947649.
\]

This cardinality is recorded only as a deterministic count. It is not treated as a probability and is not multiplied by unrelated marginal ratios.

## 7. What is now closed

### EXACT

- prefix-channel affine law;
- one-bit channel transducer;
- exact child interval partition;
- 14-root arithmetic representation of the remaining first-defect cases.

### CERTIFIED / SAFE

- shell-conditioned irreversible defect minima;
- shell-conditioned physical `X` bounds;
- complete finite closure of all first-defect shells `f>=40` in the certified list;
- resulting bound `v2(X-X_th)<=37`.

### REJECTED inference

None of the following is allowed:

- a surviving arithmetic channel is a full pre-bridge;
- an interval overlap is correction-language membership;
- a shallow endpoint exposure proves same-orbit connectivity;
- the pure-ballot/channel state automatically preserves C4F;
- marginal pruning fractions may be multiplied without independence.

## 8. Immediate next operation

The next algorithm should start from the 14 roots, not from the full physical shell and not from all `2^72` parity addresses.

For each root/child state retain at least

\[
(h,r,y,q,m_{\min},m_{\max},\eta_{\rm floor})
\]

plus whatever additional finite memory is proved necessary for the next exact formation predicate.

Use three legal rejection rules before any further split:

1. pure-ballot failure;
2. empty physical parameter interval;
3. irreversible-defect upper-bound failure.

At depth 72, every surviving cylinder is a singleton ordinary `X`, after which the actual finite orbit is deterministic.

The unresolved hard step is still to replace bit-by-bit refinement by a **proved block jump** compatible with the Christoffel/Stern-Brocot decomposition, so that reaching depth `t0` does not require `O(t0)` individual transitions.

Therefore the next mathematical target is:

\[
\boxed{
\text{derive an exact multi-bit/block transducer for }(r,y,q,m\text{-interval},\eta)
\text{ and prove its legal merge conditions.}
}
\]

Full A0 s=1 membership, C4F compatibility, Route A, all `s>=2` sectors, and the global Collatz conjecture remain OPEN.

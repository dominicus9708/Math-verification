# A0 s=1 Route-B — interval four-state cylinder compression

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Result

The previous projective interval theorem showed that

\[
\Pi_d(I)=(|I|,L\bmod2^d)
\]

is sufficient for finite-horizon interval-payload transitions.

A stronger fact holds when one fixes a residue depth `i` and considers **all** `2^i` parameter cylinders of one consecutive parent interval.

They produce at most four distinct child interval payload types.

---

## 2. Normal form

Let

\[
I=[L,U]\cap\mathbb Z,
\qquad
N=U-L+1,
\]

and put

\[
M=2^i.
\]

Write Euclidean divisions

\[
L=QM+s,
\qquad 0\le s<M,
\]

and

\[
N=tM+u,
\qquad 0\le u<M.
\]

For residue

\[
a\in\{0,1,\ldots,M-1\},
\]

write

\[
m=a+Mn.
\]

The exact child interval is

\[
I_a=
\left[
\left\lceil\frac{L-a}{M}\right\rceil,
\left\lfloor\frac{U-a}{M}\right\rfloor
\right]\cap\mathbb Z.
\]

---

## 3. Lower-endpoint formula

Because

\[
\frac{L-a}{M}=Q+\frac{s-a}{M}
\]

and `-(M-1) <= s-a <= M-1`,

\[
\left\lceil\frac{s-a}{M}\right\rceil
=
\begin{cases}
1,&a<s,\\
0,&a\ge s.
\end{cases}
\]

Therefore

\[
\boxed{
L_a'=Q+\mathbf 1_{a<s}.
}
\]

Across all `M` residue cylinders the child lower endpoint has only the two possible values

\[
Q,\qquad Q+1.
\]

---

## 4. Cardinality formula

A consecutive interval of length

\[
N=tM+u
\]

contains `t` complete turns through all residues modulo `M`, followed by `u` extra consecutive residues beginning at `s=L mod M`.

Hence residue `a` occurs `t+1` times precisely when it lies in the circular interval

\[
H=\{s,s+1,\ldots,s+u-1\}\pmod M.
\]

Equivalently,

\[
\boxed{
N_a=t+\mathbf 1_{(a-s)\bmod M<u}.
}
\]

Thus child cardinality also has only two possible values:

\[
t,\qquad t+1.
\]

When `t=0`, the `t` class is simply empty.

---

## 5. Four-state theorem

Combining the two binary flags gives

\[
\boxed{
(L_a',N_a)
=
\left(
Q+\mathbf1_{a<s},
\;t+\mathbf1_{(a-s)\bmod M<u}
\right).
}
\]

Therefore among all nonempty residue children at depth `i`,

\[
\boxed{
\#\{(L_a',N_a):I_a\ne\varnothing\}\le4.
}
\]

Because every projective interval state is a reduction of `(L_a',N_a)`, for every remaining precision `d-i` one also has

\[
\boxed{
\#\{\Pi_{d-i}(I_a):I_a\ne\varnothing\}\le4.
}
\]

This bound is independent of `i`, `N`, and the magnitude of `L`.

---

## 6. Compact residue description of the four cells

The lower-endpoint flag divides the residue line into the two ordinary intervals

\[
[0,s-1],
\qquad
[s,M-1].
\]

The heavy-cardinality flag is the circular interval `H`; its complement is another circular interval.

A circular interval modulo `M` is representable by at most two ordinary intervals in `[0,M-1]`.

Hence every joint flag cell

\[
\{a:\mathbf1_{a<s}=\epsilon,
\ \mathbf1_{(a-s)\bmod M<u}=\eta\}
\]

is the intersection of one ordinary interval with one circular interval, and therefore is a union of at most two ordinary residue intervals.

Thus the **entire interval-payload classification of all `2^i` residue cylinders** is represented by at most four classes, each with at most two ordinary residue intervals.

No residue-by-residue payload enumeration is required.

---

## 7. Relation to family-cover induction

The result separates two sources of apparent combinatorial growth.

### Payload growth

For one consecutive parent interval, the interval payload contributes at most four states at every fixed cylinder depth.

This part is now exactly controlled.

### Control/admissibility growth

The source-channel state `Q`, correction state, ballot state, and any Route-B membership certificate may still distinguish many residue cylinders.

Therefore the remaining possible exponential growth can no longer be attributed to the interval payload itself.

A family node can be factored schematically as

\[
\text{node}
=
\text{control/admissibility state}
\times
\text{one of at most four interval payload cells}.
\]

This is useful for the next state-merging audit because payload multiplicity introduces only a constant factor.

---

## 8. Finite regression audit

`collatz/src/A0_s1_routeB_interval_four_state_cylinder_certificate.py` checks

- `L=-20,...,20`;
- `N=1,...,40`;
- residue depth `i=1,...,10`;
- every residue modulo `2^i`.

The implementation audit contains:

- 3,355,440 direct formula comparisons;
- 16,400 exact partition checks;
- 16,400 four-state checks;
- 65,600 compact joint-cell reconstruction checks.

These checks are guards.  The theorem follows from the two Euclidean-division identities above.

---

## 9. DSD audit

### Exact / closed

- child lower endpoints across a full depth-`i` residue family have only two values;
- child cardinalities have only two values;
- at most four exact interval payload states occur;
- each payload state residue cell is representable by at most two ordinary intervals;
- the payload state count is independent of the cylinder depth.

### Not implied

- the source-channel/correction/ballot control state need not have only four values;
- the four-state result does not prove Route-B admissibility;
- it does not prove a polynomial or finite global membership automaton.

### Updated bottleneck

\[
\boxed{
\text{All possible large state growth now lies in the control/admissibility quotient, not in the interval payload.}
}
\]

The next target is therefore to remove redundant coordinates from the product control state and quantify exact merging there.

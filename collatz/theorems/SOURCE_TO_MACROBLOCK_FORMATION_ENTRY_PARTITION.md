# Source-to-macroblock formation entry partition

Status: **EXACT / CLOSED local entry theorem; NOT a global formation-rank bridge**

## Purpose

The active S10 source family is kept as

\[
X=r+2^h m,
\qquad
T^h(X)=Y(m)=y+3^q m,
\qquad
m_{lo}\le m\le m_{hi},
\]

with

\[
q=Q(h)+S.
\]

This note answers one state-sufficiency question precisely:

> Does the minimized source state contain enough information to enter the exact maximal-macroblock formation grammar?

Yes, **as an exact partition of the live parameter interval**.  In general it does not assign one common formation label to the whole source cylinder.

This theorem concerns the maximal accelerated parity blocks

\[
1^H0^D.
\]

It does **not** identify these local block labels with the separate suffix-slack / formation-subtraction rank path.  The stitching obstruction for that global identification remains in force.

---

## 1. Normalize an arbitrary endpoint to the next odd state

Because

\[
A:=3^q
\]

is odd, every source parameter gives the exact endpoint

\[
Y(m)=y+Am.
\]

For a fixed positive endpoint define

\[
b:=v_2(Y),
\qquad
O:=Y/2^b.
\]

Then \(O\) is odd and the first continuation segment is exactly

\[
0^b.
\]

For this odd state define

\[
H:=v_2(O+1)\ge1,
\qquad
u:=\frac{O+1}{2^H}\quad(\nu\text{ odd}),
\]

and

\[
D:=v_2(3^H\nu-1)\ge1.
\]

The maximal accelerated parity block beginning at \(O\) is therefore

\[
\boxed{1^H0^D}.
\]

Thus the exact local entry descriptor is

\[
\boxed{E(m)=(b,H,D)}.
\]

---

## 2. Exact odd-state formation residue

For prescribed \(H,D\ge1\), exactness of the terminal even valuation is

\[
3^H\nu\equiv1+2^D\pmod{2^{D+1}}.
\]

Since \(3^H\) is a unit modulo \(2^{D+1}\), define the unique odd residue

\[
\boxed{
\nu_{H,D}
\equiv
3^{-H}(1+2^D)
\pmod{2^{D+1}}.
}
\]

Then the odd starts having maximal macroblock type \((H,D)\) are exactly

\[
\boxed{
O\equiv x_{H,D}:=2^H\nu_{H,D}-1
\pmod{2^{H+D+1}}.
}
\]

This is the established one-macroblock formation congruence, rewritten here as the input to the active source cylinder.

---

## 3. Exact source-parameter preimage

Prescribing the full local entry descriptor \((b,H,D)\) is equivalent to

\[
Y(m)
\equiv
2^b x_{H,D}
\pmod{2^{K}},
\]

where

\[
\boxed{K=b+H+D+1.}
\]

Indeed, \(x_{H,D}\) is odd, so this congruence gives \(v_2(Y)=b\) exactly, after which division by \(2^b\) gives the odd-state formation congruence.

Substituting

\[
Y(m)=y+Am,
\qquad A=3^q,
\]

and using that \(A\) is a unit modulo \(2^K\), there is exactly one parameter residue

\[
\boxed{
\rho_{b,H,D}
\equiv
\bigl(2^b x_{H,D}-y\bigr)A^{-1}
\pmod{2^K}.
}
\]

Therefore

\[
\boxed{
E(m)=(b,H,D)
\iff
m\equiv\rho_{b,H,D}
\pmod{2^{b+H+D+1}}.
}
\]

After intersecting with the live finite interval,

\[
I=[m_{lo},m_{hi}]\cap\mathbb Z,
\]

each local formation type is therefore either empty or one exact arithmetic subcylinder.

This gives the exact partition

\[
\boxed{
I
=
\bigsqcup_{b\ge0,\ H,D\ge1}
\left(
I\cap
\bigl(\rho_{b,H,D}+2^{b+H+D+1}\mathbb Z\bigr)
\right).
}
\]

The union is conceptually countable, but only finitely many parts are nonempty for a finite source interval.

---

## 4. Source-state sufficiency

The active persistent state is

\[
\boxed{(r,y,m_{lo},m_{hi},h,S).}
\]

From \((h,S)\),

\[
q=Q(h)+S
\]

and hence

\[
A=3^q
\]

are derived exactly.

The residue formula above then uses only

\[
(y,A,m_{lo},m_{hi})
\]

together with the transient proposed label \((b,H,D)\).

Therefore no historical parity word, no additional persistent H/L state, and no extra formation-rank coordinate is required to **compute the local maximal-macroblock entry partition**.

The state-sufficiency conclusion is

\[
\boxed{
(r,y,m_{lo},m_{hi},h,S)
\text{ is sufficient for exact local macroblock-entry partitioning.}
}
\]

---

## 5. Why there is generally no single cylinder-wide formation label

Suppose a live source cylinder contains two consecutive parameter values \(m,m+1\).

Because \(A=3^q\) is odd,

\[
Y(m+1)-Y(m)=A\equiv1\pmod2.
\]

Hence \(Y(m)\) and \(Y(m+1)\) have opposite parity.

Thus their initial even valuations cannot agree:

\[
\boxed{v_2(Y(m))\ne v_2(Y(m+1)).}
\]

Consequently their full descriptors \((b,H,D)\) differ.

Therefore every source cylinder with at least two consecutive live parameters necessarily intersects at least two local formation-entry classes.

So the correct interface is

\[
\boxed{
\text{source cylinder}
\longrightarrow
\text{exact residue partition by }(b,H,D),
}
\]

not

\[
\text{source cylinder}
\longrightarrow
\text{one persistent formation label}.
\]

---

## 6. Relation to valuation and multibit transducers

A local descriptor \((b,H,D)\) corresponds to the exact continuation grammar

\[
0^b1^H0^D
\]

with one additional dyadic look-ahead bit implicit in exact maximality of the terminal zero run.

Thus the residue modulus

\[
2^{b+H+D+1}
\]

is one bit finer than merely consuming the \(b+H+D\) displayed parity steps.

This is compatible with the existing source-preserving multibit transducer.  It is a compiled dyadic subcylinder description, not a new independent source coordinate.

In particular, using the local formation partition and then separately charging the same forced parity information as independent valuation/multibit pruning would double-count information.

---

## 7. What this theorem does not prove

This theorem does **not** prove any of the following:

1. that one \((b,H,D)\) labels an entire current source cylinder;
2. that distinct formation-entry subcylinders may be merged after their labels coincide;
3. that local maximal macroblocks form the suffix-slack formation-subtraction rank path;
4. that the bounded-rank formation path counts apply to arbitrary Route-B source cylinders;
5. that formation partitioning itself rejects any source integer;
6. that the number of formation types has a horizon-independent finite bound.

The already-certified direct stitching obstruction remains untouched.

---

## 8. DSD status

### EXACT / CLOSED

- endpoint normalization \(Y=2^bO\);
- maximal macroblock descriptor \((b,H,D)\);
- one-type odd-state residue \(x_{H,D}\);
- unique source-parameter preimage \(\rho_{b,H,D}\);
- exact interval partition by local formation type;
- sufficiency of the minimized source state for computing that partition;
- impossibility of one common local entry descriptor on any parameter interval containing two consecutive integers.

### NON-INDEPENDENT

The local formation-entry partition is a dyadic re-expression / compilation of exact future parity information.  It is not automatically an independent pruning factor beside the valuation or multibit transducers.

### OPEN

A source-sensitive contraction theorem would still need at least one of:

- a whole-subcylinder rejection inequality expressed naturally in \((b,H,D)\);
- a right-congruence proving safe merging after formation partitioning;
- a new explicit bridge from these local blocks to the separate bounded-rank formation automaton, including every boundary carry/rank condition.

Until then, formation entry is an exact transient grammar interface rather than a proof-level quotient.

# MATH-205 — Q-free ordinary carry chain and exact reset graph

Date: 2026-09-18

Status: `EXACT STRUCTURAL LEMMA / GLOBAL-Q ELIMINATION / NESTED DYADIC SELECTOR / r=10 OPEN`

## 1. Purpose

MATH-204 rewrites a dangerous singleton overshoot in normalized 2-adic coordinates as

\[
X-\eta_e(Q)=2^z\delta,
\qquad
X'=\beta_e(Q)+\delta.
\]

The remaining split was:

- zero carry: \(\delta=0\);
- nonzero quotient carry: \(\delta\ne0\).

This note returns to the ordinary MATH-091 carry coordinate and shows that an entire chain of dangerous singleton handoffs is independent of the accumulated global odd-count coordinate \(Q\).

The chain is an exact affine integer carry transducer with a unique dyadic residue selector at every continuation.

No paid layer, first universal Farey cell, or Collatz theorem is closed here.

## 2. Canonical factor notation

Let a canonical exact factor \(e\) be

\[
\boxed{
A_e+2^{z_e}t
\longmapsto
B_e+3^{q_e}t.
}
\]

Here \(z_e\) is the exact dyadic source length used by the singleton overshoot and \(q_e\) is its odd-count increment.

Suppose the factor is entered with ordinary transported carry \(d\).

Then MATH-091 gives the exact child intercept

\[
\boxed{
B^{\rm child}=B_e+3^{q_e}d.
}
\]

MATH-204's normalized carry is the same information in normalized coordinates.

## 3. Two consecutive dangerous factors

Let the current factor be \(e\), and let the next factor be \(f\).

The next exact source is

\[
A_f+2^{z_f}t.
\]

Therefore continuation from the child of \(e\) into \(f\) requires

\[
B_e+3^{q_e}d\equiv A_f\pmod{2^{z_f}}.
\]

Define the pair constant

\[
\boxed{
c_{e,f}:=B_e-A_f.
}
\]

Then the continuation condition is

\[
\boxed{
3^{q_e}d+c_{e,f}\equiv0\pmod{2^{z_f}}.
}
\]

Because \(3^{q_e}\) is odd, it is invertible modulo every power of two.

Hence a fixed pair \((e,f)\) and depth \(z_f\) accepts exactly one carry residue class:

\[
\boxed{
d
\equiv
-c_{e,f}3^{-q_e}
\pmod{2^{z_f}}.
}
\]

This removes the global \(Q\) coordinate completely from the address-continuation test.

## 4. Exact next-carry recurrence

When the congruence holds, define

\[
\boxed{
d'
=
\frac{3^{q_e}d+c_{e,f}}{2^{z_f}}.
}
\]

Then \(d'\in\mathbb Z\) exactly, and it is the ordinary carry transported into the next factor.

Thus the dangerous singleton chain is the exact integer transducer

\[
\boxed{
d
\xmapsto[e\to f]{z_f}
\frac{3^{q_e}d+B_e-A_f}{2^{z_f}},
}
\]

with the divisibility condition understood as part of transition legality.

The global normalized address \(X\) and accumulated odd count \(Q\) are not independent state coordinates for this continuation law.

## 5. Relation to MATH-204 normalized carry

Let the global odd count before factor \(e\) be \(Q\).

MATH-204 has

\[
\delta=3^{-Q}d.
\]

After factor \(e\), the new global odd count is

\[
Q'=Q+q_e.
\]

For the next factor \(f\),

\[
X'-\eta_f(Q')
=
3^{-(Q+q_e)}
\left(
B_e-A_f+3^{q_e}d
\right).
\]

Therefore

\[
X'-\eta_f(Q')
\equiv0\pmod{2^{z_f}}
\]

is exactly equivalent to

\[
3^{q_e}d+B_e-A_f
\equiv0\pmod{2^{z_f}}.
\]

The normalized and ordinary carry descriptions are thus exactly the same transition, but the ordinary form cancels \(Q\).

## 6. Zero-carry branch

Assume the current carry is

\[
d=0.
\]

Then the next dangerous factor \(f\) can exist only if

\[
\boxed{
B_e\equiv A_f\pmod{2^{z_f}}.
}
\]

For the present \(r=10\) danger threshold, MATH-202 gives \(z_f\ge13\). Hence

\[
\boxed{
d=0
\text{ and next }r=10\text{ danger}
\Longrightarrow
B_e\equiv A_f\pmod{8192}.
}
\]

If the next carry is also zero, then the recurrence gives the stronger exact condition

\[
\boxed{
d=0, d'=0
\Longleftrightarrow
B_e=A_f.
}
\]

Therefore a repeated all-zero-carry chain is not merely a modular resonance chain.

It is an exact canonical endpoint-to-source concatenation graph:

\[
\boxed{
e\to f
\quad\Longleftrightarrow\quad
B_e=A_f
}
\]

subject to the existing legal/Hensel/terminal conditions.

This is a finite graph whenever the relevant canonical factor catalogue is finite.

## 7. Exit from zero carry into nonzero carry

If \(d=0\) but \(d'\ne0\), then

\[
d'
=
\frac{B_e-A_f}{2^{z_f}}.
\]

Hence a zero-carry state can enter a nonzero dangerous \(r=10\) continuation only if

\[
\boxed{
\nu_2(B_e-A_f)\ge13,
\qquad
B_e\ne A_f.
}
\]

Thus the zero branch has an exact finite audit split:

1. exact-reset edges \(B_e=A_f\);
2. high-valuation exits \(\nu_2(B_e-A_f)\ge13\);
3. immediate safety when the valuation is smaller than 13.

## 8. Multi-step nested selector

Consider a fixed sequence of canonical factors

\[
e_0,e_1,\ldots,e_m
\]

and dangerous continuation depths

\[
z_1,\ldots,z_m.
\]

For \(i=0,\ldots,m-1\), put

\[
q_i:=q_{e_i},
\qquad
c_i:=B_{e_i}-A_{e_{i+1}}.
\]

The carries obey

\[
\boxed{
2^{z_{i+1}}d_{i+1}
=
3^{q_i}d_i+c_i.
}
\]

Define

\[
Z_0=0,
\qquad
Z_j=\sum_{i=1}^{j}z_i,
\]

\[
Q_0=0,
\qquad
Q_j=\sum_{i=0}^{j-1}q_i,
\]

and

\[
K_0=0,
\qquad
K_{j+1}
=
3^{q_j}K_j+2^{Z_j}c_j.
\]

Induction gives the exact identity

\[
\boxed{
2^{Z_m}d_m
=
3^{Q_m}d_0+K_m.
}
\]

Since \(3^{Q_m}\) is odd, continuation through all \(m\) transitions requires exactly one initial carry residue class:

\[
\boxed{
d_0
\equiv
-3^{-Q_m}K_m
\pmod{2^{Z_m}}.
}
\]

Thus every additional dangerous singleton handoff fixes additional low bits of the initial carry.

## 9. r=10 precision accumulation

If every continuation belongs to the current \(r=10\) danger kernel, then

\[
z_i\ge13.
\]

Therefore

\[
\boxed{
Z_m\ge13m.
}
\]

A fixed length-\(m\) dangerous factor sequence can therefore accept at most one residue class

\[
\boxed{
d_0\pmod{2^{13m}}.
}
\]

Examples:

\[
m=1:\quad 13\text{ forced bits},
\]

\[
m=2:\quad 26\text{ forced bits},
\]

\[
m=3:\quad 39\text{ forced bits},
\]

and so on.

This is exact nested dyadic selection, not a probabilistic sparsity statement.

## 10. Infinite-chain 2-adic consequence

For any fixed infinite legal factor/depth sequence, the compatible residue classes are nested because

\[
Z_m\to\infty.
\]

Therefore there is at most one 2-adic initial carry

\[
d_0\in\mathbb Z_2
\]

compatible with the entire infinite sequence.

Equivalently, an infinite dangerous symbolic path does not represent a positive-density or free family of carry states.

It specifies at most one 2-adic carry address.

This does not by itself exclude that address from being an ordinary integer.

## 11. DSD interpretation

The remaining singleton state decomposes into four independent channels:

1. canonical factor type;
2. exact legality/Hensel state;
3. terminal defect state;
4. ordinary quotient carry \(d\).

The address channel no longer needs global \(Q\).

For a fixed factor transition, only one residue class of \(d\) modulo the required power of two can remain dangerous.

Repeated danger recursively consumes carry bits and exposes the quotient.

The former large AP-source index is therefore not a natural proof-state coordinate.

## 12. Immediate next audit

The next exact calculation should use the current legal \(r=10\) canonical factor catalogue and construct two finite objects.

### A. Zero-carry reset graph

Retain only pairs satisfying

\[
B_e=A_f.
\]

Audit every directed cycle against:

- legal first-return structure;
- Hensel viability;
- terminal defect \(J\ge0\);
- already-closed ordinary/periodic descent structures.

### B. High-valuation exit graph

For pairs with

\[
B_e\ne A_f,
\]

retain only

\[
\nu_2(B_e-A_f)\ge13.
\]

Attach the exact quotient

\[
d'=(B_e-A_f)/2^{z_f}
\]

and continue with the Q-free carry recurrence.

This directly targets the two MATH-204 branches without returning to the 278,725-source AP scan.

## 13. Claim boundary

Established:

- exact elimination of global \(Q\) from consecutive singleton carry transitions;
- exact ordinary carry recurrence;
- one-residue-class selector for each canonical factor pair and depth;
- exact zero-to-zero condition \(B_e=A_f\);
- exact zero-to-nonzero high-valuation condition;
- exact multi-step nested congruence;
- at least \(13m\) forced carry bits along an \(m\)-step all-\(r=10\) dangerous chain;
- at most one 2-adic initial carry per fixed infinite symbolic danger path.

Not established:

- absence of cycles in the actual legal zero-carry reset graph;
- absence of high-valuation nonzero carry paths;
- contraction or boundedness of every nonzero carry orbit;
- closure of \(r=10\);
- first universal Farey-cell emptiness;
- the Collatz conjecture.

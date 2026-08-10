# Delta-Q=1 carry-wrap dominance correction

Date: 2026-08-11

Status: **exact algebraic correction + exact finite carry certificate + revised theorem target**.

This note supersedes the earlier proposed target

\[
G=r_L-3r_H>0
\]

for every coefficient-surviving true first merge with \(Q_H=Q_L+1\). That stronger statement is false. The Pareto start-order target remains viable and is strictly weaker.

## 1. Setup

Let a true first merge at depth \(k\) have

\[
Q_H=q+1,\qquad Q_L=q,
\]

with canonical starts \(r_H,r_L\), common endpoint \(y\), and correction numerators \(R_H,R_L\):

\[
2^k y=3^{q+1}r_H+R_H=3^q r_L+R_L.
\]

Define

\[
G:=r_L-3r_H=\frac{R_H-R_L}{3^q}.
\]

The quantity that is actually required by same-endpoint Pareto dominance is not \(G>0\), but

\[
\boxed{J:=r_L-r_H>0.}
\]

Since

\[
r_L=3r_H+G,
\]

we have the exact identity

\[
\boxed{J=2r_H+G.}
\]

Thus negative correction order \(G<0\) does not by itself imply a start-order failure.

---

## 2. Explicit counterexample to the stronger G>0 target

An exact coefficient-surviving true first merge occurs at depth

\[
\boxed{k=37}
\]

with

\[
r_H=11,828,881,407,
\]

\[
r_L=35,486,644,219.
\]

Direct accelerated iteration verifies survival at every prefix through depth 37. Immediately before the final step,

\[
T^{36}(r_H)=145,846,228,108,
\]

\[
T^{36}(r_L)=48,615,409,369.
\]

The final parity pair is Type B,

\[
(p_H,p_L)=(0,1),
\]

and

\[
T^{37}(r_H)=T^{37}(r_L)=72,923,114,054.
\]

The odd-counts are

\[
Q_H=25,\qquad Q_L=24,
\]

so \(\Delta Q=1\), but

\[
\boxed{G=r_L-3r_H=-2.}
\]

Therefore the earlier proposed First-Merge Correction Order \(G>0\) is false.

Nevertheless,

\[
J=r_L-r_H=23,657,762,812>0,
\]

so the higher-\(Q\) state still dominates in the start-order sense required by the endpoint Pareto quotient.

---

## 3. Joint 3-adic carry and 2-adic wrap

Write the odd positions as

\[
0=a_0<a_1<\cdots<a_q
\]

for the H channel and

\[
0=b_0<b_1<\cdots<b_{q-1}
\]

for the L channel.

Coefficient survival gives the exact position bounds

\[
a_i\le\kappa(i),\qquad b_i\le\kappa(i),
\]

where

\[
\kappa(i)=\lfloor i\log_2 3\rfloor.
\]

The correction difference is represented by the integer carry chain

\[
c_q=0,
\]

\[
\boxed{
3c_i=2^{a_{i+1}}-2^{b_i}+c_{i+1},
\qquad i=q-1,\ldots,0,
}
\]

with

\[
\boxed{G=1+c_0.}
\]

Carry integrality alone does not force a common endpoint. Canonical residues satisfy the automatic congruence

\[
r_L-3r_H\equiv G\pmod{2^k}.
\]

Therefore define the binary wrap channel

\[
\boxed{
m:=\frac{r_L-3r_H-G}{2^k}\in\mathbb Z.
}
\]

The endpoint difference is exactly

\[
\boxed{
y_L-y_H=3^q m.}
\]

Hence

\[
\boxed{m=0}
\]

is precisely the common-endpoint condition.

For a true first merge the final parities must differ, so the last odd positions determine the contact depth:

### Type A

\[
a_q=k-1>b_{q-1}.
\]

### Type B

\[
b_{q-1}=k-1>a_q.
\]

Equivalently,

\[
\boxed{k=\max(a_q,b_{q-1})+1.}
\]

This gives an exact joint carry/wrap characterization of the negative-G branch.

---

## 4. Exact carry DP

The implementation

`collatz/src/deltaq1_carry_wrap_dominance.cpp`

builds the complete finite carry state

\[
(a_{i+1},b_i,c_i)
\]

under the coefficient-survival bounds and the terminal condition \(c_q=0\).

The value \(\kappa(i)\) is generated with exact integer comparison

\[
2^{\kappa(i)}<3^i<2^{\kappa(i)+1},
\]

so no floating-point logarithm is used in the certificate.

Only negative terminal roots are subsequently expanded, because

\[
J=2r_H+G
\]

shows that a start-order failure is impossible when \(G\ge0\).

For each negative path, the code reconstructs \(R_H,R_L\), fixes the true-contact depth from the last odd positions, reconstructs the canonical residues modulo \(2^k\), checks \(m=0\), and finally checks

\[
J=r_L-r_H.
\]

---

## 5. Negative carry spectrum

The exact DP gives:

- for \(2\le q\le21\): no negative root \(c_0\);
- for every tested \(22\le q\le33\): the only negative root is
  \[
  \boxed{c_0=-3},
  \]
  hence
  \[
  \boxed{G=-2}.
  \]

No \(c_0=-7,-11,\ldots\) root appears through \(q=33\).

The root-only state calculation reaches

\[
q=33,\qquad \kappa(33)=52,
\]

with 1,961,592 peak carry states and still only the root \(c_0=-3\).

This is an exact finite computational statement, not an asymptotic theorem.

---

## 6. Consequence for start-order through q<=33

For coefficient-surviving prefixes of depth at least two,

\[
r_H\equiv3\pmod4,
\]

so

\[
r_H\ge3.
\]

If \(G\ge0\), then immediately

\[
J=2r_H+G>0.
\]

For the only negative root found through \(q=33\),

\[
G=-2,
\]

so

\[
\boxed{J=2r_H-2\ge4>0.}
\]

Therefore the carry certificate proves the following finite statement:

> For every Delta-Q=1 coefficient-surviving true first merge whose lower odd-count satisfies \(q\le33\), the higher-Q canonical state has the smaller start,
> \[
> \boxed{r_H<r_L.}
> \]

This statement does not require enumeration of every endpoint class. Any actual true merge is a subset of the carry-admissible state family tested by the certificate.

A merge with \(q\le33\) can occur only at depth

\[
k\le\kappa(33)=52,
\]

but this does not assert coverage of all possible merges through depth 52 with larger \(q\).

---

## 7. Full negative-path checks

The companion result file is

`collatz/results/deltaq1_carry_wrap_q22_q33.csv`.

Full negative-path expansion was completed through \(q=31\). Representative results are:

- \(q=24\): 22 true negative-G merges, 0 dominance failures;
- \(q=28\): 4,653 true negative-G merges, 0 dominance failures;
- \(q=30\): 34,934 true negative-G merges, 0 dominance failures;
- \(q=31\): 152,208 true negative-G merges, 0 dominance failures.

All true negative-G merges in this range have \(G=-2\).

The purpose of the full expansion is diagnostic; once the negative root spectrum is known to contain only \(-3\), the start-order conclusion follows directly from \(J=2r_H-2>0\).

---

## 8. Revised theorem target

The false strong target

\[
G>0
\]

is replaced by the exact target actually needed by the endpoint quotient:

### Delta-Q=1 First-Merge Start Dominance

For every coefficient-surviving true first merge with

\[
Q_H=Q_L+1,
\]

prove

\[
\boxed{r_H<r_L.}
\]

Equivalently,

\[
\boxed{J=2r_H+1+c_0>0.}
\]

The next structural question is therefore not whether negative carries exist. They do. It is:

> How negative can the admissible root carry \(c_0\) become as \(q\to\infty\), and is that negativity always too small in magnitude to overcome \(2r_H\)?

Two possible closure routes are now separated cleanly:

1. prove a universal or asymptotic lower bound on \(c_0\), ideally \(c_0\ge-3\) or a sufficiently slow negative growth bound;
2. combine any lower bound on \(c_0\) with a lower bound on the coefficient-surviving canonical start \(r_H\).

This is the revised DSD-style bad-set problem:

\[
\boxed{
\mathfrak B
=
\{\text{true merge}:\Delta Q=1,\ J\le0\}
}
\]

and the objective is to prove that \(\mathfrak B\) is unreachable.

---

## 9. DSD interpretation

The useful discrete DSD state now has three distinct comparison channels:

1. the 3-adic correction carry \(c_0\), controlling \(G=1+c_0\);
2. the 2-adic wrap index \(m\), controlling endpoint equality;
3. the start-order channel
   \[
   J=r_L-r_H.
   \]

The earlier use of \(G\) alone conflated correction order with Pareto start order. The explicit depth-37 counterexample separates those roles.

The resulting hierarchy is

\[
\text{coefficient-survival admissibility}
\to
\text{3-adic carry}
\to
\text{2-adic wrap/contact}
\to
\text{start-order }J.
\]

No physical DSD propagation term is used. This remains a purely discrete arithmetic application of the state/channel/transition framework.

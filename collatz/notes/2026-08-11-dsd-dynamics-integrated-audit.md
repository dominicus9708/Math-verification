# Integrated DSD-style dynamics audit for Collatz

Date: 2026-08-11

Status: **exact finite computation + structural reduction + theorem targets**. This note does not claim a proof of the Collatz conjecture, coefficient stopping-time equality, or global first-merge order.

## 1. Purpose

The purpose of this audit is to test the Collatz program in the same layered order used in the reorganized DSD framework:

1. admissible state formation;
2. static channel state;
3. exact channel-indexed dynamics;
4. block composition;
5. endpoint quotient;
6. two-channel first-merge dynamics;
7. bad-set reachability.

The DSD physical propagation terms are not imported. In particular, no wave equation, Laplacian, reorganization velocity, or information-propagation speed is assumed. Only the state/channel/transition/aggregation architecture is used.

The implementation is:

`collatz/src/dsd_dynamics_reachability_audit.cpp`

The reference output is:

`collatz/results/dsd_dynamics_depth32.csv`

---

## 2. Single-channel state and closure

For the accelerated Collatz map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
\]

write the depth-\(k\) canonical state as

\[
\Xi_k=(r_k,y_k,R_k,u_k,v_k,Q_k,e_k),
\]

where

\[
u_k=3^{Q_k},\qquad v_k=2^k,
\]

and \(Q_k\) is the number of odd steps in the parity prefix. The correction numerator is fixed by

\[
\boxed{v_k y_k=u_k r_k+R_k.}
\]

For coefficient survival, the admissible state set is

\[
\mathcal A_k=\{\Xi_k:u_k\ge v_k\}.
\]

Equivalently, with

\[
a_k=\lceil k\log_3 2\rceil,
\qquad e_k=Q_k-a_k,
\]

admissibility is \(e_k\ge0\).

---

## 3. Exact channel dynamics

Let the requested next parity be

\[
p_k\in\{0,1\}.
\]

The canonical lift bit is

\[
\boxed{c_k=p_k\oplus(y_k\bmod2).}
\]

Then the exact transition is

\[
r_{k+1}=r_k+c_kv_k,
\]

\[
\widetilde y_k=y_k+c_ku_k,
\]

\[
y_{k+1}=\frac{3^{p_k}\widetilde y_k+p_k}{2},
\]

\[
Q_{k+1}=Q_k+p_k,
\]

\[
u_{k+1}=3^{p_k}u_k,
\qquad
v_{k+1}=2v_k,
\]

and

\[
\boxed{R_{k+1}=3^{p_k}R_k+p_kv_k.}
\]

The audit verifies the closure

\[
v_{k+1}y_{k+1}=u_{k+1}r_{k+1}+R_{k+1}
\]

before the coefficient-survival filter is applied.

Through depth 32:

- exact branch transitions checked: **100,701,368**;
- closure failures: **0**;
- transition-identity failures: **0**.

Thus the DSD-style single-channel state is computationally closed for the entire enumerated coefficient-surviving tree through depth 32.

---

## 4. Block dynamics

For a depth-\(k\) parity cylinder, every lift

\[
n=r_k+m2^k
\]

obeys

\[
\boxed{T^k(n)=y_k+3^{Q_k}m.}
\]

This is the block form of the channel dynamics. The audit directly iterates deterministic sample lifts and compares them with the block formula.

Through depth 32:

- deterministic block-lift samples checked: **20,040**;
- block-lift failures: **0**.

This is the same structural identity used by the prefix-channel interval scanner, now embedded in the integrated dynamics audit.

---

## 5. Endpoint quotient

At a fixed depth, define endpoint equivalence by

\[
\Xi_i\sim_y\Xi_j
\quad\Longleftrightarrow\quad
y_i=y_j.
\]

This quotient is descriptive rather than causal: distinct histories that reach the same endpoint have identical future Collatz evolution from that endpoint.

At depth 32:

- coefficient-surviving states: **41,347,483**;
- endpoint classes: **38,890,504**;
- immediate quotient reduction: **2,456,979 states**, about **5.94%**;
- collision classes: **2,437,971**;
- maximum class size: **4**.

Reference checks reproduce earlier counts:

- depth 20: 27,328 survivors and 25,644 endpoint classes;
- depth 24: 286,581 survivors and 269,145 endpoint classes;
- depth 28: 3,524,586 survivors and 3,312,992 endpoint classes.

---

## 6. True first merge

For a canonical child, the actual value immediately before its final branch is not the unlifted parent endpoint. It is

\[
\boxed{\widetilde y=y+c3^Q.}
\]

Therefore two states at depth \(k\) form a true first merge when

\[
y_H=y_L
\]

but

\[
\widetilde y_{H,k-1}\ne\widetilde y_{L,k-1}.
\]

This corrected definition supersedes earlier diagnostics that compared only unlifted parent endpoints.

Through depth 32 the exact cumulative true-first-merge count is

\[
\boxed{6996}.
\]

Their odd-count differences are

\[
\Delta Q=1:4549,
\]

\[
\Delta Q=2:2305,
\]

\[
\Delta Q=3:141,
\]

\[
\Delta Q=4:1.
\]

No equal-\(Q\) true merge occurred in the tested range.

Thus \(\Delta Q=1\) is the largest single first-merge sector, about 65.0% of the observed true merges, but the earlier claim that it represented about 99% was based on the superseded first-merge definition and must not be used.

---

## 7. Delta-Q=1 two-channel sector

At a common endpoint, write

\[
Q_H=Q+1,
\qquad Q_L=Q.
\]

Define the merge contrast

\[
\boxed{G=r_L-3r_H.}
\]

The common endpoint identity gives

\[
\boxed{3^QG=R_H-R_L.}
\]

Hence the correction-order target

\[
R_H>R_L
\]

is exactly equivalent to

\[
G>0.
\]

The bad merge set is therefore

\[
\boxed{\mathfrak M^-_1
=\{\Delta y=0,\ \Delta Q=1,\ G<0\}.}
\]

The finite reachability question is whether the admissible dynamics enters this set.

Through depth 32:

\[
\boxed{|\mathfrak M^-_1\cap\mathcal R_{\le32}|=0.}
\]

There are 4,549 reachable true first merges with \(\Delta Q=1\), and none has \(G<0\).

The exact observed positive distribution is

\[
G=2:4421,
\]

\[
G=6:37,
\]

\[
G=10:91.
\]

No other positive \(G\) occurred through depth 32. This is a finite observation, not a proposed global upper bound.

Since coefficient-surviving canonical starts satisfy

\[
r_H\equiv r_L\equiv3\pmod4,
\]

one already has

\[
G\equiv2\pmod4.
\]

Thus the computed values are precisely the first three positive values allowed by this congruence.

---

## 8. Last-step interaction types

A true merge requires different final parity branches. For \(\Delta Q=1\), only two last-step types are possible.

Type A:

\[
\Delta Q:0\xrightarrow{(1,0)}1.
\]

Type B:

\[
\Delta Q:2\xrightarrow{(0,1)}1.
\]

Through depth 32:

- Type A: **1,079**;
- Type B: **3,470**.

Their \(G\)-distributions are

Type A:

\[
G=2:979,\qquad G=6:9,\qquad G=10:91.
\]

Type B:

\[
G=2:3442,\qquad G=6:28.
\]

Thus every observed \(G=10\) merge occurs in Type A, while Type B remains confined to \(G\in\{2,6\}\) through depth 32.

This separation is a useful theorem-discovery target but is not yet proved.

---

## 9. What the DSD formulation adds

The affine parity formula itself is not a novelty claim. The potentially distinctive layer is the organization

\[
\text{admissible state}
\to
\text{channel-indexed exact dynamics}
\to
\text{block channel}
\to
\text{endpoint quotient}
\to
\text{two-channel merge surface}
\to
\text{bad-set reachability}.
\]

Existing affine/parity/residue/stopping-time results should be cited where they overlap. The present project should emphasize only the structural reduction and any theorem that is actually proved within this framework.

In particular, the current proof target is not that the finite data look favorable. It is to prove

\[
\boxed{\mathfrak M^-_1\text{ is unreachable from the admissible initial state set}.}
\]

---

## 10. Next computational and proof targets

### A. Backward bad-set transfer

Construct an exact reverse transfer for the two legal final interaction types and propagate symbolic or interval constraints backward from

\[
\Delta y=0,\quad \Delta Q=1,\quad G<0.
\]

The objective is to show that the reverse reachable set loses integrality, parity admissibility, or coefficient survival before reaching depth zero.

### B. Type-separated theorem search

Treat Type A and Type B independently. The finite data suggest that Type B may admit a stronger restriction than the general \(G>0\) target.

### C. Quotient before enumeration

The current audit performs the endpoint quotient after flat state generation. A stronger exact solver should propagate endpoint/Pareto classes directly so that the roughly 6% same-depth redundancy is never materialized.

### D. Connect to the existing prefix-channel scanner

Use a moderate block depth \(B\) as a static aggregation layer, then propagate block states through the DSD dynamics rather than individual parity bits. This is the route most likely to improve both proof search and large-depth exact computation.

---

## 11. Reference run

Reference command:

```text
g++ -O3 -std=c++17 collatz/src/dsd_dynamics_reachability_audit.cpp -o dsd_audit
./dsd_audit 32 1024 > collatz/results/dsd_dynamics_depth32.csv
```

Representative local run:

- wall time: about 33 s;
- maximum resident memory: about 2.03 GB.

Runtime and memory are machine-dependent. The exact integer counts and zero-failure checks are the reproducible result.

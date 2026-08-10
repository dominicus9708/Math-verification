# Delta-q=1 true first-merge two-channel system

Date: 2026-08-10

Status: **exact algebraic reduction + corrected finite diagnostics + theorem targets**. This note does not prove Collatz convergence or coefficient/classical stopping-time equality.

## 1. Accelerated affine channel

Write the accelerated Collatz branch as

\[
F_p(x)=\frac{3^p x+p}{2},\qquad p\in\{0,1\}.
\]

For a parity prefix of length j, let q_j be its number of odd steps and let R_j be the additive correction numerator. Then

\[
T^j(r)=\frac{3^{q_j}r+R_j}{2^j},
\]

with exact recursion

\[
q_{j+1}=q_j+p_j,
\qquad
R_{j+1}=3^{p_j}R_j+p_j2^j.
\]

After normalization C_j=R_j/2^j, the correction channel obeys the same affine branch map:

\[
\boxed{C_{j+1}=F_{p_j}(C_j).}
\]

Thus endpoint evolution and normalized-correction evolution have the same two-branch affine form; they differ only in initial data.

## 2. Exact relative two-channel dynamics

For a high-q channel H and low-q channel L, define

\[
\Delta x_j=x_{H,j}-x_{L,j},
\qquad
d_j=q_{H,j}-q_{L,j}.
\]

Given a parity pair (p_H,p_L), the exact relative update is

\[
x_{L,j+1}=\frac{3^{p_L}x_{L,j}+p_L}{2},
\]

\[
\boxed{
\Delta x_{j+1}
=
\frac{
3^{p_H}\Delta x_j
+(3^{p_H}-3^{p_L})x_{L,j}
+(p_H-p_L)
}{2},
}
\]

\[
\boxed{d_{j+1}=d_j+p_H-p_L.}
\]

Equivalently,

\[
\begin{pmatrix}
x_{L,j+1}\\
\Delta x_{j+1}\\
d_{j+1}\\1
\end{pmatrix}
=
\begin{pmatrix}
3^{p_L}/2&0&0&p_L/2\\
(3^{p_H}-3^{p_L})/2&3^{p_H}/2&0&(p_H-p_L)/2\\
0&0&1&p_H-p_L\\
0&0&0&1
\end{pmatrix}
\begin{pmatrix}
x_{L,j}\\
\Delta x_j\\d_j\\1
\end{pmatrix}.
\]

The same relative matrix applies to the normalized correction variables C_H,C_L.

## 3. Correct definition of a true first merge

A depth-k canonical child may be obtained from its depth-(k-1) parent by adding a lift c2^{k-1}. If the parent has state (r,y,q), the actual time-(k-1) value of the lifted child is

\[
\boxed{\widetilde y=y+c3^q.}
\]

Therefore two depth-k states with a common endpoint form a true first merge only when their actual lifted predecessors are different. Comparing the unlifted parent endpoints is insufficient.

The repository diagnostic `endpoint_first_merge_diagnostics.cpp` has been corrected accordingly. Earlier 2026-08-10 first-merge counts based on unlifted parent_y are superseded.

## 4. Last-step classification at a true merge

Let two distinct predecessors u_H,u_L satisfy

\[
F_{p_H}(u_H)=F_{p_L}(u_L)=y.
\]

Because each branch F_0 and F_1 is injective on its own parity domain, a true merge requires

\[
\boxed{p_H\ne p_L.}
\]

The two possible predecessors of a merge endpoint are

\[
u_E=2y,
\qquad
u_O=\frac{2y-1}{3}.
\]

The odd predecessor exists as an odd integer iff

\[
\boxed{y\equiv2\pmod3.}
\]

Whenever it exists,

\[
\boxed{u_E=3u_O+1.}
\]

Now impose the final condition

\[
\Delta q_k=q_{H,k}-q_{L,k}=1.
\]

There are exactly two last-step types:

### Type A: H odd, L even

\[
(p_H,p_L)=(1,0),
\qquad
\Delta q_{k-1}=0,
\]

and

\[
u_L=3u_H+1.
\]

### Type B: H even, L odd

\[
(p_H,p_L)=(0,1),
\qquad
\Delta q_{k-1}=2,
\]

and

\[
u_H=3u_L+1.
\]

Thus a Delta-q=1 true merge can enter the merge surface only through

\[
\boxed{0\xrightarrow{(1,0)}1}
\qquad\text{or}\qquad
\boxed{2\xrightarrow{(0,1)}1}.
\]

This sharply reduces the final-step interaction types.

## 5. Exact merge-gap identity

At a depth-k common endpoint y, write

\[
q_H=q+1,\qquad q_L=q.
\]

Let r_H,r_L be the two canonical starts and R_H,R_L their correction numerators. Then

\[
2^k y=3^{q+1}r_H+R_H
      =3^q r_L+R_L.
\]

Therefore

\[
\boxed{
G:=r_L-3r_H
=\frac{R_H-R_L}{3^q}.
}
\]

This is the natural scalar order parameter for the Delta-q=1 merge.

Hence the proposed correction-order statement

\[
R_H>R_L
\]

is exactly equivalent to

\[
\boxed{G>0.}
\]

If G>0, then in fact

\[
r_L>3r_H>r_H,
\]

which is stronger than the ordinary start-order inequality r_H<r_L.

## 6. Congruence restriction from coefficient survival

Any coefficient-surviving state through depth at least 2 must begin with two odd parity steps, because

\[
3^1<2^2.
\]

Thus its canonical start satisfies

\[
r\equiv3\pmod4.
\]

For both channels,

\[
r_H\equiv r_L\equiv3\pmod4,
\]

so the merge gap satisfies

\[
\boxed{G\equiv2\pmod4.}
\]

Therefore G=0 is impossible. The positive-order target is equivalently the exclusion of

\[
G\in\{-2,-6,-10,\ldots\}.
\]

The smallest admissible positive gap is G=2.

## 7. Odd-position / 3-adic carry representation

Let the H parity word contain q+1 odd positions

\[
0=a_0<a_1<\cdots<a_q,
\]

and the L word contain q odd positions

\[
0=b_0<b_1<\cdots<b_{q-1}.
\]

Their corrections are

\[
R_H=\sum_{i=0}^{q}3^{q-i}2^{a_i},
\qquad
R_L=\sum_{i=0}^{q-1}3^{q-1-i}2^{b_i}.
\]

Therefore the exact normalized gap is

\[
\boxed{
G
=1+
\sum_{i=0}^{q-1}
\frac{2^{a_{i+1}}-2^{b_i}}{3^{i+1}}.
}
\]

At a genuine common-endpoint collision this quantity is an integer. The divisibility can be represented as a backward 3-adic carry channel. Set

\[
c_q=0,
\]

and for i=q-1,\ldots,0 define

\[
\boxed{
c_i=
\frac{2^{a_{i+1}}-2^{b_i}+c_{i+1}}{3}.
}
\]

For a collision every c_i is an integer, and

\[
\boxed{G=1+c_0.}
\]

Thus the global correction-order problem can be restated as a sign problem for the terminal pair-carry:

\[
\boxed{c_0\ge0.}
\]

The internal carries need not remain nonnegative; only the final c_0 sign is the target. This prevents an unjustified local-monotonicity proof.

## 8. Corrected exact finite diagnostics

Using the true lifted-predecessor definition, exact enumeration through depth 28 gives:

- true first-merge pairs: 805;
- equal-q true first merges: 0;
- Delta q=1 pairs: 507;
- Delta q=2 pairs: 276;
- Delta q=3 pairs: 22;
- same-last-parity true merges: 0;
- correction-order failures R_H<=R_L: 0;
- start-order failures r_H>=r_L: 0.

For the 507 Delta-q=1 true first merges, the gap distribution is

\[
\boxed{G=2\text{ in }504\text{ cases},\qquad G=6\text{ in }3\text{ cases}.}
\]

The last-step orientations are

\[
(p_H,p_L)=(1,0):40\text{ cases},
\]

\[
(p_H,p_L)=(0,1):467\text{ cases}.
\]

These are finite computational observations, not asymptotic theorems.

## 9. Refined theorem target

The broad first-merge correction-order target can now be split.

### Primary Delta-q=1 target

For every coefficient-surviving true first merge with q_H=q_L+1, prove

\[
\boxed{G=r_L-3r_H>0.}
\]

Equivalently, prove any one of

\[
R_H>R_L,
\qquad
c_0\ge0,
\qquad
r_L>3r_H.
\]

The formulation using c_0 is attractive because the collision divisibility has already been absorbed into an exact integer carry recursion.

### Secondary structural target

Determine whether the observed small-gap phenomenon

\[
G\in\{2,6\}
\]

persists beyond depth 28 or whether larger positive values eventually occur. No theorem is asserted for this stronger pattern.

## 10. Relation to the channelized DSD-style formalism

The useful import from the reorganized dynamics framework is formal rather than physical:

- two indexed channels H,L;
- a relative state (x_L,Delta x,d);
- an affine pair-transition matrix selected by (p_H,p_L);
- a coalescence surface Delta x=0;
- a scalar order channel G or c_0 at first contact.

No propagation-speed, wave, Laplacian, or physical transport assumption is used. The resulting system is a purely discrete arithmetic two-channel dynamics derived exactly from the Collatz map.

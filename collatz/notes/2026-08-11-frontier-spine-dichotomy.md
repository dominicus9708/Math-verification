# Frontier-preserving spine and width-collapse dichotomy

Date: 2026-08-11

Status: **exact structural lemmas** for the centered survivor-channel system. These lemmas classify how a bounded-frontier hypothetical survivor can persist. They do not prove the Collatz conjecture.

## 1. Centered state

Use the exact centered survivor channel

\[
s=(k,\rho,h,u,N),
\]

representing

\[
\llbracket s\rrbracket
=\{\rho+2^k t:0\le t\le N\},
\]

with

\[
T^k(\rho+2^k t)=\rho+h+ut.
\]

For one binary child, write

\[
t=c+2t',\qquad c\in\{0,1\}.
\]

After imposing the new no-descent inequality, suppose the surviving child interval in \(t'\) begins at \(J_c\ge0\). The centered child frontier is

\[
\boxed{
\rho'=\rho+c2^k+2^{k+1}J_c.
}
\]

---

## 2. Frontier monotonicity theorem

Every surviving child satisfies

\[
\boxed{\rho'\ge\rho.}
\]

Moreover,

\[
\boxed{
\rho'=\rho
\iff
c=0\text{ and }J_0=0.
}
\]

Therefore a parent channel has at most one frontier-preserving child.

This child is exactly the child containing the current least represented integer \(\rho\). Every other surviving child strictly increases the channel frontier.

---

## 3. Unique plateau spine

Consider an infinite nested survivor-channel path

\[
s_k\to s_{k+1}\to s_{k+2}\to\cdots.
\]

If its frontier is bounded, then because the frontier is integer-valued and nondecreasing, it eventually stabilizes at some finite value \(n\).

From the frontier monotonicity theorem, every transition after stabilization must use

\[
\boxed{c=0,\qquad J=0.}
\]

Hence after stabilization the path is unique: it is the binary child spine containing the fixed integer \(n\).

On that spine,

\[
\boxed{h_j=T^j(n)-n.}
\]

Thus a bounded-frontier infinite survivor path is necessarily the unique persistent spine of one fixed starting integer. The set-level representation has reduced all branching ambiguity before this terminal obstruction.

---

## 4. Finite-width collapse lemma

Suppose a frontier-preserving transition has finite parent width \(N<\infty\). Since \(c=0\), the inherited width before the new filter is

\[
\left\lfloor\frac N2\right\rfloor.
\]

The new no-descent filter can only remove additional points. Therefore

\[
\boxed{
N'\le\left\lfloor\frac N2\right\rfloor.
}
\]

Consequently, if the frontier remains fixed and the width is finite at some time, then after at most

\[
\boxed{\left\lceil\log_2(N+1)\right\rceil}
\]

further frontier-preserving refinements, either the channel is removed, the frontier increases, or the channel becomes the singleton

\[
\boxed{\{n\}.}
\]

Once \(N=0\), the width can never increase again under refinement.

---

## 5. Unbounded-width persistence criterion

If \(N=+\infty\), then the inherited frontier-preserving child also has unbounded width before the new no-descent filter.

At depth \(k+1\), the new difference along the child lift coordinate is

\[
A+B t',
\]

with

\[
B=u'-2^{k+1}.
\]

If \(B<0\), the inequality \(A+Bt'\ge0\) imposes a finite upper bound whenever the child is nonempty. Therefore an unbounded child can survive only when

\[
\boxed{u'>2^{k+1}.}
\]

Equality is impossible for positive powers of 2 and 3.

Hence an infinite frontier-preserving path that remains unbounded at every sufficiently large depth must satisfy coefficient survival at every such depth.

---

## 6. Counterexample-path dichotomy

Assume a bounded-frontier infinite unresolved path exists. After the frontier stabilizes at some finite integer \(n\), exactly one of two structural modes is possible.

### Tail mode

The channel remains unbounded forever. Then the fixed-n spine is accompanied by an unbounded lift tail and the multiplier condition

\[
3^{Q_j}>2^j
\]

must persist indefinitely.

This is the finite-integer infinite coefficient-survivor obstruction.

### Spine mode

At some depth the channel becomes bounded. The finite-width collapse lemma then forces the frontier-preserving channel to become the singleton \(\{n\}\) in finite additional time. Any further unresolved persistence is a singleton spine.

Thus every hypothetical counterexample path is reduced to

\[
\boxed{
\text{infinite coefficient-surviving tail}
\quad\text{or}\quad
\text{infinite unresolved singleton spine}.
}
\]

The first mode should be attacked by lift/residue/coefficient-survival constraints. The second mode should be attacked by a universal attribute/Lyapunov argument on the fixed-frontier dynamics, not by enumerating individual starting integers.

---

## 7. Proof-design consequence

The mixed mass/frontier proof target can now be localized:

1. all non-spine children make strict frontier progress;
2. finite-width plateau channels have a well-founded width rank and collapse to singleton;
3. only unbounded coefficient-surviving tails and singleton spines can support indefinite bounded-frontier persistence.

Therefore future attribute refinement should focus only on these two terminal obstruction classes. Broad depth enumeration of all channels is no longer a main proof task.

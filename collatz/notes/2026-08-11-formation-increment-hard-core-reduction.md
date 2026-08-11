# Formation-increment bit and hard-core mass reduction

Date: 2026-08-11

Status: **exact global reduction**. This note separates survivor-tree branches that automatically escape to large formation floor from the unique floor-preserving hard core relevant to finite positive-integer counterexamples.

## 1. Binary formation increment

Let `w` be a survivor prefix of length `k` with formation floor

\[
\rho_k=\rho_k(w).
\]

Its two length-`k+1` residue lifts differ by `2^k`. Along a chosen child path define

\[
\boxed{
\beta_k
:=
\frac{\rho_{k+1}-\rho_k}{2^k}.
}
\]

Then

\[
\boxed{\beta_k\in\{0,1\}}
\]

and

\[
\boxed{
\rho_{k+1}=\rho_k+\beta_k2^k.
}
\]

Iterating from any depth `K`,

\[
\boxed{
\rho_k
=
\rho_K+
\sum_{j=K}^{k-1}\beta_j2^j.
}
\]

---

## 2. Finite-natural criterion in binary form

Because all summands are nonnegative,

\[
\boxed{
\rho_k\text{ is bounded}
\iff
\beta_k=0\text{ for all sufficiently large }k.
}
\]

Equivalently,

\[
\boxed{
\beta_k=1\text{ infinitely often}
\Longrightarrow
\rho_k\to\infty.
}
\]

Thus an infinite parity path corresponds to one fixed finite positive integer exactly when its formation-increment sequence is eventually zero.

This is the ordinary-binary version of the 2-adic/natural-number distinction in the survivor tree.

---

## 3. Unique floor-preserving child

At a depth-`k` exact channel, let `rho_k` be its least represented start and let

\[
y_k:=T^k(\rho_k).
\]

The two possible residue lifts are

\[
\rho_k
\quad\text{and}\quad
\rho_k+2^k.
\]

Their depth-`k` endpoints differ by the odd number `3^{q_k}`, so they have opposite next parities.

If `p_k` denotes the next parity bit of the chosen child, then

\[
\boxed{
p_k\equiv y_k+\beta_k\pmod2.}
\]

Hence

\[
\boxed{
\beta_k=0
\iff
p_k\equiv T^k(\rho_k)\pmod2.
}
\]

There is therefore **at most one child** of a survivor node that preserves its formation floor. The other child, when nonempty, raises the floor by exactly `2^k`.

This gives the survivor tree a spine-and-side-branch structure:

- one possible `beta=0` child continues the current minimum start;
- the `beta=1` child jumps to a new formation scale.

---

## 4. Full-support geometric mass

For any fixed `z in (0,1)`, use

\[
\mu_z(A)
=
\sum_{n\in A}(1-z)z^{n-2}.
\]

The total mass of the integer tail beginning at `2^k` is

\[
\boxed{
\mu_z(\{n\ge2^k\})
=z^{2^k-2}.
}
\]

Every `beta_k=1` child has

\[
\rho_{k+1}=\rho_k+2^k\ge2^k,
\]

so all such survivor children at depth `k+1` together represent a disjoint subset of `{n>=2^k}`. Therefore

\[
\boxed{
M_{k+1}^{(1)}(z)
\le
z^{2^k-2},
}
\]

where `M_{k+1}^{(1)}` is the total unresolved mass in children with `beta_k=1`.

For the dyadic choice `z=1/2`,

\[
\boxed{
M_{k+1}^{(1)}
\le
2^{2-2^k}.
}
\]

Thus the floor-jumping side branches have automatically vanishing full-support mass, without any detailed Collatz estimate.

---

## 5. Hard-core mass

Let

\[
M_{k+1}^{(0)}(z)
\]

be the total unresolved mass in floor-preserving `beta_k=0` children. Then exactly

\[
M_{k+1}(z)
=
M_{k+1}^{(0)}(z)+M_{k+1}^{(1)}(z).
\]

Since

\[
M_{k+1}^{(1)}(z)\to0,
\]

we obtain the exact asymptotic reduction

\[
\boxed{
M_k(z)\to0
\iff
M_k^{(0)}(z)\to0.
}
\]

Hence the full-support mass proof problem may be restricted to the **floor-preserving hard core**. The high-floor side branches disappear automatically in the generating mass.

---

## 6. Counterexample interpretation

A finite positive-integer counterexample must eventually satisfy

\[
\boxed{
\beta_k=0\quad\text{for every sufficiently large }k.
}
\]

After that depth, its formation floor is fixed at the same integer `n`, and the survivor path follows the unique floor-preserving child at every refinement.

Therefore the final proof no longer needs to treat both child types symmetrically:

1. `beta=1` is a formation-escape branch and is automatically harmless in full-support mass;
2. `beta=0` is the only branch type capable of supporting a fixed finite counterexample.

The arithmetic survival-ceiling/headroom analysis should therefore be concentrated on the eventual `beta=0` spine.

---

## 7. Refined global theorem target

The Two-Boundary Escape Target can be sharpened to the following equivalent form.

### Eventual-Zero Spine Exclusion Target

Prove that no infinite survivor branch can satisfy

\[
\boxed{
\beta_k=0
\quad\text{for all sufficiently large }k.
}
\]

Equivalently, every infinite survivor branch must contain infinitely many formation jumps

\[
\beta_k=1,
\]

and hence must have

\[
\rho_k\to\infty.
\]

A proof of this target would exclude all finite positive-integer counterexamples while allowing the full 2-adic parity path space to remain intact.

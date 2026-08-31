# A0 s=1 Route-B C4F semantic-scope audit

## Purpose

This note performs a DSD proof-interface audit on the remaining long-membership gate.

The label `C4F` has appeared in downstream status statements, but the current proof record does not supply it as a formally defined Boolean predicate with a specified domain, decision rule, composition law, or equivalence relation.

Therefore `C4F` must not be used as though it were already a mathematical state coordinate or a proved semantic predicate.

This is a scope correction, not a negative mathematical result.

---

## 1. DSD definition audit

A predicate used as a proof gate must at minimum specify

\[
P:\mathcal D\to\{0,1\}
\]

with a defined domain \(\mathcal D\) and an explicit criterion for `P=1`.

A quotient state claimed to preserve the predicate must additionally justify

\[
\sigma(u)=\sigma(v)
\Longrightarrow
P(ur)=P(vr)
\]

for the relevant continuation domain, or provide another exact semantic preservation theorem.

The current `C4F` label does not yet meet that interface. Accordingly:

\[
\boxed{
\text{“C4F-preserving quotient” is not yet a legal proof claim.}
}
\]

Existing certificates correctly avoid making that claim:

- the composable ballot/address state explicitly says `C4F_preserved_by_this_state = False`;
- the correction-state certificate does not claim C4F or unique-target membership;
- prefix-defect pruning explicitly does not promote surviving cylinders to C4F or same-orbit membership.

---

## 2. Replace the placeholder by an explicit semantic target

For a fixed parent physical channel

\[
X(m)=r+2^h m,
\]

define the actual Collatz trajectory deterministically by

\[
X_0(m)=X(m),
\qquad
X_{j+1}(m)=T(X_j(m)).
\]

Let

\[
b_j(m)=X_j(m)\bmod2
\]

be its actual parity sequence.

At any finite horizon \(H\), define

\[
\mathsf{RB}_H(m)=1
\]

iff the actual trajectory of `X(m)` through horizon `H` satisfies **every separately and explicitly defined Route-B gate invoked at that horizon**.

An undefined label such as `C4F` is not counted as a gate until it is replaced by an explicit predicate.

This makes the semantic target well formed even while individual subgates are still being developed.

---

## 3. Physical-domain scope reduction

The existing 72-bit channel-completion theorem proves that in the present A0 physical shell

\[
2^{71}<X<2^{72},
\]

exposing the physical 72-bit address leaves no further source-address parameter:

\[
X=r_{72}+2^{72}n,
\qquad n=0.
\]

Hence every surviving completed address is one unique physical integer `X`, and its later parity sequence is deterministic.

Therefore the current branch does **not** require a decoder for every abstract binary word of arbitrary length.

A sufficient theorem is narrower:

\[
\boxed{
\text{evaluate/close the deterministic long-orbit predicate for every surviving physical }X.
}
\]

The previously stated “universal long-language decoder” is stronger than what this physical A0 branch needs.

This reduction does not make the surviving population small; it removes only unnecessary abstract-word branching.

---

## 4. Same-parameter / same-orbit coherence lemma

Fix one parent channel

\[
X=r+2^h m,
\qquad
Y=T^h(X)=y+3^q m.
\]

Suppose a source-side condition \(P_2\) and an endpoint/formation-side condition \(P_3\) are both pulled back to the **same integer parameter** `m`:

\[
P_2=P_2(m),
\qquad
P_3=P_3(y+3^q m).
\]

Then any representative `m` in their exact intersection refers to one and the same physical pair

\[
(X,Y)=(r+2^h m,\ y+3^q m).
\]

In particular, when the dual-axis CRT pullback produces

\[
m\equiv\omega\pmod M,
\]

every representative of that class satisfies the two conditions on the same underlying channel member.

Thus

\[
\boxed{
\text{exact same-parameter pullback prevents cross-witness gluing.}
}
\]

This is stronger and safer than separately showing that a dyadic witness exists and a ternary witness exists and then assuming they describe the same orbit.

It does **not** assert that every independently constructed state merge is same-orbit coherent; the common-parameter derivation is essential.

---

## 5. Consequence for family closure

The exact finite-horizon family theorem and the dual-axis CRT theorem now provide the following legal pipeline:

\[
\text{parent channel}
\to
\text{common parameter }m
\to
\begin{cases}
\text{dyadic finite-horizon block state},\\
\text{ternary finite formation state}
\end{cases}
\to
\text{exact CRT family}
\to
\mathsf{RB}_H.
\]

All finite-horizon subpredicates that are explicitly defined can therefore be transported family-wise without singleton enumeration and without witness mismatch.

---

## 6. What remains genuinely open

After removing the undefined placeholder, the remaining semantic problem is:

> Find a recursively/hierarchically computable sufficient state for the **explicit deterministic long-orbit Route-B predicate** on the surviving physical A0 addresses.

The state may use already certified coordinates such as correction/channel state, ballot state, formation rank/carry or finite target residues, and hierarchy/run metadata, but every included coordinate must have an explicit preservation theorem.

The desired statement is of the form

\[
\boxed{
\mathsf{RB}_{H'}(m)
=F(\sigma_{H,H'}(m))
}
\]

where \(\sigma\) can be renewed or composed without materializing all \(H'-H\) bits.

---

## 7. DSD status

✅ `C4F` identified as a semantic placeholder rather than a proved predicate;

✅ undefined predicate is removed from legal proof dependencies;

✅ physical-domain obligation reduced from all abstract long words to all surviving deterministic physical trajectories;

✅ same-parameter coherence closes the witness-gluing problem for exact family pullbacks;

✅ finite-horizon dyadic/ternary family transport remains valid;

❌ no recursive state for the complete deterministic long-orbit predicate has yet been proved;

❌ target Christoffel hierarchy cannot automatically be assigned to an arbitrary candidate trajectory;

❌ no Route-B global closure or Collatz conclusion is claimed.

## Gate update

The next gate should no longer be written as “prove C4F preservation.”

Use instead:

\[
\boxed{
\textbf{G4-S: deterministic semantic renewal / hierarchy factorization.}
}
\]

G4-S asks whether every surviving physical channel family can be advanced through a long deterministic segment using a finite or recursively renewable state, while preserving every explicitly defined Route-B predicate.

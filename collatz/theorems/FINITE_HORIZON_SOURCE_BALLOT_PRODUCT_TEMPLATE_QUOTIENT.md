# Finite-horizon source/ballot quotients

Status: **EXACT for a fixed future bit horizon / not a global source-payload merge**

## Purpose

The 8-jump Route-B frontier contains many exact affine source cylinders. Equal ballot control alone does not justify merging different source payloads, but short-horizon transition work can still be shared exactly.

Two nested finite-horizon quotients are useful:

1. a **full transition template** preserving the emitted parity map and ballot decisions;
2. a coarser **predicate-relative acceptance signature** preserving only pure-ballot accept/reject behavior.

Neither identifies distinct exact source families.

## 1. Source projective state

Let

\[
T^h(X)=y+3^q m.
\]

For future raw-bit horizon \(d\), define

\[
\boxed{
Q_d^{src}(y,q)
=
\left(y\bmod2^d,\;3^q\bmod2^d\right).
}
\]

The certified source-channel projective theorem implies that for every low parameter residue

\[
m\bmod2^d,
\]

this state determines the complete emitted parity prefix of length \(d\).

## 2. Ballot future signature

Let

\[
Q(n)=\lceil n\log_3 2\rceil,
\qquad
S=q-Q(h)\ge0.
\]

Define

\[
\boxed{
B_d(h,S)
=
(S,\Delta_1,\ldots,\Delta_d),
}
\]

where

\[
\Delta_i=Q(h+i)-Q(h+i-1)\in\{0,1\}.
\]

For any proposed future parity word \(w_1\cdots w_d\), every intermediate ballot inequality is determined by comparing

\[
S+\sum_{j=1}^i w_j
\]

with

\[
\sum_{j=1}^i\Delta_j.
\]

Hence \(B_d\) determines all pure-ballot verdicts through the horizon.

## 3. Full product-template theorem

Define

\[
\boxed{
P_d=(B_d,Q_d^{src}).
}
\]

If two exact source cylinders have the same \(P_d\), then for every low parameter residue modulo \(2^d\) they:

1. emit the same parity word of length \(d\);
2. receive the same pure-ballot accept/reject verdict at every intermediate prefix;
3. have the same outgoing surplus relative to the corresponding end-of-horizon threshold phase.

Thus \(P_d\) is an exact finite-horizon transition template.

## 4. Predicate-relative quotient

For the active pure-ballot predicate, preserving rejected-path parity details is stronger than necessary.

Define the depth-\(d\) binary decision tree \(\mathcal A_d\) over future parameter bits \(e\in\{0,1\}\):

- follow the exact source/parity transition induced by the parameter bit;
- mark a branch `REJECT` as soon as the ballot inequality fails;
- otherwise recurse;
- at depth \(d\), mark the surviving leaf `ACCEPT`.

Two source states are **predicate-equivalent through depth \(d\)** when their interned decision trees are identical.

Then they have exactly the same accepted low-parameter residues modulo \(2^d\) for the pure-ballot predicate, even if their rejected branches emit different parity words.

Therefore

\[
\boxed{
\mathcal A_d
\text{ is a coarser exact predicate-relative quotient than }P_d.
}
\]

It remains finite-horizon: after the requested depth, later source-sensitive predicates may distinguish the states.

## 5. What may be shared

Equal full templates may share:

- parameter-bit to parity-bit transition code;
- ballot decision logic;
- accepted low-residue masks;
- any computation proven to observe only these finite-horizon coordinates.

Equal predicate-relative signatures may share pure-ballot pruning logic and accepted-residue masks, but not rejected-path parity details.

The following remain exact payload data:

\[
r,\quad[m_{lo},m_{hi}],
\]

and any finer source information needed after the horizon.

Thus

\[
\boxed{
\text{finite-horizon quotient equality}
\not\Rightarrow
\text{source-family identity}.
}
\]

## 6. Current 8-jump measurement — full templates

At the certified 8-jump frontier there are

\[
14{,}224
\]

exact source cylinders.

| future raw bits \(d\) | full templates | reused payload instances |
|---:|---:|---:|
| 1 | 18 | 14,206 |
| 2 | 88 | 14,136 |
| 3 | 203 | 14,021 |
| 4 | 583 | 13,641 |
| 5 | 1,964 | 12,260 |
| 6 | 3,453 | 10,771 |
| 7 | 5,715 | 8,509 |
| 8 | 8,372 | 5,852 |
| 9 | 10,888 | 3,336 |
| 10 | 12,582 | 1,642 |
| 11 | 13,443 | 781 |
| 12 | 13,923 | 301 |
| 13 | 14,102 | 122 |
| 14 | 14,148 | 76 |
| 15 | 14,178 | 46 |
| 16 | 14,209 | 15 |
| 17 | 14,213 | 11 |
| 18 | **14,224** | **0** |

At \(d=4\), about \(95.90\%\) of one-template-per-payload transition work is reusable. At \(d=8\), the corresponding figure is about \(41.14\%\).

## 7. Current 8-jump measurement — predicate-relative signatures

After forgetting all rejected-path parity information and retaining only the exact pure-ballot acceptance decision tree:

| future raw bits \(d\) | acceptance signatures | reused payload instances |
|---:|---:|---:|
| 4 | 169 | 14,055 |
| 8 | 7,612 | 6,612 |
| 12 | 13,786 | 438 |
| 16 | 14,207 | 17 |
| 18 | **14,224** | **0** |

This is stronger evidence than the full-template table for the current finite frontier: even after predicate-relative forgetting, all 14,224 payloads are distinguished by their next-18-bit pure-ballot acceptance language.

This does **not** prove that no stronger invariant or quotient exists.

## 8. DSD interpretation

### Resolution

Both quotients are explicitly indexed by finite horizon \(d\). Their source precision is consumed as bits are processed.

### Predicate-relative forgetting

Discarding rejected-path parity details is legal for the pure-ballot predicate and yields a strictly coarser quotient.

### State sufficiency

The quotient is sufficient only for the selected horizon and predicate. It is not sufficient for indefinite source continuation, checkpoint realization, or later source-sensitive predicates.

### Equivalence

Equal finite-horizon signature means equal finite-horizon problem, not equal mathematical source object.

### Closure

The observed complete separation at \(d=18\) shows that neither the full product template nor the pure-ballot-only acceptance signature currently provides a stable horizon-independent compression of the 8-jump payloads.

## 9. Consequence for S10

Use these quotients as **execution/DAG-sharing tools**.

They reduce duplicated short-horizon computation while preserving every exact source payload. But proof-level contraction still requires at least one of:

1. a stronger source-sensitive invariant whose future width stays bounded or contracts;
2. an exact whole-payload rejection predicate;
3. a later predicate whose activation makes previously distinct source information irrelevant and therefore legally forgettable.

## Certificate

`../src/A0_s1_routeB_8jump_source_ballot_product_template_quotient_certificate.py`

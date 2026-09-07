# First universal cell: 340-block nearest-neighbor endpoint-halo decomposition

Date: 2026-09-07

Status: **SAFE address-geometric reduction.** This theorem does not eliminate any block by itself. It proves that candidate-language endpoint/Hensel interactions between different surviving top-address blocks are strictly nearest-neighbor and confined to exact narrow boundary halos.

No Collatz proof is claimed.

---

## 1. Current ordinary-start partition

The current first-cell start window is

\[
2^{71}<N<1364\cdot2^{61}.
\]

At resolution `2^61`, define

\[
I_a=[a2^{61},(a+1)2^{61}),
\qquad
a=1024,\ldots,1363.
\]

There are exactly

\[
\boxed{340}
\]

surviving top-address blocks, each of width

\[
W=2^{61}.
\]

---

## 2. Endpoint-fiber displacement bound

The full-first-cell endpoint q-lock theorem gives, for two candidate-language states sharing one endpoint,

\[
q_1=q_2=q
\]

and

\[
|N_1-N_2|
=\frac{|R_1-R_2|}{3^q}
=|S_1-S_2|.
\]

Every universal-spine correction obeys

\[
S\le q/3.
\]

Therefore

\[
|N_1-N_2|<q/3\le q_0/3.
\]

For

\[
q_0=72,057,431,991,
\]

`q0` is divisible by 3 and the start displacement is an integer. Hence the largest possible positive integer displacement is

\[
\boxed{
H=\frac{q_0}{3}-1
=24,019,143,996.
}
\]

In particular,

\[
\boxed{H<2^{35}\ll2^{61}=W.}
\]

---

## 3. Nearest-neighbor block theorem

Because

\[
2H<W,
\]

one same-endpoint candidate fiber cannot cross two block boundaries.

Therefore:

\[
\boxed{
\text{one endpoint fiber can meet at most two adjacent top-address blocks.}
}
\]

It can never connect

\[
I_a\longleftrightarrow I_{a+r}
\qquad (|r|\ge2).
\]

Thus the block-coupling graph induced by candidate-language endpoint/Hensel equivalence is a subgraph of the path

\[
1024-1025-\cdots-1363.
\]

This is an exact lineage statement, not a heuristic locality assumption.

---

## 4. Boundary halos

For an internal boundary

\[
b_a=(a+1)2^{61}
\]

between `I_a` and `I_{a+1}`, define its two-sided endpoint halo by the integer starts within distance at most `H` needed for a cross-boundary fiber.

Only starts in

\[
[b_a-H,b_a-1]
\]

or

\[
[b_a,b_a+H-1]
\]

can participate in a candidate-language endpoint fiber crossing that boundary.

There are

\[
339
\]

internal boundaries. Since `2H<W`, all these internal boundary halos are pairwise disjoint.

Their total integer cardinality is exactly

\[
\boxed{
2H\cdot339
=16,284,979,629,288.
}
\]

The strict candidate interval contains

\[
340\cdot2^{61}-1
\]

integers, so

\[
\boxed{
\frac{\text{internal cross-block halo integers}}
{\text{candidate-window integers}}
<\frac1{48,140,000}.
}
\]

This fraction is diagnostic of computational locality only. It is **not** a density-to-emptiness argument.

---

## 5. Interior independence for endpoint quotienting

Define a uniform protected interior

\[
J_a=[a2^{61}+H,(a+1)2^{61}-H).
\]

Any candidate-language endpoint fiber containing a start in `J_a` is entirely contained in `I_a`.

Therefore endpoint quotienting of the block interiors may be performed **independently block by block**.

Only the 339 adjacent block pairs require synchronized treatment, and only inside their exact boundary halos.

This changes the computational architecture from a nominal all-to-all 340-block coupling problem into

\[
\boxed{
340\ \text{block-local interior problems}
+339\ \text{nearest-neighbor halo interfaces}.
}
\]

---

## 6. Scope at the outer boundaries

The lower and upper edges of the entire candidate interval are not treated as ordinary internal block interfaces.

A start close to `B0` or the upper cap may in principle have an endpoint mate outside the present candidate window. Whether such an outside state is admissible or can be used as a minimality competitor depends on the separate hypotheses of the relevant Hensel/root-minimality theorem.

Therefore the present halo count concerns **internal cross-block candidate-language coupling only**.

---

## 7. DSD audit

### CLOSED / SAFE

1. full-first-cell endpoint q-lock gives common `q` inside a candidate endpoint fiber;
2. universal-spine correction gives `|N1-N2|<q/3`;
3. terminal displacement is bounded by `H=24,019,143,996<2^35`;
4. each top block has width `2^61`;
5. an endpoint fiber can meet at most two adjacent blocks;
6. the 339 internal coupling halos are disjoint and have exactly `16,284,979,629,288` integer starts in total;
7. block interiors are independent with respect to candidate-language endpoint quotienting.

### OPEN

1. solve or compress the 340 block-local interior problems;
2. solve the 339 local halo interfaces;
3. combine endpoint locality with root-Hensel maximality through depth 195 and terminal correction requirements;
4. eliminate the first universal cell.

### PROHIBITED UPGRADES

1. Do not infer that the small halo fraction means the halos are empty.
2. Do not discard outer-window competitors solely because they are outside the 340-block candidate language.
3. Do not treat endpoint locality as locality of all other proof constraints; terminal correction remains a global same-word requirement.
4. Do not infer first-cell or Collatz closure from the decomposition.

---

## 8. Reproducibility

Certificate:

`collatz/src/first_cell_340block_endpoint_halo_certificate.py`

Commit:

`f2774276400f8d4519545d0c43b63c1f3e8a12ea`

Expected output:

```text
PASS
surviving top-address blocks = 340
max same-endpoint candidate displacement = 24019143996
internal block boundaries = 339
endpoint block-coupling graph is nearest-neighbor only
```

---

## 9. Next target

The next useful calculation is **one-block normalization**. Translate

\[
N=a2^{61}+x,
\qquad 0\le x<2^{61},
\]

and determine which parts of the root-prefix and terminal-correction obligations depend only on `x`, which depend on the 11-bit block label `a`, and which are confined to the `H`-wide interfaces. A valid translation/right-congruence theorem could then group multiple block interiors without losing the same ordinary integer.
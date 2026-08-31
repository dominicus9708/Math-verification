# A0 s=1 Route-B — online parameter/parity transducer

Date: 2026-08-31  
Branch: `collatz-stage4-window-threshold`

## 1. Why this step matters

The projective family quotient reduced a finite source family to

\[
\mathcal F_d(P,I)=\left(Q_d(P),\Pi_d(I)\right),
\]

but the remaining family-cover problem was phrased in terms of residue sets

\[
R_\sigma\subseteq\mathbb Z/2^\ell\mathbb Z.
\]

A naive implementation would first enumerate all `2^ell` residues, convert them to parity blocks, classify the blocks, and only then group the residues.

That enumeration is not structurally necessary.  The parameter residue bits and parity bits are connected by an exact online bijective transducer.

---

## 2. Exact one-bit source decomposition

At a source channel write

\[
T^h(X)=y+g m,
\qquad
g=3^q\quad\text{odd}.
\]

Split the current parameter as

\[
m=e+2n,
\qquad e\in\{0,1\}.
\]

Then

\[
y+g(e+2n)=y+ge+2gn.
\]

Because `g` is odd, the next parity bit is

\[
\boxed{
b\equiv y+ge\equiv y+e\pmod2.
}
\]

Hence

\[
\boxed{e\equiv b-y\pmod2.}
\]

The input parameter bit determines the output parity bit, and conversely the output parity bit determines the input parameter bit once the current channel state is known.

---

## 3. Exact affine transition

If `b=0`,

\[
T(y+gm)
=
\frac{y+ge}{2}+gn,
\]

so

\[
\boxed{
y'={y+ge\over2},\qquad g'=g.}
\]

If `b=1`,

\[
T(y+gm)
=
{3(y+ge)+1\over2}+3gn,
\]

so

\[
\boxed{
y'={3(y+ge)+1\over2},\qquad g'=3g.}
\]

Both numerators are even precisely because `b` was chosen as the parity of `y+ge`.

This is an exact integer identity, not a finite approximation.

---

## 4. Projective one-bit transducer

For `d>=1`, let

\[
Q_d=(Y,G)
=
(y\bmod2^d,\;g\bmod2^d).
\]

Given an input parameter bit `e`, define

\[
b=(Y+e)\bmod2.
\]

For `b=0`,

\[
Y'={Y+Ge\over2}\pmod{2^{d-1}},
\qquad
G'=G\pmod{2^{d-1}}.
\]

For `b=1`,

\[
Y'={3(Y+Ge)+1\over2}\pmod{2^{d-1}},
\qquad
G'=3G\pmod{2^{d-1}}.
\]

Therefore there is a deterministic exact transition

\[
\boxed{
\delta_d:(Q_d,e)\longmapsto(b,Q_{d-1}).
}
\]

The inverse input bit is simultaneously available from

\[
\boxed{e=(b-Y)\bmod2.}
\]

Thus the transition is triangular and online-bijective.

---

## 5. Depth-d bijection theorem

Let

\[
a=e_0+2e_1+\cdots+2^{d-1}e_{d-1}
\]

be a parameter residue modulo `2^d`.

Starting at `Q_d`, feed the bits `e_0,e_1,...,e_{d-1}` into the transducer.  It emits a parity block

\[
B=(b_0,b_1,\ldots,b_{d-1}).
\]

Because every output bit recovers the corresponding input bit online, the depth-`d` map

\[
\boxed{
a\pmod{2^d}\longleftrightarrow B\in\{0,1\}^d}
\]

is a bijection.

This is the bitwise refinement of the previously certified batch theorem that

\[
B\mapsto m_B\pmod{2^d}
\]

is a permutation.

The online theorem is stronger operationally: the residue address does not have to be materialized before the parity-language state can be updated.

---

## 6. Product-state pullback of a parity classifier

Let `S` be any deterministic parity-language state whose bit transition is

\[
S' = \Delta(S,b).
\]

Examples include the already derived finite-resolution correction state and exact compositional ballot state, provided the chosen `S` retains every coordinate required by the certificate being tested.

Form the product state

\[
\boxed{\mathcal P_d=(Q_d,S).}
\]

A parameter bit `e` then induces

\[
(Q_d,S)
\xrightarrow{e}
(Q_{d-1}',\Delta(S,b)),
\]

where `b` is emitted by the exact source transducer.

Consequently any block class determined by the terminal parity state can be pulled back directly to parameter residues by traversing this product machine.

For a terminal class `sigma`,

\[
R_\sigma
=
\{a\pmod{2^d}:\text{the product transducer ends in class }\sigma\}.
\]

No preliminary list of all parity blocks or all parameter residues is mathematically required.

---

## 7. Exact decision-DAG representation

At level `i`, merge all prefixes that reach the same product state

\[
(Q_{d-i},S_i).
\]

Because future transitions depend only on that state and the remaining parameter bits, merged prefixes have identical continuation languages.

Hence the accepted residue family has an exact layered decision-DAG representation whose nodes are the reachable product states, not the raw set of `2^d` prefix addresses.

This establishes an exact **recursive representation principle** for the sets `R_sigma`.

However, no polynomial node bound follows automatically.  In the worst case the number of distinct reachable states can still grow exponentially with `d`.  State merging is therefore available exactly, but sufficient state reuse remains a quantitative/open issue.

---

## 8. Coupling to interval payloads

The decision DAG is compatible with the interval quotient from the previous step.

At each parameter input bit `e`, the source interval is restricted to the corresponding parity class of its current parameter and pulled back by

\[
m=e+2n.
\]

The interval state

\[
\Pi_d(I)=(|I|,L\bmod2^d)
\]

then transitions exactly to `Pi_{d-1}` of the child, while `Q_d` transitions to `Q_{d-1}`.

Thus a full finite-horizon recursive node may be taken as

\[
\boxed{
\mathcal N_d=(Q_d,\Pi_d,S).
}
\]

The source rank

\[
(|I|,d)
\]

remains lexicographically well-founded along nonempty child paths.

---

## 9. Finite implementation audit

`collatz/src/A0_s1_routeB_parameter_parity_online_transducer_certificate.py` checks through `d=8`:

- 2,400 exact one-bit/projective transition comparisons;
- 76,500 exhaustive parameter-residue to parity-block comparisons against the batch formula;
- 76,500 online inverse reconstructions;
- 76,500 comparisons with deliberately different exact representatives of the same `Q_d` state.

For each tested parent and depth, all `2^d` parameter residues emit `2^d` distinct parity blocks.

These computations audit the implementation.  The bijection theorem follows from the exact one-bit identities above.

---

## 10. DSD audit

### Exact / closed

- the next parity bit obeys `b=(y+e) mod 2`;
- the parameter input bit is recovered as `e=(b-y) mod 2`;
- exact affine child formulas are available for both output bits;
- the transition depends only on `Q_d` at future precision `d`;
- depth-`d` parameter residues and parity blocks are related by an online bijection;
- any deterministic parity-state classifier can be pulled back to a parameter-bit product transducer;
- residue classes `R_sigma` therefore admit exact recursive decision-DAG generation;
- coupling this DAG to `Pi_d` preserves the previous finite-horizon family induction and rank descent.

### Finite regression only

- the exhaustive checks through depth 8 are implementation guards, not the proof.

### Still open

1. a useful upper bound on the number of reachable product states as `d` grows;
2. proof that the Route-B admissibility/correction/ballot state merges enough nodes to avoid exponential growth at all relevant scales;
3. a horizon-independent right-congruence or recursive hierarchy sufficient for universal Route-B membership;
4. the global Collatz conjecture.

---

## 11. Updated bottleneck

The residue sets themselves no longer need to be treated as explicit address lists.  They can be generated exactly as product-state DAGs.

The next question is now quantitative and structural:

\[
\boxed{
\text{How many distinct reachable }(Q,S)\text{ nodes survive per depth, and what exact identities merge them?}
}
\]

The next audit should therefore measure and then attempt to prove state-merging laws for the actual Route-B correction+ballot classifier, while keeping the Christoffel/run hierarchy target-specific unless universality is independently proved.

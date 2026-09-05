# S10 block arithmetic / block-language gap audit

Date: 2026-09-03

Status: **block arithmetic CLOSED / source-sensitive finite block quotient OPEN**

## Audited question

Can the active A0 `s=1` Route-B source families now be advanced in large blocks without the cylinder explosion seen under repeated one-odd-event valuation jumps?

The answer separates into four distinct claims that must not be conflated.

## 1. Fixed-block arithmetic — CLOSED

For any supplied fixed parity block `B` with

\[
(|B|,q(B),C(B))=(b,p,\gamma),
\]

the exact multibit source-channel transducer consumes the block on an affine source family without bitwise orbit enumeration.

For

\[
X=r+2^h m,
\qquad
T^h(X)=y+3^q m,
\]

there is exactly one parameter residue modulo `2^b` realizing `B`, and the child remains an exact affine source/current-state cylinder.

Therefore **large-block arithmetic is not the missing theorem**.

Canonical object:

- `../src/A0_s1_multibit_block_transducer_certificate.py`.

## 2. Valuation-tree compilation — CLOSED

A finite valuation tuple

\[
(a_1,\ldots,a_d)
\]

emits the block

\[
B=0^{a_1}1\cdots0^{a_d}1.
\]

The sequential valuation-jump refinement is exactly identical to one multibit transition by this compiled block, including the source residue, endpoint affine channel and parameter interval.

Therefore finite future ballot-control signatures may be compiled into reusable macroblock transition templates without changing source semantics.

Canonical objects:

- `../theorems/VALUATION_MACROBLOCK_COMPILATION.md`;
- `../src/A0_s1_valuation_macroblock_compilation_certificate.py`.

This reduces transition overhead, not the number of distinct source payloads.

## 3. Universal maximal macroblock formation — CLOSED but infinite-type

The existing exact macroblock formation theorem states that every odd positive state has a unique maximal accelerated block

\[
1^H0^D,
\qquad H,D\ge1,
\]

with its formation set equal to one exact dyadic residue class. Any finite sequence of prescribed macroblock types determines a nested source residue class.

Thus there is a universal macroblock language in the broad sense.

However its alphabet

\[
\{(H,D):H,D\ge1\}
\]

is infinite. The theorem does not collapse all dangerous Route-B candidates to a bounded finite set of block types.

Historical exact source:

- `../notes/2026-08-11-macroblock-formation-classes.md`.

## 4. Christoffel / Euclidean finite-state reductions — SCOPE-LIMITED

### Exact Christoffel two-block alphabet

The historical theorem reducing macroblocks to

\[
(H,D)\in\{(1,1),(2,1)\}
\]

applies explicitly to the **exact Christoffel supercritical renewal equality class**, not to arbitrary near-Christoffel or general active Route-B candidate words.

Therefore it cannot be promoted to a universal two-block alphabet for the 14-root family without an additional membership theorem.

### Euclidean `(Sigma,M)` multiplicity state

For a fixed mechanical reference block, the pair

\[
(\Sigma,M)
\]

is sufficient for pure survival/slack continuation, and multiple internal bit patterns may share the same future survival set.

But the same theorem records distinct canonical source residues for those internal patterns. Therefore equal `(Sigma,M)` is a **control equivalence**, not automatically a source-sensitive Route-B equivalence.

These objects can be reused as control templates only while the exact source payload remains separate.

## DSD classification

### D — Domain

The active domain is the 14-root A0 `s=1` Route-B source forest after certified upstream pruning.

Historical Christoffel equality and Euclidean survival theorems may be imported only in their stated domains.

### R — Resolution

The active source-sensitive resolution remains

\[
(r,y,[m_{lo},m_{hi}],h,S),
\]

with fixed-target counters derived from `(h,S)`.

A quotient that forgets `r` or the exact parameter fiber is insufficient unless every unresolved future predicate is proved invariant under that forgetting.

### S — State sufficiency

- fixed block metadata is sufficient to execute one block;
- `(Sigma,M)` is sufficient for its stated survival predicate;
- neither fact is sufficient for full source/checkpoint/debit/tail equivalence.

### E — Equivalence

The missing theorem must establish a genuine source-sensitive future equivalence, not merely equal ballot continuation or equal block multiplier.

A useful target has the form

\[
S_1\sim S_2
\iff
\mathcal F_{future}(S_1)=\mathcal F_{future}(S_2)
\]

for all still-active defined predicates at the same observation resolution.

### T — Transition

Transition arithmetic is exact and already composable. The gap lies in **language generation / quotienting**, not transition correctness.

### C — Closure

No current theorem proves that the infinite universal macroblock alphabet collapses to a fixed finite source-sensitive alphabet over all surviving Route-B families.

No current theorem proves that a finite Christoffel equality alphabet covers arbitrary active candidates.

### N — Non-independence

- H/L/Christoffel representation of the same word is not an extra pruning factor;
- equal survival state does not erase distinct source addresses;
- compiled valuation macroblocks do not create new independent restrictions.

### O — Outstanding theorem

The principal S10 gap is now:

> Construct a source-preserving finite block cover or quotient that suppresses family-state growth while preserving every still-active Route-B predicate.

Acceptable forms include either:

1. a finite or uniformly bounded family of exact macroblock classes emitted from the minimized source/control state; or
2. a proved source-sensitive equivalence that merges infinitely many/large families of macroblock histories; or
3. a block-level rejection theorem strong enough to close whole source fibers before state multiplication dominates.

## Negative result / forbidden promotion

It is **not** valid to:

- force the threshold Christoffel block or `U/D` equality alphabet on arbitrary active candidates;
- merge `001,010,100` merely because they have the same Euclidean survival state;
- call macroblock compilation itself a pruning theorem;
- replace exact source payload by multiplicity counts while later source/checkpoint predicates remain unresolved.

## Practical next step

Use the compiled finite-horizon valuation macroblocks as the implementation substrate, then attach one genuinely source-sensitive predicate at macroblock boundaries. The first useful candidate should reject or identify entire congruence fibers rather than only reuse ballot-control code.

Checkpoint residues remain late-activated according to `PREDICATE_ACTIVATION_SCHEDULE.md`; they should not be carried globally merely to manufacture such a predicate.

# A0 s=1 Route-B closure status

Date: 2026-08-28

Status: **current audited stopping point**. This document summarizes what is closed, what is only necessary pruning, and what remains open. It is intentionally conservative.

## 1. Fixed A0 s=1 data

\[
J_0=10439860591,\qquad R_0=6586818670,
\]

\[
t_0=10J_0=104398605910,\qquad j_0=10R_0+1=65868186701.
\]

Current physical input shell:

\[
2^{71}<X<2^{72}.
\]

The checkpoint satisfies

\[
2^{72}<Z<2^{73}.
\]

## 2. Exact structural reductions already closed

### 2.1 Ten-block threshold compression

The threshold word is exactly

\[
W_{th}=U L^9,
\]

where `L` is the lower mechanical/Christoffel word of slope `R0/J0`, and `U` differs from `L` only at the left endpoint.

The base word `L` is represented by an exact 129-node Stern-Brocot/Christoffel DAG instead of `J0` individual bits.

### 2.2 Correction injectivity and target-aware decoding

For fixed `(t,j)`, the correction map is injective. A target correction therefore has at most one parity word.

Modulo `2^h`,

\[
C_{req}\equiv-3^{j_0}X\pmod{2^h},
\]

so every shallow odd position can be decoded from `X` without materializing the giant correction or knowing `Z`.

### 2.3 Pure-ballot coordinate theorem

For odd positions `a_r`, pure ballot is exactly equivalent to

\[
2^{a_r}\le3^{r-1}
\]

for all ranks `r`, together with the terminal odd-count condition.

Hence full prefix scanning can be replaced by an odd-position coordinate test once the positions are decoded.

### 2.4 Physical 72-bit determinization

Because `2^71<X<2^72`, the first 72 parity bits expose the complete ordinary integer `X`. Once `X` is fixed, every later finite parity bit is deterministic under the actual Collatz map.

This permits shallow address enumeration to hand off to exact orbit extension without introducing an additional finite-parity formation state.

## 3. Finite near-threshold closure

Independent direct and determinized implementations agree through Hamming radius 7 at depth 75.

Every bounded physical pure-ballot first-75 word with

\[
d_{75}\le7
\]

fails under deterministic continuation.

At exact radius 7:

- pure-ballot first-75 words: `188,574,243`;
- physical-shell candidates: `11,784,860`;
- candidates satisfying the then-current X upper bound: `4,662,684`;
- survivors through the deterministic scan: `0`;
- latest pure-ballot failure: prefix `454`.

Therefore

\[
\boxed{d_{75}\ge8}
\]

is a SAFE necessary condition for any remaining Route-B survivor.

## 4. Correction-envelope and physical-X pruning

The 129-node Christoffel DAG gives a directed interval for the normalized base correction:

\[
4751385314<\frac{C(L)}{2^{J_0}}<4751385315.
\]

Consequently the full threshold correction satisfies

\[
47513853148<\frac{C(W_{th})}{2^{t_0}}<47513853149.
\]

Combining the threshold envelope with the certified radius-7 correction-defect floor yields

\[
\boxed{X\le3234977022306677631165.}
\]

This supersedes the earlier coarser upper bound

\[
X\le3295414002074039191016.
\]

The logical dependency is one-way:

`old X bound -> radius-7 closure -> d75>=8 -> defect floor -> refined X bound`.

The refined bound must not be used retroactively as the proof of radius-7 closure.

## 5. First-defect dyadic shell

Let

\[
X_{th}=4697939311072332635131.
\]

For any remaining pure-ballot candidate, the first threshold disagreement is necessarily `0 -> 1` and can occur only at

\[
F=\{2,5,8,10,13,16,18,21,24,27,29,32,
35,37,40,43,46,48,51,54,56,59,62,65\}.
\]

Hence

\[
\boxed{v_2(X-X_{th})\in F.}
\]

Inside the refined X interval, the union of these 24 disjoint dyadic shells contains exactly

`125,072,439,876,495,812,978`

ordinary integers out of

`873,793,780,871,855,024,317`,

about `14.3137%`.

This is exact cardinality pruning, not a probability statement.

## 6. Refined boundary exposure

The physical and correction bounds sharpen the boundary windows.

### Checkpoint Z

The actual Z interval is narrow enough that

\[
2^{27}3^{28}
\]

already exceeds its width. Therefore

\[
\boxed{27\text{ tail dyadic bits}+28\text{ prefix terminal trits}}
\]

suffice for CRT singleton exposure of `Z`.

### Debit L_minus

The refined corridor is

\[
669562762561\le L_-\le934928480993.
\]

Its width is below `3^24`, so terminal prefix information needs only

\[
\boxed{24\text{ trits}}
\]

for ordinary-value exposure, improving the previous 26-trit depth.

### Credit L_plus

The existing coarse corridor width is below `2^39`, so

\[
\boxed{39\text{ dyadic bits}}
\]

suffice, improving the previous 40-bit depth.

These are exposure theorems only. They do not imply full long-block extension.

## 7. Mixed-place / C4F audit

The renewal/shadow notes show that genuine formation arithmetic can couple three places through a normalized Christoffel defect `eta`:

- real shadow lowering;
- 2-adic formation-address shift;
- modular renewal-gap shift.

However no repository object currently justifies identifying every local surplus/Hensel variable with a complete `C4F` Boolean predicate.

The early first-75 defect also vanishes modulo `3^47` in the terminal ternary channel because its `3`-power is enormous. Thus a direct contradiction between the new early dyadic defect and terminal `3^28`/`3^47` saturation is REJECTED.

The dyadic channel does see the defect sharply through the 24 valuation shells.

## 8. Current exact OPEN gate

The Route-B problem has been reduced to a synchronized long-extension/membership problem:

\[
\boxed{C_{req}(X,Z)\in\mathcal C_{pre}}
\]

with the candidate already constrained by

- refined X interval;
- 24 dyadic first-defect shells;
- exact pure-ballot odd-position inequalities;
- 27x28 checkpoint exposure;
- 24-trit `L_-` exposure;
- 39-bit `L_+` exposure;
- deterministic finite continuation after 72 exposed X bits.

The remaining work is not to enumerate all corrections. By injectivity, one target has at most one correction word. The desired final mechanism is a compressed block-jump valuation/formation decoder that proves or rejects that unique candidate through the full `t0` pre bridge and the tail first-passage bridge.

## 9. What is not proved

The following remain OPEN and must not be silently absorbed into the closed Route-B results:

1. full correction-language membership / nonmembership for every remaining X shell;
2. exact C4F/renewal-gap/global formation compatibility;
3. full pre and tail extension;
4. Route-A independent lower-bound completion;
5. all-surplus `s>=2` coverage;
6. cycle, K1 surplus recovery, later/infinite survivor, and final global branch completeness.

Therefore the repository does **not** contain a proof of the Collatz conjecture.

## 10. DSD classification at this stopping point

### EXACT THEOREM

- ten-block Christoffel structure;
- correction injectivity;
- modular prefix decoder;
- pure-ballot/odd-position equivalence;
- composable pure-ballot/address state;
- physical 72-bit determinization;
- refined shallow exposure depths.

### CERTIFIED ARITHMETIC

- radius 0..7 finite closure and its independent cross-checks;
- threshold correction interval;
- refined X bound and L-minus corridor;
- first-defect shell cardinalities.

### SAFE NECESSARY PRUNING

- `d75>=8`;
- `X<=3234977022306677631165`;
- `v2(X-X_th) in F`;
- 27x28 / 24-trit / 39-bit boundary exposure constraints.

### REJECTED

- interval inclusion implies correction-language membership;
- endpoint/address exposure implies same-orbit connectivity;
- multiplying marginal density/cardinality ratios as if independent;
- using terminal ternary saturation to contradict an early defect that vanishes in that modulus;
- treating an unspecified C4F memory state as already preserved by the pure-ballot quotient.

### OPEN

The unique-target long block-jump formation decoder and global branch completeness.

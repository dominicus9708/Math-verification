# G13 natural-cut reverse same-word handoff

Date: 2026-08-16

Status: **exact candidate-specific reverse preimage exclusion + finite diagnostic over a beam-generated candidate set**.  The reverse formulas are exact.  The explicit `delta=1` G13 ordinary candidate is rigorously excluded from the current R1 start interval.  The 124-candidate aggregate is a diagnostic because the candidate set itself came from a beam search and is not exhaustive.  This note does not prove Collatz.

## 1. Why the natural cut changes the problem

The current R1 entrance theorem gives

\[
\boxed{x_{1539}<2^{954}.}
\]

Hence, in 19-bit canonical lift chunks for the internal G13 gate,

\[
\boxed{t_{50}<16,\qquad t_b=0\ (b\ge51).}
\]

Once the high lift chunks vanish, the G13 tail is not a freely selectable parity orientation.  It is the deterministic accelerated Collatz orbit of the finite ordinary gate-start integer `x`.

Thus a candidate G13 relation must pass two different tests:

1. internal gate arithmetic / same-q relation;
2. reverse same-word attachment to an ordinary start in the current pre-gate R1 core.

## 2. A natural G13 small-credit candidate

A finite search respecting the `2^954` natural cut found the ordinary gate start

\[
\begin{aligned}
x={}&9311066934133191055179217771751644756458780835642375520644606697570370834878851085876330120952372828601875854086643506229770877868471756436379730259097164274868063513702695410370082518062231340901656195848133042167901156081765468572447679246085622583924868464925000059470402523777450879.
\end{aligned}
\]

Its bit length is 950.

For the compared pair `x` and `x-4096`, the blockwise same-q relation reaches, at G13 block 51,

\[
\boxed{\delta=1.}
\]

At that block both local words have `q=4`; the small credit is obtained by spending eight units of local odd-count height relative to the mechanical block:

\[
H_{\rm loc}:1\to-7.
\]

This proves that the finite-natural cut alone does not force the scalar credit to stay large.

The remaining question is whether this ordinary G13 start is actually reachable after 1539 steps from the same current R1 start.

## 3. Exact reverse maps

Reverse the accelerated map from the G13 entrance.

A reverse edge corresponding to a forward even step is

\[
\boxed{E(x)=2x.}
\]

A reverse edge corresponding to a forward odd step is

\[
\boxed{O(x)=\frac{2x-1}{3},}
\]

which exists exactly when

\[
x\equiv2\pmod3.
\]

Suppose `r` reverse steps remain, of which exactly `k` are `E` edges and `m=r-k` are `O` edges.

Among all orders of those maps, the exact endpoint envelopes are

\[
\boxed{
E^kO^m(x)
=\frac{2^k3^m+2^r(x-1)}{3^m}
}
\]

and

\[
\boxed{
O^mE^k(x)
=\frac{3^m+2^m(2^kx-1)}{3^m}.
}
\]

They supply an exact branch-and-bound test against the present numerical R1 interval

\[
[N_0,N_{\max}].
\]

No floating-point comparison is needed.

## 4. Exact exclusion of the delta=1 candidate

Apply the root envelopes for every possible total forward-even count `E=0,...,30` over the 1539 pre-gate steps.

For the candidate above, exactly one total is numerically capable of reaching the R1 interval:

\[
\boxed{E=14.}
\]

All other totals are excluded at the root by the exact interval envelopes.

The complete reverse tree for `E=14`, with the modulo-3 condition enforced at every reverse odd edge, contains only

\[
\boxed{3131\text{ nodes}.}
\]

The number of leaves reaching the numerical interval is

\[
\boxed{0.}
\]

Therefore a fortiori the number of leaves in the current `m=44` Cantor core is also zero.

Hence this explicit ordinary G13 relation is rigorously incompatible with the same pre-gate R1 ordinary start:

\[
\boxed{\text{natural G13 }\delta=1\text{ candidate}\not\leftarrow\text{current R1 core}.}
\]

This is an exact candidate-specific theorem.

## 5. 124-candidate diagnostic

A beam search inside the `2^954` natural-cut section produced 124 ordinary G13 starts whose failure-time relation difference was positive and at most 397.

For each candidate, first apply the same exact root envelope over pre-gate even count.

Results:

- 72 candidates have no possible pre-gate even total at all;
- 39 candidates permit only `E=12`;
- 10 candidates permit only `E=13`;
- 3 candidates permit only `E=14`.

The 52 nontrivial sparse reverse trees contain, in total,

\[
\boxed{38,526\text{ nodes}.}
\]

The largest individual tree has 3131 nodes.

Across all 124 candidates the number of reverse leaves reaching even the numerical interval `[N_0,N_max]` is

\[
\boxed{0.}
\]

This aggregate is **not** an exhaustive section theorem because the 124 forward candidates were beam-generated.  Its role is diagnostic: every small-credit natural witness encountered so far is destroyed by the pre-gate same-word attachment before the ternary Cantor test is even needed.

## 6. Structural interpretation

The active obstruction is no longer

\[
\text{G13 internal relation existence}.
\]

That channel is flexible: exact `4096 -> 1` relations exist, and finite-natural ordinary starts can also create very small local credits.

The observed obstruction is instead

\[
\boxed{
\text{G13 finite-natural relation}
\cap
\text{1539-step reverse same-word preimage}
\cap
\text{current R1 start core}.
}
\]

The reverse envelope also explains why the sparse-even entrance theorem is high leverage.  Gate starts near the top of the current `2^954` window can only come from very sparse pre-gate parity histories, typically around `E=12,13,14`.  Those are precisely the next finite layers exposed by the first-73 sparse-even analysis.

## 7. Next exact target

The current global theorem already excludes pre-gate totals `E<=11`.

The next natural target is therefore to close, in order,

\[
\boxed{E=12,\quad E=13,\quad E=14}
\]

for the current R1 core, or to intersect those sparse pre-gate layers directly with the finite-natural G13 relation transducer.

For `E=12`, the run-cover theorem forces at most eight even positions in the first 73 bits.  Layers through seven zeros are already closed, so only the exact eight-zero layer remains.

This is substantially sharper than continuing an unrestricted 20026-bit G13 parity search.

## Reproducibility

Exact candidate-specific reverse verifier:

`collatz/src/g13_natural_cut_reverse_sameword_certificate.cpp`

The 124-candidate aggregate was produced by an exploratory finite beam and should remain classified as a diagnostic until its forward candidate generation is replaced by an exhaustive state construction.

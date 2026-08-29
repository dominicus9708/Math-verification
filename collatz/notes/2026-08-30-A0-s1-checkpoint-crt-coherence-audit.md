# A0 s=1 same-checkpoint CRT coherence audit — 2026-08-30

## Status

- **EXACT:** same-checkpoint 2-adic / 3-adic residues admit a unique CRT class.
- **EXACT:** the pre-checkpoint 3-adic endpoint residue is terminal-local after `M` odd events.
- **SAFE:** at the current `(K,M)=(27,28)`, every coherent boundary signature has at most one ordinary checkpoint `Z` in the current checkpoint corridor.
- **REJECTED:** Cartesian pairing of independently counted pre- and post-boundary marginals.
- **OPEN:** construct or enumerate the provenance-preserving paired boundary relation.
- **OPEN:** C4F renewal/gap conditions and the global Collatz conclusion.

Primary certificates:

- `collatz/src/A0_s1_checkpoint_crt_coherence_certificate.py`
- `collatz/src/A0_s1_terminal_ternary_residue_compression_certificate.py`

## 1. Affine correction identity

For a parity word `w` of length `n` and odd count `q(w)`, define `C(w)` by

\[
2^n T^n(X)=3^{q(w)}X+C(w).
\]

For concatenation `uv`,

\[
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
\]

This is the only composition law used below.

## 2. Pre-checkpoint ternary endpoint residue

Suppose a word `u` carries an ordinary start to the checkpoint `Z`:

\[
2^{|u|}Z=3^{q(u)}X+C(u).
\]

For `M<=q(u)`, reduction modulo `3^M` gives

\[
\boxed{
Z\equiv 2^{-|u|}C(u)\pmod{3^M}.
}
\]

Define

\[
R_M(w):=2^{-|w|}C(w)\pmod{3^M}.
\]

### Terminal locality

Let `u=ab`. From correction composition,

\[
R_M(ab)
=
2^{-|a|-|b|}3^{q(b)}C(a)
+
2^{-|b|}C(b)
\pmod{3^M}.
\]

If `q(b)>=M`, then the first term vanishes modulo `3^M`. Hence

\[
\boxed{
R_M(ab)=R_M(b)\pmod{3^M}
\qquad(q(b)\ge M).
}
\]

Therefore the checkpoint residue modulo `3^M` is determined by any terminal suffix ending at the same checkpoint that contains at least `M` odd events.

A canonical choice is the shortest suffix beginning at the `M`-th-last odd event. It contains exactly `M` odd bits.

For the current `M=28`, everything earlier than the 28th-last odd event is exactly irrelevant **for this residue only**.

## 3. Streaming ternary state

The normalized residue can be updated without materializing the large correction integer.

If the next parity bit is `0`,

\[
R'\equiv \frac{R}{2}\pmod{3^M}.
\]

If it is `1`,

\[
R'\equiv \frac{3R+1}{2}\pmod{3^M}.
\]

Starting from `R=0`, consuming a terminal word produces `R_M(w)` exactly.

This gives a finite modular left-boundary state of size `3^M`, but it is **not** by itself a complete language state: provenance and the terminal-word constraints must still be preserved.

## 4. Post-checkpoint dyadic address

For a post-checkpoint parity prefix `v` exposing at least `K` bits, the deterministic parity-address theorem gives

\[
\boxed{
Z\equiv A_K(v)\pmod{2^K}.
}
\]

The present boundary uses `K=27`.

## 5. Same-checkpoint paired signature

For a pre-checkpoint terminal suffix `b` and a post-checkpoint prefix `v` that are known to meet at the **same ordinary checkpoint** `Z`, define

\[
\boxed{
\Gamma_{K,M}(b\mid v)
=
\left(
A_K(v),
R_M(b)
\right).
}
\]

The two moduli are coprime, so CRT produces one class

\[
Z\equiv Z_\Gamma\pmod{2^K3^M}.
\]

This is an arithmetic theorem conditional only on the same-checkpoint provenance of the pair.

## 6. Current uniqueness window

Current exact values are

\[
2^{27}=134,217,728,
\]

\[
3^{28}=22,876,792,454,961,
\]

and

\[
\boxed{
2^{27}3^{28}
=3,070,471,107,232,407,748,608.
}
\]

The current checkpoint corridor is

\[
7,083,549,723,369,539,339,554
\le Z\le
9,444,732,965,739,290,427,391,
\]

with span

\[
\boxed{
2,361,183,242,369,751,087,837.
}
\]

Hence

\[
2^{27}3^{28}-(Z_{\max}-Z_{\min})
=
\boxed{
709,287,864,862,656,660,771
}>0.
\]

Therefore every coherent boundary signature has **at most one** ordinary lift in the current corridor:

\[
\boxed{
\Gamma_{27,28}\Longrightarrow \text{at most one ordinary }Z.
}
\]

It may still have no lift in the corridor.

## 7. Why this does not license marginal multiplication

The theorem does **not** say that every independently allowed pre-boundary residue may be paired with every independently allowed post-boundary address.

Doing so would destroy the only fact needed for CRT relevance: both values must refer to the same checkpoint on the same admissible boundary object.

Accordingly:

- a pre-boundary terminal word count is not automatically a count of distinct `Z mod 3^M` values;
- a post-boundary tail-word count is not automatically a count of distinct `Z mod 2^K` values;
- neither marginal count may be multiplied by the other without an explicit paired relation or a proved independence/product theorem.

This is especially important for the previously obtained `8,478,475` necessary tail-27 ballot words. Until an address-image theorem is proved for that collection, the value remains a **word count**, not a distinct-checkpoint count.

## 8. Interaction with the f=37 low-projection saturation

The `f=37` checkpoint sieve has no pruning power after projection to `Z mod 2^27` alone because its allowed interval is much wider than `2^27`.

That negative result does not contradict the present theorem. The paired signature uses the product modulus

\[
2^{27}3^{28},
\]

which is larger than the full checkpoint corridor and therefore restores ordinary-checkpoint uniqueness once coherence is known.

Thus the correct next target is not a finer marginal count. It is

\[
\boxed{
\text{marginal boundary information}
\longrightarrow
\text{provenance-preserving paired boundary relation}.
}
\]

## 9. Next exact construction target

A legal paired state must carry enough information to certify that its two sides refer to one boundary object. A minimal candidate interface is

\[
\mathcal B_{K,M}
=
(\Pi,\,A_K,\,R_M),
\]

where `Pi` is an explicit provenance / boundary-identity component, not merely a label discarded during merging.

Any merge is legal only if every future conclusion-relevant predicate is invariant under that merge. In particular, equality of `(A_K,R_M)` alone is insufficient to merge states if their admissible continuation or prehistory languages differ.

The next task is therefore to derive a provenance-preserving composition rule from the existing long correction / Christoffel-Stern-Brocot representation, rather than taking a Cartesian product of the existing marginals.

## 10. Audit conclusion

The arithmetic coherence gate itself is now closed:

\[
\boxed{
\text{same checkpoint}
\Rightarrow
(A_{27},R_{28})
\Rightarrow
\text{at most one ordinary }Z
}
\]

in the current corridor.

The remaining gate is structural, not CRT arithmetic:

\[
\boxed{
\text{prove which }(A_{27},R_{28})\text{ pairs are generated by one admissible long object.}
}
\]

No C4F or global Collatz conclusion follows from this certificate alone.

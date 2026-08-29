# A0 s=1 checkpoint CRT coherence and local-splice audit — 2026-08-30

## Status

- **EXACT:** same-checkpoint 2-adic / 3-adic residues admit a unique CRT class.
- **EXACT:** the pre-checkpoint 3-adic endpoint residue is terminal-local after `M` odd events.
- **EXACT:** if the left terminal suffix contains **exactly `M` odd events**, a positive CRT lift together with a `K`-bit right word constructs a genuine ordinary local orbit segment across the checkpoint.
- **SAFE:** at the current `(K,M)=(27,28)`, every locally compatible boundary signature has at most one ordinary checkpoint `Z` in the current checkpoint corridor.
- **SAFE:** positivity of the reconstructed left start is automatic in the current corridor for every exact-28-odd terminal suffix.
- **REJECTED:** treating an independently counted left/right Cartesian product as automatically satisfying the full long-language conditions.
- **OPEN:** construct or enumerate globally admissible left/right boundary states, preserving every nonlocal conclusion-relevant predicate.
- **OPEN:** C4F renewal/gap conditions and the global Collatz conclusion.

Primary certificates:

- `collatz/src/A0_s1_checkpoint_crt_coherence_certificate.py`
- `collatz/src/A0_s1_terminal_ternary_residue_compression_certificate.py`
- `collatz/src/A0_s1_checkpoint_local_splice_certificate.py`

## 1. Affine correction identity

For a parity word `w` of length `n` and odd count `q(w)`, define `C(w)` by

\[
2^n T^n(X)=3^{q(w)}X+C(w).
\]

For concatenation `uv`,

\[
\boxed{
C(uv)=3^{q(v)}C(u)+2^{|u|}C(v).
}
\]

This is the composition law used throughout the audit.

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

Let `u=ab`. Then

\[
R_M(ab)
=
2^{-|a|-|b|}3^{q(b)}C(a)
+
2^{-|b|}C(b)
\pmod{3^M}.
\]

If `q(b)>=M`, the first term vanishes modulo `3^M`, hence

\[
\boxed{
R_M(ab)=R_M(b)\pmod{3^M}
\qquad(q(b)\ge M).
}
\]

Therefore the checkpoint residue modulo `3^M` is determined by any terminal suffix ending at the same checkpoint that contains at least `M` odd events.

A canonical choice is the shortest suffix beginning at the `M`-th-last odd event. It contains **exactly `M` odd bits**.

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

This is an exact finite modular state for the endpoint residue, but not by itself a complete state for every long-language predicate.

## 4. Post-checkpoint dyadic address

For a post-checkpoint parity prefix `v` exposing at least `K` bits, the deterministic parity-address theorem gives

\[
\boxed{
Z\equiv A_K(v)\pmod{2^K}.
}
\]

The current boundary uses `K=27`.

## 5. CRT boundary signature

For a left terminal suffix `b` and a right prefix `v`, define

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

Because `2^K` and `3^M` are coprime, CRT produces one class

\[
Z\equiv Z_\Gamma\pmod{2^K3^M}.
\]

At this stage alone, `Gamma` is a modular compatibility signature. The next section shows that when the left suffix is the canonical **exact-M-odd** suffix, a positive CRT lift is stronger: it constructs a genuine local orbit splice.

## 6. Exact local-splice theorem

Let `b` have length `n` and exactly `M` odd bits:

\[
q(b)=M.
\]

Let `v` expose `K` right-hand parity bits. Suppose an ordinary positive integer `Z` satisfies

\[
Z\equiv R_M(b)\pmod{3^M},
\]

and

\[
Z\equiv A_K(v)\pmod{2^K}.
\]

Define

\[
\boxed{
Y:=\frac{2^nZ-C(b)}{3^M}.
}
\]

The ternary congruence makes the numerator divisible by `3^M`, so `Y` is an integer.

Moreover,

\[
3^M Y\equiv -C(b)\pmod{2^n}.
\]

Since `3^M` is invertible modulo `2^n`,

\[
\boxed{
Y\equiv -3^{-M}C(b)=A_n(b)\pmod{2^n}.
}
\]

By the deterministic parity-address theorem, the actual first `n` parity bits of `Y` are exactly `b`. The defining affine equation then gives

\[
\boxed{T^n(Y)=Z.}
\]

Likewise `Z mod 2^K=A_K(v)` forces the actual first `K` future parity bits of `Z` to equal `v`.

Therefore

\[
\boxed{
\text{exact-M left suffix}
+
\text{K-bit right word}
+
\text{positive CRT lift}
\Longrightarrow
\text{genuine local ordinary orbit segment }b\mid v.
}
\]

This removes the need for an additional opaque provenance label **for local checkpoint continuity**.

### Why `q(b)=M` is essential here

If `q(b)>M`, the congruence modulo `3^M` proves divisibility only by `3^M`, not by the full `3^{q(b)}` required by the affine endpoint equation. Therefore the local-splice theorem intentionally uses the canonical suffix with exactly `M` odd events.

The certificate includes a counter-regression showing that replacing `q(b)=M` by merely `q(b)>=M` would be unsound for this reconstruction step.

## 7. Current positivity is automatic

For every binary word `b` of length `n` with exactly `M` odd bits,

\[
C(b)
<
2^n\sum_{j=0}^{M-1}3^j
=
2^n\frac{3^M-1}{2}.
\]

For `M=28`,

\[
\frac{3^{28}-1}{2}
=
\boxed{11,438,396,227,480}.
\]

The checkpoint corridor begins at

\[
Z_{\min}
=
7,083,549,723,369,539,339,554,
\]

so

\[
Z_{\min}>\frac{3^{28}-1}{2}.
\]

Hence for every canonical exact-28-odd suffix and every checkpoint lift in the current corridor,

\[
2^nZ>C(b),
\]

and therefore

\[
\boxed{Y>0}
\]

automatically.

## 8. Current CRT uniqueness window

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

Therefore a specific exact-28-odd left suffix and 27-bit right word have **at most one** local checkpoint splice in the current corridor.

They may still have no lift in the corridor.

## 9. What Cartesian pairing now means

The earlier warning against arbitrary Cartesian pairing needs a precise refinement.

### Locally

For a **specific** exact-28-odd left word `b` and a **specific** 27-bit right word `v`, it is legitimate to:

1. compute `R_28(b)`;
2. compute `A_27(v)`;
3. CRT-combine them;
4. test whether the unique class has a lift in the checkpoint corridor;
5. if it does, reconstruct `Y`.

A successful test certifies a genuine ordinary local orbit segment `b|v`.

Thus local same-checkpoint continuity no longer requires an external provenance object.

### Globally

It remains **invalid** to interpret every locally splicable pair as a survivor of the full Route-B language.

A left terminal word may fail to admit a legal long prehistory with the required accumulated rank, ballot, defect, correction, or shell constraints. A right word may fail the required long continuation. Cross-boundary aggregate predicates may also depend on state not contained in `(A_27,R_28)`.

Therefore an independently counted marginal product is still not a valid count of globally admissible long objects unless the missing nonlocal predicates are proved invariant or carried explicitly.

In particular:

- a pre-boundary terminal-word count is not automatically a count of distinct `Z mod 3^28` values;
- a post-boundary tail-word count is not automatically a count of distinct `Z mod 2^27` values;
- the previously obtained `8,478,475` necessary tail-27 ballot words remain a **word count** until their exact boundary orientation and address-image relation are verified from the generating certificate.

## 10. Interaction with f=37 low-projection saturation

The `f=37` checkpoint sieve has no pruning power after projection to `Z mod 2^27` alone because its allowed interval is wider than `2^27`.

The local-splice signature instead uses the product modulus

\[
2^{27}3^{28},
\]

which is larger than the whole checkpoint corridor. Therefore once a concrete left/right pair is available, CRT recovers zero or one ordinary checkpoint and the exact late-shell reducer can then be applied to that ordinary `Z`.

## 11. Correct remaining structural gate

The local arithmetic gate is now closed:

\[
\boxed{
(b_{q=28},v_{27})
\xrightarrow{\ CRT\ }
Z
\xrightarrow{\ exact\ reconstruction\ }
Y\to Z\to\text{right future}
}
\]

whenever the unique CRT class hits the corridor.

The remaining gate is **not** “prove that two modular residues refer to the same local orbit.” That part is reconstructible.

The remaining gate is:

\[
\boxed{
\text{which locally splicable }(b,v)
\text{ also possess the required long left/right extensions and cross-boundary states?}
}
\]

A legal compressed boundary state therefore needs only the nonlocal information not recoverable from the local splice. Schematically,

\[
\mathcal B
=
(\Sigma_{\mathrm{nonlocal}},\,b_{q=28},\,v_{27}),
\]

or a compressed equivalent in which every future conclusion-relevant predicate is invariant under state merging.

## 12. Audit conclusion

Three layers are now separated cleanly:

1. **Local ordinary-orbit continuity:** **CLOSED / EXACT** for an exact-28-odd left suffix and a 27-bit right word whose CRT class hits the current corridor.
2. **Long-language left/right compatibility:** **OPEN.** This is now the main Route-B boundary gate.
3. **C4F / global Collatz conclusion:** **OPEN.** No implication is claimed from the local certificates alone.

The immediate next task is to identify the exact generating objects behind the existing `8,478,475` tail-27 word count and the compatible left terminal-language representation, then apply the local CRT-splice filter without discarding the nonlocal state needed by Route B.

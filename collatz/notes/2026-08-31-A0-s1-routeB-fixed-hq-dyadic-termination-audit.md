# A0 s=1 Route-B fixed-(h,q) dyadic termination audit

Date: 2026-08-31
Branch: `collatz-stage4-window-threshold`
Status: universal finite-block adaptive identification termination closed; target-aware long-language membership remains open.

## 1. Statement

For a parity block `w` of length `h`, one-count `q`, and Collatz correction `C(w)`, write

\[
T^h(X)=\frac{3^qX+C(w)}{2^h}.
\]

The canonical source residue is

\[
r(w)\equiv -C(w)(3^q)^{-1}\pmod{2^h},\qquad 0\le r(w)<2^h.
\]

The exact prefix-channel transducer already establishes a bijection between length-`h` parity prefixes and the `2^h` canonical residues modulo `2^h`.

The new theorem is:

> If distinct blocks `u != v` have the same length `h` and the same one-count `q`, then
> \[
> v_2(C(u)-C(v))\le h-2.
> \]
> Consequently the first dyadic correction resolution that distinguishes them satisfies
> \[
> K_*=v_2(C(u)-C(v))+1\le h-1.
> \]

There are no distinct same-`q` pairs at `h=1`, so the nontrivial statement begins at `h=2`.

## 2. Proof

Assume for contradiction that

\[
2^{h-1}\mid C(u)-C(v).
\]

Because `u` and `v` have the same `q`, multiplication by the same odd unit `(3^q)^{-1}` gives

\[
r(u)\equiv r(v)\pmod{2^{h-1}}.
\]

By the prefix-channel bijection, this means the first `h-1` parity symbols of `u` and `v` are identical.

Their total one-counts are also identical. Therefore their final parity symbols must be identical as well. Hence `u=v`, contradicting the hypothesis.

Thus

\[
2^{h-1}\nmid C(u)-C(v),
\]

so

\[
v_2(C(u)-C(v))\le h-2.
\]

This proves finite termination of dyadic refinement for every finite block once `(h,q)` is fixed.

## 3. Exhaustive regression

Certificate:

`collatz/src/A0_s1_routeB_fixed_hq_dyadic_termination_certificate.py`

Regression through `h=12` verifies:

- prefix-to-residue bijection at every depth;
- fixed-`(h,q)` injectivity of `C`;
- the valuation bound for every same-`q` pair;
- sharpness of `K_* <= h-1` for every audited `h=2..12`.

Counts:

- prefix bijection checks: `8190`
- fixed-`(h,q)` pair checks: `1826175`
- `h=12` same-`q` pair checks: `1350030`

At `h=12`, the first distinguishing dyadic resolution distribution is:

| `K_*` | pair count |
|---:|---:|
| 1 | 646646 |
| 2 | 335920 |
| 3 | 175032 |
| 4 | 91520 |
| 5 | 48048 |
| 6 | 25344 |
| 7 | 13440 |
| 8 | 7168 |
| 9 | 3840 |
| 10 | 2048 |
| 11 | 1024 |

The occurrence of `K_*=h-1=11` shows that the theorem's bound cannot be uniformly reduced using only the fixed-`(h,q)` argument.

## 4. Consequence for adaptive G4 decoding

The previous adaptive bridge+ballot audit was finite-domain evidence that collision classes can be split by increasing `K` or `L` only when needed.

This theorem supplies the missing termination guarantee for finite blocks:

\[
\boxed{\text{fixed }(h,q)\text{ finite block} \Longrightarrow \text{dyadic identification terminates by }K\le h-1.}
\]

Ternary refinement may still be cheaper for a particular collision class, and the ballot summary may separate it without any resolution increase. However, neither is required for termination: dyadic refinement is an exact fallback.

This does **not** give an `h`-independent finite-state quotient. The required resolution may grow linearly with block length, consistent with the earlier Christoffel hierarchy result where very large blocks required very large dyadic distinguishing depth.

## 5. Formation Axiom System audit

The proof uses the already-defined prefix-channel formation rule: each parity extension exposes exactly one additional dyadic residue digit. No undefined coordinate or hidden expanded-word assumption is introduced.

The fixed total one-count `q` closes the last-symbol ambiguity once the first `h-1` symbols have been formed.

## 6. Axis Property audit

`K` remains an external resolution axis rather than an intrinsic block coordinate. The theorem supplies a block-relative stopping bound `K<=h-1`; it does not promote a fixed global resolution to an intrinsic property.

This reinforces the earlier rejection of a globally fixed low-resolution state and supports adaptive/hierarchical evaluation instead.

## 7. DSD cross-audit

Closed:

- universal finite-block identification termination for fixed `(h,q)`;
- exact dyadic stopping bound `K_*<=h-1`;
- finite regression and sharpness audit through `h=12`.

Still open:

- target-aware recognition of the remaining Route-B correction language;
- proving that every long admissible survivor reaches/rejects the unique correction target;
- first-passage/renewal/same-orbit integration where those predicates are required;
- G5 universal Route-B membership;
- global Collatz integration.

## 8. Next obligation

Attach the now-terminating adaptive identification mechanism to the actual long-membership/first-defect representation. The decoder must carry enough target-relative data to decide admissibility, not merely distinguish two finite blocks.

The desired next step is to identify the current Route-B target/correction state and prove exact block-level update/rejection rules for

\[
(\text{channel},K,L,S_{K,L},m,a,\text{target locator},\text{defect data}).
\]

Only unresolved target-relative blocks should descend recursively.

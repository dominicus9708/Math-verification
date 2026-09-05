# Source-activation / checkpoint provenance join

## Scope

This theorem isolates the exact missing source-to-checkpoint provenance gate in
`A0, s=1, Route-B`.

It does **not** enumerate the long terminal suffix and does **not** claim that
an arbitrary left marginal and right marginal belong to one orbit.  Instead it
states the exact criterion which, once one source-derived activation record and
one synchronized boundary record are supplied, proves that they splice on the
same ordinary Collatz orbit.

## 1. Exact source activation channel

Let an exact source-preserving channel at the late activation cut be

\[
X=r+2^h k,\qquad T^h(X)=y+3^q k,\qquad k\in[k_{lo},k_{hi}].
\]

For the current terminal seam,

\[
q=j_0-28.
\]

In the canonical S10 representation, `q` is derived from

\[
q=Q(h)+S,
\]

so it is not an additional persistent coordinate.

## 2. Exact terminal suffix descriptor

Let `B` be a valid binary parity word with

\[
|B|=n,\qquad q(B)=M=28,
\]

and correction

\[
C_B=C(B).
\]

The local affine identity is

\[
2^n Z=3^{28}Y+C_B.
\]

For fixed `(n,28)`, the correction language is injective, so an already
validated pair `(n,C_B)` determines the exact terminal parity word.  Raw
storage of all bits is therefore not mathematically necessary at this
interface.

Define the reconstructed start of the terminal suffix by

\[
\boxed{
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}}.
}
\]

The terminal residue condition

\[
Z\equiv 2^{-n}C_B\pmod{3^{28}}
\]

is exactly the integrality condition for `Y_B(Z)`.

## 3. Source-fiber provenance criterion

A synchronized checkpoint candidate `Z` belongs to the **same ordinary orbit**
as the source activation channel through terminal suffix `B` if and only if

\[
\boxed{
Y_B(Z)-y\equiv0\pmod{3^q}
}
\]

and

\[
\boxed{
k_*:=\frac{Y_B(Z)-y}{3^q}\in[k_{lo},k_{hi}].}
\]

When these conditions hold, set

\[
X_*=r+2^h k_*.
\]

Then the source-channel identity gives

\[
T^h(X_*)=Y_B(Z),
\]

and the validated terminal suffix gives

\[
T^n(Y_B(Z))=Z.
\]

Therefore

\[
\boxed{T^{h+n}(X_*)=Z.}
\]

Because the activation endpoint is affine with nonzero slope `3^q`, there is
at most one source parameter `k_*` for the fixed tuple `(source channel,B,Z)`.

## 4. Post-checkpoint continuation

Let a 27-bit post-checkpoint prefix `V` have address

\[
z_2=A_{27}(V).
\]

If the synchronized right-H observation `z_H` and `z_2` lift to the ordinary
checkpoint `Z` in the certified corridor, then

\[
Z\equiv z_2\pmod{2^{27}}
\]

forces the actual ordinary orbit of `Z` to begin with `V`.

Thus the conjunction

1. exact source activation channel,
2. validated 28-one terminal suffix `(n,C_B)`,
3. synchronized `(z_2,z_H)` with corridor lift `Z`,
4. terminal-residue equality for `(n,C_B,Z)`, and
5. the source-fiber criterion above,

proves a genuine local source-to-checkpoint-to-post-checkpoint ordinary orbit
splice.  No marginal-density multiplication or independence assumption is
used.

## 5. What the existing certificates already close

Existing exact certificates provide the following pieces separately:

- terminal 28-one suffix locality exposes `Z mod 3^28`;
- terminal residue transfers affinely to the critical right-H carry;
- `(z_2,z_H)` has at most one ordinary checkpoint lift in the SAFE corridor;
- exact-M local splice proves ordinary-orbit provenance once the actual suffix
  and post-prefix are paired at one `Z`;
- an exposed `Z` gives deterministic source-fiber cardinality bounds through
  the debit corridor.

The last item is only a necessary source-fiber localization.  The debit
relation `L_-=3X-Z` does not by itself prove that `X` reaches `Z` under the
Collatz map.

## 6. Current export-interface gap

The current canonical jump-8 source export does **not yet** emit a paired late
activation record of the form

```text
source_parent_id
(r,y,k_lo,k_hi,h,S) at q=j0-28
(n,C_B) with exact 28-one suffix validity/provenance
z2 with post-checkpoint provenance
zH with right-H provenance
```

Consequently the source-fiber congruence/inclusion test in Section 3 cannot yet
be run on the 14,224 current source parents without reconstructing the missing
long source-to-activation relation.

This is the precise remaining interface, rather than CRT arithmetic itself.

## DSD audit

- **EXACT/CLOSED**: source activation fiber + validated terminal suffix + one
  checkpoint `Z` gives the criterion above.
- **EXACT/CLOSED**: a successful criterion yields a genuine same-orbit splice,
  not merely residue compatibility.
- **EXACT/CLOSED**: at most one source parameter belongs to a fixed
  `(activation channel,B,Z)` tuple.
- **SAFE**: `(n,C_B)` may replace raw `B` only when fixed-`(n,28)` correction
  language validity/injectivity has been discharged.
- **REJECTED**: treating the debit-corridor source-fiber cap as same-orbit
  provenance.
- **REJECTED**: Cartesian pairing of independently generated `z_2` and `z_H`
  marginals.
- **OPEN**: construction/export of the actual paired late-activation records
  from the current source families and right-H language.
- **OPEN**: Route-B and global Collatz closure.

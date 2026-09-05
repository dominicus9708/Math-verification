# S10 source-activation / checkpoint provenance join audit

## Question

Does the existing synchronized checkpoint arithmetic already prove that one of
the current source families reaches the CRT checkpoint on the same ordinary
Collatz orbit?

**No.**  It closes the checkpoint and local-splice arithmetic, but the current
exports do not yet carry the paired late-activation source provenance required
to apply that splice to the 14,224 source families.

## Exact chain now closed

Suppose the caller supplies an exact late activation channel

\[
X=r+2^h k,\qquad T^h(X)=y+3^qk,\qquad k\in[k_{lo},k_{hi}],
\]

with `q=j0-28`, a validated exact 28-one terminal suffix descriptor `(n,C_B)`,
and a synchronized checkpoint candidate `Z`.

Set

\[
Y_B(Z)=\frac{2^nZ-C_B}{3^{28}}.
\]

Then the source provenance gate is exactly

\[
Y_B(Z)-y\equiv0\pmod{3^q},
\]

followed by

\[
k_*=(Y_B(Z)-y)/3^q\in[k_{lo},k_{hi}].
\]

If it passes, the unique source value

\[
X_*=r+2^hk_*
\]

satisfies

\[
T^{h+n}(X_*)=Z.
\]

Together with the exact 27-bit post-checkpoint address, this is genuine local
same-orbit provenance rather than CRT compatibility only.

## Existing modules and what they do not supply

### CLOSED

- `A0_s1_checkpoint_late_activation_certificate.py`
  - proves terminal 28-one ternary locality and late 27-bit dyadic activation;
- `A0_s1_routeB_terminal_residue_rightH_transfer_certificate.py`
  - gives the exact affine transfer between `Z mod 3^28` and right-H carry;
- `A0_s1_routeB_synchronized_checkpoint_CRT_singleton_certificate.py`
  - gives at most one ordinary checkpoint `Z` in the SAFE corridor;
- `A0_s1_checkpoint_local_splice_certificate.py`
  - proves exact-M terminal suffix + post-prefix + one `Z` is a genuine local
    ordinary orbit splice;
- `A0_s1_routeB_synchronized_checkpoint_source_fiber_certificate.py`
  - gives deterministic source-parameter cardinality bounds once `Z` is known.

### Not sufficient for same-orbit provenance

The debit-corridor source-fiber certificate uses

\[
L_-=3X-Z
\]

only to localize source parameters.  That relation is a necessary corridor
constraint; it does not prove `T^t(X)=Z`.

Likewise, `BoundarySignature` in the CRT-coherence certificate explicitly
requires callers to preserve same-checkpoint provenance.  The data structure
cannot create that provenance from separately generated marginals.

## Minimal paired export contract

The proof kernel can consume the following logical record:

```text
source_parent_id
activation channel (r,y,k_lo,k_hi,h,S) with q=Q(h)+S=j0-28
terminal suffix descriptor (n,C_B) + exact fixed-(n,28) validity witness
post-checkpoint dyadic address z2 + provenance
right-H carry zH + provenance
```

`q` is derived and should not become a redundant persistent S10 coordinate.
Raw terminal bits are not required if fixed-`(n,28)` correction-language
validity/injectivity is certified.

## DSD tuple

### D — domain

Exact positive ordinary accelerated-Collatz states, one current Route-B source
family, the late `q_rem=28` activation seam, and the 27-bit post-checkpoint
prefix.

**Status: CLOSED.**

### R — resolution

- left: exact 28-one terminal correction descriptor;
- checkpoint: `2^27 x 3^28` synchronized exposure plus ordinary corridor lift;
- source: exact activation affine fiber.

**Status: CLOSED for the join kernel; export construction OPEN.**

### S — state sufficiency

The proposed paired record is sufficient for the local source-to-checkpoint
same-orbit decision.

Current jump-8 export does not contain that late activation record.

**Status: kernel CLOSED / current exporter INSUFFICIENT.**

### E — equivalence

CRT residue compatibility is not equivalent to same-orbit provenance.  The
activation-fiber equality is the missing equivalence test.

**Status: CLOSED distinction.**

### T — transition

A successful activation-fiber test followed by the terminal suffix produces
`Z` exactly, and the 27-bit address fixes the actual post-checkpoint prefix.

**Status: CLOSED.**

### C — closure

No Route-B family is closed merely by this theorem.  Actual paired activation
records still have to be generated or ruled out.

**Status: OPEN.**

### N — non-independence

- do not Cartesian-product unrelated `z2` and `zH` marginals;
- do not multiply their marginal densities;
- do not treat the debit source-fiber cap as orbit realization.

**Status: CLOSED audit rule.**

### O — outstanding

Construct a source-preserving late-activation exporter which reaches
`q=j0-28` without expanding the raw ~10^11-bit middle word, and emits the
validated `(n,C_B)` terminal descriptor with source provenance.  Pair it with
the right-H/post-checkpoint record and run the exact join kernel.

## Classification

- **EXACT/CLOSED**: source-activation membership criterion.
- **EXACT/CLOSED**: successful criterion implies a genuine ordinary same-orbit
  splice to the checkpoint.
- **EXACT/CLOSED**: uniqueness of the source parameter for a fixed
  `(activation channel,B,Z)` record.
- **REJECTED**: CRT compatibility => source realization.
- **REJECTED**: debit corridor localization => source realization.
- **OPEN**: compressed construction of the paired late-activation relation on
  the 14,224 current source families.
- **OPEN**: A0,s=1,Route-B closure.

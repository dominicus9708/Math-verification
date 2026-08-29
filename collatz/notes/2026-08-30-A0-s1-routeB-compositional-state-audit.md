# A0 s=1 Route-B compositional-state audit — 2026-08-30

## Result

The exact prefix-channel state `(h,r,y,q)` admits the correction-coordinate reduction

`C = 2^h y - 3^q r`.

Because `3^q` is invertible modulo `2^h`, `(h,q,C)` reconstructs the full channel:

- `r = -C (3^q)^(-1) mod 2^h`,
- `y = (3^q r + C)/2^h`.

Therefore `r` and `y` are redundant coordinates once `(h,q,C)` is known.

For adjacent parity blocks `u,v`, the exact composition law is

`C(uv) = 3^{q(v)} C(u) + 2^{h(u)} C(v)`.

This is the integer form of the normalized Christoffel-DAG correction composition already used upstream.

## Exhaustive audit

`collatz/src/A0_s1_routeB_correction_state_certificate.py` checks:

- all 32,767 binary prefixes through depth 14 against the exact `(h,r,y,q)` transducer;
- 98,305 split/composition identities through total depth 12;
- 18,943 three-block associativity checks.

All checks pass.

Explicit irredundancy witnesses were also found:

- dropping `C`: words `10` and `01` have equal `(h,q)=(2,1)` but different channels;
- dropping `q`: words `11100` and `10001` have equal `(h,C)=(5,19)` but reconstruct different channels;
- dropping `h` without supplying block length externally: words `1` and `10` have equal `(q,C)=(1,1)` but compose differently with the next nonzero block.

## Pure-ballot phase audit

For a local block `B` placed after absolute threshold position `h`, define

`mu_h(B) = min_{0<=u<=|B|} [Q_B(u) - (REQ[h+u]-REQ[h])]`.

If the entering prefix has slack `s=q-REQ[h] >= 0`, then pure-ballot legality through the whole block is exactly

`s + mu_h(B) >= 0`.

For adjacent blocks `U,V`,

`mu_h(UV) = min(mu_h(U), k(U)-(REQ[h+|U|]-REQ[h]) + mu_{h+|U|}(V))`.

A local exhaustive audit checked 221,208 block compositions and 122,760 legality comparisons with no failure.

The ballot state is necessarily phase-sensitive. The same one-bit block `0` has margin `-1` at `h=0`, where the threshold next bit is `1`, but margin `0` at `h=2`, where the threshold next bit is `0`. Thus a phase-free local state is unsound. A correct long decoder must carry absolute threshold phase `h`, or an exact equivalent location in the Christoffel/mechanical-word decomposition.

## DSD audit status

- ✅ Exact correction-coordinate reduction: closed.
- ✅ Exact two-block correction composition: closed.
- ✅ Exact phase-sensitive ballot-margin composition: closed algebraically and finitely regression-tested.
- ✅ Hidden-state audit: phase-free ballot state rejected by explicit witness.
- ❌ Finite quotient of the full correction language: not established.
- ❌ Unique-target long correction-language membership: still open.
- ❌ Collatz conjecture: not proved.

## Next gate

The next main-line task is no longer to increase the local Hamming radius. It is to attach the pair of exact summaries

`(h,q,C)` and `mu_h`

to the existing 129-node Christoffel/Stern-Brocot DAG, so that gigantic threshold/correction blocks can be jumped compositionally without materializing their bits. The remaining question is whether the unique target's required path is reachable under those exact jump states and the existing SAFE pruning inequalities.

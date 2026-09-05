#!/usr/bin/env python3
"""Exact channel/block parameter partition for A0 s=1 Route-B.

For a parent parity-prefix channel

    X = r + 2^h m,
    T^h(X) = y + 3^q m,

and a candidate block B of fixed length ell, the exact block-jump primitive
selects one parameter residue

    m == m_B (mod 2^ell).

This certificate proves computationally, over an exhaustive audit domain, the
stronger decoder property suggested by the exact cylinder theory:

For every fixed parent channel and block length ell, the map

    B  ->  m_B mod 2^ell

from all 2^ell parity blocks to all 2^ell parameter residues is a permutation.
Thus the complete set of length-ell blocks partitions the parent parameter
axis exactly, with no overlap and no gap.  Restricting the admissible block set
therefore removes exactly the corresponding parameter residue classes.

The theorem itself follows from parity-cylinder uniqueness: every length-ell
parity word has one canonical source residue rho_B mod 2^ell, these residues
are all distinct, and the parent map

    rho_B -> (rho_B-y)*(3^q)^(-1) mod 2^ell

is an affine bijection because 3^q is odd.

Scope:
  * exact block-to-parameter partition primitive: CLOSED;
  * this does not decide which blocks are Route-B admissible;
  * universal correction-language membership remains OPEN.
"""

PARENT_MAX_DEPTH = 5
BLOCK_MAX_LENGTH = 8


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def refine_channel(state, bit: int):
    h, r, y, q = state
    assert bit in (0, 1)
    m0 = (bit - (y & 1)) & 1
    r2 = r + (m0 << h)

    if bit == 0:
        numer = y + (3 ** q) * m0
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q
    else:
        numer = 3 * y + (3 ** (q + 1)) * m0 + 1
        assert numer % 2 == 0
        y2 = numer // 2
        q2 = q + 1

    return h + 1, r2, y2, q2


def channel_state(bits):
    state = (0, 0, 0, 0)
    for bit in bits:
        state = refine_channel(state, bit)
    return state


def block_state(bits):
    ell = qB = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << ell)
            qB += 1
        ell += 1
    return ell, qB, C


def block_residue(block):
    ell, qB, C = block
    modulus = 1 << ell
    return (-C * pow(pow(3, qB, modulus), -1, modulus)) % modulus


def jump_channel(parent, block):
    h, r, y, q = parent
    ell, qB, C = block
    modulus = 1 << ell

    rho = block_residue(block)
    mB = ((rho - y) * pow(pow(3, q, modulus), -1, modulus)) % modulus

    r2 = r + (mB << h)
    numer = (3 ** qB) * (y + (3 ** q) * mB) + C
    assert numer % modulus == 0
    y2 = numer // modulus

    return (h + ell, r2, y2, q + qB), mB


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def parameter_pullback(L: int, U: int, mB: int, ell: int):
    assert L <= U
    step = 1 << ell
    lo = ceil_div(L - mB, step)
    hi = (U - mB) // step
    return None if lo > hi else (lo, hi)


parents = []
for h in range(PARENT_MAX_DEPTH + 1):
    for address in range(1 << h):
        bits = tuple((address >> i) & 1 for i in range(h))
        parents.append((bits, channel_state(bits)))

assert len(parents) == 63

permutation_checks = 0
block_jump_checks = 0
endpoint_lift_checks = 0
interval_partition_checks = 0

for parent_bits, parent in parents:
    for ell in range(1, BLOCK_MAX_LENGTH + 1):
        residues = []
        block_rows = []

        for address in range(1 << ell):
            bits = tuple((address >> i) & 1 for i in range(ell))
            block = block_state(bits)
            jumped, mB = jump_channel(parent, block)

            assert jumped == channel_state(parent_bits + bits)
            block_jump_checks += 1

            residues.append(mB)
            block_rows.append((bits, mB, jumped))

            # Check several lifted members of the child arithmetic channel.
            h2, r2, y2, q2 = jumped
            for n in (0, 1, 3):
                X = r2 + (1 << h2) * n
                z = X
                got_bits = []
                for _ in range(h2):
                    got_bits.append(z & 1)
                    z = T(z)
                assert tuple(got_bits) == parent_bits + bits
                assert z == y2 + (3 ** q2) * n
                endpoint_lift_checks += 1

        # Strong partition statement: every parameter residue occurs once.
        assert sorted(residues) == list(range(1 << ell))
        permutation_checks += 1

        # Exact finite-interval partition: union over all block pullbacks is
        # exactly every integer parent parameter once.
        for L, U in ((0, 0), (0, 5), (3, 17), (10, 41), (-7, 23)):
            labeled_parameters = []
            for bits, mB, _jumped in block_rows:
                child_interval = parameter_pullback(L, U, mB, ell)
                if child_interval is None:
                    continue
                n_lo, n_hi = child_interval
                for n in range(n_lo, n_hi + 1):
                    m = mB + (1 << ell) * n
                    assert L <= m <= U
                    labeled_parameters.append((m, bits))

            values = [m for m, _bits in labeled_parameters]
            assert sorted(values) == list(range(L, U + 1))
            assert len(values) == len(set(values))
            interval_partition_checks += 1


assert permutation_checks == 504
assert block_jump_checks == 32_130
assert endpoint_lift_checks == 96_390
assert interval_partition_checks == 2_520

print("PASS A0 s=1 Route-B exact channel/block parameter partition certificate")
print("parent_max_depth", PARENT_MAX_DEPTH)
print("parent_channels", len(parents))
print("block_max_length", BLOCK_MAX_LENGTH)
print("permutation_checks", permutation_checks)
print("block_jump_checks", block_jump_checks)
print("endpoint_lift_checks", endpoint_lift_checks)
print("interval_partition_checks", interval_partition_checks)
print(
    "formation_audit",
    "each candidate block forms exactly one child parameter residue class; the complete block family forms an exact partition",
)
print(
    "axis_audit",
    "block choice and parent parameter residue are equivalent coordinates at resolution ell; no duplicate child coordinate exists",
)
print(
    "dsd_audit",
    "full block family has neither overlap nor omission on the parent parameter axis; admissibility pruning can therefore be transferred exactly to residue-class pruning",
)
print(
    "status",
    "G4 exact block-to-parameter partition CLOSED; admissible-block language decoder remains OPEN",
)

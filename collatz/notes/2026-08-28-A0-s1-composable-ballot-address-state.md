# A0 s=1: composable ballot-address block state

Date: 2026-08-28

Status: **SAFE for pure ballot + 2-adic address / C4F OPEN.**

The radius-five finite closure shows that raw Hamming-shell expansion is useful but scales poorly.  The next step is therefore to summarize a candidate block relative to the Christoffel threshold skeleton by quantities that compose exactly.

## 1. Block summary

Let `b` be a reference block and `w` a candidate block of the same length `n`.

Define

\[
\Delta q=q(w)-q(b),
\]

\[
S_{\min}
=
\min_{0\le k\le n}
\left(Q_w(k)-Q_b(k)\right),
\]

\[
D=d_H(w,b),
\]

and for an address precision `K`,

\[
A_K(w)
=
-\sum_{r=1}^{q(w)}3^{-r}2^{a_r}
\pmod{2^K}.
\]

Keep the state

\[
\boxed{
\Sigma_K(w\mid b)
=
(n,q,\Delta q,S_{\min},D,A_K).
}
\]

## 2. Exact concatenation law

For

\[
(b,w)=(b_1b_2,w_1w_2),
\]

write the two block states as `Sigma_1`, `Sigma_2`.

Then

\[
n=n_1+n_2,
\qquad
q=q_1+q_2,
\]

\[
\Delta q=\Delta q_1+\Delta q_2,
\]

\[
\boxed{
S_{\min}
=
\min\left(
S_{\min,1},
\Delta q_1+S_{\min,2}
\right),
}
\]

and

\[
D=D_1+D_2.
\]

The 2-adic address obeys

\[
\boxed{
A_K(w_1w_2)
=
A_K(w_1)
+2^{n_1}3^{-q_1}A_K(w_2)
\pmod{2^K}.
}
\]

Thus all six coordinates compose without expanding the internal parity word.

## 3. Ballot criterion with incoming surplus

Suppose a preceding block leaves ballot surplus `S>=0` relative to the same reference skeleton.

The entire candidate block is valid iff

\[
\boxed{
S+S_{\min}\ge0.
}
\]

If valid, the outgoing surplus is

\[
\boxed{
S'=S+\Delta q.
}
\]

This means `S_min` is the exact information needed from the internal block for pure-ballot viability; individual internal prefix values need not be retained after the summary is certified.

## 4. Address closure at 72 bits

For the current physical shell, choose

\[
K=72.
\]

Once the accumulated prefix length is at least 72, a candidate address in

\[
0<X<2^{72}
\]

has no additional Hensel lift freedom.

In the concatenation law, once `n_1>=72`,

\[
2^{n_1}\equiv0\pmod{2^{72}},
\]

so later blocks no longer alter the original physical address modulo `2^72`:

\[
\boxed{
A_{72}(w_1w_2)=A_{72}(w_1)
\quad(n_1\ge72).
}
\]

This formally separates two tasks:

- the first 72 positions identify the physical start address;
- later blocks test whether the deterministic continuation remains inside the admissible ballot/formation corridor.

## 5. Relation to the Christoffel DAG

Each Christoffel DAG node already stores exact reference length and odd count.

The new state can be attached to a deviation alternative at the node.  Child states combine using the formulas above, so a parent does not need the expanded child words.

For pure ballot and physical-address propagation, two states may be merged only when the retained coordinates are identical and the same incoming-surplus regime is used.

This provides a rigorous route from

\[
\text{raw deviation words}
\]

to

\[
\boxed{
\text{node-composable certified summaries}.
}
\]

## 6. DSD audit

### SAFE

- `Delta q` addition under concatenation;
- the `S_min` min-plus composition law;
- Hamming-defect addition;
- the 2-adic address concatenation law;
- incoming-surplus ballot test `S+S_min>=0`;
- outgoing surplus `S+Delta q`;
- after a 72-position prefix, later blocks cannot alter `A mod 2^72`.

The companion certificate exhaustively checks all pairs of reference/candidate blocks of lengths up to four on both sides of a cut and verifies multiple cut positions of the target 75-bit threshold word.

### NOT PROMOTED

This state is **not** yet declared sufficient for `C4F`.

A merge based only on

\[
(n,q,\Delta q,S_{\min},D,A_{72})
\]

is legal only for conclusions depending on pure ballot and the 72-bit parity address.  If `C4F` distinguishes two histories sharing these coordinates, additional formation-state coordinates must be added before those histories may merge.

### NEXT GATE

The next task is to identify the minimal `C4F` memory and append it to this compositional state.  Only after that audit should the 129-node Christoffel DAG be used for aggressive long-block state merging.

## Companion certificate

- `collatz/src/A0_s1_composable_ballot_address_state_certificate.py`
- `collatz/src/A0_s1_72bit_near_threshold_block_jump_certificate.py`
- `collatz/src/A0_s1_christoffel_correction_dag_certificate.py`

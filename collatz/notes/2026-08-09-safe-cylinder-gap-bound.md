# Safe-cylinder gap bound for the backward Bellman channel

Date: 2026-08-09

Status: **DERIVED LEMMA + INDEPENDENT SMALL-DEPTH CHECK**

This note gives a uniform upper bound on the backward lift value `J`.  It is useful for certified branch-and-bound but does not prove growth of `mu(K)`.

## 1. Coefficient boundary

Let

\[
\alpha=\log_3 2,
\qquad
a_j=\lceil\alpha j\rceil.
\]

For a coefficient-surviving state at split depth `k`, its odd-count satisfies

\[
q\ge a_k.
\]

Fix target depth `K`, remaining horizon `m=K-k`, and define the remaining odd deficit

\[
\boxed{d=\max(0,a_K-q).}
\]

Because `a_j` increases by at most one per step,

\[
0\le d\le a_K-a_k\le K-k=m.
\]

## 2. Consecutive-odd safe prefix

If `d>0`, choose the next `d` parity channels all odd.

After `j<=d` such steps the accumulated odd-count is `q+j`.  Since

\[
q\ge a_k
\]

and

\[
a_{k+j}\le a_k+j,
\]

we have

\[
q+j\ge a_{k+j}.
\]

Thus the consecutive-odd prefix is coefficient-admissible.

After `d` odd steps,

\[
q+d\ge a_K.
\]

Therefore every remaining suffix of length `m-d` is automatically coefficient-admissible, even if it contains no further odd steps.

Hence the future admissible language contains the full cylinder

\[
\boxed{O^d\{E,O\}^{m-d}.}
\]

## 3. Residue cylinder

The length-`d` all-odd parity prefix has canonical residue

\[
\boxed{\rho\equiv-1\equiv2^d-1\pmod{2^d}.}
\]

Therefore `A_{k,q,m}` contains the entire residue cylinder

\[
\rho\equiv2^d-1\pmod{2^d}.
\]

After the transformed scaling

\[
S_{k,q,m}=3^{-q}A_{k,q,m}\pmod{2^m},
\]

this becomes one complete congruence class modulo `2^d`:

\[
\boxed{
s\equiv-3^{-q}\pmod{2^d}.
}
\]

Its points are spaced exactly `2^d` around the cyclic group `Z/2^m Z`.

## 4. Cyclic-gap bound

Since the full transformed admissible set contains this complete congruence class, its maximum cyclic point spacing obeys

\[
\boxed{
G_{\max}(S_{k,q,m})\le2^d.
}
\]

Equivalently, for every transformed endpoint query `xi`,

\[
\boxed{
0\le J_{k,q,m}(\xi)\le2^d-1.
}
\]

If `q>=a_K`, then `d=0` and every future suffix is allowed, so

\[
\boxed{J_{k,q,m}(\xi)=0.}
\]

## 5. State-specific certified upper bound

Let `y` be the untransformed endpoint.  The unique lift modulo `2^d` that forces the next `d` parities to be all odd is

\[
\boxed{
C_*(k,q,K;y)
=
\left[3^{-q}(2^d-1-y)\right]_{2^d}.
}
\]

Take the actual lift integer `C=C_*`, with all higher lift bits zero.
The first `d` future channels are then odd, and after those channels the coefficient count has reached `a_K`; the actual remaining tail is therefore automatically safe.

Thus

\[
\boxed{
J_{k,q,m}(3^{-q}y)
\le C_*<2^d.
}
\]

This is often sharper than the uniform `2^d-1` bound and is cheap to evaluate.

## 6. Interpretation

The backward lift does not need all `m` nominal future bits.
Its minimum value always fits in at most

\[
\boxed{d=a_K-q}
\]

bits when `q<a_K`.

Thus surplus odd-count at the split has a precise computational value: each unit of surplus removes one potentially necessary high lift bit from this unconditional upper envelope.

This is an upper bound only.  It cannot by itself prove a lower bound on `mu(K)`.

## 7. Verification

An independent Wolfram exhaustive check compared the exact lift minimum with `C_*` for every coefficient-surviving state at every split `0<=k<=K` for

\[
5\le K\le12.
\]

No violation of

\[
J\le C_*
\]

was found.

## 8. Next use

The bound supplies a certified incumbent for a forward/backward branch-and-bound calculation.
To obtain proof-relevant pruning, it should be paired with a lower bound on `J`, for example from a short exact lookahead or an arithmetic exclusion of a block of small lift values.

A state can then be removed whenever its certified lower final cost exceeds the best certified upper final cost from another state.

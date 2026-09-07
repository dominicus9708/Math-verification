# First universal cell: endpoint q-lock and Hensel/address equivalence

Date: 2026-09-07

Status: **SAFE structural theorem across the full first-universal-cell universal-spine range, through the terminal first crossing.** The original `k<=195` version remains a valid weaker certificate; this revision replaces its weak fixed-`(k,q)` correction envelope by the root-spine mechanical position bound.

No Collatz proof is claimed.

---

## 1. Current window and first cell

Use

\[
B_0=2^{71},
\qquad
B_0<N<C_*:=\frac{1364}{1024}B_0,
\]

and the first universal first-coefficient-crossing cell

\[
(A_0,q_0)
=(114,208,327,604,
72,057,431,991).
\]

For a length-`k` parity prefix `w` with `q` odd entries write

\[
T^k(N)=\frac{3^qN+R(w)}{2^k}
=\frac{3^q}{2^k}\left(N+S(w)\right),
\qquad
S(w):=\frac{R(w)}{3^q}.
\]

Every candidate prefix before the first crossing lies on the universal minimal-counterexample spine, so its coefficient has not crossed below one at any earlier depth.

---

## 2. Universal-spine correction theorem

Let the zero-indexed positions of the odd bits be

\[
0\le p_1<p_2<\cdots<p_q.
\]

Immediately before the `r`-th odd bit, the prefix has length `p_r` and contains `r-1` odd bits. Because the first coefficient crossing has not yet occurred,

\[
3^{r-1}\ge2^{p_r}.
\]

Hence

\[
p_r\le\lfloor(r-1)\log_2 3\rfloor.
\]

Therefore

\[
\begin{aligned}
S(w)
&=\sum_{r=1}^q\frac{2^{p_r}}{3^r}\\
&\le\frac13\sum_{n=0}^{q-1}2^{-\{n\log_2 3\}}\\
&\le\frac q3.
\end{aligned}
\]

Thus every universal-spine prefix through the first cell satisfies

\[
\boxed{S(w)\le q/3.}
\]

Since

\[
q\le q_0<3B_0,
\]

we obtain the much stronger global first-cell scale separation

\[
\boxed{S(w)<B_0}
\]

for **every candidate prefix through `k=A0`, including the terminal first crossing**.

This is stronger than the earlier fixed-`(k,q)` envelope, whose all-word root-safe horizon stopped at `k=195`. The distinction is essential: the present theorem compares two states that both remain inside the universal-spine candidate language, while full-Hensel maximality must allow arbitrary competing words.

---

## 3. Endpoint q-lock theorem — full first cell

Take two candidate-window universal-spine starts `N_1,N_2` at a common depth

\[
1\le k\le A_0
\]

and suppose

\[
T^k(N_1)=T^k(N_2).
\]

Let their odd counts and normalized corrections be `(q_1,S_1)` and `(q_2,S_2)`.

Then

\[
3^{q_1}(N_1+S_1)=3^{q_2}(N_2+S_2).
\]

Assume `q_1>q_2`. Then

\[
N_2+S_2
=3^{q_1-q_2}(N_1+S_1)
>3B_0.
\]

But the current start cap and the universal-spine correction theorem give

\[
N_2+S_2
<C_*+B_0
<3B_0,
\]

contradiction.

Therefore

\[
\boxed{
T^k(N_1)=T^k(N_2),\ 1\le k\le A_0
\Longrightarrow
q_1=q_2.
}
\]

The endpoint **q-lock therefore holds throughout the entire first universal cell**, not merely through depth 195.

---

## 4. Ordering inside a locked endpoint fiber

With `q_1=q_2=q`, equality of endpoints gives

\[
3^qN_1+R_1=3^qN_2+R_2,
\]

hence

\[
\boxed{R_1-R_2=3^q(N_2-N_1).}
\]

Thus

\[
\boxed{N_1<N_2\iff R_1>R_2.}
\]

So within a candidate-language endpoint fiber, the smallest ordinary start is exactly the largest-correction representative.

For a hypothetical minimal positive counterexample, every larger member of that same endpoint fiber is impossible because it merges after `k` steps with a smaller positive start.

---

## 5. Exact relation to Hensel/address translation

Equal `q` and equal endpoint imply

\[
R_1\equiv R_2\pmod{3^q}.
\]

Conversely, if

\[
R_1-R_2=t3^q,
\qquad t\in\mathbb Z,
\]

then shifting the ordinary start by `t` produces the same endpoint:

\[
3^q(N-t)+R_1=3^qN+R_2.
\]

Hence on the q-locked candidate language,

\[
\boxed{
\text{same endpoint fiber}
\Longleftrightarrow
\text{same full-Hensel correction class together with its exact start translation}.
}
\]

If `M` is the larger correction and

\[
R=M-t3^q,
\qquad t>0,
\]

then their canonical start residues differ by exactly

\[
\boxed{t}.
\]

The Hensel credit is therefore literally the horizontal ordinary-address displacement inside the locked endpoint fiber.

---

## 6. New displacement bound inside the universal spine

For two same-endpoint candidate states with common odd count `q`,

\[
|N_1-N_2|
=\frac{|R_1-R_2|}{3^q}
=|S_1-S_2|.
\]

Since each correction is at most `q/3`, a coarse but exact bound is

\[
\boxed{|N_1-N_2|<q/3.}
\]

At the terminal first cell this gives

\[
|N_1-N_2|<q_0/3<2^{35}.
\]

Thus any endpoint fiber is extremely local compared with a top-address block of width `2^61`:

- it cannot skip a top-11-bit block;
- it can meet two adjacent top blocks only inside a boundary halo of width `<2^35`;
- away from those halos, endpoint quotienting is strictly internal to one of the 340 surviving blocks.

This is an address-geometric consequence, not a density statement.

---

## 7. Relation to the earlier root-Hensel theorem

The original root full-Hensel maximality theorem remains stronger in a different direction: it compares the actual minimal-counterexample prefix with **arbitrary** same-class words, even when the competitor itself violates the universal spine. That arbitrary-competitor theorem is only universally credit-safe through depth 195 under the current floor.

The endpoint q-lock theorem instead compares two states already inside the candidate universal-spine language. It therefore remains valid through the whole first cell.

Accordingly:

- through depth 195, endpoint quotient and full-Hensel maximality overlap strongly and must not be double-counted;
- beyond depth 195, candidate-language endpoint quotient remains legal even though arbitrary-word full-Hensel maximality is no longer automatically credit-safe.

---

## 8. DSD audit

### CLOSED / SAFE

1. universal-spine odd positions obey `p_r<=floor((r-1)log_2 3)`;
2. every first-cell candidate prefix satisfies `S<=q/3<B0`;
3. equal endpoint inside the current candidate window forces equal odd count throughout `k<=A0`;
4. once `q` is locked, smaller start iff larger correction;
5. the endpoint fiber is an exact Hensel/address-translation fiber;
6. endpoint fibers have total ordinary-address diameter `<q/3`, hence `<2^35` at the first-cell terminal depth.

### IMPORTANT NON-UPGRADE

Endpoint quotienting inside the q-locked language is not an independent probabilistic filter. In the overlap range it expresses the same exact merge/minimality geometry as root-Hensel translation.

### OPEN

1. exploit candidate-language endpoint quotient after depth 195 without importing arbitrary-word Hensel maximality;
2. use the `<2^35` endpoint-fiber diameter to organize each of the 340 top-address blocks and their boundary halos;
3. prove enough intra-block endpoint/address incompatibility to remove blocks;
4. transfer the surviving address information to terminal correction and close the first cell.

### PROHIBITED UPGRADES

1. Do not apply `S<=q/3` to an arbitrary competitor that does not satisfy the universal prefix spine.
2. Do not extend full-Hensel arbitrary-competitor maximality merely because candidate-language q-lock extends.
3. Do not treat the `<2^35` fiber diameter as an emptiness statement.
4. Do not infer Collatz or even first-cell closure from endpoint quotient alone.

---

## 9. Reproducibility and revision history

Original weaker certificate:

`collatz/src/first_cell_endpoint_q_lock_certificate.py`

commit:

`e4e921f9b19aeacc85d96c37731e0867c52fea98`

Full-first-cell scale certificate:

`collatz/src/first_cell_endpoint_q_lock_global_spine_certificate.py`

commit:

`522b7412e7b3bbf96e3c2ea8b45c642d9c46b305`

Revision note:

- the `k<=195` statement is preserved as a correct weaker historical stage;
- the current canonical statement uses the universal-spine mechanical correction bound and holds through `k=A0`.

---

## 10. Next exact target

The next useful object is the **340-block address geometry with local endpoint halos**. Since a same-endpoint candidate fiber has diameter `<2^35` while each top block has width `2^61`, endpoint interactions across different top blocks are confined to an exponentially thin exact boundary region. The next calculation should separate interior block states from boundary-halo states and test which constraints remain genuinely cross-block.
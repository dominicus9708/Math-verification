# First universal cell: endpoint q-lock and Hensel/address equivalence

Date: 2026-09-07

Status: **SAFE structural theorem in the current first-cell candidate window through depth 195.** This note documents the theorem certified by `collatz/src/first_cell_endpoint_q_lock_certificate.py`, and separates the genuinely new endpoint/address interpretation from the already-known root-Hensel maximality filter.

No Collatz proof is claimed.

---

## 1. Current window

Use

\[
B_0=2^{71},
\qquad
B_0<N<C_*:=\frac{1364}{1024}B_0.
\]

For a length-`k` parity prefix `w` with `q` odd entries write

\[
T^k(N)=\frac{3^qN+R(w)}{2^k}
=\frac{3^q}{2^k}\left(N+S(w)\right),
\qquad
S(w):=\frac{R(w)}{3^q}.
\]

For coefficient-surviving prefixes, the universal normalized-correction envelope is

\[
S(w)
\le
2^{k-q}\left(1-\left(\frac23\right)^q\right).
\]

The exact certificate verifies that for every coefficient-surviving prefix through

\[
\boxed{k\le195}
\]

one has

\[
\boxed{S(w)<B_0.}
\]

The first envelope failure occurs at `(k,q)=(196,124)`.

---

## 2. Endpoint q-lock theorem

Take two candidate-window starts `N_1,N_2` with coefficient-surviving length-`k` prefixes, `k<=195`, and suppose they have the same endpoint:

\[
T^k(N_1)=T^k(N_2).
\]

Let their odd counts and normalized corrections be `(q_1,S_1)` and `(q_2,S_2)`.

Then

\[
3^{q_1}(N_1+S_1)=3^{q_2}(N_2+S_2).
\]

Assume without loss of generality `q_1>q_2`. Then

\[
N_2+S_2
=3^{q_1-q_2}(N_1+S_1)
>3B_0.
\]

But the current start cap and the correction envelope give

\[
N_2+S_2
<C_*+B_0
=\left(\frac{1364}{1024}+1\right)B_0
<3B_0,
\]

which is impossible.

Therefore

\[
\boxed{
T^k(N_1)=T^k(N_2),\ k\le195
\Longrightarrow
q_1=q_2.
}
\]

This is the endpoint **q-lock**.

---

## 3. Ordering inside a locked endpoint fiber

With `q_1=q_2=q`, equality of endpoints gives

\[
3^qN_1+R_1=3^qN_2+R_2,
\]

hence

\[
\boxed{
R_1-R_2=3^q(N_2-N_1).
}
\]

Thus

\[
\boxed{
N_1<N_2
\iff
R_1>R_2.
}
\]

So within a candidate-window endpoint fiber through depth 195, the smallest ordinary start is exactly the largest-correction representative.

For a hypothetical minimal positive counterexample, every larger member of the same endpoint fiber is impossible: it merges after `k` steps with a smaller positive start and hence cannot be minimal.

Therefore endpoint quotienting may retain only the smallest start in each locked fiber.

---

## 4. Exact relation to full-Hensel classes

For two length-`k` words with the same odd count `q`, equal endpoints satisfy

\[
R_1-R_2=3^q(N_2-N_1).
\]

In particular

\[
R_1\equiv R_2\pmod{3^q}.
\]

Conversely, if two words have equal `q` and

\[
R_1-R_2=t3^q,
\qquad t\in\mathbb Z,
\]

then shifting their ordinary starts by `t` gives the exact same endpoint:

\[
3^q(N-t)+R_1=3^qN+R_2.
\]

Hence, once q-lock holds,

\[
\boxed{
\text{same endpoint fiber}
\Longleftrightarrow
\text{full-Hensel correction class plus its exact start translation}.
}
\]

This is important for bookkeeping: the endpoint quotient is **not an additional independent exclusion filter** on top of root-Hensel maximality in the q-locked range. It is the same root-minimality mechanism expressed in an address-faithful endpoint coordinate.

---

## 5. Address-translation form

Let `M` be the maximum correction in one full-Hensel class and let another class member have

\[
R=M-t3^q,
\qquad t>0.
\]

If the maximum-correction representative has canonical start residue `n_k`, then the lower-correction member has canonical residue

\[
\boxed{n_k+t\pmod{2^k}.}
\]

Moreover, for every integer lift `ell`,

\[
T^k(n_k+\ell2^k)
=
T^k(n_k+t+\ell2^k)
\]

when the respective parity words are used.

Thus the Hensel credit `t` is literally the horizontal displacement between same-endpoint ordinary starts.

This is the useful new interpretation for the 340-block problem: Hensel classes preserve the same-integer address translation rather than merely a correction congruence.

---

## 6. DSD audit

### CLOSED / SAFE

1. `S(w)<B0` for every coefficient-surviving prefix through depth 195;
2. equal endpoint inside the current candidate window forces equal odd count through depth 195;
3. once `q` is locked, smaller start iff larger correction;
4. the endpoint fiber equals the translated full-Hensel class in that range;
5. retaining the smallest start / maximum correction representative is a legal minimal-counterexample quotient.

### IMPORTANT NON-UPGRADE

The q-lock theorem does **not** create a second independent pruning factor on top of root-Hensel maximality. Counting both as independent exclusions would double-count the same mechanism.

### OPEN

1. exploit the endpoint/Hensel quotient while retaining the ordinary 72-bit address;
2. compress the surviving 340 top-address blocks without enumerating all lower 61 bits;
3. extend safe endpoint dominance beyond the all-q locked range `k<=195`;
4. transfer the surviving root address to the terminal first crossing `(A0,q0)`.

### PROHIBITED UPGRADES

1. Do not transfer the q-lock beyond its proved correction-envelope range without an additional inequality.
2. Do not infer that one endpoint representative means one global orbit class at all later depths unless the exact merge has already occurred.
3. Do not treat endpoint quotient and Hensel maximality as statistically independent filters.
4. Do not infer first-cell closure from this quotient alone.

---

## 7. Reproducibility

Certificate:

`collatz/src/first_cell_endpoint_q_lock_certificate.py`

Commit containing the certificate:

`e4e921f9b19aeacc85d96c37731e0867c52fea98`

Expected output includes:

```text
PASS
endpoint q-lock depth = 195
equal endpoint inside current candidate window => equal odd count
with equal q: smaller start <=> larger correction
```

---

## 8. Next target

The endpoint formulation suggests a safe continuation beyond the globally q-locked range. If two same-endpoint candidate starts have unequal odd counts, their count gap and the low-q correction envelope constrain which member can be smaller. The next step is therefore an **unequal-q endpoint-gap dominance theorem**, rather than an unsupported extension of full q-lock.
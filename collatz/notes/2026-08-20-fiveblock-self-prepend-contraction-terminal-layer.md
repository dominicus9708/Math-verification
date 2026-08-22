# Five-block self-prepend contraction and the finite terminal layer

Date: 2026-08-20

Status: **exact five-step transport lemmas plus a finite-floor theorem.** These results sharpen the sparse-tail min-plus reduction. They do **not** prove coefficient stopping and do **not** prove the Collatz conjecture.

We use the accelerated map

\[
T(x)=\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2,
\end{cases}
\]

and

\[
b_k=\lceil k\alpha\rceil,
\qquad \alpha=\log_3 2.
\]

The generalized coefficient-survivor language is

\[
\mathcal S_{s,h}(J)
=
\{x\ge1:q_j(x)\ge b_{s+j}-b_s-h\quad(1\le j\le J)\},
\]

with minimum \(\mu_{s,h}(J)\).

For a length-five parity word \(w\), write

\[
2^5 c_w=3^{q_w}r_w+R_w,
\]

where \(r_w\) is its canonical start, \(c_w=T^5(r_w)\), \(q_w\) is its odd count, and \(R_w\ge0\) is its affine correction.

## 1. High-odd blocks reproduce at their suffix phase

Assume \(w\) is admissible at phase-height state \((s,h)\), and put

\[
d_s=b_{s+5}-b_s\in\{3,4\},
\qquad
h'=h+q_w-d_s.
\]

### Lemma 1

If

\[
q_w\ge4,
\]

then the same word \(w\) is admissible at the suffix state

\[
(s+5,h').
\]

### Proof

For every \(j\le5\), both phase increments

\[
b_{s+j}-b_s,
\qquad
b_{s+5+j}-b_{s+5}
\]

lie in \(\{b_j-1,b_j\}\), so their difference is at most one.

If \(d_s=3\), then \(q_w\ge4\) gives \(h'\ge h+1\), which absorbs that possible one-unit phase increase.

If \(d_s=4\) and \(s>0\), write \(\theta=\{s\alpha\}\) and \(\delta=\{5\alpha\}=5\alpha-3\). The condition \(d_s=4\) is \(\theta\ge1-\delta\). Hence after five steps

\[
\theta'=\{(s+5)\alpha\}=\theta+\delta-1<\theta.
\]

Therefore for every \(j\le5\),

\[
b_{s+5+j}-b_{s+5}
\le
b_{s+j}-b_s.
\]

Since now \(h'\ge h\), admissibility transfers again. The case \(s=0\) follows from

\[
b_{5+j}-b_5\le b_j.
\]

Thus every admissible \(q_w\ge4\) five-block is suffix-self-admissible. \(\square\)

## 2. Self-prepend transport

Fix the suffix state

\[
(A,H)=(s+5,h').
\]

Let \(y\in\mathcal S_{A,H}(J)\) satisfy

\[
y\equiv c_w\pmod{3^{q_w}}.
\]

Define its exact predecessor through \(w\):

\[
x
=
r_w+32\frac{y-c_w}{3^{q_w}}
=
\frac{32y-R_w}{3^{q_w}}.
\]

For \(q_w\ge4\), Lemma 1 handles the first five steps at state \((A,H)\). For later steps, the five-step barrier increment is always at most four:

\[
b_{A+t}-b_{A+t-5}\le4\le q_w.
\]

Therefore the \(q_w\) odd steps supplied by the prepended block are enough to bridge the phase displacement, and

\[
\boxed{x\in\mathcal S_{A,H}(J).}
\]

This is the key self-prepend property.

## 3. Strong high-q syndrome penalty lower bound

Let

\[
\mu'=\mu_{A,H}(J)
\]

and let \(\nu\) be the least member of \(\mathcal S_{A,H}(J)\) in the ternary syndrome

\[
y\equiv c_w\pmod{3^{q_w}}.
\]

Applying the self-prepend map to \(\nu\) gives a member of the same suffix survivor set, hence by minimality

\[
\frac{32\nu-R_w}{3^{q_w}}
\ge
\mu'.
\]

Therefore

\[
\boxed{
32(\nu-\mu')-R_w
\ge
(3^{q_w}-32)\mu'.
}
\]

This is stronger than merely proving \(P_w-E_w\ge0\).

If

\[
c_{s,h}=\frac{2^s}{3^{b_s+h}},
\qquad
c'=\frac{2^{s+5}}{3^{b_s+h+q_w}},
\]

then the normalized recurrence increment satisfies

\[
\boxed{
P_w-E_w
\ge
(c_{s,h}-c')\mu'
\ge0,
\qquad q_w\ge4.
}
\]

Thus all high-odd five-blocks are lossless in the exact normalized min-plus transport; any negative penalty-minus-rebate event must lie in \(q_w\le3\).

## 4. Low-q algebra and the sharp finite threshold 16

For \(q_w\le3\), no self-prepend contraction is available because \(3^{q_w}<32\). But \(\nu\ge\mu'\) gives

\[
x
=\frac{32\nu-R_w}{3^{q_w}}
\ge
\frac{32\mu'-R_w}{3^{q_w}}.
\]

Across all 32 five-bit parity words, the exact maximum corrections at each odd count are

\[
\begin{array}{c|rrrrrr}
q&0&1&2&3&4&5\\\hline
\max R_w&0&16&40&76&130&211.
\end{array}
\]

For \(q\le3\), the worst threshold for ensuring \(x\ge\mu'\) is

\[
\max_{q\le3,w}
\frac{R_w}{32-3^q}
=
\frac{76}{5}
=15.2,
\]

attained by the word with canonical residue \(r=28\), odd count \(q=3\), and \(R=76\).

Hence the integer threshold

\[
\boxed{\mu'\ge16}
\]

implies

\[
\boxed{x\ge\mu'}
\]

for **every** low-q block as well.

Therefore once the suffix floor reaches 16, no admissible five-block can pull the exact unnormalized branch minimum below the suffix minimum.

## 5. The floor 16 is reached outside a linear terminal layer

For every integer

\[
1\le x\le15,
\]

direct exact trajectories enter the \(1\leftrightarrow2\) accelerated cycle and satisfy the uniform bound

\[
\boxed{q_j(x)\le j/2+2\qquad(j\ge1).}
\]

The bound is sharp at \(x=15\), where \(2q_j-j\) reaches 4 before cycle entry.

If such an \(x\) belonged to \(\mathcal S_{s,h}(J)\), then the mechanical one-slack inequality would give

\[
q_J(x)
\ge
b_{s+J}-b_s-h
\ge
b_J-1-h.
\]

Thus

\[
b_J\le J/2+h+3.
\]

But

\[
\alpha=\log_3 2>5/8
\]

because the exact integer inequality

\[
2^8=256>243=3^5
\]

holds. Therefore, if

\[
J\ge8(h+3),
\]

then

\[
b_J>\alpha J>J/2+h+3,
\]

a contradiction.

Hence

\[
\boxed{
J\ge8(h+3)
\quad\Longrightarrow\quad
\mu_{s,h}(J)\ge16
}
\]

for every phase \(s\ge0\) and every slack \(h\ge0\).

This removes the small-floor anomaly uniformly: it can occur only in a terminal boundary layer whose thickness is linear in \(h\).

## 6. Uniform five-block no-drop corollary

For a source state \((s,h)\), every five-block suffix has

\[
h'\le h+2
\]

because \(q_w\le5\) and \(b_{s+5}-b_s\ge3\).

Therefore if the remaining suffix horizon satisfies

\[
J\ge8(h+5),
\]

then every admissible suffix state obeys

\[
\mu_{s+5,h'}(J)\ge16.
\]

Combining the high-q self-prepend theorem with the low-q threshold gives

\[
\boxed{
\mu_{s,h}(J+5)
\ge
\min_{w\in\mathcal W_{s,h}}
\mu_{s+5,h'_w}(J),
\qquad
J\ge8(h+5).
}
\]

Thus all possible exact five-block decreases of the unnormalized minimal-survivor floor are confined to the finite terminal layer.

## 7. What remains open

This does not yet force \(\mu_{s,h}(J)\) past the full zero-lift box threshold \(3^{b_s+h}\). The remaining hard branch is a long tail dominated by \(q_w\ge4\) blocks: the self-prepend theorem prevents them from undercutting the suffix minimum, but it does not by itself force a uniform multiplicative increase.

That remaining high-odd-density obstruction is consistent with the classical necessary density condition for a hypothetical divergent Collatz orbit, so it must not be declared closed without an additional pointwise theorem.

Certificate:

`collatz/src/fiveblock_self_prepend_contraction_terminal_layer_certificate.py`.

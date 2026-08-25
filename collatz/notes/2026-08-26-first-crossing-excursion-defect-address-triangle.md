# First-crossing excursion, correction defect, and formation-address triangle

Date: 2026-08-26

Status: **exact algebraic theorem.** This is a binary first-crossing theorem and does not use the disputed ternary recursively-sufficient selector, repeated L7/L14 pullback, or a probabilistic independence assumption. It does not prove the Collatz conjecture.

## 1. First-crossing language

Use the accelerated map

\[
T(n)=\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2.
\end{cases}
\]

Let a length-\(A\) parity word \(w\) have prefix odd counts \(q_i\), and suppose \(A\) is its **first coefficient crossing**:

\[
3^{q_i}\ge2^i\quad(1\le i<A),
\qquad
3^{q_A}<2^A.
\]

Put

\[
\alpha:=\log_3 2,
\qquad
k_i:=\lceil i\alpha\rceil.
\]

At a first crossing one necessarily has

\[
q_{A-1}=k_{A-1}=k_A-1,
\qquad
w_{A-1}=0.
\]

Let \(m\) denote the unique mechanical boundary word with prefix sums

\[
\sum_{t=0}^{i-1}m_t=k_i\qquad(i<A)
\]

and the same final zero.  It has the same total odd count \(q=q_A\) as \(w\).

## 2. Height excursion

Define

\[
h_i:=q_i-k_i\qquad(0\le i<A).
\]

Then

\[
\boxed{h_i\ge0,\qquad h_0=0,\qquad h_{A-1}=0.}
\]

Moreover

\[
h_{i+1}-h_i=w_i-m_i.
\]

Thus height can rise only where the mechanical word has a zero and the actual word uses a one, and it can fall only where the mechanical word has a one and the actual word uses a zero.

Every nonmechanical first-crossing word is therefore a collection of excursions above the Beatty boundary.  This is a purely combinatorial encoding of the coefficient-survival constraint.

## 3. Ordinal displacement theorem

Let

\[
0\le a_1<\cdots<a_q<A
\]

be the positions of the odd bits of \(w\), and

\[
0\le b_1<\cdots<b_q<A
\]

those of the mechanical word.

Prefix dominance implies

\[
\boxed{a_j\le b_j\quad(1\le j\le q).}
\]

Define the displacement

\[
s_j:=b_j-a_j\ge0.
\]

The total displacement is exactly the area under the Beatty-height excursion:

\[
\boxed{
\sum_{j=1}^q s_j
=
\sum_{i=1}^{A-1}h_i.
}
\]

Hence the height path and the ordinal displacement vector carry the same total transport information.

## 4. Exact correction-defect identity

For a word whose odd positions are \(a_j\), the affine correction is

\[
R(w)=\sum_{j=1}^{q}3^{q-j}2^{a_j}.
\]

The mechanical correction is

\[
R_{\rm mech}=\sum_{j=1}^{q}3^{q-j}2^{b_j}.
\]

Therefore the full correction loss is not merely bounded by the displacement; it is exactly

\[
\boxed{
E:=R_{\rm mech}-R(w)
=
\sum_{j=1}^{q}
3^{q-j}\bigl(2^{b_j}-2^{a_j}\bigr).
}
\]

Equivalently,

\[
\boxed{
\frac{E}{3^q}
=
\sum_{j=1}^{q}
\frac{2^{b_j}}{3^j}igl(1-2^{-s_j}\bigr).
}
\]

Since for the mechanical positions

\[
2^{b_j}\le3^{j-1}<2^{b_j+1},
\]

one obtains the deterministic charge bound

\[
\boxed{
\frac{E}{3^q}
>
\frac16
\sum_{j=1}^{q}(1-2^{-s_j}).
}
\]

In particular every nonmechanical first-crossing word has normalized defect greater than \(1/12\), but the exact identity retains much more information than this coarse one-defect bound.

## 5. Exact formation-address identity

Every length-\(A\) parity word determines one canonical root residue

\[
\rho(w)\pmod{2^A}
\]

through

\[
3^q\rho(w)+R(w)\equiv0\pmod{2^A}.
\]

Let \(\rho_{\rm mech}\) be the mechanical residue.  Subtracting the two formation congruences gives

\[
3^q\bigl(\rho(w)-\rho_{\rm mech}\bigr)
\equiv E\pmod{2^A}.
\]

Because \(3\) is invertible modulo \(2^A\),

\[
\boxed{
\rho(w)-\rho_{\rm mech}
\equiv
\sum_{j=1}^{q}
3^{-j}\bigl(2^{b_j}-2^{a_j}\bigr)
\pmod{2^A}.
}
\]

Using \(s_j=b_j-a_j\), this is

\[
\boxed{
\rho(w)-\rho_{\rm mech}
\equiv
\sum_{j=1}^{q}
2^{a_j}(2^{s_j}-1)3^{-j}
\pmod{2^A}.
}
\]

Thus the same displacement vector has two simultaneous projections:

\[
\boxed{
\text{real/additive projection}
\longleftrightarrow E/3^q,
\qquad
\text{dyadic formation projection}
\longleftrightarrow \rho-\rho_{\rm mech}.
}
\]

This is the useful DSD-style state alignment: the correction and formation channels are not independent descriptors.

## 6. Finite-address truncation

Reducing the address identity modulo \(2^K\), with \(K\le A\), shows that any displacement whose actual and mechanical positions are both at least \(K\) vanishes from the \(K\)-bit address equation.

Therefore

\[
\boxed{
\rho(w)\pmod{2^K}
\text{ is controlled only by displacement transport touching the first }K
\text{ positions}.}
\]

Later defects can alter the real correction budget while being unable to repair an already-fixed low-\(K\) formation address.

For the first global resonance, every candidate start is below \(2^{72}\), so the \(K=72\) projection is the complete ordinary start address.  The mechanical address itself lies above the allowed start ceiling, hence every remaining first-resonance candidate must carry a nonzero **early displacement channel** touching the first 72 positions.

## 7. What the single-swap diagnostic shows

The mechanical 72-bit prefix admits several one-adjacent-left-swap variants whose canonical starts do fall inside the first-resonance start band.  Direct exact orbit checks show that those particular starts suffer their coefficient crossing at depth 73--81 and descend below the start there.

This is diagnostic only.  It disproves the overly strong claim that the 72-bit formation band alone forces a large displacement count.  What remains plausible is the stronger joint statement:

> a displacement pattern capable of keeping the **same finite natural address** coefficient-surviving all the way to the first resonance must accumulate enough later defect/formation incompatibility to violate the near-return budget.

The theorem above gives the exact common variables in which that statement should be attacked.

## 8. DSD proof-chain interpretation

The remaining first-resonance problem can now be written as one synchronized chain rather than three separate searches:

\[
\boxed{
\text{Beatty excursion }h
\leftrightarrow
\text{ordinal transport }s
\longrightarrow
\begin{cases}
\text{real correction defect},\\
\text{dyadic formation address},
\end{cases}
\longrightarrow
\text{tiny near-return gap }g.
}
\]

The next target is an **address--defect incompatibility theorem** for bounded ordinary roots.  It must use both projections of the same displacement vector; using only the real defect or only the 72-bit address is demonstrably too weak.

Companion regression certificate:

`collatz/src/first_crossing_excursion_defect_address_certificate.py`.

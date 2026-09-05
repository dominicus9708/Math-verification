# Whole-prefix nearest credit and logarithmic state compression

Date: 2026-08-24

Status: **unconditional finite nearest-credit theorem through H=32 + unconditional polynomial endpoint-fibre theorem + logarithmic dangerous-core reduction conditional only on the cited Rhin linear-form estimate.**  This is not a proof of the Collatz conjecture.

## 1. Replace class-maximum credit by nearest useful credit

For a complete length-H word w with q odd steps and correction R_w,

\[
T^H(N)=\frac{3^qN+R_w}{2^H}.
\]

If another complete q-word u satisfies

\[
R_u=R_w+3^q d,
\qquad d>0,
\]

then the smaller root

\[
M=N-d
\]

reaches exactly the same H-step endpoint.  Therefore a minimal counterexample only needs **one** larger correction in its complete Hensel class.  It is unnecessary to move all the way to the class maximum.

Define

\[
\boxed{
d_{\rm near}(w)
:=\min\left\{
\frac{R'-R_w}{3^q}:R'>R_w,\ R'\equiv R_w\pmod{3^q}
\right\}
}
\]

when the set is nonempty, and

\[
\boxed{G_H:=\max_w d_{\rm near}(w)}
\]

over non-maximal coefficient-surviving H-prefixes.

This is a strictly more relevant root-credit quantity than the distance to the complete class maximum.

## 2. Exact H=28,...,32 values

The exact finite calculations give

\[
\boxed{
G_{28}=25,
\quad G_{29}=25,
\quad G_{30}=34,
\quad G_{31}=34,
\quad G_{32}=34.
}
\]

For comparison, the corresponding maximum-credit distances to the complete class maximum were already larger:

\[
D_{28}=29,
\quad D_{29}=47,
\quad D_{30}=59,
\quad D_{31}=71,
\quad D_{32}=71.
\]

Thus the root predecessor actually needed by minimality remains substantially closer than the global maximum sibling.

## 3. Exact H=32 layer theorem

At H=32 the terminal coefficient-surviving odd counts are q=21,...,32.  The exact nearest-credit maxima are

\[
\boxed{
(G_{32,q})_{q=21}^{32}
=(34,25,12,6,6,1,1,1,1,1,0,0).
}
\]

The q=21 layer alone contains

\[
13,472,296
\]

coefficient-surviving words.  Among them

\[
2,547,774
\]

are non-maximal in their complete Hensel class and therefore possess a larger same-class sibling.  Of these,

\[
\boxed{2,488,626}
\]

already have

\[
d_{\rm near}=1.
\]

No q=21 survivor has nearest credit above 34.

For q=22,...,32 the exact maxima decrease to

\[
25,12,6,6,1,1,1,1,1,0,0.
\]

Certificate:

`collatz/src/h32_whole_prefix_nearest_credit_certificate.cpp`.

## 4. Endpoint/Hensel multiplicity is polynomial without proving injectivity

Fix H, endpoint y and odd count q.  Two complete whole-prefix maximum representatives with the same y and q would satisfy

\[
3^q r_1+R_1=3^q r_2+R_2.
\]

Hence

\[
R_1\equiv R_2\pmod{3^q}.
\]

They lie in the same complete Hensel class.  Since both are the maximum correction representative of that class,

\[
R_1=R_2,
\]

and then r_1=r_2.  The parity-vector/canonical-residue bijection makes the words identical.

Therefore for fixed y and q there is at most one whole-prefix maximum word.  Terminal coefficient survival requires

\[
q\ge q_{\min}(H):=\lceil H\log_3 2\rceil,
\]

so every endpoint fibre of the whole-prefix maximum language has multiplicity at most

\[
\boxed{
H-q_{\min}(H)+1=O(H).
}
\]

Thus endpoint/Hensel multiplicity contributes only

\[
\boxed{O(\log H)=o(H)}
\]

information bits.  The stronger experimentally observed endpoint injectivity is unnecessary for obtaining zero exponential multiplicity rate.

## 5. Rhin turns the first-crossing dangerous core logarithmic

At a first coefficient crossing put

\[
\sigma=\lceil q\log_2 3\rceil,
\qquad
D=2^\sigma-3^q>0,
\]

and

\[
\Lambda=\sigma\log2-q\log3>0.
\]

The previously derived one-coordinate order-reversal criterion says that a dangerous odd-position coordinate i must satisfy

\[
3^{q-i}\ge D.
\]

Rozier and Terracol, Proposition 6.3 of *Paradoxical behavior in Collatz sequences* (arXiv:2502.00948v5; Discrete Mathematics 349 (2026), 115167), quote Rhin's effective estimate

\[
|\Lambda|\ge H^{-13.3}
\]

for the integer linear form in 1, log 2 and log 3, where here H=max(\sigma,q)=\sigma.

Since

\[
D=3^q(e^\Lambda-1)>3^q\Lambda,
\]

we obtain

\[
D>3^q\sigma^{-13.3}.
\]

Combining this with the dangerous-axis condition gives

\[
3^{-i}>\sigma^{-13.3},
\]

hence

\[
\boxed{i<13.3\log_3\sigma.}
\]

Equivalently, because 13.3=133/10, every dangerous coordinate satisfies the exact integer inequality

\[
\boxed{3^{10i}<\sigma^{133}.}
\]

Therefore the dangerous interaction dimension satisfies

\[
\boxed{h(q)=O(\log q).}
\]

This replaces the older coarse linear bound of about 14.44% of q by a logarithmic bound.  The only external input in this reduction is the quoted Rhin theorem; the remaining implication is elementary.

Finite exact diagnostic:

`collatz/src/rhin_logarithmic_dangerous_core_certificate.py`.

The exact record dangerous dimensions through q=200,000 are

\[
\begin{array}{c|c}
q&h(q)\\\hline
1&1\\
5&2\\
29&3\\
41&4\\
253&5\\
306&6\\
8951&7\\
13606&8\\
15601&9\\
47468&10\\
79335&11\\
190537&15
\end{array}
\]

These records are finite diagnostics only; the O(log q) theorem comes from the Rhin inequality above, not from the scan.

## 6. Current unconditional state budget

After the pullback audit, two potential exponential channels are now independently compressed:

1. **endpoint/Hensel multiplicity:** at most O(H), hence O(log H) bits;
2. **first-crossing dangerous coordinate signature:** O(log H) coordinates under Rhin.

The whole-prefix nearest root credit also remains small in every exact horizon currently checked:

\[
25,25,34,34,34
\quad(H=28,...,32).
\]

No asymptotic theorem for G_H is asserted yet.

## 7. Next proof-level target

The next target is now sharper than global class-maximum control:

> **Nearest Hensel-gap theorem.**  Prove that the maximum nearest positive whole-prefix Hensel credit G_H grows subexponentially, preferably polynomially or linearly.

A bound

\[
G_H=2^{o(H)}
\]

is sufficient for the root-credit channel to have zero exponential information rate.  Combined with the O(H) endpoint fibre and O(log H) dangerous-coordinate core, this would leave the selector/dyadic same-address correlation as the only remaining candidate exponential Stage-4 channel.

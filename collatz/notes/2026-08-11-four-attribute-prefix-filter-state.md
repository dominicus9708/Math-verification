# Exact four-attribute prefix/filter state

Date: 2026-08-11

Status: **exact global state reduction for all parity-prefix classes**. This note gives a closed state/filter system over parity classes without enumerating starting integers. It does not yet supply the universal quotient or contraction theorem needed for a Collatz proof.

## 1. Prefix affine state

For a realizable accelerated Collatz parity prefix of length \(k\), let

\[
q=Q_k
\]

be the odd-step count and let \(R\ge0\) be the correction in

\[
\boxed{
T^k(n)=\frac{3^q n+R}{2^k}.
}
\]

The prefix state will carry only

\[
\boxed{
S=(k,q,R,\Theta),
}
\]

where \(\Theta\in\mathbb Q_{\ge0}\cup\{+\infty\}\) is the minimum survival ceiling created by all contracting prefix times seen so far.

---

## 2. Formation residue from the same correction

Every integer realizing the prefix must satisfy the endpoint integrality congruence

\[
3^qn+R\equiv0\pmod{2^k}.
\]

Because \(3^q\) is invertible modulo \(2^k\), the prefix has the unique residue

\[
\boxed{
r(S)
\equiv
-3^{-q}R
\pmod{2^k}.
}
\]

Choose the canonical representative \(0\le r<2^k\). The least admissible integer \(n\ge2\) in the class is

\[
\boxed{
\rho(S)=
\begin{cases}
r,&r\ge2,\\
2^k,&r=0,\\
1+2^k,&r=1.
\end{cases}
}
\]

for \(k\ge1\), with \(\rho=2\) at the root \(k=0\).

Thus the formation floor is not an independent state variable: it is a 2-adic/modular projection of \((k,q,R)\).

---

## 3. Survival ceiling from the same correction

At a contracting prefix time,

\[
3^q<2^k,
\]

the no-first-descent condition at that time is

\[
\boxed{
n\le C(S):=\frac{R}{2^k-3^q}.}
\]

Therefore the cumulative survival ceiling is the minimum over all contracting prefix times. It is carried recursively as \(\Theta\).

Thus the same correction \(R\) has two distinct proof roles:

\[
\boxed{
R\xrightarrow{\text{mod }2^k}\text{formation residue/floor},
}
\]

\[
\boxed{
R\xrightarrow{\text{real ratio}}\text{survival ceiling}.
}
\]

This 2-adic/Archimedean dual use of \(R\) is the central coupling of the state system.

---

## 4. Exact represented survivor set

The positive starts represented by \(S\) are exactly

\[
\boxed{
\llbracket S\rrbracket
=
\{\rho(S)+2^k m:m\in\mathbb Z_{\ge0},\ \rho(S)+2^km\le\Theta\},
}
\]

with the upper condition omitted when \(\Theta=+\infty\).

Hence the state is nonempty iff

\[
\boxed{
\rho(S)\le\Theta
}
\]

or \(\Theta=+\infty\).

No starting integer is individually iterated to decide this filter.

---

## 5. Exact binary prefix transition

Extend the parity prefix by one bit

\[
p\in\{0,1\}.
\]

Then

\[
\boxed{k'=k+1,}
\]

\[
\boxed{q'=q+p,}
\]

and

\[
\boxed{
R'=3^pR+p2^k.
}
\]

This is the complete affine-prefix update.

If

\[
3^{q'}<2^{k'},
\]

the new contracting-prefix ceiling is

\[
\boxed{
C'=rac{R'}{2^{k'}-3^{q'}}.
}
\]

Update

\[
\boxed{
\Theta'=\min(\Theta,C')
}
\]

with the usual convention for \(+\infty\). If the new coefficient remains expanding, set

\[
\boxed{\Theta'=\Theta.}
\]

Then compute the child formation residue and floor from \((k',q',R')\). The child is retained exactly when

\[
\boxed{
\rho(k',q',R')\le\Theta'.
}
\]

This gives an exact closed binary state/filter transition on the four attributes \((k,q,R,\Theta)\).

---

## 6. Relation to the unresolved sets

Starting from the root

\[
\boxed{S_0=(0,0,0,+\infty),}
\]

apply both parity extensions at each depth and remove every child violating

\[
\rho\le\Theta.
\]

The represented sets of the retained states form a disjoint partition of

\[
\boxed{
U_k=\{n\ge2:T^j(n)\ge n\text{ for }1\le j\le k\}.
}
\]

Thus all positive starts are processed classwise by four exact attributes and one universal filter.

---

## 7. Why this is still not the final proof

Naively expanding both parity children produces a growing prefix tree. A valid Collatz proof cannot rely on enumerating that tree to increasing depth.

The remaining task is therefore a second abstraction:

> find a fixed quotient, potential, or monotone inequality on \((k,q,R,\Theta)\) that proves all infinite bounded-formation paths eventually violate \(\rho\le\Theta\), without expanding the parity tree prefix by prefix.

Equivalently, prove that the 2-adic formation projection of \(R\) and the Archimedean survival projection of \(R\) cannot remain compatible forever on a finite-natural-realizable path.

This is now the single main theorem target for the property-filter approach.

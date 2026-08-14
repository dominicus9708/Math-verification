# Primitive gate congruence and unification with the isolated R1 resonance

Date: 2026-08-14

Status: **exact arithmetic/continued-fraction reduction theorem**.  This identifies the currently isolated R1 resonance as one finite subgate of the same induced Euclidean rotation obtained from the R2 type-0 gate hierarchy.  It does not prove Collatz.

## 1. Residual gate coordinate

Put

\[
\alpha:=\log_3 2,
\qquad
\varepsilon:=12-19\alpha.
\]

The length-19 type-0 first-return construction renormalizes the mechanical phase by continued-fraction approximants to `epsilon`.

For any reduced rational approximation

\[
\frac pq\approx\varepsilon,
\qquad \gcd(p,q)=1,
\]

solve the affine relation `epsilon = 12 - 19 alpha` for `alpha`.  The corresponding rational approximation to `alpha` is

\[
\boxed{
\widetilde\alpha
=\frac{12q-p}{19q}.
}
\]

The associated time/odd-count gate vector before primitive reduction is therefore

\[
\boxed{
(L,H)=(19q,\ 12q-p).
}
\]

Its coefficient sign is controlled by the error of `p/q` relative to `epsilon`:

\[
H-\alpha L
=q\varepsilon-p.
\]

Hence

\[
\frac pq<\varepsilon
\Longleftrightarrow
\frac{3^H}{2^L}>1,
\]

and the opposite inequality gives a contracting gate.

## 2. Primitive reduction theorem

For reduced `p/q`,

\[
\gcd(12q-p,q)=\gcd(p,q)=1.
\]

Let

\[
g:=\gcd(12q-p,19q).
\]

Any prime dividing `g` and `q` would divide `p`, impossible.  Therefore `g` is coprime to `q`, and since `g|19q` we must have

\[
\boxed{
g\mid 19.}
\]

More precisely,

\[
\boxed{
\gcd(12q-p,19q)=\gcd(12q-p,19).
}
\]

Because `19` is prime, only two cases occur:

1. no collapse: `g=1`, leaving primitive denominator `19q`;
2. full gate collapse: `g=19`, leaving primitive denominator `q`.

The second case is equivalent to the one-digit congruence

\[
\boxed{
p\equiv12q\pmod{19}.}
\]

Thus the large induced return hierarchy carries an exact finite `mod 19` phase selecting which return vectors collapse to primitive time/odd-count pairs.

## 3. Semiconvergent runs

Let a continued-fraction semiconvergent family of `epsilon` be

\[
p_k=kp_1+p_0,
\qquad
q_k=kq_1+q_0.
\]

The primitive-collapse condition becomes

\[
\boxed{
(12q_1-p_1)k+(12q_0-p_0)
\equiv0\pmod{19}.
}
\]

It is linear in the local subgate index `k`.  If the increment is nonzero modulo 19, there is at most one solution modulo 19; in any partial-quotient run of length below 19 there is therefore at most one primitive-collapse subgate.

## 4. The current isolated R1 resonance

The epsilon continued-fraction hierarchy contains consecutive convergents

\[
\frac{235,984,999}{19,131,826,526},
\qquad
\frac{350,384,211}{28,406,424,013},
\]

followed by a partial quotient `13`.

Its 13 semiconvergents are

\[
p_k
=k\cdot350,384,211+235,984,999,
\]

\[
q_k
=k\cdot28,406,424,013+19,131,826,526,
\qquad 1\le k\le13.
\]

Modulo 19 the primitive numerator

\[
12q_k-p_k
\]

advances by `7` at every increment of `k`.  The unique zero in this run is

\[
\boxed{k=7.}
\]

At `k=7`,

\[
\boxed{
p_7=2,688,674,476,}
\]

\[
\boxed{
q_7=217,976,794,617.
}
\]

Moreover

\[
\boxed{
12q_7-p_7
=19\cdot137,528,045,312.
}
\]

Therefore the primitive gate vector is

\[
\boxed{
(A,H)
=(217,976,794,617,\ 137,528,045,312),
}
\]

exactly the currently isolated R1 first-crossing resonance.

Equivalently,

\[
\boxed{
\frac{12A-19H}{A}
=
\frac{2,688,674,476}{217,976,794,617}
}
\]

is the seventh semiconvergent in that induced gate run.

## 5. Structural interpretation

The R1 and R2 analyses are therefore not using unrelated continued fractions.

- R2 type-0 first return produces the epsilon hierarchy.
- Primitive gate vectors are selected inside that hierarchy by a finite congruence modulo 19.
- The sole presently isolated R1 resonance is the `k=7` primitive-collapse state inside one partial-quotient-13 gate.

Hence the huge R1 pair may be labeled by a finite renormalized state:

\[
\boxed{
(\text{epsilon CF level},\ a_{n}=13,\ k=7,\ \text{primitive-collapse mod }19).
}
\]

This replaces the interpretation of the resonance as an arbitrary enormous pair by a finite Euclidean/gate coordinate.

## 6. General version

The same argument works for any coprime rational reference `a/b` and residual

\[
\varepsilon=a-b\alpha.
\]

For a reduced `p/q`, the induced approximation is

\[
\frac{aq-p}{bq},
\]

and

\[
\boxed{
\gcd(aq-p,bq)=\gcd(aq-p,b).
}
\]

Thus primitive reductions of induced gates are controlled entirely by congruences modulo the reference denominator `b`.

This provides a natural modular phase coordinate to carry together with the Euclidean continued-fraction state at higher renormalization levels.

## 7. Proof-program consequence

The next useful target is no longer to analyze the isolated R1 pair with `H` individual odd events.  Its renormalized address is the finite state `partial quotient 13 / subgate 7 / mod-19 primitive collapse`.

The state-monoid, Hensel sibling-max, dyadic canonical-address and headroom channels should therefore be propagated on the induced gate hierarchy itself.  A contradiction at the finite `k=7` state would eliminate the current R1 resonance without expanding its full bit word.

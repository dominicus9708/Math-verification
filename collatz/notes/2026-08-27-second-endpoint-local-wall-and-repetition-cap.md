# Second-endpoint local wall and finite repetition cap

Date: 2026-08-27

Status: **SAFE LEMMA + exact rational certificate inside the repaired second-resonance branch.** The only external ingredient is the classical Legendre theorem for continued fractions. No ternary Cantor-core entry and no repeated-local pullback is used. This is not a proof of the Collatz conjecture.

## 1. Input state

From the repaired second-resonance gap theorem, let a current endpoint on the future orbit of a hypothetical minimal counterexample be

\[
X=N+d,
\qquad
N>2^{71},
\qquad
0\le d<7\cdot2^{33}.
\]

Every future orbit value is at least `N`.

Suppose `(j,q)` is the first coefficient-subcritical prefix from `X`:

\[
3^q<2^j.
\]

Every proper prefix is coefficient-surviving, so its affine correction satisfies

\[
R\le q3^{q-1}.
\]

Writing

\[
C=\frac{3^q}{2^j}<1,
\]

we obtain

\[
T^j(X)
\le
C\left(X+\frac q3\right).
\]

Minimal-counterexample no-descent requires

\[
T^j(X)\ge N=X-d.
\]

Hence necessarily

\[
\boxed{
1-C
\le
\frac{d+Cq/3}{X}
<
\frac{7\cdot2^{33}+q/3}{2^{71}}.
}
\]

This is the local near-survival wall appropriate to the second endpoint.

## 2. Diophantine constant falls below Legendre's threshold

Let

\[
\alpha=\log_3 2.
\]

For a subcritical pair put

\[
\delta=j\ln2-q\ln3>0.
\]

If the necessary inequality holds, then

\[
1-e^{-\delta}\le H,
\]

with

\[
H<\frac{7\cdot2^{33}+q/3}{2^{71}}.
\]

For

\[
j<J_0:=10439860591,
\]

we have

\[
q\le R_0:=6586818670.
\]

Thus a uniform exact rational bound gives

\[
\left|\alpha-\frac qj\right|
<\frac{K}{j^2},
\]

with

\[
\boxed{K<0.251<\frac12.}
\]

Therefore Legendre's theorem applies: after reducing `q/j`, the fraction must be a continued-fraction convergent of `alpha`.

This is stronger than the earlier Worley-type finite superset. The larger second-endpoint gap still leaves the approximation constant below the classical `1/2` threshold.

## 3. Complete lower-convergent audit below J0

The positive lower convergents before `R0/J0` are exactly

\[
\frac12,
\frac58,
\frac{41}{65},
\frac{306}{485},
\frac{15601}{24727},
\frac{79335}{125743},
\frac{190537}{301994},
\frac{10781274}{17087915},
\frac{171928773}{272500658},
\frac{397573379}{630138897}.
\]

A candidate `(q,j)` may be a positive multiple

\[
(q,j)=m(a,b)
\]

of one of these primitive convergents.

For one primitive lower convergent define

\[
D_0=b\ln2-a\ln3>0.
\]

Then

\[
1-e^{-mD_0}
\ge
\frac{mD_0}{1+mD_0}.
\]

Subtract the maximal second-endpoint allowance

\[
\frac{7\cdot2^{33}+ma/3}{2^{71}}.
\]

The resulting real function of `m` is concave. Therefore positivity at `m=1` and at

\[
m_{\max}=\left\lfloor\frac{J_0-1}{b}\right\rfloor
\]

proves positivity throughout the whole integer multiplicity range.

The exact rational certificate performs this check for all ten primitive lower convergents. Every range fails the necessary near-survival inequality.

Hence

\[
\boxed{
\text{no coefficient-subcritical prefix can occur for }1\le j<J_0.
}
\]

## 4. The first surviving local resonance

At

\[
(J_0,R_0)
=(10439860591,6586818670),
\]

the same necessary inequality is no longer contradictory.

Thus

\[
\boxed{
(J_0,R_0)
\text{ is the first possible local coefficient-subcritical pair.}
}
\]

In particular, every endpoint satisfying the common gap bound `d<7*2^33` coefficient-survives all proper prefixes before this depth.

## 5. One exact J0 crossing consumes a fixed additive gap

Assume the local crossing actually occurs at `(J0,R0)`.

Put

\[
\delta_0=J_0\ln2-R_0\ln3>0,
\qquad
C_0=e^{-\delta_0}<1.
\]

If

\[
X=N+d
\]

and

\[
X'=T^{J_0}(X)=N+d',
\]

then the correction bound gives

\[
d'
\le
C_0\left(d+\frac{R_0}{3}\right)
-(1-C_0)N.
\]

Using

\[
C_0<1,
\qquad
1-C_0
\ge
\frac{\delta_0}{1+\delta_0},
\qquad
N>2^{71},
\]

we obtain

\[
d'
<
d+rac{R_0}{3}
-2^{71}\frac{\delta_0}{1+\delta_0}.
\]

The exact logarithm certificate proves

\[
\boxed{
2^{71}\frac{\delta_0}{1+\delta_0}
-\frac{R_0}{3}
>rac52\,2^{33}.
}
\]

Therefore every actual local `J0/R0` crossing satisfies the strict gap loss

\[
\boxed{
d'<d-\frac52\,2^{33}.}
\]

This is a deterministic additive resource loss, not a density or average statement.

## 6. Same-resonance repetition cap

Starting from the second-resonance annulus

\[
d_0<7\cdot2^{33},
\]

one `J0/R0` crossing gives

\[
d_1
<
7\cdot2^{33}-\frac52\,2^{33}
=rac92\,2^{33}.
\]

A second gives

\[
d_2
<
\frac92\,2^{33}-\frac52\,2^{33}
=2\cdot2^{33}.
\]

A third would force

\[
d_3
<
2\cdot2^{33}-\frac52\,2^{33}<0,
\]

which is impossible because every future orbit value is at least `N`.

Hence

\[
\boxed{
\text{the local resonance }(J_0,R_0)
\text{ can occur at most twice consecutively.}
}
\]

After at most two such returns, the orbit must escape this local resonance scale by coefficient-surviving past `J0` or by entering a later admissible Diophantine scale.

## 7. DSD interpretation

The repaired proof line now has a finite-resource renewal mechanism:

\[
\boxed{
\text{near-root gap}
\longrightarrow
\text{continued-fraction wall}
\longrightarrow
\text{first admissible local resonance}
\longrightarrow
\text{strict gap debit}.
}
\]

The gap is not merely a descriptive endpoint variable. It is a monotone resource whenever the same lower resonance is reused.

This removes one possible pathology from the terminal branch: a hypothetical counterexample cannot remain forever near `N` by repeatedly recycling the same `10.44`-billion-step coefficient-subcritical block.

## 8. Audit classification

- **SAFE:** near-survival necessary inequality.
- **SAFE:** Legendre reduction with exact `K<1/2`.
- **SAFE:** complete multiplicity exclusion for all earlier lower convergents.
- **SAFE:** fixed additive gap debit at the first admissible local resonance.
- **SAFE:** at-most-two consecutive repetition theorem.
- **OPEN:** identify and exclude the later resonance scale forced after the repetition cap, or show that the branch coefficient-survives into a surplus-recovery regime.

Companion certificate:

`collatz/src/second_endpoint_local_wall_repetition_cap_certificate.py`

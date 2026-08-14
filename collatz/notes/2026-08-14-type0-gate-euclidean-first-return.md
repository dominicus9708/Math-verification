# Exact type-0 gate first return and Euclidean renormalization

Date: 2026-08-14

Status: **exact irrational-rotation first-return theorem + exact coefficient-sign certificates**.  This compresses the length-19 mechanical phase process to a two-letter 81/82 gate word and then to a 13/14 supergate word.  It is a structural renormalization theorem, not a Collatz proof.

## 1. Length-19 phase coordinate

Put

\[
\alpha:=\log_3 2\in(0,1),
\qquad
\varepsilon:=12-19\alpha.
\]

Since

\[
3^{12}>2^{19},
\]

we have

\[
\boxed{\varepsilon>0.}
\]

For the mechanical time word of slope `alpha`, a length-19 factor contains either 11 or 12 odd symbols.  In a standard rotation phase coordinate `x in [0,1)`, the 11-odd factor occurs on one interval of length

\[
\boxed{|I|=\varepsilon.}
\]

After translating the phase origin we may take

\[
\boxed{I=[0,\varepsilon).}
\]

Moving one length-19 block backward changes phase by

\[
-19\alpha\equiv\varepsilon\pmod1,
\]

because

\[
19\alpha=12-\varepsilon.
\]

Thus the predecessor-block phase dynamics is exactly

\[
\boxed{x\mapsto x+\varepsilon\pmod1.}
\]

The interval `I` is the type-0 / 11-odd gate.

## 2. Exact 81/82 return-time theorem

The rational inequalities

\[
\boxed{
\frac{971}{1539}<\alpha<\frac{983}{1558}
}
\]

are equivalent to the exact integer comparisons

\[
\boxed{3^{971}<2^{1539},}
\qquad
\boxed{3^{983}>2^{1558}.}
\]

They imply

\[
\boxed{81\varepsilon<1<82\varepsilon.}
\]

Define

\[
\delta:=1-81\varepsilon.
\]

Then

\[
0<\delta<\varepsilon.
\]

For every `1<=n<=80`,

\[
T^n(I)=[n\varepsilon,(n+1)\varepsilon)
\]

without circular wrap, so it is disjoint from `I`.  At time 81:

- points `x in [delta,epsilon)` return, because
  \[
  x+81\varepsilon\equiv x-\delta\in[0,\varepsilon-\delta);
  \]
- points `x in [0,delta)` do not yet return.

For those remaining points, time 82 gives

\[
x+82\varepsilon\equiv x+\varepsilon-\delta
\in[\varepsilon-\delta,\varepsilon),
\]

so they return then.

Therefore the first-return time to the type-0 gate is exactly

\[
\boxed{81\text{ or }82.}
\]

No other first-return time occurs.

## 3. Induced gate rotation

The first-return partition is

\[
\boxed{
I_{82}=[0,\delta),
\qquad
I_{81}=[\delta,\varepsilon).
}
\]

Both branches of the first-return map are the same modulo the interval length `epsilon`:

\[
\boxed{x\mapsto x-\delta\pmod\varepsilon.}
\]

After rescaling `I` to the unit circle, define

\[
\boxed{
\rho:=\frac{\delta}{\varepsilon}
=\frac1\varepsilon-81.
}
\]

Hence the induced dynamics is again an irrational rotation.  The 82-gate frequency is `rho`, while the 81-gate frequency is `1-rho`.

Numerically only for orientation,

\[
\varepsilon\approx0.0123346821423087,
\]

\[
\rho\approx0.0722147893815912.
\]

The exact theorem does not depend on these decimals.

## 4. Gate macroblock coefficient vectors

A length-19 ordinary mechanical block has 12 odd symbols, while the type-0 gate has 11.  Between two type-0 occurrences there is exactly one 11-odd block and all other length-19 blocks have 12 odds.

Thus the two first-return macroblocks have total time/odd-count vectors

\[
\boxed{
G_{81}:(L,q)
=(19\cdot81,\ 12\cdot81-1)
=(1539,971),
}
\]

\[
\boxed{
G_{82}:(L,q)
=(19\cdot82,\ 12\cdot82-1)
=(1558,983).
}
\]

Their mechanical coefficients lie on opposite sides of one:

\[
\boxed{
\frac{3^{971}}{2^{1539}}<1,
}
\]

\[
\boxed{
\frac{3^{983}}{2^{1558}}>1.
}
\]

Thus `G_81` is slightly contracting and `G_82` slightly expanding.

## 5. Second return: exact 13/14 theorem

The new slope satisfies

\[
\boxed{
\frac1{14}<\rho<\frac1{13}.
}
\]

Equivalently,

\[
13\rho<1<14\rho.
\]

In terms of `alpha` this is exactly

\[
\boxed{
\frac{13606}{21565}
<\alpha<
\frac{12635}{20026}
=rac{665}{1054}.
}
\]

The required exact power inequalities are

\[
\boxed{3^{13606}<2^{21565},}
\qquad
\boxed{3^{665}>2^{1054}.}
\]

Applying the same interval-return argument to the induced rotation shows that returns to the 82-gate interval occur after exactly

\[
\boxed{13\text{ or }14}
\]

first-level gates.

Put

\[
\rho_2:=\frac1\rho-13.
\]

Then the induced second-return rotation has slope `rho_2` up to the harmless orientation convention.  Numerically,

\[
\rho_2\approx0.847578987122515.
\]

## 6. Second-level macroblocks

A 13-gate return contains one `G_82` and twelve `G_81` blocks; a 14-gate return contains one `G_82` and thirteen `G_81` blocks.  Order/conjugacy matters for correction arithmetic, but not for the total `(L,q)` vector.

Therefore

\[
\boxed{
G_{13}:(L,q)
=(12\cdot1539+1558,\ 12\cdot971+983)
=(20026,12635),
}
\]

\[
\boxed{
G_{14}:(L,q)
=(13\cdot1539+1558,\ 13\cdot971+983)
=(21565,13606).
}
\]

The signs reverse:

\[
\boxed{
\frac{3^{12635}}{2^{20026}}>1,
}
\]

\[
\boxed{
\frac{3^{13606}}{2^{21565}}<1.
}
\]

Moreover

\[
\boxed{
\frac{12635}{20026}=\frac{665}{1054},
}
\]

and `665/1054` is a continued-fraction convergent of `log_3 2`.

Thus the gate renormalization has rediscovered the continued-fraction / Christoffel hierarchy from the length-19 phase process itself.

## 7. Exact drift formulas

Let

\[
\Delta(L,q):=q-\alpha L.
\]

From the definitions,

\[
\delta=1-81\varepsilon,
\qquad
\rho=\delta/\varepsilon.
\]

Then

\[
\boxed{
\Delta(G_{81})=-\delta,
}
\]

\[
\boxed{
\Delta(G_{82})=\varepsilon-\delta.
}
\]

At the next level,

\[
\boxed{
\Delta(G_{13})=\varepsilon-13\delta>0,
}
\]

\[
\boxed{
\Delta(G_{14})=\varepsilon-14\delta<0.
}
\]

Writing

\[
\rho_2=1/\rho-13
\]

gives

\[
\Delta(G_{13})=\delta\rho_2,
\]

\[
\Delta(G_{14})=-\delta(1-\rho_2).
\]

Hence the induced Sturmian frequencies cancel the two drifts exactly.  The coefficient-critical symbolic structure is therefore reproduced at the next scale rather than destroyed.

## 8. Continued-fraction interpretation

The first two exact Euclidean steps are

\[
\boxed{
\frac1\varepsilon=81+\rho,
}
\]

\[
\boxed{
\frac1\rho=13+\rho_2.
}
\]

Thus the continued fraction begins

\[
\boxed{
\varepsilon=[0;81,13,\ldots].
}
\]

Independent high-precision evaluation gives the diagnostic continuation

\[
[0;81,13,1,5,1,1,3,1,1,1,1,\ldots],
\]

but only the first two digits are used in the exact theorem above.

## 9. State-monoid lift

Let an actual realization of one deterministic gate macroblock differ from the mechanical block by the established relative state

\[
(\Sigma,M).
\]

The existing concatenation law remains exact:

\[
\Sigma_{UV}=\Sigma_U+\Sigma_V,
\]

\[
M_{UV}=\min(M_U,\Sigma_U+M_V).
\]

If the mechanical gate has odd count `q_*`, an actual realization with net relative count `Sigma` has coefficient

\[
\boxed{
\frac{3^{q_*+\Sigma}}{2^L}
=3^{\Sigma}\frac{3^{q_*}}{2^L}.
}
\]

Therefore the near-critical coefficient channel is isolated at `Sigma=0`.  A one-unit surplus or deficit changes the macroblock coefficient by an exact factor three, even though the mechanical coefficient itself may be arbitrarily close to one at high Euclidean levels.

This is the correct interface for attaching:

- survival state `(Sigma,M)`;
- Hensel sibling maxima / alternate-predecessor coverage;
- dyadic canonical-lift state;
- headroom/minimality-excess state.

## 10. Strategic consequence

The result is both a compression and a limitation.

It compresses the deterministic phase process

\[
20\text{ length-19 factor types}
\longrightarrow
\{81,82\}
\longrightarrow
\{13,14\}
\]

with no loss of mechanical coefficient information.

But coefficient signs alone continue to form a balanced Sturmian critical word at each induced scale.  Hence Euclidean renormalization by itself is not a contradiction theorem.

The useful next target is to propagate the **non-coefficient channels** across these very long return blocks.  In particular, the Hensel sibling-max and same-integer dyadic-address conditions can now be tested on a gate-to-gate macroblock instead of on thousands of individual time bits.

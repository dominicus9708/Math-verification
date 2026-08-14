# Gate-wide Hensel cubes at the 81/82 and 13/14 Euclidean scales

Date: 2026-08-14

Status: **exact constructive same-state difference-set theorem + exact integer power certificates**.  This lifts the earlier 57-bit `J=21/22` suffix cubes to the full first-return gates and then to the second-return supergates.  It is an arithmetic-freedom theorem, not a Collatz proof.

## 1. Mechanical prefix bound

Put

\[
\alpha:=\log_3 2.
\]

For every mechanical/Sturmian factor of slope `alpha`, the number `Q(t)` of odd symbols in any prefix of length `t` satisfies

\[
\boxed{Q(t)\le\lceil t\alpha\rceil.}
\]

Therefore an explicit binary word with prefix-one count `b(t)` lies weakly above every such mechanical prefix whenever

\[
\boxed{b(t)\ge\lceil t\alpha\rceil.}
\]

Because `b(t)` is an integer, this condition is exactly equivalent to the integer power comparison

\[
\boxed{3^{b(t)}\ge2^t.}
\]

Likewise

\[
b(t)\ge Q(t)-1
\]

is guaranteed by

\[
\boxed{3^{b(t)+1}\ge2^t.}
\]

No floating-point estimate is needed for the certificates below.

## 2. Generic front-loaded pair cube

Let a gate have time length `L` and mechanical odd count `q`, and put

\[
E:=L-q.
\]

### Neutral construction

Set

\[
J_0:=E-1,
\qquad
F_0:=q-J_0=2q-L+1.
\]

Consider the orientation family

\[
\boxed{
\mathcal C_0
=
1^{F_0}(01/10)^{J_0}0.
}
\]

Every vertex has length `L` and exactly `q` odd symbols.  Its prefix-minimal vertex is obtained by choosing `01` in every pair.

If the minimal vertex satisfies

\[
3^{b_0(t)}\ge2^t
\qquad(1\le t<L),
\]

then every vertex stays weakly above the mechanical prefix count.  At `t=L` the total odd count agrees exactly, so every vertex has

\[
\boxed{(\Sigma,M)=(0,0).}
\]

### One-slack construction

Now use one fewer actual odd symbol.  Set

\[
J_1:=E,
\qquad
F_1:=(q-1)-J_1=2q-L-1,
\]

and

\[
\boxed{
\mathcal C_{-1}
=
1^{F_1}(01/10)^{J_1}0.
}
\]

Every vertex has `q-1` odd symbols.  If its minimal vertex satisfies

\[
3^{b_1(t)+1}\ge2^t
\qquad(1\le t<L),
\]

then its relative height never falls below `-1`; at the endpoint the height is exactly `-1`. Hence

\[
\boxed{(\Sigma,M)=(-1,-1).}
\]

In both constructions, changing a pair from `01` to `10` only raises one intermediate prefix and returns to the same height one step later. Thus it can never violate the corresponding floor condition once the all-`01` vertex is certified.

## 3. Triangular correction basis

Within either cube, every variable pair contains exactly one odd event.  Number the actual odd events in increasing time order.

In the neutral cube the variable odd ranks are

\[
F_0+1,\ldots,q,
\]

and in the one-slack cube they are

\[
F_1+1,\ldots,q-1.
\]

For a pair whose odd event is rank `k` and whose left time position is `p`, switching

\[
01\longleftrightarrow10
\]

changes the affine correction by

\[
\boxed{
\Delta R=\pm3^{q_{\rm act}-k}2^p.
}
\]

Hence the `J` independent coordinates have exact 3-adic valuations

\[
\boxed{J-1,J-2,\ldots,0.}
\]

The coefficient after removing the displayed power of three is always a 3-adic unit.  Balanced-ternary triangular lifting therefore gives

\[
\boxed{
\mathcal C_0-\mathcal C_0
=
\mathbb Z/3^{J_0}\mathbb Z
}
\]

and

\[
\boxed{
\mathcal C_{-1}-\mathcal C_{-1}
=
\mathbb Z/3^{J_1}\mathbb Z.
}
\]

These are explicit difference-set identities, not density estimates.

## 4. First-return gate `G_81`

The exact first-return vector is

\[
\boxed{(L,q)=(1539,971).}
\]

Thus

\[
E=568.
\]

The two cubes are

\[
\boxed{
\mathcal C_0^{81}
=1^{404}(01/10)^{567}0,
}
\]

\[
\boxed{
\mathcal C_{-1}^{81}
=1^{402}(01/10)^{568}0.
}
\]

Exact integer comparison at every proper prefix verifies

\[
3^{b_0(t)}\ge2^t,
\]

\[
3^{b_1(t)+1}\ge2^t.
\]

Consequently

\[
\boxed{
\mathcal D_{81}^{(0)}
=
\mathbb Z/3^{567}\mathbb Z,
}
\]

\[
\boxed{
\mathcal D_{81}^{(-1)}
=
\mathbb Z/3^{568}\mathbb Z.
}
\]

## 5. First-return gate `G_82`

For

\[
\boxed{(L,q)=(1558,983),}
\]

we have

\[
E=575.
\]

The explicit cubes are

\[
\boxed{
1^{409}(01/10)^{574}0
}
\]

and

\[
\boxed{
1^{407}(01/10)^{575}0.
}
\]

The same exact prefix-power audit proves

\[
\boxed{
\mathcal D_{82}^{(0)}
=
\mathbb Z/3^{574}\mathbb Z,
}
\]

\[
\boxed{
\mathcal D_{82}^{(-1)}
=
\mathbb Z/3^{575}\mathbb Z.
}
\]

Thus the earlier 57-bit `J=21/22` construction was only a very small local portion of a gate-wide triangular cube.

## 6. Second-return supergate `G_13`

The expanding second-return vector is

\[
\boxed{(L,q)=(20026,12635),}
\]

so

\[
E=7391.
\]

Exact prefix-power checks give the neutral and one-slack dimensions

\[
\boxed{J_0=7390,}
\qquad
\boxed{J_1=7391.}
\]

Therefore

\[
\boxed{
\mathcal D_{13}^{(0)}
=
\mathbb Z/3^{7390}\mathbb Z,
}
\]

\[
\boxed{
\mathcal D_{13}^{(-1)}
=
\mathbb Z/3^{7391}\mathbb Z.
}
\]

## 7. Second-return supergate `G_14`

For the contracting vector

\[
\boxed{(L,q)=(21565,13606),}
\]

we have

\[
E=7959.
\]

The exact dimensions are

\[
\boxed{J_0=7958,}
\qquad
\boxed{J_1=7959,}
\]

and hence

\[
\boxed{
\mathcal D_{14}^{(0)}
=
\mathbb Z/3^{7958}\mathbb Z,
}
\]

\[
\boxed{
\mathcal D_{14}^{(-1)}
=
\mathbb Z/3^{7959}\mathbb Z.
}
\]

## 8. Relation to the synchronized Beatty clock

The cube dimension is controlled by the even budget

\[
E=L-q.
\]

This is the same resource that appears in the binary Hensel integerization criterion

\[
E\ge\lceil d\log_2(3/2)\rceil.
\]

Thus Euclidean phase renormalization and low-order 3-adic correction freedom are not separate phenomena.  At every gate scale, the number of explicit triangular Hensel coordinates grows linearly with the same even/odd budget dictated by the critical Beatty slope.

## 9. Proof-program consequence

At the first-return scale, a contradiction cannot depend only on a prescribed correction-difference target through hundreds of low ternary digits:

\[
J\le567\text{ or }574
\]

in the neutral fibre, and one digit more in the one-slack fibre.

At the next Euclidean scale the protected low-order freedom reaches several thousand ternary digits.

This is a strong negative result for a purely low-Hensel obstruction, but a positive structural result for renormalization: the low-order correction channel admits an explicit state-preserving basis whose dimension is known exactly at each certified gate vector.

Therefore any terminal boundary incompatibility must use information not captured by those low difference digits alone, such as

1. correction ordering / positivity for an actual smaller predecessor;
2. the fixed ordinary dyadic zero-lift fibre;
3. the early first-defect address channel;
4. the Archimedean renewal/headroom inequality;
5. higher 3-adic digits beyond the gate-wide cube;
6. compatibility of the cube orientation with the *same* ternary-Cantor start address.

The immediate next target is to couple the early six first-defect channels with the gate-wide cube while retaining the ordinary-start dyadic address, rather than to search for another low-order Hensel residue obstruction.
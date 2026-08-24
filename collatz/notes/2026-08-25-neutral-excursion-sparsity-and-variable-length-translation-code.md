# Neutral-excursion sparsity and variable-length translation code

Date: 2026-08-25

Status: **exact algebraic reduction using the harmonic budget plus the root-translation ultrametric theorem.**  This does not prove Collatz.  It shows that completed neutral excursions are necessarily sparse and that every hypothetical hard orbit contains arbitrarily long open-positive excursions.  It also identifies a prefix-free 2-adic code carried by each completed excursion.

## 1. Mechanical odd-event blocks

Let

\[
\gamma:=\log_2 3.
\]

The coefficient-critical mechanical valuation word is

\[
r_j^{\rm mech}
=\lfloor(j+1)\gamma\rfloor-\lfloor j\gamma\rfloor
\in\{1,2\}.
\]

Its time-expanded parity block `j` starts with an odd bit at

\[
\boxed{B_j:=\lfloor j\gamma\rfloor}
\]

and ends just before

\[
B_{j+1}=\lfloor(j+1)\gamma\rfloor.
\]

For an actual coefficient-surviving parity path, write the cumulative odd-event halving positions as

\[
A_i=\sum_{t<i}v_t,
\]

and

\[
\boxed{
\lambda_i:=\frac{2^{A_i}}{3^i}.
}
\]

The harmonic theorem gives

\[
\boxed{
\sum_{i<q}\lambda_i\le C_Nq^{1/9}
}
\]

for a hypothetical nonperiodic no-first-descent orbit from fixed positive integer `N`.

## 2. A completed positive excursion costs at least 1/3 of harmonic mass

Use the time-expanded relative odd-count height

\[
h(k)=q_{\rm actual}(k)-q_{\rm mech}(k)\ge0.
\]

A nontrivial positive excursion ends when `h` drops from a positive value to zero.  Such a final drop can occur only at a mechanical odd bit `B_j`, where the actual bit is zero.

Immediately after processing `B_j`, both words have exactly `j+1` odd symbols.  The next actual odd position is therefore `A_{j+1}`.

It must satisfy

\[
A_{j+1}\ge B_j+1.
\]

Coefficient survival through the next actual odd event gives

\[
A_{j+1}\le\lfloor(j+1)\gamma\rfloor=B_{j+1}.
\]

Hence

\[
B_j+1\le A_{j+1}\le B_{j+1}.
\]

Therefore

\[
A_{j+1}-(j+1)\gamma
\ge
\lfloor j\gamma\rfloor+1-(j+1)\gamma
=1-\gamma-\{j\gamma\}
> -\gamma.
\]

Since `2^gamma=3`,

\[
\boxed{
\lambda_{j+1}=2^{A_{j+1}-(j+1)\gamma}>2^{-\gamma}=\frac13.
}
\]

Thus every completed nontrivial neutral excursion consumes more than `1/3` of the global harmonic sum.

## 3. Excursion-count sparsity

Let `J(q)` be the number of completed nontrivial positive excursions whose associated odd-event index is below `q`.

Distinct completed excursions give distinct indices `j+1`, and each contributes a `lambda_i>1/3`.  Therefore

\[
\frac13J(q)
<\sum_{i<q}\lambda_i
\le C_Nq^{1/9}.
\]

Hence

\[
\boxed{
J(q)<3C_Nq^{1/9}.
}
\]

In particular the completed neutral-return count has zero density and the `r`th completed excursion can occur only at odd-event scale

\[
\boxed{q_r=\Omega_N(r^9).}
\]

This is the harmonic counterpart of the root-translation locking theorem.

## 4. Arbitrarily long open-positive excursions are unavoidable

There are two cases.

### 4.1 Finitely many neutral returns

After the last return, the relative height remains strictly positive forever.  Hence there is an infinite open-positive tail.

### 4.2 Infinitely many neutral returns

Among the first `q` odd events, at most `O_N(q^{1/9})` positive excursions are completed.  These excursions and the zero-height gaps partition a total time scale of order `q` in odd-event coordinates (and order `gamma q` in parity-time coordinates).

Therefore at least one open-positive excursion among the first `q` odd events has span

\[
\boxed{
\Omega_N(q^{8/9}).
}
\]

along an unbounded sequence of `q`.

Consequently every hypothetical hard orbit contains open-positive excursions of arbitrarily large length, whether or not neutral returns occur infinitely often.

This collapses the previous bookkeeping fork to one common asymptotic target:

\[
\boxed{
\text{locked same-integer entry state}
\longrightarrow
\text{arbitrarily long open-positive excursion}.
}
\]

## 5. Excursion translation as a prefix-free 2-adic code

Fix a mechanical prefix and a zero-height state at position `a`.  Consider the family of nontrivial positive excursions beginning at `a` and returning for the first time at positions `b>a`.

For one such excursion `e`, let `D_e` be its root-globalized canonical-start translation.  The ultrametric theorem gives

\[
\boxed{v_2(D_e)=a.}
\]

Define the normalized low-bit translation word

\[
\boxed{
c_e:=D_e/2^a\pmod{2^{b-a}}.}
\]

Its first low-order bit is necessarily `1`.

Now take two distinct excursions `e_1,e_2` with return lengths `b_1-a<=b_2-a`.  Suppose the longer translation code had the shorter one as a low-bit prefix:

\[
c_{e_2}\equiv c_{e_1}\pmod{2^{b_1-a}}.
\]

Adding back the common mechanical canonical residue implies equality of the two actual canonical start residues modulo `2^{b_1}`.  By the parity-prefix bijection, their actual parity prefixes of length `b_1` must then be identical.

But `e_1` has already returned to height zero at `b_1`, whereas `e_2`, whose first return is later, must still have positive height there.  Contradiction.

Hence the normalized translation words form a prefix-free family in the low-bit/2-adic direction.

Equivalently, the corresponding dyadic cylinders are disjoint.  Since every codeword begins in the odd normalized coset,

\[
\boxed{
\sum_e2^{-(b_e-a)}\le\frac12.
}
\]

This is a 2-adic Kraft inequality for neutral-excursion translations.

## 6. Why this matters for Stage 4

The earlier weighted-L2 to first-order conversion failed because a fixed-depth Cauchy estimate introduced the ambient factor `sqrt(2^H)`.

The excursion code supplies a different geometry: the relevant next-return translation cylinders are variable-length and prefix-free, hence disjoint before any first-order selector mass is summed.

For a selector probability measure `mu` and a prefix-free excursion family `F`, one may work with the multiscale cylinder energy

\[
\boxed{
\mathcal E_F(\mu)
:=\sum_{I\in F}\frac{\mu(I)^2}{|I|}.
}
\]

Cauchy on the disjoint cylinders gives

\[
\sum_{I\in F}\mu(I)
\le
\left(\sum_{I\in F}\frac{\mu(I)^2}{|I|}\right)^{1/2}
\left(\sum_{I\in F}|I|\right)^{1/2}
\le
\boxed{\sqrt{\mathcal E_F(\mu)/2}}.
\]

Thus the ambient `2^H` factor is replaced by the Kraft mass of the actual excursion family.

This does **not** yet close Stage 4: a usable theorem must still bound the selector's multiscale energy on these translated excursion cylinders.  But it gives a first-order-compatible target that respects both same-integer locking and variable return lengths.

## 7. Correct next target

The main open calculation is now:

\[
\boxed{
\text{bound the ternary-selector Carleson/multiscale energy
on long open-positive excursion translation cylinders.}
}
\]

This is preferable to multiplying finite-window densities or building a finite-height recurrent SCC.  The harmonic theorem guarantees arbitrarily long open excursions, while ultrametric locking guarantees that their entry translation is genuine same-integer information.

## 8. Finite regression

`collatz/src/neutral_excursion_harmonic_budget_regression.cpp`

exhaustively checks the first 28 mechanical bits.  Across the exact `3,524,586` coefficient-surviving words it checks `6,441,884` visible completed-excursion endpoints and verifies `lambda_i>1/3` in every case.  The smallest observed finite-window value is approximately

\[
0.3464394161>1/3.
\]

The finite calculation is only an implementation regression; Sections 2--5 are algebraic.

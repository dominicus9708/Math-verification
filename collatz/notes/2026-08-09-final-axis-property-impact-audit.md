# Impact audit: finalized realized-axis property axioms vs. Collatz calculation layer

Date: 2026-08-09

Status: **INTERFACE / SCOPE AUDIT; NO NUMERICAL COLLatz FORMULA CHANGED**

This note audits the current Collatz E/O, defect, min-plus, and matrix calculations against the finalized paper **Axioms for the Property Structure of Realized Axes in Dimensional-Structural Describability**. The finalized axis-property theory is explicitly a Stage-VI-based, non-dynamical, pre-aggregation extension. Therefore the required change is mainly a type/layer separation, not a replacement of the exact Collatz arithmetic.

## 1. Finalized dependency order

The correct project-level order is

\[
\boxed{
\text{Formation Stage VI}
\to
\text{optional realized-axis property extension}
\to
\text{analytic term realization / static aggregation}
\to
\text{Collatz affine / dynamic arithmetic}
}
\]

The axis-property layer factors through the Stage-VI formation record and is independent of post-Stage-VI term/composition coordinates. Therefore the static aggregation layer must not be treated as part of the primitive axis-property base.

## 2. Minimal Collatz axis-property extension

If the E/O bookkeeping plane is to be explicitly represented inside the finalized axis-property system, use one representational two-line carrier

\[
E^{\rm EO}=\mathbb R^2,
\qquad
\ell_E=\operatorname{span}(e_E),
\qquad
\ell_O=\operatorname{span}(e_O).
\]

For each inherited admitted Collatz channel selected as an axis channel, set

\[
\operatorname{AxLine}(c)=
\begin{cases}
\ell_E,&c\text{ is an even-step tag},\\
\ell_O,&c\text{ is an odd-step tag}.
\end{cases}
\]

Distinct step tags may realize the same E or O line; this is allowed by the finalized system. The carrier is bookkeeping/representational data and is not a physical two-dimensional space.

A minimal extension needs no bilinear, normal, closure, quaternion, or constitutive data:

- `K_bil = empty`;
- no bilinear-dependent property kind is declared;
- representation/closure/triadic/subspace option tags remain inactive unless independently needed.

Primitive PI is then the only substantive realization condition; PII is vacuous in this minimal Collatz use.

## 3. Optional unary coefficient property

If desired, declare a zero-free real-valued unary tag property `lambda_EO` by

\[
\Xi_{\lambda}(c)=
\begin{cases}
-\log 2,&c\text{ is E},\\
\log(3/2),&c\text{ is O}.
\end{cases}
\]

If all tags on the same realized E/O line receive the same value, line invariance is derived from the assignment; it is not a primitive declaration.

This property is optional. The exact Collatz arithmetic does not require it to be promoted into the axis-property signature.

## 4. Static aggregation should be downstream

Define a downstream analytic term map

\[
\Theta_{\rm EO}(c)=
\begin{cases}
(1,0)^T,&c\text{ is E},\\
(0,1)^T,&c\text{ is O}.
\end{cases}
\]

For a finite prefix `F_h`, static composition gives

\[
\mathbf c_h
=\sum_{c\in F_h}\Theta_{\rm EO}(c)
=\binom{e_h}{q_h}.
\]

With

\[
\lambda=\binom{-\log2}{\log(3/2)},
\]

the aggregate multiplicative drift is most economically written

\[
\boxed{
\Lambda_h=\lambda^T\mathbf c_h
=-e_h\log2+q_h\log(3/2)
}
\]

and

\[
e^{\Lambda_h}=3^{q_h}/2^h.
\]

The previously used diagonal matrix

\[
G=\operatorname{diag}(-\log2,\log(3/2))
\]

may be retained as a downstream analytic operator, but should no longer be described as an axis-property block unless an explicit unary/binary property block declaration satisfying the finalized typing rules is supplied.

The dot-product form `lambda^T c_h` is the cleaner default.

## 5. Two different 2x2 spaces must be separated

The finalized axis-property carrier and the exact Collatz affine homogeneous coordinate are different typed objects even if both are two dimensional.

### E/O bookkeeping carrier

\[
E^{\rm EO}=\operatorname{span}(e_E,e_O)
\]

records realized bookkeeping lines and optional static properties.

### Affine homogeneous state carrier

\[
H^{\rm aff}=\{(n,1)^T\}
\]

supports the exact branch operators

\[
M_E=\begin{pmatrix}1/2&0\\0&1\end{pmatrix},
\qquad
M_O=\begin{pmatrix}3/2&1/2\\0&1\end{pmatrix}.
\]

These matrices encode the Collatz map itself. They are not the property blocks of Section 7 of the finalized axis-property paper and should not be justified by Primitive PI/PII.

Thus the notation and prose should explicitly distinguish

\[
\boxed{E^{\rm EO}\neq H^{\rm aff}}
\]

as typed spaces, even if both are represented by `R^2` in code.

## 6. Order correction and defect channels remain downstream arithmetic

The exact correction

\[
R(w)=\sum_i2^{d_i}3^{q-1-i}
\]

and the affine identity

\[
T^h(n)=\frac{3^q n+R(w)}{2^h}
\]

are order-sensitive dynamical/arithmetic data. The finalized axis-property axioms explicitly do not supply temporal evolution, propagation, reorganization, or response laws.

Therefore the following current project objects should remain outside the primitive axis-property layer:

- parity order / correction cocycle `R(w)`;
- slack and defect coordinates `z_i`;
- canonical residue/carry states `(r,y)`;
- high-resolution defect residue `A`;
- min-plus/Bellman values `D,J`;
- interval and endpoint-progression certificates;
- affine/skew-product transition matrices.

They may consume typed channel/property data, but they are downstream derived mathematics.

## 7. Undefined is not zero: matrix caution

In the finalized property-block definition, an absent/undefined off-diagonal relation is represented as `undefined`, not numerical zero. Therefore one must not obtain a diagonal matrix such as `G` by silently replacing unspecified E/O cross-relations with zeros.

Either:

1. keep `G` purely as a downstream analytic diagonal operator; or
2. explicitly declare a zero-bearing binary relation and define the required cross entries to be zero.

For the Collatz program, option 1 is preferable because the binary relation contributes no proof content.

## 8. What does not need to change

No change is required to the exact arithmetic identities currently used in the Collatz branch, including

\[
T^h(n)=\frac{3^q n+R(w)}{2^h},
\]

the adjacent-swap correction ordering, canonical residue congruence, defect transfer, min-plus recurrence, two-channel successor Bellman recurrence, direct-sum factorization, and endpoint interval certificates.

These calculations are independent downstream mathematics. Their proofs do not rely on the stronger property claims excluded by the finalized axis-property scope.

## 9. Recommended revised front-end notation

Use four explicitly typed layers:

\[
\boxed{
\begin{array}{rcl}
\mathcal F_h&:&\text{formation-tagged E/O step channels},\\
\mathcal A_{\rm EO}&:&\text{optional realized-axis/property extension},\\
\mathbf c_h=(e_h,q_h)&:&\text{static aggregate count state},\\
\mathcal H_{\rm aff}&:&\text{exact affine Collatz state/dynamics}.
\end{array}}
\]

Then the working chain is

\[
\mathcal F_h
\to\mathcal A_{\rm EO}
\to\mathbf c_h
\to\Lambda_h
\quad\text{and independently}\quad
w\to R(w)\to M_w\to T^h(n).
\]

The two branches meet in the exact two-term identity

\[
\boxed{
T^h(n)=e^{\Lambda_h}n+\frac{R(w)}{2^h}.
}
\]

This preserves the original two-term intuition while respecting the finalized layer boundaries.

## 10. Audit conclusion

**Required revision: semantic/interface refactor only.**

- retain all exact Collatz formulas and certificates;
- retain the E/O count plane as a coarse analytic organization;
- move `G` explicitly to downstream analytic/static aggregation unless a typed property-block declaration is intentionally supplied;
- explicitly separate the E/O realized-axis carrier from the homogeneous affine state carrier;
- do not attribute `M_E`, `M_O`, `R`, defect, carry, Bellman, or min-plus dynamics to the axis-property axioms;
- use the finalized axis-property layer only when the retained typed distinction (tag vs line, property domain/status, optional unary property) is actually useful.

This yields a cleaner three-foundation interface: Formation controls admission and channel identity; the realized-axis property axioms optionally type the E/O bookkeeping carrier and properties; static aggregation realizes finite sums; standard Collatz arithmetic supplies the iterative affine dynamics.
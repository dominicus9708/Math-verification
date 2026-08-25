# Post-address selector mixing handoff

Date: 2026-08-26

Status: **exact structural handoff + finite Stage-4 diagnostic.** This note identifies where selector mixing ceases to be a meaningful intermediate theorem for a fixed ternary layer and must hand off to deterministic same-integer extinction. It is not a proof of the Collatz conjecture.

## 1. Address exposure theorem for a finite selector layer

For the recursively sufficient depth-\(m\) family

\[
\mathcal C_m
=\left\{
4\left(3^m+\sum_{i=0}^{m-1}a_i3^i\right)+3:
 a_i\in\{0,1\}
\right\},
\]

the layer maximum is

\[
N_{\max}(m)=6\,3^m+1.
\]

Define the full binary-address exposure depth

\[
\boxed{
K_{\rm addr}(m):=
\min\{K:N_{\max}(m)<2^K\}
=\operatorname{bitlength}(N_{\max}(m)).
}
\]

The parity-vector/canonical-residue correspondence is bijective modulo \(2^K\). Therefore, once \(K\ge K_{\rm addr}(m)\), a length-\(K\) canonical parity prefix can contain **at most one** integer of \(\mathcal C_m\).

Equivalently, conditional on an exact surviving canonical prefix beyond the exposure depth, the selector measure is either empty or a point mass.

For the current resonance layers,

\[
\boxed{K_{\rm addr}(44)=73,\qquad K_{\rm addr}(45)=74.}
\]

This is the measure-theoretic version of the finite-address deterministic-tail lemma: after the dyadic modulus exceeds the entire layer, there is no remaining selector-address branching.

## 2. Why uniform post-address mixing is the wrong target

Let \(P\) be an exact canonical past at depth \(K\ge K_{\rm addr}(m)\), and suppose it contains one selector integer \(N\). Let \(A\) be a future deterministic-language event.

Then

\[
\mu(A\mid P)
\in\{0,1\}.
\]

If the unique integer survives \(A\), then

\[
\boxed{
\mu(A\mid P)=1,
\qquad
\frac{\mu(A\mid P)}{\nu(A\mid P)}
=\frac1{\nu(A\mid P)}.
}
\]

Thus a theorem of the form

\[
\frac{\mu(A\mid P)}{\nu(A\mid P)}<K
\quad\text{for every post-address past }P
\]

is no longer a mixing theorem. Whenever \(\nu(A\mid P)<1/K\), it is logically equivalent to proving that **no selector singleton in that past survives \(A\)**.

This explains why fresh-window transversality cannot simply be iterated indefinitely at fixed \(m\): the conditional selector distribution ultimately becomes atomic by exact address exposure.

## 3. First complete strengthened Stage-4 window after exposure

Both \(m=44\) and \(m=45\) are fully exposed before binary depth 84. The first aligned full 28-step Stage-4 window beginning after both exposure depths is therefore

\[
\boxed{84\to112.}
\]

For the simultaneous L7+L14 residue-maximal two-state language \(z\in\{0,1\}\), exact enumeration at the genuine mechanical phase beginning at depth 84 gives

\[
\boxed{
M_{84}=
\begin{pmatrix}
89,202&228,029\\
331,500&861,043
\end{pmatrix}.
}
\]

Hence the unresolved low-to-low row masses are

\[
\boxed{
M_0=317,231,
\qquad
M_1=1,192,543.
}
\]

These are exactly the global minimum row masses used in the existing strengthened two-state certificate.

## 4. Singleton amplification at the handoff window

Under dyadic measure, after a fixed parity past the next 28 parity bits are uniform over \(2^{28}\) lifts. Therefore

\[
\nu(A_0\mid P)=\frac{317,231}{2^{28}},
\qquad
\nu(A_1\mid P)=\frac{1,192,543}{2^{28}}.
\]

For the existing strengthened branch allowance \(K=150\), the exact comparisons are

\[
150\cdot317,231
=47,584,650
<268,435,456=2^{28},
\]

\[
150\cdot1,192,543
=178,881,450
<268,435,456=2^{28}.
\]

Thus, if a fully exposed selector singleton survives the next unresolved window,

\[
\boxed{
K_{\rm singleton}(z=0)
=\frac{2^{28}}{317,231}
\approx846.183>150,
}
\]

\[
\boxed{
K_{\rm singleton}(z=1)
=\frac{2^{28}}{1,192,543}
\approx225.095>150.
}
\]

So at the first complete post-address window, the desired \(K<150\) statement cannot follow from residual selector mixing. It would force direct extinction of every selector singleton remaining in the relevant state.

## 5. Correct proof-program split

The same-address program should therefore be divided into three regimes.

### Regime A: pre-address transport

For

\[
K<K_{\rm addr}(m),
\]

many selector integers can occupy the same dyadic cylinder. Child-imbalance, Fourier-shell, matching, and spectral-complementarity arguments are meaningful here.

### Regime B: address handoff

At

\[
K\approx K_{\rm addr}(m),
\]

the selector fibres become singleton or empty. The relevant object is the exact finite intersection of the selector layer with the dangerous canonical frontier.

### Regime C: deterministic post-address tail

For

\[
K>K_{\rm addr}(m),
\]

no new selector-address choices exist. One must propagate the surviving fixed integers through deterministic Collatz dynamics, terminal maximality, or another exact descendant/endpoint compression. Generic selector equidistribution is no longer available or required.

## 6. Asymptotic size of the deterministic handoff interval

Since

\[
N_{\max}(m)=6\,3^m+1,
\]

we have

\[
\boxed{
K_{\rm addr}(m)
=m\log_2 3+O(1)
\approx1.584962501\,m+O(1).
}
\]

The previously proved whole-prefix root-safe horizon satisfies

\[
H_{\rm safe}(m)
\sim4.294473792\,m.
\]

Therefore the root-safe interval **after full selector-address exposure** has asymptotic length

\[
\boxed{
H_{\rm safe}(m)-K_{\rm addr}(m)
\sim2.709511291\,m.
}
\]

This is a substantial deterministic interval. It shows that the global proof architecture should not demand an all-horizon selector-mixing exponent on a fixed layer. The natural handoff is much earlier than the end of the available root-safe range.

## 7. Revised immediate target

For the fixed current layers, the next target is not another conditional-window mixing theorem. It is the exact or compressed evaluation of the selector intersection at address exposure and its deterministic descendants.

For \(m=45\), a useful first target is

\[
\boxed{
\mathcal C_{45}
\cap
\mathcal D_{74}
\longrightarrow
\mathcal D_{84}
\longrightarrow
\mathcal D_{112},
}
\]

where \(\mathcal D_K\) denotes the currently justified dangerous same-integer canonical frontier at depth \(K\), with all branch assumptions stated explicitly.

The objective is to prove emptiness or obtain a sharply compressed finite list before attempting further asymptotic transfer.

## 8. Audit consequence

- fresh-window selector transversality remains valid and useful before address exposure;
- uniform arbitrary-past transversality is too strong as a fixed-layer target after exposure;
- the support-size/Fourier barrier and finite-address theorem are two views of the same handoff;
- the next fixed-layer computation is a **finite cross-base intersection problem followed by deterministic propagation**, not a continued mixing problem;
- global uniform-in-\(m\) work should be reformulated around this moving address-exposure boundary.

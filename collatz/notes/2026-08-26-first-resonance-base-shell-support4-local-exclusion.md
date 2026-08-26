# First resonance: base-shell support-4 local exclusion

Date: 2026-08-26

Status: **exact finite certificate inside the repaired first-global-resonance branch.** This is not a proof of the Collatz conjecture.

## 1. Setup

Let \(d_j\) denote the mechanical displacement of the \(j\)-th odd state. The scaled-shell theorem gives

\[
2^{d_j}N<x_j<2^{d_j+1}N.
\]

Hence at a base-shell state \(d_0=0\),

\[
N<x_0<2N<\frac83 2^{71}<2^{73}.
\]

For the first-resonance mechanical gap sequence, take 49 consecutive odd states, hence 48 mechanical gaps. The rational mechanical slope has exactly 49 distinct anchored length-48 gap factors.

Suppose this 49-odd-state window has at most four positive displacement states:

\[
\#\{0\le j<49:d_j>0\}\le4,
\qquad d_0=0.
\]

Ordering gives

\[
d_{j+1}\le d_j+g_j-1,
\qquad g_j\in\{1,2\}.
\]

Starting from \(d_0=0\), support at most four therefore also bounds the displacement sizes and guarantees that the first 73 time-parity bits are exposed.

## 2. Exact finite quotient

The companion C++ certificate enumerates every admissible displacement path over every one of the 49 mechanical gap factors.

Exact counts:

\[
\boxed{1,767,989}
\]
raw admissible displacement paths,

\[
\boxed{1,246,024}
\]
distinct 73-bit parity words after deduplication.

Each 73-bit word has one canonical residue modulo \(2^{73}\). Since the broad base shell lies below \(2^{73}\), each word contributes at most one ordinary positive integer in

\[
2^{71}<x<\frac83 2^{71}.
\]

Exactly

\[
\boxed{518,937}
\]
canonical shell starts occur.

## 3. Exact descent scan

Every one of those 518,937 starts is iterated with the accelerated Collatz map

\[
T(x)=
\begin{cases}
x/2,&x\text{ even},\\
(3x+1)/2,&x\text{ odd}.
\end{cases}
\]

Every candidate reaches a value below \(2^{71}\).

The largest observed stopping depth in this complete finite quotient is

\[
\boxed{336}
\]
accelerated steps, attained at

\[
\boxed{5506931844860979677689}.
\]

Thus a hypothetical first-resonance minimal counterexample cannot contain such a local state.

## 4. Local forbidden-pattern theorem

Therefore:

\[
\boxed{
 d_i=0
 \Longrightarrow
 \#\{j\in[i,i+48]:d_j>0\}\ge5,
}
\]
whenever the full 49-odd-state block lies inside the first-resonance word.

Since \(d_i=0\), equivalently the following 48 odd states contain at least five positive shell displacements.

This is stronger than merely forbidding a long all-zero run.

## 5. DSD interpretation

The DSD proof chain here is

\[
\text{dyadic shell descriptor }d
\to
\text{finite mechanical factor quotient}
\to
\text{canonical formation residue}
\to
\text{finite descent certificate}
\to
\text{universal local forbidden pattern}.
\]

No infinite orbit enumeration is used: the enormous set of phases is quotiented to 49 mechanical factors and then to 1,246,024 finite parity words.

Companion certificate:

`collatz/src/first_resonance_base_shell_support4_local_certificate.cpp`.

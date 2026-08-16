# Scope correction: E=13 4096 pre-gate pullback obstruction

Date: 2026-08-16

Status: **scope clarification for the immediately preceding 4096 obstruction note/source**.

The exact `K<=28` terminal-residue over-family uses the previously certified maximal even-position bounds

\[
p_0\le72,\quad p_1\le186,\quad p_2\le365,\quad p_3\le647,\quad p_4\le1093.
\]

Those bounds were derived with the current numerical ceiling

\[
U_0\le N_{\max}+1,
\qquad
N_{\max}=6\cdot3^{44}+1.
\]

Therefore the precise theorem proved by

`collatz/src/r1_e13_4096_pullback_obstruction.cpp`

is

\[
\boxed{
\begin{gathered}
N,N'\le N_{\max},\\
e_{1539}(N)=e_{1539}(N')=13
\end{gathered}
\Longrightarrow
T^{1539}(N)-T^{1539}(N')\ne4096.
}
\]

More generally, the orientation/sign may be reversed, but no same-q `E=13` pair below the current ceiling realizes absolute entrance displacement `4096`.

The earlier prose phrase

> no pair of ordinary E=13 pre-gate paths

should therefore be read with the explicit current-size condition `N,N'<=N_max`.  It is not a theorem about arbitrarily large positive starting integers.

This restriction is sufficient for the intended minimal-counterexample predecessor use: the actual current R1 start satisfies `N<=N_max`, and any useful smaller ordinary predecessor satisfies `N'<N<=N_max` automatically.

The logical conclusion remains unchanged in the intended domain:

\[
\boxed{
\text{the specific G13 entrance credit }4096
\text{ cannot be pulled through the current E=13 pre-gate channel}
}
\]

as a same-q smaller-ordinary-predecessor relation.

This scope correction does not alter any residue count

\[
545,204,158,83,42,20,4,2,2,2,0
\]

for `K=18,...,28`.

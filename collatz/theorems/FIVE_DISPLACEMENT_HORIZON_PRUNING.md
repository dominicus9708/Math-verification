# Five-displacement horizon pruning

Status: **EXACT finite current-frontier theorem + SAFE endpoint use**.

Domain: the canonical `A0, s=1, Route-B` jump-8 source frontier after the certified first-75 and `eta_future>=1/3` cuts.

## 1. Bounded-displacement reachability

For future target ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` be the number of ranks among the first `r` future one-events with `d_k>0`.

Define

\[
H_4=\max\{r:\text{an exact source-preserving pure-ballot path with }D_r\le4\text{ exists}\}.
\]

A 32-shard exact decision at horizon 49 gives exactly two surviving source parents:

- one in shard 3;
- one in shard 24.

Every other shard is empty at horizon 49.

Exact continuation of the two exceptions gives

\[
\begin{aligned}
\text{shard 3:}&\quad \text{live}(49)=1,\quad \text{live}(50)=0,\\
\text{shard 24:}&\quad \text{live}(49)=1,\quad \text{live}(50)=1,\quad \text{live}(51)=0.
\end{aligned}
\]

Therefore

\[
\boxed{H_4=50}.
\]

Equivalently every horizon-51 survivor satisfies

\[
\boxed{D_{51}\ge5}.
\]

No source payload merging or linear extrapolation is used.

## 2. Normalized future defect

The already-certified target-phase bound gives, for every displaced target rank,

\[
\epsilon_r>\frac1{12}.
\]

Hence a horizon-51 survivor has

\[
\eta_{future}=\sum\epsilon_r
>5\cdot\frac1{12}
=\frac5{12}.
\]

Thus

\[
\boxed{\eta_{future}>\frac5{12}}.
\]

For monotone endpoint rejection it is safe to weaken this to

\[
\boxed{\eta_{future}\ge\frac5{12}}.
\]

This replaces the older `>=1/3` lower bound.  The two lower bounds are not added.

## 3. Exact endpoint consequence

Applying the `>=5/12` floor to the same first-75-tightened source intervals removes an additional

\[
\boxed{25{,}290{,}635}
\]

integers beyond the `>=1/3` frontier.

The canonical population becomes

\[
\boxed{26{,}859{,}837{,}368{,}480{,}843{,}030}.
\]

The number of source intervals remains `14,224`; no whole interval is removed.

The `>=5/12` cut affects `7,198` intervals relative to the uncut first-75 set.  Its cumulative removal from the first-75-tightened frontier is

\[
107{,}427{,}224.
\]

## 4. Scope

This is a finite theorem on the current canonical Route-B source frontier.  It proves neither an asymptotic displacement density nor Route-B closure.

The next bounded-displacement question is `c=5`; its result must again be obtained without extrapolating the sequence of finite horizons.

## Certificates

- `../src/A0_s1_8jump_c4_h49_shard_certificate.py`
- `../src/A0_s1_8jump_c4_exception_horizon_certificate.py`
- `../src/A0_s1_8jump_c4_displacement_horizon_shard.py`
- `../src/A0_s1_8jump_five_displacement_eta_pruning_certificate.py`
- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py`

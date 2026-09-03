# Six-displacement horizon pruning

Status: **EXACT finite current-frontier reachability result + SAFE endpoint use**.

Domain: the canonical `A0, s=1, Route-B` jump-8 source frontier after the certified first-75 and `eta_future>=5/12` cuts.

## 1. Exact c=5 horizon-51 decision

For future target ranks write

\[
u_k=t_{q+k}-d_k,
\qquad d_k\ge0,
\]

and let `D_r` be the number of ranks among the first `r` future one-events with `d_k>0`.

Define

\[
H_5=\max\{r:\text{an exact source-preserving pure-ballot path with }D_r\le5\text{ exists}\}.
\]

The exact 64-shard horizon-51 decision on all `14,224` current source parents gives

\[
\boxed{\#\{\text{parents admitting a }D_{51}\le5\text{ path}\}=0}.
\]

GitHub Actions run `33756884264` aggregates:

- `shard_count = 64`;
- `parent_count = 14224`;
- `parents_with_c5_path_h51 = 0`;
- `live_shard_count = 0`.

Therefore

\[
\boxed{H_5\le50}
\]

and every horizon-51 survivor satisfies

\[
\boxed{D_{51}\ge6}.
\]

This calculation does **not** establish `H_5=50`: equality would additionally require an exact `D<=5` witness at horizon 50 on the relevant pre-cut frontier.

No source payload merging, sampling, or horizon extrapolation is used.

## 2. Normalized future defect

The certified target-phase bound gives, for every displaced target rank,

\[
\epsilon_r>\frac1{12}.
\]

Hence any horizon-51 survivor has

\[
\eta_{future}=\sum\epsilon_r
>6\cdot\frac1{12}
=\frac12.
\]

Thus

\[
\boxed{\eta_{future}>\frac12}.
\]

For monotone endpoint rejection it is safe to weaken this to

\[
\boxed{\eta_{future}\ge\frac12}.
\]

This replaces the older `>=5/12` lower bound. The two floors are not added.

## 3. Exact endpoint consequence

Both the old `>=5/12` and new `>=1/2` cuts are recomputed from the same first-75-tightened source intervals.

The `>=1/2` floor removes an additional

\[
\boxed{25{,}304{,}566}
\]

integers beyond the `>=5/12` frontier.

The canonical population becomes

\[
\boxed{26{,}859{,}837{,}368{,}455{,}538{,}464}.
\]

The cumulative removal from the first-75-tightened frontier is

\[
132{,}731{,}790.
\]

The `>=1/2` cut affects `7,299` source intervals relative to the uncut first-75 set, but all `14,224` source intervals remain nonempty.

## 4. Scope and direction

This is a finite theorem on the current canonical Route-B frontier. It establishes an exact horizon-51 non-reachability statement for displacement budget five, not an asymptotic displacement law.

Because recent displacement-floor increments remove only about 25 million integers and still close zero whole source intervals, further `c` expansion should be compared against the independent source/checkpoint same-orbit obstruction before becoming the principal route.

## Certificates / evidence

- GitHub Actions run `33756884264` (`c=5`, horizon 51, 64 shards)
- `../src/A0_s1_8jump_c5_h51_shard_probe.py`
- `../src/A0_s1_8jump_six_displacement_eta_half_measurement.py`
- `../src/A0_s1_8jump_six_displacement_eta_half_pruning_certificate.py`
- `../src/A0_s1_8jump_cumulative_pruned_frontier_export.py`

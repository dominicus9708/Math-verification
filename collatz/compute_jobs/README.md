# GitHub Actions compute jobs for the Collatz proof program

This directory is the execution interface between the exact Collatz verifiers in `collatz/src/` and GitHub Actions.

The mathematical certificates and branch definitions remain in the source and notes.  GitHub Actions is used only as a durable, parallel execution layer for large finite exact computations.

## Why this exists

Large branch scans eventually exceeded the short interactive execution window even though each individual candidate usually reached coefficient contraction quickly.  The Actions workflow moves those flat finite scans out of the chat/runtime session and gives them:

- independent jobs per ternary branch;
- a much longer per-job execution window;
- reproducible compiler commands;
- persistent state/result artifacts;
- a machine-readable aggregate summary;
- exact continuation after one branch finishes without recomputing all other branches.

## Workflow

`.github/workflows/collatz-compute.yml`

Primary trigger on the working branch:

- a push that changes `collatz/compute_jobs/current.json`.

The workflow has three stages.

1. `prepare`
   - compiles `terminal_familyA_parallel_state_generator.cpp`;
   - generates the exact high-state file once;
   - compresses and uploads it as `prepared-states`.
2. `scan`
   - downloads the prepared state artifact;
   - runs `terminal_state_tau_scan.cpp` as a matrix over requested upper-four ternary codes;
   - uploads one exact text result per code.
3. `aggregate`
   - downloads all completed branch results;
   - writes `summary.json`;
   - reports total starts, survivors, overflow count, and the global maximum coefficient stopping time.

The matrix uses `fail-fast: false`: one long or failed branch does not discard completed branch certificates.

## Manifest schema

`current.json` has the following fields.

```json
{
  "name": "human-readable job name",
  "K": "geometry-specific terminal congruence constant",
  "R18": 0,
  "carry": 0,
  "zcap": 1000000,
  "c_start": "9191195087047038173556",
  "codes": [0, 1, 2, 3],
  "maxk": 1000,
  "state_threads": 4,
  "scan_threads": 4
}
```

Notes:

- `K` may be written as a JSON string or integer.  A string is recommended for consistency.
- `c_start` **must be a decimal string** because it exceeds the exact integer range of ordinary JSON/JavaScript numbers.
- `codes` contains upper-four ternary branch codes in `[0,15]`.  Omit it to scan all 16 codes.
- `maxk` is the exact coefficient-stopping search depth for the actual ordinary starts.
- `zcap` is a safe inherited-amplitude ceiling already established by the mathematical branch analysis.  It is not inferred by the workflow.
- the workflow does not upgrade a diagnostic bound into a theorem; the manifest must only contain already justified branch constants and safe ceilings.

## Result contract

Each branch result has the form

```text
count=<N> max_tau=<K> max_x=<X> survivors=<S> overflow=<O>
```

The aggregate artifact `summary.json` records:

- requested and completed codes;
- missing codes;
- total geometry-specific ordinary starts scanned;
- total survivors through `maxk`;
- 128-bit overflow count;
- global maximum `tau_c` and its maximizing start;
- the per-code rows.

A branch is excluded at the requested target depth only when the mathematical reduction says the scanned set is a safe superset and the corresponding computation returns `survivors=0` and `overflow=0` at a certified `maxk` that is sufficient for the intended exclusion.

## Artifact policy

Prepared high-state artifacts are retained for 7 days.  Per-branch results are retained for 30 days.  Aggregate summaries are retained for 90 days.

Large prepared state files are explicitly gzipped before upload.  The Actions artifact layer is used for transfer between jobs and durable result storage, not as a substitute for a mathematical certificate.

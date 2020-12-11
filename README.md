# Segfault with ddtrace profiling

We are seeing a segfault in certain scenarios when using profiling with our services that utilize pandas. This is a minimal reproduction that will result in a segfault during execution when profiling is enabled.

## Running

Run the `run.sh` script to run the example with profiling enabled to witness the segfault, you can then disable profiling by running `DD_PROFILING_ENABLED=false run.sh` which will demonstrate the segfault does not happen with profiling disabled.

The same behaviour is exhibited when using `ddtrace-run` but it was not used in this example so that it could be a single script reproduction of the issue.

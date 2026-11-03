# Hygon HCU / DTK Environment Validation Guide

## 1. When to Read This Guide
Before baseline measurement, compilation, graph capture, or model training on a new or changed Hygon HCU environment; also when diagnosing package defaults, memory allocation, asset paths, or connectivity problems.

## 2. Core Decisions & Rules

- **Device Allocation**: Inspect available `hy-smi`/`rocm-smi` output and memory queries. Record actual used/free memory for each allocated device. Container PID visibility may be incomplete; obtain host-side ownership if unexplained memory use remains. Zero utilization does not mean free.
- **Allocation Blockers**: If another task occupies required memory, report that allocation blocker. Do not kill unrelated processes or keep sleeping/retrying. Use another allocated device only when available to the task.
- **Local Assets**: Check local datasets and tokenizers before measurement. Offline environment variables do not create missing assets.
- **Runtime Defaults**: Record observed Inductor/Dynamo settings and package versions. Do not force every runtime to identical defaults without validation.
- **ATEN & GEMM**: ATEN is a conservative initial GEMM choice; hotspot backends must be compared by shape and dtype on actual HCU hardware.

## 3. Verification Commands

```bash
# Check device status
hy-smi

# Run HCU test suite
bash scripts/test_hcu.sh
```

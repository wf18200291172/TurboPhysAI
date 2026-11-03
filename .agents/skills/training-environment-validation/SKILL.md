---
name: training-environment-validation
description: Verify training environment setup, DTK/PyTorch compatibility, hardware allocation, and dependency conflicts on Hygon HCU hardware.
---

## When to use
- Setting up a new training node or container environment before baseline measurement or model training.
- Investigating dependency conflicts, missing Hygon/DTK libraries, or device allocation errors.

## When not to use
- For running ordinary code formatting checks or writing unit tests.

## Inputs expected
- Target host/container, intended GPU/DCU allocation, model/dataset paths, and framework version specs.

## Outputs required
- Environment check report, device/memory allocation status, dependency compatibility analysis, and critical/warning findings.

## Execution steps

1. **Run Environment Probe Script**
   ```bash
   python3 scripts/check_env.py --json --out env_report.json \
     --model-path model/ --dataset-path data/
   ```
   *(If `scripts/check_env.py` is not present, use standard py/torch inspection or verify via `pytest -m hcu test`)*

2. **Verify Hygon HCU / DTK & Device Allocation**
   ```bash
   hy-smi || rocm-smi
   python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available() if hasattr(torch, 'cuda') else 'NPU/DCU')"
   ```

3. **Check pytest HCU markers**
   ```bash
   bash scripts/test_hcu.sh
   ```

## Troubleshooting

### Error: "Device allocation failed / Out of memory"
- **Cause**: Another task is occupying HCU/DCU memory.
- **Check**: Run `hy-smi` to inspect actual used/free memory for each device.
- **Fix**: Select a free device or wait for existing training tasks to complete. Do not kill unrelated processes.

### Error: "DTK library not found or version mismatch"
- **Cause**: DTK software stack is not properly loaded in PATH or LD_LIBRARY_PATH.
- **Check**: Verify environment variables and DTK installation path.
- **Fix**: Source the DTK initialization script (e.g., `source /opt/dtk/env.sh`).

## References
- [GUIDE.md](GUIDE.md) — Detailed environment probe and decision guide.
- [Installation Guide](../../../docs/zh/get_started/installation.md)
- [Troubleshooting Guide](../../../docs/zh/user_guide/troubleshooting.md)

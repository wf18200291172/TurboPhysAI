# HCU Adaptation Guide for TurboPhysAI Skills

When reusing reference repositories (hygonpilot-skills, MindIE-SD, DrivingSDK), ensure comprehensive TurboPhysAI/HCU adaptation across these six dimensions.

---

## 1. Hardware & Runtime Layer

- [ ] Replace Ascend/Atlas references with Hygon HCU terminology
- [ ] Update device detection: `hy-smi` command instead of `rocm-smi`
- [ ] Adapt kernel/memory allocation to HCU memory hierarchy
- [ ] Map ATEN/GEMM optimization parameters to DTK equivalents

---

## 2. Software Stack Adaptation

- [ ] DTK version specifications (e.g., 26.04, 25.04)
- [ ] PyTorch/ROCm → PyTorch+DTK stack
- [ ] Container base images (DTK Docker image repositories)
- [ ] Python 3.10 compatibility with DTK libraries

---

## 3. Performance & Profiling

- [ ] DTK profiler tools (trace collection, timeline analysis)
- [ ] Replace Ascend-specific profiling commands with DTK equivalents
- [ ] HCU memory bandwidth/latency characteristics
- [ ] Operator-level optimization tuning for HCU architecture

---

## 4. Testing & Validation

- [ ] HCU device availability detection (@pytest.mark.hcu)
- [ ] DTK library dependency checks
- [ ] HCU-specific numerical accuracy tolerances (fp16 vs fp32)
- [ ] Multi-HCU distributed training considerations (AllReduce, collective ops)

---

## 5. Documentation & Examples

- [ ] Replace Ascend model references with TurboPhysAI models
- [ ] Update installation paths: `/opt/hygon/` vs `/opt/ascend/`
- [ ] Container execution examples for HCU environment
- [ ] DTK-specific compilation flags and environment variables

---

## 6. Verification Checklist

- [ ] Run `python3 scripts/agent/validate_skills.py --root .agents/skills`
- [ ] Pass `python3 scripts/check_docs.py` (no hardcoded paths/internal IPs)
- [ ] Pass `python3 scripts/agent/check_commit_compliance.py`
- [ ] Test on actual HCU hardware or HCU-enabled CI environment

# DTK Performance Analysis & Validation Guide

## 1. When to Read This Guide
When analyzing operator-level runtime bottlenecks, measuring optimization speedup on Hygon HCU, or investigating latency and throughput regressions.

Reference docs: [Performance Report Format](../../../docs/zh/user_guide/report.md)

## 2. Profiling Workflow

### Step 1: Enable DTK Trace Collection
```bash
export DTK_ENABLE_TRACE=1
python scripts/test_hcu.sh  # or your benchmark script
```

### Step 2: Analyze Trace with hipprof / DTK Tools
```bash
hipprof trace.json --output analysis.html
```

### Step 3: Identify Hotspots & Compare Baseline
- Kernel time dominance (>80% warmed stage)
- Operator attribution using critical path analysis
- Memory bandwidth saturation detection

## 3. Baseline & Regression Threshold
- **Acceptable regression**: < 3% wall-clock time variance
- **Red flag speedup**: >1.5x without code changes (validation needed)

## 4. Decision Tree
```
Is latency > baseline?
├─ YES → Check kernel time ↓ 
│        └─ Yes: Memory bound / schedule bottleneck
│        └─ No: Host overhead (Python, CPU copies)
└─ NO → Speedup confirmed ✓
```

## 5. Common Issues & Fixes

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| Missing trace file | DTK_ENABLE_TRACE not set or trace too large | Enable env var, split by batch size |
| All kernels in one category | Operator fusion, not granular | Check graph optimization level |
| Huge memory BW but low utilization | Memory copies, not computation | Profile with rocprof or hipprof --memory |
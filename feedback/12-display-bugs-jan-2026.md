# Display Bugs - January 2026

**Date:** 2026-01-11
**Type:** Bug Report
**Priority:** 🟡 Medium
**Status:** Identified

---

## Summary

Two display issues identified in the `ralf-notes generate` command output:
1. **Skipped Files Explanation** - Working correctly but needs clarification
2. **Time/Speed Display Bug** - Shows 0.0s and 0.0 files/s (incorrect)

---

## Issue 1: Skipped Files (320) - ✅ NOT A BUG

### User Observation
```
⏭️  Skipped: 320
```

### Root Cause Analysis

**Location:** `ralf_notes/core/file_processor.py:108-114`

```python
if target_path.exists() and not overwrite:
    if console:
        console.warning(f"Skipping {file_path.name} (output already exists. Use --overwrite to replace.)")
    results['skipped'] += 1
    if progress and task_id is not None:
        progress.update(task_id, advance=1)
    continue
```

**Explanation:**
- Files are skipped if output already exists AND `--overwrite` flag not used
- This is **correct behavior** - protects existing documentation
- 320 files already had generated outputs

### Solution
✅ **No code fix needed** - Working as designed

**Recommendation:** Add to user guide explaining skip behavior and `--overwrite` flag

---

## Issue 2: Time and Speed Display Bug 🔴 ACTUAL BUG

### User Observation
```
Time: 0.0s
Speed: 0.0 files/s
```

### Root Cause Analysis

The `generate` command runs 3 stages, each creating its own results dict without timing:

#### Stage 1: Raw Generation (`_generate_raw_logic`)
**Location:** `ralf_notes/cli.py:337-338`

```python
results = {
    'total': processed_count + failed_count,
    'success': processed_count,
    'failed': failed_count,
    'dry_run': False,
    'duration': 0,  # ❌ HARDCODED
    'files_per_second': 0  # ❌ HARDCODED
}
```

**Issue:** No time tracking, values hardcoded to 0

#### Stage 2: Initial Formatting (`_format_initial_logic`)
**Location:** `ralf_notes/cli.py:428-434`

```python
results = {
    'total': processed_count + failed_count + skipped_count,
    'success': processed_count,
    'failed': failed_count,
    'skipped': skipped_count,
    'dry_run': dry_run
    # ❌ MISSING: duration and files_per_second
}
```

**Issue:** No timing fields at all

#### Stage 3: Finalization (`_finalize_logic`)
**Location:** `ralf_notes/cli.py` (similar issue)

**Issue:** No timing tracked

### Correct Implementation Example

**Reference:** `file_processor.py:141-143` (works correctly)

```python
import time
start_time = time.time()

# ... processing loop ...

duration = time.time() - start_time
results['duration'] = duration
results['files_per_second'] = results['total'] / duration if duration > 0 else 0
```

---

## Fix Required

### Files to Update

| File | Function | Lines | Change |
|------|----------|-------|--------|
| `ralf_notes/cli.py` | `_generate_raw_logic()` | 292, 337-338 | Add timing |
| `ralf_notes/cli.py` | `_format_initial_logic()` | 385, 428-434 | Add timing |
| `ralf_notes/cli.py` | `_finalize_logic()` | ~474, results dict | Add timing |

### Implementation

For each of the three stage functions:

```python
def _stage_function(...):
    import time
    start_time = time.time()  # ADD at start of processing

    # ... existing code ...
    processed_count = 0
    failed_count = 0
    skipped_count = 0

    # ... processing loop ...

    duration = time.time() - start_time  # ADD before results dict

    results = {
        'total': processed_count + failed_count + skipped_count,
        'success': processed_count,
        'failed': failed_count,
        'skipped': skipped_count,
        'dry_run': dry_run,
        'duration': duration,  # ADD
        'files_per_second': processed_count / duration if duration > 0 else 0  # ADD
    }
```

**Note:** Use `processed_count` (not `total`) for files_per_second to match actual work done

---

## Expected Output After Fix

### Before (Current)
```
╭───────────────────────────────── 📊 Results ─────────────────────────────────╮
│                                                                              │
│ Total Files: 782                                                             │
│ ✅ Success: 462                                                              │
│ ❌ Failed: 0                                                                 │
│ ⏭️  Skipped: 320                                                              │
│                                                                              │
│ Time: 0.0s           ← BUG
│ Speed: 0.0 files/s   ← BUG
╰──────────────────────────────────────────────────────────────────────────────╯
```

### After (Fixed)
```
╭───────────────────────────────── 📊 Results ─────────────────────────────────╮
│                                                                              │
│ Total Files: 782                                                             │
│ ✅ Success: 462                                                              │
│ ❌ Failed: 0                                                                 │
│ ⏭️  Skipped: 320                                                              │
│                                                                              │
│ Time: 125.4s         ← FIXED
│ Speed: 3.7 files/s   ← FIXED (462 / 125.4s)
╰──────────────────────────────────────────────────────────────────────────────╯
```

---

## Testing Plan

### Test Case 1: Stage 1 Only
```bash
ralf-notes generate-raw ~/code/project
```

**Expected:** Duration and speed shown for raw generation

### Test Case 2: Stage 2 Only
```bash
ralf-notes format-initial ~/stage1_raw
```

**Expected:** Duration and speed shown for formatting

### Test Case 3: Full Pipeline
```bash
ralf-notes generate ~/code/project
```

**Expected:**
- Each stage shows its own timing
- Final summary shows total pipeline time (all 3 stages)

### Test Case 4: Large Batch
```bash
ralf-notes generate ~/large-codebase --overwrite
```

**Expected:**
- Accurate timing for 100+ files
- Speed calculation correct (files/second)

---

## Priority

**Priority:** 🟡 Medium

**Rationale:**
- Not blocking functionality
- Users can still process files
- But provides poor user experience (no progress feedback)
- Important for understanding performance

**Recommendation:** Fix in Phase 6 along with other bugs

---

## Related Issues

### From Code Review (feedback/11-code-review-jan-2026.md)
- Schema-parser mismatch (critical)
- Config propagation (critical)
- 6 medium priority issues

**Suggestion:** Fix all display/UX issues together in Phase 6.2

---

## Verification

### After Fix, Verify

- [ ] `generate` command shows correct timing
- [ ] `generate-raw` command shows correct timing
- [ ] `format-initial` command shows correct timing
- [ ] `finalize` command shows correct timing
- [ ] Speed calculation accurate (success / duration)
- [ ] Duration > 0 for all non-empty runs
- [ ] Dry-run still shows timing
- [ ] Multiple stages show cumulative time

---

## Documentation Updates Needed

### User Guide
- Explain `--overwrite` flag and skip behavior
- Document expected timing output
- Add performance benchmarks

### Developer Guide
- Document timing implementation pattern
- Add to testing checklist

---

## Conclusion

**Status:** 2 issues identified

1. ✅ **Skipped files** - Not a bug, working correctly
2. 🔴 **Time/Speed display** - Actual bug, needs fix

**Impact:** Medium - UX issue, not blocking

**Estimate:** 30 minutes to fix all 3 stage functions

**Recommendation:** Include in Phase 6.2 (UX improvements)

---

**Document Version:** 1.0
**Date:** 2026-01-11
**Reporter:** User
**Analyst:** Code Review Session

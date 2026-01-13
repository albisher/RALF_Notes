# CLI Structure Issues - January 2026

**Date:** 2026-01-11
**Type:** Design Review & Issues
**Priority:** 🟡 Medium
**Status:** Identified

---

## Summary

After user feedback from first run, identified 4 CLI structure issues:

1. 🔴 **Missing Command:** `fine-tune` command disappeared
2. 🟡 **Naming Inconsistency:** `check-health` should be `health-check`
3. 🟡 **Command Structure:** Stage commands should be options, not separate commands
4. ⚪ **Unclear Options:** `--show-completion` and `--install-completion` purpose unclear

---

## Issue 1: Missing `fine-tune` Command 🔴

### Problem

**User Report:** "auto fine tune commands disappeared!"

**Current Status:**
```bash
ralf-notes --help
# Shows: init, watch, generate, generate-raw, format-initial,
#        finalize, check-health, tags
# ❌ NO fine-tune command
```

**Expected Command:**
```bash
ralf-notes fine-tune [--quick | --full]
```

### Root Cause

The auto-tuning system was designed in `roadmap/06-auto-tuning-system.md` but **never implemented** in CLI.

**Design Document Shows:**
- Complete auto-tuning architecture
- 7 boxes (Orchestrator, Profiler, Benchmarker, etc.)
- CLI specification: `ralf-notes fine-tune`
- But code never added to `cli.py`

### Impact

- 🔴 **HIGH** - Core enhancement feature missing
- User expectation not met
- Auto-tuning system (70% complete in backend) not accessible

### Fix Required

**Add to `cli.py`:**

```python
@app.command(name="fine-tune")
def fine_tune(
    mode: str = typer.Option("quick", "--mode", "-m", help="Benchmark mode: 'quick' or 'full'"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output config file"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
):
    """
    Auto-tune RALF Note configuration for optimal performance.

    Runs benchmarks and generates optimized configuration.
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    # Show banner
    if not quiet:
        console.banner(get_banner('simple'))
        console.print("")
        console.info(f"🔧 RALF Note Auto-Tuning ({mode} mode)")
        console.print("")

    try:
        # Initialize components
        profiler = SystemProfiler()
        # ... rest of fine-tune logic from 06-auto-tuning-system.md

    except Exception as e:
        console.error(f"Auto-tuning failed: {e}")
        raise typer.Exit(1)
```

**Files to Update:**
- `ralf_notes/cli.py` - Add `fine_tune()` command
- Import tuning components (already imported at top)
- Wire up orchestrator logic

**Testing:**
- `ralf-notes fine-tune --help`
- `ralf-notes fine-tune --mode quick`
- `ralf-notes fine-tune --mode full`

**Priority:** HIGH (Phase 7)

**Estimate:** 2-3 hours (wiring + testing)

---

## Issue 2: Command Naming - `check-health` vs `health-check` 🟡

### Problem

**User Report:** "health check needs to be health-check not the other way around"

**Current Implementation:**
```python
@app.command()
def check_health():
    """Checks the health of the RALF Note system..."""
```

**Current Usage:**
```bash
ralf-notes check-health  # ❌ Feels backwards
```

**Preferred Naming:**
```bash
ralf-notes health-check  # ✅ More natural (noun-verb)
```

### Rationale

**Standard CLI Conventions:**
- `health-check` follows pattern of other commands
- Noun-first is more common in CLI design
- Matches: `fine-tune`, `generate-raw`, etc.

**Examples from Other Tools:**
```bash
docker health-check    # Not check-health
k8s health-check       # Not check-health
terraform health-check # Not check-health
```

### Fix Required

**Change Command Name:**

```python
@app.command(name="health-check")
def health_check():
    """Checks the health of the RALF Note system..."""
    # ... existing code ...
```

**Note:** Function name changed to `health_check` (Python naming convention)
**Command name:** `health-check` (CLI convention)

**Files to Update:**
- `ralf_notes/cli.py:961` - Change command name and function

**Testing:**
- `ralf-notes health-check` works
- `ralf-notes check-health` shows error

**Breaking Change:** YES - users using `check-health` will need to update

**Mitigation:** Document in changelog, show helpful error

**Priority:** MEDIUM (Phase 6)

**Estimate:** 10 minutes

---

## Issue 3: Stage Commands Should Be Options 🟡

### Problem

**User Report:** "stage1, stage2, stage3 should be more like options for generate if used then the app knows what to do"

**Current Structure:**
```bash
ralf-notes generate         # All 3 stages
ralf-notes generate-raw     # Stage 1 only
ralf-notes format-initial   # Stage 2 only
ralf-notes finalize         # Stage 3 only
```

**Proposed Structure:**
```bash
ralf-notes generate              # All 3 stages (default)
ralf-notes generate --stage 1    # Stage 1 only
ralf-notes generate --stage 2    # Stage 2 only
ralf-notes generate --stage 3    # Stage 3 only
ralf-notes generate --stage 1,2  # Stages 1 and 2
```

### Rationale

**Advantages:**
1. ✅ Cleaner command structure (fewer top-level commands)
2. ✅ More intuitive (generate with stage control)
3. ✅ Easier to remember (one main command)
4. ✅ Matches user mental model

**Disadvantages:**
1. ⚠️ Breaking change for existing users
2. ⚠️ More complex option parsing
3. ⚠️ Need to validate stage combinations

### Proposed Implementation

```python
@app.command()
def generate(
    source_path: Optional[Path] = typer.Argument(None, help="Source path to process"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output directory"),
    stages: Optional[str] = typer.Option(None, "--stage", "-s",
                                         help="Stages to run: 1, 2, 3, or combinations (1,2 or 2,3). Default: all stages."),
    raw_output: Optional[Path] = typer.Option(None, "--raw-output", help="Stage 1 output directory"),
    formatted_output: Optional[Path] = typer.Option(None, "--formatted-output", help="Stage 2 output directory"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview without writing"),
    overwrite: bool = typer.Option(False, "--overwrite", help="Overwrite existing files"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Minimal output"),
    model: Optional[str] = typer.Option(None, "--model", "-m", help="Override model name"),
):
    """
    Generate Obsidian documentation from source files.

    By default, runs all 3 stages. Use --stage to run specific stages:
      --stage 1      Generate raw LLM output
      --stage 2      Format raw output to markdown
      --stage 3      Finalize and validate
      --stage 1,2    Run stages 1 and 2
    """
    console = Console(quiet=quiet)
    config_manager = ConfigManager()

    # Parse stages option
    if stages is None:
        run_stages = [1, 2, 3]  # Default: all stages
    else:
        try:
            run_stages = [int(s.strip()) for s in stages.split(',')]
            if not all(1 <= s <= 3 for s in run_stages):
                console.error("Invalid stage number. Must be 1, 2, or 3.")
                raise typer.Exit(1)
        except ValueError:
            console.error("Invalid stage format. Use: 1, 2, 3, or combinations like 1,2")
            raise typer.Exit(1)

    # Run requested stages
    if 1 in run_stages:
        console.info("[bold green]--- Stage 1: Raw Content Generation ---[/bold green]")
        # ... stage 1 logic ...

    if 2 in run_stages:
        console.info("[bold green]--- Stage 2: Initial Formatting ---[/bold green]")
        # ... stage 2 logic ...

    if 3 in run_stages:
        console.info("[bold green]--- Stage 3: Finalization ---[/bold green]")
        # ... stage 3 logic ...
```

### Backwards Compatibility

**Option 1: Keep old commands as aliases (deprecated)**
```python
@app.command(name="generate-raw", deprecated=True, hidden=True)
def generate_raw_deprecated():
    """Deprecated. Use: ralf-notes generate --stage 1"""
    console.error("⚠️  This command is deprecated. Use: ralf-notes generate --stage 1")
    raise typer.Exit(1)
```

**Option 2: Remove old commands, document migration**
- Cleaner approach
- Document in CHANGELOG
- Provide migration guide

### Migration Path

**Version 2.1:**
- Add `--stage` option to generate
- Mark old commands as deprecated
- Show migration warnings

**Version 2.2:**
- Remove old commands
- Update all documentation

### Files to Update
- `ralf_notes/cli.py` - Refactor generate command
- Add stage parsing logic
- Optionally deprecate old commands
- Update tests
- Update documentation

**Priority:** MEDIUM (Phase 7 or 8)

**Estimate:** 4-6 hours (refactoring + testing)

**Decision Required:** Backwards compatibility approach?

---

## Issue 4: Unclear Completion Options ⚪

### Problem

**User Report:** "options --show-completion --install-completion are not clear as their need .. research what is best to keep them or remove them"

**Current Behavior:**
```bash
ralf-notes --show-completion
# Shows shell completion script

ralf-notes --install-completion
# Installs completion for current shell
```

### What Are These?

**Source:** Typer's automatic shell completion feature

**Enabled by:**
```python
app = typer.Typer(
    name="ralf-notes",
    help="...",
    add_completion=True  # ← This adds the options
)
```

### Purpose

**Shell Completion** allows:
```bash
ralf-notes ge<TAB>      → ralf-notes generate
ralf-notes generate --<TAB>  → shows all options
ralf-notes tags an<TAB>      → ralf-notes tags analyze
```

**Benefits:**
- ✅ Faster typing
- ✅ Discover commands
- ✅ Reduce typos
- ✅ Professional CLI experience

### Research: Other CLI Tools

**Tools WITH completion options:**
```bash
docker --install-completion     # ✅ Has it
kubectl completion bash         # ✅ Has it (different syntax)
gh completion -h                # ✅ Has it
pip completion --bash           # ✅ Has it
```

**Tools WITHOUT visible completion:**
```bash
git                             # Built-in, no flag needed
npm                             # Built-in, no flag needed
```

### User Experience Analysis

**Confusing Aspects:**
1. ❌ Options appear in `--help` but unclear what they do
2. ❌ No explanation of shell completion concept
3. ❌ Users may not know if they need it

**Clear Aspects:**
1. ✅ Standard Typer feature
2. ✅ Useful for power users
3. ✅ Can be hidden if desired

### Recommendation

**Option A: Keep but improve documentation** ⭐ RECOMMENDED

**Pros:**
- Useful feature for power users
- Standard CLI practice
- Minimal work

**Implementation:**
1. Keep `add_completion=True`
2. Add completion guide to docs
3. Add section to README

**Documentation to add:**
```markdown
## Shell Completion

Enable tab completion for faster command entry:

### Bash
ralf-notes --install-completion bash

### Zsh
ralf-notes --install-completion zsh

### Fish
ralf-notes --install-completion fish

After installation, restart your shell or run:
source ~/.bashrc  # or ~/.zshrc
```

**Option B: Hide options**

```python
app = typer.Typer(
    name="ralf-notes",
    help="...",
    add_completion=False  # Remove from help
)
```

**Pros:**
- Cleaner help output
- Less confusion

**Cons:**
- Lose useful feature
- Users have to know about it

**Option C: Custom implementation**

Create separate `completion` command:
```bash
ralf-notes completion install
ralf-notes completion show
```

**Pros:**
- More discoverable
- Better help text

**Cons:**
- More code to maintain
- Reimplementing Typer feature

### Decision

**Recommended: Option A (Keep + Document)**

**Rationale:**
1. Standard feature in modern CLI tools
2. Valuable for users who know about it
3. Minimal work (just documentation)
4. Doesn't hurt users who don't use it

**Action Items:**
- [ ] Add "Shell Completion" section to README
- [ ] Add completion guide to docs
- [ ] Maybe add note in help text

**Alternative: If user prefers cleaner help:**
- Set `add_completion=False`
- Add custom `completion` command later if needed

**Priority:** LOW

**Estimate:** 30 minutes (documentation)

---

## Summary of Issues

| Issue | Severity | Fix Time | Phase | Breaking? |
|-------|----------|----------|-------|-----------|
| **1. Missing fine-tune** | 🔴 High | 2-3 hrs | 7 | No |
| **2. check-health naming** | 🟡 Medium | 10 min | 6 | Yes |
| **3. Stage commands** | 🟡 Medium | 4-6 hrs | 7-8 | Yes |
| **4. Completion options** | ⚪ Low | 30 min | 8 | No |

---

## Recommended Action Plan

### Phase 6: Quick Fixes
1. ✅ Rename `check-health` → `health-check` (10 min)
2. ✅ Document breaking change in CHANGELOG

### Phase 7: Feature Completion
1. ✅ Add `fine-tune` command (2-3 hrs)
2. ✅ Wire up auto-tuning orchestrator
3. ✅ Test benchmarking workflow

### Phase 7-8: Structure Refactoring
1. ✅ Add `--stage` option to `generate`
2. ✅ Test all stage combinations
3. ✅ Deprecate old commands or remove
4. ✅ Update documentation

### Phase 8: Documentation
1. ✅ Add shell completion guide
2. ✅ Document command changes
3. ✅ Migration guide for users

---

## Breaking Changes Summary

### Version 2.1 (Phase 6-7)

**Breaking:**
- `check-health` → `health-check`

**Deprecated:**
- `generate-raw` (use `generate --stage 1`)
- `format-initial` (use `generate --stage 2`)
- `finalize` (use `generate --stage 3`)

**New:**
- `fine-tune` command added
- `--stage` option for `generate`

---

## Testing Checklist

### After Fixes
- [ ] `ralf-notes health-check` works
- [ ] `ralf-notes fine-tune --help` shows help
- [ ] `ralf-notes fine-tune --mode quick` runs
- [ ] `ralf-notes generate --stage 1` works
- [ ] `ralf-notes generate --stage 1,2` works
- [ ] `ralf-notes generate` (all stages) works
- [ ] Old commands show deprecation warning
- [ ] Completion install works: `ralf-notes --install-completion`
- [ ] Tab completion works after install

---

## User Documentation Updates Needed

### README.md
- [ ] Update command examples
- [ ] Add shell completion section
- [ ] Document `--stage` usage
- [ ] Migration guide for v2.0 → v2.1

### CHANGELOG.md
- [ ] Document breaking changes
- [ ] Document new features
- [ ] Migration instructions

### docs/user-guide.md (if exists)
- [ ] Update all command references
- [ ] Add stage workflow examples
- [ ] Completion setup instructions

---

## Conclusion

**Total Issues:** 4
**Critical:** 1 (missing fine-tune)
**Medium:** 2 (naming, structure)
**Low:** 1 (completion docs)

**Recommended Approach:**
1. Phase 6: Quick fix (health-check rename)
2. Phase 7: Add fine-tune command
3. Phase 7-8: Refactor stage commands
4. Phase 8: Documentation improvements

**Total Effort:** ~8-10 hours across phases

**User Impact:** Positive - cleaner CLI, expected features

---

**Document Version:** 1.0
**Date:** 2026-01-11
**Type:** CLI Design Review
**Next Review:** After Phase 7 implementation

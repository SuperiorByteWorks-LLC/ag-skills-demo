# Task 1: Manual Rollback Procedure

## Purpose

This document describes how to rollback the data tree reorganization migration if issues are encountered.

## Pre-Rollback Checklist

Before executing rollback:

- [ ] Identify the specific issue causing the rollback
- [ ] Ensure no active processes are writing to `data/` directory
- [ ] Verify git working directory is clean (or stash changes)
- [ ] Confirm backup of any critical data generated post-migration

## Rollback Steps

### Step 1: Stop Active Processes

```bash
# Check for active Python processes writing to data/
ps aux | grep -E "(python|run_farm_pipeline)" | grep -v grep

# If any found, terminate them
kill -TERM <PID>
```

### Step 2: Restore from Git (Full Rollback)

```bash
# Option A: Hard reset to pre-migration commit
# WARNING: This will discard ALL changes since baseline
git reset --hard a202c0a

# Option B: Revert specific migration commit (if committed)
git revert <migration-commit-hash> --no-edit

# Option C: Restore specific files/directories
git checkout a202c0a -- data/
```

### Step 3: Verify Rollback

```bash
# Verify directory structure matches baseline
find data/ -type f | sort | diff - .sisyphus/evidence/task-1-baseline.txt

# Check for legacy paths in scripts
grep -r "data/field-boundaries\|data/soil\|data/weather\|data/cdl\|data/EDA" data/scripts --include="*.py" | wc -l
# Expected: Non-zero (legacy paths should exist in baseline)

# Verify pipeline can run
python data/scripts/run_farm_pipeline.py --help
```

### Step 4: Clean Up Partial Migration Artifacts

```bash
# Remove any canonical directories created during migration
# (Only if they exist and are not part of baseline)
ls -la data/ | grep -E "(scripts|shared|growers)"

# Remove if present (use with caution)
# rm -rf data/scripts/lib  # Only if helper modules were added
# rm -rf data/shared       # Only if shared/ was created
# rm -rf data/growers      # Only if growers/ was created
```

## Partial Rollback Scenarios

### Scenario A: Rollback Script Changes Only

If only script modifications need to be reverted:

```bash
# Restore original scripts
git checkout a202c0a -- data/scripts/

# Keep any new data directories created
```

### Scenario B: Rollback Data Structure Only

If only data directory changes need to be reverted:

```bash
# Restore original data structure (excluding scripts)
git checkout a202c0a -- data/field-boundaries/
git checkout a202c0a -- data/soil/
git checkout a202c0a -- data/weather/
git checkout a202c0a -- data/EDA/

# Remove canonical directories if created
rm -rf data/shared 2>/dev/null
rm -rf data/growers 2>/dev/null
```

### Scenario C: Rollback Helper Modules

If only helper modules need to be removed:

```bash
# Remove helper modules
rm -rf data/scripts/lib/

# Restore scripts to use inline path construction
git checkout a202c0a -- data/scripts/
```

## Verification Commands

After rollback, verify with:

```bash
# 1. Directory structure matches baseline
echo "=== Directory Structure ==="
find data/ -type f | sort

# 2. Legacy paths exist in scripts
echo "=== Legacy Path References ==="
grep -r "data/field-boundaries\|data/soil\|data/weather\|data/cdl\|data/EDA" data/scripts --include="*.py" | head -20

# 3. Pipeline entrypoint works
echo "=== Pipeline Check ==="
python data/scripts/run_farm_pipeline.py --help

# 4. No canonical paths remain
echo "=== Canonical Path Check ==="
ls data/ | grep -E "^(scripts|shared|growers)$" || echo "No canonical roots found (expected for baseline)"
```

## Post-Rollback Actions

1. **Document the issue** that caused rollback in `.sisyphus/notepads/data-tree-reorganization/issues.md`
2. **Notify team** if working in shared environment
3. **Re-plan migration** addressing the identified issue
4. **Update evidence** if re-attempting migration

## Emergency Contacts / Escalation

- Review `.sisyphus/plans/data-tree-reorganization.md` for migration details
- Check `.sisyphus/drafts/data-tree-reorganization.md` for canonical structure specification
- Consult `data/README.md` for data organization documentation

---

**Last Updated**: 2025-03-08
**Baseline Commit**: a202c0a
**Migration Plan**: .sisyphus/plans/data-tree-reorganization.md

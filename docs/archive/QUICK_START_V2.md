# RALF Note V2 - Quick Start Guide

**Version:** 2.0
**Date:** 2026-01-09

---

## 🚀 Quick Start (2 Minutes)

### 1. Test Connection
```bash
python ralf.py test
```
Expected output: ✅ Connected to Ollama

### 2. Generate Documentation
```bash
python ralf.py generate
```
This will process files from `/Users/amac/Documents/code/WindowCleanner/` and output to `to_obsidian/`

### 3. Check Results
```bash
ls to_obsidian/
```
You should see generated `.md` files!

---

## 📖 Common Commands

### Generate Documentation
```bash
# Default (uses config.py paths)
python ralf.py generate

# Specific path
python ralf.py generate /path/to/code

# Custom output directory
python ralf.py generate --output /path/to/output

# Dry run (preview)
python ralf.py generate --dry-run

# Overwrite existing docs
python ralf.py generate --overwrite

# Quiet mode (minimal output)
python ralf.py generate --quiet

# Different model
python ralf.py generate --model qwen2.5:14b
```

### Check Status
```bash
python ralf.py status
```
Shows configuration and paths

### Test Ollama
```bash
python ralf.py test
```
Tests connection to Ollama

### Show Version
```bash
python ralf.py version
```
Shows version info

---

## 🎨 What You'll See

### Beautiful Banner
```
╔══════════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗  ║
║   ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║  ║
╚══════════════════════════════════════════════════════════════╝
```

### Progress Bar
```
Processing files ━━━━━━━━━━━━━━━━━━━━━━━━ 75% • 0:01:30 • 0:00:30
```

### File Progress
```
📄  Analyzing: main.py
✅  Generated: main.md
```

### Summary Panel
```
╭─────────── 📊 Results ───────────╮
│ Total Files: 100                 │
│ ✅ Success: 95                   │
│ ❌ Failed: 3                     │
│ Time: 125.4s                     │
╰──────────────────────────────────╯
```

---

## ⚙️ Configuration

Edit `config.py` to change:
- `SOURCE_PATHS` - Where to find code
- `TARGET_DIR` - Where to save documentation
- `MODEL_NAME` - Which Ollama model to use
- `OLLAMA_HOST` - Ollama server address

Example `config.py`:
```python
SOURCE_PATHS = [
    '/path/to/your/code/',
    '/another/path/',
]

TARGET_DIR = '/path/to/output/'
MODEL_NAME = 'ministral-3:3b'
OLLAMA_HOST = 'http://127.0.0.1:11434'
```

---

## 📊 Performance

- **Single file:** ~14 seconds
- **100 files:** ~23 minutes
- **LLM calls:** 1 per file (9x less than V1!)
- **Code complexity:** 58% less than V1

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'typer'"
**Solution:**
```bash
pip install typer rich ollama
```

### Error: "Failed to connect to Ollama"
**Solution:**
1. Start Ollama: `ollama serve`
2. Pull model: `ollama pull ministral-3:3b`

### Some files show "JSON parsing failed"
**This is normal!** The fallback creates a warning document with the raw output. The system is working as designed.

---

## 📁 Output Format

Each generated file has:
```markdown
---
tags: #tag1, #tag2, #tag3
created: 2026-01-09
type: code-notes
---

# filename

## Summary
High-level purpose

## Details
Detailed explanation

## Key Functions
### `function_name`
Description

## Usage
How to use

## Dependencies
Libraries used

## Related
- [[Related File]]

> [!INFO]- Key insight
> Important information
```

---

## 🎯 What's Different from V1?

| Feature | V1 | V2 |
|---------|----|----|
| **Generators** | 9 separate | 1 unified |
| **LLM Calls** | 9 per file | 1 per file |
| **Code Lines** | ~1,437 | ~600 |
| **TUI** | None | Beautiful! |
| **Speed** | ~15s/file | ~14s/file |
| **Complexity** | High | Low |

---

## 💡 Tips

1. **Use dry-run** to preview before generating
   ```bash
   python ralf.py generate --dry-run
   ```

2. **Use quiet mode** for scripts
   ```bash
   python ralf.py generate --quiet
   ```

3. **Check status** before running
   ```bash
   python ralf.py status
   ```

4. **Test connection** if having issues
   ```bash
   python ralf.py test
   ```

---

## 📚 Documentation

- **Full roadmap:** `roadmap/README.md`
- **PoC analysis:** `roadmap/00-poc-analysis.md`
- **Implementation plan:** `roadmap/04-implementation-roadmap.md`
- **Architecture:** `roadmap/02-architecture-refactoring.md`
- **Complete guide:** `V2_IMPLEMENTATION_COMPLETE.md`

---

## 🎉 You're Ready!

Just run:
```bash
python ralf.py generate
```

And watch your code turn into beautiful Obsidian documentation! ✨

---

**Questions? Check:**
- `V2_IMPLEMENTATION_COMPLETE.md` - Full implementation details
- `roadmap/` - Complete technical documentation
- `ARCHIVE_SUMMARY.md` - What was archived and why

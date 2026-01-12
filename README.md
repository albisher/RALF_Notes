# RALF Note v2.0

**Recursive AI-powered Learning Framework for Obsidian Documentation**

[![License](https://img.shields.io/badge/License-Custom-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-green.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Required-orange.svg)](https://ollama.ai/)

AI-powered documentation generator that transforms your code into beautiful Obsidian notes with a single command.

---

## ✨ Features

- 🚀 **Single LLM Call** - 9x faster than multi-generator approach
- 🎨 **Beautiful TUI** - Colored output, progress bars, ASCII art
- 📦 **Unified JSON** - One structured response, deterministic formatting
- 🏗️ **Clean Architecture** - Boxes methodology, OOP, dependency injection
- 💻 **Professional CLI** - Typer-powered with intuitive commands
- 📊 **Real-time Progress** - See exactly what's happening
- 🔄 **Batch Processing** - Process entire codebases at once
- 🎯 **Smart Validation** - Auto-fixes common issues

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- [Ollama](https://ollama.ai/) installed and running
- Model: `ollama pull ministral-3:3b`

### Installation

```bash
# Install from GitHub
pip install git+https://github.com/albisher/RALF_Notes.git

# Or install from PyPI (coming soon)
pip install ralf-notes
```

### First-Time Setup

```bash
# Run interactive setup wizard
ralf-notes setup

# This will:
# 1. Create configuration
# 2. Set up directories
# 4. Guide you through first use
```

### Generate Documentation

```bash
# Generate from configured paths
ralf-notes generate

# Or generate from specific path
ralf-notes generate /path/to/code
```

That's it! Your documentation will be in your configured output directory.

> **Note:** For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md)

---

## 📖 Usage

### Setup & Configuration

```bash
# Complete setup wizard (first-time users)
ralf-notes setup

# Initialize configuration
ralf-notes init

# Manage configuration
ralf-notes config --show                    # View config
ralf-notes config --add-source /path        # Add source directory
ralf-notes config --set-target /path        # Set output directory
ralf-notes config --set-model model-name    # Change model

# Check status
ralf-notes status
```

### Generate Documentation

```bash
# Generate from configured paths
ralf-notes generate

# Generate for specific path
ralf-notes generate /path/to/code

# Custom output directory
ralf-notes generate --output /custom/output

# Dry run (preview)
ralf-notes generate --dry-run

# Overwrite existing docs
ralf-notes generate --overwrite

# Quiet mode (minimal output)
ralf-notes generate --quiet

# Use different model
ralf-notes generate --model qwen2.5:14b
```

### Testing & Info

```bash
# Test Ollama connection
ralf-notes check-health

# Show version
ralf-notes version

# Get help
ralf-notes --help
```

---

## 🎨 Beautiful Output

```
╔══════════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗  ║
║   ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║  ║
║   ██╔══██╗██╔══██║██║     ██╔══╝      ██║╚██╗██║██║   ██║  ║
║   ██║  ██║██║  ██║███████╗██║         ██║ ╚████║╚██████╔╝  ║
╚══════════════════════════════════════════════════════════════╝

ℹ️  Model: ministral-3:3b
ℹ️  Target: to_obsidian/
ℹ️  Found 100 files to process
📄  Analyzing: main.py
✅  Generated: main.md
...
Processing files ━━━━━━━━━━━━━━━━━━━━━━━━ 100% • 0:02:10 • 0:00:00

╭─────────── 📊 Results ───────────╮
│ Total Files: 100                 │
│ ✅ Success: 95                   │
│ ❌ Failed: 3                     │
│ Time: 125.4s                     │
╰──────────────────────────────────╯
```

---

## ⚙️ Configuration

RALF Note stores configuration at `~/.ralf-notes/config.json`

### Quick Configuration

```bash
# Interactive setup
ralf-notes setup

# Or manually configure
ralf-notes config --add-source ~/projects/my-app
ralf-notes config --set-target ~/Documents/MyDocs
ralf-notes config --set-model qwen2.5:14b
```

### Configuration File

Default location: `~/.ralf-notes/config.json`

```json
{
  "source_paths": ["/path/to/code"],
  "target_dir": "./to_obsidian",
  "model_name": "ministral-3:3b",
  "ollama_host": "http://127.0.0.1:11434",
  "temperature": 0.1,
  "num_ctx": 10000
}
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| **Processing Time** | ~14s per file |
| **LLM Calls** | 1 per file (9x reduction!) |
| **Batch 100 files** | ~23 minutes |
| **Code Complexity** | 58% less than V1 |

---

## 🏗️ Architecture

RALF Note v2.0 uses a unified JSON approach:

```
File → JSONGenerator → JSONExtractor → JSONValidator → MarkdownFormatter → Obsidian MD
         (1 LLM call)   (Parse JSON)    (Validate)      (Format)         (Beautiful!)
```

### Key Components

- **JSONGenerator** - Single LLM call for all sections
- **JSONExtractor** - Robust JSON parsing with fallbacks
- **JSONValidator** - Schema validation and auto-fixing
- **MarkdownFormatter** - Deterministic markdown generation
- **DocumentPipeline** - Orchestrates the flow
- **FileProcessor** - Batch processing with progress
- **TUI** - Beautiful terminal interface

All following **Boxes methodology** with clean OOP design.

---

## 📁 Project Structure

```
RALF_Notes/
├── core_v2/              # Core components
│   ├── models.py         # Data models
│   ├── json_generator.py # LLM interaction
│   ├── json_extractor.py # JSON parsing
│   ├── json_validator.py # Validation
│   ├── markdown_formatter.py # Formatting
│   ├── document_pipeline.py  # Orchestration
│   └── file_processor.py     # Batch processing
├── tui/                  # Terminal UI
│   ├── console.py        # Rich console
│   ├── progress.py       # Progress bars
│   └── ascii_art.py      # ASCII banners
├── roadmap/              # Implementation docs
├── ralf.py               # Main CLI
├── config.py             # Configuration
└── LICENSE               # License terms
```

---

## 📝 Output Format

Each generated file includes:

```markdown
---
tags: #python, #documentation, #automation
created: 2026-01-09
type: code-notes
---

# filename

## Summary
High-level purpose in 1-2 sentences

## Details
Detailed explanation of logic and architecture

## Key Functions
### `function_name`
Description with signature and return value

## Usage
How to use this code

## Dependencies
Required libraries and modules

## Related
- [[Related File 1]]
- [[Related File 2]]

> [!INFO]- Key Insight
> Important information highlighted in callouts
```

---

## 🎯 What's New in V2?

| Feature | V1 | V2 |
|---------|----|----|
| **Architecture** | 9 generators | 1 unified pipeline |
| **LLM Calls** | 9 per file | 1 per file |
| **Code Lines** | ~1,437 | ~600 |
| **TUI** | None | Beautiful! |
| **Complexity** | High | Low |
| **Speed** | ~15s/file | ~14s/file |

---

## 💡 Why RALF Note?

- ✅ **Save Time** - Automated documentation generation
- ✅ **Stay Organized** - Obsidian integration
- ✅ **Understand Code** - AI-powered analysis
- ✅ **Knowledge Base** - Build a searchable library
- ✅ **Local & Private** - Runs on your machine with Ollama

---

## 📚 Documentation

- **Quick Start:** [QUICK_START_V2.md](QUICK_START_V2.md)
- **Implementation:** [V2_IMPLEMENTATION_COMPLETE.md](V2_IMPLEMENTATION_COMPLETE.md)
- **Roadmap:** [roadmap/README.md](roadmap/README.md)
- **Archive:** [ARCHIVE_SUMMARY.md](ARCHIVE_SUMMARY.md)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

By contributing, you agree that your contributions will be licensed under the same terms as this project.

---

## 📄 License

**Personal Use:** FREE ✅
**Team Use:** $1/month per user 💼
**Enterprise:** Custom quote 🏢

**Commercial forking/modification is NOT allowed.** See [LICENSE](LICENSE) for details.

### Quick Summary:
- ✅ **FREE for personal use** - Use, modify, learn
- 💰 **Paid for teams** - $1/month/user for businesses
- 🚫 **No commercial forks** - Can't create competing products
- 📧 **Contact for licensing:** [abalbisher@gmail.com](mailto:abalbisher@gmail.com)

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'typer'"
```bash
pip install typer rich ollama
```

### "Failed to connect to Ollama"
```bash
# Start Ollama
ollama serve

# Pull model
ollama pull ministral-3:3b
```

### "JSON parsing failed"
This is normal! The fallback creates a warning document with debug info.

---

## 📧 Contact

**Author:** Abdullah Albisher
**Email:** [abalbisher@gmail.com](mailto:abalbisher@gmail.com)
**GitHub:** [https://github.com/albisher/RALF_Notes](https://github.com/albisher/RALF_Notes)

---

## ⭐ Support

If you find RALF Note useful:
- ⭐ Star the repository
- 📢 Share with others
- 🐛 Report bugs
- 💡 Suggest features
- 💰 Purchase a license if using commercially

---

## 🙏 Acknowledgments

Built with:
- [Ollama](https://ollama.ai/) - Local LLM inference
- [Rich](https://github.com/Textualize/rich) - Terminal formatting
- [Typer](https://github.com/tiangolo/typer) - CLI framework

---

**RALF Note v2.0 - Transforming code into knowledge, one file at a time.** 📚✨

# RALF Note - Installation Guide

**Version:** 2.0.0
**Last Updated:** 2026-01-09

---

## 🚀 Installation Methods

### Method 1: Install from GitHub (Recommended)

```bash
# Install directly from GitHub
pip install git+https://github.com/albisher/RALF_Notes.git

# Or clone and install
git clone https://github.com/albisher/RALF_Notes.git
cd RALF_Notes
pip install -e .
```

### Method 2: Install from PyPI (Coming Soon)

```bash
# This will be available once published to PyPI
pip install ralf-notes
```

---

## ✅ Verify Installation

```bash
# Check if installed
ralf-notes --help

# Show version
ralf-notes version
```

**You should see:**
```
╔══════════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ██╗     ███████╗    ███╗   ██╗ ██████╗   ║
║   ██╔══██╗██╔══██╗██║     ██╔════╝    ████╗  ██║██╔═══██╗  ║
║   ██████╔╝███████║██║     █████╗      ██╔██╗ ██║██║   ██║  ║
╚══════════════════════════════════════════════════════════════╝

RALF Note v2.0.0 - Unified JSON Architecture
```

---

## 📋 Prerequisites

### Required

1. **Python 3.9+**
   ```bash
   python --version  # Should show 3.9 or higher
   ```

2. **Ollama**
   - Download: https://ollama.ai/
   - Install and start:
     ```bash
     # Start Ollama server
     ollama serve

     # Pull model (in another terminal)
     ollama pull ministral-3:3b
     ```

### Optional

- **Git** (for installing from GitHub)
- **Obsidian** (for viewing generated documentation)

---

## 🎯 Quick Start (3 Steps)

### Step 1: Install

```bash
pip install git+https://github.com/albisher/RALF_Notes.git
```

### Step 2: Setup

```bash
# Interactive setup wizard
ralf-notes setup
```

This will:
- ✅ Create configuration file
- ✅ Set up directories
- ✅ Test Ollama connection
- ✅ Guide you through first use

### Step 3: Generate

```bash
# Generate documentation
ralf-notes generate
```

That's it! Your documentation is in the configured output directory.

---

## 📁 Configuration

### Configuration File Location

RALF Note stores configuration at:
```
~/.ralf-notes/config.json
```

### Manual Configuration

You can also configure manually:

```bash
# Initialize configuration
ralf-notes init

# Add source paths
ralf-notes config --add-source /path/to/code

# Set output directory
ralf-notes config --set-target /path/to/output

# Change model
ralf-notes config --set-model qwen2.5:14b

# View configuration
ralf-notes config --show
```

---

## 📖 Available Commands

### Setup & Configuration

```bash
# Complete setup wizard (recommended for first-time users)
ralf-notes setup

# Initialize configuration
ralf-notes init

# Manage configuration
ralf-notes config --show                    # View config
ralf-notes config --add-source /path        # Add source
ralf-notes config --remove-source /path     # Remove source
ralf-notes config --set-target /path        # Set output dir
ralf-notes config --set-model model-name    # Change model
ralf-notes config --reset                   # Reset to defaults

# Show status
ralf-notes status
```

### Documentation Generation

```bash
# Generate from configured paths
ralf-notes generate

# Generate from specific path
ralf-notes generate /path/to/code

# Custom output directory
ralf-notes generate --output /custom/output

# Dry run (preview)
ralf-notes generate --dry-run

# Overwrite existing
ralf-notes generate --overwrite

# Quiet mode
ralf-notes generate --quiet

# Use different model
ralf-notes generate --model qwen2.5:14b
```

### Testing

```bash
# Test Ollama connection
ralf-notes test

# Show version
ralf-notes version
```

---

## 🎨 Example Workflows

### First-Time Setup

```bash
# 1. Install
pip install git+https://github.com/albisher/RALF_Notes.git

# 2. Run setup wizard
ralf-notes setup
# Follow prompts to configure

# 3. Generate docs
ralf-notes generate
```

### Daily Use

```bash
# Generate docs for current project
ralf-notes generate /path/to/project

# Generate with overwrite
ralf-notes generate --overwrite
```

### Configuration Management

```bash
# Add new source path
ralf-notes config --add-source ~/projects/my-app

# View current config
ralf-notes status

# Change output directory
ralf-notes config --set-target ~/Documents/MyDocs
```

---

## 🐛 Troubleshooting

### Issue: "ralf-notes: command not found"

**Solution:**
```bash
# Make sure pip install path is in PATH
# Check where it was installed
python -m pip show ralf-notes

# Or use python -m
python -m ralf_notes.cli --help
```

### Issue: "No module named 'ralf_notes'"

**Solution:**
```bash
# Reinstall package
pip uninstall ralf-notes
pip install git+https://github.com/albisher/RALF_Notes.git
```

### Issue: "Failed to connect to Ollama"

**Solution:**
```bash
# Start Ollama
ollama serve

# In another terminal, pull model
ollama pull ministral-3:3b

# Test connection
ralf-notes test
```

### Issue: "No source paths configured"

**Solution:**
```bash
# Run setup wizard
ralf-notes setup

# Or manually add paths
ralf-notes config --add-source /path/to/code
```

---

## 📂 Directory Structure After Installation

```
~/.ralf-notes/
└── config.json          # Your configuration

Your configured output directory:
└── to_obsidian/         # Generated documentation
    ├── file1.md
    ├── file2.md
    └── ...
```

---

## 🔄 Updating

### Update from GitHub

```bash
pip install --upgrade git+https://github.com/albisher/RALF_Notes.git
```

### Check Current Version

```bash
ralf-notes version
```

---

## 🗑️ Uninstallation

```bash
# Uninstall package
pip uninstall ralf-notes

# Optionally remove configuration
rm -rf ~/.ralf-notes
```

---

## 💡 Tips

### 1. Use Setup Wizard for First Time

```bash
ralf-notes setup
```
This provides guided configuration and testing.

### 2. Check Status Before Generating

```bash
ralf-notes status
```
Verifies your configuration is correct.

### 3. Test Ollama Connection

```bash
ralf-notes test
```
Ensures Ollama is working before generating.

### 4. Use Dry Run for Testing

```bash
ralf-notes generate --dry-run
```
Preview what will be generated without writing files.

### 5. Add Multiple Source Paths

```bash
ralf-notes config --add-source ~/project1
ralf-notes config --add-source ~/project2
ralf-notes config --add-source ~/project3
```
Then generate from all with one command:
```bash
ralf-notes generate
```

---

## 🎓 Learning Path

### For Beginners

1. Install: `pip install git+https://github.com/albisher/RALF_Notes.git`
2. Setup: `ralf-notes setup`
3. Generate: `ralf-notes generate`
4. Explore output in your configured directory

### For Advanced Users

1. Configure manually: `ralf-notes config`
2. Use custom models: `ralf-notes generate --model qwen2.5:14b`
3. Integrate into CI/CD pipelines
4. Automate documentation updates

---

## 📚 Additional Resources

- **Main README:** [README.md](README.md)
- **Quick Start:** [QUICK_START_V2.md](QUICK_START_V2.md)
- **Implementation Details:** [V2_IMPLEMENTATION_COMPLETE.md](V2_IMPLEMENTATION_COMPLETE.md)
- **Roadmap:** [roadmap/README.md](roadmap/README.md)
- **License:** [LICENSE](LICENSE)

---

## 📧 Support

**Issues:** https://github.com/albisher/RALF_Notes/issues
**Email:** abalbisher@gmail.com
**GitHub:** https://github.com/albisher/RALF_Notes

---

## ✨ Next Steps

After installation:
1. ✅ Run `ralf-notes setup`
2. ✅ Add your source directories
3. ✅ Generate documentation
4. ✅ Open generated files in Obsidian
5. ✅ Enjoy your AI-generated knowledge base!

---

**Ready to transform your code into beautiful documentation!** 📚✨

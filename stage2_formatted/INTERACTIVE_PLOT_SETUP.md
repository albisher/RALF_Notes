**Tags:** #troubleshooting, #tkinter, #interactive_plots, #venv, #visualization, #PyQt5, #macos, #python
**Created:** 2026-01-13
**Type:** troubleshooting-notes

# INTERACTIVE_PLOT_SETUP

## Summary

```
Provides solutions for enabling interactive 3D plots in Python environments, focusing on resolving missing dependencies like `tkinter` or `PyQt5`.
```

## Details

> This document addresses the issue where interactive plots fail in a virtual environment (venv) due to missing GUI dependencies, specifically `tkinter`. It outlines three primary solutions: installing `PyQt5` via pip, leveraging system Python on macOS, or installing `python-tk` via Homebrew. The document also describes the expected behavior of the visualization tool—saving PNG images automatically while enabling interactive controls when dependencies are met.

## Key Functions

### ``pip install PyQt5``

Installs the PyQt5 library to enable interactive plots in venv.

### ``scenarios/exploration/visualization/visualize_exploration.py``

Main script for running interactive 3D plots.

### ``brew install python-tk``

Installs the `tkinter` package for macOS to support GUI-based visualizations.

## Usage

1. **For PyQt5**: Run `pip install PyQt5` in the venv, then execute `python scenarios/exploration/visualization/visualize_exploration.py`.
2. **For System Python (macOS)**: Use `/usr/bin/python3` to run the script directly.
3. **For tkinter**: Install `python-tk` via Homebrew, then reinstall Python in the venv or switch to system Python.

## Dependencies

> ``PyQt5``
> ``tkinter` (if manually installed)`
> `system Python (macOS).`

## Related

- [[None]]

>[!INFO] Important Note
> Ensure the virtual environment is activated before installing `PyQt5` or `python-tk` to avoid conflicts with system Python packages.

>[!WARNING] Caution
> If using `python-tk`, verify Homebrew’s installation path matches the venv’s Python configuration to avoid runtime errors.

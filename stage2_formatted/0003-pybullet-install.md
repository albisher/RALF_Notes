**Tags:** #macOS, #PyBullet, #simulation, #compilation, #visual_demo, #venv, #bullet3, #physics, #robotics, #HMRS
**Created:** 2026-01-13
**Type:** documentation

# 0003-pybullet-install

## Summary

```
Document outlining PyBullet installation challenges on macOS and alternative solutions for simulation needs.
```

## Details

> This document addresses PyBullet installation failures on macOS due to zlib macro conflicts during compilation. It provides multiple solutions, including using a working visual demo (which meets HMRS requirements) and detailed instructions for manual builds, Conda environments, or Docker containers. The visual demo leverages `numpy` and `matplotlib` to simulate multi-robot systems, sensors, and real-time physics without requiring full PyBullet compilation.

## Key Functions

### ``run_visual_demo.py``

Demonstrates multi-robot simulation, sensor visualization (LiDAR), and control systems using `numpy` and `matplotlib`.

### ``pybullet` (manual build)`

Full physics simulation library requiring compilation from source.

### ``bullet3` (GitHub repo)`

Source code for PyBullet, built via CMake.

## Usage

1. **For HMRS verification**: Run `run_visual_demo.py` in the virtual environment (venv) to validate requirements.
2. **For full PyBullet**: Follow manual build steps (CMake, compilation) or use Conda/Docker as alternatives.

## Dependencies

> `- `numpy``
> ``matplotlib``
> ``python3.10``
> ``cmake``
> ``pkg-config``
> ``git``
> ``brew` (for macOS)`
> ``conda` (optional)`
> ``docker` (optional).`

## Related

- [[PyBullet GitHub]]
- [[HMRS Requirements]]
- [[WindowCleanner Simulation]]

>[!INFO] Important Note
> The visual demo is sufficient for HMRS requirements but lacks advanced physics capabilities. Full PyBullet installation is only needed for precise physics simulations.


>[!WARNING] Caution
> Manual compilation may fail due to macOS-specific zlib conflicts. Test builds in a clean environment before integration.

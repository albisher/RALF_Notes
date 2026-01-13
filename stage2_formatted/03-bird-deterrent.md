**Tags:** #open-source, #ultrasonic, #bird-control, #acoustic-deterrent, #YOLOv8, #ROS2, #drones, #habituation-prevention
**Created:** 2026-01-13
**Type:** research-notes

# 03-bird-deterrent

## Summary

```
Explores open-source bird deterrent system using ultrasonic frequencies and YOLOv8 for detection.
```

## Details

> This document outlines a **production-ready bird deterrent system** leveraging **open-source technologies** for detection (YOLOv8) and control (acoustic emitters). The system employs **ultrasonic frequencies (200–12,800 Hz)** with rapid sweeps (0.05-sec pulses) to deter birds within a 10–20m range, triggered by visual detection within 10m. Multi-frequency rotation prevents habituation. Power is managed via drone batteries (<10W), and directional transducers (60° beam) ensure targeted emission.

## Key Functions

### `Acoustic Emitter`

Generates high-frequency ultrasonic pulses (200–12,800 Hz) in rapid sweeps (0.05 sec) for habituation prevention.

### `Bird Detection`

Uses YOLOv8 for real-time visual detection of birds within a 10m zone.

### `Acoustic Activation`

Triggers emitter upon detection within 10m, with multi-frequency rotation to avoid adaptation.

### `ROS2 Integration`

Implements control logic and pattern generation for modular system expansion.

## Usage

1. Deploy YOLOv8 for bird detection in a 10m radius.
2. Activate ultrasonic emitter (200–12,800 Hz, 0.05-sec pulses) within 15–30m escape distance.
3. Rotate frequencies dynamically to prevent habituation.
4. Power via drone battery (<10W) with directional transducers (60° beam).

## Dependencies

> ``pyaudio``
> ``sounddevice``
> ``numpy``
> ``YOLOv8``
> ``OpenCV``
> ``ROS2``
> ``PyTorch``
> ``TensorFlow``

## Related

- [[Bird Deterrent Protocols]]
- [[Open-Source Ultrasonic Systems]]

>[!INFO] **Frequency Optimization**
> Prioritize **12,800 Hz** for maximum repulsion; lower frequencies (200–4,000 Hz) reduce effectiveness.

>[!WARNING] **Habituation Risk**
> Rapid frequency rotation (multi-patterns) is critical to avoid bird adaptation; test in controlled environments first.

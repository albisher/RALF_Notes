**Tags:** #robot-identification, #character-design, #code-versioning, #role-based-classification
**Created:** 2026-01-13
**Type:** documentation

# whatMakesRobot

## Summary

```
Describes attributes and metadata for categorizing and identifying robots, including physical traits, functional roles, and narrative context.
```

## Details

> This document outlines structured attributes for defining robots, such as **code/version labels** (e.g., "X1" or "exploration"), **physical appearance** (e.g., body parts, colors, eye descriptions), and **functional roles** (e.g., assigned tasks, movement methods). It also includes **historical/design constraints** (e.g., limitations, dependencies) and **social dynamics** (e.g., factions, allies/enemies). The document suggests a system for tracking compliance with core code sets (e.g., rogue status) and narrative tags (e.g., "rebel").
> 
> The structure appears to be a **metadata framework** for robot classification, blending technical specifications with storytelling elements.

## Key Functions

### `Primary Identification`

Assigns version/style labels (e.g., "X1") and names for robot categorization.

### `Physical Attributes`

Defines visual and mechanical traits (e.g., body parts, colors, movement).

### `Creation & History`

Logs creation date, assigned tasks, and limitations to avoid redundancy.

### `Social Context`

Maps relationships (allies/enemies) and faction alignment for narrative cohesion.

### `Rogue/Rebel Check`

Uses a variable flag to determine if a robot deviates from core code (e.g., "rebel" tag).

## Usage

1. **For Designers**: Fill in attributes to define a robot’s identity (e.g., "Main Color: Silver").
2. **For Coders**: Use version labels to differentiate units (e.g., "X1" vs. "exploration").
3. **For Storytellers**: Apply faction tags (e.g., "Allies: Alliance of Machines") to shape narratives.
4. **For Compliance Checks**: Verify if a robot’s code deviates (e.g., "Rogue" flag) or aligns with assigned tasks.

## Dependencies

> `none (standalone metadata template)`

## Related

- [[Robot Metadata Template]]
- [[Narrative Role Guidelines]]

>[!INFO] **Code vs. Narrative Separation**
> The distinction between "assigned tasks" (functional) and "story context" (social) ensures robots remain versatile for both technical and creative use cases.

>[!WARNING] **Overloading Limitations**
> Explicitly listing limitations (e.g., "needs other robot") prevents unintended redundancy in robot design.

# Pygame Visual Effects Application

## Overview
This is a Python pygame application that demonstrates various visual effects including radial gradients, wavy shaders, bloom/glow effects, and shockwave animations. Created by cdelor on October 24, 2025.

## Project Type
Desktop GUI application using pygame

## Features
- Radial gradient backgrounds
- Wavy shader effects (animated fog/mist)
- Bloom/glow post-processing
- Interactive shockwave effects (triggered by mouse clicks)
- 60 FPS rendering

## Technical Details
- **Language**: Python 3.11
- **Framework**: pygame 2.6.1
- **Display**: 800x600 window
- **Package Manager**: uv

## How to Run
The application runs automatically in VNC mode, showing the pygame window with animated visual effects. Click anywhere to create a shockwave effect.

## Project Structure
```
.
├── fleur jeu.py          # Main pygame application with visual effects
├── README.md             # Project readme
├── pyproject.toml        # Python project configuration
├── uv.lock              # UV lock file
└── .pythonlibs/         # Virtual environment (gitignored)
```

## Dependencies
- pygame: Core graphics and event handling library

## Recent Changes
- **2025-11-16**: Imported from GitHub and configured for Replit environment
  - Installed Python 3.11 and pygame
  - Configured VNC workflow for GUI display
  - Added .gitignore for Python project
  - Created project documentation

## Architecture
Single-file pygame application with:
1. Shader functions for visual effects (radial gradient, wavy shader, bloom, shockwave)
2. Main game loop handling events and rendering
3. Real-time visual effects processing at 60 FPS

# 1 Brain Cell Game

This repository contains a small Python project created as part of a course exercise.  
The aim was to practise **basic Python coding skills** in a group setting, focusing on writing simple, working code rather than production-ready software.

## Overview

- A lightweight Python game split across several scripts to keep the code organised.
- Designed to be **clear and readable** for someone learning Python.
- No advanced optimisation or frameworks required.

## File Descriptions

- **`main_game.py`** – The main entry point. Runs the game loop and ties together mechanics, graphics, and messages.
- **`game_mechanics.py`** – Contains core gameplay logic (rules, actions, and behaviours).
- **`game_mechanics_options.py`** – Provides alternative or extended mechanics that can be swapped into the main game.
- **`boss_mechanics.py`** – Specialised rules and logic for handling “boss” style encounters.
- **`room_mechanics.py`** – Manages different rooms/areas of the game and how the player interacts with them.
- **`graphics.py`** – Handles simple drawing, text display, and visual elements.
- **`messages.py`** – Stores in-game text, dialogue, or messages displayed to the player.
- **`Testing_Sound.py`** – A standalone script used to test sound functionality.

> The `__pycache__/` folder is automatically created by Python and does not need to be modified.

## How to Run

1. Make sure you have **Python 3.8+** installed.
2. Clone or download this repository.
3. From the project folder, run:

```bash
python main_game.py
```

## Learning Focus

This project was written to demonstrate:
- How to organise a small multi-file Python script
- Use of functions and control flow
- Splitting responsibilities across multiple files
- Collaboration on a simple exercise
- Adding comments to explain code behaviour

## Notes

- The code is intentionally simple and may not cover all edge cases.
- Improvements (such as more error handling, tests, or packaging) could be added later, but the purpose here is to show **entry-level understanding** of Python.

---

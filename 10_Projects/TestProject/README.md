# TestProject

A collection of small Python programs for practicing functions, user input, image processing, and basic testing.

## Programs

| File | Purpose |
| --- | --- |
| `main.py` | Confirms that the Rich terminal-output package is installed |
| `RPS_Game.py` | Interactive Rock-Paper-Scissors game |
| `Draw_Tree.py` | Draws a recursive tree using Python's `turtle` graphics |
| `remove_bg.py` | Removes an image background using `rembg` |
| `test_main.py` | Automated tests for the game logic and main entry point |

## Requirements

Use Python 3.10 or newer. The background-removal script uses third-party packages listed in `requirements.txt`. The turtle demo requires a desktop environment capable of opening a graphics window.

## Setup (Windows PowerShell)

From this directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can run the virtual environment's Python directly using `.venv\Scripts\python.exe`.

## Run a program

```powershell
python main.py
python RPS_Game.py
python Draw_Tree.py
python remove_bg.py
```

The background-removal script looks for `Bleach.jpg` in this project directory by default and writes `output_image.png` to the same directory. You can also call `remove_background(input_path, output_path)` from another Python script.

The first run of `rembg` may download a machine-learning model, which can take time and disk space. Use only images you have permission to process.

## Run tests

```powershell
python -m pytest
```

The tests exercise game logic and the Rich output entry point; they do not run background removal or open a turtle graphics window.

## Troubleshooting

- **ModuleNotFoundError:** Activate this project's virtual environment and install `requirements.txt`.
- **Input image not found:** Put `Bleach.jpg` beside `remove_bg.py`, or pass an explicit path to `remove_background()`.
- **Turtle window does not open:** Run the turtle demo on a local desktop session rather than a headless terminal.

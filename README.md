# Words Swapper

A Python script that monitors keyboard input and automatically replaces specific words with custom replacements in real-time.

## Features

- Monitors keyboard input in real-time
- Automatically replaces words
- Easy to customize for other word replacements
- Safe operation with failsafe mechanisms
- Simple start/stop controls

## Requirements

- Python 3.6 or higher
- Linux (tested on Ubuntu/Debian)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make the script executable:
```bash
chmod +x main.py
```

## Usage

1. Run the script:
```bash
python3 main.py
```

2. The script will start monitoring your keyboard input
3. Type normally - whenever you type 'my' or 'myself' followed by a space, tab, or enter, it will automatically be replaced with 'omer'
4. Press `ESC` to stop the script

## How It Works

- The script uses `pynput` to monitor keyboard events
- It maintains a buffer of typed characters
- When a space, tab, or enter is detected, it checks if the buffer contains a word to replace
- If a replacement is needed, it uses `pyautogui` to delete the original word and type the replacement
- The script runs in the background until stopped

## Safety Features

- `pyautogui.FAILSAFE = True` - Move your mouse to any corner of the screen to stop the script
- Built-in delays to prevent overwhelming the system
- Error handling for various edge cases

## Customization

To modify which words are replaced, edit the `words_to_replace` list in the `WordsSwapper` class:

```python
self.words_to_replace = ['my', 'myself', 'your_word_here']
```

To change the replacement text, modify the `replacement` variable:

```python
self.replacement = 'your_replacement_here'
```

## Troubleshooting

- **Permission issues**: On some systems, you may need to run with `sudo` for keyboard access
- **Dependencies not found**: Make sure you've installed the requirements with `pip install -r requirements.txt`
- **Script not responding**: Try moving your mouse to any corner of the screen to trigger the failsafe

## Note

This script requires access to your keyboard input, which may require elevated permissions on some systems. Use responsibly and ensure you understand the implications of granting keyboard access to scripts.

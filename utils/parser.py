import argparse

parser = argparse.ArgumentParser(description="keylogger")

parser.add_argument("-e", "--email", required=False, metavar="email",
                    type=str, help="email address where you send logs",
                    nargs=2)
parser.add_argument("-p", "--path", type=str, metavar="path",
                    required=False, help="path where you save logs")

if __name__ == "__main__":
    parsed = parser.parse_args()
    print(parsed.email)

import logging
import os


def setlog(path):

    if not os.path.isfile(path):
        file = open(path, "w")
        file.close()

    log = logging.getLogger()
    file_handler = logging.FileHandler(path)
    formatter = logging.Formatter("%(message)s")

    log.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    log.addHandler(file_handler)

    return log


logger = None

if __name__ == "__main__":
    setlog(os.path.join(os.getcwd(), "file.log"))

import logging
import os


def setlog(path):

    if not os.path.isfile(f"{ path }/file.log"):
        file = open(f"{ path }/file.log", "w")
        file.close()

    logger = logging.getLogger()
    file_handler = logging.FileHandler(f"{ path }/file.log")
    formatter = logging.Formatter("%(message)s")

    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    setlog(os.path.join(os.getcwd(), "file.log"))

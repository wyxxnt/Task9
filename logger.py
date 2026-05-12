import time

levels = {"DEBUG": 0, "INFO": 1, "ERROR": 2}
current = "DEBUG"


def log(level="INFO"):
    def decorator(func):
        def wrapper(*args):
            if levels[level] < levels[current]:
                return func(*args)
            t = time.strftime("%H:%M:%S")

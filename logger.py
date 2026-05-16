import time

levels = {"DEBUG": 0, "INFO": 1, "ERROR": 2}
current = "DEBUG"


def log(level="INFO"):
    def decorator(func):
        def wrapper(*args):
            if levels[level] < levels[current]:
                return func(*args)
            t = time.strftime("%H:%M:%S")
            try:
                result = func(*args)
                print(t + " [" + level + "] " + func.__name__ + str(args) + " -> " + str(result))
                return result
            except Exception as e:
                print(t + " [ERROR] " + func.__name__ + str(args) + " error: " + str(e))
        return wrapper
    return decorator
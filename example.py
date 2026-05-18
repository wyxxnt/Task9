import logger
from logger import log

@log("INFO")
def add(a, b):
    return a + b

@log("DEBUG")
def multiply(a, b):
    return a * b

@log("ERROR")
def divide(a, b):
    return a / b

print("=== all logs ===")
add(2, 3)
multiply(4, 5)

print("\n=== only INFO+ ===")
logger.current = "INFO"
add(10, 20)
multiply(4, 5)

print("\n=== error ===")
logger.current = "DEBUG"
divide(10, 0)

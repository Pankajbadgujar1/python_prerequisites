import logging

# Create logger
logger = logging.getLogger("ArithmeticApp")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("app1.log")

# Console handler
console_handler = logging.StreamHandler()

# Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Function
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

add(10, 3)

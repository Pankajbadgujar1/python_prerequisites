import logging

## Create a logger from module1 

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

## Create a logger for module2

logger2 = logging.getLogger("Module2")
logger2.setLevel(logging.WARNING)

#Confugure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s -%(name)s- %(levelname)s  -%(message)s',
    datefmt='%Y-%m- %d %H:%M:%S'
)

logger1.debug("This is debuge message for modeule 1")
logger2.warning("This is a warning message from module 2")
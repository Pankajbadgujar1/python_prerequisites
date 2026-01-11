"""
Python Logging

Logging is a crucial aspect of any application, aproviding a way to track events, errors, 
and operational infromation. Python's built-in logging module offers a flexible framework for
emitting log messages from python programs.



Different Log Levels (Very Important)
Level	                Use
DEBUG	    =>       Developer details
INFO	    =>        Normal events
WARNING	    =>       Something unusual
ERROR	    =>        Something failed
CRITICAL	=>       App crashed


"""
import logging
## Configure the basic logging settings
logging.basicConfig(level=logging.DEBUG)

## Log Messanges
logging.debug("This is dubug message")

logging.info("This is an info message")

logging.warning("This is warnnig info")

logging.error("This is error messange")

logging.critical("This is critical message")
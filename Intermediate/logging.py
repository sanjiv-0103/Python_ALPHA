import logging
# basic log levels
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

# show debug and above
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug is now visible")
logging.info("program started")

# custom message format
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)
logging.warning("something may be wrong")
# create custom logger
logger=logging.getLogger("my_app")
logger.info("hello from custom logger")
logger.error("an error occurred")

# log to file
file_handler=logging.FileHandler("app.log")
logger.addHandler(file_handler)
logger.error("this message is also saved in app.log")
# try except with logging
try:
    nums=[1,2,3]
    print(nums[5])
except IndexError as e:
    logging.error(e)
# log traceback
try:
    value=10/0
except ZeroDivisionError as e:
    logging.error(e,exc_info=True)
# stream handler
stream_handler=logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
logger.addHandler(stream_handler)
logger.warning("warning shown in console")

# file handler with level
error_file=logging.FileHandler("error.log")
error_file.setLevel(logging.ERROR)
logger.addHandler(error_file)
logger.error("this goes to error.log")
import logging

# create logger with a unique name
logger = logging.getLogger('clean_code')

# configure logger to log messages of INFO level and above
logger.setLevel(logging.DEBUG)

# Define a handler to specify where the log messages be sent 
handler = logging.StreamHandler() # Logs messages to the console
logger.addHandler(handler)

# Log messages at different levels all of which will show because the log level is set to DEBUG
# logger.debug('This is a debug message') 
# logger.info('just testing the logger')
# logger.warning('This is a warning')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# Change the log level to WARNING
logger.setLevel(logging.WARNING)

# Log messages INFO and DEBUG will not show because the log level is set to WARNING
logger.debug('This is a debug message')
logger.info('This is an info')
logger.warning('This is a warning')
logger.error('This is an error message')
logger.critical('This is a critical message')
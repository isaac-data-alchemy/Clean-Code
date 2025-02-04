import logging 
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('rotating_file_logger')

# settung log level
logger.setLevel(logging.INFO)

# formatter 
formatter = logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')

# needs a handler 
handler = RotatingFileHandler('app.log', maxBytes=2097152, backupCount=4)
# handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


# messages
messages = ["this is one message", "and this is another message", "this is a third activity for the logger to see", "how about another one"]
RANGE= 100
while RANGE > 0:
    for msg in messages:
        logger.info(msg)
        logger.warning(msg) 
        logger.error(msg) 
        logger.critical(msg) 
        # logger.info([msg for msg in messages])
        RANGE -=10

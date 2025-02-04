import logging

# create an instance
logger = logging.getLogger("custom_formatter")

# configure level
logger.setLevel(logging.DEBUG)

# Define custom formatter
class CustomFormatter(logging.Formatter):
    def format(self, record):
        formatted_message = f'[{record.levelname}] {record.msg}'
        return formatted_message

# Define a handler with the custmo formatter
# handler = logging.StreamHandler()
handler = logging.FileHandler('custom.log')
formatter = CustomFormatter()
handler.setFormatter(formatter)


# configure with our logger
logger.addHandler(handler)

messages = ["this is one message", "and this is another message", "this is a third activity for the logger to see", "how about another one"]
RANGE= 100
while RANGE > 0:
    for msg in messages:
        logger.info(msg)
        logger.warning(msg) 
        logger.error(msg) 
        logger.critical(msg) 
        RANGE -=15
        # logger.info([msg for msg in messages])

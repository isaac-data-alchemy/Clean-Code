import logging
from sre_constants import RANGE
import sys

# instance
logger = logging.getLogger("filter_logger")

RANGE = 100
class NoParsingFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().startswith("parsing")
        # return not record.getMessage().find("parsing")


class FindFilter(logging.Filter):
    def filter(self, record):
        return not record.getMessage().find("parsing")



def function_a(range=RANGE):
    while range > 0:
        logger.warning("socket message")
        range-=20

def function_b(range=RANGE):
    while range > 0:
        logger.info("parsing another message")
        range-=20

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logger.addFilter(FindFilter())
    function_a()
    function_b()
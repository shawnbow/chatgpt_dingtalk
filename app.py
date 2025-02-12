# encoding:utf-8

from channels.channel_factory import create_channel
from common.log import logger


if __name__ == '__main__':
    try:

        # create channel
        channel = create_channel("dt")

        # startup channel
        logger.info("App starting up...")
        channel.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)

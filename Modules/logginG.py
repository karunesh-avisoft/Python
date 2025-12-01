import logging

# Configure basic logging (outputs to console by default)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get a logger instance
logger = logging.getLogger(__name__)

# Emit log messages at different levels
logger.debug("This is a debug message.")  # Won't be displayed with INFO level
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
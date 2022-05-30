import logging

# set thresold for logging

logging.basicConfig(level=logging.INFO)

# 1 --- Way 1
logging.info("Info Message via .info()")

# 2 --- way 2
logging.log(logging.INFO, "Info Message via .log()")

# 3 Cusotm Logger
logger = logging.getLogger("Custom Logger")
logger.info("Info Message via .info()")

# 4 File
file_handler = logging.FileHandler("Python/codes/logging/sample.log", mode="w")
file_handler.setLevel(logging.INFO)
file_log_formatter = logging.Formatter("%(levelname)s {-> %(asctime)s [-> %(message)s")
file_handler.setFormatter(file_log_formatter)

logger.addHandler(file_handler)

logger.debug("Debug Message Log")
logger.info("Informations Message Log")

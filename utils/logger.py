import  os

import  logging

def get_logger (name="selenium"):

    logger=logging.getLogger(name)

    logger.setLevel(logging.info())

    log_path = "test/test.log"

    os.mkdir(os.path.dirname(log_path),exist_ok=True)

    fh = logging.FileHandler(log_path,encoding='utf-8')

    formatter = logging.Formatter ("%(asctime)s - % (level)s - %(name)s")

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return  fh
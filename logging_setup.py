import logging

def setup_logger(name, log_file='server.log', level = logging.DEBUG):

    logger = logging.getLogger(name)

    logger.setLevel(level)
    file_hanlder = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_hanlder.setFormatter(formatter)
    logger.addHandler(file_hanlder)

    return logger
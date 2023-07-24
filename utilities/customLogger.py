import logging


class Logger1:
    @staticmethod
    def sample_logger():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(datefmt='%m-%d-%Y %I:%M:%S %p', fmt="%(asctime)s - %(module)s - %(levelname)s : "
                                                                          "%(message)s ")
        fh = logging.FileHandler(filename="Logs/logs.log",
                                 mode='a', encoding='utf-8')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


if __name__ == '__main__':
    customer_loger = Logger1.sample_logger()
    customer_loger.debug(f"Debug\t The result of Addition is:")
    customer_loger.info(f"Info\t The result of Addition is:")
    customer_loger.warning(f"Warning\t The result of Addition is:")
    customer_loger.error(f"Error\t The result of Addition is:")
    customer_loger.critical(f"Critical\t The result of Addition is:")

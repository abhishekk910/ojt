import logging
logging.basicConfig(level=logging.INFO,
                    filename="file1.log",
                    filemode= "w",
                    format="%(asctime)s:%(filename)s:%(levelname)s:%(name)s"
                    )

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

logging.info("Addition is {}".format(add(10, 5)))
logging.info("Substraction is {}".format(sub(10, 5)))
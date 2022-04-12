import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="file2.log",
                    filemode= "w",
                    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s"
                    )
class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.debug("Name is {} {}".format(self.first, self.last))

p1 = Person("A", "B")
p2 = Person("I", "K")
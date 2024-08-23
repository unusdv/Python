# Abstraction - Mavhumlashtirish
from abc import ABC, abstractmethod

class Jonzot (ABC):
    @abstractmethod
    def harakatlanish(self):
        pass


class Odam (Jonzot):
    def harakatlanish(self):
        print("Men yurdim")


class Ilon (Jonzot):
    def harakatlanish(self):
        print("Men sudraldim")


if __name__ == "__main__":
    o = Odam()
    o.harakatlanish()

    i = Ilon()
    i.harakatlanish()

    # j = Jonzot()  # Error
    # j.harakatlanish()

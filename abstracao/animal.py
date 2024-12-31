from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def dizer_algo(self):
        pass


from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def emitir_som(self):
        pass


class Gato(Animal):

    def emitir_som(self):
        return "Miau"


class Cachorro(Animal):

    def emitir_som(self):
        return "Au Au"


class AnimalFacory:

    def emitir_som(self, animal):
        return animal().emitir_som()


factory = AnimalFacory()

print(factory.emitir_som(Cachorro))
print(factory.emitir_som(Gato))

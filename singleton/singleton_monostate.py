#Padrão Borg, todos os objetos podem ter endereço de memoria diferente porem devem ter o mesmo estado.

class Borg: 
    __shared_state = {}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b  = Borg()
b1 = Borg()

b.x = 4

print("b object: ", b)
print("b1 object: ", b1)

print("Object state b: ", b.__dict__)
print("Object state b1: ", b1.__dict__)

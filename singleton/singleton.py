#Padrão singleton, todos objetos vão ter o mesmo endereço de memoria compartilhando o mesmo estado


class Pessoa:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Pessoa, cls).__new__(cls)
        return cls.instance


class Endereco:
    def __init__(self):
        pass


pessoa1 = Pessoa()

print("Objeto Pessoa 1 Singleton", pessoa1)

pessoa2 = Pessoa()

print("Objeto Pessoa 2 Singleton", pessoa2)

endereco1 = Endereco()

print("Objeto Endereco 1 não Singleton", endereco1)

endereco2 = Endereco()

print("Objeto Endereco 1 não Singleton", endereco2)


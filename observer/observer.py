# Define uma dependencia de um pra muitos entre os objetos, de modo que qualquer alteração sera notificada
# aos dependentes de maneira automatica


class CanalDeNoticia:

    def __init__(self):
        self.__inscritos = []
        self.__noticia = ''

    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)

    def desinscrever(self):
        self.__inscritos.pop()

    def inscritos(self):
        return [type(x).__name__ for x in self.__inscritos]

    def notificar_inscritos(self):
        for inscrito in self.__inscritos:
            inscrito.update()

    def adicionar_noticia(self, noticia):
        self.__noticia = noticia

    @property
    def noticia(self):
        return self.__noticia

from abc import ABCMeta, abstractmethod


class Assinar(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMS(Assinar):

    def __init__(self, assinatura):
        self.assinatura = assinatura
        self.assinatura.inscrever(self)

    def update(self):
        print(type(self).__name__, self.assinatura.noticia)


class Email(Assinar):

    def __init__(self, assinatura):
        self.assinatura = assinatura
        self.assinatura.inscrever(self)

    def update(self):
        print(type(self).__name__,  self.assinatura.noticia)


canal_de_noticia = CanalDeNoticia()

sms = SMS(canal_de_noticia)
email = Email(canal_de_noticia)

print('Inscritos', canal_de_noticia.inscritos())

print('#### Adicionando noticia ####')
canal_de_noticia.adicionar_noticia('Noticia 1')
print('#### Noticia adicionada ####')

print('#### Notificar inscritos ####')
canal_de_noticia.notificar_inscritos()


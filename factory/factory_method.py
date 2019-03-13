from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):

    @abstractmethod
    def descricao(self):
        pass


class Album(Secao):

    def descricao(self):
        return 'Seção de Album'


class Descricao(Secao):

    def descricao(self):
        return 'Seção de Descrição pessoal'


class Postagem(Secao):

    def descricao(self):
        return 'Seção de Postagens'


class Projetos(Secao):

    def descricao(self):
        return 'Seção de Projetos'


class RedeSocialFactory(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil_rede_social()

    @abstractmethod
    def criar_perfil_rede_social(self):
        pass

    def adiciona_secao(self, secao):
        self.secoes.append(secao)

    def retorna_secoes(self):
        return self.secoes


class Facebook(RedeSocialFactory):

    def criar_perfil_rede_social(self):
        self.adiciona_secao(Album())
        self.adiciona_secao(Descricao())
        self.adiciona_secao(Postagem())


class Linkedin(RedeSocialFactory):

    def criar_perfil_rede_social(self):
        self.adiciona_secao(Album())
        self.adiciona_secao(Descricao())
        self.adiciona_secao(Postagem())
        self.adiciona_secao(Projetos())


facebook = Facebook()

print("Perfil no Facebook criado com: ")
for secao in facebook.retorna_secoes():
    print(secao.descricao())

linkedin = Linkedin()

print("Perfil no Linkedin criado com: ")
for secao in linkedin.retorna_secoes():
    print(secao.descricao())


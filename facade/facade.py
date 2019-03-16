# Oferece uma interface simplificada para que o cliente não se preocupe com a complexidade dos subsistemas


class Igreja:

    def realiza_reserva(self):
        print('reserva da igreja realizada com sucesso')


class Decoracao:

    def contrata_decoracao(self):
        print('Decoração contratada')


class Grafica:

    def encomenda_convites(self):
        print('convites encomendados')


class GerenteDeEventosFacade:

    def __init__(self):
        print('Olá eu sou o gerente de eventos e vou cuidar de toda organização pra você')

    def organiza_casamento(self):
        igreja = Igreja()
        igreja.realiza_reserva()

        decoração = Decoracao()
        decoração.contrata_decoracao()

        grafica = Grafica()
        grafica.encomenda_convites()


class Noivos:

    def organiza_casamento(self):
        gerente_de_eventos = GerenteDeEventosFacade()
        gerente_de_eventos.organiza_casamento()


noivos = Noivos()
noivos.organiza_casamento()

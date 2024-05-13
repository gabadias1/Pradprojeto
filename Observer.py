class Assunto:
    def __init__(self):
        self._observadores = []

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.atualizar()

class AssuntoConcreto(Assunto):
    def __init__(self):
        super().__init__()
        self._estado = None

    def estado(self):
        return self._estado

    def estado(self, estado):
        self._estado = estado
        self.notificar()

class Observador:
    def atualizar(self):
        pass

class ObservadorConcreto(Observador):
    def atualizar(self):
        print("Observador: Estado alterado.")

if __name__ == "__main__":
    assunto = AssuntoConcreto()
    observador1 = ObservadorConcreto()
    observador2 = ObservadorConcreto()

    assunto.adicionar_observador(observador1)
    assunto.adicionar_observador(observador2)

    assunto.estado = "Novo Estado"
.

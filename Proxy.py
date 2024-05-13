class Assunto:
    def solicitar(self):
        pass

class AssuntoReal(Assunto):
    def solicitar(self):
        print("AssuntoReal: Lidando com a solicitação.")

class Proxy(Assunto):
    def __init__(self):
        self._assunto_real = AssuntoReal()

    def solicitar(self):
        print("Proxy: Lidando com a solicitação.")
        self._assunto_real.solicitar()

if __name__ == "__main__":
    proxy = Proxy()
    proxy.solicitar()
.

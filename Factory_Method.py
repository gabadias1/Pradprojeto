from abc import ABC, abstractmethod

class Produto(ABC):
    def operacao(self):
        pass

class ProdutoConcreto(Produto):
    def operacao(self):
        return "Operação do ProdutoConcreto"

class Criador(ABC):
    def metodo_de_fabrica(self):
        pass

    def alguma_operacao(self):
        produto = self.metodo_de_fabrica()
        return f"Criador: {produto.operacao()}"

class CriadorConcreto(Criador):
    def metodo_de_fabrica(self):
        return ProdutoConcreto()

if __name__ == "__main__":
    criador = CriadorConcreto()
    print(criador.alguma_operacao())
.

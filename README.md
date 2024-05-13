# Atividade de Padrão de Projeto
Este repositorio esta destinado ao trabalho sobre `padrão de projeto` para a materia de Engenharia de Software da faculdade UTFPR-CM.

## Padrões Escolhidos

### `Padrão Comportamental`: Observer

`Propósito`: O padrão Observer é utilizado quando um objeto (sujeito) precisa notificar outros objetos (observadores) sobre mudanças em seu estado.

`Solução`: Define uma relação de um-para-muitos entre os objetos, de modo que, quando o objeto sujeito muda de estado, todos os objetos observadores são notificados e atualizados automaticamente.

```python
if __name__ == "__main__":
    assunto = AssuntoConcreto()
    observador1 = ObservadorConcreto()
    observador2 = ObservadorConcreto()

    assunto.adicionar_observador(observador1)
    assunto.adicionar_observador(observador2)

    assunto.estado = "Novo Estado"
```

- Nesse trecho, utilizamos um metedo, criando um objeto `AssuntoConcreto` e dois objetos `ObservadorConcreto`. Em seguida, adicionando esses observadores ao assunto usando o método `adicionar_observador()`. Quando o estado do assunto é alterado para `"Novo Estado"`, os observadores são notificados automaticamente e o método `atualizar()` é chamado para cada observador.

### `Padrão Criacional`: Factory Method

`Propósito`: O padrão Factory Method é usado quando uma classe não pode antecipar a classe de objetos que ela deve criar.

`Solução`: Define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Isso encapsula a criação de objetos, permitindo que as subclasses alterem o tipo de objetos que serão criados.

```python
if __name__ == "__main__":
    criador = CriadorConcreto()
    print(criador.alguma_operacao())
```

-Nesse trecho, está sendo criado um objeto `CriadorConcreto` e chamando o método `alguma_operacao()`. Esse método utiliza o padrão Factory Method para criar um objeto `ProdutoConcreto` e chamar o método `operacao()` desse produto.

### `Padrão Estrutural`: Proxy

`Propósito`: O padrão Proxy é usado para controlar o acesso a um objeto complexo, adicionando funcionalidades adicionais ao acesso a esse objeto.

`Solução`: Define um objeto substituto que atua como intermediário entre o cliente e o objeto real. Isso permite controlar o acesso ao objeto real, implementar atrasos na inicialização e adicionar lógica de cache, entre outras funcionalidades.

```python
if __name__ == "__main__":
    proxy = Proxy()
    proxy.solicitar()
```

-Nesse trecho, estamos utlizando um objeto Proxy e chamando o método `solicitar()`. O proxy atua como intermediário entre o cliente e o objeto real `AssuntoReal`. Quando o método `solicitar()` é chamado no proxy, ele adiciona funcionalidades adicionais antes de passar a solicitação para o objeto real.

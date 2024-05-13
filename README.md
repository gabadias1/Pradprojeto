# Atividade de Padrão de Projeto
Este repositorio esta destinado ao trabalho sobre `padrão de projeto` para a materia de Engenharia de Software da faculdade UTFPR-CM.

## Padrões Escolhidos

### `Padrão Comportamental`: Observer

`Propósito`: O padrão Observer é utilizado quando um objeto (sujeito) precisa notificar outros objetos (observadores) sobre mudanças em seu estado.

`Solução`: Define uma relação de um-para-muitos entre os objetos, de modo que, quando o objeto sujeito muda de estado, todos os objetos observadores são notificados e atualizados automaticamente.

### `Padrão Criacional`: Factory Method

`Propósito`: O padrão Factory Method é usado quando uma classe não pode antecipar a classe de objetos que ela deve criar.

`Solução`: Define uma interface para criar um objeto, mas permite que as subclasses decidam qual classe instanciar. Isso encapsula a criação de objetos, permitindo que as subclasses alterem o tipo de objetos que serão criados.

### `Padrão Estrutural`: Proxy

`Propósito`: O padrão Proxy é usado para controlar o acesso a um objeto complexo, adicionando funcionalidades adicionais ao acesso a esse objeto.

`Solução`: Define um objeto substituto que atua como intermediário entre o cliente e o objeto real. Isso permite controlar o acesso ao objeto real, implementar atrasos na inicialização e adicionar lógica de cache, entre outras funcionalidades.

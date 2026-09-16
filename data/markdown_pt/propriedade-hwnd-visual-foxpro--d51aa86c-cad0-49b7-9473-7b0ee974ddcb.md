# Propriedade hWnd (Visual FoxPro)

Retorna um identificador para objetos Form e Toolbar definidos pelo usuário.

```foxpro
Object.hWnd
```

# Observações

O ambiente operacional Microsoft Windows identifica cada formulário em um aplicativo atribuindo a ele um identificador, ou hWnd. A propriedade hWnd é usada com chamadas à API do Windows. Muitas funções do ambiente operacional Windows exigem o hWnd da janela ativa como argumento.

O identificador retornado pela propriedade hWnd é atribuído ao formulário em tempo de execução. Portanto, o identificador pode ter um valor diferente cada vez que o formulário é executado, mas o valor permanece constante durante a vida do formulário. Se o mesmo formulário é executado várias vezes, cada instância do formulário pode ter um valor hWnd diferente.

hWnd está disponível em objetos Form e Toolbar definidos pelo usuário e é somente leitura tanto em tempo de execução quanto em tempo de design.

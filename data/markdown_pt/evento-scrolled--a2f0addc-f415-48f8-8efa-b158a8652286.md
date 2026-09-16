# Evento Scrolled

Ocorre em um controle Grid ou objeto Form ao mover barras de rolagem horizontais ou verticais ou mover uma caixa de rolagem. O evento Scrolled também ocorre para uma grade se você chamar o método DoScroll a partir de um programa. O evento Scrolled não ocorre ao pressionar as teclas de seta do teclado.

```foxpro
PROCEDURE Object.Scrolled
LPARAMETERS nDirection
```

#### Parâmetros
 **nDirection**
Especifica como o usuário rolou pelo conteúdo de um controle Grid ou um formulário. A tabela a seguir descreve os valores possíveis para nDirection . Valor O usuário rolou usando... 0 Seta para cima na barra de rolagem vertical. 1 Seta para baixo na barra de rolagem vertical. 2 Barra de rolagem vertical na área acima da caixa de rolagem. 3 Barra de rolagem vertical na área abaixo da caixa de rolagem 4 Seta para a esquerda na barra de rolagem horizontal. 5 Seta para a direita na barra de rolagem horizontal. 6 Barra de rolagem horizontal na área à esquerda da caixa de rolagem. 7 Barra de rolagem horizontal na área à direita da caixa de rolagem.

# Observações

Aplica-se a: Form Object | Grid Control

A propriedade Scrollbars determina se um formulário tem barras de rolagem.

Problemas de pintura de tela podem ocorrer quando a grade ou formulário é rolado. Portanto, evite criar estados de espera, por exemplo, usando o comando WAIT WINDOW, dentro do evento Scrolled.

# Comando @ ... SCROLL

Move uma área da janela principal do Microsoft Visual FoxPro ou de uma janela definida pelo usuário para cima, para baixo, para a esquerda ou para a direita.

```foxpro
@ nRow1, nColumn1 TO nRow2, nColumn2 SCROLL
[UP | DOWN | LEFT | RIGHT]   [BY nMoveAmount]
```

#### Parâmetros
 **@ nRow1 , nColumn1 TO nRow2 , nColumn2 SCROLL**
Move uma área retangular cujo canto superior esquerdo está em nRow1, nColumn1 e o canto inferior direito está em nRow2 , nColumn2 .
**UP | DOWN | LEFT | RIGHT**
Especifica a direção na qual a área retangular é movida. Se você omitir uma cláusula de direção, a área é movida para cima.
**BY nMoveAmount**
Especifica o número de linhas ou colunas pelas quais a área retangular é movida. Se você omitir BY nMoveAmount , a região é movida por uma linha ou coluna.

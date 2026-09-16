# Comando SCROLL

Rola uma área da janela principal do Visual FoxPro ou de uma janela definida pelo usuário para cima, para baixo, para a esquerda ou para a direita.

```foxpro
SCROLL nRow1, nColumn1, nRow2, nColumn2, nRowsScrolled
    [, nColumnsScrolled]
```

#### Parâmetros
 **nRow1 , nColumn1 , nRow2 , nColumn2**
Especifica a região retangular onde a rolagem ocorre na janela principal do Visual FoxPro ou na janela definida pelo usuário ativa. nRow1 , nColumn1 especifica o canto superior esquerdo da região, e nRow2 , nColumn2 especifica o canto inferior direito.
**nRowsScrolled**
Especifica o número de linhas para cima ou para baixo a rolar dentro da região retangular. Se a expressão numérica nRowsScrolled for positiva, o Visual FoxPro rola para cima o número de linhas. Se nRowsScrolled for negativa, o Visual FoxPro rola para baixo o número de linhas. Se nRowsScrolled for 0 e você omitir nColumnsScrolled , o Visual FoxPro limpa a região retangular.
**nColumnsScrolled**
Especifica o número de colunas para a esquerda ou para a direita a rolar dentro da região retangular. Se a expressão numérica nColumnsScrolled for positiva, o Visual FoxPro rola para a direita o número de colunas. Se nColumnsScrolled for negativa, o Visual FoxPro rola para a esquerda o número de colunas. Se você incluir nRowsScrolled e nColumnsScrolled , o Visual FoxPro rola a área diagonalmente.

# Exemplo

O comando a seguir rola uma pequena região retangular:

```foxpro
CLEAR
@ 4, 1 FILL TO 10, 8 COLOR GR+/B
WAIT WINDOW 'Press key to scroll left top corner'
SCROLL 0, 0, 5, 5, -2, 1
```

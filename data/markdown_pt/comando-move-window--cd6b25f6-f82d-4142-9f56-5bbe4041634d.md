# Comando MOVE WINDOW

Move uma janela definida pelo usuário criada com DEFINE WINDOW, ou uma janela de sistema do Visual FoxPro (como a janela Command ou a janela Browse) para um novo local.

```foxpro
MOVE WINDOW WindowName TO nRow1, nColumn1   | BY nRow2, nColumn2 | CENTER
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela a mover.
**TO nRow1 , nColumn1**
Move a janela para um local, especificado por nRow1 , nColumn1 , na janela principal do Visual FoxPro ou em uma janela definida pelo usuário.
**BY nRow2 , nColumn2**
Move uma janela para um local relativo à sua posição atual. A expressão numérica nRow2 especifica o número de linhas para mover a janela (para baixo se nRow2 for positivo, para cima se negativo). A expressão numérica nColumn2 especifica o número de colunas para mover a janela (para a direita se nColumn2 for positivo, para a esquerda se negativo).
**CENTER**
Centraliza uma janela na janela principal do Visual FoxPro ou em sua janela pai.

# Observações

Uma janela pode ser movida para uma posição específica ou relativa à sua posição atual. Se uma janela está definida, ela pode ser movida; não precisa estar ativa ou visível.

Para mover uma janela de sistema e/ou uma barra de ferramentas (no Visual FoxPro), coloque o nome inteiro da janela de sistema ou da barra de ferramentas entre aspas. Por exemplo, para mover a barra de ferramentas Report Controls (quando não estiver encaixada) no Visual FoxPro, emita o seguinte comando:

```foxpro
MOVE WINDOW "Report Controls" BY 1,1
```

Historicamente em versões anteriores do Visual FoxPro, a janela Data Session sempre foi referida como a janela View. Além disso, a linguagem usada para controlar essa janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a essa janela como a janela View. O Visual FoxPro continua a se referir à janela View para o comando MOVE WINDOW.

# Exemplo

No exemplo a seguir, depois que a janela chamada `wEnter` é definida e ativada, a janela é movida.

```foxpro
DEFINE WINDOW wEnter FROM 10,4 TO 15,54 SYSTEM ;
   TITLE "Nomadic Window"
ACTIVATE WINDOW wEnter
WAIT WINDOW 'Press any key to move the window'
MOVE WINDOW wEnter TO 20,15
WAIT WINDOW 'Press any key to center the window'
MOVE WINDOW wEnter CENTER
WAIT WINDOW 'Press any key to release the window'
RELEASE WINDOW wEnter
```

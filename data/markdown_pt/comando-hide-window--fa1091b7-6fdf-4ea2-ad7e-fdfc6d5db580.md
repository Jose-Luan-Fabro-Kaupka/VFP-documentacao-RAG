# Comando HIDE WINDOW

Oculta uma janela definida pelo usuário ativa ou uma janela de sistema do Microsoft Visual FoxPro.

```foxpro
HIDE WINDOW WindowName1 [, WindowName2 ... ] | ALL | SCREEN
   [ IN [WINDOW] WindowNameN | IN [WINDOW] SCREEN | IN [WINDOW]
   [BOTTOM | TOP | SAME]
```

#### Parâmetros
 **WindowName1 [, WindowName2 ...]**
Especifica o nome da janela ou uma lista de janelas (separadas por vírgulas) a ocultar. Se você emitir HIDE WINDOW sem argumentos, a janela ativa é ocultada. No Visual FoxPro, você pode especificar o nome de uma barra de ferramentas para ocultar. Consulte Comando SHOW WINDOW para uma lista de nomes de barras de ferramentas do Visual FoxPro.
**ALL**
Oculta todas as janelas.
**SCREEN**
Oculta a janela principal do Visual FoxPro. Para exibir a janela principal do Visual FoxPro novamente, emita ACTIVATE WINDOW SCREEN ou SHOW WINDOW SCREEN.
**IN [WINDOW] WindowNameN**
Oculta a janela dentro de uma janela pai.
**IN [WINDOW] SCREEN**
Oculta explicitamente uma janela na janela principal do Visual FoxPro.
**BOTTOM | TOP | SAME**
Especifica onde as janelas são ocultadas em relação a outras janelas. BOTTOM coloca uma janela atrás de todas as outras janelas. TOP (o padrão) coloca uma janela na frente de todas as outras janelas. SAME oculta uma janela sem afetar sua posição da frente para trás. Para preservar as posições relativas de múltiplas janelas ocultas quando elas forem exibidas novamente com SHOW WINDOW ALL, inclua a palavra-chave SAME ao ocultar as janelas.

# Observações

HIDE WINDOW remove uma janela ou um conjunto de janelas da janela principal do Visual FoxPro ou de uma janela definida pelo usuário. Você pode usar HIDE WINDOW para ocultar janelas de sistema, como a janela Command, a janela Data Session e assim por diante.

Ocultar uma janela não é o mesmo que fechá-la. Quando uma janela é ocultada, ela permanece residente na memória e continua ativa. A saída pode ser enviada a uma janela oculta, mas você não pode vê-la.

Liberar uma janela a remove da memória. Janelas removidas da memória devem ser definidas novamente para serem exibidas novamente. Uma janela pode ser exibida com ACTIVATE WINDOW ou SHOW WINDOW.

Para ocultar uma janela de sistema ou uma barra de ferramentas (no Visual FoxPro), coloque o nome completo da janela de sistema ou barra de ferramentas entre aspas. Por exemplo, para ocultar a barra de ferramentas Report Controls no Visual FoxPro, emita o seguinte comando:

```foxpro
HIDE WINDOW "Report Controls"
```

Historicamente, em versões anteriores do Visual FoxPro, a janela Data Session sempre foi referida como a janela View. Além disso, a linguagem usada para controlar essa janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a essa janela como a janela View. O Visual FoxPro continua a se referir à janela View para o comando HIDE WINDOW.

# Exemplo

No exemplo a seguir, uma janela chamada `wOutput1` é definida e ativada. O programa aguarda que você pressione uma tecla e, em seguida, oculta a janela. O programa aguarda que você pressione uma tecla novamente e, em seguida, exibe a janela. Pressionar uma tecla pela terceira vez remove a janela da tela e da memória.

```foxpro
DEFINE WINDOW wOutput1 FROM 6,1 TO 19,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
ACTIVATE WINDOW wOutput1
WAIT WINDOW 'Press a key to hide this window'
HIDE WINDOW wOutput1
WAIT WINDOW 'Press a key to see the window again'
SHOW WINDOW wOutput1
WAIT WINDOW 'Press a key to remove the window from memory'
DEACTIVATE WINDOW wOutput1
RELEASE WINDOW wOutput1
```

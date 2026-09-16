# Comando DEACTIVATE WINDOW

Desativa janelas definidas pelo usuário ou do sistema Visual FoxPro e as remove da tela, mas não da memória.

```foxpro
DEACTIVATE WINDOW WindowName1 [, WindowName2 ...] | ALL
```

#### Parâmetros
 **WindowName1 [, WindowName2 ...]**
Especifica uma ou mais janelas. Podem ser janelas do sistema, como Command ou Browse.
**ALL**
Desativa todas as janelas ativas. Para exibir novamente a janela principal, escolha Visual FoxPro Screen no menu Window ou execute ACTIVATE WINDOW SCREEN ou SHOW WINDOW SCREEN.

# Observações

Várias janelas definidas pelo usuário podem estar simultaneamente na janela principal, mas a saída é direcionada somente à mais recentemente ativada. Ao desativar a janela atual, seu conteúdo é limpo, ela é removida da tela e a saída subsequente vai para a janela anteriormente ativada. Se não houver uma, a saída vai para a janela principal.

Use CLEAR WINDOWS ou RELEASE WINDOWS para remover janelas da tela e da memória.

Para desativar uma janela do sistema ou barra de ferramentas, coloque o nome inteiro entre aspas. Exemplo:

```foxpro
DEACTIVATE WINDOW "Report Controls"
```

Em versões anteriores, a janela Data Session era chamada de View. A linguagem usada para controlá-la, como HIDE WINDOW, ACTIVATE WINDOW e WONTOP( ), também usa esse nome. DEACTIVATE WINDOW continua a se referir a ela como View.

# Exemplo

Uma janela chamada `wOutput1` é definida e ativada. Após exibir um registro de `customer`, o programa aguarda uma tecla e desativa a janela.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
DEFINE WINDOW wOutput1 FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
ACTIVATE WINDOW wOutput1
DISPLAY
WAIT WINDOW 'Press a key to deactivate the window'
DEACTIVATE WINDOW wOutput1
RELEASE WINDOW wOutput1
```

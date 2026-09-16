# Comando RELEASE WINDOWS

Remove janelas definidas pelo usuário ou janelas do sistema Visual FoxPro da memória.

```foxpro
RELEASE WINDOWS [WindowNameList]
```

#### Parâmetros
 **WindowNameList**
Especifica as janelas liberadas da memória. WindowNameList pode incluir tanto janelas definidas pelo usuário quanto janelas do sistema Visual FoxPro. Separe os nomes das janelas com vírgulas. Se WindowNameList não for incluída, a janela definida pelo usuário ativa é liberada.

# Observações

RELEASE WINDOWS pode ser usado para remover janelas do sistema Visual FoxPro da janela principal do Visual FoxPro ou de uma janela pai definida pelo usuário.

A lista a seguir inclui janelas do sistema que podem ser liberadas da janela principal do Visual FoxPro ou de uma janela pai.
 - Command
- Data Session (use RELEASE WINDOW "View")
- Debug
- Debug Output
- Document View
- Locals
- Trace
- Watch
- View

Para liberar uma janela do sistema e/ou uma barra de ferramentas (no Visual FoxPro), coloque o nome completo da janela do sistema ou da barra de ferramentas entre aspas. Por exemplo, para liberar a barra de ferramentas Report Controls no Visual FoxPro, execute o seguinte comando:

```foxpro
RELEASE WINDOW "Report Controls"
```

Historicamente, em versões anteriores do Visual FoxPro, a janela Data Session sempre foi referida como a janela View. Além disso, a linguagem usada para controlar esta janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a esta janela como a janela View. O Visual FoxPro continua a se referir à janela View para o comando RELEASE WINDOWS.

Use ACTIVATE WINDOW para colocar uma janela do sistema na janela principal do Visual FoxPro ou em uma janela definida pelo usuário.

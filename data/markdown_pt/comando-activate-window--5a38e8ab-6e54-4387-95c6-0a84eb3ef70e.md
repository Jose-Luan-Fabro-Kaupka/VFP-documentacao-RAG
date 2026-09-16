# Comando ACTIVATE WINDOW

Exibe e ativa uma ou mais janelas definidas pelo usuário ou janelas de sistema do Visual FoxPro.

```foxpro
ACTIVATE WINDOW WindowName1 [, WindowName2 ...]
| ALL   [IN [WINDOW] WindowName3 | IN SCREEN
[BOTTOM | TOP | SAME]    [NOSHOW]
```

#### Parâmetros
 **WindowName1 [, WindowName2 ...]**
Especifica o nome de cada janela a ativar. Separe os nomes das janelas com vírgulas. No Visual FoxPro, você pode especificar o nome de uma barra de ferramentas a ativar. Consulte Comando SHOW WINDOW para uma lista de nomes de barras de ferramentas do Visual FoxPro.
**ALL**
Especifica que todas as janelas são ativadas. A última janela ativada é a janela de saída ativa.
**IN [WINDOW] WindowName3**
Especifica o nome da janela pai na qual a janela é colocada e ativada. A janela ativada torna-se uma janela filha. Uma janela pai pode ter várias janelas filhas. Uma janela filha ativada dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai é movida, a janela filha se move com ela. Observação A janela pai deve estar visível para que qualquer de suas janelas filhas esteja visível.
**IN SCREEN**
Coloca e ativa uma janela na janela principal do Visual FoxPro. Uma janela pode ser colocada em uma janela pai incluindo IN WINDOW em DEFINE WINDOW quando a janela é criada. Incluir a cláusula IN SCREEN em ACTIVATE WINDOW substitui a cláusula IN WINDOW em DEFINE WINDOW.
**BOTTOM | TOP | SAME**
Especifica onde as janelas são ativadas em relação a outras janelas ativadas anteriormente. Por padrão, uma janela torna-se a janela superior quando é ativada. Incluir BOTTOM coloca uma janela atrás de todas as outras janelas. TOP coloca-a na frente de todas as outras janelas. SAME ativa uma janela sem afetar sua posição de frente para trás.
**NOSHOW**
Ativa e direciona a saída para uma janela sem exibir a janela.

# Observações

Para usar este comando com sucesso em janelas definidas pelo usuário, qualquer janela definida pelo usuário de destino deve ter sido criada usando o comando DEFINE WINDOW.

Ativar uma janela torna-a a janela superior e direciona toda a saída para essa janela. A saída pode ser direcionada para apenas uma janela por vez. Uma janela permanece a janela de saída ativa até ser desativada ou liberada, ou até que outra janela ou a janela principal do Visual FoxPro seja ativada.

Os nomes das janelas definidas pelo usuário aparecem na seção inferior do menu Janela. O nome da janela definida pelo usuário ativa é marcado com uma marca de seleção.

Mais de uma janela pode ser colocada na janela principal do Visual FoxPro ao mesmo tempo, mas a saída é direcionada apenas para a última janela ativada. Quando mais de uma janela está aberta, desativar a janela de saída ativa remove-a da janela principal do Visual FoxPro e envia a saída subsequente para outra janela. Se não houver janela de saída ativa, a saída é direcionada para a janela principal do Visual FoxPro.

> **Observação:** Para garantir que a saída seja direcionada para uma janela específica quando você desativa a janela de saída ativa, você deve ativar explicitamente a janela para a qual deseja enviar saída com ACTIVATE WINDOW.

Todas as janelas ativadas são exibidas até que DEACTIVATE WINDOW ou HIDE WINDOW seja emitido para removê-las da visualização. Emitir qualquer um dos comandos remove as janelas da visualização, mas não da memória. As janelas podem ser exibidas novamente emitindo ACTIVATE WINDOW ou SHOW WINDOW.

Para remover janelas da visualização e da memória, use CLEAR WINDOWS, RELEASE WINDOWS ou CLEAR ALL. Janelas que são removidas da memória devem ser redefinidas para serem colocadas novamente na janela principal do Visual FoxPro.

Você pode usar ACTIVATE WINDOW para colocar janelas de sistema do Visual FoxPro na janela principal do Visual FoxPro ou em uma janela pai.

As janelas de sistema a seguir podem ser abertas com ACTIVATE WINDOW:
 - Command
- Call Stack
- Debug
- Debug Output
- Document View
- Locals
- Trace
- Watch
- View

Para ativar uma janela de sistema e/ou uma barra de ferramentas, coloque o nome completo da janela de sistema ou barra de ferramentas entre aspas. Por exemplo, para ativar a janela de depuração Call Stack no Visual FoxPro, emita o comando a seguir:

```foxpro
ACTIVATE WINDOW "Call Stack"
```

Historicamente, em versões anteriores do Visual FoxPro, a janela Data Session sempre foi referida como a janela View. Além disso, a linguagem usada para controlar esta janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a esta janela como a janela View. O Visual FoxPro continua a se referir à janela View para o comando ACTIVATE WINDOW.

Use HIDE WINDOW ou RELEASE WINDOW para remover uma janela de sistema da janela principal do Visual FoxPro ou de uma janela pai.

# Exemplo

O exemplo a seguir define uma janela chamada `output` e a ativa, colocando-a na janela principal do Visual FoxPro. O comando WAIT pausa a execução, a janela é ocultada e depois exibida novamente.

```foxpro
CLEAR
DEFINE WINDOW output FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
ACTIVATE WINDOW output
WAIT WINDOW 'Press any key to hide window output'
HIDE WINDOW output
WAIT WINDOW 'Press any key to show window output'
SHOW WINDOW output
WAIT WINDOW 'Press any key to release window output'
RELEASE WINDOW output
```

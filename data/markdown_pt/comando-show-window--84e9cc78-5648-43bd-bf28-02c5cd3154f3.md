# Comando SHOW WINDOW

Exibe uma ou mais janelas definidas pelo usuário ou janelas do sistema Visual FoxPro sem ativá-las.

```foxpro
SHOW WINDOW WindowName1 [, WindowName2 ...] | ALL | SCREEN
   [IN [WINDOW] WindowName3   [REFRESH]   [TOP | BOTTOM | SAME]   [SAVE]
```

#### Parâmetros
 **WindowName1 [, WindowName2 ...]**
Especifica o nome de uma ou mais janelas a exibir.
**ALL**
Exibe todas as janelas definidas pelo usuário.
**SCREEN**
Exibe a janela principal do Visual FoxPro quando está oculta. Você também pode escolher Screen no menu Window para exibir a janela principal do Visual FoxPro. Você pode ocultar a janela principal do Visual FoxPro clicando na caixa de fechamento ou emitindo DEACTIVATE WINDOW SCREEN, HIDE WINDOW SCREEN ou RELEASE WINDOW SCREEN.
**IN [WINDOW] WindowName3**
Exibe a janela dentro de uma janela pai especificada com WindowName3. A janela não assume as características da janela pai. Uma janela exibida dentro de uma janela pai não pode ser movida para fora da janela pai. Se a janela pai é movida, a janela filha se move com ela. A janela pai especificada com WindowName3 deve primeiro ser criada com DEFINE WINDOW.
**IN SCREEN**
Exibe explicitamente a janela na janela principal do Visual FoxPro em vez de em outra janela. Janelas são colocadas na janela principal do Visual FoxPro por padrão.
**REFRESH**
Redesenha uma Browse window. Esta opção é útil em uma rede para garantir que você está navegando na versão mais atual de uma tabela. A área de trabalho para a tabela da Browse window é selecionada. Janelas de edição de memo são atualizadas com alterações feitas no campo memo por outros usuários em uma rede. SET REFRESH determina o intervalo entre atualizações de janelas de edição de memo. Consulte SET REFRESH para informações adicionais sobre como os dados são atualizados em tabelas abertas para uso compartilhado em uma rede.
**TOP**
Coloca a janela especificada na frente de todas as outras janelas.
**BOTTOM**
Coloca a janela especificada atrás de todas as outras janelas.
**SAME**
Coloca a janela especificada de volta em uma pilha de janelas na mesma posição que a janela ocupava antes de ser desativada. SAME afeta apenas janelas que foram previamente exibidas ou ativadas e depois removidas da janela principal do Visual FoxPro com DEACTIVATE WINDOW.
**SAVE**
Mantém uma imagem da janela na janela principal do Visual FoxPro ou em outra janela depois que a janela é liberada. Normalmente, janelas são removidas da janela principal do Visual FoxPro depois que são liberadas. A imagem da janela pode ser removida da janela principal do Visual FoxPro ou de uma janela com CLEAR.

# Observações

SHOW WINDOW controla a exibição e a colocação da frente para trás na tela das janelas. Se uma janela está oculta ou não foi ativada, SHOW WINDOW exibe a janela sem ativá-la. Se uma ou mais janelas estão atualmente exibidas, SHOW WINDOW permite alterar a ordem da frente para trás das janelas.

Você também pode exibir janelas do sistema, como a Command window.

No Visual FoxPro, você pode usar SHOW WINDOW para exibir as toolbars do Visual FoxPro. Use HIDE WINDOW para remover uma toolbar da janela do FoxPro. Toolbars devem estar ativas antes de poderem ser exibidas. A tabela a seguir lista os nomes das toolbars do Visual FoxPro para usar em SHOW WINDOW e HIDE WINDOW. Coloque o nome da toolbar entre aspas.

| Nomes de toolbars | | |
| --- | --- | --- |
| Color Palette | Layout | Report Designer |
| Database Designer | Print Preview | Standard |
| Form Controls | Query Designer | View Designer |
| Form Designer | Report Controls | |

Para mostrar uma janela do sistema, coloque o nome completo da janela do sistema entre aspas.

Você não pode especificar onde a saída é direcionada para janelas definidas pelo usuário com SHOW WINDOW. Use ACTIVATE WINDOW para direcionar saída para uma janela definida pelo usuário criada com DEFINE WINDOW.

Historicamente em versões anteriores do Visual FoxPro, a Data Session window sempre foi referida como a View window. Além disso, a linguagem usada para controlar esta janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a esta janela como a View window. O Visual FoxPro continua a referenciar a View window para o comando SHOW WINDOW.

# Exemplo

No exemplo a seguir, uma janela chamada `wOutput1` é criada e exibida. Como SHOW WINDOW é usado para exibir a janela, a saída não pode ser direcionada para a janela até que seja ativada.

```foxpro
CLEAR
DEFINE WINDOW wOutput1 FROM 2,1 TO 13,75 TITLE 'Output' ;
   CLOSE FLOAT GROW ZOOM
SHOW WINDOW wOutput1
```

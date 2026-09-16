# Comando WAIT

Exibe uma mensagem e pausa a execução do Visual FoxPro até que o usuário pressione uma tecla ou clique no mouse.

```foxpro
WAIT [cMessageText] [TO VarName] [WINDOW [AT nRow, nColumn]] [NOWAIT]
   [CLEAR | NOCLEAR] [TIMEOUT nSeconds]
```

#### Parâmetros
 **cMessageText**
Especifica uma mensagem personalizada a exibir. Você pode especificar qualquer função, objeto ou tipo de dados válido do Visual FoxPro em vez de cMessageText . Se você omitir cMessageText , o Visual FoxPro exibe a mensagem padrão. Se cMessageText for uma cadeia de caracteres vazia (""), o Visual FoxPro não exibe uma mensagem e aguarda até que uma tecla seja pressionada antes de continuar a execução do programa. O comprimento de cMessageText pode ser de até 255 caracteres. Observação O Visual FoxPro converte referências de objeto para a cadeia de caracteres "(Object)". Se a função que você especificar avaliar para um valor não caractere, o Visual FoxPro usa automaticamente a função TRANSFORM( ) para fornecer o equivalente em caractere. No exemplo a seguir, uma data do tipo caractere é retornada e passada para WAIT WINDOW : WAIT DATE() WINDOW AT 20,20 TIMEOUT 10
**TO VarName**
Salva a tecla pressionada em uma variável ou um elemento de matriz. Se a variável ou um elemento de matriz que você especificar com VarName não existir, ele é criado. A cadeia de caracteres vazia é armazenada em VarName se você pressionar ENTER ou uma tecla ou combinação de teclas não imprimível, ou clicar no mouse.
**WINDOW**
Exibe a mensagem em uma janela de mensagem do sistema localizada no canto superior direito da janela principal do Visual FoxPro. A janela pode ser temporariamente ocultada pressionando a tecla CTRL ou SHIFT. A partir do Visual FoxPro 7, os atributos de fonte principais, incluindo nome da fonte, tamanho da fonte e estilo da fonte, são derivados das características de fonte especificadas na guia Aparência do Painel de controle de exibição do Windows.
**AT nRow , nColumn**
No Visual FoxPro, especifica a posição da janela de mensagem na tela.
**NOWAIT**
Continua a execução do programa imediatamente após a mensagem ser exibida. O programa não aguarda que a mensagem seja removida da janela principal do Visual FoxPro, mas continua executando na linha do programa imediatamente após a linha do programa que contém WAIT NOWAIT. Se você omitir NOWAIT, a execução do programa pausa até que a mensagem seja removida da janela principal do Visual FoxPro pressionando uma tecla ou clicando no mouse.
**CLEAR**
Remove uma janela do sistema Visual FoxPro ou uma janela de mensagem WAIT da janela principal do Visual FoxPro de dentro de um programa. Por exemplo, talk de indexação, classificação e assim por diante é direcionado para uma janela do sistema Visual FoxPro se você emitir SET TALK WINDOW. A janela pode ser removida interativamente se você pressionar uma tecla ou mover o mouse. Emita WAIT CLEAR para remover a janela de dentro de um programa.
**NOCLEAR**
Especifica que uma janela de mensagem WAIT permanece na janela principal do Visual FoxPro até que WAIT CLEAR ou outro comando WAIT WINDOW seja emitido, ou uma mensagem do sistema Visual FoxPro seja exibida.
**TIMEOUT nSeconds**
Especifica o número de segundos que podem decorrer sem entrada do teclado ou do mouse antes que o WAIT seja encerrado. nSeconds especifica o número de segundos, as frações de segundos que são permitidas, que decorrem. Se TIMEOUT não for a última cláusula em WAIT, o Visual FoxPro gera uma mensagem de erro de sintaxe.

# Observações

Se uma mensagem WAIT é exibida no Visual FoxPro para Windows, pressionar as teclas SHIFT ou CTRL oculta todas as janelas, incluindo a mensagem WAIT.

# Guia Debug, caixa de diálogo Options

Permite definir opções para personalizar as janelas do depurador do Visual FoxPro, incluindo:
 - Fonte e cores.
- Se o código de evento Timer deve ser rastreado.
- Se os números de linha são exibidos.
- Se a saída da janela Debug Output deve ser registrada em um arquivo.

Quando você escolhe Set As Default — que aparece em cada guia da caixa de diálogo — o Visual FoxPro salva as configurações de opção no registro (banco de dados de registro do sistema Windows).
 **Environment**
Especifica o ambiente de depuração. Debug frame Todas as janelas do depurador aparecem em um grande frame externo à janela principal do Visual FoxPro, com seus próprios menus e toolbars. Isso torna o depurador menos intrusivo no ambiente de tempo de execução do seu aplicativo. Se você escolher esta opção, pode abrir o depurador escolhendo Debugger no menu Tools. FoxPro frame As janelas do depurador aparecem na janela principal do Visual FoxPro. O ambiente FoxPro é mais útil se você deseja apenas uma única janela aberta, por exemplo a janela Watch. Se você escolher esta opção, o Visual FoxPro substitui o comando Debugger no menu Tools por comandos para abrir janelas de depuração individuais, e toolbars para janelas de depuração individuais são organizadas em mosaico na janela principal do Visual FoxPro. Observação Você não pode alterar esta opção se o depurador completo ou qualquer janela do depurador estiver aberta, ou se a toolbar de depuração estiver aberta na área de trabalho do Visual FoxPro.
**Display timer events**
Escolha esta opção se desejar que os eventos de timer do Timer Control sejam exibidos na Trace Window quando seu valor de intervalo for atingido. Se você desmarcar esta opção, o evento de timer ainda ocorre, mas não é exibido; é tratado como se você tivesse especificado Step Over para esse evento. Com esta caixa de seleção desmarcada, o Visual FoxPro filtra eventos de timer mesmo quando você está percorrendo um evento de timer no momento. Isso é intencional. O Visual FoxPro entra dentro de um evento de timer nas seguintes situações: SET STEP está ON. Um breakpoint está definido em uma linha de código. Um breakpoint está definido em um valor que é alterado. Um novo método ou procedimento é chamado.

# Specify Window

Escolha uma opção para especificar para qual janela do depurador você deseja definir opções. A janela que você escolher aqui afeta as opções disponíveis a seguir.
 **Call Stack**
Exibe as seguintes opções para a janela: Show call stack order Exibe um número ao lado de cada programa listado na Call Stack Window, com o número mais alto indicando o programa em execução no momento. Show current line indicator Indica se o indicador de linha atual é exibido na janela Call Stack. Show Call Stack indicator Indica se uma seta é exibida na janela Call Stack para indicar o procedimento exibido na Trace Window. Se os procedimentos de linha atual e call stack são os mesmos, o Visual FoxPro exibe apenas o indicador de linha atual.
**Locals**
Nenhuma opção adicional está disponível para esta janela.
**Output**
Exibe a área Log debug output, que contém as seguintes opções: Log Debug Output Copia os valores escritos na Debug Output Window para um arquivo de texto. Se você escolher registrar valores de saída, precisa especificar um arquivo para registrá-los. A extensão de arquivo padrão para um arquivo de log é .log. O Visual FoxPro registrará a saída em um arquivo apenas se a janela Output estiver exibida. Você pode exibir informações na janela Output (e enviá-las para o arquivo de log) usando o comando DEBUGOUT ou o comando SET PRINTER em um programa. Quando você sai do Visual FoxPro, esta opção é desmarcada, para que você não substitua inadvertidamente um arquivo de log na próxima vez que iniciar o Visual FoxPro. Append Especifica que a saída de depuração é escrita após o conteúdo atual de um arquivo existente, preservando o conteúdo original. Overwrite Especifica que a saída de depuração substitui o conteúdo do arquivo especificado.
**Trace**
Exibe as seguintes opções para a janela: Show line numbers Exibe números de linha à esquerda das linhas de código na Trace Window. Trace between breakpoints Executa código entre breakpoints na velocidade do throttle. A velocidade do throttle indica a pausa em segundos entre a execução de cada linha de código. Se você desmarcar esta opção, o código entre breakpoints é executado na velocidade normal, a configuração padrão da variável de sistema _THROTTLE, que é 0. Equivalente a usar o comando SET TRBETWEEN. Pause between line execution Define o throttle, que é o atraso em segundos entre a execução de cada linha de código. Esta opção permite reduzir a velocidade de execução do programa para que você possa observar as linhas de código sem precisar percorrer cada linha individualmente. Trace between breakpoints deve estar ativado para que esta configuração tenha algum efeito. Equivalente a definir a variável de sistema _THROTTLE.
**Watch**
Nenhuma opção adicional está disponível para esta janela.
**Font**
Escolha uma fonte e estilo para a janela do depurador especificada. Por exemplo, para definir a fonte da janela Trace do depurador, escolha Trace em Specify Window e então escolha Font para selecionar a fonte, tamanho e estilo.

# Colors
 **Area**
Selecione o elemento de texto para o qual deseja especificar uma cor. Por exemplo, para especificar uma cor para o texto usado para valores alterados, selecione ChangedValue. As opções na lista Area dependem de qual janela foi especificada em Specify Window.
**Foreground**
Escolha uma cor para o texto da área selecionada. Para usar a cor padrão estabelecida no painel de controle do Windows, selecione Automatic.
**Background**
Escolha uma cor de fundo para a área selecionada. Por exemplo, para mostrar comentários em texto amarelo sobre fundo azul, selecione amarelo em Foreground e azul em Background. Para usar a cor padrão estabelecida no painel de controle do Windows, selecione Automatic.

Para obter mais informações, consulte Testing and Debugging Applications.

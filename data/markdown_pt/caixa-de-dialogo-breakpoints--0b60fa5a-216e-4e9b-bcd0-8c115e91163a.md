# Caixa de diálogo Breakpoints

Permite especificar opções para pontos de interrupção.

Esta caixa de diálogo aparece quando você escolhe Breakpoints no menu Tools da janela Debugger.
**Type**
O tipo de ponto de interrupção. Escolha uma das seguintes configurações: Configuração Descrição Break at location Interrompe a execução em uma linha de código. Break at location if expression is true Interrompe a execução em uma linha de código quando uma expressão se torna verdadeira. Break when ' Interrompe a execução quando uma expressão se torna verdadeira. Break when expression has changed Interrompe a execução quando o valor de uma expressão muda.
**Location**
Onde suspender a execução. O local pode ser um programa, um procedimento ou um método ou evento específico. Você pode suspender a execução do programa em uma linha específica do local incluindo o número da linha depois do local e de uma vírgula. Dica: para exibir números de linha na janela Trace, escolha Show line numbers na guia Debug da caixa de diálogo Options.
**File**
O arquivo em que o local se encontra. O arquivo pode ser um arquivo de programa, formulário ou classe. Se você não especificar um nome de arquivo, o ponto de interrupção será avaliado para qualquer método ou procedimento com o mesmo nome daquele informado na caixa Location.
**Pass Count**
Número de vezes que a linha de código na caixa Location deve ser executada antes que a execução do programa seja suspensa. Dica: use Pass Count com loops que apresentam problemas somente depois de determinado número de iterações.
**Expression**
Qualquer expressão válida do Visual FoxPro. Ao escolher Break when expression is true ou Break at location if expression is true na lista Type, especifique a expressão aqui.
**Breakpoints**
Lista todos os pontos de interrupção adicionados. Os pontos de interrupção ativados são marcados com uma marca de seleção e podem ser alternados com os botões Enable e Disable. Todos os pontos de interrupção exibidos na lista Breakpoints são salvos em um arquivo de configuração de depuração quando você escolhe Save Configuration no menu File da janela Debugger.
**Add**
Adiciona à lista Breakpoints o ponto de interrupção especificado pelas caixas Type, Location, File, Pass Count e Expression. Somente os pontos de interrupção adicionados são salvos quando você fecha a caixa de diálogo.
**Remove**
Remove da lista Breakpoints o ponto de interrupção selecionado.
**Disable**
Remove a marca de seleção ao lado do ponto de interrupção selecionado na lista Breakpoints. Quando você desativa um ponto de interrupção, a execução do programa não é suspensa no local ou na condição especificada.
**Enable**
Define a marca de seleção ao lado do ponto de interrupção selecionado na lista Breakpoints e o ativa.
**Clear All**
Remove todos os pontos de interrupção da lista Breakpoints.
**Display Breakpoint Messages**
Permite alternar a exibição das caixas de mensagem de ponto de interrupção quando um ponto de interrupção é encontrado. As mensagens não são exibidas quando o ponto de interrupção break at location é encontrado.

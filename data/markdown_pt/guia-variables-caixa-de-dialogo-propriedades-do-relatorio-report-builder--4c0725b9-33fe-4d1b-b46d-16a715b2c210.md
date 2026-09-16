# Guia Variables, caixa de diálogo Propriedades do relatório (Report Builder)

Permite criar, alterar ou excluir variáveis para um relatório ou etiqueta. Você também pode alterar a ordem em que as variáveis de relatório são avaliadas.

Esta guia é pré-selecionada quando você escolhe Variables no menu Report ou no menu de contexto do layout de relatório.

> **Observação:** Esta guia substitui a funcionalidade da Caixa de diálogo Variáveis de relatório nativa do Visual FoxPro quando o Report Builder está ativo.
 - Como: definir variáveis de relatório
- Como: alterar a ordem das variáveis de relatório
- Como: redefinir variáveis de relatório
 **Variables**
Exibe os nomes das variáveis definidas no layout de relatório e permite alterar a ordem de avaliação das variáveis de relatório.
**Add**
Abre uma caixa de entrada para especificar o nome de uma nova variável de relatório.
**Remove**
Exclui a variável atualmente selecionada na caixa de listagem Variables.
**Value to store**
Especifica uma expressão usada para determinar o valor da variável de relatório durante uma execução de relatório. O mecanismo de relatório avalia esta expressão cada vez que move o ponteiro de registro ao processar os registros no escopo atual. Clicar no botão de reticências (…) abre o Expression Builder para que você possa construir uma expressão. Para obter mais informações, consulte Caixa de diálogo Expression Builder .
**Initial value**
Especifica uma expressão usada para determinar o valor inicial da variável de relatório. Clicar no botão de reticências (…) abre o Expression Builder .
**Reset value based on**
Especifica o ponto em que redefinir a variável para seu valor inicial. O valor padrão é End of Report . Observação Se você especificou grupos de dados no relatório, bandas Detail ou expressões de alias de destino para bandas Detail, a lista Reset value based on exibe esses itens.
**Calculation type**
Especifica cálculos adicionais a realizar ao determinar o próximo valor da variável de relatório conforme o mecanismo de relatório move o ponteiro de registro durante uma execução de relatório. Observação Cálculos cumulativos são redefinidos dependendo da opção Reset value based on. None O resultado da expressão Value to store é atribuído diretamente ao valor da variável de relatório. Count O valor da variável de relatório é incrementado em 1. (A expressão Value to store não é avaliada.) Sum Adiciona o resultado da expressão Value to store ao valor atual da variável de relatório. Average Calcula a média aritmética do resultado da expressão Value to store para cada registro percorrido até então e atribui à variável de relatório. (O valor Initial da variável de relatório não é incluído neste cálculo.) Lowest Compara o valor atual da variável de relatório com o resultado da expressão Value to store e atribui o menor dos dois valores à variável de relatório. Highest Compara o valor atual da variável de relatório com o resultado da expressão Value to store e atribui o maior dos dois valores à variável de relatório. Std Deviation Calcula a raiz quadrada da variância do resultado da expressão Value to store para cada registro percorrido até então e atribui à variável de relatório. (O valor Initial da variável de relatório não é incluído neste cálculo.) Variance Mede o grau em que o resultado da expressão Value to store varia da média para os registros percorridos até então e atribui à variável de relatório. (O valor Initial da variável de relatório não é incluído neste cálculo.)
**Release after report**
Libera a variável de relatório da memória após o relatório ter concluído o processamento. Quando esta opção não está selecionada, a variável de relatório permanece na memória até que o Visual FoxPro seja encerrado ou os comandos CLEAR ALL ou CLEAR MEMORY sejam chamados. Para obter mais informações, consulte Comandos CLEAR

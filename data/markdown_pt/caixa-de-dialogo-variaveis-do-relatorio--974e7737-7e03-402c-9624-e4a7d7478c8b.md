# Caixa de diálogo Variáveis do relatório

A caixa de diálogo Variáveis do relatório permite criar, alterar ou excluir variáveis para um relatório ou etiqueta. Você também pode alterar a ordem de avaliação das variáveis do relatório.

Esta caixa de diálogo aparece quando você escolhe Variáveis no menu de contexto de uma janela de layout de relatório ou quando clica em Variáveis no menu Relatório.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, esta caixa de diálogo pode ser substituída por uma interface alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.
 **Variáveis**
Exibe os nomes das variáveis definidas no layout do relatório e permite alterar a ordem de avaliação das variáveis do relatório arrastando o botão de movimentação.
**Valor a armazenar**
Especifica uma expressão usada para determinar o valor da variável do relatório durante a execução de um relatório. O mecanismo de relatório avalia essa expressão cada vez que move o ponteiro de registro ao processar os registros no escopo atual. Clicar no botão de reticências (…) abre o Construtor de expressões para que você possa criar uma expressão. Para obter mais informações, consulte Caixa de diálogo Construtor de expressões.
**Valor inicial**
Especifica uma expressão usada para determinar o valor inicial da variável do relatório. Clicar no botão de reticências (…) abre o Construtor de expressões. Para obter mais informações, consulte Caixa de diálogo Construtor de expressões.
**Liberar após o relatório**
Libera a variável do relatório da memória após gerar a saída do relatório. Observação Quando esta opção não está selecionada, a variável do relatório permanece na memória até que o Visual FoxPro seja encerrado ou os comandos CLEAR ALL ou CLEAR MEMORY sejam chamados. Para obter mais informações, consulte Comandos CLEAR.
**Reiniciar com base em**
Especifica o ponto em que a variável é reiniciada para seu valor inicial. O valor padrão é Fim do relatório. Observação Se você especificou grupos de dados no relatório, bandas Detail ou expressões de alias de destino para bandas Detail, a lista Reiniciar com base em exibe esses itens.
**Inserir**
Insere uma caixa de texto em branco na caixa Variáveis para que você possa digitar um novo nome de variável.
**Excluir**
Exclui a variável selecionada na caixa Variáveis.
**Calcular**
Especifica o tipo de cálculo a ser executado ao determinar o próximo valor da variável do relatório. Alguns tipos de cálculo são cumulativos conforme o mecanismo de relatório move o ponteiro de registro durante a execução de um relatório. Observação Cálculos cumulativos são reiniciados dependendo da opção Reiniciar com base em. Nenhum O resultado da expressão Valor a armazenar é atribuído diretamente ao valor da variável do relatório. Contagem O valor da variável do relatório é incrementado em 1. (A expressão Valor a armazenar não é avaliada.) Soma Adiciona o resultado da expressão Valor a armazenar ao valor atual da variável do relatório. Média Calcula a média aritmética do resultado da expressão Valor a armazenar para cada registro percorrido até o momento e a atribui à variável do relatório. (O valor inicial da variável do relatório não é incluído neste cálculo.) Menor Compara o valor atual da variável do relatório com o resultado da expressão Valor a armazenar e atribui o menor dos dois valores à variável do relatório. Maior Compara o valor atual da variável do relatório com o resultado da expressão Valor a armazenar e atribui o maior dos dois valores à variável do relatório. Desvio padrão Calcula a raiz quadrada da variância do resultado da expressão Valor a armazenar para cada registro percorrido até o momento e a atribui à variável do relatório. O valor inicial da variável do relatório não é incluído neste cálculo. Variância Mede o grau em que o resultado da expressão Valor a armazenar varia da média dos registros percorridos até o momento e o atribui à variável do relatório. O valor inicial da variável do relatório não é incluído neste cálculo.

# Caixa de diálogo Opções de impressão de relatório e etiqueta

Especifica opções de impressão para relatórios e etiquetas.

Esta caixa de diálogo aparece ao clicar em Opções na caixa de diálogo Opções de impressão. Para obter mais informações, consulte Caixa de diálogo Opções de impressão.
 **Scope**
Especifica o intervalo de registros a imprimir. Ao selecionar Next ou Record na lista Scope, digite ou selecione um número na caixa de rotação para especificar o próximo número de registros ou um número de registro. As configurações disponíveis para a configuração Scope são as seguintes: All Imprime todos os registros do arquivo de origem. Next Imprime um intervalo de registros começando com 1. Record Imprime um número de registro específico. Rest Imprime o registro atual e todos os posteriores até o final do arquivo.
**For**
Especifica uma expressão lógica que deve ser verdadeira para que os registros sejam incluídos na impressão. Para construir uma expressão, clique no botão de reticências ( … ) para abrir a caixa de diálogo Expression Builder. Dica Não inclua o comando FOR na expressão. Por exemplo, você pode especificar country = "Canada" para ver apenas dados canadenses.
**While**
Especifica uma expressão lógica que deve ser verdadeira para continuar imprimindo registros. Para construir uma expressão, clique no botão de reticências ( … ) para abrir a caixa de diálogo Expression Builder. Dica Não inclua o comando WHILE na expressão. Por exemplo, você pode especificar sales > 1000 para ver apenas vendas superiores a mil dólares.

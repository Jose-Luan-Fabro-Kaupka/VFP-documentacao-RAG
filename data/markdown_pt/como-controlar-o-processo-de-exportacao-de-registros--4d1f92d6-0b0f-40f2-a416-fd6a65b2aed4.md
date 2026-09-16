# Como: controlar o processo de exportação de registros

Ao exportar, você pode especificar uma condição que deve ser atendida para continuar avaliando e selecionando registros. Você insere essa condição como uma expressão WHILE.

Enquanto a expressão WHILE permanecer verdadeira, o Visual FoxPro processa a tabela de origem. Depois de encontrar um registro que não atende à condição, o Visual FoxPro encerra o processo de avaliação e exporta os registros selecionados. Essa opção permite exportar registros com base em informações externas aos valores contidos nos campos.

> **Dica:** Se você usar uma expressão WHILE em um arquivo que não foi indexado, o processo de exportação pode terminar antes de avaliar todos os registros apropriados. Antes de executar o procedimento de exportação, certifique-se de que a tabela de origem tenha o índice apropriado ativo para a expressão WHILE que deseja usar.

### Para inserir critérios para encerrar a exportação de registros
- No menu Arquivo, escolha Exportar .
- Insira as informações da tabela de origem e do arquivo de destino.
- Escolha While para criar uma expressão na caixa de diálogo Expression Builder. Observação Você não precisa incluir o comando WHILE na instrução. Por exemplo, digite sales > 1000 para ver apenas vendas acima de mil dólares.
- Escolha OK . O Visual FoxPro exporta os registros que avalia enquanto a expressão é verdadeira.

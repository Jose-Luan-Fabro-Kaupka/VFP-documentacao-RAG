# Usando conjuntos de resultados

Quando você usa as funções de passagem SQL SQLEXEC( ) ou SQLMORERESULTS( ) para consultar dados, o Visual FoxPro retorna os dados em um ou vários conjuntos de resultados. Conjuntos de resultados originam-se de cursores na fonte de dados do servidor e tornam-se cursores no Visual FoxPro. O nome padrão para um conjunto de resultados é SQLRESULT.

# Como o servidor processa conjuntos de resultados e erros

Como o servidor compila cada procedimento armazenado quando você o cria, você recebe quaisquer erros de sintaxe do servidor no momento da criação. Quando você executa o procedimento armazenado, o servidor executa as instruções SQL compiladas sequencialmente (como em um programa Visual FoxPro) e o Visual FoxPro busca cada conjunto de resultados de cada instrução SQL dentro do procedimento armazenado separadamente, na ordem de execução.

Conjuntos de resultados e erros são retornados na ordem recebida, e o processamento para se um erro for encontrado. Por exemplo, se um erro em tempo de execução ocorrer quando o servidor executa a terceira instrução em um procedimento armazenado de quatro instruções, você recebe os dois primeiros conjuntos de resultados e então recebe o erro que ocorreu ao processar o terceiro conjunto de resultados. O processamento para após o erro ser retornado; o quarto conjunto de resultados não é recuperado. Você pode usar a função AERROR( ) para obter informações sobre o erro mais recente.

> **Observação:** Você pode executar procedimentos armazenados em um servidor remoto a partir do Visual FoxPro apenas usando funções de passagem SQL do Visual FoxPro. Exibições não suportam procedimentos armazenados em um servidor remoto, porque cada exibição contém uma instrução SQL SELECT explícita em sua definição SQL.

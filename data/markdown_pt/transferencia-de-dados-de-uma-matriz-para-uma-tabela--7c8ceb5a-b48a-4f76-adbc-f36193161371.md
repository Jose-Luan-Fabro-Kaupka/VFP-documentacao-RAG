# Transferência de dados de uma matriz para uma tabela

Os seguintes comandos do Visual FoxPro transferem dados de uma matriz para uma tabela:
 - GATHER transfere dados de uma matriz para um único registro de tabela.
- APPEND FROM ARRAY adiciona novos registros a uma tabela e preenche os registros com dados de uma matriz.
- INSERT - SQL anexa um único novo registro a uma tabela e preenche o registro com dados de uma matriz.

GATHER, APPEND FROM ARRAY e INSERT - SQL diferem nos seguintes aspectos:
 - GATHER transfere dados de uma matriz para o registro atual na tabela atual. Além disso, a opção GATHER MEMVAR transfere dados de um conjunto de variáveis para o registro atual da tabela.
- APPEND FROM ARRAY anexa novos registros ao final da tabela atual e depois transfere dados da matriz para os registros recém-anexados.
- INSERT - SQL anexa um novo registro e depois transfere dados da matriz para o registro recém-anexado. Diferentemente de GATHER e APPEND FROM ARRAY, INSERT - SQL pode anexar um registro em uma tabela não selecionada (uma tabela aberta em uma área de trabalho diferente da área de trabalho atual). Observação APPEND FROM ARRAY ou INSERT - SQL executa mais rapidamente que APPEND BLANK seguido de REPLACE, especialmente em uma rede.

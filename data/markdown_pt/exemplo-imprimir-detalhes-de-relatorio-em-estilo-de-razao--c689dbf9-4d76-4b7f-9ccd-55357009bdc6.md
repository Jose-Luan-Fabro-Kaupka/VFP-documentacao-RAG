# Exemplo Imprimir detalhes de relatório em estilo de razão

Arquivo: ...\Samples\Solution\Reports\Ledger.frx

O relatório Ledger.frx imprime uma lista de telefones de funcionários que alterna a impressão de um fundo cinza atrás dos registros. O ambiente de dados deste relatório contém a tabela EMPLOYEE do Testdata.dbc no projeto Solution.

No layout do relatório, a banda Page Header tem controles Label que imprimem o título do relatório, a descrição e os cabeçalhos de coluna. A banda Detail tem os controles de campo e label que imprimem as informações de cada funcionário.

Para imprimir em estilo de razão, os controles para as informações do funcionário estão sobre um retângulo. A cor do retângulo é cinza e seu modo é opaco. O relatório imprime o retângulo para cada outro registro avaliando uma expressão nas opções Print When do controle retângulo. A expressão é MOD(nCounter,2) = 1, que usa uma variável de relatório, nCounter, que incrementa para cada registro impresso. O relatório usa o valor dessa variável para determinar quando imprimir o retângulo.

# Transferência de dados de uma tabela para uma matriz

Os seguintes comandos do Visual FoxPro transferem dados de uma tabela para uma matriz:
 - SCATTER transfere dados de um único registro de tabela para uma matriz.
- COPY TO ARRAY transfere dados de uma série de registros para uma matriz.
- SELECT - SQL pode transferir os resultados de uma consulta para uma matriz. Para obter detalhes sobre SELECT - SQL, consulte o tópico Matrizes e SELECT - SQL.

SCATTER e COPY TO ARRAY diferem nos seguintes aspectos:
 - SCATTER transfere dados do registro atual na tabela atual. COPY TO ARRAY pode transferir dados de vários registros na tabela atual.
- A opção SCATTER BLANK cria automaticamente uma matriz com elementos do mesmo tamanho e tipo dos campos na tabela, mas os elementos da matriz ficam vazios.
- A opção SCATTER VAR cria automaticamente um conjunto de variáveis com o mesmo tamanho, tipo e nome dos campos na tabela.

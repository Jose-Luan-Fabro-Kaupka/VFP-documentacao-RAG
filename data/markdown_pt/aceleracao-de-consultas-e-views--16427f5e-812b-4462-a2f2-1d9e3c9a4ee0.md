# Aceleração de consultas e views

Você pode melhorar o desempenho de consultas e views adicionando índices, otimizando o processamento local e remoto e otimizando expressões de parâmetros.

# Adicionar índices a tabelas remotas

Índices remotos podem tornar as consultas significativamente mais rápidas. Consultas de várias tabelas são mais rápidas se as tabelas estiverem indexadas nos campos de junção. Ter índices em campos incluídos na cláusula WHERE de uma consulta também pode melhorar o desempenho.

Índices clusterizados oferecem o melhor desempenho. No SQL Server, cada tabela pode ter um índice clusterizado. O SQL Server Upsizing Wizard cria automaticamente índices clusterizados em tabelas que tinham uma chave primária no Visual FoxPro.

> **Dica:** Embora índices em campos de tabela usados em consultas possam acelerar o processamento, índices em conjuntos de resultados podem reduzir o desempenho. Use índices em conjuntos de resultados com cuidado.

# Otimizar processamento local e remoto

Se você precisar processar uma combinação de dados locais e remotos, crie uma view remota que combine todos os dados remotos em uma única view. Você pode então unir a view remota com os dados locais em uma view local. Como o Visual FoxPro busca ambas as views completamente antes de unir e filtrar a view combinada, é importante limitar o tamanho do conjunto de resultados da view.

Você ganha velocidade no processamento remoto limitando o conjunto de resultados da view remota à quantidade mínima de dados necessária para sua aplicação. Quando você recupera menos dados em um conjunto de resultados remoto, minimiza o tempo necessário para baixar dados remotos para o cursor de consulta ou view local.

# Otimizar views parametrizadas

Você pode acelerar a recuperação de dados durante operações REQUERY( ) Function em uma view parametrizada aberta compilando a view antes de sua execução. Para pré-compilar ou "preparar" uma view, defina a propriedade Prepared da view como true (.T.).

# Otimizar expressões de parâmetros

Parâmetros de view e SQL pass-through são expressões do Visual FoxPro e são avaliados no Visual FoxPro antes de serem enviados ao servidor remoto. O tempo de avaliação da expressão é importante, pois aumenta o tempo de execução da consulta.

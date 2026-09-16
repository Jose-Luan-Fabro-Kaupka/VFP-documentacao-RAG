# Assistente Report

Com o assistente Report, você pode criar relatórios usando uma tabela livre ou uma tabela ou exibição de um banco de dados. É possível criá-los rapidamente, executá-los a qualquer momento e salvá-los para uso futuro. Ao executar um relatório salvo, ele exibe ou imprime as informações atuais da tabela ou exibição.

Para saber como iniciar o assistente, consulte Como: criar relatórios (Visual FoxPro).

# Etapa 1 – Selecionar campos

Nesta etapa, escolha uma tabela livre ou uma tabela de banco de dados como origem. Só é possível selecionar campos de uma única tabela ou exibição. Localize e selecione a tabela ou o banco clicando no botão de reticências (...). Na lista Available fields, selecione os campos e adicione-os a Selected fields.

# Etapa 2 – Agrupar registros

Nesta etapa, use o agrupamento de dados para categorizar e classificar os registros, facilitando a leitura. Ao selecionar um campo em uma caixa Group by, você pode escolher Grouping Options e Summary Options para refinar o agrupamento. É possível escolher até três campos.

Grouping Options abre a caixa Grouping Intervals, na qual você seleciona níveis de filtragem pertinentes ao tipo de dados dos campos.

Summary Options abre a caixa Summary Options, que permite escolher o cálculo para campos numéricos:

| Opção de resumo | Retorno |
| --- | --- |
| Sum | Total dos valores no campo numérico. |
| Avg | Média dos valores no campo numérico. |
| Count | Número de registros que contêm valor não nulo no campo. |
| Min | Valor mínimo no campo numérico. |
| Max | Valor máximo no campo numérico. |

Você também pode escolher Detail and Summary, que fornece subtotais e totais de grupos; Summary only, que fornece somente totais; ou No Totals. Use Calculate percent of total for sums para acompanhar a porcentagem do total representada por cada subtotal.

Os campos escolhidos como agrupamentos não estarão disponíveis na Etapa 3.

# Etapa 3 - Escolher o estilo do relatório

Nesta etapa, escolha o formato básico entre os estilos internos do assistente. Ao clicar em um estilo, o gráfico da lupa é atualizado para exemplificá-lo.

# Etapa 4 - Definir o layout do relatório

Nesta etapa, especifique o número de linhas ou colunas e a orientação retrato ou paisagem.

Ao especificar colunas ou selecionar uma opção de layout, o assistente atualiza o gráfico da lupa.

> **Observação:** Se você especificou um agrupamento na Etapa 2, as seleções Columns e Field Layout não estarão disponíveis.

# Etapa 5 - Classificar registros

Esta etapa permite especificar um ou mais campos para classificar os registros.

Escolha até três campos ou uma marca de índice existente no banco de dados para determinar a ordem dos resultados. Selecione Ascending para ordem crescente ou Descending para decrescente.

# Etapa 6 - Concluir

Nesta etapa, escolha como e quando usar o relatório.
 **Save report for later use**
Salva o relatório como um arquivo que pode ser aberto posteriormente.
**Save report and modify in the Report Designer**
Salva o relatório e o abre no Report Designer para modificações.
**Save and print report**
Salva o relatório e o imprime imediatamente.

Se os campos selecionados não couberem em uma única linha na largura do relatório, eles serão quebrados para a linha seguinte. Para evitar isso, desmarque Wrap fields that do not fit. Se você usou uma tabela ou exibição de um banco de dados, pode escolher Use display settings stored in the database. Clique em Preview para exibir o relatório sem sair do assistente.

Depois de salvar o relatório, você poderá abri-lo e modificá-lo como qualquer outro relatório no Report Designer.

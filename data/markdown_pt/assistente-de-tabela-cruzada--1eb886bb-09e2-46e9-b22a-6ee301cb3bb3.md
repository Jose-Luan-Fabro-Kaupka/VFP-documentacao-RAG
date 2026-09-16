# Assistente de tabela cruzada

Este assistente cria uma consulta de tabela cruzada para resumir dados de uma tabela em formato de planilha.

 Para acessar o Assistente de tabela cruzada
 - No menu Ferramentas, escolha Assistentes e clique em Consulta.
- Na caixa de diálogo Seleção de assistente, escolha Assistente de tabela cruzada.

# Etapa 1 - Selecionar campos

Nesta etapa, você pode escolher uma tabela livre ou uma tabela de um banco de dados como origem da tabela dinâmica. É possível selecionar somente campos de uma única tabela ou exibição. Para obter mais informações, consulte Trabalhando com exibições (Visual FoxPro).

 Para selecionar os campos da consulta de tabela cruzada
 - Use os controles Bancos de dados e tabelas para localizar e selecionar a tabela desejada.
- Na janela Campos disponíveis, selecione três ou quatro campos da tabela e use os botões de seta para movê-los para a janela Campos selecionados.

Você precisa escolher pelo menos três campos: um para valores de linha, um para valores de coluna e um para os dados.

# Etapa 2 - Definir layout

Nesta etapa, você pode especificar quais valores de campo serão calculados para os dados. Por exemplo, se uma tabela Orders contiver, entre outros, um campo de cidade, um de região e um de valor do pedido, você poderá criar uma tabela dinâmica que exiba, na área de dados, as somas de todas as cidades por região. Na parte inferior, a tabela exibirá os totais de cada coluna. À extrema direita, exibirá os totais de cada linha.

 Para definir o layout da tabela cruzada
 - Na lista Campos disponíveis, arraste um campo para a caixa Linhas. A consulta conterá uma linha para cada valor exclusivo do campo.
- Na lista Campos disponíveis, arraste um campo para a caixa Colunas. A consulta conterá uma coluna para cada valor exclusivo do campo.
- Na lista Campos disponíveis, arraste um campo para a caixa Dados. Como esse campo será resumido, geralmente é melhor usar um campo numérico.

Se a tabela for grande, convém primeiro criar uma exibição com os campos desejados e, em seguida, criar uma consulta de tabela cruzada a partir dela.

# Etapa 3 - Adicionar informações de resumo

Nesta etapa, você pode decidir se deseja adicionar uma coluna de subtotal e informações de resumo aos dados. Para adicionar informações de resumo, selecione o botão apropriado (Soma, Contagem, Média, Máximo ou Mínimo) na seção Resumo. Para adicionar uma coluna de subtotal, selecione o botão apropriado (Soma dos dados, Número de células que contêm dados ou Percentual do total da tabela) na seção Subtotais. Caso não deseje uma coluna de subtotal, selecione Nenhum. Os totais aparecerão na coluna mais à direita dos resultados.

# Etapa 4 - Concluir

Esta etapa permite salvar e especificar o uso da consulta de tabela cruzada.
 **Salvar consulta de tabela cruzada**
Salva a consulta para uso posterior.
**Salvar e executar consulta de tabela cruzada**
Salva a consulta e a executa imediatamente.
**Salvar consulta de tabela cruzada e modificar no Designer de consultas**
Salva a consulta e a abre no Designer de consultas para que você possa modificá-la.

Você pode visualizar a consulta clicando no botão Visualizar. Para exibir valores nulos, marque a caixa Exibir valores nulos.

A qualquer momento após salvar a consulta, você pode abri-la e modificá-la como qualquer outra consulta nos designers de Consulta e Exibição.

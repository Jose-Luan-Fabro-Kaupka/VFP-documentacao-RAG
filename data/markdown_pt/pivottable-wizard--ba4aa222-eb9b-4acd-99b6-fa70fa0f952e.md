# PivotTable Wizard

Com o PivotTable wizard, você pode criar pivot tables, que são tabelas interativas de planilha usadas para resumir e analisar dados de tabelas existentes, possivelmente grandes. Você pode escolher salvar uma pivot table diretamente no Microsoft Excel ou adicionar uma como objeto em um formulário.

Você deve ter o Microsoft Excel com o Microsoft Query instalado em seu computador para criar uma pivot table. Para obter mais informações, consulte a Ajuda do Microsoft Excel.

 Para acessar o PivotTable wizard
 - No menu Tools, escolha Wizards e clique em PivotTable.

# Etapa 1 – Selecionar campos

Nesta etapa, você pode escolher uma tabela livre ou uma tabela em um banco de dados como origem da pivot table. Você pode selecionar apenas campos de uma única tabela ou view. Para obter informações, consulte Trabalhando com tabelas (Visual FoxPro) e Trabalhando com views (Visual FoxPro).

 Para selecionar os campos da pivot table
 - Use os controles Databases and Tables para localizar e selecionar a tabela que deseja usar.
- Na janela Available fields, selecione três ou quatro campos que deseja usar da tabela selecionada e use os botões de seta para movê-los para a janela Selected fields.

O wizard não permitirá que você prossiga para a próxima etapa até que tenha escolhido pelo menos três campos; um para valores de linha, um para valores de coluna e um para dados.

# Etapa 2 - Definir layout

Nesta etapa, você pode especificar quais valores de campo serão calculados para os dados. Por exemplo, se você tem uma tabela Orders que contém, entre outros, um campo para cidade, um campo para região e um campo para valor do pedido, pode criar uma pivot table que exibirá na área de dados somas para todas as cidades, por região. Na parte inferior, a tabela exibirá totais para cada coluna. Na extrema direita, a tabela exibirá totais para cada linha.

 Para definir o layout da pivot table
 - Na lista Available fields, arraste um campo para a caixa Rows. A pivot table conterá uma linha para cada valor exclusivo no campo que você arrastar para a caixa Rows.
- Na lista Available fields, arraste um campo para a caixa Columns. A pivot table conterá uma coluna para cada valor exclusivo no campo que você arrastar para a caixa Columns.
- Na lista Available fields, arraste um campo para a caixa Data. Como este campo será resumido, geralmente é melhor arrastar um campo numérico aqui.

Você também pode arrastar um campo para a caixa Page. Se arrastar um campo para a caixa Page, a pivot table conterá uma lista suspensa da qual você pode selecionar as diferentes páginas. Haverá uma página para cada valor exclusivo que existir no campo que você arrastar para a caixa Page.

Se você tem uma tabela grande, pode querer primeiro criar uma view que contenha os campos desejados e depois criar uma pivot table a partir dessa view. Para obter informações, consulte Criando views.

# Etapa 3 - Concluir

Se você selecionar Create a Microsoft Excel pivot table, o wizard exibirá a pivot table finalizada no Excel. O cálculo padrão do PivotTable wizard é somas. Se você criar uma pivot table do Excel, pode alterar facilmente o cálculo para outro suportado pelo Excel, como média ou contagem.

Se você selecionar Create a new form containing an embedded pivot table, o wizard criará um novo formulário contendo a pivot table incorporada e o abrirá no Form designer. Clique duas vezes no objeto incorporado para modificá-lo no Form designer.

# Como: consultar várias tabelas e exibições

Quando precisar acessar informações armazenadas em duas ou mais tabelas, adicione todas as tabelas necessárias à consulta ou exibição e associe-as por campos em comum. Em seguida, você poderá pesquisar os registros de todas as tabelas para encontrar as informações necessárias. É possível usar qualquer combinação de tabelas de banco de dados, tabelas livres e exibições locais ou remotas nas consultas.

O termo "exibição" pode se referir tanto a uma fonte de entrada quanto a um objeto criado no View Designer; portanto, o termo "tabela" é usado tanto para tabelas quanto para exibições empregadas como fontes de entrada.

# Adicionando exibições e tabelas a uma consulta

Quando você adiciona tabelas ou exibições à consulta, o Visual FoxPro sugere uma possível junção entre elas com base em nomes de campos correspondentes.

Por exemplo, se você adicionar a tabela Customer do diretório ...\Samples\Data do Visual FoxPro ao Query Designer e depois adicionar a tabela Orders, o Visual FoxPro sugerirá uma junção entre as tabelas com base nos campos correspondentes Customer.cust_id e Orders.cust_id.

Se estiver usando um banco de dados que contém relações persistentes definidas entre suas exibições ou tabelas, o Visual FoxPro usará as relações existentes como junções padrão.

Para adicionar tabelas ou exibições de banco de dados à consulta, talvez seja necessário abrir o banco de dados apropriado para disponibilizá-las.

### Para adicionar uma tabela ou exibição a uma consulta
- Na barra de ferramentas Query Designer, escolha Add Table.
- Na caixa de diálogo Add Table or View, selecione o banco de dados que deseja usar, escolha Tables ou Views, selecione a tabela ou exibição que deseja adicionar e escolha OK. -ou- Para adicionar uma tabela que não faça parte do banco de dados, escolha Other, localize a tabela na caixa de diálogo Open e escolha OK.
- Na caixa de diálogo Join Condition, verifique a junção sugerida e escolha OK. Se o Visual FoxPro não puder sugerir uma correspondência provável entre os campos, selecione você mesmo os campos correspondentes na caixa de diálogo Join Condition.

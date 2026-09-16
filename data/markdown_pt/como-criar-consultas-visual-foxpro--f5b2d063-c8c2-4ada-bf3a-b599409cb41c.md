# Como: criar consultas (Visual FoxPro)

O processo básico para criar uma consulta é geralmente o mesmo, independentemente do método que você usa. O processo geral a seguir descreve a criação de uma consulta a partir de uma única tabela. Você também pode criar consultas a partir de várias tabelas.

### Para criar uma consulta
- Determine o tipo de informação que você precisa encontrar e a tabela ou exibição da qual você precisa recuperar os dados.
- Selecione a tabela ou exibição e os campos correspondentes dos quais você deseja dados.
- Especifique quaisquer critérios adicionais para extrair registros das tabelas ou exibições.
- Gere a consulta e direcione os resultados para uma fonte de saída.

Quando você criou uma consulta que deseja manter, pode salvá-la dando um nome a ela. Consultas são armazenadas como arquivos com a extensão .qpr.

Você pode usar diferentes métodos para criar consultas:
 - Use o Query Wizard para guiá-lo pelas etapas de criação de consultas.
- Use o Query Designer para criar e personalizar consultas rapidamente.
- Use instruções SQL SELECT, que oferecem maneiras mais poderosas e flexíveis de gerar consultas usando código.

# Criando consultas usando o Query Wizard

Se você deseja ajuda com a criação de consultas, use o Query Wizard. O assistente solicita que você selecione as tabelas ou exibições das quais deseja informações e cria uma consulta baseada em suas respostas a uma série de perguntas. Para obter mais informações sobre o assistente, pressione a tecla F1 para Ajuda enquanto estiver usando o assistente ou consulte Query Wizard.

### Para criar uma consulta usando o Query Wizard
- Abra uma tabela livre ou, no Project Manager, abra um banco de dados ou uma tabela de banco de dados.
- No menu Tools, aponte para Wizards e clique em Query .
- Selecione Query Wizard e clique em OK .
- Siga as instruções nas telas do assistente.

Você também pode começar a criar uma consulta no Query Wizard, salvar a consulta e então usar o Query Designer para modificá-la.

# Criando consultas usando o Query Designer

Se você não precisa de ajuda para criar sua consulta, pode usar o Query Designer. O Query Designer fornece uma maneira de pesquisar registros que atendem a critérios especificados para recuperar informações armazenadas em tabelas e exibições. Você também pode organizar e agrupar os registros conforme necessário e criar relatórios, tabelas e gráficos baseados nos resultados.

### Para abrir o Query Designer
- No menu File, clique em New .
- Na caixa de diálogo New, clique em Query e então New File . O Query Designer é aberto.

Para obter mais informações, consulte Query and View Designers.

### Selecionando tabelas para consultas

Se você está criando consultas a partir de tabelas livres ou exibições, pode selecionar as tabelas ou exibições após iniciar o Query Designer. No entanto, se você deseja selecionar tabelas ou exibições de um banco de dados, abra o banco de dados antes de iniciar o Query Designer. Se suas tabelas, bancos de dados ou exibições estão em um projeto, abra o Project Manager antes de iniciar o Query Designer. Para obter mais informações sobre o uso de várias tabelas e exibições, consulte Como: consultar várias tabelas e exibições.

Ao adicionar mais de uma tabela à sua consulta, você pode especificar condições de junção para modificar o escopo dos resultados retornados. O Visual FoxPro exibe a caixa de diálogo Join Condition para você especificar a condição de junção para cada tabela adicional que você adiciona à sua consulta. Para obter mais informações sobre especificar condições de junção, consulte Como: controlar a seleção de registros com junções, Condições de junção para tabelas, consultas e exibições e Caixa de diálogo Join Condition.

### Para selecionar uma tabela livre para uma consulta
- No menu File, clique em New .
- Na caixa de diálogo New, clique em Query e então New File .
- Na caixa de diálogo Add Table or View, clique em Other .
- Selecione uma tabela e clique em Close .

### Para selecionar uma tabela de banco de dados para uma consulta
- Abra um banco de dados autônomo ou, no Project Manager, selecione um banco de dados.
- No menu File, clique em New .
- Na caixa de diálogo New, clique em Query e então New File .
- Na caixa de diálogo Add Table or View, selecione uma tabela de banco de dados e clique em Add .
- Quando terminar de selecionar tabelas, escolha Close . As tabelas aparecem na superfície do Query Designer.

Você também pode criar consultas usando o comando CREATE QUERY para abrir o Query Designer. Para obter mais informações, consulte Comando CREATE QUERY.

Em vez de usar o alias gerado automaticamente quando você adiciona uma tabela ou exibição, pode especificar um alias para cada tabela que você usa digitando-o na caixa Alias que aparece na caixa de diálogo Add Table or View.

### Removendo e adicionando outras tabelas

Você pode remover tabelas de e adicionar outras tabelas à sua consulta.

### Para remover uma tabela de e adicionar outra tabela a uma consulta
- No Query Designer , clique na tabela que deseja remover.
- Na barra de ferramentas do Query Designer, clique em Remove Table para remover a tabela e então Add Table para selecionar outra tabela ou exibição que deseja.

### Construindo consultas no Query Designer

Após selecionar as tabelas que deseja usar para sua consulta, pode começar a construir consultas no Query Designer. Você também pode selecionar tabelas e criar uma consulta no Query Wizard, salvar a consulta e então usar o Query Designer para modificar a consulta.

### Para construir uma consulta usando o Query Designer
- No Query Designer , clique na guia Fields.
- Na lista Available fields, selecione um campo e clique em Add . Para selecionar vários campos, pressione a tecla SHIFT enquanto seleciona campos e então clique em Add .
- Para especificar a ordem em que os campos aparecem na saída, clique e segure o botão de seta dupla vertical que aparece à esquerda do campo que deseja mover na lista Selected fields. Mova o mouse para posicionar o campo da maneira que deseja.

Você pode personalizar ou definir sua consulta ainda mais no Query Designer executando as seguintes tarefas:
 - Alterar a condição de junção das tabelas selecionadas na guia Join.
- Filtrar resultados por campo na guia Filter.
- Organizar resultados por campo na guia Order By.
- Agrupar resultados por campo na guia Group By.
- Selecionar um tipo diferente de saída na guia Miscellaneous.

Para obter mais informações sobre definir sua consulta, consulte Como: definir resultados de consulta. Para obter mais informações sobre personalizar sua consulta e usar as guias no Query Designer, consulte Como: personalizar consultas e Query and View Designers. Para obter mais informações sobre organizar os resultados de sua consulta, consulte Como: organizar resultados de consulta.

### Adicionando comentários a consultas

Você também pode adicionar comentários ou notas sobre a consulta para descrever sua finalidade.

### Para adicionar um comentário a uma consulta
- Clique na superfície do Query Designer para trazê-la para o primeiro plano.
- No menu Query, clique em Comments .
- Na caixa Comment, digite comentários que deseja fazer sobre a consulta.

Comentários que você adiciona a uma consulta são armazenados com a instrução SQL SELECT gerada pelo Query Designer. Você pode visualizar comentários clicando no botão View SQL na barra de ferramentas do Query Designer para abrir a janela SQL. Comentários que você insere usando a caixa Comment aparecem acima da instrução SQL SELECT e são precedidos por um asterisco (*).

> **Observação:** Quando você modifica comentários usando a caixa Comment, as alterações são feitas apenas no primeiro comentário e não afetam quaisquer outros comentários que você possa inserir manualmente na janela SQL.

Para obter mais informações sobre a instrução SQL SELECT gerada por uma consulta, consulte Comando SELECT - SQL. Para obter mais informações sobre personalizar consultas no Query Designer e usar o comando SQL SELECT na janela SQL, consulte Como: personalizar consultas e Como: personalizar consultas usando instruções SQL SELECT.

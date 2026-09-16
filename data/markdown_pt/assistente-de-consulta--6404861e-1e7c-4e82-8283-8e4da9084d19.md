# Assistente de Consulta

Com o Assistente de Consulta, você pode selecionar um grupo de registros baseado em algumas regras que você especificar. Por exemplo, se você tem tabelas que contêm grandes quantidades de informações em uma ou mais tabelas, você pode usar uma consulta cuidadosamente projetada para coletar ou exibir apenas alguns registros que satisfazem algum valor numérico ou lógico.

 Para acessar o Assistente de Consulta
 - No menu Ferramentas, escolha Assistentes , e depois clique em Consulta .
- Na caixa de diálogo Seleção de Assistente, selecione Assistente de Consulta .

# Etapa 1 – Selecionar Campos

Nesta etapa, você pode escolher tabelas livres ou tabelas dentro de um banco de dados como origem para sua consulta. Você pode selecionar campos de uma ou mais tabelas ou views.

 Para selecionar os campos para sua consulta
 - Use os controles Bancos de Dados e Tabelas para localizar e selecionar as tabelas ou views que você deseja usar.
- Na janela Campos disponíveis, selecione um ou mais campos que você deseja usar da tabela selecionada e use os botões de seta para movê-los para a janela Campos selecionados.

Repita este processo para adicionar campos de outras tabelas ou views.

# Etapa 2 – Relacionar Tabelas

Esta etapa é exibida somente se você selecionar campos de mais de uma tabela ou view. Você pode especificar quais campos em cada tabela ou view contêm as mesmas informações e, portanto, podem governar o relacionamento entre as tabelas ou views, determinando assim os registros incluídos.

Selecione os campos desejados nas duas caixas de listagem suspensa e depois escolha Adicionar. Se você usar várias tabelas em sua view, deve relacionar as tabelas indicando quais campos contêm dados correspondentes em cada tabela.

### Etapa 2a – Incluir Registros

Esta etapa é exibida somente se você selecionar campos de mais de uma tabela ou view. Você pode especificar quais registros das tabelas selecionadas serão disponibilizados para o Assistente de Consulta.

Se você estiver usando mais de uma tabela, pode especificar uma condição de junção. Para obter mais informações, consulte Como: adicionar tabelas a views. Por exemplo, se você especificar apenas linhas correspondentes na Etapa 2a, pode refinar essa escolha na Etapa 3 especificando um valor particular para um campo.
 **Somente linhas correspondentes**
Retorna apenas registros de ambas as tabelas que correspondem à condição de comparação definida entre os dois campos na condição de junção. Isso é chamado de junção interna.
**Todas as linhas desta tabela**
Retorna todas as linhas de uma das tabelas ou views listadas. Isso permite criar uma junção externa esquerda ou direita.
**Todas as linhas de ambas as tabelas**
Retorna registros correspondentes e não correspondentes de ambas as tabelas. Isso é chamado de junção externa.

Por padrão, apenas registros correspondentes são incluídos.

# Etapa 3 – Filtrar Registros

Esta etapa aparece imediatamente após a Etapa 1 se você escolheu apenas uma tabela ou view como origem para sua consulta. Você pode especificar uma condição de filtro, para que apenas alguns dos registros que você escolheu disponibilizar sejam usados na consulta.

 Para determinar a condição de filtro
 - Selecione um campo na lista suspensa Campo.
- Especifique um operador, como equals ou contains , na caixa suspensa Operador.
- Especifique um valor na caixa de texto Valor. Por exemplo, se você quisesse filtrar por uma cidade específica, como Helena, poderia escolher city na lista suspensa Campo, escolher equals na lista suspensa Operador e inserir Helena na caixa de texto Valor.

Você pode reduzir o número de registros criando expressões que filtram registros das tabelas ou views selecionadas. Você pode criar duas expressões e conectá-las com And, que retorna apenas registros que atendem a ambos os critérios especificados, ou Or, que retorna registros que atendem a qualquer um dos critérios.

Você pode ver o resultado clicando no botão Visualizar.

# Etapa 4 - Classificar Registros

Nesta etapa, você pode especificar a ordem de classificação dos registros da sua consulta. Por exemplo, se sua consulta será usada para avaliar pedidos por região, você pode classificar por estado ou código postal.

Escolha até três campos ou uma tag de índice que já existe no banco de dados para determinar a ordem em que os resultados da sua view serão classificados. Selecione Ascendente para classificar a view em ordem ascendente ou Descendente para classificar a view em ordem descendente.

### Etapa 4a – Limitar Registros

Esta etapa aparece somente se você especificou um ou mais campos de classificação na Etapa 4. Você pode limitar ainda mais o número de registros na view, baseado em uma porcentagem dos registros retornados ou em um número real de registros.

Para ver uma porcentagem dos registros disponíveis, escolha o botão de opção Porcentagem de registros e depois especifique a porcentagem na caixa de edição Valor da porção. Veja todos os registros selecionando Número de registros e depois selecionando Todos os registros. Como mostrado nos procedimentos a seguir, você pode escolher uma porção de registros do início ou do final dos registros disponíveis.

 Para ver os primeiros 10 itens
 - Escolha o botão de opção Número de registros
- Insira 10 na caixa Valor da porção.

 Para ver os últimos 10 registros.
 - Na Etapa 4, altere a ordem de classificação para Descendente .

> **Observação:** Isso altera a ordem de classificação para último registro = primeira leitura.
 - Na Etapa 4a, selecione o botão de opção Número de registros.
- Insira 10 na caixa Valor da porção.

# Etapa 5 - Concluir

Nesta etapa, você pode escolher como salvar sua consulta.
 **Salvar consulta**
Permite salvar a consulta para uso posterior.
**Salvar consulta e executá-la**
Permite salvar a consulta e executá-la imediatamente
**Salvar consulta e modificá-la no Query Designer**
Permite salvar a consulta e depois usar o Query designer para aprimorar ou modificá-la.

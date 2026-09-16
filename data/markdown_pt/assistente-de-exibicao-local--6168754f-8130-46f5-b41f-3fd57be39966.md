# Assistente de exibição local

Com o Assistente de exibição local, você pode criar exibições, que são exibições personalizadas de algumas ou todas as informações, usando dados nativos do Visual FoxPro. Você pode querer usar uma exibição se a quantidade de dados de origem for grande, mas você precisar exibir apenas uma parte específica desses dados. Se você não tiver um banco de dados aberto, será solicitado a abrir um banco de dados ou criar um.

 Para acessar o Assistente de exibição local
 - No menu Ferramentas, escolha Wizards e clique em Query .
- Na caixa de diálogo Seleção de assistente, escolha Local View Wizard .

# Etapa 1 – Selecionar campos

Nesta etapa, você especifica quais tabelas ou exibições de um banco de dados do Visual FoxPro deseja usar como origem para sua exibição local. Usando uma exibição, você pode reunir informações de uma ou mais tabelas em uma única exibição de informações. Uma exibição local, diferentemente de uma janela Browse, pode permitir que você crie uma exibição muito eficaz, talvez simples, a partir de fontes de dados grandes ou complexas.

Você pode selecionar campos de várias tabelas ou exibições. Primeiro, selecione campos de uma tabela ou exibição e mova-os para a caixa Selected fields; depois selecione campos de outra tabela ou exibição e mova-os.

# Etapa 2 – Relacionar tabelas

Esta etapa é exibida apenas se você selecionar campos de mais de uma tabela ou exibição. Você pode especificar quais campos em cada tabela ou exibição contêm informações semelhantes e podem governar a relação entre as tabelas ou exibição, determinando assim os registros incluídos.

Selecione os campos desejados nas duas caixas de listagem suspensa e escolha Add. Se você usar várias tabelas em sua exibição, deve relacionar as tabelas indicando quais campos contêm dados correspondentes em cada tabela.

### Etapa 2a – Incluir registros

Esta etapa é exibida apenas se você selecionar campos de mais de uma tabela ou exibição. Você pode especificar quais registros das tabelas selecionadas estarão disponíveis para o Assistente de exibição local.

Se você estiver usando mais de uma tabela, pode especificar uma condição de junção. Para obter mais informações, consulte Como: adicionar tabelas a exibições. Por exemplo, se você especificar apenas linhas correspondentes na Etapa 2a, pode refinar essa escolha na Etapa 3 especificando um valor particular para um campo.
 **Limitar os registros apenas a linhas correspondentes**
Retorna apenas registros de ambas as tabelas que correspondem à condição de comparação definida entre os dois campos na condição de junção. Isso é chamado de junção interna.
**Todas as linhas de uma das tabelas**
Retorna todas as linhas da tabela selecionada. Isso permite criar uma junção externa esquerda ou direita.
**Todas as linhas de ambas as tabelas**
Retorna registros correspondentes e não correspondentes de ambas as tabelas. Isso é chamado de junção externa.

Por padrão, apenas registros correspondentes são incluídos.

# Etapa 3 – Filtrar registros

Esta etapa aparece imediatamente após a Etapa 1 se você escolheu apenas uma tabela ou exibição como origem para sua exibição local. Você pode especificar uma condição de filtro, para que apenas alguns dos registros que você escolheu disponibilizar sejam usados na exibição local.

 Para determinar a condição de filtro
 - Selecione um campo na lista suspensa Field.
- Especifique um operador, como equals ou contains , na caixa suspensa Operator.
- Especifique um valor na caixa de texto Value. Por exemplo, se você deseja filtrar por uma cidade específica, como Helena, pode escolher city na lista suspensa Field, escolher equals na lista suspensa Operator e inserir Helena na caixa de texto Value.

Você pode reduzir o número de registros criando expressões que filtram registros das tabelas ou exibições selecionadas. Você pode criar duas expressões e conectá-las com And, que retorna apenas registros que atendem aos dois critérios especificados, ou Or, que retorna registros que atendem a qualquer um dos critérios.

Você pode ver o resultado clicando no botão Preview.

# Etapa 4 – Ordenar registros

Esta etapa permite especificar um ou mais campos pelos quais ordenar os registros em sua exibição local.

Escolha até três campos ou uma tag de índice que já exista no banco de dados para determinar a ordem em que os resultados da exibição serão ordenados. Selecione Ascending para ordenar a exibição em ordem ascendente ou Descending para ordenar a exibição em ordem descendente.

### Etapa 4a – Limitar registros

Esta etapa aparece apenas se você especificou um ou mais campos de ordenação na Etapa 4. Você pode limitar ainda mais o número de registros na exibição, com base em uma porcentagem dos registros retornados ou em um número real de registros.

Para ver uma porcentagem dos registros disponíveis, escolha o botão de opção Percent of records e especifique a porcentagem na caixa de edição Portion value. Veja todos os registros selecionando Number of records e depois All records. Conforme mostrado nos procedimentos a seguir, você pode escolher uma parte dos registros do início ou do final dos registros disponíveis.

 Para ver os primeiros 10 itens
 - Escolha o botão de opção Number of records.
- Insira 10 na caixa Portion value.

 Para ver os últimos 10 registros
 - Na Etapa 4, altere a ordem de classificação para Descending .

> **Observação:** Isso altera a ordem de classificação para último registro = primeira leitura.
 - Na Etapa 4a, selecione o botão de opção Number of records.
- Insira 10 na caixa Portion value.

# Etapa 5 - Concluir

Nesta etapa, você pode escolher como tratar a exibição local recém-definida.
 **Salvar exibição local**
Salva a exibição local recém-definida e sai do assistente.
**Salvar exibição local e navegar**
Permite salvar a nova exibição local e depois abri-la em uma janela Browse, para que você possa revisar os dados exibidos.
**Salvar exibição local e modificá-la no View Designer**
Permite salvar a nova exibição local e depois modificá-la quando ela abrir no View designer.

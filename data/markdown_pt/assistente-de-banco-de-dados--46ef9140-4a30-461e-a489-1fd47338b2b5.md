# Assistente de banco de dados

O assistente de banco de dados usa modelos predefinidos para ajudá-lo a criar um banco de dados contendo tabelas apropriadas.

Os seguintes modelos estão incluídos no Visual FoxPro.

> **Observação:** Você pode usar o Application wizard para criar uma aplicação que use esses modelos.

| Modelo | Descrição |
| --- | --- |
| Address Book | Inclui uma tabela para um catálogo de endereços pessoal. |
| Asset Tracking | Inclui tabelas úteis para documentar ativos e custos. |
| Books | Inclui tabelas úteis para documentar autores e livros. |
| Contact | Inclui tabelas úteis para documentar e gerenciar contatos. |
| Donation | Inclui tabelas úteis para gerenciar campanhas de doação. |
| Event Management | Inclui tabelas úteis para planejar e gerenciar eventos e pessoal. |
| Expenses | Inclui tabelas úteis para documentar despesas de funcionários e relatórios. |
| Household Inventory | Inclui tabelas úteis para gerenciar móveis e equipamentos domésticos. |
| Inventory Control | Inclui tabelas úteis para rastrear inventário. |
| Ledger | Inclui tabelas úteis para gerenciar transações. |
| Membership | Inclui tabelas úteis para gerenciar clubes ou outros grupos de associação. |
| Music Collection | Inclui tabelas úteis para gerenciar coleções de gravações. |
| Order Entry | Inclui tabelas úteis para gerenciar operações de entrada de pedidos. |
| Picture Library | Inclui tabelas úteis para gerenciar coleções de filmes e fotografias. |
| Recipes | Inclui tabelas úteis para gerenciar receitas domésticas. |
| Resource Scheduling | Inclui tabelas úteis para especificar, agendar e gerenciar recursos. |
| Service Call Management | Inclui tabelas úteis para gerenciar trabalhos de chamadas de serviço e pessoal. |
| Students and Classes | Inclui tabelas úteis para gerenciar alunos, professores, instalações e programas educacionais. |
| Time and Billing | Inclui tabelas úteis para gerenciar contas de clientes e funcionários. |
| Video Collection | Inclui tabelas úteis para gerenciar coleções de fitas de vídeo. |
| Wine List | Inclui tabelas úteis para gerenciar coleções de vinhos. |
| Workout | Inclui tabelas úteis para planejar e gerenciar um programa de condicionamento físico. |

 Para acessar o assistente de banco de dados
 - Abra o Visual FoxPro.
- No menu Tools, escolha Wizards e clique em Database .

# Etapa 1 – Selecionar um banco de dados

Nesta etapa, você pode selecionar um modelo de banco de dados do Visual FoxPro na lista na seção Select database. Para mais informações sobre cada um desses modelos, consulte a tabela anterior. Alternativamente, você pode especificar um banco de dados do Visual FoxPro ou selecionar um modelo de banco de dados Access (.mdb) clicando no botão Select. Isso exibe a caixa de diálogo Open, na qual você localiza o banco de dados remoto a ser usado como modelo.

# Etapa 2 – Selecionar tabelas e views

Nesta etapa, você pode escolher as tabelas e views que deseja incluir em seu banco de dados. O modelo especificado na Etapa 1 fornece uma lista de tabelas e views pré-selecionadas. Selecione as caixas de seleção das tabelas ou views que deseja usar em seu banco de dados.

# Etapa 3 – Indexar as tabelas

Nesta etapa, você pode determinar como deseja indexar suas tabelas. Você pode selecionar qual campo deseja usar como chave de índice primário.

 Para especificar um campo como chave de índice primário
 - Na caixa de listagem Select table, destaque a tabela que contém o campo que deseja usar.
- Na caixa de listagem Primary key, destaque o campo que deseja usar.

Você também pode selecionar caixas de seleção ao lado das opções oferecidas na seção Field Name para criar índices adicionais.

# Etapa 4 – Configurar relacionamentos

Nesta etapa, você pode estabelecer ou alterar os relacionamentos entre as tabelas no banco de dados.

 Para especificar um relacionamento entre tabelas em seu banco de dados
 - Na caixa de listagem Select table, destaque a tabela que contém o campo que deseja usar.
- Na caixa de listagem My new X table (com X sendo o nome da tabela), destaque a declaração de relacionamento que deseja editar e clique no botão Relationships....
- Na caixa de diálogo Relationships, clique no botão de opção ao lado da descrição do tipo de relacionamento que deseja criar. Você pode selecionar o campo de chave ou criar um novo campo digitando na caixa de edição.
- Clique em OK . Isso retorna à Etapa 4, onde o relacionamento novo ou editado é listado na caixa de listagem My new X table.

# Etapa 5 – Concluir

Nesta etapa, você seleciona as opções finais para seu banco de dados:

Save database for later use — Salva seu banco de dados.

Save database and modify it in the Database Designer — Salva seu banco de dados e o abre no Database designer para modificação adicional.

Populate tables with sample data — preenche o novo banco de dados com os dados de exemplo no modelo.

Após o assistente gerar o banco de dados, você pode adicionar o banco de dados a uma janela Project Manager ou à Component Gallery, ou pode abrir o Database designer para modificar as tabelas e relacionamentos do banco de dados.

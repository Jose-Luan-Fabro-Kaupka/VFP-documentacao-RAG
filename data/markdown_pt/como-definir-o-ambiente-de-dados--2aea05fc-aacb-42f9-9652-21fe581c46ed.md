# Como: definir o ambiente de dados

Cada formulário ou conjunto de formulários inclui um ambiente de dados. O ambiente de dados é um objeto que inclui as tabelas ou exibições com as quais o formulário interage e as relações entre tabelas que o formulário espera. Você pode usar o ambiente de dados para automatizar a abertura e o fechamento de tabelas e exibições quando o formulário é executado. Além disso, você pode usar o ambiente de dados para definir a propriedade ControlSource Property dos controles preenchendo a propriedade ControlSource na Janela Propriedades (Visual FoxPro) com todos os campos do ambiente de dados.

# Adicionar tabelas ao ambiente de dados

Você pode projetar visualmente o ambiente de dados e salvá-lo com o formulário. Quando você adiciona tabelas ou exibições ao Designer de ambiente de dados, pode ver os campos e índices que pertencem à tabela ou exibição.

### Para adicionar tabelas ao ambiente de dados
- Abra o formulário no Form Designer .
- No menu Exibir, clique em Ambiente de dados . O Designer de ambiente de dados é aberto para o ambiente de dados do formulário.
- No menu DataEnvironment, clique em Adicionar .
- Na caixa de diálogo Adicionar tabela ou exibição, clique no banco de dados desejado na lista Banco de dados.
- Na área Selecionar, clique em Tabelas ou Exibições .
- Na lista Tabelas no banco de dados, clique na tabela ou exibição que deseja adicionar ao ambiente de dados.
- Clique em Adicionar . Dica Se nenhum banco de dados ou projeto estiver aberto, clique em Outro para procurar e selecionar uma tabela.

Você também pode arrastar uma tabela ou exibição de um projeto aberto ou do Designer de banco de dados (Visual FoxPro) para o Designer de ambiente de dados.

A lista a seguir inclui propriedades do ambiente de dados comumente definidas:
 - Propriedade AutoCloseTables
- Propriedade AutoOpenTables
- Propriedade InitialSelectedAlias

# Definir índices para o ambiente de dados

Você pode definir a ordem em que seus registros aparecem no relatório definindo um índice para o ambiente de dados.

### Para definir um índice para o Designer de ambiente de dados
- No menu Exibir, escolha Ambiente de dados .
- No menu de atalho, escolha Propriedades .
- Na Janela Propriedades, escolha Cursor1 na caixa Objeto.
- Escolha a guia Dados e selecione a propriedade Order.
- Insira um nome de índice. - OU - Selecione um índice na lista de índices disponíveis.

Quando o Designer de ambiente de dados está ativo, a Janela Propriedades (Visual FoxPro) exibe objetos e propriedades associados ao ambiente de dados. Cada tabela ou exibição no ambiente de dados, cada relação entre tabelas e o próprio ambiente de dados é um objeto separado na caixa Objeto da janela Propriedades.

# Remover tabelas do Designer de ambiente de dados

Quando você remove uma tabela do ambiente de dados, todas as relações em que a tabela está envolvida também são removidas.

### Para remover uma tabela ou exibição do Designer de ambiente de dados
- No Designer de ambiente de dados , selecione a tabela ou exibição.
- No menu DataEnvironment, escolha Remover .

# Definir relações no ambiente de dados

Se você adicionar tabelas ao Designer de ambiente de dados que possuem relações persistentes definidas em um banco de dados, as relações são adicionadas automaticamente no ambiente de dados. Se as tabelas não possuem relações persistentes, você ainda pode relacioná-las no Designer de ambiente de dados.

### Para definir relações no Designer de ambiente de dados
- Arraste um campo da tabela primária para a tag de índice correspondente na tabela relacionada.

Você também pode arrastar um campo da tabela primária para um campo na tabela relacionada. Se não houver tag de índice na tabela relacionada correspondente ao campo na tabela primária, você será solicitado a criar a tag de índice.

# Editar relações no ambiente de dados

Quando você define uma relação no Designer de ambiente de dados, uma linha entre as tabelas indica a relação.

### Para editar as propriedades da relação
- Na janela Propriedades, selecione a relação na caixa Objeto.

As propriedades da relação correspondem a cláusulas e palavras-chave nos comandos SET RELATION Command e SET SKIP Command.

A propriedade RelationalExpr Property é definida por padrão como o nome do campo de chave primária na tabela primária. Se a tabela relacionada está indexada em uma expressão, você precisa definir a propriedade RelationalExpr para essa expressão. Por exemplo, se a tabela relacionada está indexada em `UPPER(cust_id)`, você precisa definir RelationalExpr como `UPPER(cust_id)`.

Se a relação não é um relacionamento um-para-muitos, defina a propriedade OneToMany Property como false (.F.). Isso corresponde a usar o comando SET RELATION Command sem emitir SET SKIP Command.

Definir a propriedade OneToMany de uma relação como true (.T.) corresponde a emitir o comando SET SKIP. Quando você percorre a tabela pai, o ponteiro de registro permanece no mesmo registro pai até que o ponteiro de registro percorra todos os registros relacionados na tabela filha.

> **Observação:** Se você deseja um relacionamento um-para-muitos no formulário, defina a propriedade OneToMany como true (.T.), mesmo que um relacionamento um-para-muitos persistente tenha sido estabelecido em um banco de dados.

# Table Wizard

O Table Wizard cria tabelas baseadas em estruturas de tabela típicas. Ele fornece modelos de tabela, configurações de estilo opcionais, suporte para tipos de dados Character e Memo binários, acesso a bancos de dados e permite selecionar uma tabela que atenda às suas necessidades na lista de tabelas de exemplo. Você pode personalizar a estrutura e os campos da tabela conforme avança no assistente, adicionar sua tabela a um banco de dados e usar configurações de banco de dados para determinar os formatos dos campos que adiciona à sua tabela. Você também pode estabelecer relacionamentos entre tabelas no banco de dados.

Se você tiver um ou mais bancos de dados abertos, o Table Wizard adiciona automaticamente a nova tabela ao banco de dados atual. Se você adicionar sua tabela a um banco de dados, o Table Wizard fornece formatação automática dos campos selecionados. Se nenhum banco de dados estiver aberto, o assistente cria uma free table. Se você basear sua tabela em um banco de dados, pode usar estilos, mapeamentos de campo ou uma chave primária e estabelecer ou usar relacionamentos nas tabelas do banco de dados.

Você pode iniciar o Table Wizard no menu File clicando em New, Table e depois Wizard ou no menu Tools apontando para Wizards e clicando em Table.

# Etapa 1 – Select Fields

Nesta etapa, você pode escolher uma das tabelas de exemplo e selecionar entre os campos disponíveis para criar sua tabela.

 Para selecionar campos para sua tabela
 - Use a caixa de listagem Sample Tables para localizar e selecionar a tabela que deseja usar.
- Na caixa de listagem Available fields, selecione um ou mais campos que deseja usar da tabela selecionada e use os botões de seta para movê-los para a caixa Selected fields.

Você pode categorizar sua seleção como Business ou Personal e pode selecionar campos de mais de uma tabela. Se desejar adicionar uma de suas próprias tabelas à caixa Sample tables, escolha Add.

### Etapa 1a - Select a Database

Nesta etapa você pode escolher adicionar sua tabela a um banco de dados. Adicionar a tabela a um banco de dados oferece funcionalidade aprimorada, mas sua tabela pode ser totalmente funcional sem fazer parte de um banco de dados. Se você criar sua tabela em um banco de dados, o Table wizard fornecerá opções de formatação automática e personalizada na próxima etapa.

Você também pode especificar um nome amigável ou descritivo para a nova tabela.

> **Observação:** Se você criar uma tabela independente, não poderá alterar os captions dos campos.

# Etapa 2 - Modify Field Settings

Nesta etapa você pode alterar quaisquer configurações padrão de campo. Por exemplo, você pode alterar a largura máxima de um campo de caractere ou o número de casas decimais permitidas em um campo numérico.

Você pode especificar se os campos podem conter valores nulos e pode alterar o caption ou o tipo do campo.

Se você estiver criando sua tabela em um banco de dados, também pode selecionar uma das máscaras de entrada de dados predefinidas para cada tipo de campo ou criar uma máscara de entrada personalizada. As janelas Format exibem a máscara e o código de formato que você escolher.

# Etapa 3 - Index the Table

Nesta etapa você pode especificar um campo que será a chave de índice primário da sua tabela. Você também pode designar outros campos como chaves de índice secundário.

# Etapa 4 - Set Up Relationships

Nesta etapa, se você estiver criando sua tabela dentro de um banco de dados, pode estabelecer relacionamentos entre campos na sua nova tabela e tabelas existentes no banco de dados.

Destaque o campo para o qual deseja estabelecer um relacionamento e clique no botão Relationships.

 Para definir um relacionamento
 - Clique no botão de opção que identifica o tipo de relacionamento que deseja estabelecer.
- Selecione o campo que relaciona as tabelas dentro do banco de dados. Se você selecionar <newfield>, digite o nome do campo.
- Clique em OK . A caixa de diálogo Relationships será fechada e retornará à Etapa 3, onde a lista exibe o novo relacionamento.

# Etapa 5 - Finish

Nesta etapa você pode especificar como sua tabela é salva e usada.
 **Save table for later use**
Salva a tabela em disco para uso posterior quando você clicar em Finish .
**Save table and browse it**
Salva a tabela em disco e a abre para que você possa adicionar registros imediatamente escolhendo Append New Record no menu Table após clicar em Finish .
**Save table and modify it in the Table Designer**
Salva a tabela em disco e depois a abre no Table Designer para que você possa modificá-la imediatamente após clicar em Finish .

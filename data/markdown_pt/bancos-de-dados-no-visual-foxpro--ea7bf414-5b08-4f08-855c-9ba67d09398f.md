# Bancos de dados no Visual FoxPro

Bancos de dados fornecem uma arquitetura e um ambiente de trabalho para associar, organizar e trabalhar com tabelas e views. Você pode usar bancos de dados de forma independente ou incluí-los em um projeto de aplicação. Quando você cria um banco de dados, o Visual FoxPro cria e abre um arquivo de banco de dados (.dbc) de forma exclusiva. O arquivo de banco de dados, que é uma tabela, armazena todas as informações sobre o banco de dados, incluindo os nomes de arquivos e itens associados a ele. O arquivo de banco de dados não contém fisicamente itens de nível superior, como tabelas ou campos. Em vez disso, o arquivo de banco de dados armazena ponteiros de caminho de arquivo para tabelas associadas ao banco de dados.

Bancos de dados fornecem benefícios adicionais, como os seguintes:
 - Associar tabelas a um banco de dados.
- Criar relacionamentos persistentes entre tabelas.
- Permitir criar regras de validação em nível de campo e registro sem escrever código.
- Criar regras para preservar os relacionamentos entre tabelas de banco de dados ao adicionar, atualizar ou excluir registros.
- Criar stored procedures.
- Criar views a partir de tabelas locais e remotas.
- Acessar conexões a fontes de dados remotas.

Para visualizar a estrutura de um banco de dados de exemplo, abra o arquivo NorthWind.dbc localizado no diretório Visual FoxPro ...\Samples\Northwind. Para obter mais informações, consulte How to: Open Databases.

# Recursos de dicionário de dados dos bancos de dados

Criar um banco de dados associando tabelas como um grupo fornece os benefícios dos recursos de dicionário de dados no Visual FoxPro. Um dicionário de dados oferece maior flexibilidade no design e na modificação do banco de dados e libera você de escrever código para criar validação em nível de campo e linha ou para garantir a unicidade de valores em campos de chave primária. Mais especificamente, o dicionário de dados do Visual FoxPro permite criar ou especificar os seguintes itens:
 - Chaves primárias e candidatas.
- Relacionamentos persistentes entre tabelas de banco de dados.
- Nomes longos para tabelas e campos.
- Captions em campos que são exibidos em janelas de browse e colunas de grade como cabeçalhos.
- Valores padrão em campos.
- A classe de controle padrão usada em formulários.
- Máscaras de entrada e formatos de exibição para campos.
- Regras em nível de campo e regras em nível de registro.
- Triggers.
- Stored procedures.
- Conexões a fontes de dados remotas.
- Views locais e remotas.
- Comentários para cada campo, tabela e banco de dados.

Alguns recursos de dicionário de dados, como nomes longos de campo, chaves primárias e candidatas, valores padrão, regras em nível de campo e de registro e triggers, são armazenados com o arquivo de banco de dados (.dbc), mas também podem ser criados ao criar uma tabela ou view. Para obter mais informações, consulte Working with Tables (Visual FoxPro) e Creating Views.

# Tabelas em bancos de dados

Você pode associar tabelas a um banco de dados criando-as ou adicionando-as a um banco de dados. Tabelas no Visual FoxPro podem existir como free table ou como database table. Uma free table é um arquivo de tabela (.dbf) que não está associado a nenhum banco de dados. Uma database table é um arquivo de tabela associado a um banco de dados. Database tables podem ter propriedades que free tables não têm, como regras em nível de campo e de registro, triggers e relacionamentos persistentes. Para obter mais informações, consulte Working with Tables (Visual FoxPro) e How to: Associate Tables with a Database.

# Links entre tabelas e o banco de dados

Adicionar uma tabela ao banco de dados cria links entre o arquivo de tabela e o banco de dados. As informações para esses links são armazenadas no arquivo de banco de dados (.dbc) e no arquivo de tabela (.dbf). As informações de link armazenadas no arquivo de banco de dados sobre uma tabela que ele contém são chamadas de forward link. As informações de forward link consistem no caminho relativo e no nome do arquivo para cada arquivo de tabela associado e são armazenadas no arquivo de banco de dados.

As informações de link armazenadas no arquivo de tabela sobre o banco de dados que a contém são chamadas de back link. As informações de back link consistem no caminho relativo e no nome do arquivo para o banco de dados associado à tabela e são armazenadas no cabeçalho do arquivo de tabela. Para obter mais informações, consulte How to: Update Table and Database Links.

# Relacionamentos persistentes entre tabelas de banco de dados

Criar relacionamentos persistentes entre tabelas de banco de dados em um banco de dados permite relacionar tabelas baseadas em uma expressão de índice simples ou complexa ou em seus índices para que você possa acessar os registros exatos que deseja.
 Índices fornecem a base para relacionamentos persistentes

Diferentemente de relacionamentos temporários criados com o comando SET RELATION, você não precisa recriar relacionamentos persistentes cada vez que usa as tabelas. No entanto, relacionamentos persistentes não controlam o relacionamento entre ponteiros de registro nas tabelas, portanto você precisa definir relacionamentos temporários usando o comando SET RELATION, bem como relacionamentos persistentes, ao desenvolver aplicações Visual FoxPro. Para obter mais informações, consulte SET RELATION Command.

Relacionamentos persistentes são armazenados no arquivo de banco de dados (.dbc). O seguinte também se aplica a relacionamentos persistentes:
 - São usados automaticamente como condições de junção padrão nos Query and View designers. Para obter mais informações, consulte Query and View Designers .
- Aparecem no Database Designer como linhas unindo índices de tabelas. Para obter mais informações, consulte Database Designer .
- São usados para armazenar informações de integridade referencial.
- São usados como relacionamentos padrão para formulários e relatórios em um data environment e aparecem no Data Environment Designer. Para obter mais informações, consulte Data Environment Designer .

Para obter mais informações, consulte How to: Create Persistent Relationships Between Tables.

# Integridade referencial entre tabelas de banco de dados

Você pode criar um conjunto de regras para preservar definições de relacionamento entre tabelas de banco de dados ao adicionar, atualizar ou excluir registros. O processo de criar essas regras é chamado de construir integridade referencial. Quando você cria regras para impor integridade referencial, o Visual FoxPro impede as seguintes ações:
 - Adicionar registros a uma tabela relacionada quando não existe registro associado na tabela primária.
- Alterar valores em uma tabela primária que resultem em registros órfãos em uma tabela relacionada.
- Excluir registros de uma tabela primária quando existem registros relacionados correspondentes.

Você pode escrever código de triggers e stored procedures para impor integridade referencial. Um trigger é uma expressão vinculada a uma tabela e invocada quando qualquer um dos registros da tabela é modificado usando um dos comandos de manipulação de dados especificados. No entanto, você pode usar o Referential Integrity (RI) Builder do Visual FoxPro para construir regras de integridade referencial.

O RI Builder facilita determinar os tipos de regras que você deseja impor, as tabelas com as quais impor as regras e os eventos de sistema que fazem o Visual FoxPro verificar regras de integridade referencial. O RI Builder também pode lidar com vários níveis de cascata para exclusões e atualizações em cascata. Quando você usa o RI Builder, o Visual FoxPro gera o código para impor regras de integridade relacional e o salva como triggers que referenciam stored procedures. Para obter mais informações, consulte How to: Build Referential Integrity Between Tables.

# Stored procedures em bancos de dados

Uma stored procedure é código de procedure do Visual FoxPro que opera especificamente nos dados de um banco de dados e é armazenado no arquivo de banco de dados (.dbc). Stored procedures podem melhorar o desempenho porque são carregadas na memória quando um banco de dados é aberto. Stored procedures também tornam sua aplicação mais portátil porque você não precisa gerenciar arquivos de código separados do arquivo de banco de dados.

Por exemplo, você pode usar stored procedures para criar funções definidas pelo usuário que você referencia em regras de validação em nível de campo e registro. Quando você salva uma função definida pelo usuário como stored procedure em um banco de dados, o código da função é salvo no arquivo de banco de dados e se move com o banco de dados automaticamente se você relocar o banco de dados. Para obter mais informações, consulte How to: Create and Manage Stored Procedures.

# Vários bancos de dados para ambientes de vários usuários

Para atender às necessidades organizacionais em um ambiente de vários usuários, você pode precisar de mais de um banco de dados no seu sistema. Vários bancos de dados oferecem as seguintes vantagens:
 - Controlar o acesso do usuário a um subconjunto de tabelas no sistema geral.
- Organizar dados para atender de forma eficiente às diversas necessidades informacionais de vários grupos de usuários.
- Permitir usar um subconjunto de tabelas exclusivamente para criar views locais e remotas em tempo de execução.

Por exemplo, suponha que você tenha um banco de dados com informações de vendas usado principalmente por uma equipe de vendas que trabalha com clientes e outro banco de dados que mantém informações de inventário usado principalmente por compradores que trabalham com fornecedores. Às vezes, as necessidades informacionais desses grupos se sobrepõem. Vários bancos de dados podem ser abertos e acessados ao mesmo tempo; no entanto, contêm informações diferentes.
 Vários bancos de dados podem adicionar flexibilidade ao seu sistema

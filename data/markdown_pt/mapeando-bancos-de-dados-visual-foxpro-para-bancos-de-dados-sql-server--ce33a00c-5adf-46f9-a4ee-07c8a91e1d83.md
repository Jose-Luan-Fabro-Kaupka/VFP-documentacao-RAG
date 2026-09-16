# Mapeando bancos de dados Visual FoxPro para bancos de dados SQL Server

As seções a seguir contêm informações sobre o mapeamento de um banco de dados Visual FoxPro para um banco de dados SQL Server:

# Mapeando objetos

Um banco de dados Visual FoxPro mapeia diretamente para um banco de dados SQL Server. Ao fazer upsizing de um banco de dados Visual FoxPro para um servidor, o SQL Server Upsizing Wizard cria objetos no servidor com tanta funcionalidade quanto possível em relação ao banco de dados Visual FoxPro.

O mapeamento de alguns objetos Visual FoxPro para objetos do servidor é bem direto. Bancos de dados, tabelas, campos, defaults e índices do Visual FoxPro mapeiam um a um para bancos de dados, tabelas, campos, defaults e índices do SQL Server. Uma tabela Visual FoxPro mapeia para uma tabela SQL Server, com exceção de parte do seu dicionário de dados.

No entanto, nem todos os objetos locais mapeiam diretamente para objetos do servidor. Regras de validação e integridade referencial no Visual FoxPro fazem parte do dicionário de dados e são aplicadas no nível do mecanismo. Regras de validação e integridade referencial no SQL Server não fazem parte do dicionário de dados e são aplicadas por código vinculado a uma tabela. Essas diferenças, bem como decisões de design tomadas pelo SQL Server Upsizing Wizard, significam que grande parte do dicionário de dados do Visual FoxPro não pode ser mapeada diretamente para construções do SQL Server.

A tabela a seguir resume como os objetos são mapeados do Visual FoxPro para o SQL Server.

| Objetos Visual FoxPro | Objetos SQL Server |
| --- | --- |
| Database | Database |
| Table | Table |
| Indexes | Indexes |
| Field | Field |
| Default | Default |
| Table validation rule | SQL Server stored procedures called from UPDATE and INSERT triggers |
| Field validation rule | SQL Server stored procedures called from UPDATE and INSERT triggers |
| Persistent relationships (where used for referential integrity constraints) | Update, Insert, and Delete triggers or table constraints |

### Convenções de nomenclatura para objetos com upsizing

Ao migrar objetos para uma fonte de dados, o SQL Server Upsizing Wizard cria objetos nomeados no servidor. O assistente usa prefixos para objetos que precisam de nomes novos, por exemplo, defaults e rules, porque nenhum objeto independente desse tipo existia no Visual FoxPro. Um nome de tabela e, em seguida, um nome de campo, se apropriado, seguem o prefixo. Essa convenção de nomenclatura permite que todos os objetos do mesmo tipo tenham o mesmo prefixo e apareçam juntos quando visualizados com ferramentas de administração da fonte de dados. Objetos criados na mesma tabela também são agrupados na visualização.

> **Observação:** Se as convenções de nomenclatura do SQL Server forem violadas, os nomes de banco de dados, tabela, índice e campo podem mudar durante o upsizing. Os nomes do SQL Server devem ter 30 caracteres ou menos, e o primeiro caractere deve ser uma letra ou o símbolo "@". Os caracteres restantes podem ser números, letras ou os símbolos "$", "#" e "_"; espaços não são permitidos. O SQL Server Upsizing Wizard substitui qualquer caractere ilegal pelo símbolo "_". Quaisquer nomes idênticos a palavras reservadas do SQL Server recebem o sufixo "_". Por exemplo, FROM e GROUP tornam-se FROM_ e GROUP_. O SQL Server Upsizing Wizard também coloca o símbolo "_" na frente de nomes de objetos que começam com um número.

O SQL Server Upsizing Wizard dá a cada tabela com upsizing o mesmo nome da tabela local, a menos que o nome da tabela contenha um espaço ou seja uma palavra-chave da fonte de dados.

Nomes de campo e tipos de dados são traduzidos automaticamente para campos do SQL Server quando uma tabela Visual FoxPro é exportada pelo SQL Server Upsizing Wizard.

A tabela a seguir ilustra como os tipos de dados do Visual FoxPro mapeiam para os tipos de dados do SQL Server.

| Abreviação | Tipo de dados Visual FoxPro | Tipo de dados SQL Server |
| --- | --- | --- |
| C | Character | char |
| Y | Currency | money |
| D | Date | datetime |
| T | DateTime | datetime |
| B | Double | float |
| F | Float | float |
| G | General | image |
| I | Integer | int |
| L | Logical | bit |
| M | Memo | text |
| M (Binary) | Memo (Binary) | image |
| C (Binary) | Character (Binary) | binary |
| N | Numeric | float |

Colunas timestamp são criadas usando o tipo de dados Transact-SQL timestamp. Quando você marca a caixa de seleção Timestamp column para uma tabela específica na Etapa 4 - Map Field Data Types, o SQL Server Upsizing Wizard cria um campo timestamp para essa tabela.

Se uma tabela contém um ou mais campos memo (M) ou picture (P), o SQL Server Upsizing Wizard marca a caixa de seleção Timestamp column para essa tabela por padrão e cria um campo timestamp na versão com upsizing da tabela.

Colunas Identity são criadas usando campos da propriedade Transact-SQL IDENTITY.

# Mapeando views

Se você selecionar Create Remote Views On Tables, o SQL Server Upsizing Wizard cria views remotas e atribui a elas muitas das propriedades dos campos da tabela local original.

# Mapeando defaults do SQL Server

Uma expressão default do Visual FoxPro mapeia diretamente para um único default do SQL Server. O SQL Server Upsizing Wizard tenta criar um default do SQL Server com base na expressão default de um campo Visual FoxPro. Se o default for criado com êxito, o SQL Server Upsizing Wizard o vincula ao campo SQL Server apropriado. O relatório de upsizing dos campos indica se o SQL Server Upsizing Wizard conseguiu traduzir a expressão Visual FoxPro para Transact-SQL do SQL Server. Para obter mais informações, consulte Mapeamento de expressões.

Embora os defaults do SQL Server e do Visual FoxPro sejam em grande parte semelhantes, há algumas diferenças na forma como os defaults são criados e se comportam nos dois produtos. Os defaults do SQL Server são objetos independentes, desvinculados de qualquer campo ou tabela em particular. Depois que um default é criado, ele pode ser usado por, ou vinculado a, qualquer número de campos diferentes.

Embora os campos lógicos do Visual FoxPro aceitem valores nulos, o SQL Server não os aceita. Para gerenciar essa diferença, o SQL Server Upsizing Wizard cria e vincula automaticamente um valor default chamado "UW ZeroDefault" a cada campo lógico exportado, quer você tenha ou não escolhido exportar defaults. Esse default define o valor do campo do servidor como 0 (False (.F.) no Visual FoxPro) quando você não fornece um valor.

Se a tabela local Visual FoxPro contém um valor default para um campo lógico que define o campo como True (.T.), o SQL Server Upsizing Wizard não vincula o default UW_ZeroDefault à tabela do servidor. Em vez disso, o assistente cria um default que define o campo como 1 e nomeia o default de acordo com as convenções de nomenclatura descritas anteriormente neste tópico.

> **Observação:** Os defaults do SQL Server se comportam de forma diferente dos defaults do Visual FoxPro.

### Convenções de nomenclatura para defaults

O SQL Server Upsizing Wizard nomeia defaults usando o prefixo "Dflt_" mais o nome da tabela e o nome do campo. Por exemplo, um valor default para um campo de valor de pedido em uma tabela de clientes pode ser nomeado "Dflt_Customer_Ordamt" no servidor.

> **Observação:** Se a combinação do prefixo com os nomes da tabela e do campo fizer o nome do default exceder 30 caracteres, o Visual FoxPro trunca os caracteres excedentes.

Campos com uma expressão default igual a zero são vinculados a um default chamado "UW ZeroDefault". Se dois ou mais campos tiverem a mesma expressão default diferente de zero, o SQL Server Upsizing Wizard cria dois defaults com dois nomes diferentes, mas funcionalmente idênticos.

# Conversão de índices

Os índices do SQL Server e do Visual FoxPro são muito semelhantes. A tabela a seguir mostra como os tipos de índice do Visual FoxPro são convertidos para tipos de índice do SQL Server.

| Tipo de índice Visual FoxPro | Tipo de índice SQL Server |
| --- | --- |
| Primary | Clustered Unique |
| Candidate | Unique |
| Unique Regular | Non-unique |

O SQL Server Upsizing Wizard usa os nomes de tag do Visual FoxPro como nomes dos índices no SQL Server. Se o nome da tag for uma palavra reservada no servidor, o assistente altera o nome da tag acrescentando o caractere "_".

> **Observação:** O SQL Server não oferece suporte a índices ascendentes ou descendentes nem permite expressões dentro de índices do servidor. O SQL Server Upsizing Wizard remove as expressões Visual FoxPro das expressões de índice à medida que o índice recebe upsizing; apenas os nomes de campo são enviados ao servidor.

# Mapeando triggers

Um trigger do SQL Server é uma série de instruções Transact-SQL associadas a uma tabela SQL Server em particular. Quando você escolhe fazer upsizing de Validation rules and Relationships na Etapa 8, o SQL Server Upsizing Wizard converte regras de validação de campo e de registro e relacionamentos persistentes de tabela do Visual FoxPro em stored procedures que são chamadas a partir de triggers do SQL Server. Cada trigger do servidor pode conter código para emular a funcionalidade de várias regras de validação e de integridade referencial.

> **Observação:** O SQL Server Upsizing Wizard não faz upsizing dos triggers do Visual FoxPro.

Uma tabela do servidor pode ter três triggers, um para cada um dos comandos que podem modificar dados na tabela: UPDATE, INSERT e DELETE. O trigger é executado automaticamente quando o comando associado é realizado.

A tabela a seguir descreve os triggers criados pelo SQL Server Upsizing Wizard. Qualquer trigger específico pode conter código para emular parte ou toda a funcionalidade do Visual FoxPro listada.

| Trigger | Funcionalidade Visual FoxPro emulada |
| --- | --- |
| UPDATE | Validation rules (field and record-level validation) Referential integrity |
| INSERT | Validation rules (field and record-level validation) Referential integrity (child table triggers only) |
| DELETE (Parent table only) | Referential integrity |

### Convenções de nomenclatura para triggers

O SQL Server Upsizing Wizard nomeia os triggers do servidor combinando um prefixo que indica o tipo de trigger criado com o nome da tabela SQL Server à qual o trigger pertence. O prefixo ("TrigU_" para triggers UPDATE, "TrigD_" para triggers DELETE e "TrigI_" para triggers INSERT) é colocado na frente do nome da tabela. Por exemplo, o trigger UPDATE na tabela Customer pode ser chamado `TrigU_Customer`.

# Exportando regras de validação

O SQL Server Upsizing Wizard pode exportar regras de validação de campo e de registro do Visual FoxPro, que converte em stored procedures no SQL Server. O assistente nomeia regras de nível de campo combinando o prefixo "vrf" (de "validation rule, field") com os nomes da tabela e do campo; um exemplo pode ser `vrf_customer_lname`. Regras de validação de tabela são nomeadas com o prefixo "vrt" (de "validation rule, table") mais o nome da tabela, criando um nome como `vrt_customer`.

O SQL Server Upsizing Wizard usa triggers que chamam stored procedures em vez de rules do SQL Server para aplicar a validação de nível de campo porque as rules do SQL Server não permitem exibir mensagens de erro personalizadas. Para obter mais informações sobre rules do SQL Server, consulte o comando CREATE RULE na documentação do SQL Server.

# Exportando integridade referencial

Seu aplicativo Visual FoxPro oferece suporte à integridade referencial por meio de triggers nos eventos UPDATE, DELETE e INSERT em relacionamentos persistentes de tabela que são aplicados no nível do mecanismo. Você pode escolher implementar restrições de integridade referencial no SQL Server usando um destes dois métodos:
 - Integridade referencial baseada em triggers.
- Integridade referencial declarativa.

Quando você escolhe a integridade referencial baseada em triggers, o SQL Server Upsizing Wizard cria triggers que incluem o código Transact-SQL necessário para duplicar as restrições de integridade referencial do Visual FoxPro. Se você escolher implementar a integridade referencial declarativa, o SQL Server Upsizing Wizard cria restrições do SQL Server usando o comando ALTER TABLE com a palavra-chave CONSTRAINT.

### Integridade referencial baseada em triggers

No método baseado em triggers, a integridade referencial é aplicada no SQL Server por código Transact-SQL nos triggers. Você pode usar triggers para restringir instruções UPDATE, DELETE e INSERT, e para encadear alterações resultantes de instruções DELETE e INSERT.

O SQL Server Upsizing Wizard cria triggers do SQL Server avaliando os triggers do Visual FoxPro usados para aplicar a integridade referencial em relacionamentos persistentes no banco de dados Visual FoxPro.

Um relacionamento persistente Visual FoxPro usado em uma restrição de integridade referencial pode se tornar até quatro triggers em uma fonte de dados SQL Server: dois para a tabela pai e dois para a tabela filha.

> **Observação:** Se apenas uma das tabelas de um relacionamento receber upsizing, ou se a integridade referencial não for aplicada no Visual FoxPro, o relacionamento não será exportado.

A tabela a seguir lista o mapeamento entre as restrições de Referential Integrity do Visual FoxPro e os triggers do SQL Server gerados pelo SQL Server Upsizing Wizard.

| Restrição de Referential Integrity do Visual FoxPro | Trigger SQL Server | Descrição |
| --- | --- | --- |
| UPDATE | Cascade | Cascade UPDATE trigger. |
| UPDATE | Restrict | Restrict UPDATE trigger. |
| UPDATE | Ignore | No trigger generated. |
| INSERT | Restrict | Restrict INSERT trigger. |
| INSERT | Ignore | No trigger generated. |
| DELETE | Cascade | Cascade DELETE trigger. |
| DELETE | Restrict | Restrict DELETE trigger. |
| DELETE | Ignore | No trigger generated. |

#### Tabela pai

O SQL Server Upsizing Wizard cria um trigger UPDATE que impede o usuário de alterar a chave primária da tabela pai ou encadeia essa alteração pela tabela filha, dependendo do tipo de relacionamento criado no Visual FoxPro.

O SQL Server Upsizing Wizard também cria um trigger DELETE que impede o usuário de excluir um registro com registros filhos relacionados, ou que exclui os registros filhos, novamente dependendo do tipo de relacionamento entre as tabelas no Visual FoxPro.

#### Tabela filha

O SQL Server Upsizing Wizard cria um trigger UPDATE que impede o usuário de fazer alterações na chave estrangeira que deixariam o registro órfão. Da mesma forma, um trigger INSERT é criado para impedir o usuário de adicionar um novo registro que não tenha pai.

#### Valores de erro personalizados

Em tempo de execução, se a integridade referencial estabelecida pelos triggers criados pelo SQL Server Upsizing Wizard for violada, o SQL Server coloca um valor de erro personalizado na variável @@ERROR. Os valores de erro potenciais são definidos pelo SQL Server Upsizing Wizard como parte do código do trigger. O valor de erro específico retornado em tempo de execução depende de o usuário estar tentando atualizar, inserir ou excluir.

A tabela a seguir lista os números de erro gerados para cada ação.

| Ação | Número de erro SQL Server |
| --- | --- |
| Violated validation rule | 44444 |
| Attempted delete | 44445 |
| Attempted update | 44446 |
| Attempted insert | 44447 |
| Update or Delete statement affected more than one row; statement is automatically rolled back | 44448 |

### Integridade referencial declarativa

Se você escolher implementar a integridade referencial declarativa, o SQL Server Upsizing Wizard cria restrições do SQL Server usando o comando ALTER TABLE com a palavra-chave CONSTRAINT. A restrição da tabela pai usa a palavra-chave PRIMARY KEY. A restrição da tabela filha usa as palavras-chave FOREIGN KEY e REFERENCES. A integridade referencial declarativa é suportada nos níveis RESTRICT, RESTRICT updates e RESTRICT deletes.

Você pode usar restrições do SQL Server para restringir instruções UPDATE, DELETE e INSERT.

# Mapeamento de expressões

Embora o Visual FoxPro e o Transact-SQL tenham algumas funções em comum, muitas funções do Visual FoxPro não são suportadas pelo SQL Server.

A tabela a seguir lista as expressões que são as mesmas entre o Visual FoxPro e o SQL Server.

| CEILING( ) | LOG( ) | LOWER( ) |
| --- | --- | --- |
| LTRIM( ) | RIGHT( ) | RTRIM( ) |
| SOUNDEX( ) | SPACE( ) | STR( ) |
| STUFF( ) | UPPER( ) | |

A tabela a seguir descreve o mapeamento de expressões que o SQL Server Upsizing Wizard usa para tentar converter expressões Visual FoxPro em regras de validação de campo e de registro e valores default para Transact-SQL.

| Expressão Visual FoxPro | Expressão SQL Server |
| --- | --- |
| True (.T.) | 1 |
| False (.F.) | 0 |
| # | <> |
| .AND. | AND |
| .NOT. | NOT |
| .NULL. | NULL |
| .OR. | OR |
| =< | <= |
| => | >= |
| ASC( ) | ASCII( ) |
| AT( ) | CHARINDEX( ) |
| CDOW( ) | DATENAME(dw, ...) |
| CHR( ) | CHAR( ) |
| CMONTH( ) | DATENAME(mm, ...) |
| CTOD( ) | CONVERT(datetime, ...) |
| CTOT( ) | CONVERT(datetime, ...) |
| DATE( ) | GETDATE( ) |
| DATETIME( ) | GETDATE( ) |
| DAY( ) | DATEPART(dd, ...) |
| DOW( ) | DATEPART(dw, ...) |
| DTOC( ) | CONVERT(varchar, ...) |
| DTOR( ) | RADIANS( ) |
| DTOT( ) | CONVERT(datetime, ...) |
| HOUR( ) | DATEPART(hh, ...) |
| LIKE( ) | PATINDEX( ) |
| MINUTE( ) | DATEPART(mi, ...) |
| MONTH( ) | DATEPART(mm, ...) |
| MTON( ) | CONVERT(money, ...) |
| NTOM( ) | CONVERT(float, ...) |
| RTOD( ) | DEGREES( ) |
| SUBSTR( ) | SUBSTRING( ) |
| TTOC( ) | CONVERT(char, ...) |
| TTOC( ) | CONVERT(datetime, ...) |
| YEAR( ) | DATEPART(yy, ...) |

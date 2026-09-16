# Comando SET DATABASE

Define um banco de dados aberto como o banco de dados atual ou define nenhum banco de dados atual.

```foxpro
SET DATABASE TO [DatabaseName]
```

#### Parâmetros
 **[ DatabaseName ]**
Especifica o nome de um banco de dados aberto a ser definido como o banco de dados atual. Omitir DatabaseName ou especificar uma cadeia de caracteres vazia define o banco de dados atual como nenhum banco de dados.

# Observações

SET DATABASE tem escopo na sessão de dados atual. Embora você possa ter muitos bancos de dados abertos ao mesmo tempo, somente um pode ser definido como o banco de dados atual. Comandos e funções que operam em um banco de dados operam no banco de dados atual.

Para obter mais informações, consulte How to: Set the Current Database e How to: Open Databases.

# Exemplo

O exemplo a seguir cria dois bancos de dados chamados `mydbc1` e `mydbc2`, e uma tabela chamada `table1`. SET DATABASE é usado para tornar `mydbc1` o banco de dados atual, e `table1` é adicionada a `mydbc1` quando é criada. A tabela é então fechada e removida de `mydbc1`. SET DATABASE é usado para tornar `mydbc2` o banco de dados atual, e ADD TABLE é então usado para adicionar a tabela a `mydbc2`. RENAME TABLE é usado para alterar o nome da tabela de `table1` para `table2`.

```foxpro
CREATE DATABASE mydbc1
CREATE DATABASE mydbc2
SET DATABASE TO mydbc1
CREATE TABLE table1 (cField1 C(10), n N(10))  && Adds table to mydbc1
CLOSE TABLES
REMOVE TABLE table1
SET DATABASE TO mydbc2
ADD TABLE table1
RENAME TABLE table1 TO table2
```

Para obter mais informações, consulte CREATE DATABASE Command, CREATE TABLE - SQL Command, CLOSE Commands, REMOVE TABLE Command, ADD TABLE Command e RENAME TABLE Command.

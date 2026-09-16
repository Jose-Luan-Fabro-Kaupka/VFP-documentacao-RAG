# Comando RENAME TABLE

Renomeia uma tabela no banco de dados atual.

```foxpro
RENAME TABLE TableName1 TO TableName2
```

#### Parâmetros
 **TableName1**
Especifica o nome da tabela a ser renomeada.
**TableName2**
Especifica o novo nome da tabela.

# Observações

Você não pode usar RENAME TABLE para alterar o nome de uma tabela livre; use RENAME em vez disso.

# Exemplo

O exemplo a seguir cria dois bancos de dados chamados `mydbc1` e `mydbc2` e uma tabela chamada table1. A tabela é adicionada a `mydbc1` quando é criada. A tabela é então fechada e removida de `mydbc1`. ADD TABLE é usado para adicionar a tabela a `mydbc2`. RENAME TABLE é usado para alterar o nome da tabela de `table1` para `table2`.

```foxpro
CLOSE DATABASES
CREATE DATABASE mydbc1
CREATE DATABASE mydbc2
SET DATABASE TO mydbc1
CREATE TABLE table1 (cField1 C(10), n N(10))  && Adds table to mydbc1
CLOSE TABLES     && A table must be closed to remove it from a database
REMOVE TABLE table1
SET DATABASE TO mydbc2
ADD TABLE table1
RENAME TABLE table1 TO table2
```

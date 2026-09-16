# Comando REMOVE TABLE

Remove uma tabela do banco de dados atual.

```foxpro
REMOVE TABLE TableName | ? [DELETE] [RECYCLE]
```

#### Parâmetros
 **TableName | ?**
Especifica a tabela a ser removida do banco de dados atual ou exibe a caixa de diálogo Remove para que você possa escolher uma tabela no banco de dados atual a ser removida.
**[DELETE]**
Remove a tabela do banco de dados e a exclui permanentemente do disco. Cuidado Tabelas excluídas com a palavra-chave DELETE não podem ser recuperadas. O Visual FoxPro não confirma a exclusão nem exibe um aviso, mesmo que o comando SET SAFETY esteja definido como ON.
**[RECYCLE]**
Especifica adiar a exclusão da tabela do disco e movê-la para a Lixeira do Windows.

# Observações

REMOVE TABLE remove todos os índices primários, valores padrão e regras de validação associados à tabela. Se SET SAFETY estiver definido como ON, o Visual FoxPro solicita confirmação para remover a tabela do banco de dados.

Quando uma tabela é removida do banco de dados, ela se torna uma tabela livre e pode ser adicionada a outro banco de dados.

> **Cuidado:** REMOVE TABLE afeta outras tabelas no banco de dados atual se essas tabelas tiverem regras ou relações associadas à tabela sendo removida. As regras e relações deixam de ser válidas quando a tabela é removida do banco de dados.

# Exemplo

O exemplo a seguir cria dois bancos de dados chamados `mydbc1` e `mydbc2` e uma tabela chamada table1. A tabela é adicionada a `mydbc1` quando é criada. A tabela é então fechada e removida de `mydbc1`. ADD TABLE é então usado para adicionar a tabela a `mydbc2`. RENAME TABLE é usado para alterar o nome da tabela de `table1` para `table2`.

```foxpro
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

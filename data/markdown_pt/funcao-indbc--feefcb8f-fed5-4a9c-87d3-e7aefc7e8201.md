# Função INDBC( )

Retorna true (.T.) se o objeto de banco de dados especificado estiver no banco de dados atual; caso contrário, retorna false (.F.).

```foxpro
INDBC(cDatabaseObjectName, cType)
```

#### Parâmetros
 **cDatabaseObjectName**
Especifica o nome de uma conexão nomeada, campo, índice, tabela ou SQL view para o qual INDBC( ) retorna um valor lógico indicando se o objeto está ou não no banco de dados atual.
**cType**
Especifica o tipo de objeto de banco de dados de cDatabaseObjectName. A tabela a seguir lista os valores de cType e o tipo de objeto de banco de dados correspondente. cType Tipo de objeto de banco de dados CONNECTION Conexão nomeada FIELD Campo INDEX Índice TABLE Tabela VIEW SQL View As configurações CONNECTION, FIELD, INDEX, TABLE e VIEW não podem ser abreviadas.

# Valor de retorno

Logical

# Observações

Um banco de dados deve estar aberto e ser o atual quando INDBC( ) é emitido; caso contrário, o Visual FoxPro gera uma mensagem de erro.

# Exemplo

No exemplo a seguir, um banco de dados temporário chamado `mydbc` é criado e uma tabela temporária chamada `mytable` é adicionada ao banco de dados. INDBC( ) é usado para determinar se a nova tabela está no banco de dados. O banco de dados e a tabela são fechados e apagados.

```foxpro
CLOSE DATABASES
CREATE DATABASE mydbc  && Creates a new database
CREATE TABLE mytable (field1 C(10)) && Automatically added to database
? 'MyTable in the database? '
?? INDBC('mytable', 'TABLE')  && Returns .T.
CLOSE DATABASES
DELETE DATABASE mydbc DELETETABLES
```

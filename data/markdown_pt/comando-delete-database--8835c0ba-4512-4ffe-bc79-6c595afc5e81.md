# Comando DELETE DATABASE

Exclui um banco de dados do disco.

```foxpro
DELETE DATABASE DatabaseName | ? [DELETETABLES] [RECYCLE]
```

#### Parâmetros
 **DatabaseName**
Especifica o nome do banco de dados a excluir do disco. O banco de dados especificado não pode estar aberto. DatabaseName pode incluir o caminho para o banco de dados com o nome do banco de dados.
**?**
Exibe a caixa de diálogo Excluir, na qual você pode especificar o nome do banco de dados a excluir do disco.
**DELETETABLES**
Exclui as tabelas contidas no banco de dados do disco e o banco de dados que contém as tabelas.
**RECYCLE**
Especifica que o banco de dados não é excluído imediatamente do disco e é colocado na Lixeira do Windows.

# Observações

Sempre use DELETE DATABASE para excluir um banco de dados do disco. Diferentemente do utilitário de manipulação de arquivos do sistema operacional, DELETE DATABASE remove referências ao banco de dados das tabelas no banco de dados.

Se SET SAFETY estiver ON, o Visual FoxPro pergunta se você deseja excluir o banco de dados especificado. Se SET SAFETY estiver OFF, o banco de dados é excluído automaticamente do disco.

# Exemplo

Este exemplo cria um banco de dados chamado `people`. Uma tabela chamada `friends` é criada e adicionada automaticamente ao banco de dados. DISPLAY TABLES é usado para exibir as tabelas no banco de dados, e DISPLAY DATABASES é usado para exibir informações sobre as tabelas no banco de dados.

DELETE DATABASE é usado com a opção DELETETABLES para remover o banco de dados e sua tabela `friends` do disco.

```foxpro
CLOSE ALL
CREATE DATABASE people
CREATE TABLE friends (FirstName C(20), LastName C(20))
CLEAR
DISPLAY TABLES  && Displays tables in the database
DISPLAY DATABASES  && Displays table information
CLOSE ALL
DELETE DATABASE people DELETETABLES
```

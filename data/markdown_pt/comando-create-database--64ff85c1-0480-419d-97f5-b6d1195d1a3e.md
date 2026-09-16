# Comando CREATE DATABASE

Cria e abre um banco de dados.

```foxpro
CREATE DATABASE [DatabaseName | ?]
```

#### Parâmetros
 **[ DatabaseName | ?]**
Especifica o nome do banco de dados a ser criado ou abre a caixa de diálogo Create para que você possa especificar um nome para o banco de dados e o local onde deseja salvar o banco de dados. Omitir argumentos para esses parâmetros também abre a caixa de diálogo Create. Os arquivos de banco de dados são salvos com a extensão de nome de arquivo .dbc. Observação Se o comando SET SAFETY estiver definido como ON e o nome do banco de dados que você especificar tiver o mesmo caminho e nome de um banco de dados existente, o Visual FoxPro solicitará que você especifique um caminho ou nome diferente para o banco de dados.

# Observações

Um arquivo de banco de dados (.dbc) é criado com um arquivo de memo de banco de dados (.dct) associado e um arquivo de índice de banco de dados (.dcx).

O banco de dados é aberto de forma exclusiva, independentemente da configuração de SET EXCLUSIVE. Como CREATE DATABASE abre o banco de dados após ele ter sido criado, você não precisa chamar um comando OPEN DATABASE subsequente.

Usar CREATE DATABASE não adiciona o banco de dados automaticamente a um projeto, mesmo quando o Project Manager está aberto. Você deve adicionar explicitamente um banco de dados a um projeto de aplicativo para incluí-lo. Para obter mais informações, consulte

# Exemplo

Este exemplo cria um banco de dados chamado `people`. Uma tabela chamada `friends` é criada e é adicionada automaticamente ao banco de dados. DISPLAY TABLES é usado para exibir as tabelas no banco de dados e DISPLAY DATABASES é usado para exibir informações sobre as tabelas no banco de dados.

```foxpro
CREATE DATABASE people
CREATE TABLE friends (FirstName C(20), LastName C(20))
CLEAR
DISPLAY TABLES  && Displays tables in the database
DISPLAY DATABASES  && Displays table information
```

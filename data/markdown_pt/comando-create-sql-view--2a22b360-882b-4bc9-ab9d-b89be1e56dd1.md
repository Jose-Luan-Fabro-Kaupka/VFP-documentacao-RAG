# Comando CREATE SQL VIEW

Abre o Designer de exibições para que você possa criar uma exibição SQL.

```foxpro
CREATE [SQL] VIEW [ViewName] [REMOTE]
   [CONNECTION ConnectionName [SHARE] | CONNECTION DataSourceName]
   [AS SQLSELECTStatement]
```

#### Parâmetros
 **CREATE [SQL] VIEW**
Cria uma exibição SQL.
**[ ViewName ]**
Especifica o nome da exibição a criar.
**[REMOTE]**
Especifica a criação de uma exibição usando tabelas de uma fonte de dados remota, ou uma exibição remota. Omitir REMOTE cria uma exibição usando tabelas locais.
**[CONNECTION ConnectionName [SHARE] | CONNECTION DataSourceName ]**
Especifica o nome de uma conexão previamente definida ou de uma fonte de dados existente para conectar ao abrir a exibição. Observação Quando você usa a cláusula CONNECTION e especifica o nome de uma conexão ou fonte de dados, o Visual FoxPro primeiro pesquisa no banco de dados atual uma conexão com o nome especificado. Se a conexão especificada não for encontrada, o Visual FoxPro pesquisa uma fonte de dados ODBC estabelecida com o nome especificado. Portanto, se o banco de dados atual contém uma conexão nomeada com o mesmo nome de uma fonte de dados ODBC no seu sistema, o Visual FoxPro usa a conexão nomeada. Dica Se você usar uma cláusula CONNECTION com o comando CREATE SQL VIEW, não precisa incluir a palavra-chave REMOTE. O Visual FoxPro identifica a exibição como uma exibição remota pela inclusão da palavra-chave CONNECTION. A palavra-chave SHARE especifica que o Visual FoxPro use um novo identificador de instrução para a conexão compartilhada, se disponível. Se uma conexão compartilhada não estiver disponível, o Visual FoxPro cria uma conexão compartilhada quando a exibição é aberta, que você poderá compartilhar com outras exibições.
**[AS SQLSELECTStatement ]**
Especifica uma instrução SQL SELECT para a exibição. SQLSELECTStatement deve ser uma instrução SQL SELECT válida e não deve ser colocada entre aspas (""). Dica Para exibições locais, prefixe o nome da exibição ou tabela na instrução SQL SELECT com o nome do banco de dados e um ponto de exclamação (!). Ao qualificar o nome da tabela ou exibição com o nome do banco de dados e o ponto de exclamação, o Visual FoxPro pesquisa a tabela em todos os bancos de dados abertos e no caminho de pesquisa padrão da tabela. No entanto, se você não qualificar uma tabela com um nome de banco de dados em uma definição de exibição, o banco de dados deve estar aberto antes de você poder usar a exibição. Para obter mais informações, consulte Comando SELECT - SQL .

# Observações

Uma exibição SQL permite recuperar dados de campos específicos em uma ou mais tabelas relacionadas como uma tabela que você pode atualizar. Para obter mais informações, consulte Trabalhando com exibições (Visual FoxPro).

# Exemplo

O exemplo a seguir fecha todos os bancos de dados abertos e abre o banco de dados de exemplo Northwind. CREATE SQL VIEW cria uma exibição SQL local chamada MyView usando uma instrução SQL SELECT que seleciona todos os registros da tabela Customers em que o campo Country contém "Mexico". MODIFY VIEW exibe a exibição no Designer de exibições para que você possa editá-la. Depois de fechar o Designer de exibições, DELETE VIEW exclui a exibição.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Northwind\Northwind')
CREATE SQL VIEW MyView AS SELECT * FROM Northwind!Customers;
   WHERE Country="Mexico"
MODIFY VIEW MyView
DELETE VIEW MyView
```

Para obter mais informações, consulte Comandos CLOSE, Comando OPEN DATABASE, Comando MODIFY VIEW e Comando DELETE VIEW.

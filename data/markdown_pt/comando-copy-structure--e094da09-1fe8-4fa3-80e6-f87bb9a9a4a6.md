# Comando COPY STRUCTURE

Cria uma nova tabela vazia com a mesma estrutura da tabela atualmente selecionada.

```foxpro
COPY STRUCTURE TO TableName   [FIELDS FieldList]
[[WITH] CDX | [WITH] PRODUCTION]
[DATABASE cDatabaseName [NAME cTableName]]
```

#### Parâmetros
 **TableName**
Especifica o nome da nova tabela vazia a criar. No Visual FoxPro, o suporte a valores nulos e a página de código da nova tabela livre são idênticos aos da tabela atualmente selecionada.
**FIELDS FieldList**
Especifica que somente os campos cujos nomes são especificados em FieldList são copiados para a nova tabela. Se você omitir FIELDS FieldList , todos os campos são copiados para a nova tabela.
**[WITH] CDX | [WITH] PRODUCTION**
Cria um arquivo de índice estrutural para a nova tabela que é idêntico ao arquivo de índice estrutural da tabela existente. As tags e expressões de índice do arquivo de índice estrutural original são copiadas para o novo arquivo de índice estrutural. As cláusulas CDX e PRODUCTION são idênticas. No Visual FoxPro, um índice primário da tabela atualmente selecionada é convertido em um índice candidato para a nova tabela vazia.
**DATABASE cDatabaseName**
Especifica o nome de um banco de dados existente ao qual a nova tabela é adicionada. Observe que as propriedades de tabela e campo não são copiadas para o banco de dados.
**NAME cTableName**
Especifica o nome da tabela conforme aparece no banco de dados.

# Exemplo

No exemplo a seguir, a tabela `customer` é aberta, sua estrutura é copiada para uma tabela chamada `backup` e `backup` é aberta. APPEND FROM então anexa registros à tabela `backup` da tabela `customer`, e uma janela Browse é aberta para a tabela `backup`.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
COPY STRUCTURE TO backup
USE backup
APPEND FROM customer FOR country = 'UK'
BROWSE FIELDS contact, country
USE
DELETE FILE backup.dbf
```

# Comando UPDATE - SQL

Atualiza registros em uma tabela com novos valores.

> **Observação:** O comando SQL UPDATE pode atualizar registros de apenas uma tabela.

```foxpro
UPDATE Target
   SET Column_Name1 = eExpression1 [, Column_Name2 = eExpression2 ...]
   [FROM [FORCE] Table_List_Item [[, ...] | [JOIN [ Table_List_Item]]]
   WHERE FilterCondition1 [AND | OR FilterCondition2 ...]
```

#### Parâmetros
 **UPDATE Target**
Especifica uma tabela de destino, cursor, alias de tabela ou cursor, ou arquivo a ser atualizado. Você pode incluir várias fontes de dados para a operação de atualização na cláusula FROM. Target pode ter as seguintes sintaxes: [ DatabaseName !] TableName DatabaseName ! especifica o nome de um banco de dados que contém a tabela se a tabela estiver em um banco de dados que não é o atual. Se a tabela estiver em um banco de dados que não é o atual, você deve incluir o nome do banco de dados. Use um ponto de exclamação (!) como delimitador imediatamente após o nome do banco de dados e antes do nome da tabela. TableName especifica o nome de uma tabela para a operação de atualização. Alias Alias especifica um alias que corresponde a uma tabela na cláusula FROM ou a um cursor na sessão de dados atual para a operação de atualização. FileName FileName especifica o nome de um arquivo para a operação de atualização.
**SET Column_Name1 = eExpression1 [, Column_Name2 = eExpression2 ...]**
Especifica as colunas na tabela a serem atualizadas e seus novos valores. Se você omitir a cláusula WHERE, cada linha na tabela é atualizada com o mesmo valor. Se você deseja usar uma propriedade de objeto em uma expressão, precisa especificar uma variável de memória e então usar essa variável na expressão. Por exemplo, você pode especificar x = oColField("iid").Value e então usar a cláusula SET set iid = x no seu comando UPDATE - SQL. Se você usar a propriedade do objeto, ou seja, objectname.property, diretamente na expressão, o comando a usa como um alias e falha. Você pode incluir uma subconsulta na cláusula SET para especificar uma expressão. Se a subconsulta não retornar nenhum resultado, retorna NULL . Para sintaxe e informações sobre subconsultas, consulte SELECT - SQL Command - FROM Clause . Observação Se você usar uma subconsulta na cláusula SET, não pode usar subconsultas na cláusula WHERE. Uma subconsulta na cláusula SET deve atender exatamente aos mesmos requisitos que subconsultas usadas em operações de comparação.
**[FROM [FORCE] Table_List_Item [[, ...] | [JOIN [ Table_List_Item ]]]]**
Especifica uma ou mais tabelas contendo os dados para a operação de atualização. A cláusula FROM tem a mesma sintaxe que no comando SQL SELECT, exceto pelas seguintes restrições: A tabela ou cursor de destino não pode ser incluído em um OUTER join como tabela ou cursor secundário. Deve ser possível avaliar todas as outras operações JOIN antes de executar uma operação JOIN na tabela de destino. O cursor de destino não pode ser o resultado de uma subconsulta. Para obter mais informações, consulte SELECT - SQL Command . FORCE especifica que as tabelas na lista de tabelas são unidas na ordem em que aparecem na cláusula FROM. Observação Se FORCE for omitido, o Visual FoxPro tenta otimizar a operação de atualização. No entanto, a operação de atualização pode ser executada mais rapidamente incluindo a palavra-chave FORCE para desabilitar a otimização de atualização do Visual FoxPro. Table_List_Item pode ter as seguintes sintaxes: [ DatabaseName !] Table [[AS] Local_Alias ] DatabaseName ! especifica o nome de um banco de dados que contém a tabela se a tabela estiver em um banco de dados que não é o atual. Se a tabela estiver em um banco de dados que não é o atual, você deve incluir o nome do banco de dados. Use um ponto de exclamação (!) como delimitador imediatamente após o nome do banco de dados e antes do nome da tabela. Table especifica o nome da tabela ou cursor do qual você deseja atualizar dados. Se nenhuma tabela estiver aberta, o Visual FoxPro exibe a caixa de diálogo Open para que você possa especificar a localização do arquivo. Depois que a tabela é aberta, ela permanece aberta quando a consulta é concluída. Local_Alias especifica um nome temporário para a tabela especificada em Table . Se você especificar um alias local, deve usar o alias local em vez do nome da tabela na instrução UPDATE. O alias pode representar uma tabela ou um cursor. JOIN fornece a capacidade de especificar uma ou mais tabelas secundárias. Não há limite fixo no número de tabelas, aliases ou cláusulas JOIN por instrução UPDATE. ( Subquery ) AS Subquery_Alias Uma subconsulta especifica uma instrução SELECT dentro de outra instrução SELECT. Para obter mais informações sobre subconsultas em instruções SELECT, consulte a cláusula FROM em SELECT - SQL Command .
**WHERE FilterCondition1 [AND | OR FilterCondition2 ...]]**
Especifica uma ou mais condições de filtro que os registros devem atender para serem atualizados com novos valores. Não há limite para o número de condições de filtro na cláusula WHERE. Para inverter o valor de uma expressão lógica, use o operador NOT. Para verificar se um campo está vazio, use a função EMPTY( ) . Para obter mais informações, consulte EMPTY( ) Function .

# Observações

Para determinar o número de registros atualizados, verifique o valor da variável de sistema _TALLY imediatamente após executar o comando SQL UPDATE. Para obter mais informações, consulte _TALLY System Variable.

> **Dica:** Ao atualizar vários registros em uma tabela aberta para acesso compartilhado, SQL UPDATE usa bloqueio de registro, diferentemente do comando REPLACE. Isso reduz a contenção de registros em situações multiusuário, mas pode reduzir o desempenho. Para desempenho máximo, abra a tabela para uso exclusivo ou use a função FLOCK( ) para bloquear a tabela. Para obter mais informações, consulte FLOCK( ) Function .

Na cláusula SET, o Visual FoxPro processa a atribuição sequencialmente. Se você emitir o comando, `UPDATE table1 SET field1 = field2, field2=field1`, os valores dos dois campos não são trocados; em vez disso, os valores de F1 e F2 são os mesmos.

# Exemplos de código legado

### Exemplo 1

O exemplo a seguir usa o comando OPEN DATABASE para abrir o banco de dados de exemplo do Visual FoxPro e o comando USE para abrir a tabela Customer em TestData.dbc. A instrução SQL UPDATE atualiza todos os valores no campo MaxOrdAmt para "25".

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Customer
UPDATE Customer SET MaxOrdAmt = 25
BROWSE FIELDS Company, MaxOrdAmt
```

Para obter mais informações, consulte USE Command e BROWSE Command.

### Exemplo 2

O exemplo a seguir usa o comando OPEN DATABASE para abrir o banco de dados de exemplo do Visual FoxPro, TestData.dbc. O comando SQL SELECT recupera dados da tabela Products em TestData.dbc, armazena em uma tabela, MyProductsList, e exibe a nova tabela.

O comando CREATE CURSOR cria o MyUpdateTable com um campo Prod_Unit contendo um valor inteiro de 10 e exibe a tabela.

O comando SQL UPDATE atualiza o campo In_Stock para MyProductsList com o valor de MyUpdateTable para o nome do produto, "Chai". O comando SQL SELECT retorna e exibe uma consulta para MyProductsList mostrando o campo In_Stock atualizado para o produto, "Chai".

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT in_stock, prod_name ;
    FROM Products ;
    INTO TABLE MyProductsList.dbf
BROWSE
CREATE CURSOR MyUpdateTable (prod_unit I(10))
INSERT INTO MyUpdateTable (prod_unit) VALUES (10)
BROWSE
UPDATE MyProductsList ;
    SET MyProductsList.in_stock = MyUpdateTable.prod_unit ;
    FROM MyUpdateTable ;
    WHERE MyProductsList.prod_name = "Chai"
SELECT * FROM MyProductsList
```

Para obter mais informações, consulte OPEN DATABASE Command, BROWSE Command, CREATE CURSOR - SQL Command e INSERT - SQL Command.

# Exemplos de código

### Exemplo 3

O exemplo a seguir mostra uma subconsulta usada como expressão na cláusula SET da instrução UPDATE. A consulta atualiza todos os registros na tabela products. Se não houver productID correspondente na tabela mfg_msrp, o campo unitprice é definido como NULL.

```foxpro
UPDATE products ;
   SET unitprice = ;
       (SELECT (msrp*.90) ;
          FROM mfg_msrp ;
         WHERE mfg_msrp.productID = products.productID ;
           AND mfg_msrp.discontinued = .f.)
```

### Exemplo 4

O exemplo a seguir mostra uma atualização correlacionada que toca apenas registros que correspondem às condições de filtro na cláusula WHERE.

```foxpro
UPDATE products ;
   SET unitprice = mfg_msrp.msrp*.90 ;
  FROM mfg_msrp ;
 WHERE mfg_msrp.productID = products.productID;
   AND mfg_msrp.discontinued = .f.
```

### Exemplo 5

O exemplo a seguir é de uma atualização correlacionada em que os resultados da atualização incluem apenas a primeira correspondência encontrada para um registro. Outras correspondências para o registro são ignoradas. O código de exemplo especifica dois cursors. O primeiro é o destino das atualizações. O segundo é a fonte das atualizações e contém duas alterações para o primeiro registro no cursor de destino e uma atualização que não corresponde a nenhum registro no cursor de destino. Nos resultados, o valor do primeiro registro mostra a primeira correspondência de .50 e não 10.00, o valor da segunda correspondência.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyProducts (ProdID I , ProdCategory I NULL, MSRP Y NULL)
INSERT INTO MyProducts VALUES (1,9,1.00)
INSERT INTO MyProducts VALUES (2,8,2.00)
INSERT INTO MyProducts VALUES (3,7,3.00)

CREATE CURSOR MyUpdates (ProdID I , MSRP Y)
INSERT INTO MyUpdates VALUES (1,.50) && Matches and updates.
INSERT INTO MyUpdates VALUES (2,20.00) && Matches and updates.
INSERT INTO MyUpdates VALUES (4,40.00) && No match
INSERT INTO MyUpdates VALUES (1,10.00)&& 2nd match but no update.
UPDATE MyProducts SET MSRP=MyUpdates.MSRP FROM MyUpdates WHERE MyProducts.ProdID=MyUpdates.ProdID
SELECT MyProducts
BROWSE
```

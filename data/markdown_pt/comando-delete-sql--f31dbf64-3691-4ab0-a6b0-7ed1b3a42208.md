# Comando DELETE - SQL

Marca registros para exclusão.

> **Observação:** Registros marcados para exclusão não são removidos fisicamente da tabela até que o comando PACK seja emitido. Você pode desfazer a marcação (desmarcar) de registros para exclusão usando o comando RECALL. Para obter mais informações, consulte PACK Command e RECALL Command.

```foxpro
DELETE [Target] FROM [FORCE] Table_List [[, Table_List ...] | [JOIN [ Table_List]]]
   [WHERE FilterCondition1 [AND | OR FilterCondition2 ...]]
```

#### Parâmetros
 **DELETE [ Target ]**
Especifica uma tabela de destino, cursor, alias de tabela ou cursor, ou arquivo para a operação de exclusão. Se o FROM especificar mais de uma tabela, você deve incluir o parâmetro Target. Target pode ter as seguintes sintaxes: [ DatabaseName !] TableName DatabaseName ! especifica o nome de um banco de dados que contém a tabela se a tabela estiver em um banco de dados não atual. Se a tabela estiver em um banco de dados não atual, você deve incluir o nome do banco de dados. Use um ponto de exclamação (!) como delimitador imediatamente após o nome do banco de dados e antes do nome da tabela. TableName especifica o nome de uma tabela para a operação de exclusão. Alias Alias especifica um alias que corresponde a uma tabela na cláusula FROM ou a um cursor na sessão de dados atual para a operação de exclusão. FileName FileName especifica o nome de um arquivo para a operação de exclusão.
**FROM [FORCE] Table_List [[, Table_List ...] | [JOIN [ Table_List ]]]**
Especifica uma ou mais tabelas contendo os dados para a operação de exclusão. A cláusula FROM tem a mesma sintaxe do comando SQL SELECT, exceto pelas seguintes restrições: A tabela ou cursor de destino não pode ser incluído em um OUTER join como tabela ou cursor secundário. Deve ser possível avaliar todas as outras operações JOIN antes de executar uma operação JOIN na tabela de destino. O cursor de destino não pode ser o resultado de uma subconsulta. Para obter mais informações, consulte SELECT - SQL Command. FORCE especifica que as tabelas em Table_List são unidas na ordem em que aparecem na cláusula FROM. Observação Se FORCE for omitido, o Visual FoxPro tenta otimizar a operação de exclusão. No entanto, a operação de exclusão pode ser executada mais rapidamente incluindo a palavra-chave FORCE para desabilitar a otimização de exclusão do Visual FoxPro. Table_List pode ter as seguintes sintaxes: [ DatabaseName !] Table [[AS] Local_Alias ] DatabaseName ! especifica o nome de um banco de dados que contém a tabela se a tabela estiver em um banco de dados não atual. Se a tabela estiver em um banco de dados não atual, você deve incluir o nome do banco de dados. Use um ponto de exclamação (!) como delimitador imediatamente após o nome do banco de dados e antes do nome da tabela. Table especifica o nome da tabela ou cursor do qual você deseja recuperar dados. Se nenhuma tabela estiver aberta, o Visual FoxPro exibe a caixa de diálogo Open para que você possa especificar a localização do arquivo. Depois que a tabela é aberta, ela permanece aberta quando a consulta é concluída. Local_Alias especifica um nome temporário para a tabela especificada em Table. Se você especificar um alias local, deve usar o alias local em vez do nome da tabela em toda a instrução DELETE. O alias pode representar uma tabela ou um cursor. JOIN fornece a capacidade de especificar uma ou mais tabelas secundárias. Não há limite fixo no número de tabelas, aliases ou cláusulas JOIN por instrução DELETE. ( Subquery ) AS Subquery_Alias Subquery especifica uma instrução SELECT dentro de outra instrução SELECT. Para obter mais informações sobre subconsultas em instruções SELECT, consulte SELECT - SQL Command - FROM Clause.
**WHERE FilterCondition1 [AND | OR FilterCondition2 ...]**
Especifica uma ou mais condições de filtro que os registros devem atender para serem excluídos. Não há limite para o número de condições de filtro na cláusula WHERE. Para inverter o valor de uma expressão lógica, use o operador NOT. Para verificar se um campo está vazio, use a função EMPTY( ). Para obter mais informações, consulte EMPTY( ) Function.

# Observações

Se o comando SET DELETED estiver definido como ON, registros marcados para exclusão são ignorados por todos os comandos que incluem um escopo. Para obter mais informações, consulte SET DELETED Command.

Para determinar o número de registros atualizados, verifique o valor da variável de sistema _TALLY imediatamente após executar o comando SQL DELETE. Para obter mais informações, consulte _TALLY System Variable.

> **Dica:** Ao marcar vários registros para exclusão em uma tabela aberta para acesso compartilhado, SQL DELETE usa bloqueio de registro, diferentemente do comando DELETE. Isso reduz a contenção de registros em situações multiusuário, mas pode reduzir o desempenho. Para desempenho máximo, abra a tabela para uso exclusivo ou use a função FLOCK( ) para bloquear a tabela. Para obter mais informações, consulte DELETE Command e FLOCK( ) Function.

# Exemplo 1

O exemplo a seguir usa o comando OPEN DATABASE para abrir o banco de dados de amostra Visual FoxPro, TestData.dbc. O comando USE abre a tabela Customer em TestData.dbc. A instrução SQL DELETE marca para exclusão aqueles registros em que o campo Country contém "USA". O comando CLEAR apaga a janela principal do Visual FoxPro. O comando LIST lista todos os registros marcados para exclusão. Após o comando LIST, se o comando PACK fosse chamado, os registros marcados seriam excluídos.

O comando RECALL ALL desmarca todos os registros marcados para exclusão. O comando COUNT verifica o número de registros marcados para exclusão contando-os. WAIT WINDOW exibe esse número de registros que foram marcados para exclusão.

```foxpro
CLOSE DATABASES
CLEAR
OPEN DATABASE HOME(2)+"Data\TestData"
USE Customer
DELETE FROM Customer WHERE country = "USA"
CLEAR
LIST FIELDS company, country FOR DELETED()
WAIT WINDOW "Records currently marked for deletion"+CHR(13) + ;
   "Press any key to revert..."
RECALL ALL
CLEAR
COUNT FOR DELETED()=.T. TO nDeleted
WAIT WINDOW ALLTRIM(STR(nDeleted)) + " records marked for deletion."
```

Para obter mais informações, consulte OPEN DATABASE Command, USE Command, LIST Commands, CLEAR Commands, COUNT Command e WAIT Command.

# Exemplo 2

O código a seguir mostra uma exclusão correlacionada na qual registros em um cursor MyProducts são marcados para exclusão com base no valor do campo Discontinued no cursor MSRPList. A cláusula WHERE especifica os critérios para correspondência de registros e a condição avaliada para marcar os registros.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyProducts (ProdID I , OurPrice Y NULL)
INSERT INTO MyProducts VALUES (1,1.10) && matches but is not marked for deletion
INSERT INTO MyProducts VALUES (2,2.20) && matches and is marked
INSERT INTO MyProducts VALUES (3,3.30) && matches and is marked
CREATE CURSOR MSRPList (ProdID I , ProdCategory I Null, MSRP Y, Discontinued L)
INSERT INTO MSRPList VALUES (1, 9, 1.00, .f.)
INSERT INTO MSRPList VALUES (2, 8, 2.00, .t.)
INSERT INTO MSRPList VALUES (3, 7, 3.00, .t.)
DELETE  MyProducts FROM MSRPList ;
   WHERE MSRPList.ProdID = MyProducts.ProdID;
      AND MSRPList.discontinued = .t.
SELECT MyProducts
BROWSE
```

Para obter mais informações e outro exemplo, consulte SQL Language Improvements.

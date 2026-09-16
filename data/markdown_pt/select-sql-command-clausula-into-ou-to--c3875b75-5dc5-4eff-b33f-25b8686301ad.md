# SELECT - SQL Command - Cláusula INTO ou TO

As cláusulas INTO ou TO especificam opções de saída que determinam o local para armazenar ou enviar os resultados finais da consulta de uma instrução SQL SELECT.

Para obter mais informações, consulte SELECT - SQL Command.

A sintaxe detalhada da cláusula INTO ou TO é a seguinte:

```foxpro
[INTO StorageDestination | TO DisplayDestination ]
```

#### Parâmetros
 **[INTO StorageDestination ]**
Armazena os resultados da consulta em um array, cursor ou tabela. Observação Se você não incluir a cláusula INTO, os resultados da consulta são exibidos em uma janela Browse por padrão. Para direcionar os resultados da consulta para a impressora ou um arquivo, use a cláusula TO. A tabela a seguir descreve locais nos quais você pode armazenar os resultados da consulta usando a cláusula INTO. StorageDestination Descrição ARRAY ArrayName Armazena os resultados da consulta em um array de variáveis de memória. Observação Se a consulta selecionar zero registros, o array não é criado. CURSOR CursorName [NOFILTER | READWRITE] Armazena os resultados da consulta em um cursor temporário. Observação Se você especificar o nome de uma tabela aberta, o Visual FoxPro gera uma mensagem de erro. Depois que SELECT é executado, o cursor temporário permanece aberto e ativo e somente leitura, a menos que você especifique a opção READWRITE. Quando você fecha esse cursor temporário, ele é excluído. Cursors podem existir como um arquivo temporário na unidade ou volume especificado por SORTWORK. NOFILTER cria um cursor que pode ser usado em consultas subsequentes. Observação Incluir NOFILTER pode reduzir o desempenho da consulta porque cria uma tabela temporária em disco. Quando o cursor é fechado, a tabela temporária é excluída do disco. READWRITE especifica que o cursor temporário é modificável. Se as tabelas de origem usarem auto-incremento, o cursor criado com READWRITE não herda essas configurações. Você pode criar mais de um índice estrutural em um cursor usando o argumento READWRITE. TABLE TableName [DATABASE DatabaseName [NAME LongTableName ]] Armazena os resultados da consulta em uma tabela. Cuidado Se você especificar uma tabela que está aberta e SET SAFETY estiver definido como OFF, o Visual FoxPro sobrescreve a tabela sem aviso. Se você não especificar uma extensão, o Visual FoxPro atribui à tabela uma extensão .dbf. A tabela permanece aberta e ativa depois que SELECT é executado. DATABASE DatabaseName especifica um banco de dados ao qual você pode adicionar a tabela. NAME LongTableName especifica um nome longo para a tabela. Nomes longos podem conter até 128 caracteres e podem ser usados no lugar de nomes de arquivo curtos no banco de dados.
**[TO DisplayDestination ]**
Envia os resultados da consulta para um arquivo, impressora, janela principal do Visual FoxPro ou uma janela definida pelo usuário ativa. Observação O Visual FoxPro ignora a cláusula TO se você também incluir a cláusula INTO na mesma consulta. A tabela a seguir descreve locais para os quais você pode enviar os resultados da consulta usando a cláusula TO. DisplayDestination Descrição FILE FileName [ADDITIVE] Especifica um arquivo de texto ASCII para o qual você pode direcionar os resultados da consulta. ADDITIVE anexa a saída da consulta ao conteúdo existente do arquivo de texto especificado por FileName . PRINTER [PROMPT] Direciona a saída da consulta para uma impressora. PROMPT exibe uma caixa de diálogo de impressora antes de a impressão começar. Você pode ajustar as configurações da impressora na caixa de diálogo. As configurações da impressora que você pode ajustar dependem do driver de impressora instalado atualmente. SCREEN Direciona a saída da consulta para a janela principal do Visual FoxPro ou uma janela definida pelo usuário ativa.

# Observações

O código a seguir mostra um resumo das cláusulas principais do comando SELECT - SQL:

```foxpro
SELECT Select_List
   FROM Table_List
...[WITH (BUFFERING = lExpr)]
   [WHERE Conditions]
   [GROUP BY Column_List]
   [UNION Clause]
   [HAVING Conditions]
   [ORDER BY Column_List]
   [INTO Clause | TO Clause ]
   [Additional_Display_Options]
```

Para obter mais informações sobre uma cláusula particular do comando SQL SELECT, consulte os tópicos a seguir:
 - SELECT Clause
- FROM Clause
- SELECT - SQL Command - WITH Clause
- SELECT - SQL Command - WHERE Clause
- GROUP BY Clause
- HAVING Clause
- UNION Clause
- ORDER BY Clause
- Additional Display Options

# Exemplo

O exemplo a seguir armazena o conteúdo de uma consulta em uma tabela usando a cláusula INTO TABLE TableName. O exemplo armazena o conteúdo dos campos Company, Order_Date e Shipped_On das tabelas Customer e Order, que são unidas no campo Cust_ID, em uma terceira tabela chamada CustShip. O exemplo então abre uma janela Browse para a nova tabela. A instrução SELECT especifica aliases locais para as tabelas para distinguir o mesmo nome de campo, Cust_ID, em ambas as tabelas.

```foxpro
CLOSE ALL
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\TestData')
SELECT TAlias1.company, TAlias2.order_date, TAlias2.shipped_on ;
   FROM customer TAlias1, orders TAlias2 ;
   WHERE TAlias1.cust_id = TAlias2.cust_id ;
   INTO TABLE custship.dbf
BROWSE
```

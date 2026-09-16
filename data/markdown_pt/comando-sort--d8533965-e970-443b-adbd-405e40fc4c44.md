# Comando SORT

Classifica registros na tabela atualmente selecionada e envia os registros classificados para uma nova tabela.

```foxpro
SORT TO TableName ON FieldName1 [/A | /D] [/C]
   [, FieldName2 [/A | /D] [/C] ...]   [ASCENDING | DESCENDING]
   [Scope] [FOR lExpression1] [WHILE lExpression2]
   [FIELDS FieldNameList   | FIELDS LIKE Skeleton
   | FIELDS EXCEPT Skeleton]   [NOOPTIMIZE]
```

#### Parâmetros
 **TableName**
Especifica o nome da nova tabela que contém os registros classificados. O Visual FoxPro assume uma extensão de nome de arquivo .dbf para tabelas. Uma extensão .dbf é atribuída automaticamente se o nome de arquivo que você incluir não tiver uma extensão.
**ON FieldName1**
Especifica o campo na tabela atualmente selecionada no qual a classificação é baseada. O conteúdo e o tipo de dados do campo determinam a ordem dos registros na nova tabela. Por padrão, a classificação é feita em ordem ascendente. Você não pode classificar em campos memo ou general. O exemplo a seguir classifica uma tabela no campo cust_id. A tabela customer é aberta e classificada, criando uma nova tabela chamada temp . Os registros em temp são ordenados pelo campo cust_id. CLOSE DATABASES OPEN DATABASE (HOME(2) + 'data\testdata') USE customer && Opens Customer table CLEAR LIST FIELDS company, cust_id NEXT 3 SORT TO temp ON cust_id USE temp LIST FIELDS company, cust_id NEXT 3 WAIT WINDOW 'Now sorted on CUST_ID' NOWAIT Você pode incluir nomes de campos adicionais ( FieldName2 , FieldName3 ) para ordenar ainda mais a nova tabela. O primeiro campo FieldName1 é o campo de classificação primária, o segundo campo FieldName2 é o campo de classificação secundária, e assim por diante.
**[/A | /D] [/C]**
Para cada campo que você incluir na classificação, pode especificar uma ordem de classificação ascendente ou descendente. /A especifica uma ordem ascendente para o campo. /D especifica uma ordem descendente. /A ou /D pode ser incluído com qualquer tipo de campo. Por padrão, a ordem de classificação para campos de caracteres é sensível a maiúsculas e minúsculas. Se você incluir a opção /C após o nome de um campo de caracteres, a distinção de maiúsculas e minúsculas é ignorada. Você pode combinar a opção /C com a opção /A ou /D. Por exemplo, /AC ou /DC. No exemplo a seguir, uma nova tabela chamada clients é criada. A tabela orders é classificada no campo order_date em ordem ascendente e no campo freight em ordem descendente. USE orders SORT TO clients ON order_date/A,freight/D
**ASCENDING**
Especifica uma ordem ascendente para todos os campos não seguidos por /D.
**DESCENDING**
Especifica uma ordem descendente para todos os campos não seguidos por /A. Se você omitir ASCENDING ou DESCENDING, a ordem de classificação é ascendente por padrão.
**Scope**
Especifica um intervalo de registros a classificar. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber e REST. O escopo padrão para SORT é TODOS os registros.
**FOR lExpression1**
Especifica que apenas os registros na tabela atual para os quais a condição lógica lExpression1 avalia como verdadeiro (.T.) são incluídos na classificação. Incluir FOR permite classificar registros condicionalmente, filtrando registros indesejados. A otimização de consulta Rushmore otimiza um comando SORT ... FOR se lExpression1 é uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Uma discussão sobre expressões que Rushmore pode otimizar aparece em Otimizando aplicativos .
**WHILE lExpression2**
Especifica uma condição pela qual registros da tabela atual são incluídos na classificação enquanto a expressão lógica lExpression2 avalia como verdadeiro (.T.).
**FIELDS FieldNameList**
Especifica campos da tabela original a incluir na nova tabela que SORT cria. Se você omitir a cláusula FIELDS, todos os campos da tabela original são incluídos na nova tabela.
**FIELDS LIKE Skeleton**
Especifica que campos da tabela original que correspondem ao esqueleto de campo Skeleton são incluídos na nova tabela que SORT cria.
**FIELDS EXCEPT Skeleton**
Especifica que todos os campos, exceto aqueles que correspondem ao esqueleto de campo Skeleton, são incluídos na nova tabela que SORT cria. O esqueleto de campo Skeleton suporta curingas. Por exemplo, para especificar que todos os campos que começam com as letras A e P são incluídos na nova tabela, use o seguinte: SORT TO mytable ON myfield FIELDS LIKE A*,P* A cláusula LIKE pode ser combinada com a cláusula EXCEPT: SORT TO mytable ON myfield FIELDS LIKE A*,P* EXCEPT PARTNO*
**NOOPTIMIZE**
Desabilita a otimização Rushmore de SORT. Para obter mais informações, consulte Comando SET OPTIMIZE e Usando a otimização de consulta Rushmore para acelerar o acesso a dados .

# Observações

Um ou mais campos especificados na tabela atual determinam a ordem em que os registros aparecem na nova tabela.

> **Cuidado:** Certifique-se de ter espaço em disco suficiente para a nova tabela e os arquivos de trabalho temporários criados durante a classificação. O espaço em disco necessário para executar uma classificação pode ser até três vezes o tamanho da tabela de origem. A quantidade de espaço em disco disponível pode ser determinada com DISKSPACE() e SYS(2020). Se você ficar sem espaço em disco durante uma classificação, o Visual FoxPro exibe uma mensagem de erro e os arquivos de trabalho temporários são excluídos.

Campos de tipo caractere que contêm números e espaços podem não ser classificados na ordem que você espera. Campos numéricos são preenchidos da direita para a esquerda, com espaços vazios à esquerda. Em contraste, campos de caracteres são preenchidos da esquerda para a direita, com espaços vazios à direita.

Por exemplo, se dois registros em uma tabela contêm um campo de caracteres com 1724 em um registro e 18 no outro, e a tabela é classificada neste campo em ordem ascendente, o registro contendo 1724 aparece antes do registro contendo 18. Isso ocorre porque o Visual FoxPro lê cada caractere nos campos de caracteres da esquerda para a direita, e porque 17 (em 1724) é menor que 18 (em 18), ele coloca 1724 primeiro. Para evitar este problema, sempre preceda números menores com zeros à esquerda (0018) ou torne o campo numérico.

# Comando TOTAL

Calcula totais para campos numéricos na tabela atualmente selecionada.

```foxpro
TOTAL TO TableName ON FieldName   [FIELDS FieldNameList]   [Scope]
   [FOR lExpression1]   [WHILE lExpression2]   [NOOPTIMIZE]
```

#### Parâmetros
 **TableName**
Especifica o nome da tabela que conterá os totais. Se a tabela especificada não existir, o Visual FoxPro a cria. Se a tabela existir e SET SAFETY estiver ON, o Visual FoxPro pergunta se você deseja substituir a tabela existente. Se SET SAFETY estiver OFF, você não é solicitado e a tabela de saída é substituída.
**FieldName**
Especifica o campo no qual os totais são agrupados. A tabela deve estar classificada neste campo ou um índice aberto ou tag de índice deve ter este campo como expressão de chave.
**FIELDS FieldNameList**
Especifica os campos a serem totalizados. Separe os nomes dos campos na lista com vírgulas. Se você omitir a cláusula FIELDS, todos os campos numéricos são totalizados por padrão.
**Scope**
Especifica um intervalo de registros a totalizar. O escopo padrão para TOTAL é TODOS os registros. As cláusulas de escopo são: ALL, NEXT nRecords, RECORD nRecordNumber e REST. Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses.
**FOR lExpression1**
Especifica uma condição pela qual apenas os registros que satisfazem a condição lógica lExpression1 são incluídos nos totais. Rushmore Query Optimization otimiza uma consulta criada com TOTAL ... FOR se lExpression1 for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte o comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access.
**WHILE lExpression2**
Especifica uma condição pela qual registros da tabela atual são incluídos nos totais enquanto a expressão lógica lExpression2 for avaliada como true (.T.).
**NOOPTIMIZE**
Desabilita a otimização Rushmore de TOTAL. Para obter mais informações, consulte o comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access.

# Observações

A tabela na área de trabalho atualmente selecionada deve estar classificada ou indexada. Um total separado é calculado para cada conjunto de registros com um valor de campo comum ou valor de chave de índice exclusivo. Os resultados são colocados em registros em uma segunda tabela. Um registro é criado na segunda tabela para cada valor de campo comum ou valor de chave de índice exclusivo.

Overflow numérico pode ocorrer se os campos numéricos na segunda tabela não forem largos o suficiente para conter os totais. O Visual FoxPro conserva as porções mais significativas dos totais quando ocorre overflow numérico. Quando um campo é muito pequeno para aceitar um total:
 - As casas decimais são truncadas e a porção decimal restante do total é arredondada.
- Se o total ainda não couber, a notação científica é usada se o campo total contiver sete ou mais dígitos.
- Finalmente, asteriscos substituem o conteúdo do campo.

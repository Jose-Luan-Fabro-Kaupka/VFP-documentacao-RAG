# Comando AVERAGE

Calcula a média aritmética de expressões numéricas ou campos.

```foxpro
AVERAGE [ExpressionList]   [Scope] [FOR lExpression1] [WHILElExpression2]
   [TO VarList | TO ARRAY ArrayName]   [NOOPTIMIZE]
```

#### Parâmetros
 **ExpressionList**
Especifica as expressões a calcular a média. ExpressionList pode ser uma lista de campos da tabela separados por vírgulas ou expressões numéricas envolvendo campos da tabela.
**Scope**
Especifica o registro ou intervalo de registros a incluir na média. Apenas os registros que estão no intervalo de registros especificado pelo escopo são incluídos na média. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber e REST. O escopo padrão para AVERAGE é TODOS os registros. Comandos que incluem Scope operam apenas na tabela na área de trabalho ativa.
**FOR lExpression1**
Especifica uma condição pela qual apenas os registros que satisfazem a condição lógica lExpression são incluídos. Este argumento permite filtrar registros indesejados. Rushmore Query Optimization otimiza uma consulta AVERAGE FOR se lExpression for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para informações sobre expressões otimizáveis pelo Rushmore, consulte o Comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access .
**WHILElExpression2**
Especifica que, enquanto a expressão lógica lExpression2 avaliar como true (.T.), os registros são incluídos na média.
**TO VarList**
Especifica a lista de variáveis ou elementos de array nos quais os resultados da média são armazenados.
**TO ARRAY ArrayName**
Especifica o array unidimensional no qual os resultados da média são armazenados. O array unidimensional pode ser criado antes da execução de AVERAGE. Se o array incluído em AVERAGE não existir, o Visual FoxPro cria automaticamente. Se o array existir e não for grande o suficiente para conter todos os resultados, o Visual FoxPro aumenta automaticamente o tamanho do array para acomodar as informações.
**NOOPTIMIZE**
Desabilita a otimização Rushmore de AVERAGE. Para obter mais informações, consulte o Comando SET OPTIMIZE e Using Rushmore Query Optimization to Speed Data Access .

# Observações

Todos os campos numéricos na tabela selecionada são incluídos na média, a menos que você inclua uma lista de expressões opcional. O resultado é exibido na tela se SET TALK estiver ON. Se SET HEADINGS estiver ON, os nomes dos campos ou expressões envolvendo os nomes dos campos são exibidos acima dos resultados.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE orders  && Open order table
CLEAR
AVERAGE Order_Amt  && Calcuate averages of all orders
AVERAGE Order_Amt TO gnAvg  && Store average to memory variable
? 'Average order amount: '
?? gnAvg  && Display the average again
```

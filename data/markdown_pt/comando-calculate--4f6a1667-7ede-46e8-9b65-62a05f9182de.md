# Comando CALCULATE

Executa operações financeiras e estatísticas em campos de uma tabela ou em expressões que envolvem campos.

```foxpro
CALCULATE eExpressionList [Scope] [FOR lExpression1] [WHILE lExpression2]
   [TO VarList | TO ARRAY ArrayName] [NOOPTIMIZE]
   [IN nWorkArea | cTableAlias]
```

#### Parâmetros
 **eExpressionList**
Especifica as expressões que podem conter qualquer combinação das seguintes funções: AVG( nExpression ) CNT( ) ou COUNT( ) MAX( eExpression ) MIN( eExpression ) NPV( nExpression1 , nExpression2 [, nExpression3 ]) STD( nExpression ) SUM( nExpression ) VAR( nExpression ) As funções na lista de expressões eExpressionList são separadas por vírgulas. Essas funções são específicas do CALCULATE e são descritas em detalhes mais adiante nesta seção. Elas não devem ser confundidas com funções independentes de nomes semelhantes. Por exemplo, CALCULATE MIN( ) não é o mesmo que MIN( ).
**Scope**
Especifica um intervalo de registros usado no cálculo. Somente os registros que estão dentro do intervalo de registros são incluídos no cálculo. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber e REST. Para obter mais informações, consulte Scope Clauses . Comandos que incluem Scope operam somente na tabela na área de trabalho ativa. O escopo padrão para CALCULATE é ALL registros.
**FOR lExpression1**
Especifica que somente os registros que satisfazem a condição lógica lExpression1 são incluídos no cálculo. Incluir uma cláusula FOR inclui registros condicionalmente no cálculo, filtrando registros indesejados. A Rushmore Query Optimization otimiza uma consulta CALCULATE ... FOR se lExpression1 é uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter informações sobre expressões otimizáveis pelo Rushmore, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access .
**WHILE lExpression2**
Especifica uma condição pela qual os registros são incluídos no cálculo enquanto a expressão lógica lExpression2 avalia como verdadeira (.T.).
**TO VarList**
Especifica uma ou mais variáveis nas quais os resultados do cálculo são armazenados. Se uma variável que você especificar não existir, o Visual FoxPro cria automaticamente a variável com o nome que você especificar.
**TO ARRAY ArrayName**
Especifica um nome de array no qual os resultados do cálculo podem ser armazenados. Se o nome de array que você especificar não existir, o Visual FoxPro cria automaticamente um array com o nome que você especificar. Se o array existir e não for grande o suficiente para conter todos os resultados do cálculo, o Visual FoxPro aumenta automaticamente o tamanho do array para acomodar as informações. Se um array existente for maior do que o necessário, os elementos adicionais permanecem inalterados. Os resultados são armazenados nos elementos do array na ordem em que são especificados no comando CALCULATE.
**NOOPTIMIZE**
Desabilita a otimização Rushmore do CALCULATE. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access .
**AVG( nExpression )**
Calcula a média aritmética de nExpression . Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**CNT( ) ou COUNT( )**
Retorna o número de registros na tabela. Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**MAX( eExpression )**
Retorna o valor mais alto ou mais recente de eExpression . Dentro da cláusula MAX( ), você pode especificar qualquer campo character, date, datetime, numeric, float, integer, double ou currency, ou qualquer expressão usando campos desses tipos. Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**MIN( eExpression )**
Retorna o valor mais baixo ou mais antigo de eExpression . Qualquer campo character, date, datetime, numeric, float, integer, double ou currency, ou qualquer expressão válida usando campos desses tipos, pode ser incluído em eExpression . Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**NPV( nExpression1 , nExpression2 [, nExpression3 ])**
Calcula o valor presente líquido de uma série de fluxos de caixa futuros descontados a uma taxa de juros periódica constante. nExpression1 especifica a taxa de juros expressa como um valor decimal. nExpression2 especifica um campo, expressão de campo ou uma expressão numérica que representa uma série de fluxos de caixa. Cada fluxo de caixa pode ser positivo ou negativo. Nos casos em que nExpression2 é um campo, o valor de cada registro no campo é considerado um fluxo de caixa. nExpression3 especifica um investimento inicial opcional. Se o investimento inicial não for incluído, então o investimento inicial é assumido como ocorrendo no final do primeiro período. Este investimento inicial é o primeiro registro no campo e é negativo para representar um fluxo de saída de caixa. Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**STD( nExpression )**
Calcula o desvio padrão de nExpression . O desvio padrão mede o grau em que os valores de campos ou expressões que envolvem campos diferem da média de todos os valores. Quanto menor o desvio padrão, menos os valores variam da média. Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**SUM( nExpression )**
Totaliza os valores de nExpression . Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**VAR( nExpression )**
Calcula a variância em relação à média de nExpression . A variância é o desvio padrão ao quadrado. Quanto menor a variância, menos os valores variam da média. Somente registros que atendem às condições Scope e/ou opcionais FOR ou WHILE são incluídos no resultado.
**IN nWorkArea | cTableAlias**
Especifica a área de trabalho ou o alias de tabela afetado pelo comando CALCULATE. Use esta cláusula para especificar uma área de trabalho ou uma tabela fora da área de trabalho atual.

# Observações

Registros que contêm o valor nulo não são incluídos nas operações que o CALCULATE executa.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE orders  && Open Orders table
SET TALK ON
CLEAR
CALCULATE AVG(order_amt), MIN(order_amt), MAX(order_amt)
CALCULATE STD(order_amt), VAR(order_amt) TO gnStd, gnVar
```

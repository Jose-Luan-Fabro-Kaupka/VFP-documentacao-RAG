# Comando REPLACE (Visual FoxPro)

Atualiza registros de tabela.

```foxpro
REPLACE FieldName1 WITH eExpression1 [ADDITIVE]
   [, FieldName2 WITH eExpression2 [ADDITIVE]] ... [Scope]
   [FOR lExpression1] [WHILE lExpression2] [IN nWorkArea | cTableAlias]
   [NOOPTIMIZE]
```

#### Parâmetros
 **FieldName1 WITH eExpression1 [, FieldName2 WITH eExpression2 ... ]**
Especifica que os dados em FieldName1 sejam substituídos pelo valor da expressão eExpression1 ; que os dados em FieldName2 sejam substituídos pelo valor da expressão eExpression2 ; e assim por diante. Quando o valor da expressão é maior que a largura de um campo numérico, REPLACE força o valor a caber executando as seguintes etapas: Primeiro, REPLACE trunca casas decimais e arredonda a parte decimal restante do campo. Se o valor ainda não caber, REPLACE armazena o conteúdo do campo usando notação científica. Se o valor ainda não caber, REPLACE substitui o conteúdo do campo por asteriscos.
**ADDITIVE**
Anexa ao final dos campos memo as substituições em campos memo. ADDITIVE se aplica apenas a substituições em campos memo. Se você omitir ADDITIVE, o campo memo é sobrescrito com o valor da expressão.
**Scope**
Especifica um intervalo de registros a substituir. O escopo padrão de REPLACE é o registro atual (NEXT 1). Apenas os registros que estão dentro do intervalo são substituídos. As cláusulas de escopo são: ALL, NEXT nRecords , RECORD nRecordNumber , e REST. Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses .
**FOR lExpression1**
Especifica que os campos designados sejam substituídos apenas em registros para os quais lExpression1 avalia como verdadeiro (.T.). Incluir FOR torna possível substituir registros condicionalmente, filtrando aqueles que você não deseja substituir. A Otimização de Consulta Rushmore otimiza REPLACE FOR se lExpression1 for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access .
**WHILE lExpression2**
Especifica uma condição pela qual os campos são substituídos enquanto a expressão lógica lExpression2 avalia como verdadeiro (.T.).
**IN nWorkArea**
Especifica a área de trabalho da tabela na qual os registros são atualizados.
**IN cTableAlias**
Especifica o alias da tabela na qual os registros são atualizados. Se você omitir nWorkArea e cTableAlias , os registros são atualizados na tabela na área de trabalho atualmente selecionada.
**NOOPTIMIZE**
Impede a otimização Rushmore. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access .

# Observações

REPLACE substitui dados em um campo pelo valor em uma expressão. Campos em áreas de trabalho não selecionadas devem ser precedidos por seu alias.

> **Observação:** Se a cláusula IN for omitida, nenhuma substituição ocorre se o ponteiro de registro estiver no final do arquivo na área de trabalho atual e você especificar um campo em outra área de trabalho.

# Exemplo

O exemplo a seguir cria uma tabela com 10 registros. REPLACE é usado para colocar valores aleatórios em um campo. MIN( ) e MAX( ) exibem os valores máximo e mínimo na tabela.

```foxpro
CLOSE DATABASES
CREATE TABLE Random (cValue N(3))
FOR nItem = 1 TO 10  && Append 10 records,
   APPEND BLANK
   REPLACE cValue WITH 1 + 100 * RAND()  && Insert random values
ENDFOR
CLEAR
LIST  && Display the values
gnMaximum = 1  && Initialize minimum value
gnMinimum = 100  && Initialize maximum value
SCAN
   gnMinimum = MIN(gnMinimum, cValue)
   gnMaximum = MAX(gnMaximum, cValue)
ENDSCAN
? 'The minimum value is: ', gnMinimum  && Display minimum value
? 'The maximum value is: ', gnMaximum  && Display maximum value
```

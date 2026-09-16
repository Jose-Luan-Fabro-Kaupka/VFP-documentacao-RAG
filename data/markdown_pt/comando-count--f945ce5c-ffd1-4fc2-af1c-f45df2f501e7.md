# Comando COUNT

Conta registros de tabela.

```foxpro
COUNT   [Scope] [FOR lExpression1] [WHILE lExpression2]   [TO VarName]
   [NOOPTIMIZE]
```

#### Parâmetros
 **Scope**
Especifica um intervalo de registros a ser incluído na contagem. O escopo padrão para COUNT é ALL registros. As cláusulas de escopo são: ALL, NEXT nRecords, RECORD nRecordNumber e REST. Comandos que incluem Scope operam apenas na tabela na área de trabalho ativa. Para obter mais informações sobre cláusulas de escopo, consulte Scope Clauses.
**FOR lExpression1**
Especifica que apenas os registros que satisfazem a condição lógica lExpression1 são contados. Incluir FOR permite contar registros condicionalmente, filtrando registros indesejados. Rushmore Query Optimization otimizará uma consulta COUNT FOR se lExpression1 for uma expressão otimizável. Para melhor desempenho, use uma expressão otimizável na cláusula FOR. Para obter mais informações sobre expressões otimizáveis, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.
**WHILE lExpression2**
Especifica uma condição pela qual os registros são contados enquanto a expressão lógica lExpression2 avaliar para True (.T.).
**TO VarName**
Especifica a variável ou matriz na qual a contagem de registros é armazenada. Se a variável especificada não existir, o Visual FoxPro a cria.
**NOOPTIMIZE**
Desabilita a otimização Rushmore de COUNT. Para obter mais informações, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.

# Observações

COUNT conta os registros dentro de um escopo de registros para os quais as condições FOR ou WHILE são verdadeiras. Se SET TALK estiver ON, a contagem de registros é exibida.

Registros marcados para exclusão são incluídos na contagem se SET DELETE estiver OFF.

Para uma discussão sobre como valores nulos afetam COUNT, consulte o tópico Behavior of Null Values in Commands and Functions.

# Exemplo

O exemplo a seguir conta e exibe o número de clientes em Paris.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
COUNT FOR UPPER(city) = 'PARIS'
DISPLAY FIELDS company, contact FOR UPPER(city) = 'PARIS'
```

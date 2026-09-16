# Função EVALUATE( )

Avalia uma expressão de caracteres e retorna o resultado.

```foxpro
EVALUATE(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão a ser avaliada. cExpression pode ser uma cadeia de caracteres literal ou uma expressão Visual FoxPro válida, variável, elemento de matriz ou campo de qualquer tipo de dados, entre aspas. cExpression não pode exceder 255 caracteres. Sempre que possível, use EVALUATE( ) ou uma expressão de nome para substituir a substituição de macro usando o & Command . EVALUATE e expressões de nome são executados mais rapidamente que substituição de macro.

# Valor de retorno

Character, Numeric, Currency, Date, DateTime, Logical ou Memo

# Observações

EVALUATE( ) é semelhante a TYPE( ), mas retorna o resultado de uma expressão em vez do tipo da expressão. Uma expressão contendo EVALUATE( ) não pode ser otimizada pela Rushmore Query Optimization.

Incluir a função EVALUATE( ) na cláusula WHERE de uma consulta SQL pode retornar dados incorretos.

# Exemplo

O exemplo a seguir usa a função EVALUATE() para avaliar uma expressão matemática armazenada em uma variável de caracteres.

```foxpro
cMathFunc="INT(4.33)"
nResult=EVALUATE(cMathFunc)
?nResult
```

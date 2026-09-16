# Função VARTYPE( )

Retorna o tipo de dados de uma expressão.

> **Observação:** VARTYPE( ) é semelhante à função TYPE( ), mas VARTYPE( ) é mais rápida e não requer aspas para envolver a expressão para a qual o tipo de dados é retornado.

```foxpro
VARTYPE(eExpression [, lNullDataType])
```

#### Parâmetros
 **eExpression**
Especifica a expressão para a qual o tipo de dados é retornado. VARTYPE( ) retorna um único caractere indicando o tipo de dados da expressão. A tabela a seguir lista os caracteres que VARTYPE( ) retorna para cada tipo de dados. Valor de retorno Tipo de dados C Character, Memo, Varchar, Varchar (Binary) D Date G General L Logical N Numeric, Float, Double ou Integer O Object Q Blob, Varbinary T DateTime U Unknown ou variável não existe X Null Y Currency

> **Observação:** Se eExpression for uma matriz, o primeiro elemento da matriz é avaliado.
 **lNullDataType**
Especifica se VARTYPE( ) retorna o tipo de dados quando eExpression contém o valor nulo. A tabela a seguir lista os valores de lNullDataType. lNullDataType Descrição True (.T.) Retorna o tipo de dados de eExpression. False (.F.) ou omitido Retorna 'X' para indicar que eExpression contém um valor nulo.

# Valor de retorno

Character. VARTYPE( ) retorna um caractere representando o tipo de dados da expressão especificada.

# Função LTRIM( )

Remove todos os espaços à esquerda ou caracteres de análise da expressão de caracteres especificada, ou todos os bytes zero (0) à esquerda da expressão binária especificada.

```foxpro
LTRIM(Expression [, nFlags] [, cParseChar [, cParseChar2 [, ...]]])
```

#### Parâmetros
 **Expression**
Especifica uma expressão do tipo Character ou Varbinary da qual remover espaços à esquerda ou bytes 0, respectivamente.
**nFlags**
Especifica se o corte é sensível a maiúsculas e minúsculas quando uma ou mais cadeias de análise (cParseChar, cParseChar2, …) estão incluídas. O corte é sensível a maiúsculas e minúsculas se nFlags for zero ou for omitido. O corte não é sensível a maiúsculas e minúsculas se nFlags for 1.
**cParseChar [, cParseChar2 [, ...]]**
Especifica uma ou mais cadeias de caracteres que são removidas do início de cExpression. Se cParseChar não estiver incluído, os espaços à esquerda ou bytes 0 são removidos de Expression. Observação O número máximo de cadeias permitidas em cParseChar é 23.

# Valor de retorno

Character ou Varbinary. LTRIM( ) retorna a expressão especificada sem espaços à esquerda ou caracteres de análise, ou bytes 0.

# Observações

LTRIM( ) é particularmente útil para remover os espaços à esquerda que são inseridos quando você usa a função STR( ) para converter um valor Numeric em uma cadeia de caracteres Character.

# Exemplo

```foxpro
STORE 'Redmond' TO gcCity
STORE '   Washington' TO gcState
CLEAR
? gcCity, gcState  && Displays Redmond   Washington
? gcCity, LTRIM(gcState)  && Displays Redmond Washington
```

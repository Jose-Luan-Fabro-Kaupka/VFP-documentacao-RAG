# Função TRIM( )

Remove todos os espaços à direita ou caracteres de análise da expressão de caracteres especificada, ou todos os bytes zero (0) à direita da expressão binária especificada.

```foxpro
TRIM(cExpression [, nFlags] [, cParseChar [, cParseChar2 [, ...]]])
```

#### Parâmetros
 **cExpression**
Especifica uma expressão do tipo Character ou Varbinary da qual remover todos os espaços à direita ou bytes 0, respectivamente.
**nFlags**
Especifica se o corte é sensível a maiúsculas e minúsculas quando um ou mais caracteres de análise ( cParseChar , cParseChar2 , … são incluídos. O corte é sensível a maiúsculas e minúsculas se nFlags for zero ou for omitido. O corte não diferencia maiúsculas de minúsculas se nFlags for 1.
**cParseChar [, cParseChar2 [, ...]]**
Especifica uma ou mais cadeias de caracteres que são removidas do final de cExpression. Se cParseChar não for incluído, espaços à direita ou bytes 0 são removidos de Expression. Observação O número máximo de cadeias de caracteres permitido em cParseChar é 23.

# Valor de retorno

Character ou Varbinary. TRIM( ) retorna a expressão especificada sem espaços à direita ou caracteres de análise, ou bytes 0.

# Observações

TRIM( ) é idêntico a RTRIM( ).

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
? 'The contact for '+ TRIM(company) + ' is ' + contact
```

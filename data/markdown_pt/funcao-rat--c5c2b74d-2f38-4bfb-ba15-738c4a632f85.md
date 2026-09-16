# Função RAT( )

Retorna a posição numérica da última ocorrência (mais à direita) de uma cadeia de caracteres dentro de outra cadeia de caracteres.

```foxpro
RAT(cSearchExpression, cExpressionSearched [, nOccurrence])
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caracteres que RAT( ) procura em cExpressionSearched. A expressão de caracteres pode referenciar um campo memo de qualquer tamanho.
**cExpressionSearched**
Especifica a expressão de caracteres que RAT( ) pesquisa. A expressão de caracteres pode referenciar um campo memo de qualquer tamanho.
**nOccurrence**
Especifica qual ocorrência, começando pela direita e movendo-se para a esquerda, de cSearchExpression RAT( ) procura em cExpressionSearched. Por padrão, RAT( ) procura a última ocorrência de cSearchExpression ( nOccurrence = 1). Se nOccurrence for 2, RAT( ) procura a penúltima ocorrência, e assim por diante.

# Valor de retorno

Numérico

# Observações

RAT( ), o inverso da função AT( ), pesquisa a expressão de caracteres em cExpressionSearched começando pela direita e movendo-se para a esquerda, procurando a última ocorrência da cadeia de caracteres especificada em cSearchExpression.

RAT( ) retorna um inteiro indicando a posição do primeiro caractere em cSearchExpression em cExpressionSearched. RAT( ) retorna 0 se cSearchExpression não for encontrado em cExpressionSearched, ou se nOccurrence for maior que o número de vezes que cSearchExpression ocorre em cExpressionSearched.

A pesquisa realizada por RAT( ) diferencia maiúsculas de minúsculas.

# Exemplo

```foxpro
STORE 'abracadabra' TO string
STORE 'a' TO find_str
CLEAR
? RAT(find_str,string)  && Displays 11
? RAT(find_str,string,3)  && Displays 6
```

# Função AT( )

Pesquisa uma expressão de caracteres pela ocorrência de outra expressão de caracteres.

> **Observação:** A pesquisa realizada por AT( ) diferencia maiúsculas de minúsculas. Para realizar uma pesquisa que não diferencia maiúsculas de minúsculas, use ATC( ). Para obter mais informações, consulte a função ATC( ).

```foxpro
AT(cSearchExpression, cExpressionSearched [, nOccurrence])
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caracteres a ser pesquisada em cExpressionSearched.
**cExpressionSearched**
Especifica a expressão de caracteres em que pesquisar cSearchExpression. Tanto cSearchExpression quanto cExpressionSearched podem ser campos memo de qualquer tamanho.
**nOccurrence**
Especifica qual ocorrência — primeira, segunda, terceira e assim por diante — de cSearchExpression pesquisar em cExpressionSearched. Por padrão, AT( ) pesquisa a primeira ocorrência de cSearchExpression (nOccurrence = 1).

# Valor de retorno

Numérico. AT( ) retorna um inteiro indicando a posição do primeiro caractere de uma expressão de caracteres ou campo memo dentro de outra expressão de caracteres ou campo memo, começando pelo caractere mais à esquerda. Se a expressão ou o campo não for encontrado, ou se nOccurrence for maior que o número de vezes que cSearchExpression ocorre em cExpressionSearched, AT( ) retorna 0.

# Exemplo

```foxpro
STORE 'Now is the time for all good men' TO gcString
STORE 'is the' TO gcFindString
CLEAR
? AT(gcFindString,gcString)  && Displays 5
STORE 'IS' TO gcFindString
? AT(gcFindString,gcString)  && Displays 0, case-sensitive
```

# Função ATCC( )

Retorna a posição numérica inicial da primeira ocorrência de uma expressão de caractere ou campo memo dentro de outra expressão de caractere ou campo memo, sem considerar a diferença de maiúsculas e minúsculas dessas duas expressões.

```foxpro
ATCC(cSearchExpression, cExpressionSearched [, nOccurrence])
```

#### Parâmetros
 **cSearchExpression**
Especifica a expressão de caractere que ATCC( ) procura em cExpressionSearched.
**cExpressionSearched**
Especifica a expressão de caractere que cSearchExpression procura. Tanto cSearchExpression quanto cExpressionSearched podem ser campos memo de qualquer tamanho.
**nOccurrence**
Especifica qual ocorrência (primeira, segunda, terceira e assim por diante) de cSearchExpression é procurada em cExpressionSearched. Por padrão, ATCC( ) procura a primeira ocorrência de cSearchExpression (nOccurrence = 1). Incluir nOccurrence permite procurar ocorrências adicionais de cSearchExpression em cExpressionSearched.

# Valor de retorno

Numérico

# Observações

ATCC( ) foi projetada para expressões que contêm caracteres de byte duplo. Se a expressão contém apenas caracteres de byte único, ATCC( ) é equivalente a ATC( ).

ATCC( ) procura a segunda expressão de caractere pela ocorrência da primeira expressão de caractere, sem considerar o caso (maiúsculas ou minúsculas) dos caracteres em qualquer expressão. Use AT_C( ) para realizar uma pesquisa que diferencia maiúsculas de minúsculas.

ATCC( ) retorna um inteiro correspondente à posição onde o primeiro caractere da expressão de caractere é encontrado. Se a expressão de caractere não for encontrada, ATCC( ) retorna 0.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.

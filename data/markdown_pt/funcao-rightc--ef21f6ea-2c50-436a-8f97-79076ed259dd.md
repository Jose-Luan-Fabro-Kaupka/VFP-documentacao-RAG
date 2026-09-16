# Função RIGHTC( )

Retorna o número especificado de caracteres mais à direita de uma cadeia de caracteres.

```foxpro
RIGHTC(cExpression, nCharacters)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere cujos caracteres mais à direita são retornados.
**nCharacters**
Especifica o número de caracteres retornados da expressão de caractere. RIGHTC( ) retorna a expressão de caractere inteira se nCharacters for maior que o comprimento de cExpression. RIGHTC( ) retorna uma cadeia de caracteres vazia se nCharacters for negativo ou 0.

# Valor de retorno

Caractere

# Observações

RIGHTC( ) foi projetada para expressões que contêm caracteres de byte duplo. Se a expressão contém apenas caracteres de byte único, RIGHTC( ) é equivalente a RIGHT( ).

Os caracteres são retornados começando pelo último caractere à direita e continuando por nCharacters.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.

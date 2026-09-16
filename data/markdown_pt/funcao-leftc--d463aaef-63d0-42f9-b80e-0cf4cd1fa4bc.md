# Função LEFTC( )

Retorna um número especificado de caracteres de uma expressão de caractere, começando com o caractere mais à esquerda.

```foxpro
LEFTC(cExpression, nExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere da qual LEFTC( ) retorna caracteres.
**nExpression**
Especifica o número de caracteres retornados da expressão de caractere. Se nExpression for maior que o comprimento de cExpression, toda a expressão de caractere é retornada. A cadeia de caracteres vazia é retornada se nExpression for negativo ou 0.

# Valor de retorno

Character

# Observações

LEFTC( ) foi projetada para expressões que contêm caracteres de byte duplo. Se a expressão contém apenas caracteres de byte único, LEFTC( ) é equivalente a LEFT( ).

LEFTC( ) retorna um número especificado de caracteres de uma expressão de caractere que contém qualquer combinação de caracteres de byte único e duplo.

LEFTC( ) é idêntica a SUBSTRC( ) com posição inicial 1.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.

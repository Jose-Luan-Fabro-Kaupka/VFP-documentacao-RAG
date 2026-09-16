# Função ISLEADBYTE( )

Retorna true (.T.) se o primeiro byte do primeiro caractere em uma expressão de caractere for o byte principal de um caractere de duplo byte.

```foxpro
ISLEADBYTE(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere que ISLEADBYTE( ) avalia. Quaisquer bytes após o primeiro byte no primeiro caractere em cExpression são ignorados.

# Valor de retorno

Logical

# Observações

ISLEADBYTE( ) retorna true (.T.) se o primeiro byte do primeiro caractere em uma expressão de caractere for o byte principal em um caractere de duplo byte. Se ISLEADBYTE( ) retornar false (.F.), o caractere testado é um caractere de byte único.

Esta função é útil para manipular conjuntos de caracteres de duplo byte para idiomas como Hiragana e Katakana.

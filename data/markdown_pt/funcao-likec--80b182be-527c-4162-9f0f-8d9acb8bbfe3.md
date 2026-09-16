# Função LIKEC( )

Determina se uma expressão de caractere corresponde a outra expressão de caractere.

```foxpro
LIKEC(cExpression1, cExpression2)
```

#### Parâmetros
 **cExpression1**
Especifica a expressão de caractere que LIKEC( ) compara com cExpression2 . cExpression1 pode conter curingas como * e ?. Um ponto de interrogação (?) corresponde a qualquer caractere único em cExpression2 e um asterisco (*) corresponde a qualquer número de caracteres. Você pode misturar qualquer número de curingas em qualquer combinação em cExpression1 .
**cExpression2**
Especifica a expressão de caractere que LIKEC( ) compara com cExpression1 . cExpression2 deve corresponder a cExpression1 caractere por caractere para que LIKE( ) retorne verdadeiro (.T.).

# Valor de retorno

Logical

# Observações

LIKEC( ) é projetada para expressões que contêm caracteres de byte duplo. Se a expressão contém apenas caracteres de byte único, LIKEC( ) é equivalente a LIKE( ).

LIKEC( ) determina se uma expressão de caractere corresponde a outra expressão de caractere. LIKEC( ) retorna verdadeiro (.T.) se cExpression1 corresponder a cExpression2; caso contrário, retorna falso (.F.).

SET COMPATIBLE determina como LIKEC( ) compara espaços em branco em cExpression1 e cExpression2. Se SET COMPATIBLE estiver definido como ON ou DB4, todos os espaços em branco finais são removidos de cExpression1 e cExpression2 antes de serem comparados. Se SET COMPATIBLE estiver definido como OFF ou FOXPLUS, quaisquer espaços em branco finais em cExpression1 e cExpression2 são usados na comparação.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.

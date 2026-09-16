# Função CHRTRAN( )

Substitui cada caractere em uma expressão de caracteres que corresponde a um caractere em uma segunda expressão de caracteres pelo caractere correspondente em uma terceira expressão de caracteres.

```foxpro
CHRTRAN(cSearchedExpression, cSearchExpression, cReplacementExpression)
```

#### Parâmetros
 **cSearchedExpression**
Especifica a expressão na qual CHRTRAN( ) substitui caracteres.
**cSearchExpression**
Especifica a expressão que contém os caracteres que CHRTRAN( ) procura em cSearchedExpression .
**cReplacementExpression**
Especifica a expressão que contém os caracteres de substituição. Se um caractere em cSearchExpression for encontrado em cSearchedExpression , o caractere em cSearchedExpression é substituído por um caractere de cReplacementExpression que está na mesma posição em cReplacementExpression que o respectivo caractere em cSearchExpression . Se cReplacementExpression tiver menos caracteres que cSearchExpression , os caracteres adicionais em cSearchExpression são excluídos de cSearchedExpression . Se cReplacementExpression tiver mais caracteres que cSearchExpression , os caracteres adicionais em cReplacementExpression são ignorados.

# Valor de retorno

Character

# Observações

CHRTRAN( ) traduz a expressão de caracteres cSearchedExpression usando as expressões de tradução cSearchExpression e cReplacementExpression e retorna a cadeia de caracteres resultante.

# Exemplo

```foxpro
? CHRTRAN('ABCDEF', 'ACE', 'XYZ')  && Displays XBYDZF
? CHRTRAN('ABCD', 'ABC', 'YZ')  && Displays YZD
? CHRTRAN('ABCDEF', 'ACE', 'XYZQRST')  && Displays XBYDZF
```

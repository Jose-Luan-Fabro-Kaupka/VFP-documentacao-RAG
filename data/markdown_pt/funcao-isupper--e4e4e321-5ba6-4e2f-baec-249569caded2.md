# Função ISUPPER( )

Determina se o primeiro caractere em uma expressão de caracteres é um caractere alfabético maiúsculo.

```foxpro
ISUPPER(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que ISUPPER( ) avalia. Quaisquer caracteres após o primeiro caractere em cExpression são ignorados.

# Valor de retorno

Logical

# Observações

ISUPPER( ) retorna verdadeiro (.T.) se o primeiro caractere em uma expressão de caracteres for um caractere alfabético maiúsculo; caso contrário, ISUPPER( ) retorna falso (.F.).

# Exemplo

```foxpro
? ISUPPER('Redmond')  && Displays .T.
? ISUPPER('redmond')  && Displays .F.
```

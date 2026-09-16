# Função ISDIGIT( )

Determina se o caractere mais à esquerda da expressão de caracteres especificada é um dígito (0 a 9).

```foxpro
ISDIGIT(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que ISDIGIT( ) testa. Quaisquer caracteres após o primeiro caractere em cExpression são ignorados.

# Valor de retorno

Lógico

# Observações

ISDIGIT( ) retorna true (.T.) se o caractere mais à esquerda da expressão de caracteres especificada for um dígito (0 a 9); caso contrário, ISDIGIT( ) retorna false (.F.).

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE orders  && Open Orders table
CLEAR
DISPLAY cust_id
? ISDIGIT(cust_id)  && Displays .F.
DISPLAY order_dsc
? ISDIGIT(ALLTRIM(STR(order_dsc)))  && Displays .T.
```

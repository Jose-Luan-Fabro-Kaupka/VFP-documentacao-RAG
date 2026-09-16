# Função ISALPHA( )

Determina se o caractere mais à esquerda em uma expressão de caracteres é alfabético.

```foxpro
ISALPHA(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que ISALPHA( ) avalia. Quaisquer caracteres após o primeiro caractere em cExpression são ignorados.

# Valor de retorno

Lógico

# Observações

ISALPHA( ) retorna true (.T.) se o caractere mais à esquerda na expressão de caracteres especificada for um caractere alfabético; caso contrário, ISALPHA( ) retorna false (.F.).

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open customer table
CLEAR
DISPLAY contact
? ISALPHA(contact)  && Displays .T.
DISPLAY maxordamt
? ISALPHA(cust_id)  && Displays .F.
```

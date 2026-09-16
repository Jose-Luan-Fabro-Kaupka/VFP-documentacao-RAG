# Função UPPER( )

Retorna a expressão de caractere especificada em maiúsculas.

```foxpro
UPPER(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caractere que UPPER( ) converte para maiúsculas.

# Valor de retorno

Caractere

# Observações

Cada letra minúscula (a – z) na expressão de caractere é convertida para maiúscula (A – Z) na cadeia de caracteres retornada. Isso é verdade para caracteres de alto ASCII também, mesmo se a fonte atual não os exibir como caracteres acentuados minúsculos.

# Exemplo

```foxpro
CLEAR
? UPPER('abcdefgh')  && Displays ABCDEFGH
```

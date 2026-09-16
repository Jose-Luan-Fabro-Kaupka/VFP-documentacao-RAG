# Função LOWER( )

Retorna uma expressão de caracteres especificada em letras minúsculas.

```foxpro
LOWER(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que LOWER( ) converte.

# Valor de retorno

Character

# Observações

LOWER( ) converte todas as letras maiúsculas (A – Z) na expressão de caracteres para minúsculas (a – z). Todos os outros caracteres na expressão de caracteres permanecem inalterados.

# Exemplo

```foxpro
STORE 'FOX' TO gcName
CLEAR
? LOWER(gcName)  && Displays fox
```

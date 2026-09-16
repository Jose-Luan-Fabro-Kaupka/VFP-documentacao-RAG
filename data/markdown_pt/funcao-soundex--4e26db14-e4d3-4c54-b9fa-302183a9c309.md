# Função SOUNDEX( )

Retorna uma representação fonética da expressão de caracteres especificada.

```foxpro
SOUNDEX(cExpression)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres que SOUNDEX( ) avalia.

# Valor de retorno

Character

# Observações

SOUNDEX( ) retorna uma cadeia de caracteres de quatro caracteres. Ao comparar os resultados que SOUNDEX( ) retorna para duas expressões de caracteres, você pode determinar se as duas expressões são foneticamente semelhantes, indicando que soam parecidas. Isso pode ser útil ao pesquisar registros duplicados em uma tabela.

SOUNDEX( ) não diferencia maiúsculas de minúsculas e geralmente desconsidera vogais.

# Exemplo

```foxpro
CLEAR
? SOUNDEX('Smith') = SOUNDEX('Smyth')  && Displays .T.
? SOUNDEX('Computer')  && Displays C513
```

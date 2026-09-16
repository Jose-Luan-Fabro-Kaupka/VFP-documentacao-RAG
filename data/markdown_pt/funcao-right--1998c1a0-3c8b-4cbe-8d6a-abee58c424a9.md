# Função RIGHT( )

Retorna o número especificado de caracteres mais à direita de uma cadeia de caracteres.

```foxpro
RIGHT(cExpression, nCharacters)
```

#### Parâmetros
 **cExpression**
Especifica a expressão de caracteres cujos caracteres mais à direita são retornados.
**nCharacters**
Especifica o número de caracteres retornados da expressão de caracteres. RIGHT( ) retorna toda a expressão de caracteres se nCharacters for maior que o comprimento de cExpression. RIGHT( ) retorna uma cadeia de caracteres vazia se nCharacters for negativo ou 0.

# Valor de retorno

Character

# Observações

Os caracteres são retornados começando pelo último caractere à direita e continuando pelo número especificado de caracteres.

# Exemplo

```foxpro
CLEAR
? RIGHT('Redmond, WA', 2)  && Displays WA
```

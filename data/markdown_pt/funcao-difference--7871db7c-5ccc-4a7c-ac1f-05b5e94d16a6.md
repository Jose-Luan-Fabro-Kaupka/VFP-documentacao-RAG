# Função DIFFERENCE( )

Retorna um inteiro, de 0 a 4, que representa a diferença fonética relativa entre duas expressões de caractere.

```foxpro
DIFFERENCE(cExpression1, cExpression2)
```

#### Parâmetros
 **cExpression1 , cExpression2**
Especifica as expressões de caractere que DIFFERENCE( ) compara.

# Valor de retorno

Numeric

# Observações

DIFFERENCE( ) é útil para pesquisar tabelas quando a grafia exata de uma entrada não é conhecida.

Quanto mais semelhantes as duas expressões estiverem grafadas, maior será o número que DIFFERENCE( ) retorna. Se as expressões de caractere estiverem grafadas de forma muito semelhante, DIFFERENCE( ) retorna 4. Para duas expressões de caractere com pouco em comum foneticamente, DIFFERENCE( ) retorna 0.

# Exemplo

```foxpro
STORE 'Smith' TO gcName1
STORE 'Smythe'  TO gcName2
STORE 'Smittie' TO gcName3
STORE '' TO gcName4
CLEAR
? DIFFERENCE(gcName1, gcName2)  && Displays 4
? DIFFERENCE(gcName1, gcName3)  && Displays 4
? DIFFERENCE(gcName1, gcName4)  && Displays 1
```

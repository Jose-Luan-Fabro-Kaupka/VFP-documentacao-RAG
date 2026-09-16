# Função YEAR( )

Retorna o ano da expressão de data ou datetime especificada.

```foxpro
YEAR(dExpression | tExpression)
```

#### Parâmetros
 **dExpression**
Especifica uma expressão de data da qual YEAR( ) retorna o ano. dExpression pode ser uma função que retorna uma data ou uma variável de memória, elemento de matriz ou campo do tipo Date. Também pode ser uma cadeia de data literal, como {^1998-06-06}.
**tExpression**
Especifica uma expressão datetime da qual YEAR( ) retorna o ano.

# Valor de retorno

Numeric

# Observações

YEAR( ) sempre retorna o ano com o século. A configuração CENTURY (ON ou OFF) não afeta o valor retornado.

# Exemplo

```foxpro
CLEAR
? YEAR(DATE())
```

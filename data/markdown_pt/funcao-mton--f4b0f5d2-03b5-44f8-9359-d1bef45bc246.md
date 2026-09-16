# Função MTON( )

Retorna um valor Numeric de uma expressão Currency.

```foxpro
MTON(mExpression)
```

#### Parâmetros
 **mExpression**
Especifica uma expressão Currency cujo valor MTON( ) retorna. mExpression deve ser avaliada como um valor Currency válido ou o Visual FoxPro gera um erro. Valores Currency são criados colocando um prefixo de cifrão ($) imediatamente antes de um valor Numeric.

# Valor de retorno

Tipo Numeric. MTON( ) retorna um valor do tipo Numeric com quatro casas decimais.

# Exemplo

O exemplo a seguir cria uma variável de tipo moeda chamada `gyMoney`. TYPE( ) exibe Y, indicando que a variável é do tipo moeda. MTON( ) é usada para converter a variável para um tipo numérico, e TYPE( ) agora exibe N, indicando que a variável é do tipo numérico após a conversão.

```foxpro
STORE $24.95 TO gyMoney  && Creates a currency type memory variable
CLEAR
? "gyMoney is type: "
?? TYPE('gyMoney')  && Displays Y, currency type value
gyMoney = MTON(gyMoney)     &&  Converts gyMoney to a numeric value
? "gyMoney is now type: "
?? TYPE('gyMoney')  && Displays N, numeric type value
```

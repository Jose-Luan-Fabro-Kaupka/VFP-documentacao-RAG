# Função TTOD( )

Retorna um valor Date a partir de uma expressão DateTime.

```foxpro
TTOD(tExpression)
```

#### Parâmetros
 **tExpression**
Especifica uma expressão de data e hora da qual TTOD( ) retorna um valor Date. tExpression deve ser avaliado como um DateTime válido. Se tExpression contiver apenas uma hora, o Visual FoxPro adiciona a data padrão de 12/30/1899 a tExpression e retorna essa data padrão.

# Valor de retorno

Date

# Exemplo

O exemplo a seguir cria uma variável do tipo Datetime chamada `gtDtime`. TYPE( ) exibe T, indicando que a variável é do tipo Datetime. TTOD( ) é usado para converter a variável para um tipo date, e TYPE( ) agora exibe D, indicando que a variável é do tipo date após a conversão.

```foxpro
STORE DATETIME() TO gtDtime  && Creates a Datetime type memory variable
CLEAR
? "gtDtime is type: "
?? TYPE('gtDtime')  && Displays T, Datetime type value
gtDtime = TTOD(gtDtime)     &&  Converts gtDtime to a date value
? "gtDtime is now type: "
?? TYPE('gtDtime')  && Displays D, character type value
```

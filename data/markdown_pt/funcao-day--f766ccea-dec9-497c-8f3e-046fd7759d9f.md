# Função DAY( )

Retorna o dia numérico do mês para uma expressão Date ou DateTime fornecida.

```foxpro
DAY(dExpression | tExpression)
```

#### Parâmetros
 **dExpression**
Especifica uma data da qual DAY( ) retorna um dia do mês. dExpression pode ser um literal de data, uma variável do tipo Date, um elemento de matriz ou um campo de data.
**tExpression**
Especifica uma data ou hora da qual DAY( ) retorna um dia do mês. dExpression pode ser um literal DateTime, uma variável do tipo DateTime, um elemento de matriz ou um campo DateTime.

# Valor de retorno

Numérico

# Observações

DAY( ) retorna um número de 1 a 31.

# Exemplo

```foxpro
STORE {^1998-03-05} TO gdBDate
CLEAR
? CDOW(gdBDate)  && Displays Thursday
? DAY(gdBDate) && Displays 5
? 'That date is ', CMONTH(gdBDate), STR(DAY(gdBDate),2)
```

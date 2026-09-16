# Função CMONTH( )

Retorna o nome do mês de uma expressão de data ou DateTime fornecida.

```foxpro
CMONTH(dExpression | tExpression)
```

#### Parâmetros
 **dExpression**
Especifica a expressão de data da qual CMONTH( ) retorna o nome do mês.
**tExpression**
Especifica a expressão DateTime da qual CMONTH( ) retorna o nome do mês.

# Valor de retorno

Character

# Observações

CMONTH( ) retorna o nome do mês como uma cadeia de caracteres em formato de substantivo próprio baseado no arquivo de recursos atual que você está usando e não na localidade do Windows. Para mais informações, consulte Gerenciando arquivos em uma aplicação internacional.

# Exemplo

```foxpro
? CMONTH(DATE())
STORE {^1998-02-16} TO gdDueDate
? 'Your payment was due in ', CMONTH(gdDueDate)
STORE gdDueDate+60 TO gdFinalDate
? 'You must pay by ', CMONTH(gdFinalDate)
```

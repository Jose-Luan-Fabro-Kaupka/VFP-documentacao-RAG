# Função PV( )

Retorna o valor presente de um investimento.

```foxpro
PV(nPayment, nInterestRate, nTotalPayments)
```

#### Parâmetros
 **nPayment**
Especifica o valor do pagamento periódico. nPayment pode avaliar para um número positivo ou negativo. PV( ) assume que os pagamentos são feitos no final de cada período.
**nInterestRate**
Especifica a taxa de juros periódica. Se a taxa de juros de um investimento é anual e os pagamentos são feitos mensalmente, divida a taxa de juros anual por 12.
**nTotalPayments**
Especifica o número total de pagamentos.

# Valor de retorno

Numeric

# Observações

PV( ) calcula o valor presente de um investimento baseado em uma série de pagamentos periódicos iguais a uma taxa de juros periódica constante.

# Exemplo

```foxpro
STORE 500 to gnPayment  && Periodic payments made monthly
STORE .075/12 TO gnInterest     && 7.5% annual interest rate
STORE 48 TO gnPeriods  && Four years (48 months)
CLEAR
? PV(gnPayment, gnInterest, gnPeriods)  && Displays 20679.19
```

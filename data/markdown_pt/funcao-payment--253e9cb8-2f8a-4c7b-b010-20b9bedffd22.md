# Função PAYMENT( )

Retorna o valor de cada pagamento periódico de um empréstimo com juros fixos.

```foxpro
PAYMENT(nPrincipal, nInterestRate, nPayments)
```

#### Parâmetros
 **nPrincipal**
Especifica o principal inicial do empréstimo.
**nInterestRate**
Especifica a taxa de juros fixa por período. Se os pagamentos do empréstimo forem mensais, mas a taxa de juros for anual, divida a taxa anual por 12.
**nPayments**
Especifica o número total de pagamentos do empréstimo.

# Valor de retorno

Numeric

# Observações

PAYMENT( ) pressupõe uma taxa de juros periódica constante e que os pagamentos sejam feitos ao final de cada período.

# Exemplo

```foxpro
STORE 100000 to gnPrincipal     && $100,000 beginning principal
STORE .105/12 TO gnInterest  && 10.5% annual interest rate
STORE (20*12) TO gnPayments     && 20 years of monthly payments
CLEAR
? PAYMENT(gnPrincipal, gnInterest, gnPayments)  && Displays 998.38
```

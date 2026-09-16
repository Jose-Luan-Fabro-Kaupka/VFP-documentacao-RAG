# Variável de sistema _CALCVALUE

Contém o valor numérico que a Calculadora exibe.

```foxpro
_CALCVALUE = nCalculatorDisplayValue
```

#### Parâmetros
 **nCalculatorDisplayValue**
Especifica o valor numérico que a Calculadora exibe.

# Observações

Você pode retornar o resultado de um cálculo a um programa ou pode colocar um valor específico no display da Calculadora antes de usá-la.

Para inicializar o display da Calculadora, armazene um valor numérico em _CALCVALUE com STORE ou o operador de atribuição =. Quando você usa a Calculadora, ela exibe o valor que você especificou.

# Exemplo

No exemplo a seguir, o valor numérico 1234 é armazenado em _CALCVALUE. A Calculadora então exibe o valor 1234.

```foxpro
STORE 1234 TO _CALCVALUE
ACTIVATE WINDOW calculator
```

# Variável de sistema _CALCMEM

Contém o valor numérico que o Microsoft Visual FoxPro armazena na memória da Calculadora.

```foxpro
_CALCMEM = nCalculatorValue
```

#### Parâmetros
 **nCalculatorValue**
Especifica o valor numérico que _CALCMEM armazena na memória.

# Observações

Você pode salvar o resultado de um cálculo na memória da Calculadora e retornar o resultado a um programa, ou pode colocar um valor específico na memória da Calculadora antes de usá-la.

Para inicializar a memória da Calculadora, armazene um valor numérico em _CALCMEM com STORE ou o operador de atribuição =. Quando você usa a Calculadora, sua memória contém o valor que você especificou.

# Exemplo

O exemplo de programa a seguir armazena a constante numérica 1234 em _CALCMEM. O programa então exibe a Calculadora e envia a letra R ao teclado. A tecla R exibe o valor armazenado na memória da Calculadora.

```foxpro
STORE 1234 TO _CALCMEM
ACTIVATE WINDOW calculator
CLEAR TYPEAHEAD
KEYBOARD CHR(82)
```

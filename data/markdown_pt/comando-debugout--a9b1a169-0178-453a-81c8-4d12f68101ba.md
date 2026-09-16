# Comando DEBUGOUT

Direciona o resultado de uma ou mais expressões para a janela Debug Output.

```foxpro
DEBUGOUT eExpression1 [, eExpression2] ...
```

#### Parâmetros
 **eExpression1 [, eExpression2 ] ...**
Especifica uma ou mais expressões para avaliar e exibir na janela Debug Output. Você pode especificar várias expressões de tipos diferentes. Se a expressão que você especificar for um objeto ou referência de objeto, o Visual FoxPro converte automaticamente para a cadeia de caracteres "(Object)", para fornecer o equivalente de caractere. No exemplo a seguir, a variável de sistema _VFP é retornada como "(Object)" e passada para DEBUGOUT : DEBUGOUT 123, _VFP, "Hello"

# Observações

Use DEBUGOUT para identificar quando um procedimento ou função é executado. Por exemplo, você pode colocar DEBUGOUT no início de um procedimento para exibir uma mensagem na janela Debug Output, indicando que o procedimento começou a ser executado.

> **Observação:** Você pode abreviar DEBUGOUT para um mínimo de apenas seis caracteres, o que o distingue do comando DEBUG.

Quando você passa várias expressões, uma vírgula aparece como um espaço. Uma quebra de linha de retorno de carro (CRLF) é adicionada no final da linha.

DEBUGOUT é ignorado em aplicações que você distribui.

# Exemplo

O exemplo a seguir ilustra como DEBUGOUT pode aceitar várias expressões:

```foxpro
DEBUGOUT "test", 1, 2, 3, 4, DATE(), _VFP
```

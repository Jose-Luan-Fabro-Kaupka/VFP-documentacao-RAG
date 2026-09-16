# Criando expressões lógicas

Expressões lógicas avaliam para verdadeiro ou falso, que são representados pelos valores .T. e .F. no Visual FoxPro. Componha expressões lógicas combinando operadores lógicos com os seguintes elementos do Visual FoxPro:
 - Campos do tipo lógico.
- Funções que retornam valores lógicos.
- Variáveis e elementos de array que contêm valores lógicos.
- Qualquer expressão que avalie para um valor lógico.

O Visual FoxPro avalia expressões lógicas da esquerda para a direita e somente pelo tempo necessário. No exemplo a seguir, o operador AND é usado para criar uma expressão lógica. Se qualquer um dos valores na expressão for falso (.F.), toda a expressão é falsa. Quando o Visual FoxPro encontra o primeiro falso lógico (.F.), ele não avalia o restante da expressão.

```foxpro
.T. AND .T. AND .F. AND .T. AND .T. AND .T.
```

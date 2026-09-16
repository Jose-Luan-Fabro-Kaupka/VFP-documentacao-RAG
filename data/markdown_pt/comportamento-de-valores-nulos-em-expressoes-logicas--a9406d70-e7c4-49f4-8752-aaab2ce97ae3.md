# Comportamento de valores nulos em expressões lógicas

Valores nulos persistem através de expressões lógicas na maioria dos casos. A tabela a seguir descreve o comportamento de valores nulos em expressões lógicas.

| Expressão lógica | Resultado se x =TRUE | Resultado se x =FALSE | Resultado se x =.NULL. |
| --- | --- | --- | --- |
| x AND .NULL. | .NULL. | FALSE | .NULL. |
| x OR .NULL. | TRUE | .NULL. | .NULL. |
| NOT x | FALSE | TRUE | .NULL. |

Quando uma expressão condicional encontra um valor nulo, a condição falha, porque Null Value Handling não é verdadeiro (.T.). Por exemplo, uma FOR Clauses que avalia para .NULL. é tratada como falso (.F.). Observe que valores nulos são tratados como .NULL. até que toda a expressão seja avaliada.

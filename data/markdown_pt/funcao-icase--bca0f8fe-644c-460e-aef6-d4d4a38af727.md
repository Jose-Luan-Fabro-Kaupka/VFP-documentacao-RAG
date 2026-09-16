# Função ICASE( )

Avalia os resultados de uma lista de condições.

```foxpro
ICASE( lCondition1, eResult1 [, lCondition2, eResult2] ...
   [, eOtherwiseResult])
```

#### Parâmetros
 **lCondition**
Especifica uma condição como uma expressão lógica a ser avaliada. Se lCondition for avaliada como False (.F.), ICASE( ) continua avaliando a próxima condição e retorna o eResult correspondente se ela for avaliada como True (.T.). Se lCondition for avaliada como null (.NULL.), o Visual FoxPro trata lCondition como se tivesse sido avaliada como False (.F.).
**eResult**
Especifica um resultado a ser retornado se lCondition for avaliada como True (.T.).
**eOtherwiseResult**
Contém o resultado retornado se todas as condições forem avaliadas como False (.F.).

# Valor de retorno

ICASE( ) retorna o primeiro eResult assim que lCondition for avaliada como True (.T.).

Se todas as condições forem avaliadas como False (.F.), ICASE( ) retorna eOtherwiseResult.

Se eOtherwiseResult for omitido e todas as condições forem avaliadas como False (.F.), ICASE( ) retorna null (.NULL.).

# Observações

Você deve sempre passar um conjunto de dois parâmetros para ICASE( ). Se você passar um número ímpar de parâmetros, o último parâmetro é tratado como o valor de retorno de eOtherwiseResult.

Você pode passar até 100 pares de parâmetros para ICASE( ).

Se você usar uma expressão ICASE( ) longa em uma expressão de filtro, como em uma cláusula FOR ou WHERE, certifique-se de que SYS(3055) esteja definido para um nível de complexidade apropriado para evitar a geração de um erro. Para obter mais informações, consulte SYS(3055) - FOR and WHERE Clause Complexity.

# Exemplo

O exemplo a seguir demonstra diferentes cenários usando ICASE( ) para avaliar expressões e retornar determinados valores com base nos resultados dessas expressões.

A linha de código a seguir exibe "First is true" porque a primeira expressão é avaliada como True (.T.).

```foxpro
? ICASE(1+1=2,"First is true",1+1=3,"Second is false","None are true")
```

A linha de código a seguir exibe "Second is true" porque a primeira expressão é avaliada como False (.F.), mas a segunda expressão é avaliada como True (.T.).

```foxpro
? ICASE(1+2=2,"First is false",1+2=3,"Second is true","None are true")
```

A linha de código a seguir exibe "None are true", que é o último resultado especificado, porque a primeira e a segunda expressões são avaliadas como False (.F.).

```foxpro
? ICASE(1+2=2,"First is false",1+1=3,"Second is false","None are true")
```

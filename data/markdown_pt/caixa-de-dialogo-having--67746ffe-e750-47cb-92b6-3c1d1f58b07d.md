# Caixa de diálogo Having

Especifica condições para selecionar quais grupos de registros incluir na saída da consulta.

A caixa de diálogo Having aparece quando você escolhe Having na guia Group By, Query and View Designers.
 **Field Name**
Especifica uma função, nome de campo ou outra expressão. Ao criar uma cláusula Having, selecione o campo para exibir uma lista de funções, uma lista de nomes de campo para cada tabela ou use o comando expression para exibir a caixa de diálogo Expression Builder. Se você escolher uma função, um submenu exibe uma lista de nomes de campo disponíveis para usar com essa função.
**Not**
Inverte o critério de comparação.
**Comparison criterion**
Especifica o operador para o critério de seleção. Os critérios de comparação são os seguintes: Equal (=) Especifica que o campo e o valor no campo Example têm o mesmo valor. Like Especifica que o campo deve incluir caracteres que correspondam aos caracteres no texto no campo Example. Por exemplo, Customer.state Like O corresponde a registros de Ohio, Oklahoma e Oregon. Exactly Like (==) Especifica que o campo deve corresponder, caractere por caractere, ao texto no campo Example. Greater Than (>) Especifica que o campo deve ser maior que o valor no campo Example. Less Than (<) Especifica que o campo deve ser o mesmo ou menor que o valor no campo Example. Greater Than or Equal To (>=) Especifica que o campo deve ser o mesmo ou maior que o valor no campo Example. Less Than or Equal To (<=) Especifica que o campo deve ser o mesmo ou menor que o valor no campo Example. Is NULL Especifica que o campo deve conter um valor null. Is True Especifica que o campo ou expressão à esquerda avalia como True, assumindo que o campo ou expressão avalia como um valor lógico. Between Especifica que o campo deve ser maior ou igual ao valor inferior e menor ou igual ao valor superior na condição que aparece na coluna Example. Você deve separar os dois valores na coluna Example com a palavra AND. O Visual FoxPro cria a consulta com a palavra BETWEEN. Por exemplo, Invoices.idate Between 05/10/97 AND 05/12/97 corresponde a registros dos dias 10, 11 e 12 de maio de 1997. In Especifica que o campo deve corresponder a um de vários valores na lista separada por vírgulas que aparece no campo Example. Por exemplo, Customer.name In Al,George,Mary corresponde a registros em que o nome do cliente é Al, George ou Mary.
**Example**
Especifica o valor ou texto com o qual você deseja comparar o campo. Para corresponder à capitalização do texto do exemplo, use as funções UPPER( ), LOWER( ) e PROPER( ).
**Logical**
Adiciona uma condição AND ou OR à lista de condições.
**Pri. (Priority)**
Especifica um número de 0 a 99, que indica a prioridade para operações lógicas. O número 0 indica a prioridade mais alta, enquanto o número 99 indica a prioridade mais baixa. Definir prioridades para operações lógicas determina a ordem em que as operações lógicas são executadas e usa parênteses (()) para agrupar operações. Por exemplo, suponha que você especifique uma prioridade de 0 para uma operação lógica, uma prioridade de 1 para uma segunda operação lógica e uma prioridade de 0 para uma terceira operação lógica. A primeira e a terceira operações lógicas, que têm prioridade 0, são executadas antes da segunda operação lógica, que tem prioridade 1.
**Insert**
Insere uma linha em branco acima da condição selecionada.
**Remove**
Remove a linha selecionada da lista Field Name.

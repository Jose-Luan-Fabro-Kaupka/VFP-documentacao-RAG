# Guia Dynamics, caixa de diálogo Report Control Properties (Report Builder)

Permite especificar uma ou mais expressões que alteram as propriedades de exibição em tempo de execução dos controles de relatório. A caixa de diálogo Report Control Properties aparece quando você clica em Properties no menu de atalho de um controle de relatório ou quando você clica duas vezes em um controle de relatório.
 - Como: formatar dinamicamente controles de relatório
 **Condition List**
Especifica a lista das condições de estilo dinâmico na ordem em que serão avaliadas. Para alterar a ordem de uma condição na lista, clique no botão mover à esquerda da condição e arraste-a para um novo local na lista. Observação Se você reordenou suas condições, a sequência CASE na Dynamic Script Preview Dialog Box (Report Builder) não refletirá a nova ordem até que você salve as alterações saindo da caixa de diálogo Field Properties.
**Add**
Exibe a caixa de diálogo Add Dynamic Style Condition, onde você especifica um nome para uma nova condição a ser adicionada à lista. Quando você insere um nome e clica em OK, a Configure Dynamic Properties Dialog Box (Report Builder) abre para que você possa criar uma condição e especificar um estilo para o controle quando a expressão de condição for avaliada como .T..
**Edit**
Exibe a Configure Dynamic Properties Dialog Box (Report Builder) para que você possa modificar as propriedades de estilo dinâmico da condição selecionada na lista Condition.
**Remove**
Exclui a condição dinâmica selecionada.
**Script**
Exibe a Dynamic Script Preview Dialog Box (Report Builder) para que você possa ver o código que realmente executa o estilo dinâmico em tempo de execução. Você não pode modificar o código nesta caixa de diálogo, mas pode copiá-lo e colá-lo em uma user-defined function para personalizá-lo.

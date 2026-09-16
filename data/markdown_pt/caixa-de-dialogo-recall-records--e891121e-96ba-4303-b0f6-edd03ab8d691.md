# Caixa de diálogo Recall (Records)

Permite desmarcar registros que estão marcados para exclusão. Corresponde ao comando RECALL Command.
 **Scope**
Permite especificar os registros nos quais o Visual FoxPro deve atuar. Escolha Next , All , Record ou Rest na lista suspensa. Escolha um número no controle giratório à direita quando selecionar Next ou Record na lista suspensa Scope.
**For**
Exibe a caixa de diálogo Expression Builder, onde você cria a expressão lógica que cada registro deve satisfazer para ser afetado pelo comando. Cada registro na tabela é testado usando a expressão For.
**While**
Exibe a caixa de diálogo Expression Builder. A expressão While especifica que a ação afeta registros somente enquanto a expressão lógica for verdadeira. Na primeira vez que a expressão for avaliada como falsa, a ação cessa sem considerar os registros restantes.
**Recall**
Recupera registros usando os valores Scope, For e While.

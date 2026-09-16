# Caixa de diálogo Excluir (registros)

Permite marcar registros para exclusão. Corresponde ao comando DELETE Command.

Este comando não exclui fisicamente os registros, mas apenas os marca para exclusão futura. Para excluir permanentemente registros do disco rígido, use Remover registros excluídos no menu Tabela.
 **Scope**
Permite especificar os registros nos quais o Visual FoxPro deve atuar. Escolha Next, All, Record ou Rest na lista suspensa. Escolha um número no controle giratório à direita quando você selecionar Next ou Record na lista suspensa Scope.
**For**
Exibe a Caixa de diálogo Expression Builder, onde você cria a expressão lógica que cada registro deve satisfazer para ser afetado pelo comando. Cada registro na tabela é testado usando a expressão For.
**While**
Exibe a Caixa de diálogo Expression Builder. A expressão While especifica que a ação afeta registros apenas enquanto a expressão lógica for verdadeira. Na primeira vez que a expressão é avaliada como falsa, a ação cessa sem considerar os registros restantes.
**Delete**
Exclui registros usando os valores Scope, For e While.

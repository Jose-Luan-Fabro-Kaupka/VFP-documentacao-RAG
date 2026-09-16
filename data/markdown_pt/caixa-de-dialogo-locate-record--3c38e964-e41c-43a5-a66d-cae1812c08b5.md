# Caixa de diálogo Locate Record

Pesquisa um registro na tabela ou exibição ativa que corresponda às condições especificadas. Use este comando quando quiser pesquisar uma tabela ou exibição registro por registro em um campo indexado ou não indexado, ou quando quiser encontrar mais de um registro em uma tabela.

Esta caixa de diálogo aparece quando você escolhe o comando Locate no submenu Go to Record.
 **Scope**
Permite especificar os registros nos quais o Visual FoxPro deve atuar. Escolha All , Next , Record ou Rest na lista suspensa. Escolha um número no controle giratório à direita quando selecionar Next ou Record na lista suspensa Scope.
**For**
Exibe a caixa de diálogo Expression Builder, na qual você cria a expressão lógica que cada registro deve satisfazer para ser afetado pelo comando.
**While**
Exibe a caixa de diálogo Expression Builder . A expressão While especifica que a ação afeta registros somente enquanto a expressão lógica for verdadeira. Na primeira vez que a expressão for avaliada como falsa, a ação cessa sem considerar os registros restantes.
**Locate**
Executa o comando usando os valores Scope, For e While.

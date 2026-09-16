# Caixa de diálogo Replace Field

Altera valores armazenados em um registro ou em um intervalo de registros.
 **Field**
Exibe o nome dos campos de tabela da tabela atual. Quando você clica na seta para baixo, os tipos e tamanhos dos campos são exibidos.
**With**
Especifica a expressão que descreve os valores de substituição. Digite a expressão ou escolha o botão de diálogo para exibir a caixa de diálogo Expression Builder e criar uma expressão de substituição.

# Critérios de substituição
 **Scope**
Permite especificar os registros sobre os quais o Visual FoxPro deve atuar. Next, All, Record ou Rest na lista suspensa. Escolha um número no spinner à direita quando selecionar Next ou Record na lista suspensa Scope.
**For**
Exibe a caixa de diálogo Expression Builder, onde você cria a expressão lógica que todo registro deve atender para ser afetado pelo comando. Todo registro na tabela é testado usando a expressão For.
**While**
Exibe a caixa de diálogo Expression Builder. A expressão While especifica que a ação afeta registros somente enquanto a expressão lógica for true. Na primeira vez que a expressão for avaliada como false, a ação cessa sem considerar os registros restantes.
**Replace**
Substitui registros usando os valores Scope, For e While. Habilitado somente quando você tem um nome de campo ou expressão em ambas as caixas de texto Field e With.

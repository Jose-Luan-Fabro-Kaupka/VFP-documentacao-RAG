# Guia Update Criteria, View Designer

Especifica condições para enviar alterações na exibição aos registros originais nas tabelas usadas na exibição. A guia Update Criteria aparece apenas no View Designer.
 **Table**
Especifica quais tabelas usadas na exibição podem aceitar alterações. A lista mostra as tabelas que possuem campos na lista Selected fields da guia Fields Tab, Query and View Designers .
**Reset Key**
Seleciona o campo de chave primária de cada tabela como os campos de chave da exibição e coloca uma marca de seleção sob o símbolo de chave na lista Field name para cada campo de chave primária. Campos de chave são usados para corresponder as alterações na exibição ao registro original na tabela.
**Update All**
Seleciona todos os campos, exceto os campos de chave, para atualização e coloca uma marca de seleção sob o símbolo de lápis na lista Field name.
**Send SQL Updates**
Especifica se as alterações nos registros da exibição são realmente enviadas às tabelas originais.
**Field Name Pane**
Mostra os campos que você selecionou para saída e, portanto, estão disponíveis para atualização. Key Field (marcado com um símbolo de chave) Especifica se o campo é um campo de chave. Updatable (marcado com um símbolo de lápis) Especifica se o campo é atualizável. Field Name Exibe o nome dos campos de saída disponíveis para marcar como campos de chave ou atualizáveis.

# SQL WHERE Clause Includes

Controla quais campos são adicionados à cláusula WHERE para detectar conflitos de atualização no servidor quando as alterações na exibição são enviadas às tabelas originais.

Um conflito é baseado em uma comparação entre os valores antigos na exibição, OLDVAL( ), e os valores atuais na tabela original, CURVAL( ). Se os valores são iguais, a tabela original é considerada inalterada e não existe conflito. Se não são iguais, existe um conflito e a fonte de dados retorna um erro.

O erro retornado para um conflito entre o valor antigo e o valor atual é o Erro 1585 "Record has been modified by another" ou o Erro 1494 "Update conflict. Use TABLEUPDATE( ) to force the update or TABLEREVERT( ) to rollback".
 **Key Fields Only**
Define a cláusula WHERE para detectar um conflito se um campo de chave foi alterado na tabela original. Alterações feitas por outro usuário em qualquer outro campo no registro original da tabela não são comparadas.
**Key and Updatable Fields**
Define a cláusula WHERE para detectar um conflito se outro usuário alterou qualquer um dos campos que eram atualizáveis.
**Key and Modified Fields**
Define a cláusula WHERE para detectar um conflito se o campo de chave ou um dos campos modificados no registro na tabela original foi alterado desde que a exibição foi recuperada pela primeira vez (padrão).
**Key and Timestamp**
Define a cláusula WHERE para detectar um conflito se o timestamp do registro na tabela original foi alterado desde que foi recuperado pela primeira vez. Esta opção está disponível apenas se a tabela remota possui uma coluna de timestamp.

# Update Using

Especifica como as atualizações são executadas no servidor de back-end.
 **SQL DELETE then INSERT**
Exclui o registro da tabela original e depois cria um novo registro a partir do registro modificado na exibição.
**SQL UPDATE**
Usa as alterações nos campos da exibição para modificar os campos na tabela original.

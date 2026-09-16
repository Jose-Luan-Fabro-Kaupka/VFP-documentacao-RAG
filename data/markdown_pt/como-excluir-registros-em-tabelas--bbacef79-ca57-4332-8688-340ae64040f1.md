# Como: excluir registros em tabelas

Você pode excluir registros marcando-os para exclusão e depois removendo os registros excluídos. Caso contrário, registros marcados para exclusão permanecem no disco até que você os remova. Você também pode excluir e remover todos os registros de uma tabela.

> **Dica:** Ao visualizar registros em uma janela de browse, registros marcados para exclusão ainda aparecem se o comando SET DELETED estiver definido como OFF. Para ocultar registros marcados para exclusão, defina o comando SET DELETED como ON. SET DELETED também determina se comandos que operam em registros podem acessar registros marcados para exclusão. Você também pode criar uma tag de índice usando a função DELETED( ). Para obter mais informações, consulte Índices baseados em registros excluídos.

Você pode restaurar registros marcados para exclusão antes de removê-los. Para obter mais informações, consulte Como: restaurar registros excluídos.

### Para marcar um registro para exclusão
- Abra a tabela em uma janela de browse.
- Na janela de browse, insira o cursor em um campo do registro que deseja excluir.
- No menu Table, clique em Toggle Deletion Mark. A marca de exclusão aparece na coluna à esquerda do primeiro campo no registro. Dica Você também pode clicar duas vezes na coluna para marcar o registro para exclusão.

Para obter mais informações, consulte Como: visualizar registros em tabelas.

### Para marcar vários registros para exclusão
- Abra a tabela em uma janela de browse.
- No menu Table, clique em Delete Records. A caixa de diálogo Delete é aberta.
- Na caixa Scope da caixa de diálogo Delete, selecione o intervalo de registros que deseja excluir.
- Na caixa For, digite uma expressão que os registros devem atender para serem incluídos na exclusão. Para construir uma expressão, clique no botão de reticências (...).
- Na caixa While, digite uma expressão que avalia como true para continuar avaliando registros a incluir na exclusão.
- Quando terminar, clique em Delete.

Para obter mais informações, consulte Como: visualizar registros em tabelas e Caixa de diálogo Delete (Records).

### Para marcar registros para exclusão programaticamente
- Use o comando SQL DELETE.

Para obter mais informações, consulte Comando DELETE - SQL.

### Para excluir e remover todos os registros de uma tabela
- Use o comando ZAP.

Para obter mais informações, consulte Comando ZAP.

> **Observação:** Antes de usar o comando ZAP, certifique-se de que a tabela foi aberta exclusivamente.

> **Cuidado:** Registros excluídos e removidos com ZAP não podem ser restaurados.

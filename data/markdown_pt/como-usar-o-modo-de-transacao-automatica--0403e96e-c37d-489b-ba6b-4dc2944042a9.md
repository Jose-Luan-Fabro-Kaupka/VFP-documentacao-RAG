# Como: usar o modo de transação automática

Por padrão, o Visual FoxPro envolve automaticamente em uma transação cada operação de gravação de dados enviada ao servidor remoto. Esse tratamento automático padrão é fornecido quando a propriedade Transactions está definida como 1 ou DB_TRANSAUTO.

### Para usar o modo de transação automática
- Use a função DBSETPROP( ) para definir a propriedade Transactions da conexão como 1 ou DB_TRANSAUTO. -ou-
- Use a função SQLSETPROP( ) para definir a propriedade Transactions da conexão ativa como 1 ou DB_TRANSAUTO.

O processamento de transações da tabela remota é tratado automaticamente.

> **Observação:** Os comandos BEGIN TRANSACTION e END TRANSACTION do Visual FoxPro criam uma transação somente para o cursor local do Visual FoxPro. Eles não estendem a transação ao servidor remoto.

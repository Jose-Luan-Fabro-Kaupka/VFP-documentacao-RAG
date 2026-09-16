# Exemplo Nest Transactions

Arquivo: ...\Samples\Solution\Db\transact.scx

Este exemplo ilustra o início, o término e a reversão de transações. Você pode decidir confirmar ou descartar alterações em uma única tabela ao usar buffer de tabela, mas pode decidir confirmar ou descartar alterações em qualquer número de tabelas ao usar transações.

Antes de editar qualquer uma das tabelas, clique no botão Begin. Após a edição, você pode clicar em Begin novamente para aninhar outra transação, ou pode clicar em End para confirmar suas edições na tabela ou em Rollback para descartar suas alterações.

Os comandos principais neste exemplo são os seguintes:

```foxpro
BEGIN TRANSACTION
END TRANSACTION
ROLLBACK
```

A função que retorna o número atual de transações aninhadas é a seguinte:

```foxpro
TXNLEVEL()
```

# Exemplo Criar um formulário de entrada de dados um-para-muitos

Arquivo: ...\Samples\Solution\Forms\Many.scx

Este exemplo ilustra as tarefas básicas associadas a um formulário de entrada de dados um-para-muitos.

Quando você escolhe o botão New ao lado das caixas de texto da tabela pai, o seguinte código é executado:

```foxpro
SELECT CUSTOMER
APPEND BLANK
THISFORM.Refresh
```

Quando você escolhe o botão New ao lado da grade que exibe os registros filhos, mais código é executado.

Após selecionar a tabela orders, o código calcula um novo valor de id para o pedido, adiciona o registro em branco e então armazena o id pai e o id do pedido nos campos apropriados.

```foxpro
CALCULATE MAX(order_id) ALL TO lMaxID
lMaxID = ALLTRIM(STR(VAL(lMaxID) + 1))
APPEND BLANK
REPLACE cust_id WITH Customer.Cust_id IN orders
REPLACE order_id with lMaxID in orders
```

> **Observação:** Este método de criar um novo valor de id não seria confiável se vários usuários estivessem adicionando novos pedidos ao mesmo tempo. Em vez disso, você pode criar um novo id conforme ilustrado no exemplo Criar um valor de ID exclusivo padrão para um campo.

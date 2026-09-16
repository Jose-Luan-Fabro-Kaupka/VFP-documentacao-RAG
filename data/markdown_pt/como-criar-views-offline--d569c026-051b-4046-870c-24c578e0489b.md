# Como: criar views offline

Como nos dados online, analise seus requisitos antes de criar views offline para determinar o design das views que você precisará no banco de dados offline. Depois de saber o subconjunto de dados que deseja usar offline, você pode começar com uma view existente ou criar uma nova view. Se já existir uma view que retorna os registros que você deseja usar offline, você pode usá-la ou criar uma programaticamente. A view que você leva offline é armazenada em um arquivo .dbf no contêiner do banco de dados offline.

> **Observação:** Se você planeja modificar dados em uma view offline, certifique-se de tornar a view atualizável antes de levá-la offline. Depois que uma view está offline, você só pode definir suas propriedades de atualização programaticamente; não é possível modificar uma view offline nos Query and View Designers.

### Para usar uma view existente offline
- Use a função CREATEOFFLINE( ) e o nome da view.

Por exemplo, se você deseja ir a locais de clientes para atualizar contas, adicionar clientes e registrar novas vendas, precisa das informações do cliente, bem como dos pedidos atuais e das descrições de produtos online. Você pode ter uma view chamada `customerinfo` que combina informações das tabelas Customers, Orders e OrderItems. Para criar a view, use este código:

```foxpro
CREATEOFFLINE("customerinfo")
```

### Para criar uma view offline programaticamente
- Use o comando CREATE SQL VIEW, seguido da função CREATEOFFLINE( ).

Por exemplo, o código a seguir cria uma view que exibe dados das tabelas `Products` e `Inventory` do banco de dados online. Como nenhum critério de atualização é especificado, esta view é somente leitura:

```foxpro
CREATE SQL VIEW showproducts ;
   CONNECTION dsource ;
   AS SELECT * FROM Products INNER JOIN Inventory ;
   ON Products.ProductID = Inventory.ProductID ;
CREATEOFFLINE("showproducts")
```

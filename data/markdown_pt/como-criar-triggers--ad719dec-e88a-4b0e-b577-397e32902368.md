# Como: criar triggers

Você pode criar triggers usando o Table Designer ou o comando CREATE TRIGGER. Para cada tabela, você pode criar um trigger para cada um dos três eventos: INSERT, UPDATE e DELETE. Uma tabela pode ter no máximo três triggers a qualquer momento.

### Para criar um trigger
- Na guia Table do Table Designer (Visual FoxPro) , insira a expressão de trigger ou o nome de um stored procedure contendo a expressão de trigger na caixa Insert trigger , Update trigger ou Delete trigger. -ou-
- Use o Comando CREATE TRIGGER .

Por exemplo, talvez cada vez que a Tasmanian Traders vende um item, eles desejem comparar o `Units_in_stock` restante com o `Reorder_level` e ser notificados se precisam reordenar esse item. Você pode criar um trigger Update na tabela `products` para isso. Cada vez que um produto é vendido, o trigger Update será disparado e o campo `Units_in_stock` será atualizado para refletir os itens restantes em estoque.

Para criar o trigger, você pode especificar `updProductsTrigger( )` como seu trigger Update para a tabela `products`. Você pode adicionar um campo a `products`, chamado `reorder_amount`, que armazena a quantidade que deseja pedir cada vez que reordena o item, e criar uma tabela `reorder` com os campos: `product_id` e `reorder_amount`. Você pode então adicionar este código ao seu stored procedure:

```foxpro
PROCEDURE updProductsTrigger
   IF (units_in_stock+units_on_order) <= reorder_level
   INSERT INTO Reorder VALUES(Products.product_id, ;
    Products.reorder_amount)
   ENDIF
ENDPROC
```

Você pode criar triggers semelhantes para um evento insert ou delete usando a cláusula FOR INSERT ou FOR DELETE, respectivamente, em vez da cláusula FOR UPDATE. Se você tentar criar um trigger que já existe para um evento e tabela específicos enquanto o Comando SET SAFETY estiver ativado, o Visual FoxPro solicita que você confirme a substituição do trigger existente.

> **Observação:** Quando um trigger é chamado, o Alias é sempre o do cursor sendo atualizado, independentemente do Alias selecionado no código que causou o disparo do trigger.

O Visual FoxPro inclui o Referential Integrity Builder para gerar triggers e stored procedures que impõem regras de Integridade Referencial (RI) para seu banco de dados. Para obter mais informações sobre o uso do RI Builder, consulte Referential Integrity Builder e Como: construir integridade referencial entre tabelas.

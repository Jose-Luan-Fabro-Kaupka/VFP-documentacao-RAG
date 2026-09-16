# Propriedade ChildOrder

Especifica a tag de índice para a fonte de registros do controle Grid ou do objeto Relation. Disponível em tempo de design e somente leitura em tempo de execução.

```foxpro
Object.ChildOrder[ = cTagName]
```

# Valor de retorno
 **cTagName**
Especifica um nome de tag de índice existente.

# Observações

Aplica-se a: Controle Grid | Objeto Relation

Se a propriedade ChildOrder estiver definida, a propriedade Order do Cursor para a tabela filha é ignorada.

Use esta propriedade para vincular duas tabelas que possuem um relacionamento um-para-muitos. Por exemplo, uma tabela de clientes contendo um registro por cliente se vincula a uma tabela de pedidos contendo vários pedidos por cliente. Para este relacionamento um-para-muitos, defina a propriedade ChildOrder para o campo de tag de índice de ID do cliente.

A propriedade ChildOrder imita o comportamento de SET ORDER.

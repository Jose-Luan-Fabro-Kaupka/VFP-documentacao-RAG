# Como: otimizar filtros e joins

Para tomar decisões de otimização para uma view ou consulta, você pode precisar conhecer o plano de execução: a ordem em que as cláusulas de join e de filtro serão avaliadas. Usando a função SYS(3054) - Rushmore Query Optimization Level, você pode exibir um dos três níveis de otimização Rushmore Query. Os três níveis indicam o grau em que as condições de filtro ou de join puderam usar a otimização Rushmore. Os níveis são completamente (Full), parcialmente (Partial) ou nenhum (None).

### Para exibir o plano de execução para filtros
- Na janela Command, digite SYS(3054,1) para habilitar SQL ShowPlan.
- Digite sua instrução SQL SELECT. Por exemplo, você pode digitar: SELECT * FROM customer, orders ; AND Upper(country) = "MEXICO"
- Na tela, leia o plano de execução. Para este exemplo, a tela pode exibir: Using Index Tag Country to optimize table customer Rushmore Optimization Level for table customer: Full Rushmore Optimization level for table orders: none
- Na janela Command, digite SYS(3054,0) para desativar SQL ShowPlan.

Você pode então passar 11 para a função SYS para avaliar joins nas cláusulas FROM ou WHERE.

### Para exibir o plano de execução para joins
- Na janela Command, digite SYS(3054,11) para habilitar SQL ShowPlan.
- Digite sua instrução SQL SELECT. Por exemplo, você pode digitar: SELECT * ; FROM customer INNER JOIN orders ; ON customer.cust_id = orders.cust_id ; WHERE Upper(country) = "MEXICO"
- Na tela, leia o plano de execução. Para este exemplo, a tela pode exibir: Using Index Tag Country to optimize table customer Rushmore Optimization Level for table customer: Full Rushmore Optimization level for table orders: none Joining table customer and table orders using Cust_id
- Na janela Command, digite SYS(3054,0) para desativar SQL ShowPlan.

# Controlando a avaliação de joins

Se o plano de execução dos seus joins não corresponder às suas necessidades específicas, você pode forçar a ordem do join a ser executada exatamente como escrita, sem otimização do processador.

### Para forçar a ordem de avaliação do join
- Adicione a palavra-chave FORCE e coloque suas condições de join na cláusula FROM. Observação Observação Condições de join colocadas na cláusula WHERE não são incluídas em uma avaliação de join forçada.

> **Observação:** Você não pode usar a palavra-chave FORCE em instruções SQL pass-through ou views remotas porque essa palavra-chave é uma extensão do Visual FoxPro do padrão ANSI e não é suportada em outros dicionários SQL. A cláusula FORCE é global e, portanto, se aplica a todas as tabelas na cláusula JOIN. Certifique-se de que a ordem em que as tabelas de join aparecem seja exatamente a ordem em que devem ser unidas. Você também pode usar parênteses para controlar a ordem de avaliação dos joins.

Neste exemplo, o primeiro join especificado também é o primeiro join avaliado. A tabela Customer é unida à tabela Orders primeiro. O resultado desse join é então unido à tabela `OrdItems`:

```foxpro
SELECT * ;
   FROM FORCE Customers ;
   INNER JOIN Orders ;
      ON Orders.Company_ID = Customers.Company_ID ;
   INNER JOIN OrItems;
      ON OrdItems.Order_NO = Orders.Order_NO
```

Neste exemplo, o join dentro dos parênteses para as tabelas `Orders` e `OrdItems` é avaliado primeiro. O resultado desse join é então usado na avaliação do join com `Customers`:

```foxpro
SELECT * ;
FROM FORCE Customers ;
   INNER JOIN (orders INNER JOIN OrdItems ;
      ON OrdItems.Order_No = Orders.Order_No) ;
      ON Orders.Company_ID = Customers.Company_ID
```

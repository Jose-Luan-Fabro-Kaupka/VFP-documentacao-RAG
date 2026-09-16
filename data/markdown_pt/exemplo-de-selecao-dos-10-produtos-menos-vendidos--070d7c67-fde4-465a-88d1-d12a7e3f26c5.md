# Exemplo de seleção dos 10 produtos menos vendidos

Arquivo: ...\Samples\Data\Worstten.qpr

Esta consulta exibe os 10 produtos menos vendidos com base nas vendas registradas na tabela Order Items. A consulta usa o recurso TOP n da instrução SELECT e, como a ordem padrão vai do menor para o maior, ordenar pela soma do preço e da quantidade retorna os 10 menores valores.

```foxpro
SELECT TOP 10 Products.prod_name,;
  SUM(Orditems.unit_price*Orditems.quantity);
 FROM testdata!products INNER JOIN testdata!orditems ;
   ON Products.product_id = Orditems.product_id;
 GROUP BY Products.prod_name;
 ORDER BY 2
```

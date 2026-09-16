# "field | variable" não é único e deve ser qualificado (Erro 1832)

Você referenciou um campo que existe em mais de uma tabela.

Por exemplo, se você usar o banco de dados TESTDATA e emitir o seguinte comando, o mesmo erro ocorre porque o campo `cust_id` existe nas tabelas `customer` e `orders`:

```foxpro
SELECT cust_id FROM customer,orders
```

 - Para contornar a não unicidade dos nomes de campo, emita o seguinte comando: SELECT customer.cust_id FROM customer,orders Para obter mais informações, consulte SELECT - SQL Command.

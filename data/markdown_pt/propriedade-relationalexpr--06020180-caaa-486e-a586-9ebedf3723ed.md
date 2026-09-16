# Propriedade RelationalExpr

Especifica a expressão baseada em campos da tabela pai que se relaciona a um índice na tabela filha, unindo as duas tabelas. Para o controle Grid, disponível em tempo de design; leitura/gravação em tempo de execução. Para o objeto Relation, disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.RelationalExpr[ = cExpr]
```

# Valor de retorno
 **cExpr**
Especifica qualquer expressão do Visual FoxPro, normalmente uma que corresponda ao índice atual da tabela filha conforme especificado pela propriedade ChildOrder.

# Observações

Aplica-se a: Controle Grid | Objeto Relation

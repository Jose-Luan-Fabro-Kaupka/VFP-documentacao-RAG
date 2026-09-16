# Propriedade ColumnOrder

Especifica a ordem relativa dos objetos Column em um controle Grid. Disponível em tempo de design e em tempo de execução.

```foxpro
Column.ColumnOrder[ = nExpr]
```

# Valor de retorno
 **nExpr**
Especifica a ordem de uma coluna em relação às outras colunas na grade.

# Observações

Aplica-se a: Column Object

Se um Grid contém cinco colunas e você deseja que a terceira coluna seja exibida por último, defina a propriedade ColumnOrder da terceira coluna como 5. A configuração ColumnOrder da quarta coluna passa a ser 3, a configuração ColumnOrder da quinta coluna passa a ser 4, e assim por diante.

> **Observação:** As configurações ColumnOrder não precisam ser sequenciais.

# Propriedade Partition

Especifica se um controle Grid é dividido em dois painéis e especifica onde a divisão está em relação à borda esquerda da grade. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Grid.Partition[ = nSplit]
```

# Valor de retorno
 **nSplit**
Especifica a posição onde a grade se divide em dois painéis. Se nSplit for 0, a grade não é dividida.

# Observações

Aplica-se a: Controle Grid

Observe que a propriedade SplitBar tem precedência sobre a propriedade Partition.

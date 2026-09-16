# Propriedade BoundColumn

Determina qual coluna de uma caixa de listagem ou caixa de combinação com várias colunas está vinculada à propriedade Value do controle. Disponível em tempo de design e de execução.

```foxpro
Control.BoundColumn[ = nCol]
```

# Valor de retorno
 **nCol**
Especifica o número da coluna vinculada à propriedade Value. O padrão de nCol é 1.

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Use BoundColumn quando a caixa de listagem ou caixa de combinação tiver várias colunas e você quiser que os dados de uma coluna diferente da primeira sejam armazenados na propriedade Value do controle.

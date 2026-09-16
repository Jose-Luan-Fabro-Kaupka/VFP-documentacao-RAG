# Propriedade Sorted

Especifica se os itens da parte de lista de um controle ComboBox ou ListBox são classificados automaticamente em ordem alfabética. Disponível em tempo de design e execução.

```foxpro
 [Form.]Control.Sorted[= lExpr]
```

# Valor de retorno
 **lExpr**
As configurações são: verdadeiro (.T.), os itens são classificados alfabeticamente com distinção entre maiúsculas e minúsculas, e o Visual FoxPro processa as cadeias e ajusta os números dos índices quando itens são adicionados ou removidos; falso (.F.) (padrão), os itens não são classificados.

# Observações

Aplica-se a: controle ComboBox | controle ListBox

Sorted só está disponível se RowSourceType estiver definida como 0 (None) ou 1 (Value).

Depois que os itens são classificados, definir Sorted como falso (.F.) não restaura a ordem original. Para restaurá-la, atribua a propriedade RowSource do controle a ela mesma:

```foxpro
MyForm.MyCombo1.Rowsource = MyForm.MyCombo1.Rowsource
```

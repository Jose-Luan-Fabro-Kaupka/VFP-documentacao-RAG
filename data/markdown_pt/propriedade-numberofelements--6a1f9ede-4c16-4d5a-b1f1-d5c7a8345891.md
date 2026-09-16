# Propriedade NumberOfElements

Especifica quantos itens em uma matriz são usados para preencher a parte de lista de um controle ComboBox ou ListBox. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Form.]Control.NumberOfElements[ = nTotal]
```

# Valor de retorno
 **nTotal**
Especifica o número de elementos que uma lista pode conter.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

Disponível somente quando a propriedade ListSourceType está definida como 5 (Array) e a propriedade ColumnCount está definida como 1.

NumberOfElements é útil para limitar o número de elementos em uma matriz que são exibidos em uma lista. O número de elementos usados para a lista começa com a configuração da propriedade FirstElement e inclui o número de elementos especificado na configuração da propriedade NumberOfElements.

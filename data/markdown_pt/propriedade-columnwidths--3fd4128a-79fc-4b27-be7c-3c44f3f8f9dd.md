# Propriedade ColumnWidths

Especifica a largura das colunas para um controle ComboBox ou ListBox. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.ColumnWidths[ = "cCol1Width, cCol2Width, ... cColnWidth"]
```

# Valor de retorno
 **" cCol1Width , cCol2Width , ...cColnWidth "**
Especifica a largura de uma coluna ou série de colunas no ComboBox ou ListBox. Por exemplo, cColumnWidths = "5, 7, 9" especifica que a primeira coluna tem 5 unidades de largura, a segunda coluna tem 7 unidades de largura e a terceira coluna tem 9 unidades de largura, na unidade de medida especificada pela propriedade ScaleMode do formulário. Use vírgulas para separar cada número de largura. Você pode especificar o número de colunas com a propriedade ColumnCount.

# Observações

Aplica-se a: ComboBox Control | ListBox Control

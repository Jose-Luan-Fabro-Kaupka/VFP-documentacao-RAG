# Propriedade AutoSize

Especifica se um controle é redimensionado automaticamente para ajustar seu conteúdo. Disponível em tempo de design e execução.

```foxpro
Control.AutoSize[ = lExpr]
```

# Valor de retorno
 **lExpr**
True (.T.): o controle é redimensionado automaticamente para ajustar seu conteúdo. False (.F.) (Padrão): o conteúdo é recortado quando excede a área do controle.

# Observações

Aplica-se a: controle CheckBox | controle CommandButton | controle CommandGroup | controle Label | controle OLE Bound | controle OLE Container | controle OptionButton | controle OptionGroup

Para controles OLE Container, AutoSize aplica-se apenas a objetos OLE compatíveis com edição no local. Sizable deve ser verdadeiro (.T.) para alterar o tamanho durante essa edição.

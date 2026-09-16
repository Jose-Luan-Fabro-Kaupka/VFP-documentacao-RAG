# Propriedade ControlSource

Especifica a fonte de dados à qual um objeto está vinculado. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ControlSource[ = cName]
```

# Valor de retorno
 **cName**
Para controles, cName é uma variável ou campo.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandGroup Control | EditBox Control | ListBox Control | OLE Bound Control | OptionButton Control | OptionGroup Control | Spinner Control | TextBox Control (Visual FoxPro)

Depois que a propriedade ControlSource é definida para um campo ou variável, a propriedade Value sempre tem o mesmo valor de dados e o mesmo tipo de dados que a variável ou campo para o qual a propriedade ControlSource está definida.

Para controles TextBox, cName é tipicamente um campo.

Em um controle Grid, se você não especificar uma configuração ControlSource para uma coluna, a coluna exibe o próximo campo disponível não exibido da fonte de registros do grid.

Se a propriedade Bound de uma Column está definida como True (.T.), a configuração da propriedade ControlSource da Column se aplica à coluna e a quaisquer controles contidos nela. Se você tentar definir a propriedade ControlSource do controle contido, ocorre um erro. Se a propriedade Bound de uma Column está definida como False (.F.), você pode definir a propriedade ControlSource de um controle contido diretamente. Se você posteriormente definir a configuração ControlSource da Column, ela substitui a configuração ControlSource do controle contido.

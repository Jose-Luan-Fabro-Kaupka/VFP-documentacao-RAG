# Propriedade ColorSource

Determina como as cores de um controle são definidas. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ColorSource[ = nSource]
```

# Valor de retorno
 **nSource**
As configurações de nSource são: Configuração Descrição 0 Propriedades de cor do objeto. O controle usa suas configurações de propriedades de cor (ForeColor, BackColor, e assim por diante). Esta configuração está disponível para os seguintes controles e objetos: CheckBox, ComboBox, CommandButton, CommandGroup, Container, Control, EditBox, Form, Image, Label, Line, ListBox, OptionButton, OptionGroup, Page, PageFrame, Shape, Spinner, TextBox e Toolbar. 1 Esquema de cores do formulário. O controle usa o esquema de cores do formulário no qual está colocado. Esta configuração está disponível para os seguintes controles e objetos: CheckBox, ComboBox, CommandButton, EditBox, Label, ListBox, OptionButton, Shape, Spinner e TextBox. 2 Esquema da propriedade ColorScheme. O controle usa o esquema de cores especificado em sua propriedade ColorScheme. Esta configuração está disponível para os seguintes controles e objetos: CheckBox, ComboBox, CommandButton, EditBox, Label, ListBox, OptionButton, Shape, Spinner e TextBox. 3 Esquema padrão. O controle usa seu esquema de cores padrão. Para a maioria dos controles, o esquema de cores padrão é o esquema de cores do formulário; para EditBoxes e ListBoxes, o esquema de cores padrão é o Scheme 2, User Menus. Esta configuração está disponível para os seguintes controles e objetos: CheckBox, ComboBox, CommandButton, EditBox, Label, ListBox, OptionButton, Shape, Spinner e TextBox. 4 Painel de Controle do Windows (Cores 3D) (Padrão). O controle usa as configurações de cor 3D especificadas no Painel de Controle do Windows. Esta configuração está disponível para os seguintes controles e objetos: CheckBox, ComboBox, CommandButton, CommandGroup, Container, Control, EditBox, Form, Image, Label, Line, ListBox, OptionButton, OptionGroup, Page, PageFrame, Shape, Spinner, TextBox e Toolbar. 5 Painel de Controle do Windows (Cores do Windows). O controle usa as configurações de cor especificadas no Painel de Controle do Windows. Esta configuração está disponível apenas para o objeto Form.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

Definir uma propriedade de cor (ForeColor, BackColor, SelectedForeColor, e assim por diante) para um objeto substitui a configuração da propriedade ColorSource. Se uma propriedade de cor não estiver definida para um objeto, as cores do objeto são determinadas pela configuração da propriedade ColorSource.

# Propriedade Application

Fornece uma referência ao objeto Application que contém um objeto. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.Application.Property [ = Setting]
-or-
Object.Application.Method
```

# Valor de retorno
 **Property**
Especifica qualquer propriedade do objeto Application ou da variável de sistema _VFP; por exemplo, a propriedade Caption.
**Setting**
A configuração existente ou nova da Property.
**Method**
Especifica qualquer método do objeto Application ou da variável de sistema _VFP; por exemplo, o método DoCmd.

# Observações

Aplica-se a: Controle CheckBox | Objeto Column | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Objeto Cursor | Classe CursorAdapter | Objeto Custom | Objeto DataEnvironment | Controle EditBox | Objeto Form | Objeto FormSet | Controle Grid | Objeto Header | Objeto Hyperlink | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OLE Container | Controle OptionButton | Controle OptionGroup | Objeto Page | Controle PageFrame | Objeto ProjectHook | Objeto Relation | Variável de sistema _SCREEN | Objeto Separator | Objeto Session | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro) | Controle Timer | Objeto ToolBar

Use a propriedade Application para acessar as propriedades e métodos de um objeto Application a partir de um objeto contido pela aplicação. A propriedade Application também pode ser usada com a variável de sistema _VFP para acessar propriedades e métodos da instância atual do Visual FoxPro.

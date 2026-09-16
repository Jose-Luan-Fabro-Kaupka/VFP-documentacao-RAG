# Método SetFocus

Atribui o foco a um controle.

```foxpro
Control.SetFocus
```

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Grid Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | Page Object | Spinner Control | TextBox Control (Visual FoxPro)

Você não pode atribuir o foco a um controle se a propriedade Enabled ou Visible do controle estiver definida como false (.F.), ou se o evento When do controle retornar false (.F.). Se a propriedade Enabled ou Visible foi definida como false (.F.), você deve primeiro defini-la como true (.T.) antes que o controle possa receber o foco do método SetFocus.

Depois que um controle tem o foco, qualquer entrada do usuário é direcionada a esse controle.

No Visual FoxPro 9.0, o método SetFocus não é suportado nos eventos When Event, Valid Event, RangeHigh Event e RangeLow Event. No entanto, você pode incluir um comando RETURN com um nome de objeto (RETURN <ObjectName>) nesses eventos para definir o foco em outro controle. Se um comando RETURN com um nome de objeto for incluído, o foco é definido no controle especificado com <ObjectName>.

O objeto especificado no comando RETURN deve ser um objeto válido do Visual FoxPro que possa receber o foco. Se o objeto que você especificar estiver desabilitado ou não puder receber o foco, o próximo objeto na ordem de tabulação recebe o foco. O foco permanece no objeto atual se você especificar um objeto inválido.

RETURN <ObjectName> permite definir o foco em um objeto em outro formulário visível. Você também pode definir o foco em um objeto em uma página não visível de um pageframe, mas deve incluir código para ativar essa página (por exemplo, PageFrame1.ActivePage = 2).

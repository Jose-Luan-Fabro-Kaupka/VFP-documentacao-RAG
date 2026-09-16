# Método ShowWhatsThis

Exibe o tópico da Ajuda "O que é isto?" especificado para um objeto com a propriedade WhatsThisHelpID.

```foxpro
Object.ShowWhatsThis
```

# Valor de retorno
 **Object**
Especifica o objeto para o qual o tópico da Ajuda "O que é isto?" é exibido.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

O método ShowWhatsThis é chamado automaticamente quando a tecla F1 é pressionada. Se a propriedade WhatsThisHelp estiver definida como verdadeiro (.T.), será exibido o tópico da Ajuda "O que é isto?" do objeto, especificado pela propriedade WhatsThisHelpID. Se a propriedade WhatsThisHelp estiver definida como falso (.F.), será exibido o tópico da Ajuda do objeto, especificado pela propriedade HelpContextID.

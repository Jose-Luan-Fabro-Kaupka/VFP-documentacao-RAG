# Propriedade Comment

Armazena informações sobre um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Comment[ = cTextString]
```

# Valor de retorno
 **cTextString**
Especifica uma cadeia de caracteres de texto.

# Observações

Aplica-se a: CheckBox Control | Collection Class | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | CursorAdapter Class | Custom Object | EditBox Control | Exception Class (Visual FoxPro) | Form Object | FormSet Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | ProjectHook Object | ReportListener Object | _SCREEN System Variable | Session Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

Diferentemente de outras propriedades, o valor da propriedade Comment não é usado pelo Visual FoxPro; você pode usar esta propriedade para identificar ou descrever objetos.

Você pode usar esta propriedade para atribuir uma cadeia de identificação a um objeto sem afetar nenhuma de suas outras configurações de propriedade. A propriedade Comment é útil para verificar a identidade de um controle ou formulário passado como variável para um procedimento.

Por padrão, a propriedade Comment é definida como uma cadeia de comprimento zero ("").

> **Dica:** Quando você cria uma nova instância de um formulário, atribua um valor exclusivo à propriedade Comment.

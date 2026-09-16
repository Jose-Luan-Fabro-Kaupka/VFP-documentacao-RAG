# Classes base no Visual FoxPro

O Visual FoxPro fornece um conjunto padrão de classes, ou classes base, que você pode usar imediatamente para fornecer funcionalidade básica em seu aplicativo. A tabela a seguir lista as classes base no Visual FoxPro, embora nem todas as classes base estejam disponíveis no Class Designer ou para criar subclasses.

| CheckBox | Collection | Column * | ComboBox |
| --- | --- | --- | --- |
| CommandButton | CommandGroup | Container | Control |
| Cursor | CursorAdapter | Custom | DataEnvironment |
| EditBox | Empty * | Exception | Form |
| FormSet | Grid | Header * | Hyperlink |
| Image | Label | Line | ListBox |
| OLE Bound | OLE Container | OptionButton | OptionGroup |
| Page | PageFrame | ProjectHook | Relation |
| ReportListener | Separator | Session Object | Shape |
| Spinner | TextBox | Timer | ToolBar |
| XMLAdapter | XMLField | XMLTable | |

* Não disponível para criação de subclasses

Todas as classes base do Visual FoxPro, exceto a classe Empty, reconhecem o seguinte conjunto mínimo de eventos:
 - Init Event
- Destroy Event
- Error Event

Todas as classes base do Visual FoxPro, exceto a classe Empty, têm o seguinte conjunto mínimo de propriedades:
 - Class Property
- BaseClass Property
- ClassLibrary Property
- ParentClass Property

# Evento Destroy

Ocorre quando um objeto é liberado.

```foxpro
PROCEDURE Object.Destroy
```

# Observações

Aplica-se a: CheckBox Control | Collection Class | Column Object | ComboBox Control | CommandButton Control | Container Object | Control Object (Visual FoxPro) | Cursor Object | CursorAdapter Class | Custom Object | DataEnvironment Object | EditBox Control | Exception Class (Visual FoxPro) | Form Object | FormSet Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | Page Object | PageFrame Control | ProjectHook Object | Relation Object | ReportListener Object | Session Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

O evento Destroy de um objeto container dispara antes do evento Destroy de qualquer um de seus objetos contidos; o evento Destroy do container pode referenciar seus objetos contidos antes de serem liberados.

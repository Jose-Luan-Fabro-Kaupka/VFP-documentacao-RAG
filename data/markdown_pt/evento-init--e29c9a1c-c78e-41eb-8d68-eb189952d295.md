# Evento Init

Ocorre quando um objeto é criado.

```foxpro
PROCEDURE Object.Init
[LPARAMETERS Param1, Param2,...]
```

#### Parâmetros
 **Param1, Param2...**
Os parâmetros são opcionais, mas se parâmetros são passados, você deve incluir uma instrução LPARAMETERS ou PARAMETERS que liste cada parâmetro. Caso contrário, o Visual FoxPro gera um erro.

# Observações

Aplica-se a: CheckBox Control | Collection Class | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Cursor Object | CursorAdapter Class | Custom Object | DataEnvironment Object | EditBox Control | Exception Class (Visual FoxPro) | Form Object | FormSet Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | ProjectHook Object | Relation Object | ReportListener Object | Session Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

Para form sets e outros objetos contêiner, os eventos Init de todos os objetos contidos são acionados antes do evento Init do contêiner, para que você possa acessar os objetos contidos no evento Init do contêiner. O evento Init de cada objeto contido ocorre na ordem em que foi adicionado ao objeto contêiner.

Para impedir que um controle seja criado, retorne false (.F.) do evento Init. O evento Destroy não será acionado. Por exemplo, o código a seguir retorna false (.F.) se a tabela Invoice não estiver disponível:

```foxpro
PROCEDURE INIT
  IF NOT FILE("INVOICE.DBF")
  ERROR 'Initialization Failed: File not found'
  RETURN .F.
  ELSE
  USE INVOICE IN 0 AGAIN
  THIS.WorkArea = SELECT()
  ENDIF
ENDPROC
```

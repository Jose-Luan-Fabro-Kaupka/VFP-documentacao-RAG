# Propriedade Name (Visual FoxPro)

Especifica o nome usado para referenciar um objeto no código. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.Name[ = cName]
```

# Valor de retorno
 **cName**
Especifica o nome usado para referenciar o objeto no código.

# Observações

Aplica-se a: CheckBox Control | Collection Class | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | Cursor Object | CursorAdapter Class | Custom Object | DataEnvironment Object | EditBox Control | Exception Class (Visual FoxPro) | File Object (Visual FoxPro) | Form Object | FormSet Object | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | Project Object (Visual FoxPro) | ProjectHook Object | Relation Object | ReportListener Object | _SCREEN System Variable | Session Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

O nome padrão para novos objetos é o tipo de objeto mais um inteiro exclusivo. Por exemplo, o primeiro novo objeto Form é Form1, e a terceira caixa de texto que você cria em um Form é Text3.

> **Observação:** Se o objeto é o primeiro objeto na hierarquia de objetos (ou seja, o objeto contêiner mais externo), use a variável de objeto para referenciar o objeto em vez da propriedade Name.

Para um objeto Project, a propriedade Name contém o nome e o caminho do projeto, e é somente leitura em tempo de design e em tempo de execução.

Para um objeto File, a propriedade Name contém o nome e o caminho do arquivo, e é somente leitura em tempo de design e em tempo de execução.

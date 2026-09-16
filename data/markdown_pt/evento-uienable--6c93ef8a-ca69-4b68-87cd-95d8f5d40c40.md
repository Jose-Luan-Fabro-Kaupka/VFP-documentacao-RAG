# Evento UIEnable

Ocorre para todos os objetos contidos em uma página sempre que a página é ativada ou desativada.

```foxpro
PROCEDURE Object.UIEnable
LPARAMETERS lEnable
```

#### Parâmetros
 **lEnable**
Contém um valor lógico que especifica se a página na qual o objeto está contido está sendo ativada ou desativada. Se lEnable for verdadeiro (.T.), a página na qual o objeto está contido está sendo ativada (tornando-se a página ativa). Se lEnable for falso (.F.), a página está sendo desativada (tornando-se a página inativa).

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionGroup Control | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro)

Use o evento UIEnable para especificar qualquer ação que deseja que ocorra para um objeto ou controle quando a página na qual ele está contido é ativada ou desativada.

O evento UIEnable não ocorre para páginas quando o formulário é ativado inicialmente. O evento UIEnable ocorre apenas quando uma página é ativada ou desativada programaticamente ou de forma interativa.

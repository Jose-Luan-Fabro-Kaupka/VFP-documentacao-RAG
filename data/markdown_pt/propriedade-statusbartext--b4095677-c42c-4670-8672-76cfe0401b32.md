# Propriedade StatusBarText

Especifica o texto exibido na barra de status quando um controle recebe o foco ou quando o ponteiro do mouse passa sobre o controle. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
 [Form.]Control.StatusBarText [= cExpr]
```

# Valor de retorno
 **cExpr**
Tipo de dados Character. StatusBarText especifica o texto que descreve o controle.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Grid Control | Header Object | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OptionButton Control | OptionGroup Control | PageFrame Control | Shape Control | Spinner Control | TextBox Control (Visual FoxPro)

O texto aparece na barra de status somente quando a barra de status gráfica ou a seção de status está visível.

O texto aparece na barra de status para controles que recebem foco somente quando o controle recebe o foco, independentemente de como a propriedade ShowTips do formulário está definida. O texto aparece na barra de status para controles que nunca recebem foco somente quando o mouse passa sobre o controle e a propriedade ShowTips do formulário está definida como True (.T.). Os seguintes controles nunca recebem foco:
 - CommandGroup
- OptionGroup
- Container
- Line
- Label
- Image
- Shape

Se a barra de status gráfica não estiver visível porque SET STATUS BAR está definido como `OFF`, mas a seção de status estiver visível porque SET STATUS está definido como `ON`, o texto na barra de status é exibido no centro da seção de status na parte inferior da tela.

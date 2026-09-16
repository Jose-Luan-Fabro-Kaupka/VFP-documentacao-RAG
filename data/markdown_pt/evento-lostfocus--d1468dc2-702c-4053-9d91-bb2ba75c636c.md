# Evento LostFocus

Ocorre quando um objeto perde o foco.

```foxpro
PROCEDURE Object.LostFocus
```

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | Spinner Control | TextBox Control (Visual FoxPro)

O momento em que este evento ocorre depende do tipo de objeto:
 - Um controle perde o foco por ação do usuário, como tabular para ou clicar em outro controle, ou alterando o foco em código usando o método SetFocus. Um Grid perde o foco quando um usuário pressiona CTRL+TAB no Microsoft Windows ou CONTROL+TAB no Macintosh para sair do Grid.
- Um formulário perde o foco quando o formulário não tem controles, todos os seus controles têm as propriedades Enabled e Visible definidas como false (.F.), ou outro formulário recebe o foco.

Para formulários, o evento LostFocus ocorre antes do evento Deactivate.

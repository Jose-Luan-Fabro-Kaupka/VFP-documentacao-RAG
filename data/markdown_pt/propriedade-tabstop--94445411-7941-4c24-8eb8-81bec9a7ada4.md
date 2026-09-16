# Propriedade TabStop

Especifica se um usuário pode usar a tecla TAB para mover o foco para um objeto. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Object.]Control.TabStop[ = lExpr]
```

# Valor de retorno
 **lExpr**
Especifica se um objeto está incluído na ordem de tabulação. As configurações da propriedade TabStop são as seguintes: Configuração Descrição True (.T.) (Padrão) O controle ou formulário está incluído na ordem de tabulação, conforme determinado pela propriedade TabIndex. False (.F.) O objeto é ignorado na ordem de tabulação. Para um controle, quando um usuário pressiona a tecla TAB, o foco ignora um controle cuja propriedade TabStop está definida como false (.F.). Para um formulário, quando um usuário pressiona a tecla TAB no último controle de um formulário e o próximo formulário na ordem de tabulação tem sua propriedade TabStop definida como false (.F.), o foco move para o primeiro controle no mesmo formulário. O foco não move para o próximo formulário na ordem de tabulação.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | Page Object | PageFrame Control | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

Se a propriedade TabStop estiver definida como false (.F.) para um controle ou formulário, o controle ou formulário é ignorado quando a tecla TAB é usada para percorrer a ordem de tabulação, mas ainda pode receber o foco quando o mouse é usado.

> **Observação:** Se você quiser remover um controle dentro de um controle Column da ordem de tabulação, defina a propriedade Enabled da Column como False (.F.).

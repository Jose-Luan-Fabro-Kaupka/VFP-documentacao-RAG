# Propriedade TabIndex

Especifica a ordem de tabulação dos controles em uma página e a ordem de tabulação dos formulários em um form set. Disponível em tempo de design e em tempo de execução.

```foxpro
 [Object.]Control.TabIndex[ = nOrder]
```

# Valor de retorno
 **nOrder**
Especifica a ordem de tabulação do controle.

# Observações

Aplica-se a: CheckBox Control | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Label Control (Visual FoxPro) | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | _SCREEN System Variable | Spinner Control | TextBox Control (Visual FoxPro)

Para controles em um formulário, uma ordem de tabulação é atribuída com base na ordem em que os controles são adicionados. Cada novo controle é colocado por último na ordem de tabulação.

Para um formulário em um form set, uma ordem de tabulação é atribuída com base na ordem em que o formulário foi adicionado. O formulário com nOrder definido como 1 é o primeiro formulário ativo no form set. Quando um usuário tabula do último controle em um formulário, o primeiro controle no próximo formulário na ordem de tabulação recebe o foco. Se um formulário não estiver incluído em um form set, a propriedade TabIndex é ignorada.

Você pode fazer alterações em tempo de design usando a janela Properties ou em tempo de execução usando código. No entanto, se você alterar a configuração TabIndex de um controle ou formulário, certifique-se de alterar a configuração TabIndex para todos os controles nas páginas ou formulários no form set. Se você não designar uma ordem de tabulação para todos os controles ou formulários, o Microsoft Visual FoxPro atribui a ordem de tabulação para os controles e formulários restantes com base na ordem em que são adicionados e alterados em tempo de execução, o que pode produzir resultados não intencionais.

Para ignorar a ordem de tabulação de um controle ou formulário, defina a propriedade TabStop como false (.F.).

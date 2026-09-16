# Propriedade HideSelection

Especifica se o texto selecionado aparece selecionado quando um controle perde o foco. Disponível em tempo de design e em tempo de execução.

```foxpro
Control.HideSelection[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade HideSelection são: Configuração Descrição True (.T.) (Padrão) O texto selecionado não aparece selecionado quando o controle perde o foco. False (.F.) O texto selecionado aparece selecionado quando o controle perde o foco.

# Observações

Aplica-se a: ComboBox Control | EditBox Control | Spinner Control | TextBox Control (Visual FoxPro)

Você pode usar esta propriedade para indicar o texto que está selecionado enquanto outro formulário ou uma caixa de diálogo tem o foco — por exemplo, em uma rotina de verificação ortográfica.

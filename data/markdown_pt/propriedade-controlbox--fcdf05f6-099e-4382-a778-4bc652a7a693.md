# Propriedade ControlBox

Especifica se um ícone de programa aparece no canto superior esquerdo e se os botões Minimize, Maximize, Restore e Close aparecem no canto superior direito de um formulário. No caso de Toolbars, a propriedade ControlBox controla a aparência apenas do botão Close. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.ControlBox[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade ControlBox são: Configuração Descrição True (.T.) (Padrão) Exibe um ícone de programa. False (.F.) Não exibe um ícone de programa.

# Observações

Aplica-se a: Objeto Form | Variável de sistema _SCREEN | Objeto ToolBar

Formulários modais e não modais e toolbars podem incluir um ícone de programa. Os comandos de menu disponíveis em tempo de execução dependem das configurações das propriedades relacionadas. Por exemplo, definir MaxButton e MinButton como False (.F.) desabilita os comandos de menu Maximize e Minimize no ícone do programa, mas os comandos Move e Close permanecem disponíveis.

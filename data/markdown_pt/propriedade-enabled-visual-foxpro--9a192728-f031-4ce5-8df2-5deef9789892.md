# Propriedade Enabled (Visual FoxPro)

Especifica se um objeto pode responder a eventos gerados pelo usuário. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Enabled[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Enabled são: Configuração Descrição True (.T.) (Padrão) Um objeto responde a eventos. False (.F.) Um objeto não responde a eventos.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | Page Object | PageFrame Control | _SCREEN System Variable | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | Timer Control | ToolBar Object

A propriedade Enabled permite que objetos sejam habilitados ou desabilitados em tempo de execução. Por exemplo, você pode desabilitar objetos que não se aplicam ao estado atual do aplicativo. Você também pode desabilitar um controle para restringir seu uso — por exemplo, uma caixa de edição pode ser desabilitada para exibir informações somente leitura. Se um controle estiver desabilitado, ele não pode ser selecionado.

Quando um objeto contêiner tem sua propriedade enabled definida como false (.F.), todos os controles contidos nele também são desabilitados. Se o usuário clicar em qualquer um dos controles contidos em um Form desabilitado, por exemplo, nenhum evento é disparado.

Desabilitar um controle Timer definindo Enabled como false (.F.) cancela a contagem regressiva especificada pela propriedade Interval do controle Timer.

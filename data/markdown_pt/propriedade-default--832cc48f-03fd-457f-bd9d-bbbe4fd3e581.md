# Propriedade Default

Especifica qual botão de comando ou controle OLE Container responde à tecla ENTER quando há dois ou mais botões de comando em um formulário ativo. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.Default[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Default são: Configuração Descrição True (.T.) Quando a propriedade Default do botão está definida como true (.T.) e o formulário pai está ativo, o usuário pode executar o comando do botão pressionando ENTER. (Se o foco estiver em uma caixa de edição, o usuário pode pressionar CTRL+ENTER.) Se KEYCOMP estiver definido como WINDOWS, o comando do botão padrão não é executado se o foco foi movido para outro botão de comando. Nesse caso, pressionar ENTER afeta o botão com o foco em vez do botão padrão. False (.F.) (Padrão) O botão não é o botão padrão.

# Observações

Aplica-se a: CommandButton Control | OLE Container Control

A propriedade Default só se aplica a um controle OLE Container que contém um controle ActiveX "Acts like a Button" (.ocx).

Somente um botão de comando ou controle OLE Container em um formulário pode ser o botão de comando padrão. Quando a propriedade Default é definida como true (.T.) para um botão de comando ou controle OLE Container, ela é automaticamente definida como false (.F.) para todos os outros botões de comando ou controles OLE Container no formulário. Você não pode criar um botão de comando padrão ou controle OLE Container em uma barra de ferramentas.

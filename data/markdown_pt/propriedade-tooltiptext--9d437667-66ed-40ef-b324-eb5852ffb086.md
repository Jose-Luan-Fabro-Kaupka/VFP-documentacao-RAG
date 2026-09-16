# Propriedade ToolTipText

Especifica o texto que aparece como ToolTip para um controle. Você pode definir a propriedade ToolTipText somente se a propriedade ShowTips do formulário ou barra de ferramentas que contém o controle estiver definida como True (.T.). Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Control.ToolTipText [= cExpr]
```

# Valor de retorno
 **cExpr**
Especifica o texto a usar para o ToolTip. O número máximo de caracteres que você pode especificar para cExpr é 4.095.

# Observações

Aplica-se a: Controle CheckBox | Objeto Column | Controle ComboBox | Controle CommandButton | Controle CommandGroup | Objeto Container | Objeto Control (Visual FoxPro) | Controle EditBox | Controle Grid | Objeto Header | Controle Image (Visual FoxPro) | Controle Label (Visual FoxPro) | Controle Line | Controle ListBox | Controle OLE Bound | Controle OptionButton | Controle OptionGroup | Controle PageFrame | Controle Shape | Controle Spinner | Controle TextBox (Visual FoxPro)

O Visual FoxPro suporta quebra de linha para ToolTips.

Quando você especifica a propriedade ToolTipText para controles contidos como Column, Header ou OptionButton, a propriedade ToolTipText do objeto mais interno tem precedência se o cursor do mouse se mover sobre ambos os objetos que especificam um ToolTip.

Para todos os controles contidos, exceto o controle Grid, se o objeto contido não especifica a propriedade ToolTipText, mas o contêiner sim, o Visual FoxPro não exibe um ToolTip quando o mouse se move sobre o controle contido.

Se os objetos contidos em um controle Grid não especificam a propriedade ToolTipText, mas o contêiner sim, o Visual FoxPro exibe o ToolTip do contêiner. Por exemplo, se o mouse se move sobre um objeto Header de coluna, e o Header não especifica a propriedade ToolTipText, o Visual FoxPro exibe o ToolTip da coluna.

O Visual FoxPro exibe controles dentro de uma coluna, por exemplo, um controle TextBox, que especificam a propriedade ToolTipText somente quando o controle tem foco. Se o controle não especifica um ToolTip quando tem foco, o ToolTip da coluna é exibido.

# Exemplos

Exemplo 1

As seções de código a seguir ilustram como exibir ToolTips para controles contidos que não são uma grade. O exemplo a seguir mostra como os ToolTips para o controle CommandButton e o controle CommandGroup são exibidos quando cada controle tem foco, por exemplo, quando você move o ponteiro do mouse sobre o botão de comando ou grupo de comandos.

```foxpro
CommandGroup1.ToolTipText = "Hi, I'm a CommandGroup."
CommandGroup1.Command1.ToolTipText = "Hi, I'm Command 1."
CommandGroup1.Command2.ToolTipText = "Hi, I'm Command 2."
```

Na seção de código a seguir, o ToolTip para `Command2` não é exibido quando o controle tem foco porque o ToolTip para o controle não está especificado.

```foxpro
CommandGroup1.ToolTipText = "Hi, I'm a CommandGroup."
CommandGroup1.Command1.ToolTipText = "Hi, I'm Command 1."
```

Exemplo 2

As seções de código a seguir ilustram como exibir ToolTips para controles contidos em uma grade. O exemplo a seguir mostra como o ToolTip para o controle TextBox é exibido quando o controle tem foco, por exemplo, quando você move o ponteiro do mouse sobre a caixa de texto.

```foxpro
Grid1.ToolTipText = "Hi, I'm a Grid."
Grid1.Column1.ToolTipText = "Hi, I'm a Column."
Grid1.Column1.Header1.ToolTipText = "Hi, I'm a Header."
Grid1.Column1.Text1.ToolTipText = "Hi! I'm the Textbox!"
```

Na seção de código a seguir, o ToolTip para o controle TextBox não é exibido quando o controle tem foco porque o ToolTip para a caixa de texto não está especificado.

```foxpro
Grid1.ToolTipText = "Hi, I'm a Grid."
Grid1.Column1.ToolTipText = "Hi, I'm a Column."
Grid1.Column1.Header1.ToolTipText = "Hi, I'm a Header."
```

Na seção de código a seguir, o ToolTip para a coluna aparece quando o controle Header tem foco porque o ToolTip para o cabeçalho não está especificado.

```foxpro
Grid1.ToolTipText = "Hi, I'm a Grid."
Grid1.Column1.ToolTipText = "Hi, I'm a Column."
```

Na seção de código a seguir, o ToolTip para a grade aparece quando o controle Column ou Header tem foco porque o ToolTip para a coluna ou cabeçalho não está especificado.

```foxpro
Grid1.ToolTipText = "Hi, I'm a Grid."
```

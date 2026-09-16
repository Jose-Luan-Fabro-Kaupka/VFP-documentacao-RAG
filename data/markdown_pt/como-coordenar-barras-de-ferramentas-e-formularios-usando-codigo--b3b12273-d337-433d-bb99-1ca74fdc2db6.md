# Como: coordenar barras de ferramentas e formulários usando código

Além de usar o Form Designer, você pode adicionar barras de ferramentas a conjuntos de formulários usando código.

### Para adicionar uma barra de ferramentas a um conjunto de formulários usando código
- No evento Init do conjunto de formulários, use o comando SET CLASSLIB para especificar a biblioteca que contém a classe da barra de ferramentas e, em seguida, crie uma barra de ferramentas dessa classe no conjunto de formulários.

Por exemplo, para adicionar e exibir a barra de ferramentas `tbrPrint`, baseada na classe `printing` na biblioteca de classes `inventory`, adicione o seguinte código ao evento Init do conjunto de formulários:

```foxpro
SET CLASSLIB TO inventory
THIS.AddObject("tbrPrint","printing")
THIS.tbrPrint.Show
```

> **Observação:** Se a classe da barra de ferramentas não define as ações da barra de ferramentas e de seus botões, você deve definir as ações nos procedimentos de evento associados à barra de ferramentas e aos seus botões.

Você pode definir todos os aspectos de uma barra de ferramentas em código. Por exemplo, se você adicionar o seguinte código ao evento Init de um conjunto de formulários, quando o conjunto de formulários for carregado o Visual FoxPro cria e exibe a barra de ferramentas definida no código. Essa barra de ferramentas contém dois botões.

Quando escolhidos, esses botões alteram os atributos de fonte do formulário `frmForm1` no conjunto de formulários.
 Código do evento Init do conjunto de formulários
| Código | Comentários |
| --- | --- |
| THIS.AddObject("tbrTool1","mytoolbar") THIS.tbrTool1.Show | Adiciona uma barra de ferramentas da classe mytoolbar ao conjunto de formulários atual e torna a barra de ferramentas visível. Este código está no evento Init do conjunto de formulários. |
 Código de definição da classe
| Código | Comentários |
| --- | --- |
| DEFINE CLASS myToolBar AS TOOLBAR ADD OBJECT cmdBold AS COMMANDBUTTON ADD OBJECT sep1 AS SEPARATOR ADD OBJECT cmdItalic AS COMMANDBUTTON | Início da definição da classe: uma barra de ferramentas com um botão de comando, um separador e outro botão de comando. |
| Left = 1 Top = 1 Width = 25 Caption = "Form Attributes" | Define propriedades do objeto da barra de ferramentas. |
| cmdBold.Caption = "B" cmdBold.Height = 1.7 cmdBold.Width = 10 cmdItalic.Caption = "I" cmdItalic.Height = 1.7 cmdItalic.Width = 10 cmdItalic.FontBold = .F. | Define propriedades dos controles. Observe que não há configurações de propriedade Top ou Left para controles em uma barra de ferramentas. Os controles em uma barra de ferramentas são posicionados automaticamente na ordem em que são adicionados. A propriedade FontBold de cmdItalic é definida como false (.F.) porque FontBold é true (.T.) por padrão. |
| PROCEDURE Activate THIS.cmdBold.FontBold = ; THISFORMSET.frmForm1.FontBold THIS.cmdItalic.FontItalic = ; THISFORMSET.frmForm1.FontItalic ENDPROC | Quando a barra de ferramentas é ativada, os atributos de fonte dos dois botões de comando são definidos para refletir as configurações de fonte Bold e Italic de frmForm1 . |
| PROCEDURE cmdBold.CLICK THISFORMSET.frmForm1.FontBold = ; !THISFORMSET.frmForm1.FontBold THIS.FontBold = ; THISFORMSET.frmForm1.FontBold ENDPROC | Quando o usuário clica em cmdBold , a configuração FontBold de frmForm1 é invertida e a configuração FontBold de cmdBold é definida para corresponder a ela. |
| PROCEDURE cmdItalic.CLICK THISFORMSET.frmForm1.FontItalic = ; !THISFORMSET.frmForm1.FontItalic THIS.FontItalic = ; THISFORMSET.frmForm1.FontItalic ENDPROC | Quando o usuário clica em cmdItalic , a configuração FontItalic de frmForm1 é invertida e a configuração FontItalic de cmdItalic é definida para corresponder a ela. |
| ENDDEFINE | Fim da definição da classe. |

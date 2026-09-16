# Objeto ToolBar

Cria uma barra de ferramentas personalizada.

```foxpro
ToolBar
```

# Observações

Use o objeto ToolBar para criar suas próprias barras de ferramentas para suas aplicações.

A lista a seguir descreve as propriedades de uma barra de ferramentas personalizada:
 - As barras de ferramentas ficam sempre no topo.
- As barras de ferramentas encaixam automaticamente quando são movidas para a borda da janela principal do Visual FoxPro.
- Quando as barras de ferramentas não estão encaixadas, elas têm uma barra de título de meia altura.
- Quando o tamanho de uma barra de ferramentas é alterado, os controles são reorganizados para caber.
- Você pode mover uma barra de ferramentas clicando e arrastando em qualquer área da barra de ferramentas que não seja um controle.
- Muitos controles colocados na barra de ferramentas não recebem o foco quando são escolhidos.
- Teclas de acesso em controles colocados em uma barra de ferramentas são desabilitadas.

Embora qualquer controle possa ser colocado em uma barra de ferramentas, alguns controles, como uma caixa de listagem, podem ser grandes demais para caber adequadamente em uma barra de ferramentas encaixada. Esses controles podem ser removidos programaticamente da barra de ferramentas quando ela está encaixada e substituídos por uma versão menor do mesmo controle ou por um controle diferente.

Para informações adicionais sobre como criar barras de ferramentas, consulte Designing Menus and Toolbars.

# Exemplo

O exemplo a seguir demonstra como você pode criar uma barra de ferramentas a partir da classe Toolbar. O Visual FoxPro reorganiza os botões quando a barra de ferramentas é redimensionada. Quando o objeto ToolBar é criado, o Visual FoxPro coloca automaticamente os controles da esquerda para a direita na ordem em que são adicionados à definição da classe, ignorando as propriedades Top e Left dos controles.

```foxpro
PUBLIC tbrDesktop
tbrDesktop = CREATEOBJ('myToolBar')
tbrDesktop.Show
DEFINE CLASS myToolBar AS Toolbar
   ADD OBJECT btnBold AS CommandButton
   ADD OBJECT sep1 AS Separator
   ADD OBJECT btnItalics AS CommandButton

   btnBold.Height = 20
   btnBold.Width = 50
   btnBold.Caption = "Bold"
   btnItalics.Height = 20
   btnItalics.Width = 50
   btnItalics.Caption = "Italic"
   btnItalics.FontBold = .F.

   Left = 1
   Top = 1
   Width = 25
   Caption = "Desktop Attributes"

   PROCEDURE Activate
      this.btnBold.FontBold = _SCREEN.FontBold
      this.btnItalics.FontItalic = _SCREEN.FontItalic
   ENDPROC

   PROCEDURE btnBold.Click
      _SCREEN.FontBold = !_SCREEN.FontBold
      This.FontBold =_SCREEN.FontBold
   ENDPROC

   PROCEDURE btnItalics.CLICK
      _SCREEN.FontItalic = !_SCREEN.FontItalic
      This.FontItalic = _SCREEN.FontItalic
   ENDPROC
ENDDEFINE
```

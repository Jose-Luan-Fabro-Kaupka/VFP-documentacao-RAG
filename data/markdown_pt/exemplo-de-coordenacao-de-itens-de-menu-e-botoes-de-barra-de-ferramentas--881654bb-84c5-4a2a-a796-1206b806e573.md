# Exemplo de coordenação de itens de menu e botões de barra de ferramentas

Arquivo: ...\Samples\Solution\Menus\Toolmenu.scx

Este exemplo ilustra a coordenação de itens de menu e botões de barra de ferramentas que fornecem a mesma funcionalidade.

Às vezes, você desejará tornar determinada funcionalidade acessível tanto por itens de menu quanto por botões de barra de ferramentas. Por exemplo, no Visual FoxPro você pode salvar um arquivo escolhendo o botão Salvar da barra de ferramentas ou escolhendo Salvar no menu Arquivo.

Os três componentes deste exemplo são os seguintes:

| Componente | Descrição |
| --- | --- |
| Toolmenu.scx | o formulário |
| tbrBackColor em Solution.vcx | a barra de ferramentas |
| Toolmenu.mnx | o menu |

No evento Init do formulário, um objeto de barra de ferramentas é criado cuja referência de objeto é uma propriedade no formulário, `oToolbar`.

```foxpro
SET CLASSLIB TO ..\solution
This.oToolbar = CREATEOBJECT('tbrbackcolor')
* Position the toolbar and show it
THIS.oToolbar.Left = THIS.Left + 10
THIS.oToolbar.Top = THIS.Top - 50
THIS.oToolbar.Visible = .T.
* Push the current menu on the stack so it can be
* restored in the Destroy event of the form.
PUSH MENU _MSYSMENU
* Run the menu
DO toolmenu.mpr
```

Em vez de codificar funcionalidade duplicada na barra de ferramentas e no menu, atualizando-a nos dois lugares se alterações forem necessárias, o código associado aos itens de menu chama o código associado aos botões da barra de ferramentas. Por exemplo, o seguinte comando está associado ao primeiro item de menu:

```foxpro
_VFP.ActiveForm.oToolbar.cmdRed.click
```

A cláusula SKIP FOR dos itens de menu faz com que eles sejam desabilitados quando o botão correspondente da barra de ferramentas estiver desabilitado. Por exemplo, a seguinte expressão está associada à cláusula SKIP FOR do primeiro item de menu:

```foxpro
!_VFP.ActiveForm.oToolbar.cmdRed.Enabled
```

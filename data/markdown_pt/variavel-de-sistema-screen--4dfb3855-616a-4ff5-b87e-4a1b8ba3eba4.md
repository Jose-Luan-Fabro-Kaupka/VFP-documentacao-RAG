# Variável de sistema _SCREEN

Especifica propriedades e métodos para a janela principal do Visual FoxPro. Você pode usar _SCREEN para manipular a janela principal do Visual FoxPro como um objeto. Existem duas versões da sintaxe.

```foxpro
_SCREEN.PropertyName [= eValue]
```

```foxpro
_SCREEN.MethodName
```

#### Parâmetros
 **PropertyName**
Especifica uma propriedade para a janela principal do Visual FoxPro.
**eValue**
Especifica um valor para a propriedade.
**MethodName**
Especifica um método a executar para a janela principal do Visual FoxPro.

# Observações

Você não pode criar procedimentos de eventos para _SCREEN. No entanto, você pode usar a função BINDEVENT( ) para vincular eventos de _SCREEN a outros eventos e métodos de objetos. _SCREEN é uma variável de sistema do tipo objeto.

Nas versões do Visual FoxPro 7.0 e posteriores, as propriedades Top, Height, Left, Width e hWnd de _SCREEN se aplicam apenas à área de cliente do Visual FoxPro, que é a área que pode exibir texto. Nas versões anteriores ao Visual FoxPro 7.0, as propriedades Top e Left referenciam toda a janela do aplicativo Visual FoxPro.

CLEAR WINDOWS ou RELEASE WINDOWS define a propriedade ReleaseType para _SCREEN como 1. Fechar o sistema operacional Windows define ReleaseType como 2. Para obter mais informações, consulte Comandos CLEAR e Comando RELEASE WINDOWS.

> **Observação:** O valor retornado por ReleaseType para _SCREEN pode diferir do valor retornado por ReleaseType para formulários porque é a janela principal do Visual FoxPro.

# Exemplos

O exemplo a seguir demonstra o uso de _SCREEN para personalizar a janela principal do Visual FoxPro. As linhas de código a seguir declaram variáveis locais para armazenar as configurações atuais:

```foxpro
Local oldScreenLeft
Local oldScreenTop
Local oldScreenHeight
Local oldScreenWidth
Local oldScreenColor
```

O código a seguir salva as configurações atuais da janela principal do Visual FoxPro:

```foxpro
WITH _SCREEN
 oldScreenLeft=.Left
 oldScreenTop=.Top
 oldScreenHeight=.Height
 oldScreenWidth=.Width
 oldScreenColor = .Backcolor
```

O código a seguir desabilita o redesenho da janela, altera a cor de fundo para cinza, altera o estilo da borda, define propriedades para os botões de controle da janela, torna a janela movível em tempo de execução, especifica a altura e a largura da janela, define uma legenda para a janela e habilita o redesenho da tela:

```foxpro
 .LockScreen=.T.
 .BackColor=rgb(192,192,192)
 .BorderStyle=2
 .Closable=.F.
 .ControlBox=.F.
 .MaxButton=.F.
 .MinButton=.T.
 .Movable=.T.
 .Height=285
 .Width=550
 .Caption="Custom Screen"
 .LockScreen=.F.
ENDWITH
=MESSAGEBOX("Return to normal  ",48,WTITLE())
```

O código a seguir define as propriedades da janela para suas configurações originais:

```foxpro
WITH _SCREEN
 .Left = oldScreenLeft
 .Top = oldScreenTop
 .Height = oldScreenHeight
 .Width  = oldScreenWidth
 .BackColor=oldScreenColor
 .LockScreen=.T.
 .BorderStyle=3
 .Closable=.T.
 .ControlBox=.T.
 .MaxButton=.T.
 .MinButton=.T.
 .Movable=.T.
 .Caption="Microsoft Visual FoxPro"
 .LockScreen=.F.
ENDWITH
```

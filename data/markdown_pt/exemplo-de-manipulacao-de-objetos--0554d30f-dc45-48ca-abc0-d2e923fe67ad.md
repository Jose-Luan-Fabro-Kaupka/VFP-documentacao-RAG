# Exemplo de manipulação de objetos

O exemplo a seguir define propriedades e chama código de evento de vários objetos em um conjunto de formulários. Ele inclui dois formulários, frmLeft e frmRight.
 Conjunto de formulários de exemplo no Form Designer

As duas caixas de seleção e o botão de comando de frmLeft têm código de evento associado. O nome da caixa de texto em frmLeft é `txtInput`.
 Código de evento dos objetos em LeftForm
| Objeto | Evento | Código |
| --- | --- | --- |
| chkItalic | Click | THISFORM.txtInput.FontItalic = ; THIS.Value |
| chkBold | Click | THIS.txtInput.FontBold = THIS.Value |
| cmdClear | Click | THISFORM.txtInput.Value = "" THISFORM.txtInput.FontBold = .F. THISFORM.txtInput.FontItalic = .F. THISFORM.chkItalic.Value = .F. THISFORM.chkBold.Value = .F. |

# Definindo uma propriedade de outro controle no mesmo formulário

Você pode definir as propriedades de um controle a partir do código de evento de outro usando THISFORM ou a propriedade Parent Object Reference. Os dois comandos a seguir são executados quando o usuário clica inicialmente nas caixas Italic e Bold:

```foxpro
THISFORM.txtInput.FontItalic = .T.
THIS.Parent.txtInput.FontBold = .T.
```

Neste caso, THISFORM e THIS.Parent podem ser usados alternadamente.
 Conjunto de formulários de exemplo em tempo de execução

O código do evento Click de `cmdClear` usa THISFORM para redefinir os valores dos outros controles.

# Definindo propriedades de outro formulário

Você também pode definir propriedades de um formulário a partir de outro. Form2 contém cinco botões de comando. O primeiro tem este código no evento Click:

```foxpro
THISFORMSET.frmLeft.Caption = ;
 ALLTRIM(ThisFormSet.frmLeft.txtInput.Value)
```

Observe que o conjunto e o formulário precisam ser referenciados ao definir propriedades a partir de outro formulário.
 O usuário clica no botão "Change Left Form Caption" do formulário da direita

O evento Click do segundo botão de `frmRight` demonstra como definir uma propriedade de formulário a partir de um objeto nele:

```foxpro
THISFORM.Caption = ;
 ALLTRIM(ThisFormSet.frmLeft.txtInput.Value)
```

Se o usuário escolher esse botão, Caption de frmRight mudará para o valor da caixa de texto de frmLeft.

# Acessando objetos em formulários diferentes

O código a seguir no evento Click do botão Change Bold Setting altera o valor da caixa Bold em frmLeft e chama seu código de evento.

```foxpro
THISFORMSET.frmLeft.chkBold.Value = ;
   NOT THISFORMSET.frmLeft.chkBold.Value
THISFORMSET.frmLeft.chkBold.InteractiveChange
```

A última linha chama o evento InteractiveChange de `chkBold`. Você também pode chamar esse procedimento assim:

```foxpro
THISFORMSET.frmForm1.chkBold.InteractiveChange()
```

Se a chamada for omitida, o valor da caixa muda, mas as propriedades DynamicFontBold, DynamicFontItalic, DynamicFontStrikethru e DynamicFontUnderline da caixa de texto nunca são alteradas.
 O usuário clica no botão "Change Bold Setting" do formulário da direita

# Verificando propriedades e chamando código de método de outro formulário

O código a seguir no evento Click do botão Hide Left Form oculta ou mostra frmLeft conforme o valor da propriedade Visible e altera Caption do botão:

```foxpro
IF ThisFormSet.frmLeft.Visible
   ThisFormSet.frmLeft.Hide
   THIS.Caption = "Show Left Form"
ELSE
   ThisFormSet.frmLeft.Show
   THIS.Caption = "Hide Left Form"
ENDIF
```

Observe que THIS é usado no código de evento de um controle para referenciar as propriedades do próprio controle.
 O usuário clica no botão Hide Left Form do formulário da direita

O comando a seguir no evento Click do botão Quit libera o conjunto de formulários, fechando ambos:

```foxpro
RELEASE ThisFormSet
```

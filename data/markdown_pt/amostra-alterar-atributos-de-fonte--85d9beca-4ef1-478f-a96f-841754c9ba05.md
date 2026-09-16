# Amostra Alterar Atributos de Fonte

Arquivo: ...\Samples\Solution\Toolbars\Format.scx

Este exemplo ilustra o uso de uma barra de ferramentas para definir as propriedades FontName, FontSize, FontBold, FontItalic, ForeColor e BackColor de controles em um formulário.

A barra de ferramentas é a classe tbrEditing em ...\Samples\Classes\Samples.vcx. A propriedade nAppliesTo da classe especifica se as propriedades devem ser definidas no controle atualmente selecionado, em todas as caixas de texto e caixas de edição do formulário ou em todos os controles do formulário. O código nos eventos InteractiveChange ou Click dos controles da barra de ferramentas define as propriedades. Por exemplo, o código a seguir está associado ao evento Click de cmdBold:

```foxpro
IF TYPE("_SCREEN.ActiveForm") = 'O'
   oForm = _SCREEN.ActiveForm
ELSE
   RETURN
ENDIF
DO CASE
   CASE THIS.Parent.nAppliesTo = 1   && Current Control
      oForm.ActiveControl.FontBold = THIS.Value

   CASE THIS.Parent.nAppliesTo = 2   && Text and edit boxes
      oForm.SetAll('FontBold', THIS.Value, 'TEXTBOX')
      oForm.SetAll('FontBold', THIS.Value, 'EDITBOX')
   CASE THIS.Parent.nAppliesTo = 3   && All Controls
      oForm.SetAll('FontBold', THIS.Value)
ENDCASE
```

O único código no formulário está associado ao evento GotFocus dos controles. Cada evento GotFocus contém a seguinte linha de código:

```foxpro
THISFORMSET.tbrEditing.Refresh(THIS)
```

O método Refresh de tbrEditing define os valores dos controles de edição da barra de ferramentas para refletir as configurações atuais do objeto cuja referência é passada como parâmetro.

# Exemplo Alterar páginas quando o usuário escolhe um botão

Arquivo: ...\Samples\Solution\Controls\PgFrame\Msgbox.scx

Este exemplo permite construir interativamente uma caixa de mensagem.

Há seis combinações de botões de comando possíveis em uma caixa de mensagem. Cada uma dessas combinações é exibida em uma página separada em um page frame no formulário Messagebox Builder.

Os botões de opção, rotulados de 0 a 5, permitem especificar qual combinação de botões de comando você deseja exibir em sua caixa de mensagem. O botão selecionado na página indica a seleção padrão do botão Messagebox. A propriedade ActivePage do page frame é definida para o Value do grupo de opções.

# Construindo o código MESSAGEBOX

No evento InteractiveChange dos controles no formulário, o método WriteCode do formulário é chamado para construir dinamicamente o código MESSAGEBOX.

```foxpro
* WriteCode Method
#DEFINE QM '"'
cString = '=MESSAGEBOX('
cString = cString + QM + ALLTRIM(STRTRAN(THIS.edtMessage.Value, CHR(13)+CHR(10), QM + '+CHR(13)+' + QM)) + QM + ','
cString = cString + THIS.cboIcon.Value + '+'
cString = cString + THIS.DefaultButton + '+'
cString = cString + ALLTRIM(STR(THIS.opgButtons.Value - 1)) + ','
cString = cString + QM + ALLTRIM(THIS.txtCaption.Value) + QM + ')'
THIS.edtCode.Value = cString
```

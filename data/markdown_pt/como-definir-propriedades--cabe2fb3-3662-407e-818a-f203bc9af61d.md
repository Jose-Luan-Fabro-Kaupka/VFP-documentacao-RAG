# Como: definir propriedades

Você pode definir as propriedades de um objeto em tempo de execução ou em tempo de design.

# Especificando o valor padrão de uma propriedade

Você pode definir qualquer uma das propriedades da classe base no Class Designer. Quando um objeto baseado na classe é adicionado ao formulário, o objeto reflete suas configurações de propriedade em vez das configurações de propriedade da classe base do Visual FoxPro.

> **Cuidado:** Propriedades em subclasses herdam os valores padrão de propriedade que você especifica, a menos que você escolha Reset to Default no menu de atalho da propriedade, o que redefine os valores padrão para os da classe pai.

### Para definir uma propriedade
- Use a seguinte sintaxe para definir uma propriedade de objeto programaticamente: Container . Object . Property = Value Por exemplo, as instruções a seguir definem várias propriedades de uma caixa de texto chamada txtDate em um formulário chamado frmPhoneLog : frmPhoneLog.txtDate.Value = DATE( ) && Display the current date frmPhoneLog.txtDate.Enabled = .T. && The control is enabled frmPhoneLog.txtDate.ForeColor = RGB(0,0,0) && black text frmPhoneLog.txtDate.BackColor = RGB(192,192,192) && gray background

Para as configurações de propriedade nos exemplos anteriores, `frmPhoneLog` é o objeto contêiner de nível mais alto. Se `frmPhoneLog` estivesse contido em um form set, você também precisaria incluir o form set no caminho pai:

```foxpro
frsContacts.frmPhoneLog.txtDate.Value = DATE()
```

### Para definir várias propriedades
- Use a estrutura do Comando WITH ... ENDWITH para simplificar a definição de várias propriedades.

Por exemplo, para definir várias propriedades de uma coluna em uma grade em um formulário em um form set, você poderia usar a seguinte sintaxe:

```foxpro
WITH THISFORMSET.frmForm1.grdGrid1.grcColumn1
 .Width = 5
 .Resizable = .F.
 .ForeColor = RGB(0,0,0)
 .BackColor = RGB(255,255,255)
 .SelectOnEntry = .T.
ENDWITH
```

> **Observação:** Você também pode modificar as propriedades de um objeto na Properties Window (Visual FoxPro) .

# Exemplo de uso dos controles Slider e Status Bar

Arquivo: ...\Samples\Solution\OLE\Slider.scx

Este exemplo ilustra o uso do controle Slider e do controle StatusBar.

# Controles Slider

O código no evento Scroll de cada controle slider define a propriedade Value dos outros controles.

```foxpro
#DEFINE TXT_LOC "slider value: "
THISFORM.Olecontrol2.Panels(2).Text = TXT_LOC + ALLTRIM(STR(THIS.value))
THIS.Parent.spn1.Value = THIS.Value
THIS.Parent.oleV.Value = THIS.Value
```

# Controle StatusBar

A caixa de diálogo StatusBar Control Properties facilita a configuração das propriedades da barra de status.

Para abrir a caixa de diálogo StatusBar Control Properties, escolha StatusBar Control Properties no menu de atalho de um StatusBar Control.

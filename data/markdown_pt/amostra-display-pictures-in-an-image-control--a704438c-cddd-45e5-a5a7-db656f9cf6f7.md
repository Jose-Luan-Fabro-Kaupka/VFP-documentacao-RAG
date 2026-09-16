# Amostra Display Pictures in an Image Control

Arquivo: ...\Samples\Solution\Forms\Image.scx

Esta amostra ilustra a exibição de bitmaps ou ícones em um controle image.

A list box no formulário exibe arquivos. No evento InteractiveChange da list box, a propriedade Picture do controle image é definida para o arquivo selecionado, se o arquivo for um .bmp ou .ico.

```foxpro
* lstFiles.InteractiveChange
cSelected = UPPER(THIS.List(THIS.ListIndex))
CD THIS.List(2)
IF ".BMP"$cSelected OR ".ICO"$cSelected
   THISFORM.imgDisplay.Picture = THIS.List(2) + cSelected
ENDIF
```

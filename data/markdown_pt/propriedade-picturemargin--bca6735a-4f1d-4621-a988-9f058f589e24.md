# Propriedade PictureMargin

Especifica a margem em pixels entre uma imagem conforme especificada pela propriedade Picture em um controle e a borda do controle conforme determinado pela propriedade PicturePosition. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Control.PictureMargin [= nValue]
```

# Valor de retorno
 **nValue**
Especifica o número de pixels entre uma imagem e a borda do controle. Você pode especificar um valor de 0 (padrão) a 65.535 para nValue. Quando PictureMargin é definido como 0, o posicionamento da imagem é determinado pelas propriedades PicturePosition e Alignment. Quando PictureMargin é maior que 0, a imagem aparece nValue número de pixels da borda do controle e apenas PicturePosition afeta o posicionamento da imagem. Para obter mais informações, consulte PicturePosition Property e Alignment Property.

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | OptionButton Control

PictureMargin se aplica a controles CheckBox e OptionButton quando a propriedade Style está definida como 1 (Graphical). Para obter mais informações, consulte Style Property.

PictureMargin é ignorado quando PicturePosition é definido com um valor maior que 11.

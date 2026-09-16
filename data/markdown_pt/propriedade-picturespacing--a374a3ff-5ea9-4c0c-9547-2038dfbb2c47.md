# Propriedade PictureSpacing

Especifica a margem em pixels entre a imagem especificada pela propriedade Picture e o texto especificado pela propriedade Caption em um controle. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Control.PictureSpacing [= nValue]
```

# Valor de retorno
 **nValue**
Especifica o número de pixels entre uma imagem e o texto em um controle. Você pode especificar um valor de 0 (padrão) a 65.535 para nValue . Quando PictureSpacing é definido como 0, as propriedades PicturePosition e Alignment determinam a margem entre a imagem e o controle. Quando PictureSpacing é maior que 0, o texto aparece nValue número de pixels da imagem, e as propriedades PicturePosition e Alignment afetam o posicionamento do texto no controle. PictureSpacing é ignorado quando PicturePosition é definido como um valor maior que 11. Para obter mais informações, consulte PicturePosition Property e Alignment Property .

# Observações

Aplica-se a: CheckBox Control | CommandButton Control | OptionButton Control

PictureMargin se aplica a controles CheckBox e OptionButton quando sua propriedade Style é definida como 1 (Graphical). Para obter mais informações, consulte Style Property.

# Amostra Display a System Clock

Arquivo: ...\Samples\Solution\Controls\Timer\Clock.scx

Esta amostra contém o controle personalizado Clock em Samples.vcx em um formulário. A classe inclui uma caixa de texto para exibir a data e a hora e um timer para atualizar a exibição.

A propriedade TimeFormat da classe clock pode ser definida como 0 para formato de hora de 24 horas ou 1 para formato de 12 horas. O código no evento Timer do timer atualiza a hora.

```foxpro
#DEFINE LONGDATE_LOC CDOW(DATE())+" "+CMONTH(DATE())+" "+ ;
         ALLTRIM(STR(DAY(DATE())))+", "+ALLTRIM(STR(YEAR(DATE())))
IF This.Parent.TimeFormat = 0
   This.Parent.txtTime.Value = IIF(VAL(SUBSTR(TIME(),1,2))>12, ;
      ALLTRIM(STR((VAL(SUBSTR(TIME(),1,2))-12)))+SUBSTR(TIME(),3,6),TIME())
ELSE
   This.Parent.txtTime.Value = TIME()
ENDIF
THIS.Parent.txtDate.Value = LONGDATE_LOC
```

Esta classe contém uma caixa de texto separada para valores de data e hora. Se você quiser ocultar um ou outro, pode facilmente definir sua propriedade Visible como false (.F.). Uma maneira mais fácil de exibir a hora e a data é usar uma única caixa de texto e definir o valor dessa caixa de texto em um controle timer como DATETIME( ). Isso permitirá que você aproveite as propriedades Hours, Seconds e DateFormat de uma caixa de texto.

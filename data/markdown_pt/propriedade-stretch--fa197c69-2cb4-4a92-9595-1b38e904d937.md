# Propriedade Stretch

Especifica como uma imagem é dimensionada para caber dentro de um controle. Disponível em tempo de design e em tempo de execução.

> **Observação:** Você deve definir a propriedade Picture do objeto antes de definir Stretch; caso contrário, a configuração Stretch é ignorada. Para obter mais informações, consulte Propriedade Picture.

```foxpro
 [Form.]Control.Stretch[= nType]
```

# Valor de retorno
 **nType**
Especifica um valor numérico indicando como dimensionar uma imagem para caber em um controle. A tabela a seguir contém os valores para nType. nType Descrição 0 Clip. A imagem é recortada para caber no controle. (Padrão) 1 Isométrico. A imagem é redimensionada para caber no controle mantendo suas proporções originais. 2 Stretch. A imagem é redimensionada para caber no controle, mas não mantém suas proporções originais.

# Observações

Aplica-se a: Controle Image (Visual FoxPro) | Controle OLE Bound | Controle OLE Container

# Exemplo

```foxpro
CREATE FORM myForm NOWAIT
oform=_vfp.ActiveForm
oform.ADDOBJECT("image1","image")
this1=oform.image1
this1.picture= HOME()+"\graphics\bitmaps\assorted\beanie.bmp"
this1.stretch=0
this1.height = 50
this1.width = 50
```

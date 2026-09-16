# Propriedade MaxLength

Especifica o comprimento máximo em caracteres que pode ser inserido em um controle EditBox, TextBox ou ComboBox. Para objetos XMLField, MaxLength especifica o comprimento total do campo Character ou Numeric em um cursor ao usar o método XMLTable ToCursor ou em um esquema XML ao usar o método XMLAdapter ToXML. Disponível em tempo de design e em tempo de execução. Há duas versões da sintaxe.

```foxpro
Control.MaxLength [= nMaxLength]
```

```foxpro
XMLField.MaxLength [= nMaxLength]
```

# Valor de retorno
 **nMaxLength**
Especifica o número máximo de caracteres que pode ser inserido em uma caixa de edição, caixa de texto ou caixa de combinação. Quando nMaxLength é definido como 0, não há limite para o número de caracteres que podem ser inseridos em uma caixa de edição. Para caixas de texto e de combinação, o tamanho da caixa de texto ou de combinação e seu tipo de dados determinam o número de caracteres que podem ser inseridos. Para objetos XMLField, MaxLength para campos Memo é 2147483647. Para campos Numeric , Float e Double , MaxLength é o mesmo que totalDigits+1 da faceta XML.

# Observações

Aplica-se a: controle ComboBox | controle EditBox | controle TextBox (Visual FoxPro) | classe XMLField

Para caixas de texto ou de combinação, MaxLength se aplica somente quando definido com um valor maior que 0, e o controle não usa a propriedade InputMask. Para caixas de combinação, MaxLength é significativo somente quando Style é definido como 0 e se aplica somente à porção de caixa de texto da caixa de combinação. A propriedade Value da caixa de texto deve ser do tipo Character; no entanto, a propriedade Value de uma caixa de combinação pode ser de outros tipos, como Numeric.

Se a propriedade ControlSource de um controle estiver vinculada a um campo, o Visual FoxPro trunca quaisquer caracteres inseridos que excedam o comprimento do campo.

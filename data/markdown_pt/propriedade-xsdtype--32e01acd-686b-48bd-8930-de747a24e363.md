# Propriedade XSDtype

Contém o tipo de dados XML Schema Definition (XSD) do atributo ou da base de restrição.

Os seguintes métodos XMLAdapter preenchem a propriedade XSDtype conforme apropriado:
 - LoadXML
- Attach
- AddTableSchema

Por exemplo, os tipos de dados XSD Schema xsd:int ou xs:int do XML Schema são armazenados como "int", sem seu prefixo, em XSDtype.

```foxpro
XMLField.XSDtype
```

# Valor de retorno

Tipo de dados Character. XSDtype especifica o tipo de dados XSD do atributo ou da base de restrição. Se XSDtype estiver vazio, as seguintes propriedades XMLField são ignoradas:
 - XSDmaxLength
- XSDfractionDigits
- XSDtotalDigits

# Observações

Aplica-se a: Classe XMLField

Ao gerar XML usando o método ToXML do XMLAdapter, você pode definir esta propriedade para especificar o tipo de dados XSD no esquema XSD. Você pode precisar desse comportamento quando o Visual FoxPro não suporta o valor de tipo de dados necessário para o esquema. O Visual FoxPro não valida dados nessa situação; portanto, você precisa garantir que os dados estejam em conformidade com os limites impostos pelo tipo de dados XSD especificado.

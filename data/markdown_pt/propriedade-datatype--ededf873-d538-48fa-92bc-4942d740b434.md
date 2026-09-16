# Propriedade DataType

Especifica o tipo de dados do Visual FoxPro para o campo no documento XML.

```foxpro
XMLField.DataType
```

# Valor de retorno

Tipo de dados caractere (C(1)). A propriedade DataType contém o nome de um tipo de dados do Visual FoxPro para o objeto XMLField.

# Observações

Aplica-se a: XMLField Class

Quando DataType é definido como o tipo Blob ou Varbinary, as propriedades XMLField IsBinary e NoCpTrans são definidas automaticamente como True (.T.) e a propriedade XMLField DisableEncode é definida como False (.F.). Alterações nessas propriedades não podem ser feitas quando XMLField DataType é definido como Blob ou Varbinary.

Para obter mais informações sobre o mapeamento de tipos de dados do Visual FoxPro e XML, consulte Visual FoxPro and XML Schema Data Type Mapping.

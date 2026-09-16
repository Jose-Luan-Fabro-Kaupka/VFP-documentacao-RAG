# Propriedade IsBase64

Especifica se o campo no documento XML está codificado como base64 ou hexBinary.

```foxpro
XMLField.IsBase64 [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) (Padrão) O campo está codificado como hexBinary. True (.T.) O campo está codificado como base64.

# Observações

Aplica-se a: XMLField Class

IsBase64 se aplica somente quando a propriedade IsBinary é True (.T.).

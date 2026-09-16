# Propriedade WrapMemoInCDATA

Especifica se os campos Memo devem ser encapsulados em seções CDATA.

WrapMemoInCDATA se aplica apenas ao executar os seguintes métodos XMLAdapter:
 - LoadXML
- Attach
- AddTableSchema

```foxpro
XMLAdapter.WrapMemoInCDATA [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue. lValue Descrição False (.F.) Não encapsula campos Memo em seções CDATA. (Padrão) True (.T.) Encapsula campos Memo em seções CDATA.

# Observações

Aplica-se a: XMLAdapter Class

Os métodos LoadXML, Attach e AddTableSchema do XMLAdapter usam WrapMemoInCDATA para definir a propriedade WrapInCDATA do XMLField para campos Memo.

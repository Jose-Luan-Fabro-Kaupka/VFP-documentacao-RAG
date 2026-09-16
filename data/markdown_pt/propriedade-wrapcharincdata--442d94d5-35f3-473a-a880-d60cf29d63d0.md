# Propriedade WrapCharInCDATA

Especifica se os campos de caractere devem ser encapsulados em seções CDATA.

WrapCharInCDATA se aplica somente ao executar os seguintes métodos:
 - LoadXML
- Attach
- AddTableSchema

```foxpro
XMLAdapter.WrapCharInCDATA [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados lógico. A tabela a seguir lista os valores de lValue . lValue Descrição False (.F.) Não encapsula campos de caractere em seções CDATA. (Padrão) True (.T.) Encapsula campos de caractere em seções CDATA.

# Observações

Aplica-se a: XMLAdapter Class

Os métodos LoadXML, Attach e AddTableSchema do XMLAdapter usam WrapCharInCDATA para definir a propriedade WrapInCDATA do XMLField para campos Character.

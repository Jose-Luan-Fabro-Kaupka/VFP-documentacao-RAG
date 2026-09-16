# Propriedade WrapInCDATA

Especifica se o campo é encapsulado em seções CDATA.

WrapInCDATA se aplica apenas a campos Character, Character (Binary), Memo ou Memo (Binary) e ao executar o método ToXML do XMLAdapter, que cria XML consistente com essa configuração.

```foxpro
XMLField.WrapInCDATA [= lValue]
```

# Valor de retorno

Tipo de dados lógico. O valor de WrapInCDATA assume por padrão o valor das propriedades WrapMemoInCDATA ou WrapCharInCDATA do XMLAdapter, conforme apropriado. A tabela a seguir lista os valores de lValue.

| lValue | Descrição |
| --- | --- |
| True (.T.) | O campo é encapsulado em seções CDATA. |
| False (.F.) | O campo não é encapsulado em seções CDATA. |

# Observações

Aplica-se a: Classe XMLField

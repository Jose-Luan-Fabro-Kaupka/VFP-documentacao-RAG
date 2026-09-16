# A página de código do campo "field name" não corresponde à página de código do cursor (Erro 2184)

O método ToXML da classe XMLAdapter gera este erro se a propriedade RespectCursorCP estiver definida como true (.T.), a propriedade UTF8Encoded estiver definida como false (.F.), a propriedade UseCodePage estiver definida como true (.T.), a propriedade CodePage da classe XMLField for maior que zero e não corresponder à página de código do cursor.

# A propriedade XMLName de XMLTable é uma expressão XPath (Erro 2181)

- O método ToXML da classe XMLAdapter gera este erro se a propriedade XMLNameIsXPath da classe XMLTable estiver definida como true (.T.).
- Os métodos ApplyDiffgram e ChangesToCursor da classe XMLTable geram este erro se a propriedade XMLNameIsXPath estiver definida como true (.T.).

# A propriedade XMLName do XMLAdapter é uma expressão XPath (Erro 2180)

- O método ToXML da classe XMLAdapter gera este erro se a propriedade XMLNameIsXPath Property estiver definida como true (.T.) e a propriedade XMLName Property não estiver vazia.
- Os métodos ApplyDiffgram e ChangesToCursor da classe XMLAdapter geram este erro se a propriedade XMLNameIsXPath Property estiver definida como true (.T.).
- O método ToCursor da classe XMLTable gera este erro se tanto a propriedade XMLNameIsXPath Property da classe XMLAdapter quanto a propriedade IsDiffGram Property estiverem definidas como true (.T.).

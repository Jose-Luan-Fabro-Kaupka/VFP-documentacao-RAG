# Método Nest

Aninha um objeto XMLTable em um XMLTable especificado.

```foxpro
XMLTable.Nest(oXMLTable [, oAfterXMLTable | nAfterIndex])
```

#### Parâmetros
 **oXMLTable**
Referência de objeto ao objeto XMLTable a ser aninhado.
**oAfterXMLTable**
Referência de objeto ao objeto XMLTable após o qual inserir oXMLTable.
**nAfterIndex**
Inteiro que indica qual objeto XMLTable existente inserir oXMLTable após. nAfterIndex Setting Um número menor ou igual ao número de XMLTables aninhados. oXMLTable é inserido após o objeto XLMTable no índice especificado. Um número maior que o número de tabelas aninhadas. oXMLTable é inserido como a última tabela aninhada. -1 oXMLTable é inserido como a última tabela aninhada. 0 oXMLTable é inserido como a primeira tabela aninhada. não especificado oXMLTable é inserido como a última tabela aninhada.

# Observações

Aplica-se a: XMLTable Class

O parâmetro oXMLTable e os parâmetros oAfterXMLTable devem referenciar objetos XMLTable que são membros da mesma coleção Tables do XMLAdapter.

O parâmetro nAfterTable deve ser maior ou igual a -1.

Se você remover um objeto XMLTable aninhado de uma coleção Tables do XMLAdapter, as propriedades NestedInto, NextSiblingTable e FirstNestedTable do objeto XMLTable são automaticamente definidas como null (.NULL.). Todos os seus objetos XMLTable filhos são desconectados dele, e suas propriedades NestedInto e NextSiblingTable são definidas como null (.NULL.). Os objetos filhos permanecem na coleção, mas não estão mais aninhados.

Se um objeto XMLTable estiver aninhado no momento em que o método Nest é chamado, ele é desaninhado antes que sua nova posição seja calculada.

Para obter mais informações sobre como a análise e a geração de XML são afetadas pelo aninhamento de XLMTable, consulte RespectNesting Property e XMLAdapter Class.

# Propriedade XMLName

Contém o seguinte para os objetos especificados:

XMLAdapter: XMLName contém o nome do elemento que especifica onde procurar elementos de tabela. Leitura/gravação.

Para obter mais informações sobre como os métodos LoadXML e Attach do XMLAdapter definem esta propriedade, consulte a seção Observações.

XMLTable: XMLName contém o nome do elemento dessa tabela no documento XML. Somente leitura quando associado a um objeto XMLAdapter .

XMLField: XMLName contém o nome do elemento ou atributo desse campo no documento XML. Somente leitura quando anexado a um objeto XMLTable .

```foxpro
Object.XMLName
```

# Valor de retorno

Tipo de dados Caractere. XMLName contém uma cadeia de caracteres Unicode ou está vazio ("") quando não preenchido.

> **Observação:** Antes de atribuir um valor de cadeia de caracteres a XMLName , você deve converter o valor para Unicode. Você pode usar a função STRCONV( ) para atender a esse requisito.

# Observações

Aplica-se a: classe XMLAdapter | classe XMLTable | classe XMLField

Os métodos LoadXML e Attach do XMLAdapter definem a propriedade XMLName do XMLAdapter da seguinte forma:
 - Nome do elemento ADO.NET DataSet para ADO.NET DataSet
- "data" para XML de ADO Recordset
- Cadeia de caracteres vazia ("") para Microsoft XML Data Reduced Schema (XDR) conforme usado pelo Microsoft SQL-XML

Se XMLName do XMLAdapter estiver vazio, XMLTable ToCursor procura elementos de tabela dentro do elemento referenciado pela propriedade IXMLDOMElement do XMLAdapter .

O método ToXML do XMLAdapter usa XMLName do XMLAdapter como o nome do elemento DataSet. Se XMLName estiver vazio, ToXML usa a cadeia de caracteres "VFPDataSet".

Os métodos ChangesToCursor e ApplyDiffgram do XMLTable exigem que XMLName do XMLAdapter seja definido com um valor não vazio e que o documento XML esteja no formato DiffGram.

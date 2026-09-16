# Método Attach (Visual FoxPro)

Anexa um documento DOM (Document Object Model) XML existente ou um elemento DOM e, opcionalmente, um esquema XML ao objeto XMLAdapter.

Attach também define a propriedade IXMLDOMElement do XMLAdapter. Além disso, se o esquema XML for analisado, o Visual FoxPro repopula a coleção Tables com um novo conjunto de objetos XMLTable e define as seguintes propriedades do XMLAdapter com valores apropriados:
 - XMLName
- XMLNamespace
- XMLPrefix
- IsDiffgram
- SOM

```foxpro
XMLAdapter.Attach( oDOM [, oSchema ] )
```

#### Parâmetros
 **oDOM**
Especifica um documento DOM Microsoft XML Core Services (MSXML) 4.0 existente ou um objeto IXMLDOMElement.
**oSchema**
Especifica um documento SOM (Schema Object Model) MSXML 4.0 existente, um documento DOM com um nó de esquema como elemento raiz ou um objeto IXMLDOMElement, que representa o esquema. Se você especificar um valor para oSchema, o Visual FoxPro desconsidera o valor de XMLSchemaLocation do XMLAdapter e analisa o esquema. Caso contrário, XMLSchemaLocation determina se o esquema XML é analisado.

# Observações

Aplica-se a: Classe XMLAdapter

O método Attach facilita o carregamento de resultados retornados de serviços Web, onde o conjunto de dados geralmente é retornado como dois IXMLDOMNodes com Item(0) como o esquema (oSchema) e Item(1) como os dados (oDom). Você pode anexar esses dois nós em vez de chamar LoadXML em relação a uma cadeia de caracteres.

As seguintes configurações de propriedade afetam como o método Attach é executado:
 - DisableEncode
- MapN19_4ToCurrency
- NoCpTrans
- WrapCharInCDATA
- WrapMemoInCDATA
- XMLSchemaLocation

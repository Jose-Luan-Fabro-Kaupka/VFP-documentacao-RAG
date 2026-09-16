# Propriedade IXMLDOMElement

Contém uma referência de objeto a um objeto IXMLDOMElement após a execução bem-sucedida do método LoadXML ou Attach do XMLAdapter. Os métodos do XMLAdapter operam no escopo deste objeto IXMLDOMElement.

Para obter mais informações sobre objetos IXMLDOMElement, consulte o Microsoft XML Core Services (MSXML) 4.0 SDK no site da MSDN Library em http://msdn.microsoft.com/library/.

```foxpro
XMLAdapter.IXMLDOMElement
```

# Valor de retorno

Referência de objeto. IXMLDOMElement contém uma referência de objeto a um objeto IXMLDOMElement. Quando não preenchido, IXMLDOMElement contém null (.NULL.).

# Observações

Aplica-se a: XMLAdapter Class

O método LoadXML do XMLAdapter aponta IXMLDOMElement para o elemento raiz do documento.

Se você passar um objeto XMLDOMElement como o primeiro parâmetro do método Attach do XMLAdapter, Attach atribui o elemento à propriedade IXMLDOMElement.

Se você passar um objeto IXMLDOMDocument como o primeiro parâmetro do método Attach do XMLAdapter, Attach atribui seu elemento raiz à propriedade IXMLDOMElement.

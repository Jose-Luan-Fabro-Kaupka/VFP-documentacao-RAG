# Método ReleaseXML

Libera o objeto IXMLDOMElement anexado.

```foxpro
XMLAdapter.ReleaseXML( [lDisposeSchema] )
```

#### Parâmetros
 **lDisposeSchema**
Determina se as informações de schema são limpas por ReleaseXML . A tabela a seguir lista os valores de lDisposeSchema . lDisposeSchema Descrição True (.T.) Limpa a coleção Tables e define as seguintes propriedades XMLAdapter: XMLName , XMLNamespace e XMLPrefix como uma cadeia de caracteres vazia ("") IsDiffGram como False (.F.) SOM como null (.NULL.) XMLConstraints como null (.NULL.) (Padrão) False (.F.) As informações de schema permanecem e XMLAdapter XMLName , XMLNamespace , XMLPrefix , IsDiffGram , XMLConstraints e SOM permanecem inalterados.

# Observações

Aplica-se a: XMLAdapter Class

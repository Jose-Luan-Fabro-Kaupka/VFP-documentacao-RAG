# Propriedade SOM

Contém uma referência de objeto ao documento XML Schema Object Model (SOM) (ISchema) após a execução bem-sucedida do método LoadXML ou Attach do XMLAdapter.

```foxpro
XMLAdapter.SOM
```

# Valor de retorno

Referência de objeto. SOM contém uma referência de objeto a um documento SOM ou um valor nulo (.NULL.) quando não preenchido.

# Observações

Aplica-se a: XMLAdapter Class

O SOM fornece um conjunto navegável de classes que refletem diretamente a especificação de linguagem W3C XML Schema Definition (XSD). Essas classes permitem que você percorra os elementos de um documento XML Schema e obtenha informações sobre propriedades e declarações e as relações entre elas.

Para obter mais informações sobre XML SOM ISchema, consulte a SOM Reference na referência do Microsoft XML Core Services 4.0 no site da MSDN Library em http://msdn.microsoft.com/library/.

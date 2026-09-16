# Classe XMLTable

A coleção Tables em um objeto XMLAdapter contém objetos XMLTable e descreve XML como cursores do Visual FoxPro, juntamente com quaisquer informações relacionais. Cada objeto XMLTable também pode conter um XMLTable filho e, no máximo, uma coleção Fields que contenha objetos XMLField.

```foxpro
XMLTable
```

# Observações

Para recuperar XML e decompor o XML Schema contido em um XMLTable e seus objetos XMLField correspondentes, use os métodos LoadXML ou Attach de XMLAdapter. Em seguida, você pode preencher um cursor com os dados representados pelo objeto XMLTable usando o método ToCursor de XMLTable. É possível adicionar manualmente um objeto XMLTable à coleção Tables de um XMLAdapter ou usar o método AddTableSchema de XMLAdapter para executar a mesma tarefa.

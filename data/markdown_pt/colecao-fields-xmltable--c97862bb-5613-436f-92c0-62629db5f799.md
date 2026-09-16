# Coleção Fields (XMLTable)

Cada objeto XMLTable contém, no máximo, uma única coleção Fields contendo objetos XMLField. Cada XMLField representa a estrutura de um campo significativo para o Visual FoxPro.

Quando um objeto XMLAdapter analisa XML executando seus métodos LoadXML ou Attach, ele decompõe o esquema XML contido em um ou mais objetos XMLTable e objetos XMLField correspondentes. O Visual FoxPro traduz o esquema XML de cada campo, cria objetos XMLField correspondentes e os adiciona à coleção Fields do XMLTable.

```foxpro
XMLTable.Fields
```

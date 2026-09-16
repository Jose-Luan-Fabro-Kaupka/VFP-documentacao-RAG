# O valor das propriedades XMLName, XMLNamespace ou XMLPrefix deve ser uma cadeia de caracteres Unicode. (Erro 2134)

Cadeias de caracteres não Unicode não podem ser atribuídas como valores às propriedades XMLName, XMLNamespace e XMLPrefix dos objetos XMLAdapter.
 - Use a função STRCONV( ) para converter uma cadeia de caracteres para Unicode. O código a seguir converte uma cadeia de caracteres para Unicode. oXMLTable = CREATEOBJECT("XMLTABLE") oXMLTable.XMLName = STRCONV("MyTable",12)

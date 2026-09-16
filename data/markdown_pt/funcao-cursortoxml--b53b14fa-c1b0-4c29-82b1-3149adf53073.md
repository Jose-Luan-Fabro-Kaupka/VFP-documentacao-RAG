# Função CURSORTOXML( )

Converte um cursor do Visual FoxPro em XML.

```foxpro
CURSORTOXML(nWorkArea | cTableAlias, cOutput [, nOutputFormat
[, nFlags [, nRecords [, cSchemaName [, cSchemaLocation [, cNameSpace ]]]]]])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela da qual criar a cadeia XML. Se você especificar 0 ou nenhum valor, o Visual FoxPro usa a área de trabalho atual.
**cTableAlias**
Especifica o alias da tabela da qual criar a cadeia XML.
**cOutput**
Especifica o caminho e o nome do arquivo ou o nome da variável de memória para o qual os resultados são enviados. Se nFlags estiver definido como 0 (padrão) para saída em variável de memória, o XML é retornado à variável de memória. Se a variável de memória não existir, ela é criada. Se nFlags estiver definido como 512 para saída em arquivo e o arquivo não existir, ele é criado. Se o arquivo já existir, ele é substituído. A configuração de SET SAFETY é respeitada.
**nOutputFormat**
Especifica o formato de saída da cadeia XML. A tabela a seguir lista os valores para nOutputFormat . nOuputFormat Description 1 – ELEMENTS (Default) Element-centric XML 2 – ATTRIBUTES Attribute-centric XML 3 – RAW Generic, attribute-centric XML
**nFlags**
Especifica a formatação do XML produzido e seu destino. A tabela a seguir lista os valores para nFlags . nFlags Bit Output description 0 0000 (Default) Produce XML in UTF-8 format. This setting creates a memory variable if one does not exist when specified by cOutput and returns XML to the memory variable. The XML declaration does not contain an Encoding= attribute; that is, no encoding attribute is set to UTF-8. 1 0001 Produce unformatted XML as a continuous string. 2 0010 Enclose empty elements with open and closing elements, for example, <cc04><cc04/>. 4 0100 Preserve white space in fields. 8 1000 Wrap Memo fields in CDATA sections. 16 10000 Output encoding. Output is set to the cursor code page. To ensure accurate character translation, the Visual FoxPro default code page must match the code page of the cursor. You can accomplish this by setting character and memo fields in the cursor to NOCPTRAN (character binary/memo binary). When setting this value with tables using any of the code pages, the encoding attribute in the XML is set to an empty string (""). To change to the correct encoding attribute, use the STRTRAN( ) function. For example, for code page 936, provide the following to the resulting XML string: strxml=STRTRAN(strxml, 'encoding=""', 'encoding="gb2312"' 32 100000 Output encoding. 512 1000000000 Output to the file specified by cOutput . If a file does not exist, it is created. If the file already exists, it is overwritten. The setting for SET SAFETY is observed. 4096 1000000000000 Disables base64 encoding. CURSORTOXML( ) exports Memo (Binary) fields as xsd:base64binary unless you use nFlags set to 4096. In Visual FoxPro, base64 encoding is meant for encoding only binary data. 32768 none Indicates that a code page should be used. The following table describes how the encoding attribute is written when output encoding defaults to the cursor or table code page. Note Encoding flags are set by combining bits 4 and 5 (0010000). Encoding flag Bits 4 and 5 Description +0 00 (Default) Windows-1252. +16 01 Set output encoding attribute to the cursor code page. +32 10 Set output encoding attribute to UTF-8 with no character translation. +48 11 Set output encoding attribute to UTF-8 and translate character data to UTF-8. The following table lists common Windows-compatible code pages. Code page Platform Encoding attribute in XML Declaration Comments 437 MS-DOS, US ibm437 850 MS-DOS, International ibm850 865 MS-DOS, Nordic Empty string ("") 866 MS-DOS, Russian cp866 932 Windows, Japanese shift-jis 936 Simplified Chinese gb2312 949 Windows, Korean iso-2022-kr or: ks_c_5601-1987 950 Windows, Traditional Chinese (Taiwan) big5 1250 Windows, East European Windows-1250 Note case. 1251 Windows, Russian Windows-1251 1252 Windows, U.S., West European Windows-1252 1253 Windows, Greek Windows-1253 1254 Windows, Turkish Windows-1254 1255 Windows, Hebrew Windows-1255 1256 Windows, Arabic Windows-1256 Note Visual FoxPro uses Windows-1252 as the default encoding. You can specify that the encoding attribute be set to match the code page, such as Big5 (code page 950), when using double-byte character sets (DBCS) for DBCS languages for which Visual FoxPro supports code pages. When using Windows-1252 and DBCS, no additional character translation is required to display correctly in Internet Explorer. However, to make XML more compliant for Web browsers that can interpret UTF-8, you can optionally set the encoding attribute to UTF-8 instead of Windows-1252. The result set undergoes translation to UTF-8 characters only when you set nFlags to 48 (specify the encoding attribute as UTF-8 and translate character data to UTF-8 format). This is required only when the data actually contains double-byte characters. You do not have to use character translation, STRCONV ( ) , for example, if you are outputting only Latin (single byte) characters.
**nRecords**
Especifica o número de registros a enviar para XML e tem valor padrão 0. Se nRecords for 0, todos os registros são enviados. Se nRecords for maior que o número de registros restantes na tabela, todos os registros restantes são enviados.
**cSchemaName**
Especifica o nome e o local para conter informações de esquema dos dados em cOutput , por exemplo "MySchema.xsd". Se nenhuma extensão for fornecida, o arquivo de esquema é criado com extensão .xsd. A tabela a seguir lista os valores para cSchemaName . cSchemaName Description cSchemaName Specifies the name and path of the external file for the schema (scoped to the root element of the XML). Note If cSchemaName contains a file name and cSchemaLocation is not provided or is blank, the contents of cSchemaName are written to the xsi:schemaLocation or xsi:noNamespaceSchemaLocation attribute in the XML. In the following example, Visual FoxPro generates a generic XML file named MyXMLFile.xml from the Labels.dbf file in the "Labels" alias and the schema file named MySchema in the same folder. CURSORTOXML("LABELS", "myXMLFile.xml", 1, 512, 0, "mySchema.xsd") If cSchemaName includes a URI, the schema is written to the current directory and must be uploaded to the server to be accessed by the browser or parser. External schemas always are written to the same location as the XML file. "1" Specifies an inline schema is produced. For example, the following code produces an inline schema: CURSORTOXML("LABELS", "myXMLFile.xml", 1, 512, 0, "1") "" Specifies that no schema is produced.
**cSchemaLocation**
Especifica um local opcional onde o aplicativo que lê os dados XML deve procurar o arquivo de esquema. Observação Use este parâmetro somente quando estiver implantando seu esquema em um local diferente do local dos dados XML. O conteúdo de cSchemaLocation é gravado no atributo xsi:schemaLocation ou xsi:noNamespaceSchemaLocation dos dados XML produzidos. O parâmetro cschemaLocation pode ser um endereço HTTP ou outro URI. Você precisa copiar o arquivo de esquema para o local especificado em cSchemaLocation . O exemplo a seguir produz dados XML: CURSORTOXML("LABELS", "myXMLFile.xml", 1, 512, 0, ; "mySchema.xsd", "http://www.microsoft.com/mySchema.xsd") contendo o seguinte atributo: xsi:noNamespaceSchemaLocation=" http://www.microsoft.com/mySchema.xsd" Especificar cSchemaLocation quando cSchemaName estiver em branco faz com que os mesmos atributos sejam gravados nos dados XML. Isso permite apontar para um esquema existente sem recriar o esquema cada vez que CURSORTOXML( ) é chamado.
**cNamespace**
Especifica o namespace do XML ou esquema a ser produzido e tem cadeia de caracteres vazia ("") como valor padrão. Especificar um valor para cNameSpace define o atributo targetNamespace com o mesmo valor e adiciona o atributo elementFormDefault="qualified" ao esquema. Se você não especificar um valor cNamespace e o esquema for externo, nenhuma declaração de namespace é gravada no esquema. Se você não especificar um valor cNamespace e o esquema for inline, o targetNamespace no esquema é definido como cadeia de caracteres vazia ("").

# Valor de retorno

Tipo de dados Numeric. CURSORTOXML( ) retorna o número de bytes gravados no arquivo ou em uma variável de memória.

# Observações

Você pode usar CURSORTOXML( ) com o OLE DB Provider for Visual FoxPro. Porém, a propriedade _VFP VFPXMLProgID não é suportada porque a variável de sistema _VFP não é suportada no OLE DB Provider.

> **Observação:** Para usar o Visual FoxPro OLE DB Provider com CURSORTOXML( ) , você deve instalar o MSXML 3.0 no computador com o OLE DB Provider.

A saída de CURSORTOXML( ) segue a ordem do índice do cursor, SET FIELDS TO e as configurações de filtro atuais. Porém, não preserva a posição do cursor. Após chamar CURSORTOXML( ), se todos os registros forem enviados, o ponteiro de registro do cursor indica EOF. Se não todos os registros forem enviados, ele aponta para o último registro enviado para XML.

O XML resultante de CURSORTOXML( ) contém a mesma escala da tabela exportada se a tabela contiver valores do tipo Double. Por exemplo, se uma coluna Double for criada com escala 6 usando o seguinte código, o XML resultante contém seis dígitos à direita do ponto decimal:

```foxpro
CREATE TABLE test (col1 b(6))
```

Quando você usa a função CURSORTOXML( ) para exportar uma tabela ou cursor para XML, o nó raiz é sempre chamado "VFPData", independentemente do formato de saída.

Para tipos Date apenas, você pode exportar tipos Date e DateTime "EMPTY" usando CURSORTOXML( ). Porém, a validação do esquema XML pode falhar porque "EMPTY" não é válido para esses tipos em um esquema de definição de esquema XML (XSD). Isso é um problema somente se um esquema for necessário e o XML resultante for validado contra um analisador XML que possa interpretar esquemas XSD. Para contornar esse problema, você pode precisar alterar os dados para uma representação não vazia chamando a instrução SELECT apropriada e usar CURSORTOXML( ) no cursor criado. Por exemplo, você pode alterar os valores Date ou DateTime vazios para .NULL.:

```foxpro
SELECT orderid, EVL(shippeddate,.NULL.) as ShippedDate FROM orders
```

Você também pode alterar o Date ou DateTime vazio para uma representação adequada para "empty":

```foxpro
SELECT orderid, IIF(EMPTY(shippeddate),{^1899-12-30 00:00:00},tc11);
   as ShippedDate FROM orders
```

Ao usar a flag 32768, as configurações das flags 16 e 32 podem afetar qual página de código é aplicada dependendo do tipo de dados que você está gravando em XML. As tabelas a seguir mostram as combinações possíveis de configurações e a página de código que cada combinação aplica.

Para documentos XML gravados com a flag 32768 definida, as seguintes páginas de código são aplicadas.

| Flag 16 | Flag 32 | Flag 32768 is Set |
| --- | --- | --- |
| Not set | Not set | XML documents: Window-1252. Unicode data: code page 1252. Character data: default code page, unless a field is marked as NOCPTRANS . |
| True (.T) | Not set | XML documents: Plus- CodePage property of the cursor. If XMLField CodePage property is greater than zero (0) and it doesn't match the cursor's code page, an error is reported. Unicode data: the Code page property of the cursor object. Character data: none. Raw data from the Visual FoxPro tables (.dbf) are used instead. |
| Not set | Set | XML documents: UTF-8 code page. Unicode data: UTF-8 code page. Character data: Default code page unless field is marked as NOCPTRANS , in which case no additional character translation to UTF-8 occurs. |
| Set | Set | XML documents: UTF-8 code page. Unicode data: UTF-8 code page. Character data: default code page unless a field is marked as NOCPTRANS , in which case the data are translated to UTF-8 using the SYS(3005) setting. |

Para documentos XML gravados sem definir a flag 32768, as seguintes páginas de código são aplicadas.

| Flag 16 | Flag 32 | Without the 32768 flag |
| --- | --- | --- |
| Not set | Not set | XML documents: Window-1252. Unicode data: code page 1252. Character data: default code page unless a field is marked as NOCPTRANS . |
| True (.T) | Not set | XML documents: CodePage property of the cursor. Character data: none. Raw data from the Visual FoxPro tables (.dbf) are used instead. Unicode data: code page property of the cursor object. |
| Not set | Set | XML documents: UTF-8 code page. Unicode data: UTF-8 code page. Character data: default code page unless field is marked as NOCPTRANS , in which case no additional character translation to UTF-8 occurs. |
| Set | Set | XML documents: UTF-8 code page. Unicode data: UTF-8 code page. Character data: default code page unless field is marked as NOCPTRANS , in which case, they are translated to UTF-8 using code page for the current SYS(3005) setting. |

# Propriedade VFPXMLProgID

Referencia um componente COM que você pode usar para substituir a funcionalidade interna das funções CURSORTOXML( ), XMLTOCURSOR( ) e XMLUPDATEGRAM( ).

Você pode criar o componente COM no Visual FoxPro, Visual C/C++, Visual Basic ou qualquer ferramenta de desenvolvimento que crie componentes COM com a capacidade de implementar interfaces.

```foxpro
_VFP.VFPXMLProgID [=cValue]
```

# Valor de retorno
 **cValue**
Especifica o ProgID da classe do componente COM cujas funções substituem a funcionalidade das funções XML do Visual FoxPro listadas. Definir cValue como o valor padrão de cadeia de caracteres vazia ("") redefine o uso para as implementações internas dessas funções.

# Observações

A classe que você usa deve implementar a interface IVFPXML da biblioteca de tipos do Visual FoxPro. Para fornecer métodos a substituir, abra o Object Browser no menu Tools. Da Microsoft Visual FoxPro Type Library, arraste a interface IVFPXML para um arquivo de programa (.prg).

# Exemplo

O exemplo a seguir cria classes que substituem as funções CURSORTOXML( ), XMLTOCURSOR( ) e XMLUPDATEGRAM( ). Crie um projeto para essas classes e adicione código de manipulador de função XML personalizado aos três métodos. VesrNum representa o número da versão do Visual FoxPro.

```foxpro
DEFINE CLASS MyXMLClass AS session OLEPUBLIC
   IMPLEMENTS IVFPXMLVerNum IN "VisualFoxPro.Application.VerNum"
   * Replaces CURSORTOXML().
   PROCEDURE IVFPXMLVerNum_CursorToXML(bstrAlias AS STRING, ;
      nOutputFormat AS Number, nFlags AS Number, ;
      nRecords AS Number, bstrOutputFile AS STRING, ;
      bstrSchema AS STRING, bstrSchemaLocation AS STRING, ;
      bstrNameSpace AS STRING, pVFP AS VARIANT) AS VARIANT ;
      HELPSTRING "Converts from a Cursor to XML"
      * Add user code here.
   ENDPROC
   * Replaces XMLTOCURSOR().
   PROCEDURE IVFPXMLVerNum_XMLToCursor(pvarXMLSource AS VARIANT, ;
      bstrCursorName AS STRING, nFlags AS Number, pVFP AS VARIANT) ;
      AS Number HELPSTRING "Converts from XML to a Cursor"
      * Add user code here.
   ENDPROC
   * Replaces XMLUPDATEGRAM().
   PROCEDURE IVFPXMLVerNum_XMLUpdateGramVerNum( nFlags AS Number, ;
      bstrCursorList AS STRING, pVFP AS VARIANT , ;
      bstrSchemaLocation AS STRING ) AS VARIANT;
      HELPSTRING "Generates an XML UpdateGram"
      * Add user code here.
   ENDPROC
   * Included for backward compatibility with previous
   * versions of this interface.
   PROCEDURE IVFPXMLVerNum_XMLUpdateGram(nFlags AS Number, ;
      bstrCursorList AS STRING, pVFP AS VARIANT) AS VARIANT;
      HELPSTRING "Generates an XML UpdateGram"
      * Add user code here.
   ENDPROC
ENDDEFINE
```

Quando terminar, compile o projeto em uma biblioteca de vínculo dinâmico (.dll) ou arquivo executável (.exe). Defina a propriedade VFPXMLProgID para o ProgID correto da sua classe. Por exemplo, se o nome do seu projeto é MyXMLProj, você definirá VFPXMLProgID usando a seguinte linha de código:

```foxpro
_VFP.VFPXMLProgID = "MyXMLProj.MyXMLClass"
```

Com _VFP VFPXMLProgID definido para um ProgID específico, chamadas a CURSORTOXML( ), XMLTOCURSOR( ) ou XMLUPDATEGRAM( ) são redirecionadas para o método correspondente na classe especificada por esse ProgID. Uma referência a _VFP também é passada ao método, fornecendo uma maneira de acessar e manipular cursores de dados e variáveis de memória. Para obter mais informações, consulte Propriedades, métodos e eventos da variável de sistema _VFP.

Antes do Visual FoxPro 8.0, XMLUPDATEGRAM( ) não tinha o parâmetro cSchemaLocation; portanto, a interface era diferente. O Visual Foxpro suporta ambas as interfaces e procura primeiro a interface atual. Se não for bem-sucedido, o Visual FoxPro procura a interface anterior.

O seguinte é uma definição de classe de exemplo para a interface anterior sem o parâmetro cSchemaLocation:

```foxpro
DEFINE CLASS MyXMLClass AS session OLEPUBLIC
   IMPLEMENTS IVFPXML IN "VisualFoxPro.Application.8"
   * Replaces CURSORTOXML().
   PROCEDURE IVFPXML_CursorToXML(bstrAlias AS STRING, ;
      nOutputFormat AS Number, nFlags AS Number, ;
      nRecords AS Number, bstrOutputFile AS STRING, ;
      bstrSchema AS STRING, bstrSchemaLocation AS STRING, ;
      bstrNameSpace AS STRING, pVFP AS VARIANT) AS VARIANT ;
      HELPSTRING "Converts from a Cursor to XML"
      * Add user code here.
   ENDPROC
   * Replaces XMLTOCURSOR().
   PROCEDURE IVFPXML_XMLToCursor(pvarXMLSource AS VARIANT, ;
      bstrCursorName AS STRING, nFlags AS Number, pVFP AS VARIANT) ;
      AS Number HELPSTRING "Converts from XML to a Cursor"
      * Add user code here.
   ENDPROC
   * Replaces XMLUPDATEGRAM().
   PROCEDURE IVFPXML_XMLUpdateGram(nFlags AS Number, ;
      bstrCursorList AS STRING, pVFP AS VARIANT) AS VARIANT;
      HELPSTRING "Generates an XML UpdateGram"
      * Add user code here.
   ENDPROC
ENDDEFINE
```

# Classe XMLAdapter

XMLAdapter é uma classe de "duas vias". Você pode importar XML e seu esquema contido para criar tabelas ou criar e gerar XML a partir de tabelas.

Um objeto XMLAdapter armazena referências de objeto para nós do Esquema XML e do DOM (Document Object Model). Ele não armazena informações ou conteúdo reais do esquema XML. Um objeto XMLAdapter contém uma coleção Tables com um ou mais objetos XMLTable e descreve o XML como cursores do Visual FoxPro, juntamente com todas as informações relacionais. Cada objeto XMLTable também pode conter uma XMLTable filha e, no máximo, uma coleção Fields com um ou mais objetos XMLField.

> **Observação:** A classe XMLAdapter requer Microsoft XML Core Services (MSXML) 4.0 Service Pack 1 (SP1) ou posterior.

Usando a classe XMLAdapter, você pode executar as seguintes tarefas:
 - Interpretar os seguintes formatos de esquema ao usar os métodos LoadXML e Attach de XMLAdapter: Esquemas XML do W3C (XS); Esquemas XML do W3C (XS) usados com DataSets do .NET e SQL-XML; Microsoft XML Data Reduced Schema (XDR), conforme implementado pelo SQL-XML; Esquemas de Recordset ADO. Observação: o método LoadXML de XMLAdapter pode não interpretar corretamente outros formatos de esquema XML produzidos por outros produtos.
- Recuperar o XML e seu esquema associado de uma origem XML. XMLAdapter decompõe o esquema contido em um objeto XMLTable e em seus objetos XMLField correspondentes usando os métodos LoadXML ou Attach de XMLAdapter.
- Criar um cursor baseado no esquema e preenchê-lo com os dados representados por um objeto XMLTable ao usar o método ToCursor de XMLTable.
- Representar alterações de um DiffGram do .NET em tabelas locais ou remotas ao usar o método ApplyDiffgram de XMLTable.
- Adicionar um ou mais objetos XMLTable à coleção Tables de XMLAdapter ou especificar que os métodos LoadXML, Attach ou AddTableSchema de XMLAdapter façam isso.
- Usar o método ToXML de XMLAdapter para gerar um documento XML no formato de Esquema XML do W3C a partir de um ou mais cursores ou tabelas referenciados pelo objeto XMLAdapter.

```foxpro
XMLAdapter
```

# Observações

Se você usar um objeto XMLAdapter para converter um esquema XDR em esquema XSD, deverá alterar a propriedade XMLNamespace de XMLAdapter; caso contrário, o analisador XML não poderá recarregar o XML. O exemplo a seguir ilustra esse cenário:

```foxpro
TEXT TO cXML NOSHOW
<xml xmlns:s='uuid:BDC6E3F0-6DA3-11d1-A2A3-00AA00C14882'
   xmlns:dt='uuid:C2F41010-65B3-11d1-A29F-00AA00C14882'
   xmlns:rs='urn:schemas-microsoft-com:rowset'
   xmlns:z='#RowsetSchema'>
<s:Schema id='RowsetSchema'>
   <s:ElementType name='row' content='eltOnly'>
      <s:AttributeType name='xmlfield' rs:number='1'
         rs:writeunknown='true' rs:nullable='true'>
   <s:datatype dt:type='number' rs:dbtype='currency' dt:maxLength='8'
      rs:scale='4' rs:precision='6' />
</s:AttributeType>
      <s:extends type='rs:rowbase'/>
   </s:ElementType>
</s:Schema>
<rs:data>
   <z:row xmlfield='12.12'/>
</rs:data>
</xml>
ENDTEXT
CLOSE DATABASES ALL
CLEAR
LOCAL oXMLAdapter as XMLAdapter
oXMLAdapter = NEWOBJECT('XMLAdapter')
oXMLadapter.LoadXML(cXML)
IF oXMLAdapter.Tables.Item(1).Fields.Item(1).DataType <> "Y" THEN
   ? 'Failed'
ELSE
   oXMLAdapter.Tables.Item(1).ToCursor()
   oXMLAdapter.XMLNamespace=""
   oXMLAdapter.ReleaseXML(.F.)
   oXMLAdapter.XMLSchemaLocation='c:\myxmlfile.xsd'
   oXMLAdapter.ToXML('c:\myxmlfile.xml',,.T.)
   oXMLadapter2 = NEWOBJECT('xmladapter')
   oXMLAdapter2.XMLSchemaLocation='c:\myxmlfile.xsd'
   oXMLAdapter2.LoadXML('c:\myxmlfile.xml',.T.,.T.)
ENDIF
```

Quando o esquema estiver ausente ou indisponível, você poderá especificar um esquema que o Visual FoxPro possa usar definindo a propriedade XMLSchemaLocation de XMLAdapter. Você deve especificar essa propriedade antes de chamar LoadXML. Quando o Visual FoxPro executa LoadXML, ele procura o esquema na seguinte ordem:
 - Esquema embutido
- Esquema externo conforme especificado no documento XML
- Esquema conforme especificado pela propriedade XMLSchemaLocation

O código a seguir cria um objeto XMLAdapter com uma coleção Tables que permanece vazia até que você carregue um XML válido no objeto XMLAdapter:

```foxpro
oMyAdapter=CREATEOBJECT("xmladapter")
```

Os dados XML e de esquema XML recuperados usando o método LoadXML de XMLAdapter permanecem na memória até serem substituídos por uma chamada subsequente a LoadXML ou até serem liberados especificamente quando você chama o método ReleaseXML de XMLAdapter.

Tabelas aninhadas A tabela a seguir descreve como XMLAdapter trata tabelas aninhadas como tabelas individuais ou como uma tabela inteira, dependendo da fonte de dados XML.

| Fonte de dados XML | Descrição |
| --- | --- |
| ADO.NET DataSet | XMLAdapter considera cada tabela aninhada uma tabela separada, que pode ser convertida em um cursor do Visual FoxPro. Quando o esquema XML é analisado, os métodos LoadXML e Attach de XMLAdapter criam um objeto XMLTable individual para cada tabela aninhada e o adicionam à coleção Tables. Você pode então usar os métodos ToCursor, ChangesToCursor e ApplyDiffgram de XMLTable para obter os dados de cada tabela. |
| SQL XML | XMLAdapter considera cada tabela aninhada inseparável da tabela pai. Quando os dados são recuperados, o resultado final de uma operação de junção entre essas tabelas é representado como um único resultado. Se houver vários níveis de aninhamento, como uma tabela filha contendo outra tabela filha e assim por diante, esse único resultado conterá dados de uma operação de junção entre todas as tabelas da hierarquia. Os métodos LoadXML e Attach de XMLAdapter criam objetos XMLTable para todas as tabelas. Contudo, somente o objeto XMLTable da tabela pai de nível superior é adicionado à coleção Tables. Esse objeto XMLTable representa a tabela pai e fornece acesso ao resultado único e final da operação de junção por meio do método ToCursor de XMLTable. Os objetos XMLTable das tabelas filhas são vinculados a seus pais por meio das propriedades ChildTable e ParentTable. Contudo, não há como obter dados das tabelas individuais da cadeia. |

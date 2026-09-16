# Usando VFP Report Output XML

Como entregue pelo ReportOutput Application padrão, o XML de relatório base do Visual FoxPro é transformado pela ReportListener HTML Foundation Class para fornecer uma fac-símile HTML da saída original do relatório impresso.

O XML subjacente criado pela ReportListener XML Foundation Class inclui os resultados completos de dados da execução do relatório, além de informações adicionais da tabela de relatório (.frx) necessárias para descrever o layout do relatório e as condições ambientais em vigor quando você executou o relatório.

O esquema VFP Report XML especifica o formato deste XML. Como o esquema expressa os detalhes completos de uma execução de relatório, seus aplicativos podem aproveitar o XML para fornecer muitos resultados diferentes.

Este tópico discute o esquema VFP Report XML e fornece o documento de esquema completo (.xsd).

> **Observação:** Ao explorar os detalhes deste esquema, você notará muitos elementos opcionais. A inclusão ou exclusão desses elementos ajusta o esquema para diferentes usos. Por exemplo, a ReportListener HTML Foundation Class requer informações de formatação para determinar o posicionamento de elementos de layout em uma página de saída, mas uma execução de relatório que gera um cache pesquisável de conteúdo XML não requer informações de formatação. Se você usar a ReportListener XML Foundation Class para fornecer um documento VFP Report XML, usa várias propriedades da classe para definir essas opções. Para obter mais informações, consulte ReportListener XML Foundation Class .

# Descrição do Esquema VFP Report XML

O design do documento VFP Report XML pode ser descrito amplamente da seguinte forma:

Um documento contém uma ou várias representações de execuções de VFP Report.

Cada nó VFP Report contém um ou ambos os dois possíveis nós filhos:
 - Um nó Layout ou definição de relatório (RDL), contendo as instruções de formatação do relatório armazenadas na tabela de relatório (.frx) por ferramentas de design de relatório, e/ou
- Um nó Data, com os elementos que foram gerados conforme o Report Engine percorria o escopo de dados do relatório em tempo de execução.

Quando você usa ReportListener XML Foundation Class para gerar seu XML, a classe determina qual tipo de informação está contido no nó VFP Report usando sua propriedade XMLMode, conforme especificado na tabela a seguir.

| Valor XMLMode da ReportListener XML | Constante que representa o resultado XML | Caso de uso |
| --- | --- | --- |
| 0 | OUTPUTXML_DATA_ONLY | Os dados gerados serão usados em uma apresentação não baseada no layout original do relatório, como uma página Web usando critérios de design independentes, ou para uma tradução centrada em dados (sem formatação), como um cache gerado de cálculos contábeis. |
| 1 | OUTPUTXML_RDL_ONLY | A definição de relatório gerada eventualmente residirá em um servidor de relatórios. Os dados virão de uma consulta no servidor em tempo de execução. O XML RDL serve para definir essa consulta, bem como as expressões de saída desejadas e o layout do resultado. Os dados de relatório em tempo de execução originais, neste cenário, fornecem um conjunto de amostra contra o qual o layout de relatório projetado no VFP é executado para gerar o XML, mas não são usados pelo servidor. |
| 2 | OUTPUTXML_DATA_RDL | Os dados gerados serão combinados com instruções de layout de relatório usando um mecanismo externo, como XSLT, para fornecer formas adicionais de saída. |

Se o nó VFP Report inclui os dados processados em tempo de execução junto com seu nó RDL, você pode escolher se deseja incluir dados de bandas de formatação e, se sim, se deseja que esses dados sejam integrados com as bandas de dados padrão ou incluídos como coleções separadas.

> **Observação:** O esquema define bandas de cabeçalho e rodapé de Page e Column como bandas de formatação porque ocorrem em pontos arbitrários e independentes de dados durante o processamento em tempo de execução. A saída dessas bandas, bem como os pontos exatos em que ocorrem, mudam dependendo do layout de página e do tamanho de página da impressora atual. Para alguns relatórios e alguns cenários XML, as informações nessas bandas não são relevantes.

O diagrama a seguir fornece uma visão de alto nível do VFP Report XML e seus principais componentes.

### Nó VFP-RDL

O componente de definição de relatório do VFP Report XML fornece detalhes completos das informações de layout contidas na tabela de relatório mais as condições de ambiente durante a execução do relatório, conforme detalhado na tabela abaixo.

| Elemento VFP-RDL | Conteúdo |
| --- | --- |
| VFPFRXLayoutObject | Uma junção entre colunas da tabela de relatório (.frx), colunas calculadas por FRXCursor e algumas colunas calculadas especializadas para diferentes tipos de registros da tabela de relatório. Para obter mais informações sobre os detalhes de relatório fornecidos por FRXCursor, consulte FRX Cursor Foundation Class . |
| VFPFRXLayoutNode | Um conjunto de elementos indicando quais nomes de nós de elemento são usados para diferentes tipos de objetos de relatório na porção de dados do documento, pois isso é configurável pelo usuário. |
| VFPDataSource | Uma descrição de todas as tabelas abertas na sessão de dados que fornece dados para o relatório, incluindo seus índices, relacionamentos, filtros e colunas. Esta seção é opcional. |
| VFPFRXCommand | Uma lista das cláusulas de execução REPORT FORM e condições de ambiente existentes, derivadas do membro CommandClauses do Listener e de outras configurações ambientais. Para obter mais informações, consulte Propriedade CommandClauses . |
| VFPFRXPrintJob | Um conjunto de atributos fornecendo configuração de impressora e informações de layout de página usadas para esta execução de relatório, como a altura da página. |

### Nó Data

O nó Data fornece uma sequência de bandas contendo os resultados gerados do processamento de saída que foram renderizados durante a execução do relatório. Como indicado acima, relatórios contêm dois tipos básicos de bandas:
 - Bandas dependentes de dados e escopo. Bandas de grupo e detalhe aparecem em uma ordem e em números totalmente dependentes do escopo de dados escolhido pelo usuário para este relatório. Bandas Title e Summary, se usadas, aparecem exatamente uma vez no início e no final do escopo escolhido.
- Bandas dependentes de formatação. Cabeçalhos e rodapés de Page e Column são acionados pelo Report Engine conforme os requisitos das dimensões de página do relatório original e suas interações com o comprimento de outros dados no relatório.

O conteúdo de bandas dependentes de dados e escopo sempre estará contido no nó Data. Instâncias dessas bandas aparecerão na mesma ordem em que aparecem na saída real do relatório.

Dependendo das suas especificações para bandas de formatação, esta sequência pode incluir bandas de formatação, omitir bandas de formatação inteiramente ou incluir coleções separadas de bandas de formatação, conforme mostrado no diagrama a seguir.

> **Observação:** Você pode associar bandas de formatação às suas bandas dependentes de dados e escopo usando um relacionamento id:idref, familiar para usuários do Visual FoxPro como chaves primárias e estrangeiras. Bandas dependentes de dados e escopo têm um atributo idref especificando seu número de página original, e bandas de formatação têm um atributo id especificando seu número de página original.

### Conteúdo das Bandas

Todos os tipos de bandas representam seu conteúdo renderizado da mesma forma: há um elemento filho para cada elemento de layout renderizado em cada instância de banda. Embora o diagrama a seguir detalhe uma banda de detalhe, o mesmo conteúdo de elemento poderia ser expandido para as bandas de cabeçalho e rodapé.

Os nós de elementos de layout incluem atributos opcionais para descrever sua formatação, como posição superior e esquerda na página.

> **Observação:** O esquema afirma que o processamento de atributos é lax para elementos de layout e vários outros tipos, para permitir que extensões personalizadas do esquema permaneçam válidas sem declaração explícita. Por exemplo, você poderia adicionar atributos representando ajuste dinâmico de cor em elementos de layout em tempo de execução, e esses atributos não invalidariam sua saída XML de acordo com o esquema VFP Report XML.

### Associando Elementos Data e VFP-RDL

Todas as bandas dependentes de dados e escopo, bem como elementos de layout, podem ser referenciados com suas descrições de layout baseadas na tabela de relatório usando seu atributo `id`, que contém o valor RECNO() de seu registro original na tabela de relatório. Por exemplo, o fragmento XML a seguir fornece uma instância em tempo de execução de uma banda de rodapé de página contendo dois elementos Field ou Expression e um elemento Text ou Label.

```foxpro
   <PF id="1" idref="4">
    <E id="7" c="0" l="0" t="9920" w="650" h="170">8/13/2004</E>
    <T id="8" c="0" l="6980" t="9910" w="400" h="160">Page </T>
    <E id="9" c="0" l="7380" t="9920" w="490" h="170">    1</E>
   </PF>

```

Abaixo está o nó VFPLayoutObject que descreve o layout e o design do primeiro elemento Expression nesta banda de rodapé de página. O elemento filho `frxrecno` no VFPLayoutObject abaixo corresponde ao atributo id no nó E (expression) acima.

```foxpro
    <VFPFRXLayoutObject>
     <frxrecno>7</frxrecno>
     <platform>WINDOWS</platform>
     <name/>
     <expr>DATE()</expr>
     <offset>0</offset>
     <vpos>7708.333</vpos>
     <hpos>0.000</hpos>
     <height>1875.000</height>
     <objtype>8</objtype>
     <!-- … -->
     <start_band_id>_1AI121WEG</start_band_id>
     <band_offset>2</band_offset>
     <end_band_id>_1AI121WEG</end_band_id>
     <bandstretch>false</bandstretch>
    </VFPFRXLayoutObject>

```

> **Dica:** Elementos de layout continuados em páginas subsequentes concatenam um sinal "+" aos valores de atributo id baseados em número de registro. Esta convenção significa que o nó não é uma nova instância do elemento de layout. Permite que sua análise XML considere esta informação, para concatenar texto que foi renderizado em páginas separadas na saída impressa original.

Bandas de formatação têm um relacionamento semelhante com seus registros VFPLayoutObject, mas usam seu atributo `idref` para corresponder ao valor `frxrecno` no registro VFPLayoutObject apropriado. Como explicado na última seção, essas bandas usam seu atributo id para representar o número de página original em que apareceram. No fragmento XML acima, o rodapé de página tem um valor `id` de `1`, indicando que ocorreu na primeira página, e você pode ver que os elementos de dados neste rodapé de página de fato indicam que o rodapé ocorreu na página 1 do relatório. O rodapé de página tem um `idref` de `4`, que indica que seu elemento VFPFRXLayoutObject associado tem um valor `frxrecno` de `4`.

Os nomes de nós de bandas e objetos podem ser configurados na ReportListener XML Foundation Class, para usar nomes de nós não padrão. O VFP-RDL usa elementos VFPFRXLayoutNode para associar nomes de nós a tipos de objetos da tabela de relatório dinamicamente no resultado de saída XML. No fragmento a seguir, o nome de nó `E` está associado ao tipo de objeto `8`, indicando que expressões de relatório usam este nome de elemento na porção Data do documento.

```foxpro
    <VFPFRXLayoutNode>
     <name>E</name>
     <type>8</type>
     <code>0</code>
     <info>Expression object nodename</info>
    </VFPFRXLayoutNode>

```

> **Dica:** A ReportListener XML Foundation Class inclui elementos VFPFRXLayoutNode para atributos de formatação, para que você possa atribuir dinamicamente esses nomes de atributos também. Se sua classe derivada adicionar mais atributos de formatação à sua versão do VFP Report Output XML, adicione esses atributos como propriedades da sua classe com a cadeia de caracteres " attr " como parte do nome da propriedade. A ReportListener XML Foundation Class inclui quaisquer propriedades que seguem esta convenção de nomenclatura e seus valores na lista de VFPFRXLayoutNodes e atribui um tipo de objeto distintivo.

# Documento de Esquema VFP Report XML

O seguinte é o esquema VFP Report XML completo (.xsd). O documento XSD inclui elementos de anotação descrevendo aspectos significativos deste esquema e seu uso, e direciona você a várias propriedades da ReportListener XML Foundation Class para especificar seus componentes opcionais.

> **Observação:** O esquema VFP Report XML usa nomes breves de nós XML para descrever vários elementos de relatório, como <PH> para "Page Header." A ReportListener XML Foundation Class fornece um mecanismo para alterar os nomes de nós padrão, se você preferir nomes mais longos para legibilidade ou desejar mudar para outros nomes de nós mais consistentes com uma descrição de cada elemento no seu idioma. Embora o VFP Report XML use os nomes de nós padrão, o esquema também fornece um mecanismo para descrever os nomes em uso para cada tipo de registro da tabela de relatório e outros aspectos de uma execução de relatório.

```foxpro
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xs:element name="Reports">
    <xs:annotation>
      <xs:documentation>
This schema describes the Visual FoxPro 9.0  XMLListener base delivery
format.  As noted in various places, actual element and attribute
NCNames are user-configurable at runtime, and the schema uses default
names.
As also noted, many elements of the schema are minOccurs=0.  In some
cases these elements do not appear at all depending on the
configuration of the report run or the XMLListener-specific properties
for that report run. Examples: a SUMMARY report does not have detail
bands, and if XMLListener.IncludeFormattingInLayoutObjects is .F. no
formatting attributes appear.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="VFP-Report" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFP-Report">
    <xs:annotation>
      <xs:documentation>
Contents of VFP-Report element are determined by XMLListener.XMLMode
property.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="VFP-RDL" minOccurs="0"/>
        <xs:element ref="Data" minOccurs="0"/>
            <xs:element ref="Run" minOccurs="0"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
   <xs:element name="Run">
      <xs:annotation>
         <xs:documentation>
            Allows runtime data-dependent document attributes, such as
            contents of report variables or other accumulated data
            elements that do not occur in the layout itself, to be
            added at the conclusion of a report run.
            Content type is set at xs:any deliberately to allow
            extensions such as cursor-shaped XML for rows.
         </xs:documentation>
      </xs:annotation>
      <xs:complexType mixed="true">
         <xs:sequence maxOccurs="unbounded">
            <xs:element name="property" type="VFP-Property"/>
         </xs:sequence>
      </xs:complexType>
   </xs:element>
   <xs:complexType name="VFP-Property" mixed="true">
      <xs:sequence>
         <xs:any processContents="skip" minOccurs="0" maxOccurs="unbounded"/>
      </xs:sequence>
      <xs:attribute name="id" type="xs:string" use="required"/>
      <xs:anyAttribute processContents="lax"/>
   </xs:complexType>
  <xs:element name="Data">
    <xs:annotation>
      <xs:documentation>
Contents and structure of Data element are determined by
XMLListener.includeBreaksInData property.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:choice>
        <xs:group ref="IntegratedFormattingBands"/>
        <xs:group ref="SeparateFormattingBands"/>
      </xs:choice>
    </xs:complexType>
  </xs:element>
  <xs:group name="SeparateFormattingBands">
    <xs:sequence>
      <xs:element name="Title" type="Band" minOccurs="0"/>
      <xs:group ref="GroupedBands" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Summary" type="Band" minOccurs="0"/>
      <xs:element name="Pages">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="PH" type="FormattingBand" minOccurs="0"/>
            <xs:element name="PF" type="FormattingBand" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="Columns">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="CH" type="FormattingBand" minOccurs="0"/>
            <xs:element name="CF" type="FormattingBand" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:group>
  <xs:group name="GroupedBands">
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="GH" type="Band" minOccurs="0" maxOccurs="unbounded"/>
      <xs:group ref="DetailBandSet" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="GF" type="Band" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:group>
  <xs:group name="DetailBandSet">
    <xs:sequence>
      <xs:element name="DH" type="Band" minOccurs="0"/>
      <xs:element name="D" type="Band" minOccurs="0"/>
      <xs:element name="DF" type="Band" minOccurs="0"/>
    </xs:sequence>
  </xs:group>
  <xs:group name="IntegratedFormattingBands">
    <xs:sequence>
      <xs:element name="Title" type="Band" minOccurs="0"/>
      <xs:group ref="FormattedPageBandSeries" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="Summary" type="Band" minOccurs="0"/>
    </xs:sequence>
  </xs:group>
  <xs:group name="FormattedPageBandSeries">
    <xs:sequence>
      <xs:element name="PH" type="FormattingBand" minOccurs="0"/>
      <xs:element name="CH" type="FormattingBand" minOccurs="0" maxOccurs="unbounded"/>
      <xs:group ref="GroupedBands" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="CF" type="FormattingBand" minOccurs="0" maxOccurs="unbounded"/>
      <xs:element name="PF" type="FormattingBand" minOccurs="0"/>
    </xs:sequence>
  </xs:group>
  <xs:complexType name="Band">
    <xs:annotation>
      <xs:documentation>
All bands are inherently minOccurs="0" unless
XMLListener.includeBandsWithNoObjects is .T.
Band id and idref attributes are configurable via associated
XMLListener properties.  Throughout schema, default attribute
names are shown.
      </xs:documentation>
      <xs:documentation>
All band nodenames are configurable, with defaults shown in the schema;
see annotation for VFPFRXLayoutNode name attribute.
      </xs:documentation>
    </xs:annotation>
    <xs:group ref="LayoutObjects"/>
    <xs:attribute name="id" type="xs:string" use="required">
      <xs:annotation>
        <xs:documentation>
Indicates FRXRecno for associated FRX metadata in VFP-RDL, with
concatenated "+" if this band has been continued.
      </xs:documentation>
      </xs:annotation>
    </xs:attribute>
    <xs:attribute name="idref" type="xs:positiveInteger" use="required">
      <xs:annotation>
        <xs:documentation>
Indicates the associated page number, for non-formatting bands.
      </xs:documentation>
      </xs:annotation>
    </xs:attribute>
    <!-- restriction by pattern here? -->
  </xs:complexType>
  <xs:group name="LayoutObjects">
    <xs:choice minOccurs="0" maxOccurs="unbounded">
      <xs:element name="T" type="LayoutObjectNoContinuation"/>
      <xs:element name="P" type="LayoutObjectNoContinuation"/>
      <xs:element name="S" type="LayoutObject"/>
      <xs:element name="E" type="LayoutObject"/>
      <xs:element name="L" type="LayoutObject"/>
    </xs:choice>
  </xs:group>
  <xs:complexType name="FormattingBand">
    <xs:group ref="LayoutObjects"/>
    <xs:attribute name="idref" type="xs:positiveInteger" use="required">
      <xs:annotation>
        <xs:documentation>
Indicates the FRXRecno for associated metadata, for formatting bands.
      </xs:documentation>
      </xs:annotation>
    </xs:attribute>
    <xs:attribute name="id" type="xs:positiveInteger" use="required">
      <xs:annotation>
        <xs:documentation>
Indicates the associated page number, for formatting bands.
      </xs:documentation>
      </xs:annotation>
    </xs:attribute>
  </xs:complexType>
  <xs:complexType name="LayoutObject">
    <xs:annotation>
      <xs:documentation>
All layout objects' nodenames are configurable, with defaults shown in
the schema; see annotation for VFPFRXLayoutNode name attribute.
Availability of layout objects' formatting attributes is determined by
XMLListener.IncludeFormattingInLayoutObjects property.  All attribute
names, both formatting and non-formatting, are also configurable via
XMLListener associated properties.
      </xs:documentation>
    </xs:annotation>
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="id" type="xs:string" use="required">
          <xs:annotation>
            <xs:documentation>
Indicates FRXRecno for associated FRX metadata in VFP-RDL, with
concatenated "+" if this object has been continued from a previous
page.
            </xs:documentation>
          </xs:annotation>
        </xs:attribute>
        <xs:attribute name="c" type="xs:byte" default="0"/>
        <xs:attribute name="l" type="xs:integer"/>
        <xs:attribute name="t" type="xs:integer"/>
        <xs:attribute name="w" type="xs:positiveInteger"/>
        <xs:attribute name="h" type="xs:positiveInteger"/>
        <xs:attribute name="img" type="xs:string">
          <xs:annotation>
            <xs:documentation>
Supplies generated filename if this XML is generated by HTMLListener
subclass and the image comes from a non-filebased image type (general
field or image control).
            </xs:documentation>
          </xs:annotation>
        </xs:attribute>
        <xs:anyAttribute processContents="lax"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="LayoutObjectNoContinuation">
    <xs:simpleContent>
      <xs:restriction base="LayoutObject">
        <xs:attribute name="c" fixed="0"/>
      </xs:restriction>
    </xs:simpleContent>
  </xs:complexType>
  <xs:element name="VFP-RDL">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="VFPDataSet"/>
      </xs:sequence>
      <xs:attribute name="id" type="xs:string" use="required"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPDataSet">
    <xs:complexType>
      <xs:sequence>
        <xs:element ref="VFPFRXLayoutObject" maxOccurs="unbounded"/>
        <xs:element ref="VFPFRXLayoutNode" maxOccurs="unbounded"/>
        <xs:element ref="VFPDataSource" minOccurs="0" maxOccurs="unbounded"/>
        <xs:element ref="VFPFRXCommand"/>
        <xs:element ref="VFPFRXPrintJob"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPDataSource">
    <xs:annotation>
      <xs:documentation>
The set of VFPDataSource elements represents a snapshot of the  FRX's
CurrentDataSession, similar to a FoxPro View file in XML
format.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element name="the_alias"/>
        <xs:element name="rpt_driver"/>
        <xs:element name="the_dbf"/>
        <xs:element name="the_order"/>
        <xs:element name="order_desc"/>
        <xs:element name="the_filter"/>
        <xs:element name="the_skip"/>
        <xs:element ref="flds" maxOccurs="unbounded"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPFRXCommand">
    <xs:annotation>
      <xs:documentation>
Base attributes are determined by the member properties of the
XMLListener.CommandClauses object.  Additional user-defined attributes
are permitted.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:attribute name="ASCII" type="xs:boolean" use="required"/>
      <xs:attribute name="DE_NAME" type="xs:string" use="required"/>
      <xs:attribute name="ENVIRONMENT" type="xs:boolean" use="required"/>
      <xs:attribute name="FILE" type="xs:string" use="required"/>
      <xs:attribute name="HEADING" type="xs:string" use="required"/>
      <xs:attribute name="INSCREEN" type="xs:boolean" use="required"/>
      <xs:attribute name="INWINDOW" type="xs:string" use="required"/>
      <xs:attribute name="ISDESIGNERLOADED" type="xs:boolean" use="required"/>
      <xs:attribute name="ISREPORT" type="xs:boolean" use="required"/>
      <xs:attribute name="NOCONSOLE" type="xs:boolean" use="required"/>
      <xs:attribute name="NODIALOG" type="xs:boolean" use="required"/>
      <xs:attribute name="NOEJECT" type="xs:boolean" use="required"/>
      <xs:attribute name="NOPAGEEJECT" type="xs:boolean" use="required"/>
      <xs:attribute name="NORESET" type="xs:boolean" use="required"/>
      <xs:attribute name="NOWAIT" type="xs:boolean" use="required"/>
      <xs:attribute name="OFF" type="xs:boolean" use="required"/>
      <xs:attribute name="OUTPUTTO" type="xs:byte" use="required"/>
      <xs:attribute name="PDSETUP" type="xs:boolean" use="required"/>
      <xs:attribute name="PLAIN" type="xs:boolean" use="required"/>
      <xs:attribute name="PREVIEW" type="xs:boolean" use="required"/>
      <xs:attribute name="PROMPT" type="xs:boolean" use="required"/>
      <xs:attribute name="RANGEFROM" type="xs:boolean" use="required"/>
      <xs:attribute name="RANGETO" type="xs:byte" use="required"/>
      <xs:attribute name="RECORDTOTAL" type="xs:byte" use="required"/>
      <xs:attribute name="SAMPLE" type="xs:boolean" use="required"/>
      <xs:attribute name="SUMMARY" type="xs:boolean" use="required"/>
      <xs:attribute name="TOFILE" type="xs:string" use="required"/>
      <xs:attribute name="TOFILEADDITIVE" type="xs:boolean" use="required"/>
      <xs:attribute name="WINDOW" type="xs:string" use="required"/>
      <xs:anyAttribute processContents="lax"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPFRXLayoutNode">
    <xs:annotation>
      <xs:documentation>
Provides metadata specific to XMLListener's base XML
format.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name">
          <xs:annotation>
            <xs:documentation>
Indicates the current nodename as defined in the XMLListener's
configuration table, for elements, or as an XMLListener property, for
attributes.  Names used for layout objects and band types in the Data
portion of this schema represent only the default values for these
nodenames; for readability and localization purposes these nodenames
are configurable and should be looked up from the VFPFRXLayoutNode
portion of the VFP-RDL at runtime.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="type">
          <xs:annotation>
            <xs:documentation>
Matches FRX.objtype for this nodename
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="code">
          <xs:annotation>
            <xs:documentation>
Matches FRX.objcode for this nodename
      </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="info">
          <xs:annotation>
            <xs:documentation>
      Description of this type of node from XMLListener's configuration
table (for elements) or a matching XMLListener member property (for
attributes).
            </xs:documentation>
          </xs:annotation>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPFRXLayoutObject">
    <xs:annotation>
      <xs:documentation>
Provides metadata specific to the FRX format, using FRX columns
directly as well as derived columns from FRXCursor helper object and
other sources.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
    <xs:element name="frxrecno"/>
    <xs:element name="platform"/>
    <xs:element name="name"/>
    <xs:element name="expr"/>
    <xs:element name="offset"/>
    <xs:element name="vpos"/>
    <xs:element name="hpos"/>
    <xs:element name="height"/>
    <xs:element name="objtype"/>
    <xs:element name="tag"/>
    <xs:element name="tag2"/>
    <xs:element name="pensize"/>
    <xs:element name="penpat"/>
    <xs:element name="fillpat"/>
    <xs:element name="width"/>
    <xs:element name="style"/>
    <xs:element name="picture"/>
    <xs:element name="order"/>
    <xs:element name="comment"/>
    <xs:element name="fillchar"/>
    <xs:element name="penred"/>
    <xs:element name="pengreen"/>
    <xs:element name="penblue"/>
    <xs:element name="fillred"/>
    <xs:element name="fillgreen"/>
    <xs:element name="fillblue"/>
    <xs:element name="fontface"/>
    <xs:element name="fontstyle"/>
    <xs:element name="fontsize"/>
    <xs:element name="mode"/>
    <xs:element name="float"/>
    <xs:element name="stretch"/>
    <xs:element name="stretchtop"/>
    <xs:element name="fontbold"/>
    <xs:element name="fontitalic"/>
    <xs:element name="fontunderline"/>
    <xs:element name="fontstrikethrough"/>
    <xs:element name="unpathedimg"/>
    <xs:element name="pathedimg"/>
    <xs:element name="top"/>
    <xs:element name="bottom"/>
    <xs:element name="norepeat"/>
    <xs:element name="pagebreak"/>
    <xs:element name="colbreak"/>
    <xs:element name="resetpage"/>
    <xs:element name="general"/>
    <xs:element name="spacing"/>
    <xs:element name="swapheader"/>
    <xs:element name="swapfooter"/>
    <xs:element name="ejectbefor"/>
    <xs:element name="ejectafter"/>
    <xs:element name="totaltype"/>
    <xs:element name="resettotal"/>
    <xs:element name="fontcharset"/>
    <xs:element name="supalways"/>
    <xs:element name="supovflow"/>
    <xs:element name="suprpcol"/>
    <xs:element name="supgroup"/>
    <xs:element name="supvalchng"/>
    <xs:element name="supexpr"/>
    <xs:element name="user"/>
    <xs:element name="bandid" minOccurs="0"/>
    <xs:element name="bandtype" minOccurs="0"/>
    <xs:element name="bandlabel" minOccurs="0"/>
    <xs:element name="start" minOccurs="0"/>
    <xs:element name="stop" minOccurs="0"/>
    <xs:element name="band_seq" minOccurs="0"/>
    <xs:element name="rel_band_id" minOccurs="0"/>
    <xs:element name="objid" minOccurs="0"/>
    <xs:element name="objname" minOccurs="0"/>
    <xs:element name="locale_id" minOccurs="0"/>
    <xs:element name="start_band_id" minOccurs="0"/>
    <xs:element name="band_offset" minOccurs="0"/>
    <xs:element name="end_band_id" minOccurs="0"/>
    <xs:element name="bandstretch" minOccurs="0"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="VFPFRXPrintJob">
    <xs:annotation>
      <xs:documentation>
Provides information specific to this report execution run as available
in the VFP environment.  These elements determine formatting
coordinates for instances of the layout objects as the Report Engine
calculates their placement during the report run.
      </xs:documentation>
    </xs:annotation>
    <xs:complexType>
      <xs:attribute name="pagewidth" type="xs:short" use="required"/>
      <xs:attribute name="pageheight" type="xs:short" use="required"/>
      <xs:attribute name="name" type="xs:string" use="required">
        <xs:annotation>
          <xs:documentation>
Provided by XMLListener.PrintJobName.
          </xs:documentation>
        </xs:annotation>
      </xs:attribute>
      <xs:attribute name="pagedesign" type="xs:string" use="required"/>
      <xs:attribute name="printresolution" type="xs:short" use="required"/>
    <xs:anyAttribute processContents="lax"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="flds">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="the_alias">
          <xs:annotation>
            <xs:documentation>
            Repeated on the field level for use with SET FIELDS GLOBAL.
            </xs:documentation>
          </xs:annotation>
        </xs:element>
        <xs:element name="the_field"/>
        <xs:element ref="the_type"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="the_type">
    <xs:annotation>
      <xs:documentation>
      Derived from AFIELDS(), matches VFP codes for various table-based
datatypes.
      </xs:documentation>
    </xs:annotation>
    <xs:simpleType>
      <xs:restriction base="xs:string">
        <xs:enumeration value="C"/>
        <xs:enumeration value="Y"/>
        <xs:enumeration value="D"/>
        <xs:enumeration value="T"/>
        <xs:enumeration value="B"/>
        <xs:enumeration value="F"/>
        <xs:enumeration value="G"/>
        <xs:enumeration value="I"/>
        <xs:enumeration value="L"/>
        <xs:enumeration value="M"/>
        <xs:enumeration value="N"/>
        <xs:enumeration value="Q"/>
        <xs:enumeration value="V"/>
        <xs:enumeration value="W"/>
      </xs:restriction>
    </xs:simpleType>
  </xs:element>
</xs:schema>

```

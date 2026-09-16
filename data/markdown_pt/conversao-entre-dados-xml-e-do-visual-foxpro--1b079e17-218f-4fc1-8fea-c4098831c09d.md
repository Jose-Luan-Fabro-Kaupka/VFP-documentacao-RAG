# Conversão entre dados XML e do Visual FoxPro

Você pode trocar dados com mais facilidade com outros aplicativos convertendo dados do Visual FoxPro para o formato XML. O Visual FoxPro inclui as seguintes funções para que você possa converter dados entre os formatos XML e Visual FoxPro:
 - Função CURSORTOXML( )
- Função XMLTOCURSOR( )
- Função XMLUPDATEGRAM( )

> **Observação:** Você deve ter o analisador Microsoft XML Core Services (MSXML) instalado para poder usar as funções XML do Visual FoxPro.

As seções a seguir abordam considerações sobre a conversão entre dados XML e do Visual FoxPro:
 - Processamento de dados XML em variáveis ou cadeias de caracteres em vez de arquivos
- Conversão de cadeias de caracteres XML
- Importação e exportação de XML usando esquemas

Você pode substituir a funcionalidade interna das funções CURSORTOXML( ), XMLTOCURSOR( ) e XMLUPDATEGRAM( ) fazendo referência a um componente COM por meio da propriedade VFPXMLProgID. Para obter mais informações, consulte Propriedade VFPXMLProgID.

O Visual FoxPro oferece suporte a XML formatado hierarquicamente para os formatos XML DiffGram e ADO.NET DataSet do .NET Framework por meio das classes XMLAdapter, XMLTable e XMLField. Para obter mais informações, consulte Funcionalidade XML usando XMLAdapters.

# Processamento de dados XML em variáveis ou cadeias de caracteres em vez de arquivos

XMLTOCURSOR( ) processa dados de forma diferente quando eles vêm de uma variável ou cadeia de caracteres e quando vêm de um arquivo. Ao converter XML em um cursor, o método usado para passar o XML à função afeta o tratamento dos caracteres de conjuntos de caracteres de byte duplo (DBCS) no XML. Os caracteres DBCS são interpretados corretamente quando um arquivo é usado como XMLSource. No entanto, se você precisar usar uma variável de memória ou cadeia de caracteres, poderá forçar a interpretação como DBCS usando o seguinte código em XMLTOCURSOR( ):

```foxpro
STRCONV(string,11)
```

O exemplo a seguir abre a tabela de exemplo Customer do Visual FoxPro localizada no diretório ..\Samples\Data\ do Visual FoxPro, converte os dados da tabela Customer e salva os dados da tabela como XML em uma variável de memória, lcXML:

```foxpro
CLEAR
CLOSE DATABASES ALL
USE HOME()+'samples\data\customer'
CURSORTOXML('customer','lcXML',1,48,5,"","","")
```

A linha a seguir insere caracteres incorretos no cursor resultante:

```foxpro
XMLTOCURSOR(lcXML,"curCustomerList",4)
```

A linha a seguir usa a função STRCONV( ), converte corretamente o XML em dados DBCS e abre uma janela de navegação para a tabela:

```foxpro
XMLTOCURSOR(STRCONV(lcXML,11),"curCustomerList",4)
BROWSE
```

# Conversão de cadeias de caracteres XML

XMLTOCURSOR( ) não realiza conversões automáticas de cadeias de caracteres XML, por exemplo, de ANSI para UTF-8. Isso pode ocorrer ao ler uma cadeia de caracteres XML de um arquivo. Para realizar uma conversão, use a função STRCONV( ).

O exemplo a seguir demonstra o erro de análise que ocorre quando o Visual FoxPro encontra o primeiro caractere ASCII:

```foxpro
CLOSE DATABASE ALL
USE HOME(2)+"\data\customer"
CURSORTOXML("customer","lcXML",1,32)
STRTOFILE(lcXML,"customer.xml")
XMLTOCURSOR("customer.xml","curCustomer",512)
RETURN
```

Você pode evitar o erro de análise gerado convertendo a cadeia de caracteres para UTF-8 quando o XML é gravado ou quando é gravado no arquivo. O exemplo a seguir converte a cadeia de caracteres para UTF-8 à medida que ela é gravada no arquivo, usando a função STRCONV( ) com a função STRTOFILE( ):

```foxpro
CLOSE DATABASE ALL
USE HOME(2)+"\data\customer"
CURSORTOXML("customer","lcXML",1,32)
STRTOFILE(STRCONV(lcXML,9),"customer.xml")
XMLTOCURSOR("customer.xml","curCustomer",512)
RETURN
```

No exemplo, você pode usar o valor 48 para o parâmetro nFlag na função STRCONV( ) para criar o XML codificado como UTF-8. No entanto, isso não funciona para XML fornecido por uma origem externa nem para XML que não tenha sido gerado com a função CURSORTOXML( ).

Para obter mais informações, consulte Função STRCONV( ).

# Importação e exportação de XML usando esquemas

Quando você importa XML usando a função XMLTOCURSOR( ), o Visual FoxPro usa um esquema externo ou interno, se disponível, para determinar a estrutura do cursor ou da tabela antes de fazer uma única passagem para converter os dados. Quando nenhum esquema é fornecido, o Visual FoxPro faz duas passagens pelos dados XML: a primeira determina a estrutura dos dados da melhor forma possível e a segunda realiza a conversão. Em geral, além de ser bem formado, o XML deve estar em conformidade com um formato que possa ser interpretado como uma tabela. Um XML bem formado que não possa ser decomposto facilmente em um formato de tabela não será importado.

Veja a seguir um exemplo de esquema XSD gerado pela função CURSORTOXML( ) do Visual FoxPro:

```foxpro
<?xml version = "1.0" encoding="Windows-1252" standalone="yes"?>
<xsd:schema id="VFPSchema" targetNamespace="http://microsoft.com" xmlns="http://microsoft.com" xmlns:xsd="http://www.w3.org/2000/10/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" elementFormDefault="qualified">
   <xsd:element name="atxm">
      <xsd:complexType>
         <xsd:all>
            <xsd:element name="ikey" minOccurs="0" type="xsd:int"/>
            <xsd:element name="nc00" minOccurs="0">
               <xsd:simpleType>
                  <xsd:restriction base="xsd:decimal">
                     <xsd:precision value="10"/>
                     <xsd:scale value="4"/>
                  </xsd:restriction>
               </xsd:simpleType>
            </xsd:element>
            <xsd:element name="mc03" minOccurs="0">
               <xsd:simpleType>
                  <xsd:restriction base="xsd:string">
                     <xsd:maxLength value="2147483647"/>
                  </xsd:restriction>
               </xsd:simpleType>
            </xsd:element>
            <xsd:element name="cc04" minOccurs="0">
               <xsd:simpleType>
                  <xsd:restriction base="xsd:string">
                     <xsd:maxLength value="128"/>
                  </xsd:restriction>
               </xsd:simpleType>
            </xsd:element>
            <xsd:element name="lc05" minOccurs="0" type="xsd:boolean"/>
            <xsd:element name="fc06" minOccurs="0" type="xsd:double"/>
            <xsd:element name="yc07" minOccurs="0" type="xsd:decimal"/>
            <xsd:element name="ic08" minOccurs="0" type="xsd:int"/>
            <xsd:element name="bc09" minOccurs="0" type="xsd:double"/>
            <xsd:element name="dc10" minOccurs="0" type="xsd:date"/>
            <xsd:element name="tc11" minOccurs="0"
type="xsd:timeInstant"/>
            <xsd:element name="ts12" minOccurs="0">
               <xsd:simpleType>
                  <xsd:restriction base="xsd:binary">
                     <xsd:encoding value="base64"/>
                  </xsd:restriction>
               </xsd:simpleType>
            </xsd:element>
         </xsd:all>
      </xsd:complexType>
   </xsd:element>
   <xsd:element name="VFPData" msdata:lsDataSet="true">
      <xsd:complexType>
         <xsd:choice maxOccurs="unbounded">
            <xsd:element ref="atxm"/>
         </xsd:choice>
      </xsd:complexType>
   </xsd:element>
</xsd:schema>
```

Atualmente, o Visual FoxPro exporta XML nos seguintes formatos:
 - Centrado em elementos Cada campo de um cursor ou tabela resultante ou de origem é representado por um subelemento do elemento de nível superior. <?xml version="1.0" encoding="Windows-1252" standalone="yes" ?> <!-- Observe targetNamespace no elemento raiz (VfpData). Se definido como padrão (""), o atributo xmlns não será gravado --> <VfpData xmlns="http://www.microsoft.com"> <alltypesxm> <ikey>2</ikey> <nc00>1.1111</nc00> <mc03>H1111111111111111111</mc03> <cc04>H111111111111111111</cc04> <lc05>true</lc05> <fc06>-1111000</fc06> <yc07>-111111111.1111</yc07> <ic08>-11111111</ic08> <bc09>-111111111111.1</bc09> <dc10>1999-03-02T08:00:00</dc10> <tc11>1999-03-02T09:01:01</tc11> <ts12>AAAAAAAAAr8=</ts12> </alltypesxm> </VfpData>
- Centrado em atributos O cursor é identificado pela palavra-chave "VFPData", e cada campo de um cursor ou tabela resultante ou de origem é representado por um atributo do elemento VFPData. <?xml version="1.0" encoding="Windows-1252" ?> <!-- Observe targetNamespace no elemento raiz --> <VFPData xmlns="http://www.microsoft.com"> <atxm_attr ikey="2" nc00="12345.1111" mc03="H1111111111111111111" cc04="H111111111111111111" lc05="1" fc06="-1111000.0000" yc07="-111111111.1111" ic08="-11111111" bc09="-111111111111.100000" dc10="1999-03-02" tc11="1999-03-02T01:01:01" ts12="AAAAAAAAAr0=" /> <atxm_attr ikey="3" nc00="2.1111" mc03="H2222222222222222222" cc04="H222222222222222222" lc05="1" fc06="22220000.0000" yc07="2222222222.2222" ic08="222222222" bc09="222222222222.2200000" tc11="2000-10-03T02:02:02" ts12="AAAAAAAAAr8=" /> </VFPData>
- Bruto Cada linha de um cursor ou tabela resultante ou de origem é representada por um elemento XML com o identificador genérico " row", e cada valor de coluna é mapeado para um atributo do elemento row cujo nome é igual ao nome da coluna. Esse formato é idêntico ao centrado em atributos, exceto por "row" como nome do elemento de nível superior. <?xml version="1.0"?> <!-- Observe que não há targetNamespace no elemento raiz --> <VFPData> <row CustomerID="CACTU" CompanyName="Cactus Comidas para llevar" ContactName="Patricio Simpson" ContactTitle="Sales Agent" Address="Cerrito 333" City="Buenos Aires" PostalCode="1010" Country="Argentina" Phone="(1) 135-5555" Fax="(1) 135-4892"/> </VFPData>

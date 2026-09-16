# Propriedade XMLConstraints

Contém uma referência de objeto ao objeto ISchemaItemCollection após a execução bem-sucedida do método LoadXML ou Attach do XMLAdapter.

Se os métodos LoadXML e Attach analisarem o esquema XML, eles definem XMLConstraints para o valor apropriado, embora o Visual FoxPro não analise nem aplique nenhuma restrição declarada na coleção XMLConstraints.

```foxpro
Object.XMLConstraints
```

# Valor de retorno

Referência de objeto. XMLConstraints contém uma referência de objeto ao objeto ISchemaItemCollection ou um valor nulo (.NULL.) quando não preenchido.

# Observações

Aplica-se a: XMLAdapter Class | XMLTable Class

O esquema XML pode conter restrições, que estão associadas ao esquema. XMLConstraints fornece acesso a restrições definidas no elemento DataSet.

O Visual FoxPro não inclui nenhuma funcionalidade no XMLAdapter que use essas restrições, mas fornece acesso para que você possa obter informações de restrições e usá-las em sua aplicação, se necessário.

No exemplo XML a seguir, observe a localização da restrição Primary Key:

```foxpro
<?xml version="1.0" encoding="Windows-1252"?>
<DataSet xmlns="http://tempuri.org/">
<xs:schema id="NewDataSet" xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
<xs:element name="NewDataSet" msdata:IsDataSet="true">
   <xs:complexType>
      <xs:choice maxOccurs="unbounded">
         <xs:element name="Tbl2">
            <xs:complexType>
               <xs:sequence>
                  <xs:element name="source"/>
                  <xs:element name="num" type="xs:int"/>
                  <xs:element name="xdtime" type="xs:dateTime"/>
                  <xs:element name="xlog" type="xs:boolean"/>
               </xs:sequence>
            </xs:complexType>
         </xs:element>
      </xs:choice>
   </xs:complexType>
   <xs:unique name="Constraint1" msdata:PrimaryKey="true">
      <xs:selector xpath=".//Tbl2"/>
      <xs:field xpath="source"/>
   </xs:unique>
</xs:element>
</xs:schema>
<diffgr:diffgram xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns:diffgr="urn:schemas-microsoft-com:xml-diffgram-v1">
<NewDataSet xmlns="">
   <Tbl2 diffgr:id="Tbl21" msdata:rowOrder="0">
      <source>Buckner             </source>
      <num>9</num>
      <xdtime>2002-04-03T00:00:00.0000000-08:00</xdtime>
      <xlog>true</xlog>
   </Tbl2>
</NewDataSet>
   </diffgr:diffgram>
</DataSet>
```

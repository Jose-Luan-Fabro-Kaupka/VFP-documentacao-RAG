# Propriedade ChildTable

Contém uma referência de objeto a um objeto XMLTable filho. Leitura/gravação.

```foxpro
XMLTable.ChildTable
```

# Valor de retorno

Referência de objeto. ChildTable contém uma referência de objeto a um objeto XMLTable filho e null (.NULL.) quando não preenchido.

# Observações

Aplica-se a: XMLTable Class

Para tabelas aninhadas em SQL XML, o Visual FoxPro preenche a propriedade ChildTable com informações sobre as tabelas aninhadas envolvidas na operação de join. No entanto, XMLAdapter não atribui a propriedade ChildTable ao trabalhar com ADO.NET DataSets. Para obter mais informações sobre como XMLAdapter trata tabelas aninhadas para fontes de dados ADO.NET DataSet e SQL XML, consulte XMLAdapter Class.

# Exemplo

O exemplo a seguir ilustra como um objeto XMLAdapter trata a tabela `Orders` como tabela filha da tabela `Customers` e a tabela `Order_details` como tabela filha da tabela `Orders`.

```foxpro
<?xml version="1.0" encoding="utf-8"?>
<SqlXmlAdoData>
   <Schema name="Schema1" xmlns="urn:schemas-microsoft-com:xml-data" xmlns:dt="urn:schemas-microsoft-com:datatypes">
      <ElementType name="Customers" content="eltOnly" model="closed" order="many">
         <element type="Orders" maxOccurs="*"/>
         <element type="CustomerID"/>
         <element type="CompanyName"/>
      </ElementType>
      <ElementType name="CustomerID" content="textOnly" model="closed" dt:type="string"/>
      <ElementType name="CompanyName" content="textOnly" model="closed" dt:type="string"/>
      <ElementType name="Orders" content="eltOnly" model="closed" order="many">
         <element type="Order_details" maxOccurs="*"/>
         <element type="OrderID"/>
         <element type="OrderDate"/>
         <element type="ShipName"/>
      </ElementType>
      <ElementType name="OrderID" content="textOnly" model="closed" dt:type="i4"/>
      <ElementType name="OrderDate" content="textOnly" model="closed" dt:type="dateTime"/>
      <ElementType name="ShipName" content="textOnly" model="closed" dt:type="string"/>
      <ElementType name="Order_details" content="eltOnly" model="closed" order="many">
         <element type="ProductID"/>
         <element type="UnitPrice"/>
         <element type="Quantity"/>
      </ElementType>
      <ElementType name="ProductID" content="textOnly" model="closed" dt:type="i4"/>
      <ElementType name="UnitPrice" content="textOnly" model="closed" dt:type="fixed.14.4"/>
      <ElementType name="Quantity" content="textOnly" model="closed" dt:type="i2"/>
   </Schema>
   <Customers xmlns="x-schema:#Schema1">
      <CustomerID>CACTU</CustomerID>
      <CompanyName>Cactus Comidas para llevar</CompanyName>
      <Orders>
         <OrderID>10521</OrderID>
         <OrderDate>1997-04-29T00:00:00</OrderDate>
         <ShipName>Cactus Comidas para llevar</ShipName>
         <Order_details>
            <ProductID>35</ProductID>
            <UnitPrice>18</UnitPrice>
            <Quantity>3</Quantity>
         </Order_details>
         <Order_details>
            <ProductID>41</ProductID>
            <UnitPrice>9.65</UnitPrice>
            <Quantity>10</Quantity>
         </Order_details>
         <Order_details>
            <ProductID>68</ProductID>
            <UnitPrice>12.5</UnitPrice>
            <Quantity>6</Quantity>
         </Order_details>
      </Orders>
   </Customers>
</SqlXmlAdoData>
```

# Exemplo Load and Generate XML Using the XMLAdapter Class

Arquivo: ...\Samples\Solutions\Toledo\XMLAdapter.scx

Você pode usar a classe XMLAdapter para criar vários cursors a partir de XML, como ADO.NET DataSets, e, inversamente, gerar XML a partir de vários cursors.

Este exemplo demonstra alguns dos muitos usos da classe XMLAdapter, como selecionar um arquivo XML para criar cursors ou gerar XML a partir de várias tabelas.

Para obter mais informações, consulte XMLAdapter Class.

# Carregando XML

Neste exemplo, você pode carregar um XML DataSet em um objeto XMLAdapter clicando em Load XML na guia XMLTables e selecionando um arquivo XML válido, como um gerado a partir de um ADO.NET DataSet ou outro objeto XMLAdapter. O evento Click do botão Load XML contém o código a seguir que usa o método LoadXML do XMLAdapter:

```foxpro
ThisForm.oXMLAdapter.LoadXML(cFilename, .T.)
```

O nome do arquivo que você seleciona é passado como o primeiro parâmetro ao método LoadXML. O segundo parâmetro de LoadXML indica que o primeiro parâmetro é um arquivo; caso contrário, assume que o primeiro parâmetro é uma variável que contém a cadeia de caracteres XML.

Depois de selecionar um arquivo, a coleção Tables do XMLAdapter é preenchida com tantos objetos XMLTable quantas forem as tabelas no XML DataSet, que você pode usar para gerar cursors.

# Adicionando tabelas

Neste exemplo, você pode adicionar tabelas e gerar XML selecionando Add Table na guia XMLTables, selecionando uma tabela e clicando em To XML.

Quando você seleciona Add Table, aparece uma lista de tabelas Northwind para que você possa selecionar uma ou mais tabelas. Depois de abrir uma tabela, a tabela é adicionada ao objeto XMLAdapter usando o método AddTableSchema da seguinte forma:

```foxpro
USE ? SHARED IN 0
cTable = LOWER(ALIAS())
ThisForm.oXMLAdapter.AddTableSchema(cTable)
```

# Gerando XML

Neste exemplo, você pode gerar XML depois de adicionar tabelas ao objeto XMLAdapter e definir quaisquer propriedades adicionais na guia XMLAdapter Properties.

Para gerar XML, selecione To XML na guia XMLTables, que chama o método ToXML do XMLAdapter:

```foxpro
ThisForm.oXMLAdapter.ToXML(XML_FILENAME,, .T., ;
ThisForm.tabXMLAdapter.Page1.chkBefore.Value, ;
ThisForm.tabXMLAdapter.Page1.chkChangesOnly.Value)
```

Em ToXML, deixar o segundo parâmetro em branco indica que o schema deve ser gerado inline. O terceiro parâmetro indica se o primeiro parâmetro é o nome de um arquivo (True - .T.) ou uma variável (False - .F.).

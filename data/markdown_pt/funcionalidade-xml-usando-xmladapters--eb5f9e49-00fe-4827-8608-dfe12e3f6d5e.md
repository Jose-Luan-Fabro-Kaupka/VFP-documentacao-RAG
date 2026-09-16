# Funcionalidade XML usando XMLAdapters

O Visual FoxPro aprimora seus recursos XML existentes e sua compatibilidade com os formatos XML DiffGram e ADO.NET DataSet do .NET Framework fornecendo as classes XMLAdapter, XMLTable e XMLField. Com essas classes, o Visual FoxPro suporta XML formatado hierarquicamente para o seguinte:
 - Arquivos XML que têm esquema associado, inline ou externo, conforme implementado por ADO.NET DataSets baseados no .NET Framework. Para obter mais informações, consulte ADO.NET DataSets .
- Microsoft XML Data Reduced Schema (XDR) conforme usado pelo Microsoft SQL XML
- Esquemas ADO Recordset que são produzidos quando um ADO Recordset é salvo como XML em um arquivo ou stream

O Visual FoxPro pode fatorar um arquivo XML representando uma coleção de tabelas diferentes e possivelmente relacionadas, como um objeto ADO.NET DataSet, em cursors separados do Visual FoxPro. Geralmente, este arquivo contém dados de um sistema de gerenciamento de banco de dados (DBMS) com a estrutura Parent > Child > Child. O XML também pode ter um formato aninhado como Parent > Child, Parent > Child, ou um formato serial como Parent-Parent, Child-Child.

Quando você tem XML hierárquico que representa uma única tabela resultante de um comando SQL JOIN de várias tabelas, o Visual FoxPro cria apenas um cursor.

> **Observação:** As classes XMLAdapter , XMLTable e XMLField requerem Microsoft XML Core Services (MSXML) 4.0 Service Pack 1 (SP1). Para obter mais informações sobre essas classes, consulte Classe XMLAdapter , Classe XMLTable e Classe XMLField . Para obter mais informações sobre MSXML, consulte Microsoft XML Core Services 4.0 SP1 no site da MSDN Library em http://msdn.microsoft.com/downloads/ .

> **Observação:** Esquema XML Schema Definition (XSD) conforme gerado por ADO.NET DataSets do Visual Studio pode conter elementos não suportados pelo Visual FoxPro. Para obter mais informações, consulte Suporte para esquemas gerados por ADO.NET DataSets .

# ADO.NET DataSets

No .NET Framework, ADO.NET é um conjunto de classes que expõem serviços de acesso a dados ao programador. ADO.NET fornece acesso consistente a fontes de dados como Microsoft SQL Server e outras fontes de dados expostas por OLE DB e XML.

O ADO.NET DataSet é usado como a classe principal para manipular dados e encapsula dados como XML. Um objeto ADO.NET DataSet pode produzir XML de várias maneiras:
 - Retornando o ADO.NET DataSet inteiro ao aplicativo chamador. Este método retorna todas as linhas na consulta original em formato XML DiffGram com esquema inline e operações de atualização, inserção e exclusão conforme indicado. Linhas que permanecem inalteradas não têm o atributo diffgr:hasChanges. Quando um objeto DataSet retorna ao aplicativo chamador de um método em um aplicativo que usa o .NET Framework e retorna objetos ADO.NET DataSet, ele é sempre serializado, ou convertido, em XML. O Visual FoxPro pode converter este XML em cursors, que você pode então manipular em um aplicativo Visual FoxPro.
- Retornando apenas alterações ao ADO.NET DataSet ao aplicativo baseado em .NET. Este método retorna apenas aquelas linhas, em formato XML DiffGram, que foram modificadas, adicionadas ou excluídas. Se o objeto ADO.NET DataSet contiver alterações, elas são marcadas com os atributos DiffGram:hasChanges="modified" ou DiffGram:hasChanges="inserted" . Para registros marcados como "modified" , os valores anteriores aparecem na seção diffgr:before . Registros excluídos aparecem apenas na seção diffgr:before e não na seção principal do DiffGram.
- Usando os métodos GetXml e GetXMLSchema do ADO.NET DataSet para retornar XML como um tipo stream ou string .CLR.
- Usando os métodos WriteXml e WriteXmlSchema do ADO.NET DataSet para gravar o ADO.NET DataSet como XML em um arquivo com esquema inline, sem esquema ou com esquema separado.

Para obter mais informações sobre formatos XML DiffGram e ADO.NET DataSet, consulte o .NET Framework SDK no site da MSDN Library em http://msdn.microsoft.com/library/.

# Suporte para esquemas gerados por ADO.NET DataSets

XML que tem esquema XML Schema Definition (XSD) externo ou inline conforme gerado por ADO.NET DataSets pode conter elementos não suportados pelo Visual FoxPro, que desconsidera esses elementos. Por exemplo, esses elementos podem incluir o seguinte:
 - xs:unique name
- xs:annotation
- Instruções de processamento e atributos adicionais como os seguintes: Suporte a prefixo de esquema, como msdata:Prefix, que define o escopo de um grupo de elementos Suporte a prefixo XML, como o atributo vfpx, que delimita o prefixo aos elementos raiz Atributo msprop e outros atributos que usam este namespace Outros atributos msdata que referenciam itens não suportados pelo Visual FoxPro, como msdata:Locale ou msdata:Comment

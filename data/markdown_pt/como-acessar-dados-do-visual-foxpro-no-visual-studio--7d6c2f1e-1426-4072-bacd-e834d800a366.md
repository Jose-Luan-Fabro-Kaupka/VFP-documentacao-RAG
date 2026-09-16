# Como: acessar dados do Visual FoxPro no Visual Studio

Você pode acessar bancos de dados e tabelas do Visual FoxPro no Visual Studio usando o Provedor OLE DB do Visual FoxPro. O Provedor OLE DB do Visual FoxPro está disponível por meio do Visual Studio Server Explorer ou usando cadeias de conexão em código.

# Acessando fontes de dados do Visual FoxPro usando o Visual Studio Server Explorer

Você pode acessar bancos de dados e tabelas do Visual FoxPro no Visual Studio adicionando-os à lista de conexões de dados que aparecem no painel Visual Studio Server Explorer. Você precisa primeiro especificar uma conexão por meio do Provedor OLE DB do Visual FoxPro para os bancos de dados e tabelas desejados. Você pode então selecionar os bancos de dados ou tabelas para que apareçam no painel Visual Studio Server Explorer.

> **Observação:** Você deve ser capaz de especificar o banco de dados ou pasta de tabela do Visual FoxPro que deseja acessar fornecendo o caminho e o nome do arquivo ou navegando até ele.

### Para conectar a um banco de dados ou tabela do Visual FoxPro por meio do Provedor OLE DB do Visual FoxPro
- Abra o Visual Studio.
- No menu View, selecione Server Explorer.
- No painel Server Explorer, clique com o botão direito em Data Connections e clique em Add Connection.
- Na caixa de diálogo Data Link Properties, clique na guia Provider.
- Selecione Microsoft OLE DB Provider for Visual FoxPro. A guia Connection na caixa de diálogo Data Link Properties aparece.

### Para adicionar um banco de dados ou tabela do Visual FoxPro
- Na guia Connection e na caixa Select or enter a database name, digite o caminho e o nome do banco de dados ou pasta de tabela desejado. -ou- Para procurar um banco de dados ou pasta de tabela do Visual FoxPro, clique no botão de reticências ( ... ) à direita da caixa Select or enter a database name para abrir a caixa de diálogo Configure Connection.
- Especifique uma sequência de ordenação diferente, se desejado.
- Para testar a conexão, clique em Test Connection. Se a conexão for bem-sucedida, clique em OK.

O banco de dados ou diretório de tabela especificado aparece no painel Visual Studio Server Explorer abaixo do nó Data Connections.

# Acessando fontes de dados do Visual FoxPro usando cadeias de conexão

Para acessar uma fonte de dados do Visual FoxPro em código, use uma cadeia de conexão válida para especificar o Provedor OLE DB do Visual FoxPro, fonte de dados ou nome da fonte de dados. Por exemplo, você pode acessar o Provedor OLE DB do Visual FoxPro usando código do Visual FoxPro.

Você também pode especificar um Nome de Fonte de Dados ODBC (DSN) existente do Visual FoxPro em vez de uma fonte de dados. O Provedor usa a fonte de dados indicada no DSN e a expande para uma cadeia de conexão apropriada do Provedor.

### Para conectar ao Provedor OLE DB do Visual FoxPro no Visual FoxPro
- Estabeleça um objeto Connection ActiveX Data Object (ADO) e crie um objeto de dados no Visual FoxPro.
- Especifique o Provedor OLE DB do Visual FoxPro e a fonte de dados em uma cadeia de conexão conforme mostrado no código a seguir: oConn = CREATEOBJECT("ADODB.Connection") oConn.ConnectionString = "provider=vfpoledb.1;; data source=.\ MyTestDatabase .dbc" oConn.Open

Este código cria um objeto de dados que você pode usar para recuperar dados.

> **Observação:** Certifique-se de substituir MyTestDatbase pelo nome de banco de dados apropriado.

Em vez de uma fonte de dados, você pode usar um nome de fonte de dados Open Database Connectivity (ODBC) existente (DSN) na cadeia de conexão para o Provedor OLE DB do Visual FoxPro. O Provedor OLE DB do Visual FoxPro aceita o argumento `DSN = cDSNName` e usa a fonte de dados especificada pelo DSN conforme mostrado no exemplo a seguir:

```foxpro
oConn=CREATEOBJECT("adodb.connection")
oConn.ConnectionString="Provider=vfpoledb;DSN=ODBCdataSourceName"
oConn.Open()
```

> **Observação:** Certifique-se de substituir ODBCdataSourceName pelo DSN ODBC apropriado, por exemplo, vfpTestData.

Após a conexão ser aberta, você pode consultar o valor de `ConnectionString` para determinar a fonte de dados avaliada.

Uma cadeia de conexão inclui as seguintes palavras-chave e valores de atributo:
 **Provider= cVFPOLEDBProvider**
Especifica o Provedor OLE DB do Visual FoxPro (VFPOLEDB).
**Data Source= cPath**
Especifica o caminho para o banco de dados do Visual FoxPro ou uma pasta contendo tabelas livres. Por exemplo, c:\Microsoft Visual FoxPro\Samples\Data\Testdata.dbc
**DSN= cDSNName**
Especifica um DSN ODBC existente.
**Mode= cMode**
Especifica um dos seguintes: Read, ReadWrite, Share Deny None (padrão), Share Deny Read, Share Deny Write ou Share Exclusive, que inclui os dois modos anteriores.

Para uma explicação completa da sintaxe de cadeia de conexão, consulte o Microsoft OLE DB 2.5 Programmer's Reference and SDK Guide.

# Atualizando dados do Visual FoxPro

Você pode atualizar dados do Visual FoxPro por meio do Provedor OLE DB do Visual FoxPro usando ADO. O procedimento a seguir descreve três maneiras de atualizar dados do Visual FoxPro usando dados do banco de dados de exemplo Northwind, localizado no diretório Visual FoxPro ..\Samples\Northwind.

> **Observação:** Certifique-se de substituir NorthWind.dbc pelo banco de dados que deseja usar.

### Para atualizar dados do Visual FoxPro por meio do Provedor OLE DB do Visual FoxPro usando ADO
- Chame um comando update, insert ou delete diretamente. Para chamar um comando update diretamente, use o método Execute do ADO. Por exemplo: CLEAR LOCAL oConn as "adodb.connection" LOCAL oRS as "adodb.recordset" oConn = CREATEOBJECT('adodb.connection') oRS = CREATEOBJECT('adodb.recordset') cConnStrng = ; "Provider=vfpoledb;Data Source="+HOME(2)+"Northwind\Northwind.dbc" oConn.Open(cConnStrng) oConn.BeginTrans() oConn.Execute("UPDATE Customers SET contactname = 'Patricio X. Simpson'; WHERE customerid='CACTU'") oRS = oConn.Execute("SELECT * FROM customers WHERE customerid = 'CACTU'") ?oRS.Fields("contactname").Value oConn.RollbackTrans() oRS.Requery() ?oRS.Fields('contactname').Value oRS.Close() oConn.Close() -ou-
- Use um cursor de cliente. Por exemplo: CLEAR LOCAL oConn as "adodb.connection" LOCAL oRS as "adodb.recordset" oConn = CREATEOBJECT('adodb.connection') oRS = CREATEOBJECT('adodb.recordset') cConnStrng = ; "Provider=vfpoledb;Data Source="+HOME(2)+"Northwind\Northwind.dbc" oConn.CursorLocation= 3 && adUseClient oConn.Open(cConnStrng) *!* Open RecordSet using keyset cursor and optimistic locking. oRS.Open(; "SELECT * FROM customers WHERE customerid = 'CACTU'",oConn,1,3,1) ? 'Current value:',oRS.Fields("contactname").Value oRS.Fields("contactname").Value = "Patricio X. Simpson" oRS.Update() oRS.Requery() ? 'New value:',oRS.Fields("contactname").Value oRS.Close() oConn.Close() -ou-
- Use um cursor de servidor. Por exemplo: LOCAL oRS as "adodb.recordset" oConn = CREATEOBJECT('adodb.connection') oRS = CREATEOBJECT('adodb.recordset') cConnStrng = ; "Provider=vfpoledb;Data Source="+HOME(2)+"Northwind\Northwind.dbc" oConn.Open(cConnStrng) *!* Updatable server cursors must use the USE command to *!* open the table, not a SELECT statement. Server cursor is updatable, *!* opened keyset, and lock optimistic. oRS.Open("USE customers",oconn,1,3,1) ? 'CursorLocation:',IIF(oRS.CursorLocation=2,"adUseServer","adUseClient") * Find CACTU. ? oRS.Find("customerid='CACTU'") ? 'Current value:',oRS.Fields("contactname").Value oRS.Fields("contactname").Value = "Patricio Simpson" oRS.Update() oRS.Requery() oRS.Find("customerid='CACTU'") ? 'New value:',oRS.Fields("contactname").Value oRs.Close() oRS ='' oConn.Close()oConn=''

# Acessando dados do Visual FoxPro de diferentes linguagens

Você pode acessar o Provedor OLE DB do Visual FoxPro de outras linguagens usando diferentes cadeias de conexão, dependendo da linguagem. Por exemplo, para conectar a um banco de dados do Visual FoxPro de um aplicativo Visual C#, você pode usar a seguinte cadeia de conexão, substituindo `myVFPDatabase` pelo nome de fonte de dados apropriado:

```foxpro
oleDbConnection1.ConnectionString = "Provider=VFPOLEDB.1;" +
   "Data Source=C:\\myVFPDatabase.DBC;";
```

Os exemplos de código a seguir ilustram como usar cadeias de conexão que especificam o Provedor OLE DB do Visual FoxPro e a fonte de dados ao acessar dados do Visual FoxPro de diferentes linguagens.

> **Observação:** Certifique-se de substituir myVFPDatabase pela fonte de dados ou DSN apropriado.

### Para acessar uma fonte de dados do Visual FoxPro em Visual C#
- Use uma cadeia de conexão para especificar o Provedor OLE DB do Visual FoxPro e acessar a fonte de dados conforme mostrado no código a seguir: OleDbConnection oleDbConnection1 = new OleDbConnection("Provider=VFPOLEDB.1;" + "Data Source=C:\\ myVFPDatabase .DBC;"); oleDbConnection1.Open();

### Para acessar uma fonte de dados do Visual FoxPro em Visual Basic
- Use uma cadeia de conexão para especificar o Provedor OLE DB do Visual FoxPro e a fonte de dados conforme mostrado no código a seguir, onde oConnection representa um objeto Connection ADO: oConnection.Open("Provider=vfpoledb.1; Data Source=.\ myVFPDatabase .dbc")

### Para acessar dados do Visual FoxPro usando ActiveX Data Objects (ADO) em Visual Basic
- Use uma cadeia de conexão para especificar o Provedor OLE DB do Visual FoxPro e a fonte de dados conforme mostrado no código a seguir: Imports System.Data.OleDb Public Class ConnectToVFP Public Function ADONETOpenVFPDatabase() As Boolean Dim bIsConnected As Boolean = True Try Dim cnn As New OleDbConnection("Provider=VFPOLEDB.1;" + _ "Data Source=.\ MyTestDatabase .dbc;") cnn.Open() Catch e As System.Exception bIsConnected = False End Try Return bIsConnected End Function End Class Observação Certifique-se de substituir MyTestDatabase pelo nome do banco de dados ou diretório de tabela que deseja acessar.

### Para acessar uma fonte de dados do Visual FoxPro em Visual C++
- Defina as propriedades do banco de dados especificando a matriz DBSetProp, a matriz DBProp e o ponteiro IDBProperties, seguido de uma cadeia de conexão que especifica o Provedor OLE DB do Visual FoxPro conforme mostrado no código a seguir: HRESULT hr; CLSID clsid; // Set the DBProp array. DBPROP iProp[1]; DBPROPSET rgIP; IDBProperties* pIDBProperties = NULL; IDBInitialize *pIDBInitialize = NULL; VariantInit(&iProp[0].vValue); iProp[0].dwOptions = DBPROPOPTIONS_OPTIONAL; // Required iProp[0].colid = DB_NULLID; // Set the location of data source. iProp[0].dwPropertyID = DBPROP_INIT_DATASOURCE; iProp[0].vValue.vt = VT_BSTR; iProp[0].vValue.bstrVal = L"c:\ myVFPDatabase .dbc"; // Data source // Set DBpropset to point to the DBPROP array. rgIP.guidPropertySet = DBPROPSET_DBINIT; rgIP.cProperties = 1; rgIP.rgProperties = iProp; ::CoInitialize(NULL); hr = CLSIDFromProgID(L"vfpoledb.1",&clsid); // Specify OLE DB Provider. hr = CoCreateInstance(clsid, NULL, CLSCTX_INPROC_SERVER, IID_IDBInitialize, (void**)&pIDBInitialize); // Initialize. hr = piDBInitialize->QueryInterface(_uuidof(IDBProperties), (void**)&pIDBProperties); hr = pIDBProperties->SetProperties(1 , &rgIP) ; hr = pIDBProperties->Release(); hr = pIDBInitialize->Initialize();

### Para acessar uma fonte de dados do Visual FoxPro em ASP usando ActiveX Data Objects (ADO)
- Crie uma página ASP com tags HTML apropriadas.
- Para estabelecer uma conexão e executar comandos usando ADO, adicione código Visual Basic Scripting Language (VBScript): <% Set conn = Server.CreateObject("ADODB.Connection") conn.ConnectionString="Provider=VFPOLEDB.1; Data Source= myVFPDatabase .dbc" conn.Open sql = "select * from tableName " Set rsArrival = conn.Execute(sql) %> Observação Certifique-se de substituir tableName pelo nome da tabela desejada.

### Para acessar uma fonte de dados do Visual FoxPro em JScript
- Use uma cadeia de conexão para especificar o Provedor OLE DB do Visual FoxPro e a fonte de dados conforme mostrado no código a seguir: var vbOKCancel = 0; var vbInformation = 64; var vbCancel = 2; var L_Welcome_MsgBox_Message_Text = "This script demonstrates how to access VFP OLE DB Provider using the Windows Scripting Host."; var L_Welcome_MsgBox_Title_Text = "VFP OLE DB Provider JScript Sample"; var sBuffer = ""; var sConnString = "Provider=vfpoledb.1;Data Source= myVFPDatabase .dbc"; var oConn = new ActiveXObject("ADODB.Connection"); var oRS = new ActiveXObject("ADODB.Recordset"); oConn.Open(sConnString); oRS.Open("select * from tableName where fieldName1 =' fieldValue '",oConn,3,3); // Get tableName . fieldName2 sBuffer = oRS.Fields( 'fieldName2' ).value; var WSHShell = WScript.CreateObject("WScript.Shell"); var intDoIt; intDoIt = WSHShell.Popup(sBuffer, 0, L_Welcome_MsgBox_Title_Text, vbOKCancel ); if (intDoIt == vbOKCancel) { oRS.Close(); oConn.Close(); WScript.Quit(); } Observação Certifique-se de substituir myVFPDatabase, tableName, fieldName1, fieldName2 e fieldValue pelos valores apropriados. Você deve usar caracteres de escape de barra invertida (\) para incluir o caractere de barra invertida no caminho do arquivo, por exemplo, "c:\\MyFolder\\MyVFP.dbc".

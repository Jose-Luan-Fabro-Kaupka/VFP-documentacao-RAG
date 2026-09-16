# Método CursorRefresh

Atualiza um cursor com dados atuais da fonte de dados. CursorRefresh reexecuta o valor do parâmetro SelectCmd no evento BeforeCursorRefresh com relação ao CursorAdapter DataSourceType.

> **Observação:** Se o parâmetro SelectCmd no evento BeforeCursorRefresh contiver parâmetros, você pode modificar o escopo das linhas retornadas pela consulta original alterando os parâmetros.

```foxpro
CursorAdapter.CursorRefresh()
```

# Valor de retorno

Tipo de dados Logical. CursorRefresh retorna True (.T.) se o cursor for repopulado com sucesso e False (.F.) se não for repopulado com sucesso.

> **Observação:** Para recuperar informações de erro quando CursorRefresh retorna False (.F.), você deve chamar a função AERROR( ) porque o tratamento de erros do Visual Foxpro, como o comando ON ERROR, o evento Error e o comando TRY...CATCH...FINALLY, não captura essas informações de erro.

# Observações

Aplica-se a: CursorAdapter Class

CursorRefresh atualiza as seguintes propriedades do cursor baseado em ADO ou ODBC a partir das seguintes propriedades CursorAdapter:
 - AllowSimultaneousFetch
- CompareMemo
- FetchAsNeeded
- FetchMemo
- FetchSize
- MaxRecords
- Prepared
- UseMemoSize

O Visual FoxPro gera uma mensagem de erro quando o cursor contém alterações não salvas.

Se a propriedade DataSourceType do CursorAdapter for "ADO" ao executar o método CursorFill do CursorAdapter, CursorRefresh se comporta da seguinte maneira:
 - CursorAdapter object has an attached cursor resulting from executing SelectCmd using CursorFill : Sets the ADO Command CommandText property for the ADO RecordSet ActiveCommand object to the SelectCmd used to open the ADO RecordSet unless CommandText already contains this value. Refreshes the Command object parameters collection and re-evaluates the parameter values. Calls the ADO RecordSet Requery method and passes the same values in the nOptions parameter used by CursorFill to open the ADO RecordSet.
- CursorAdapter object has an attached cursor resulting from passing an already open ADO RecordSet to the CursorFill Source parameter. Calls the ADO RecordSet Requery method and pass the same value for the nOptions parameter used by CursorFill .

> **Observação:** O método CursorRefresh ignora as propriedades MapBinary e MapVarchar para mapeamento de tipos de dados.

# Exemplo

Example 1

O exemplo a seguir ilustra a recuperação de resultados usando ADO com um parâmetro e usando CursorRefresh para atualizar dados. As configurações de cadeia de conexão para SQL Server (localhost) e Visual FoxPro OLE DB Provider são as seguintes:

```foxpro
* .ConnectionString = 'provider=SQLOLEDB.1;data source=localhost;'+
* 'initial catalog=Northwind;trusted_connection=yes'
CLEAR
LOCAL loConn AS ADODB.CONNECTION, ;
   loCommand AS ADODB.COMMAND, ;
   loException AS EXCEPTION, ;
   loCursor AS CURSORADAPTER, ;
   country, ;
   laErrors[1]
loConn = CREATEOBJECT('ADODB.Connection')
WITH loConn
   .ConnectionString = 'provider=vfpoledb;data source=' + ;
   HOME(2)+'northwind\Northwind.dbc'
   TRY
      .OPEN()
   CATCH TO loException
      MESSAGEBOX(loException.MESSAGE)
      CANCEL
   ENDTRY
ENDWITH
loCommand = CREATEOBJECT('ADODB.Command')
loCommand.ActiveConnection = loConn
loCursor = CREATEOBJECT('CursorAdapter')
WITH loCursor
   .ALIAS          = 'Customers'
   .DATASOURCETYPE = 'ADO'
   .SELECTCMD      = ;
   'select * from customers where country=?lcCountry'
   lcCountry       = 'Brazil'
   .DATASOURCE = CREATEOBJECT('ADODB.Recordset')
   .DATASOURCE.ActiveConnection = loConn
   llReturn = .CURSORFILL(.F., .F., 0, loCommand)
   IF llReturn
      BROWSE
      lcCountry = 'Canada'
      llReturn  = .CURSORREFRESH()
      IF llReturn
         BROWSE
      ENDIF llReturn
   ELSE
      AERROR(laErrors)
      MESSAGEBOX(laErrors[2])
   ENDIF llReturn
ENDWITH
```

O exemplo a seguir ilustra o uso de CursorRefresh com um ADO Recordset já aberto. The connection string settings for SQL Server (localhost) and the Visual FoxPro OLE DB Provider are:

```foxpro
* .ConnectionString = 'provider=SQLOLEDB.1;data source=localhost;' + ;
* 'initial catalog=Northwind;trusted_connection=yes'
CLEAR
LOCAL loConn AS ADODB.CONNECTION, ;
   loCommand AS ADODB.COMMAND, ;
   loParam AS ADODB.PARAMETER, ;
   loRs AS ADODB.Recordset,;
   loException AS EXCEPTION, ;
   loCursor AS CURSORADAPTER, ;
   lcCountry, ;
   laErrors[1]
loConn = CREATEOBJECT('ADODB.Connection')
WITH loConn
   .ConnectionString = 'provider=vfpoledb;data source=' + ;
      HOME(2)+'northwind\Northwind.dbc'
   TRY
      .OPEN()
   CATCH TO loException
      MESSAGEBOX(loException.MESSAGE)
      CANCEL
   ENDTRY
ENDWITH
loCommand = CREATEOBJECT('ADODB.Command')
loCommand.CommandText = ;
   "SELECT * FROM customers WHERE Country = ?"
loParam = loCommand.CreateParameter("Country", 129, 1, 15, "")
loCommand.PARAMETERS.APPEND(loParam)
loCommand.PARAMETERS("Country") = "Brazil"
loCommand.ActiveConnection = loConn
loRs = loCommand.Execute()
loCursor = CREATEOBJECT('CursorAdapter')
WITH loCursor
   .ALIAS          = 'Customers'
   .DATASOURCETYPE = 'ADO'
   llReturn = .CURSORFILL(.F., .F., 0, loRs)
   IF llReturn
      BROWSE
      loRs.ActiveCommand.PARAMETERS("Country") = "Canada"
      llReturn  = .CURSORREFRESH()
      IF llReturn
         BROWSE
      ENDIF llReturn
   ELSE
      AERROR(laErrors)
      MESSAGEBOX(laErrors[2])
   ENDIF llReturn
ENDWITH
```

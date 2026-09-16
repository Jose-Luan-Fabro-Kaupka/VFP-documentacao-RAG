# Função EVENTHANDLER( )

Associa um evento de servidor COM a métodos de interface implementados em um objeto Visual FoxPro.

Para informações sobre associação de eventos de objetos nativos do Visual FoxPro, consulte Event Binding for Visual FoxPro Objects.

```foxpro
EVENTHANDLER(oCOMObject, oVFPObject [, lUnbind])
```

#### Parâmetros
 **oCOMObject**
Especifica a referência de objeto cujos eventos serão associados. oCOMObject deve ser um objeto COM válido.
**oVFPObject**
Especifica a referência de objeto do Visual FoxPro que contém código de método definido pelo usuário, que mapeia para os eventos correspondentes do objeto COM. A classe deve implementar a interface de eventos do objeto COM específico passado no primeiro parâmetro. Por exemplo, você deve implementar a interface RecordsetEvents para associar a um objeto ADO Recordset.
**lUnbind**
O Visual FoxPro libera automaticamente o objeto COM quando ele sai de escopo. Ao passar este parâmetro com o valor .T., você pode liberar a associação de eventos enquanto ambos os objetos permanecem em escopo.

# Valor de retorno

Tipo de dados lógico. EVENTHANDLER( ) retorna True (.T.) se bem-sucedido e False (.F.) se não for bem-sucedido.

# Observações

Você pode associar um único objeto COM a vários objetos Visual FoxPro, ou pode associar vários objetos COM ao mesmo objeto Visual FoxPro.

O tratamento de eventos é desassociado automaticamente quando o objeto Visual FoxPro ou o objeto COM é liberado. Você pode chamar explicitamente a função EVENTHANDLER( ) e passar o parâmetro lUnbind para desassociar objetos sem liberar referências de objeto.

# Exemplo

```foxpro
LOCAL oEvents
LOCAL oRS AS adodb.recordset
LOCAL oConn AS adodb.Connection
oEvents = NEWOBJECT("myclass")
oConn = NEWOBJECT("adodb.connection")
oConn.Provider="MSDASQL"
* Make sure to set the SourceDB property
* below to your TESTDATA location.
oConn.ConnectionString="DSN=Visual FoxPro Database;" + ;
"SourceType=DBC; SourceDB=D:\VFP\DATA\TESTDATA.DBC"
oConn.Open
oRS = oConn.Execute("select * from customer")
? EVENTHANDLER(oRS, oEvents)
?
? PADR(oRS.Fields(0).Value,20)
? EVENTHANDLER (oRS, oEvents, .T.)
oRS.MoveNext
? PADR(oRS.Fields(0).Value,20)
oRS.MoveNext
CLEAR all
RETURN
DEFINE CLASS myclass AS session
IMPLEMENTS RecordsetEvents IN "adodb.recordset"
PROCEDURE Recordsetevents_WillChangeField(cFields AS Number @, Fields AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_FieldChangeComplete(cFields AS Number @, Fields AS VARIANT @, pError AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_WillChangeRecord(adReason AS VARIANT @, cRecords AS Number @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_RecordChangeComplete(adReason AS VARIANT @, cRecords AS Number @, pError AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_WillChangeRecordset(adReason AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
   ?adreason,adstatus,precordset.recordcount
PROCEDURE Recordsetevents_RecordsetChangeComplete(adReason AS VARIANT @, pError AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_WillMove(adReason AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_MoveComplete(adReason AS VARIANT @, pError AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_EndOfRecordset(fMoreData AS LOGICAL @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_FetchProgress(Progress AS Number @, MaxProgress AS Number @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
PROCEDURE Recordsetevents_FetchComplete(pError AS VARIANT @, adStatus AS VARIANT @, pRecordset AS VARIANT @) AS VARIANT
   ? " "+program() + ' ' + TRANSFORM(DATETIME())
ENDDEFINE
```

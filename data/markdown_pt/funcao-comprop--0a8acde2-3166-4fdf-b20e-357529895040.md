# Função COMPROP( )

Define ou retorna a configuração de comportamento de uma propriedade de objeto COM.

```foxpro
COMPROP(oCOMObject, cProperty [, eValue])
```

#### Parâmetros
 **oComObject**
Especifica uma referência a um objeto COM. cProperty não diferencia maiúsculas e minúsculas. Você deve usar o nome completo do objeto COM. Se eValue não for fornecido, COMPROP( ) retornará o valor de cProperty.
**cProperty**
Especifica o nome da propriedade COM a definir. Valores possíveis: UTF8 determina se cadeias UNICODE retornadas por um objeto COM são convertidas em ANSI; a conversão é executada por padrão. PUTREF determina se a atribuição inicial de objeto é PROPERTY_PUT (padrão) ou PUTREF.
**eValue**
Especifica um valor que representa o comportamento aplicado a cProperty. 0 aplica o comportamento padrão. 1 aplica o comportamento não padrão descrito para cProperty. Por exemplo, eValue igual a 1 para UTF8 impede que caracteres multibyte sejam exibidos como pontos de interrogação. Para PUTREF, faz o Visual FoxPro tentar primeiro a atribuição como PUTREF e, somente se falhar, como PROPERTY_PUT. A atribuição a propriedades de alguns controles ActiveX ou objetos COM exige PUTREF, enquanto o padrão do Visual FoxPro é PROPERTY_PUT.

# Valor de retorno

COMPROP( ) retorna o valor de cProperty.

# Exemplos

O exemplo a seguir retorna dados de métodos de um recordset ADO como UNICODE, em vez de permitir a conversão em ANSI:

```foxpro
LOCAL oConn AS adodb.Connection, oRS AS adodb.Recordset
LOCAL lcStr AS STRING
oConn=CREATEOBJECT("ADODB.Connection")
oConn.Open("DSN=Nwind;")  && DSN to SQL Server
oRS=oConn.Execute("select * from customers")
COMPROP(oRS,'UTF8',1)
DO WHILE NOT oRS.Eof
   lcStr = oRS.Fields(4).Value
   oRS.MoveNext
ENDDO
oRS.Close()
oRS.ActiveConnection=NULL
oRS=NULL
oConn.Close()
oConn=NULL
```

No exemplo a seguir, um controle ActiveX é configurado para usar PUTREF em vez de PROPERTY_PUT:

```foxpro
=COMPROP(oForm.OLECONTROL1, 'PUTREF',1)
```

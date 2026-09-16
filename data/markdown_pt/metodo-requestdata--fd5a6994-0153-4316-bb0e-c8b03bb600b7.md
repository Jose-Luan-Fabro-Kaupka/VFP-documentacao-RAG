# Método RequestData

Cria uma matriz contendo dados de uma tabela aberta em uma instância do Visual FoxPro.

```foxpro
ApplicationObject.RequestData([nWorkArea | cTableAlias] [, nRecords])
```

# Valor de retorno

Array

# Valor de retorno
 **nWorkArea**
Especifica o número da área de trabalho da tabela da qual os dados são armazenados na matriz. Se você omitir cTableAlias e nWorkArea , os dados da tabela aberta na área de trabalho atual são armazenados na matriz.
**cTableAlias**
Especifica o alias da tabela da qual os dados são armazenados na matriz.
**nRecords**
Especifica o número de registros armazenados na matriz, começando do registro atual. Se nRecords for omitido e houver memória suficiente disponível, todos os registros, começando do registro atual, são armazenados na matriz.

# Observações

Aplica-se a: Objeto Application | Variável de sistema _VFP

Use o método RequestData para recuperar dados de uma instância do Visual FoxPro.

# Exemplo

O exemplo a seguir, executado dentro do Visual FoxPro, cria uma segunda instância do Visual FoxPro. A tabela Customer é aberta na segunda instância do Visual FoxPro.

Uma matriz contendo dados da tabela Customer é criada na primeira instância do Visual FoxPro, e o conteúdo da matriz é exibido. A matriz contém dados dos primeiros 5 registros na tabela Customer. A segunda instância do Visual FoxPro é então fechada.

```foxpro
oNewInstance = CREATEOBJECT('VisualFoxPro.Application')
oNewInstance.DoCmd "USE (HOME(2) + 'Data\Customer')"
aCustomerArray = oNewInstance.RequestData('Customer',5)
DISPLAY MEMORY LIKE aCustomerArray
oNewInstance.DoCmd('QUIT')
```

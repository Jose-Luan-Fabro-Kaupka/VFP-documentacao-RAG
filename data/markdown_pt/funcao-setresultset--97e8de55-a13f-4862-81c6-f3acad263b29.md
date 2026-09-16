# Função SETRESULTSET( )

Marca um cursor como um conjunto de resultados na sessão de dados atual.

> **Observação:** Apenas um cursor por sessão de dados pode ser marcado. Ao marcar um novo cursor, SETRESULTSET( ) remove a marcação de qualquer cursor marcado anteriormente.

```foxpro
SETRESULTSET( nWorkArea | cTableAlias )
```

#### Parâmetros
 **nWorkArea**
Especifica um número de área de trabalho.
**cTableAlias**
Especifica o alias do cursor que você deseja marcar.

# Valor de retorno

Numeric. SETRESULTSET( ) retorna o número da área de trabalho do cursor marcado anteriormente na sessão de dados atual ou zero (0) se nenhum cursor estiver marcado na sessão de dados atual.

# Observações

SETRESULTSET( ) é suportado no Visual FoxPro e no Provedor OLE DB do Visual FoxPro. Você pode usar SETRESULTSET( ) em um procedimento armazenado de contêiner de banco de dados (DBC) ou enviá-lo ao Provedor OLE DB do Visual FoxPro, assumindo que o cursor tenha sido aberto anteriormente pelo Provedor OLE DB. Por exemplo, suponha que um comando anterior abra um cursor chamado MyCursor no Provedor OLE DB. A seguinte linha de código recupera um RecordSet ADO para o cursor MyCursor:

```foxpro
oRecordSet = oConn.Execute("SETRESULTSET('MyCursor')")
```

Usando SETRESULTSET( ) para marcar um cursor ou tabela aberta pelo Provedor OLE DB do Visual FoxPro, você pode recuperar um conjunto de linhas criado da tabela ou cursor de um procedimento armazenado de contêiner de banco de dados (DBC). Quando o Provedor OLE DB conclui a execução do comando, ele cria um conjunto de linhas do cursor marcado, se existir, e então remove a marcação do cursor.

> **Observação:** Neste cenário, o Provedor OLE DB desconsidera todos os outros valores de retorno. Por exemplo, se um procedimento armazenado contém uma instrução RETURN Value e um cursor marcado, o Provedor OLE DB não retorna o valor. Em vez disso, retorna o cursor marcado como um conjunto de linhas para a aplicação chamadora. Quando o conjunto de linhas é fechado, o cursor também é fechado.

No entanto, embora o Provedor OLE DB desconsidere todos os valores de retorno quando existe um cursor marcado, você pode usar SETRESULTSET( ) com o comando RETURN. Por exemplo:

```foxpro
RETURN SETRESULTSET("MyCursor")
```

Esta instrução cria e retorna um conjunto de linhas do cursor marcado, não o valor de retorno de SETRESULTSET( ).

# Função SQLIDLEDISCONNECT( )

Permite que uma conexão ou conexões SQL pass-through sejam temporariamente desconectadas.

```foxpro
SQLIDLEDISCONNECT(nStatementHandle)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução da conexão a ser temporariamente desconectada. Especifique 0 para nStatementHandle para desconectar temporariamente todas as conexões ativas.

# Valor de retorno

Numérico.

1 é retornado se SQLIDLEDISCONNECT( ) desconectar temporariamente com sucesso a conexão ou conexões SQL pass-through.

-1 é retornado se SQLIDLEDISCONNECT( ) não puder desconectar temporariamente a conexão ou conexões SQL pass-through.

# Observações

A função falha (retorna -1) se o identificador de instrução estiver ocupado ou se uma conexão estiver no modo de confirmação manual. A função AERROR( ) pode ser usada para obter informações sobre a causa do erro.

Uma conexão temporariamente desconectada é restaurada automaticamente assim que é necessária para executar uma operação; a cadeia de conexão original é usada. A propriedade ODBC ODBChstmt retorna 0 se o identificador de instrução foi temporariamente liberado e a propriedade ODBChdbc retorna 0 se a conexão foi temporariamente desconectada. Uma conexão compartilhada é temporariamente desconectada assim que todos os seus identificadores de instrução são temporariamente desconectados (liberados).

# Função GETRESULTSET( )

Recupera o número da área de trabalho de um cursor marcado por SETRESULTSET( ) na sessão de dados atual.

```foxpro
GETRESULTSET()
```

# Valor de retorno

Numeric. GETRESULTSET( ) retorna o número da área de trabalho do cursor marcado na sessão de dados atual ou zero (0) se nenhum cursor estiver marcado na sessão de dados atual.

# Observações

GETRESULTSET( ) é suportado no Visual FoxPro e no Visual FoxPro OLE DB Provider. Você pode usar GETRESULTSET( ) em um procedimento armazenado de container de banco de dados (DBC) ou enviá-lo ao Visual FoxPro OLE DB Provider, assumindo que o cursor tenha sido previamente aberto pelo OLE DB Provider.

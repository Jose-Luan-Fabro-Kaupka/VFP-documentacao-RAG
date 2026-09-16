# Função CLEARRESULTSET( )

Remove o marcador de um cursor marcado por SETRESULTSET( ) na sessão de dados atual.

```foxpro
CLEARRESULTSET()
```

# Valor de retorno

Numeric. CLEARRESULTSET( ) retorna o número da área de trabalho do cursor previamente marcado ou zero (0) se nenhum cursor estiver marcado na sessão de dados atual.

# Observações

CLEARRESULTSET( ) é suportado no Visual FoxPro e no Visual FoxPro OLE DB Provider. Você pode usar GETRESULTSET( ) em uma stored procedure de um container de banco de dados (DBC) ou enviá-lo ao Visual FoxPro OLE DB Provider, assumindo que o cursor tenha sido previamente aberto pelo OLE DB Provider.

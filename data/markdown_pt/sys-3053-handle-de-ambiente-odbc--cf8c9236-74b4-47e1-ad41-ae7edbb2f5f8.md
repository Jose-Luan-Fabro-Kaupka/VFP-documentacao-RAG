# SYS(3053) - Handle de ambiente ODBC

Retorna o handle de ambiente ODBC.

```foxpro
SYS(3053)
```

# Valor de retorno

Character

# Observações

Se o ODBC não estiver carregado, SYS(3053) o carrega e retorna o handle de ambiente ODBC.

O handle de ambiente retornado por SYS(3053) fornece acesso ao ODBC por meio de chamadas à API ODBC. O acesso à API ODBC está disponível no Visual FoxPro por meio de DECLARE - DLL e de rotinas de biblioteca de API externas do Visual FoxPro.

Somente um handle de ambiente ODBC deve ser usado por vez. Um programa Visual FoxPro que usa chamadas ODBC deve usar SYS(3053) para obter o handle de ambiente ODBC, em vez de realocar e liberar o handle de ambiente ODBC por meio de chamadas à API ODBC.

Tenha cuidado ao manipular um handle de ambiente ODBC. Para obter mais informações sobre a API ODBC, consulte a documentação do Microsoft ODBC SDK.

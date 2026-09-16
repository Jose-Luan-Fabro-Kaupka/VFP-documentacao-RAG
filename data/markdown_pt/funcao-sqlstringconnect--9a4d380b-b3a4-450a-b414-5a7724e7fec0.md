# Função SQLSTRINGCONNECT( )

Estabelece uma conexão com uma fonte de dados usando uma cadeia de conexão.

```foxpro
SQLSTRINGCONNECT([lShared] | [cConnectString [, lSharable]])
```

#### Parâmetros
 **lShared**
Especifica se deve criar uma conexão compartilhada. lShared Descrição False (.F.) SQLSTRINGCONNECT( ) não cria uma conexão compartilhada. (Padrão) True (.T.) SQLSTRINGCONNECT( ) cria uma conexão compartilhada.
**cConnectString**
Especifica a cadeia de conexão da fonte de dados exigida por alguns drivers Open Database Connectivity (ODBC). O Visual FoxPro passa a cadeia de conexão para o driver ODBC. Para obter mais informações sobre cadeias de conexão de fonte de dados, consulte a documentação do seu driver ODBC. Você também pode escolher uma fonte de dados na Caixa de diálogo Select Connection or Data Source , que aparece quando você chama SQLSTRINGCONNECT( ) sem cConnectString .
**lSharable**
Especifica se a fonte de dados especificada com cConnectString tem uma conexão compartilhada.

# Valor de retorno

Tipo de dados numérico. SQLSTRINGCONNECT( ) retorna um valor numérico positivo diferente de zero como o identificador de instrução se você se conectar com sucesso à fonte de dados. SQLSTRINGCONNECT( ) retorna –1 se não conseguir fazer a conexão.

> **Dica:** Você deve armazenar esse identificador de instrução em uma variável de memória e usar a variável em chamadas de função subsequentes que exigem um identificador de conexão.

# Observações

As funções SQLCONNECT( ) e SQLSTRINGCONNECT( ) retornam um valor numérico como o identificador de instrução em vez de um identificador de conexão. Você não pode obter um identificador de conexão diretamente. Você ainda pode definir e obter propriedades de conexão usando as funções SQLSETPROP( ) e SQLGETPROP( ) passando o identificador de instrução dessa conexão e a cadeia de caracteres, "Shared", como argumentos. Todas as outras funções SQL usam um identificador de instrução em vez de um identificador de conexão.

SQLSTRINGCONNECT( ) sempre cria uma nova conexão quando consegue fazer uma conexão com sucesso. No entanto, definir o parâmetro lShared determina se você pode compartilhar a conexão posteriormente. Se você especificar uma conexão como compartilhável definindo lShared como True (.T.), você pode compartilhar a conexão posteriormente chamando SQLCONNECT( ) e passando o valor numérico do identificador de conexão como o primeiro parâmetro. Para obter mais informações, consulte Função SQLCONNECT( ).

Você pode usar SQLCONNECT( ) para obter um novo identificador de instrução em uma conexão compartilhada que foi aberta usando SQLSTRINGCONNECT( ).

# Exemplo

Exemplo 1

O exemplo a seguir assume que existe e está disponível uma fonte de dados ODBC chamada MyFoxSQLNT. SQLSTRINGCONNECT( ) retorna um valor numérico, que é armazenado em uma variável chamada `gnHandle`.

Se você se conectar com sucesso à fonte de dados, SQLSTRINGCONNECT( ) retorna um número positivo, uma caixa de diálogo aparece e SQLDISCONNECT( ) é chamado para desconectar da fonte de dados.

Se você não conseguir se conectar à fonte de dados, SQLSTRINGCONNECT( ) retorna um número negativo e exibe uma mensagem.

```foxpro
STORE SQLSTRINGCONNECT('dsn=MyFoxSQLNT;uid=myUserID;pwd=myPassword')
   TO gnConnHandle
IF gnConnHandle < 0
   = MESSAGEBOX('Cannot make connection', 16, 'SQL Connect Error')
ELSE
   = MESSAGEBOX('Connection made', 48, 'SQL Connect Message')
   = SQLDISCONNECT(gnHandle)
ENDIF
```

Exemplo 2

Os exemplos a seguir mostram como você pode usar a função SQLSTRINGCONNECT( ) sem um Data Source Name (DSN).

```foxpro
lcDSNLess="driver = SQL Server;server=<servername>;uid=<userid>;pwd=<password>"
```

-ou-

```foxpro
lcDSNLess="driver = {SQL Server};server=<servername>;uid=<userid>;pwd=<password>"
```

-ou-

```foxpro
lcDSNLess="DRIVER = {SQL Server};" ;
+ "SERVER=<servername>;" ;
+ "UID=<userid>;" ;
+ "PWD=<password>;" ;
+ "DATABASE=PUBS;" ;
+ "WSID=<machine name or userid>;" ;
+ "APP=MicroX(R) Sample App"
lnConnHandle=SQLSTRINGCONNECT(m.lcDSNLess)
```

Exemplo 3

Cada um dos exemplos a seguir cria uma nova conexão compartilhada. Na primeira instrução, a Caixa de diálogo Select Connection or Data Source aparece e SQLSTRINGCONNECT( ) cria a conexão resultante como compartilhada.

```foxpro
SQLSTRINGCONNECT(.T.)
SQLSTRINGCONNECT('myConnectionString', .T.)
```

# Função SQLCONNECT( )

Estabelece uma conexão com uma fonte de dados. Existem duas versões da sintaxe.

```foxpro
SQLCONNECT([nStatementHandle])
```

```foxpro
SQLCONNECT([cConnectionName | cDataSourceName [, cUserID [, cPassword ]][, lShared]])
```

#### Parâmetros
 **nStatementHandle**
Especifica que um novo handle de instrução seja criado para a conexão compartilhada subjacente representada por nStatementHandle . O novo handle de instrução usa as configurações fornecidas por nStatementHandle em vez de usar as configurações padrão. Observação Você não pode criar um novo handle de instrução para uma conexão que não é compartilhada. O Visual FoxPro gera um erro se você tentar criar um novo handle de instrução em uma conexão não compartilhada. Você também pode usar SQLCONNECT( ) para obter um novo handle de instrução em uma conexão compartilhada que foi aberta usando SQLSTRINGCONNECT( ) .
**cConnectionName**
Especifica uma conexão nomeada criada pelo comando CREATE CONNECTION. Ao usar CREATE CONNECTION ou o Connection Designer para criar uma conexão nomeada, você pode configurar a conexão especificando um nome de fonte de dados, ID de usuário e senha. Ao usar a conexão nomeada em SQLCONNECT( ) como cConnectionName , você pode passar valores diferentes dos da conexão nomeada para os parâmetros opcionais cUserID e cPassword. Esses valores passados são usados em vez do ID de usuário e da senha na conexão nomeada especificada por cConnectionName . Por exemplo, suponha que você criou uma conexão nomeada chamada myNamedConnection usando CREATE CONNECTION ou o Connection Designer e especificou os valores myUserID e myPassword para a conexão nomeada. Para SQLCONNECT( ) , você pode especificar myNamedConnection como cConnectionName e, em seguida, especificar myAltUserID e myAltPassword como um ID de usuário e senha alternativos, como no código a seguir: SQLCONNECT("myNamedConnection", "myAltUserID", "myAltPassword") No entanto, se você criar uma conexão nomeada usando uma cadeia de conexão com CREATE CONNECTION ou o Connection Designer, usar a conexão nomeada em SQLCONNECT( ) e tentar passar parâmetros opcionais de ID de usuário e senha para SQLCONNECT( ) , o Visual FoxPro gera a mensagem apropriada. Ao criar uma nova conexão compartilhada, o parâmetro cConnectionName refere-se a uma conexão nomeada no contêiner de banco de dados atual (DBC). Ao criar um novo handle de instrução baseado em uma conexão compartilhada existente, o parâmetro cConnectionName refere-se a uma conexão anterior aberta em modo compartilhado. Se você usar o parâmetro cConnectionName sem o parâmetro lShared ou com o parâmetro lShared como False (.F.), você sempre criará uma nova conexão que não é compartilhada. Ao usar cConnectionName , se lShared é True (.T.) e a conexão nomeada já está aberta em modo compartilhado, o nome de usuário e a senha fornecidos devem corresponder aos usados anteriormente. Caso contrário, o Visual FoxPro gera a mensagem apropriada.
**cDataSourceName**
Especifica o nome de uma fonte de dados conforme definido no arquivo Odbc.ini. Você também pode escolher uma fonte de dados na caixa de diálogo Select Connection or Data Source Dialog Box , que aparece quando você chama SQLCONNECT( ) sem argumentos adicionais ou apenas com o parâmetro lShared.
**cUserID**
Especifica o identificador de usuário usado para fazer logon na fonte de dados.
**cPassword**
Especifica a senha para obter acesso à fonte de dados.
**lShared**
Especifica se deve ou não criar uma conexão compartilhada. lShared Descrição False (.F.) SQLCONNECT( ) não cria uma conexão compartilhada. (Padrão) True (.T.) SQLCONNECT( ) cria uma conexão compartilhada.

# Valor de retorno

Tipo de dados numérico. SQLCONNECT( ) retorna um valor numérico positivo diferente de zero como o handle de instrução se você se conectar com sucesso à fonte de dados. SQLCONNECT( ) retorna –1 se não conseguir estabelecer a conexão.

> **Dica:** Você deve armazenar este handle de instrução em uma variável de memória e usar a variável em chamadas de função subsequentes que exigem um handle de conexão.

# Observações

As funções SQLCONNECT( ) e SQLSTRINGCONNECT( ) retornam um valor numérico como o handle de instrução em vez de um handle de conexão. Você não pode obter um handle de conexão diretamente. Você ainda pode definir e obter propriedades de conexão usando as funções SQLSETPROP( ) e SQLGETPROP( ) passando o handle de instrução para essa conexão e a cadeia de caracteres, "Shared", como argumentos. Todas as outras funções SQL usam um handle de instrução em vez de um handle de conexão.

Se você emitir uma instrução como `SQLCONNECT(cConnectionName, .T.)`, e uma conexão compartilhada já estiver aberta com o mesmo nome, as configurações dessa conexão não mudam para as configurações armazenadas para essa conexão no contêiner de banco de dados (DBC). No entanto, o novo handle de instrução usará as configurações de instrução do DBC.

> **Observação:** Você deve desabilitar a caixa de diálogo de logon do Open Database Connectivity (ODBC) para dar suporte a SQL pass through com o Microsoft Transaction Server. Para desabilitar a caixa de diálogo de logon ODBC, use a instrução SQLSETPROP(nStatementHandle, 'DispLogin', 3) , onde cStatementHandle é o handle de instrução retornado por SQLCONNECT( ) . Você também pode desabilitar a caixa de diálogo de logon ODBC no Connection Designer .

# Exemplo

Exemplo 1

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT existe e está disponível. SQLCONNECT( ) retorna um valor numérico, que é armazenado em uma variável chamada `gnConnHandle`.

Se você se conectar com sucesso à fonte de dados, SQLCONNECT( ) retorna um número positivo, uma caixa de diálogo aparece e SQLDISCONNECT( ) é chamado para desconectar da fonte de dados.

Se você não conseguir se conectar à fonte de dados, SQLCONNECT( ) retorna um número negativo e exibe uma mensagem.

```foxpro
STORE SQLCONNECT('MyFoxSQLNT', 'myUserID', 'myPassword') TO gnConnHandle
IF gnConnHandle <= 0
   = MESSAGEBOX('Cannot make connection', 16, 'SQL Connect Error')
ELSE
   = MESSAGEBOX('Connection made', 48, 'SQL Connect Message')
   = SQLDISCONNECT(gnHandle)
ENDIF
```

Exemplo 2

Cada um dos exemplos a seguir cria novas conexões compartilhadas. A caixa de diálogo Choose Data Source aparece, e SQLCONNECT( ) cria a conexão resultante como compartilhada.

```foxpro
SQLCONNECT(.T.)
SQLCONNECT( myConnectionName, .T. )
SQLCONNECT( myDataSourceName, myUserID, myPassword, .T. )
```

Exemplo 3

Cada um dos exemplos a seguir cria um novo handle de instrução baseado em uma conexão compartilhada existente.

```foxpro
SQLCONNECT( nStatementHandleValue )
SQLCONNECT( myConnectionName, .T. )
```

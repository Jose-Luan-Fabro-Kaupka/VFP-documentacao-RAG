# Função SQLDISCONNECT( )

Encerra uma conexão com uma fonte de dados.

```foxpro
SQLDISCONNECT(nStatementHandle)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado por SQLCONNECT( ). Especifique 0 para nStatementHandle para encerrar todas as conexões ativas.

# Valor de retorno

Numérico. SQLDISCONNECT( ) retorna 1 se a conexão for encerrada com sucesso, – 1 se houver um erro no nível da conexão e – 2 se houver um erro no nível do ambiente.

# Observações

SQLDISCONNECT( ) encerra uma conexão com uma fonte de dados. Você deve fornecer o identificador de instrução que SQLCONNECT( ) retornou quando você estabeleceu a conexão.

> **Observação:** Se você executar SQLDISCONNECT( ) dentro de uma sequência de função assíncrona ou durante uma transação, SQLDISCONNECT( ) gera um erro.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. SQLCONNECT( ) é emitido e seu valor de retorno é armazenado em uma variável chamada `gnHandle`.

Se você se conectar com sucesso à fonte de dados, SQLCONNECT( ) retorna um número positivo, uma caixa de diálogo é exibida e SQLDISCONNECT( ) é usado para desconectar da fonte de dados.

Se você não puder se conectar à fonte de dados, SQLCONNECT( ) retorna um número negativo e uma mensagem é exibida.

```foxpro
STORE SQLCONNECT('MyFoxSQLNT', '<userid>', '<password>') TO gnHandle
IF gnHandle <= 0
   = MESSAGEBOX('Cannot make connection', 16, 'SQL Connect Error')
ELSE
   = MESSAGEBOX('Connection made', 48, 'SQL Connect Message)
   = SQLDISCONNECT(gnHandle)
ENDIF
```

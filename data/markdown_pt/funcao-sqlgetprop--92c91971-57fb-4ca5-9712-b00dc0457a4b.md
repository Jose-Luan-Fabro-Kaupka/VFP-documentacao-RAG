# Função SQLGETPROP( )

Recupera as configurações atuais ou padrão de uma conexão ativa.

```foxpro
SQLGETPROP(nStatementHandle, cSetting)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado por SQLCONNECT( ). Se você especificar 0 para nStatementHandle, SQLGETPROP( ) retorna a configuração do ambiente.
**cSetting**
Especifica a configuração. Para uma lista das configurações que você pode especificar, consulte SQLSETPROP( ) Function.

# Valor de retorno

Character, Numeric ou Logical. SQLGETPROP( ) retorna as configurações atuais ou padrão de uma conexão ativa. SQLGETPROP( ) retorna -1 se ocorrer um erro em nível de conexão e -2 se ocorrer um erro em nível de ambiente.

# Exemplo

O exemplo a seguir usa SQLCONNECT( ) para exibir a caixa de diálogo Select Connection or Data Source. Escolha uma fonte de dados, a conexão com a fonte de dados é testada e o exemplo exibe os resultados usando SQLGETPROP( ) e o cSetting para a fonte de dados.

```foxpro
CLOSE ALL
CLEAR ALL
CLEAR
nHandle=SQLCONNECT()
IF nHandle > 0
 cSource= SQLGETPROP(nHandle, "datasource")
 =MESSAGEBOX("Current Data Source = "+cSource,0,"Connection Results")
ELSE
 =MESSAGEBOX("Connection Error = " + ;
  ALLTRIM(STR(nHandle)),0,"Connection Results")
ENDIF
=SQLDISCONNECT(nHandle)
```

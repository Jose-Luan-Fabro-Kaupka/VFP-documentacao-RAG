# Função SQLCANCEL( )

Solicita o cancelamento de uma instrução SQL em execução.

SQLCANCEL( ) cancela a execução de SQLCOLUMNS( ), SQLEXEC( ), SQLMORERESULTS( ) e SQLTABLES( ) no modo assíncrono. Para estabelecer o modo assíncrono, use a função SQLSETPROP( ).

```foxpro
SQLCANCEL(nStatementHandle)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução ativo cuja instrução SQL deve ser cancelada.

# Valor de retorno

Numérico. SQLCANCEL( ) retorna 1 se a instrução SQL é cancelada com sucesso, – 1 se há um erro no nível de conexão e – 2 se há um erro no nível de ambiente.

# Exemplo

O exemplo a seguir assume que SQLCONNECT( ) é emitido com sucesso e seu valor de retorno é armazenado em uma variável de memória chamada `gnHandle`.

SQLEXEC( ) é usado para enviar uma instrução SQL à fonte de dados e retornar os resultados a um cursor. SQLCANCEL( ) é emitido para interromper a consulta.

```foxpro
= SQLSETPROP(gnHandle, 'asynchronous', .T.)   && To stop SQLEXEC()
= SQLEXEC(gnHandle, 'SELECT * FROM authors')
= SQLCANCEL(gnHandle)   && Wrong select statement, cancel
```

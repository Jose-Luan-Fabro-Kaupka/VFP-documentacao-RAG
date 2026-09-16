# Evento dbc_CloseData

Ocorre quando um banco de dados é fechado. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_CloseData(cDatabaseName, lAll)
```

```foxpro
PROCEDURE dbc_CloseData
LPARAMETERS cDatabaseName, lAll
```

#### Parâmetros
 **cDatabaseName**
Especifica o nome do banco de dados de destino.
**lAll**
Especifica se a palavra-chave ALL foi incluída no comando CLOSE DATABASES. Se DBC Events estiver ativado, o evento ocorrerá sempre que um banco de dados for fechado, explicitamente ou não.

# Observações

Use dbc_CloseData para verificar cDatabaseName e lAll ou rastrear o acesso ao banco de dados quando ele estiver prestes a ser fechado.

Quando vários bancos de dados são fechados ao mesmo tempo, o método dbc_CloseData de cada um é disparado sucessivamente. Assim, CLOSE DATABASES ALL pode executar vários eventos e métodos.

Retorne .F. deste procedimento para impedir o fechamento.

# Exemplo

```foxpro
PROCEDURE dbc_CloseData ;
         (cDatabaseName,;
          lAll)
? '     cDatabaseName = ' + TRANSFORM(cDatabaseName) + ' - ' ;
                      + TYPE('cDatabaseName')
? '     lAll          = ' + TRANSFORM(lAll)          + ' - ' ;
                      + TYPE('lAll')+' /end/ '
RETURN .F.     && This will prevent database closure.
ENDPROC
```

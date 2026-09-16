# Evento dbc_BeforeCreateOffline

Ocorre antes que uma view seja colocada offline. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeCreateOffline(cViewName, cPath)
```

```foxpro
PROCEDURE dbc_BeforeCreateOffline
LPARAMETERS cViewName, cPath
```

#### Parâmetros
 **cViewName**
Especifica o nome da view sendo colocada offline.
**cPath**
Especifica o diretório no qual a view offline é colocada e o nome da view offline.

# Observações

Você pode usar o evento dbc_BeforeCreateOffline para verificar valores apropriados para cViewName e cPath ou usar esses parâmetros em um procedimento para rastrear tentativas de acesso ao banco de dados antes que uma view offline seja criada.

Retorne .F. deste procedimento para impedir que a view seja colocada offline.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeCreateOffline ;
         (cViewName,;
          cPath)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cViewName =  ' + TRANSFORM(cViewName) + ' - ' ;
                  + TYPE('cViewName')
? '     cPath     =  ' + TRANSFORM(cPath)     + ' - ' ;
                  + TYPE('cPath')+' /end/ '
ENDPROC
```

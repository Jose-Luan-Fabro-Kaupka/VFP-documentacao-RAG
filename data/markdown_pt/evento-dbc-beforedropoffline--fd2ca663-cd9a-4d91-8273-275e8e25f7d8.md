# Evento dbc_BeforeDropOffline

Ocorre imediatamente antes de uma função DROPOFFLINE( ), que retorna uma visualização offline para online. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDropOffline(cViewName, cPath)
```

```foxpro
PROCEDURE dbc_BeforeDropOffline
LPARAMETERS cViewName, cPath
```

#### Parâmetros
 **cViewName**
Especifica o nome da visualização offline sendo retornada para online.
**cPath**
Especifica o diretório no qual a visualização offline está localizada.

Retorne .F. deste procedimento para impedir que a visualização seja retornada para online.

# Observações

Você pode usar o evento dbc_BeforeDropOffline para rastrear tentativas de acesso ao banco de dados antes de uma visualização offline ser retornada para online.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeDropOffline ;
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

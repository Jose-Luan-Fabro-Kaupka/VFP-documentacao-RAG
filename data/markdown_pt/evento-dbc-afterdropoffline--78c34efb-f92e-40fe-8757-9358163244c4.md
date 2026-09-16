# Evento dbc_AfterDropOffline

Ocorre depois que DROPOFFLINE( ) foi concluído. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDropOffline(cViewName, cPath)
```

```foxpro
PROCEDURE dbc_AfterDropOffline
LPARAMETERS cViewName, cPath
```

#### Parâmetros
 **cViewName**
Especifica o nome da view offline retornada online.
**cPath**
Especifica o diretório no qual a view offline está localizada.

# Observações

Você pode usar o evento dbc_AfterDropOffline para rastrear o acesso ao banco de dados depois que uma view offline é retornada online.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterDropOffline ;
         (cViewName,;
          cPath)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cViewName = ' + TRANSFORM(cViewName) + ' - ' ;
                  + TYPE('cViewName')
? '     cPath     = ' + TRANSFORM(cPath)     + ' - ' ;
                  + TYPE('cPath')+' /end/ '
ENDPROC
```

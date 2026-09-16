# Evento dbc_AfterCreateOffline

Ocorre após a conclusão de CREATEOFFLINE( ). Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCreateOffline(cViewName, cPath)
```

```foxpro
PROCEDURE dbc_AfterCreateOffline
LPARAMETERS cViewName, cPath
```

#### Parâmetros
 **cViewName**
Especifica o nome da view existente que está sendo colocada offline.
**cPath**
Especifica o diretório no qual a view offline foi colocada.

# Observações

Você pode usar o evento dbc_AfterCreateOffline para rastrear o acesso ao banco de dados após a criação de uma view offline.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterCreateOffline ;
         (cViewName,;
          cPath)
? '>>   ' + PROGRAM()
?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
? '     cViewName =  ' + TRANSFORM(cViewName) + ' - ' ;
                  + TYPE('cViewName')
? '     cPath     =  ' + TRANSFORM(cPath)     + ' - ' ;
                  + TYPE('cPath') + ' /end/ '
ENDPROC
```

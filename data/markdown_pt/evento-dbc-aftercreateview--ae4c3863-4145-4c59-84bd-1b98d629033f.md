# Evento dbc_AfterCreateView

Ocorre depois que uma view SQL é criada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterCreateView(cViewName, lRemote)
```

```foxpro
PROCEDURE dbc_AfterCreateView
LPARAMETERS cViewName, lRemote
```

#### Parâmetros
 **cViewName**
Especifica o nome da view que foi criada.
**lRemote**
Especifica se a view é remota.

# Observações

Você pode usar o evento dbc_AfterCreateView para rastrear o acesso ao banco de dados depois que uma view é criada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterCreateView ;
         (cViewName, ;
          lRemote)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cViewName  = ' + TRANSFORM(cViewName) + ' - ' ;
                    + TYPE('cViewName ')
 ? '     lRemote    = ' + TRANSFORM(lRemote)   + ' - ' ;
                    + TYPE('lRemote')+' /end/ '
ENDPROC
```

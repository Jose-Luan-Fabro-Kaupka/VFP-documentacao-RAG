# Evento dbc_BeforeCreateView

Ocorre antes de uma view SQL (cursor atualizável) ser criada. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeCreateView(cViewName)
```

```foxpro
PROCEDURE dbc_BeforeCreateView
LPARAMETERS cViewName)
```

#### Parâmetros
 **cViewName**
Especifica o nome da view sendo criada.

# Observações

Você pode usar o evento dbc_BeforeCreateView para rastrear tentativas de acesso ao banco de dados antes de uma view ser criada.

Retorne .F. deste procedimento para impedir que a view seja criada.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameters passed.
PROCEDURE dbc_BeforeCreateView ;
         (cViewName, ;
          lRemote)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cViewName =  ' + TRANSFORM(cViewName) + ' - ' ;
                   + TYPE('cViewName ')+' /end/ '
*RETURN .f.
ENDPROC
```

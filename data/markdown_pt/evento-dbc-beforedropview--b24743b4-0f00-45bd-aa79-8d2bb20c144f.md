# Evento dbc_BeforeDropView

Ocorre antes de uma View ser removida do banco de dados atual. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDropView(cViewName)
```

```foxpro
PROCEDURE dbc_BeforeDropView
LPARAMETERS cViewName
```

#### Parâmetros
 **cViewName**
Especifica o nome da view a ser excluída do banco de dados atual.

# Observações

DROP VIEW é quase idêntico a DELETE VIEW; DROP VIEW é a sintaxe padrão ANSI SQL para excluir uma view SQL. Ambos os comandos removem uma definição de view do banco de dados ativo, mas a sintaxe é ligeiramente diferente.

Você pode usar o evento dbc_BeforeDropView para rastrear tentativas de acesso ao banco de dados antes que uma view seja removida do banco de dados.

Retorne .F. deste procedimento para impedir que a view seja removida.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeDropView ;
         (cViewName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cViewName =  ' + TRANSFORM(cViewName) + ' - ' ;
                   + TYPE('cViewName ')+' /end/ '
ENDPROC
```

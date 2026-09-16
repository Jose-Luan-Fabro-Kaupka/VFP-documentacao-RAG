# Evento dbc_AfterDropView

Ocorre após a definição de view SQL ser removida do banco de dados atual. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDropView(cViewName)
```

```foxpro
PROCEDURE dbc_AfterDropView
LPARAMETERS cViewName
```

#### Parâmetros
 **cViewName**
Especifica o nome da view excluída do banco de dados atual.

# Observações

DROP VIEW é quase idêntico a DELETE VIEW; DROP VIEW é a sintaxe padrão ANSI SQL para excluir uma view SQL. Ambos os comandos removem uma definição de view do banco de dados ativo, mas a sintaxe é ligeiramente diferente.

Você pode usar o evento dbc_AfterDropView para rastrear o acesso ao banco de dados após uma definição de view ser removida do banco de dados.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterDropView ;
         (cViewName)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     cViewName  = ' + TRANSFORM(cViewName) + ' - ' ;
                    + TYPE('cViewName ')+' /end/ '
ENDPROC
```

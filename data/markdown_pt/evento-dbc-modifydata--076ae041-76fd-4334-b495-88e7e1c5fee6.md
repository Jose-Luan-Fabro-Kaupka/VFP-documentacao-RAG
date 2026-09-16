# Evento dbc_ModifyData

Ocorre imediatamente após a emissão de MODIFY DATABASE. Use para impedir a abertura da janela do Database Designer. Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_ModifyData(cDatabaseName, lNoWait, lNoEdit )
```

```foxpro
PROCEDURE dbc_ModifyData
LPARAMETERS [cDatabaseName, lNoWait, lNoEdit ]
```

#### Parâmetros
 **CDatabaseName**
Especifica o nome do banco de dados que está sendo modificado.
**lNoWait**
Especifica se a palavra-chave NOWAIT foi incluída no comando MODIFY DATABASE, o que faria a execução do programa continuar após a abertura do Database Designer.
**lNoEdit**
Especifica se a palavra-chave NOEDIT foi incluída no comando MODIFY DATABASE, o que impediria a edição do banco de dados.

# Observações

Você pode usar o evento dbc_ModifyData para rastrear o acesso ao banco de dados quando ele é modificado. Retorne .F. desse procedimento para impedir que o banco de dados seja modificado.

# Exemplo

```foxpro
PROCEDURE dbc_ModifyData ;
         (CDatabaseName, ;
            lNoWait, ;
            lNoEdit)
? '     cDatabaseName = ' + cDatabaseName + ' - ' ;
                      + TYPE('cDatabaseName ')
 ? '     lNoWait       = ' + TRANSFORM(lNoWait) + ' - ' ;
                       + TYPE('lNoWait')
 ? '     lNoEdit       = ' + TRANSFORM(lNoEdit) + ' - ' ;
                       + TYPE('lNoEdit')+' /end/ '
* Stop user from changing the database in the Designer.
IF lNoEdit
   RETURN .T.
ELSE
   RETURN .F.
ENDIF
ENDPROC
```

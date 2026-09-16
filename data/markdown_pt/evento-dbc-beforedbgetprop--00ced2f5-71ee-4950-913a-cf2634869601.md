# Evento dbc_BeforeDBGetProp

Ocorre antes da execução da função DBGetProp( ). Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDBGetProp(cName, cType, cProperty)
```

```foxpro
PROCEDURE dbc_BeforeDBGetProp
LPARAMETERS cName, cType, cProperty
```

#### Parâmetros
 **cName**
Especifica o valor do primeiro parâmetro da função DBGetProp( ): o nome do banco de dados, campo, conexão nomeada, tabela ou exibição sobre o qual DBGETPROP( ) retorna informações.
**cType**
Especifica o valor do segundo parâmetro da função DBGetProp( ): o tipo de objeto do item nomeado em cName.
**cProperty**
Especifica o valor do terceiro parâmetro da função DBGetProp( ): a propriedade sobre a qual DBGETPROP( ) retorna informações.

# Observações

Você pode usar o evento dbc_BeforeDBGetProp para rastrear tentativas de acesso ao banco de dados antes da execução de DBGetProp( ).

Retorne .F. deste procedimento para impedir que o valor da propriedade seja retornado a DBGetProp(). Isso fará a função DBGetProp() retornar NULL.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeDBGetProp ;
         (cName,;
          cType,;
          cProperty)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC: ' + SUBSTR(DBC(),RAT('\',DBC())+1)
 ? '     cName     =  ' + TRANSFORM(cName)     + ' - ' + TYPE('cName')
 ? '     cType     =  ' + TRANSFORM(cType)     + ' - ' + TYPE('cType')
 ? '     cProperty =  ' + TRANSFORM(cProperty) + ' - ' + TYPE('cProperty')+' /end/ '
ENDPROC
```

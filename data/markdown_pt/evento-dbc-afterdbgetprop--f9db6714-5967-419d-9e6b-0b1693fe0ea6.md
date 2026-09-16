# Evento dbc_AfterDBGetProp

Ocorre depois que a função DBGetProp( ) é concluída. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDBGetProp(cName, cType, cProperty)
```

```foxpro
PROCEDURE dbc_AfterDBGetProp
LPARAMETERS cName, cType, cProperty
```

#### Parâmetros
 **cName**
Especifica o valor do primeiro parâmetro na função DBGetProp(), o nome do banco de dados, campo, conexão nomeada, tabela ou view para o qual DBGETPROP( ) retorna informações.
**cType**
Especifica o valor do segundo parâmetro na função DBGetProp(), o tipo de objeto do item nomeado em cName.
**cProperty**
Especifica o valor do terceiro parâmetro na função DBGetProp(), a propriedade para a qual DBGETPROP( ) retorna informações.

Para detalhes sobre valores válidos de cType e cProperty, consulte a Ajuda.

# Observações

Você pode usar o evento dbc_AfterDBGetProp para rastrear o acesso ao banco de dados depois que DBGetProp é executado.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterDBGetProp ;
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

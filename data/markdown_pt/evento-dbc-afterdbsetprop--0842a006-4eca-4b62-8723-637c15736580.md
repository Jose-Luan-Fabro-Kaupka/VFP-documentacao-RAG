# Evento dbc_AfterDBSetProp

Ocorre após a conclusão da função DBSetProp( ). Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterDBSetProp(cName, cType, cProperty, ePropertyValue)
```

```foxpro
PROCEDURE dbc_AfterDBSetProp
LPARAMETERS cName, cType, cProperty, ePropertyValue
```

#### Parâmetros
 **cName**
Especifica o valor do primeiro parâmetro da função DBGetProp( ), o nome do banco de dados, campo, conexão nomeada, tabela ou exibição cujo valor é alterado por DBSETPROP( ).
**cType**
Especifica o valor do segundo parâmetro da função DBSetProp( ), o tipo de objeto do item nomeado em cName.
**cProperty**
Especifica o valor do terceiro parâmetro da função DBSetProp( ), a propriedade cujo valor é alterado por DBSETPROP( ).
**ePropertyValue**
Especifica o valor do quarto parâmetro da função DBSetProp( ), o valor a ser atribuído à propriedade em cProperty.

Para obter detalhes sobre valores válidos de cType e cProperty, consulte Função DBSETPROP( ) e Função DBGETPROP( ) na Ajuda.

# Observações

Você pode usar o evento dbc_AfterDBCSetProp para rastrear o acesso ao banco de dados após a execução de DBGETPROP( ).

Alguns valores de propriedades podem ser alterados usando DBSetProp( ) ou um designer. Por exemplo, você pode alterar a propriedade Comment de uma tabela usando DBSetProp( ) ou o designer de tabelas. Como DBSetProp( ) faz alterações diretamente no próprio banco de dados, os eventos dbc_BeforeModifyTable e dbc_AfterModifyTable não capturam alterações feitas por DBSETPROP( ). Para interceptar alterações que possam ser feitas de qualquer uma das formas, use os eventos dbc_BeforeDBSetProp, dbc_AfterDBSetProp, dbc_BeforeModifyTable e dbc_AfterModifyTable para verificar as alterações apropriadas.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_AfterDBSetProp ;
         (cName,;
          cType,;
          cProperty,;
          ePropertyValue)
 ? '>>   ' + PROGRAM()
 ?? ' in ' + SUBSTR(SYS(16),RAT('\',SYS(16))+1)
 ? '     Current DBC:     ' + SUBSTR(DBC(),RAT('\',DBC())+1)
 ? '     cName          = ' + TRANSFORM(cName)          + ' - ' + TYPE('cName')
 ? '     cType          = ' + TRANSFORM(cType)          + ' - ' + TYPE('cType')
 ? '     cProperty      = ' + TRANSFORM(cProperty)      + ' - ' + TYPE('cProperty')
 ? '     ePropertyValue = ' + TRANSFORM(ePropertyValue) + ' - ' + TYPE('ePropertyValue')+' /end/ '
ENDPROC
```

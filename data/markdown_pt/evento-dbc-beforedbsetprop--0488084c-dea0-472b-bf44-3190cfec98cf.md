# Evento dbc_BeforeDBSetProp

Ocorre antes da execução de DBSetProp( ). Há duas versões da sintaxe.

```foxpro
PROCEDURE dbc_BeforeDBSetProp(cName, cType, cProperty, ePropertyValue)
```

```foxpro
PROCEDURE dbc_BeforeDBSetProp
LPARAMETERS cName, cType, cProperty, ePropertyValue
```

#### Parâmetros
 **cName**
Especifica o valor do primeiro parâmetro da função DBGetProp( ), o nome do banco de dados, campo, conexão nomeada, tabela ou exibição para o qual DBSETPROP( ) altera o valor.
**cType**
Especifica o valor do segundo parâmetro da função DBSetProp( ), o tipo de objeto do item nomeado em cName.
**cProperty**
Especifica o valor do terceiro parâmetro da função DBSetProp( ), a propriedade cujo valor DBSETPROP( ) altera.
**ePropertyValue**
Especifica o valor do quarto parâmetro da função DBSetProp( ), o valor a ser atribuído à propriedade indicada em cProperty.

Para obter detalhes sobre valores válidos de cType e cProperty, consulte as funções DBSETPROP( ) e DBGETPROP( ) na Ajuda.

# Observações

Você pode usar o evento dbc_BeforeDBSetProp para acompanhar tentativas de acesso ao banco de dados antes da execução da função DBSETPROP( ).

Retorne .F. desse procedimento para impedir que o valor seja definido. Isso fará a função DBSetProp() retornar .F..

Alguns valores de propriedade podem ser alterados por DBSetProp( ) ou por um designer. Por exemplo, Comment de uma tabela pode ser alterada das duas maneiras. Como DBSetProp( ) altera diretamente o banco de dados, os eventos dbc_BeforeModifyTable e dbc_AfterModifyTable não capturam essas mudanças. Para capturar alterações feitas por qualquer meio, use dbc_BeforeDBSetProp, dbc_AfterDBSetProp, dbc_BeforeModifyTable e dbc_AfterModifyTable.

# Exemplo

```foxpro
* Reports to the screen Event name, where it is called from and ;
* the parameter passed.
PROCEDURE dbc_BeforeDBSetProp ;
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

# Evento AfterUpdate

Ocorre imediatamente após uma operação de atualização para um registro ser executada.

> **Observação:** Se a atualização em lote é usada, ou seja, a propriedade BatchUpdateCount do CursorAdapter é maior que 1, AfterUpdate não ocorre.

```foxpro
PROCEDURE Object.AfterUpdate
LPARAMETERS cFldState, lForce, nUpdateType, UpdateInsertCmd, DeleteCmd, lResult
```

#### Parâmetros
 **cFldState**
Especifica os estados de campo da linha sendo processada. Este é o mesmo valor obtido ao chamar a seguinte função: GETFLDSTATE(-1) Por exemplo, este valor pode ser uma cadeia de caracteres consistindo em valores de status de exclusão e edição para todos os campos na tabela ou cursor. Se uma tabela tem cinco campos e apenas o primeiro campo foi editado, GETFLDSTATE( ) retorna um valor de 121111. O número 1 na primeira posição indica que o status de exclusão não foi alterado.
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE( ).
**nUpdateType**
Especifica o valor do parâmetro nUpdateType do evento BeforeUpdate.
**UpdateInsertCmd**
Especifica o valor do parâmetro UpdateInsertCmd do evento BeforeUpdate.
**DeleteCmd**
Especifica o valor do parâmetro DeleteCmd do evento BeforeUpdate.
**lResult**
Especifica o valor retornado ao executar TABLEUPDATE( ) para este registro. A tabela a seguir descreve os valores de lResult. lResult Descrição True (.T.) Limpa os estados de campo do registro. False (.F.) Não limpa os estados de campo do registro. Você pode alterar o valor de lResult para substituir o resultado retornado.

# Observações

Aplica-se a: classe CursorAdapter

Você pode chamar a função AERROR( ) para recuperar erros de fontes de dados upstream.

No Visual FoxPro 9.0, o registro de destino é mantido atual em um ADODB.Recordset durante o evento AfterUpdate.

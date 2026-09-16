# Evento AfterInsert

Ocorre imediatamente após a execução de uma operação de inserção de registro.

> **Observação:** Se a atualização em lote é usada, ou seja, a propriedade BatchUpdateCount do CursorAdapter é maior que 1, AfterInsert não ocorre.

```foxpro
PROCEDURE Object.AfterInsert
LPARAMETERS cFldState, lForce, cInsertCmd, lResult
```

#### Parâmetros
 **cFldState**
Especifica os estados dos campos da linha sendo processada. Este é o mesmo valor obtido ao chamar a seguinte função: GETFLDSTATE(-1) Por exemplo, este valor pode ser uma cadeia de caracteres consistindo em valores de status de exclusão e edição para todos os campos na tabela ou cursor. Se uma tabela tem cinco campos e apenas o primeiro campo foi editado, GETFLDSTATE() retorna um valor de 121111. O número 1 na primeira posição indica que o status de exclusão não foi alterado.
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE().
**cInsertCmd**
Especifica o valor do parâmetro cInsertCmd do evento BeforeInsert.
**lResult**
Especifica o valor retornado pela execução de TABLEUPDATE( ) para este registro. Se lResult é True (.T.), os estados dos campos são limpos para este registro. Se lResult é False (.F.), os estados dos campos não são limpos para este registro. Você pode alterar o valor de lResult para substituir o resultado retornado.

# Observações

Aplica-se a: Classe CursorAdapter

Você pode chamar a função AERROR( ) para recuperar erros de fontes de dados upstream.

No Visual FoxPro 9.0, o registro de destino permanece atual em um ADODB.Recordset durante o evento AfterInsert.

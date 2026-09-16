# Evento BeforeInsert

Ocorre imediatamente antes que um comando de inserção para um registro seja executado.

> **Observação:** Se a atualização em lote é usada, ou seja, a propriedade BatchUpdateCount do CursorAdapter é maior que 1, BeforeInsert não ocorre.

```foxpro
PROCEDURE Object.BeforeInsert
LPARAMETERS cFldState, lForce, cInsertCmd
```

#### Parâmetros
 **cFldState**
Especifica os estados dos campos da linha sendo processada. Este é o mesmo valor obtido ao chamar a seguinte função: GETFLDSTATE(-1) Por exemplo, este valor pode ser uma cadeia de caracteres consistindo em valores de status de exclusão e edição para todos os campos na tabela ou cursor. Se uma tabela tem cinco campos e apenas o primeiro campo foi editado, GETFLDSTATE( ) retorna um valor de 121111. O número 1 na primeira posição indica que o status de exclusão não foi alterado.
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE( ).
**cInsertCmd**
Especifica o valor da propriedade InsertCmd. O Visual FoxPro usa o valor de cInsertCmd como o comando de inserção, que você pode alterar neste evento. No entanto, se você alterar o valor do parâmetro cInsertCmd, o valor da propriedade InsertCmd não é alterado.

# Observações

Aplica-se a: CursorAdapter Class

Se o código em BeforeInsert retornar False (.F.), a operação de inserção não ocorre.

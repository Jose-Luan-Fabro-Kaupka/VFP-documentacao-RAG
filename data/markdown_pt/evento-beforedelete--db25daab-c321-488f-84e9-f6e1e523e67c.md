# Evento BeforeDelete

Ocorre imediatamente antes da execução de um comando de exclusão de um registro.

> **Observação:** Se a atualização em lote for usada, ou seja, a propriedade BatchUpdateCount do CursorAdapter for maior que 1, BeforeDelete não ocorre.

```foxpro
PROCEDURE Object.BeforeDelete
LPARAMETERS cFldState, lForce, cDeleteCmd
```

#### Parâmetros
 **cFldState**
Especifica os estados de campo da linha sendo processada. Este é o mesmo valor obtido ao chamar a seguinte função: GETFLDSTATE(-1) Por exemplo, este valor pode ser uma cadeia de caracteres consistindo em valores de status de exclusão e edição para todos os campos na tabela ou cursor. Se uma tabela tiver cinco campos e somente o primeiro campo tiver sido editado, GETFLDSTATE( ) retorna um valor de 121111. O número 1 na primeira posição indica que o status de exclusão não foi alterado.
**lForce**
Especifica o valor do parâmetro lForce da função TABLEUPDATE( ).
**cDeleteCmd**
Especifica o valor da propriedade DeleteCmd. O Visual FoxPro usa o valor de cDeleteCmd como o comando de exclusão, que você pode alterar neste evento. No entanto, se você alterar o valor do parâmetro cDeleteCmd, o valor da propriedade DeleteCmd não muda.

# Observações

Aplica-se a: CursorAdapter Class

Se o código em BeforeDelete retornar False (.F.), a operação de exclusão não ocorre.

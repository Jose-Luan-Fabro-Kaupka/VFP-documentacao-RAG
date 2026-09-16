# Evento BeforeCursorFill

Ocorre imediatamente antes de um objeto CursorAdapter tentar anexar um novo cursor.

```foxpro
PROCEDURE Object.BeforeCursorFill
LPARAMETERS lUseCursorSchema, lNoDataOnLoad, cSelectCmd
```

#### Parâmetros
 **lUseCursorSchema**
Especifica o valor do parâmetro lUseCursorSchema do método CursorFill.
**lNoDataOnLoad**
Especifica o valor da propriedade lNoData em CursorFill .
**cSelectCmd**
Especifica o valor atual da propriedade SelectCmd. Você pode alterar o valor do parâmetro cSelectCmd neste evento. No entanto, o valor na propriedade SelectCmd não muda. Se você alterar o valor do parâmetro cSelectCmd neste evento, o Visual FoxPro usa o valor alterado de cSelectCmd .

# Observações

Aplica-se a: CursorAdapter Class

O Visual FoxPro armazena as alterações de valor, que são usadas por CursorFill. O método CursorRefresh usa o valor do parâmetro SelectCmd, não a propriedade SelectCmd. Isso facilita a construção de consultas personalizadas "sob demanda". Por exemplo, você pode armazenar um comando SELECT – SQL básico na propriedade SelectCmd e adicionar uma cláusula WHERE ao parâmetro SelectCmd neste evento sem alterar o valor subjacente da propriedade. O valor do parâmetro SelectCmd é então passado ao evento AfterCursorFill.

Se o código em BeforeCursorFill retornar um valor False (.F.), CursorFill não é executado e o cursor atualmente anexado permanece aberto. No entanto, se o código em BeforeCursorFill não retornar false, o cursor atualmente anexado é fechado e CursorFill é executado.

Alterações feitas nesses parâmetros têm precedência sobre os valores originais armazenados nas respectivas propriedades ou passados para CursorFill.

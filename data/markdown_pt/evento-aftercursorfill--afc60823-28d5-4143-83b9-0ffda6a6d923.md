# Evento AfterCursorFill

Ocorre imediatamente após um objeto CursorAdapter tentar criar um novo cursor.

```foxpro
PROCEDURE Object.AfterCursorFill
LPARAMETERS lUseCursorSchema, lnoDataOnLoad, cSelectCmd, lResult
```

#### Parâmetros
 **lUseCursorSchema**
Especifica o valor no parâmetro lUseCursorSchema do método CursorFill.
**lnoDataOnLoad**
Especifica o valor no parâmetro lNoData de CursorFill.
**cSelectCmd**
Especifica o mesmo parâmetro SelectCmd usado pelo evento BeforeCursorFill.
**lResult**
Especifica o valor True (.T.) ou False (.F.) retornado por CursorFill.

# Observações

Aplica-se a: CursorAdapter Class

Se qualquer um dos três primeiros parâmetros for alterado em BeforeCursorFill, AfterCursorFill usa os valores alterados em vez dos valores reais nas propriedades, que não mudam.

No Visual FoxPro 9.0, o registro de destino é mantido atual em um ADODB.Recordset durante o evento AfterCursorFill.

# Exemplo

O exemplo a seguir ilustra o uso do evento AfterCursorFill para definir a ordem do índice a partir de uma propriedade predefinida:

```foxpro
PROCEDURE AfterCursorFill
LPARAMETERS lUseCursorSchema, noDataOnLoad, cSelectCmd, lResult
SELECT (this.Alias)
SET ORDER TO (this.Order)
ENDPROC
```

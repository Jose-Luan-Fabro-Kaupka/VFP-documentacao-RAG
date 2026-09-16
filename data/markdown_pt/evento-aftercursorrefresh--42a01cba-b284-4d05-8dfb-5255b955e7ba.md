# Evento AfterCursorRefresh

Ocorre após um objeto CursorAdapter tentar atualizar.

```foxpro
PROCEDURE Object.AfterCursorRefresh
LPARAMETERS cSelectCmd, lResult
```

#### Parâmetros
 **cSelectCmd**
Especifica o valor atual de SelectCmd conforme estabelecido no evento BeforeCursorFill. Por exemplo, se o parâmetro cSelectCmd é alterado em BeforeCursorFill, então o valor alterado de SelectCmd é usado. No entanto, o valor na propriedade SelectCmd não é alterado.
**lResult**
Especifica o valor True (.T.) ou False (.F.) retornado pelo método CursorRefresh.

# Observações

Aplica-se a: CursorAdapter Class

No Visual FoxPro 9.0, o registro de destino é mantido atual em um ADODB.Recordset durante o evento AfterCursorRefresh.

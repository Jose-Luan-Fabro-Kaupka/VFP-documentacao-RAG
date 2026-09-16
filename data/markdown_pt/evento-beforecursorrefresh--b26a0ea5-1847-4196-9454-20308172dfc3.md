# Evento BeforeCursorRefresh

Ocorre imediatamente antes de um objeto CursorAdapter tentar atualizar.

```foxpro
PROCEDURE Object.BeforeCursorRefresh
LPARAMETERS cSelectCmd
```

#### Parâmetros
 **cSelectCmd**
Especifica o valor atual de SelectCmd conforme estabelecido no evento BeforeCursorFill. Por exemplo, se o parâmetro cSelectCmd for alterado em BeforeCursorFill, o valor alterado de SelectCmd é usado. No entanto, o valor da propriedade SelectCmd não é alterado.

# Observações

Aplica-se a: CursorAdapter Class

Se o código em BeforeCursorRefresh retornar um valor False (.F.), o objeto CursorAdapter não atualiza.

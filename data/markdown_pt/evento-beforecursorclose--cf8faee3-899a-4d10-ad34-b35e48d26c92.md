# Evento BeforeCursorClose

Ocorre imediatamente antes de um cursor ser fechado. Você pode usar este evento para executar quaisquer operações necessárias antes de fechar um cursor ou tabela, e assim por diante.

```foxpro
PROCEDURE Object.BeforeCursorClose
LPARAMETERS cAlias
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou tabela que está sendo fechado.

# Observações

Aplica-se a: CursorAdapter Class

Se o código em BeforeCursorClose retornar um valor False (.F.), o cursor não é fechado e o Visual FoxPro gera uma mensagem de erro.

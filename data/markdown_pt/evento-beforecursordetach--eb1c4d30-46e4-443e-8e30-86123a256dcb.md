# Evento BeforeCursorDetach

Ocorre imediatamente antes de um objeto CursorAdapter desanexar um cursor. Você pode usar este evento para executar quaisquer operações necessárias antes de desanexar o cursor ou a tabela.

```foxpro
PROCEDURE Object.BeforeCursorAttach
LPARAMETERS cAlias
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou da tabela que está sendo desanexado.

# Observações

Aplica-se a: Classe CursorAdapter

Se o código em BeforeCursorDetach retornar um valor False (.F.), o cursor não é desanexado e quaisquer valores de retorno são ignorados.

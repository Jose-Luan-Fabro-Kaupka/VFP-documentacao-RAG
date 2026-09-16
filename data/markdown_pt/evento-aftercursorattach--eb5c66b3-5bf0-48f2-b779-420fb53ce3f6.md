# Evento AfterCursorAttach

Ocorre imediatamente após o objeto CursorAdapter tentar anexar o cursor. Você pode usar este evento para executar tarefas como personalizar cursors e cursor adapters conforme apropriado e realizar validações.

```foxpro
PROCEDURE Object.AfterCursorAttach
LPARAMETERS cAlias, lResult
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou da tabela anexado.
**lResult**
Especifica True (.T.) se o cursor ou a tabela foi anexado com êxito e False (.F.) se não foi anexado com êxito.

# Observações

Aplica-se a: Classe CursorAdapter

No Visual FoxPro 9.0, o registro de destino permanece atual em um ADODB.Recordset durante o evento AfterCursorAttach.

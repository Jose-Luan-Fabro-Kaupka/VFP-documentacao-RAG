# Evento AfterCursorDetach

Ocorre imediatamente depois que um objeto CursorAdapter desanexa um cursor. Você pode usar AfterCursorDetach para executar tarefas como redefinir propriedades do cursor adapter e realizar operações na tabela liberada.

```foxpro
PROCEDURE Object.AfterCursorAttach
LPARAMETERS cAlias, lResult
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou tabela desanexado.
**lResult**
Especifica True (.T.) se o método CursorAdapterCursorDetach desanexou o cursor ou tabela com sucesso e False (.F.) se não foi desanexado com sucesso.

# Observações

Aplica-se a: CursorAdapter Class

No Visual FoxPro 9.0, o registro de destino permanece atual no ADODB.Recordset durante o evento AfterCursorDetach.

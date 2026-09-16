# Evento BeforeCursorAttach

Ocorre imediatamente antes de o objeto CursorAdapter tentar anexar um cursor. Você pode usar este evento para executar as operações necessárias antes de anexar o cursor ou a tabela, determinar um alias a anexar e assim por diante.

```foxpro
PROCEDURE Object.BeforeCursorAttach
LPARAMETERS cAlias
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou da tabela que está sendo anexada.

# Observações

Aplica-se a: classe CursorAdapter

Se o código de BeforeCursorAttach retornar False (.F.), o cursor não será anexado.

> **Observação:** O objeto CursorAdapter respeita quaisquer alterações feitas no parâmetro cAlias por BeforeCursorAttach.

# Exemplo

O exemplo a seguir mostra como abrir uma exibição local em BeforeCursorAttach para anexá-la a um objeto CursorAdapter:

```foxpro
PROCEDURE BeforeCursorAttach
OPEN DATABASE HOME(2)+"tastrade\data\tastrade.dbc"
USE 'product listing'
ENDPROC
```

Em seguida, faça a chamada a seguir para anexar a exibição:

```foxpro
CursorAttach('product listing', .T.)
```

# Evento AfterCursorClose

Ocorre imediatamente após um cursor ser fechado. Você pode usar este evento para redefinir propriedades do CursorAdapter e assim por diante.

```foxpro
PROCEDURE Object.AfterCursorClose
LPARAMETERS cAlias, lResult
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou tabela fechado.
**lResult**
Especifica True (.T.) se o cursor ou tabela for fechado com sucesso e False (.F.) se não for fechado com sucesso, por exemplo, se o cursor contiver alterações não salvas.

# Observações

Aplica-se a: CursorAdapter Class

Você deve limpar ou redefinir a propriedade Alias se desejar remover seu valor anterior. Quando um cursor estendido é fechado, o Visual FoxPro marca o objeto CursorAdapter como não mais vinculado a um cursor, mas não limpa a propriedade Alias.

# Comando SET WINDOW OF MEMO

Incluído para compatibilidade com versões anteriores. Use o TextBox Control (Visual FoxPro).

Especifica uma janela na qual os campos memo são editados.

```foxpro
SET WINDOW OF MEMO TO window name
```

#### Parâmetros
 window name

 Especifique o nome da janela na qual deseja editar os campos memo com window name.

# Observações

SET WINDOW OF MEMO é incluído para compatibilidade com versões anteriores. Use @ ...EDIT.

Use SET WINDOW para editar campos memo em uma janela definida pelo usuário. Você pode então abrir a janela de edição de memo emitindo @ ... GET, APPEND, BROWSE, CHANGE, EDIT ou MODIFY MEMO. A janela definida pelo usuário na qual o editor de memo é colocado deve ser definida antes de você a incluir em SET WINDOW OF MEMO.

Para editar um campo memo na janela especificada, mova o cursor para o campo memo e pressione Ctrl+Home, Ctrl+Page Up ou Ctrl+Page Down, ou clique duas vezes no campo memo.

# Propriedade FetchMemo

Especifica se os campos memo são buscados com os resultados da view. Ao manipular esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir FetchMemo se aplica apenas a objetos CursorAdapter com fontes de dados ODBC ou ADO e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.FetchMemo [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores para lValue. lValue Description True (.T.) Busca campos memo com os resultados da view. False (.F.) Não busca campos memo com os resultados da view.

# Observações

Aplica-se a: CursorAdapter Class

FetchMemo se aplica principalmente a views remotas e definir isso não afeta views locais. No entanto, você pode predefinir esta propriedade para views locais que serão upsized.

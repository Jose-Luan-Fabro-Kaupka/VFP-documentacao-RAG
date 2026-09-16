# Propriedade SendUpdates

Especifica se uma consulta de atualização SQL deve ser enviada para atualizar tabelas. Ao manipular esta propriedade para cursores regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir SendUpdates aplica-se apenas a objetos CursorAdapter com fontes de dados ODBC ou ADO e substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP( ) não tem efeito.

```foxpro
CursorAdapter.SendUpdates [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores para lValue. lValue Description True (.T.) Send an SQL update query to update tables when a view is used to make the update. (Default) False (.F.) Do not send an SQL update query to update tables.

# Observações

Aplica-se a: CursorAdapter Class

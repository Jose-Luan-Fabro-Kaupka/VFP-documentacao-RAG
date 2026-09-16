# Propriedade UpdatableFieldList

Especifica uma lista separada por vírgulas de campos na view e inclui campos do cursor. Ao trabalhar com esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Você deve incluir uma lista de nomes de campos para que as atualizações funcionem ao usar atualização automática.

> **Observação:** Definir UpdatableFieldList para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.UpdatableFieldList [= cList]
```

# Valor de retorno
 **cList**
Tipo de dados caractere. O parâmetro cList especifica uma lista separada por vírgulas de campos na view e inclui campos do cursor.

# Observações

Aplica-se a: CursorAdapter Class

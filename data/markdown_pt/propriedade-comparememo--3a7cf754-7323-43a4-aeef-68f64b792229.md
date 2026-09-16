# Propriedade CompareMemo

Especifica se campos memo dos tipos Memo, General ou Picture são incluídos na cláusula WHERE ao usar atualização automática. Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP() e CURSORGETPROP(). Leitura/gravação.

> **Observação:** Definir CompareMemo para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.CompareMemo [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. A tabela a seguir lista os valores de lValue. lValue Description True (.T.) Inclui campos memo na cláusula WHERE. True (.F.) Não inclui campos memo na cláusula WHERE.

# Observações

Aplica-se a: classe CursorAdapter

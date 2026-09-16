# Propriedade KeyFieldList

Especifica uma lista separada por vírgulas de campos primários para o cursor ou objeto CursorAdapter. Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir KeyFieldList para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP( ) não tem efeito.

```foxpro
CursorAdapter.KeyFieldList [= cList]
```

# Valor de retorno
 **cList**
Tipo de dados Character. O parâmetro cList especifica uma lista separada por vírgulas de campos primários para o cursor ou objeto CursorAdapter e não tem um valor padrão. Observação Você deve incluir uma lista de nomes de campos ao usar atualização automática para que as atualizações funcionem.

# Observações

Aplica-se a: Classe CursorAdapter

# Propriedade Tables

Especifica uma lista separada por vírgulas de nomes de tabelas, que deve ter os nomes das tabelas na ordem exata em que você deseja que apareçam nos comandos SQL UPDATE, INSERT e DELETE. Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP() e CURSORGETPROP(). Leitura/gravação.

> **Observação:** Você deve incluir esta lista de nomes de tabelas ao usar atualização automática para que as atualizações funcionem.

> **Observação:** Definir Tables para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.Tables [= cList]
```

# Valor de retorno
 **cList**
Tipo de dados Character. O parâmetro cList especifica uma lista separada por vírgulas de nomes de tabelas que exibe os nomes das tabelas na ordem exata em que você deseja que apareçam nos comandos SQL UPDATE , INSERT e DELETE. Não existe configuração padrão.

# Observações

Aplica-se a: Classe CursorAdapter

Tables não deve fazer referência a um cursor que foi anexado a um objeto CursorAdapter por CursorAttach.

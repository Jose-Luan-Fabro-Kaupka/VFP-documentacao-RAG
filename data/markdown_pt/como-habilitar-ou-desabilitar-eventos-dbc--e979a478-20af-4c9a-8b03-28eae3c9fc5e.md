# Como: habilitar ou desabilitar eventos DBC

Antes de adicionar código de procedure aos eventos do Database Container (DBC), você precisa ativá-los. Quando não deseja executar código em eventos DBC, pode desativá-los.

> **Cuidado:** Eventos DBC não estão disponíveis em versões anteriores ao Visual FoxPro 7.0. Portanto, ativar eventos DBC torna o banco de dados incompatível com versões anteriores ao Visual FoxPro 7.0. Tentar acessar um banco de dados com eventos DBC habilitados usando uma versão anterior ao Visual FoxPro 7.0 gera um erro.

### Para ativar eventos DBC
- Abra o banco de dados no Database Designer .
- No menu Database, clique em Properties .
- Na caixa de diálogo Database Properties, clique em Set Events On .
- Clique em OK .

Para obter mais informações, consulte Database Properties Dialog Box.

### Para ativar eventos DBC programaticamente
- Certifique-se de que o banco de dados esteja aberto como o banco de dados atual.
- Use a função DBSETPROP( ).

Por exemplo, o código a seguir ativa eventos DBC:

```foxpro
DBSETPROP(cDBCName,'Database','DBCEvents',.T.)
```

Para obter mais informações, consulte DBSETPROP( ) Function.

### Para desativar eventos DBC
- Abra o banco de dados no Database Designer .
- No menu Database, clique em Properties .
- Na caixa de diálogo Database Properties, desmarque Set Events On .
- Clique em OK .

Para obter mais informações, consulte Database Properties Dialog Box.

### Para desativar eventos DBC programaticamente
- Use a função DBSETPROP( ).

Por exemplo, o código a seguir desativa eventos DBC:

```foxpro
DBSETPROP(cDBCName,'Database','DBCEvents',.F.)
```

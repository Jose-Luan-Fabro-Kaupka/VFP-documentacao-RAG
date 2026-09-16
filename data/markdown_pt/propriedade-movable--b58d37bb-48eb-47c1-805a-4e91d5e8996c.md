# Propriedade Movable

Especifica se um objeto pode ser movido em tempo de execução pelo usuário. Disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.Movable[ = lExpr]
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Movable são: Configuração Descrição True (.T.) (Padrão) O objeto pode ser movido. Para formulários no Visual FoxPro for Windows, o comando Move é adicionado ao menu Control. False (.F.) O objeto não pode ser movido. Para colunas de grade, você não pode mover a coluna por manipulação direta. Porém, a coluna pode ser movida se você alterar a propriedade ColumnOrder da coluna ou mover outra coluna sobre ela.

# Observações

Aplica-se a: Column Object | Form Object | _SCREEN System Variable | ToolBar Object

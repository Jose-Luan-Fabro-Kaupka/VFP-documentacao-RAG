# Função REQUERY( )

Recupera os dados novamente para uma view SQL.

```foxpro
REQUERY([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho na qual a view SQL está aberta.
**cTableAlias**
Especifica o alias da view SQL. Se você omitir nWorkArea e cTableAlias, os dados da view SQL aberta na área de trabalho atualmente selecionada são recuperados.

# Valor de retorno

Numeric. REQUERY( ) retorna 1 se os dados são recuperados com sucesso; caso contrário, retorna 0.

# Observações

REQUERY( ) é normalmente usado para atualizar uma view SQL quando os dados foram alterados na fonte de dados.

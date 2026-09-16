# Propriedade ParentAlias

Especifica o nome de alias da tabela pai. Somente leitura em tempo de design e em tempo de execução.

```foxpro
DataEnvironment.Relation.ParentAlias[ = cAliasName]
```

# Valor de retorno
 **cAliasName**
Especifica o nome de alias da tabela pai na relação.

# Observações

Aplica-se a: Relation Object

A configuração da propriedade ParentAlias deve ser o mesmo nome da configuração da propriedade Alias do objeto Cursor que representa a tabela pai.

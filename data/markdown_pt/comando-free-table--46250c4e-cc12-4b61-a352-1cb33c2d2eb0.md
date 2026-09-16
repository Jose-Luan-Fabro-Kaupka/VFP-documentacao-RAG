# Comando FREE TABLE

Remove uma referência de banco de dados de uma tabela.

```foxpro
FREE TABLE TableName
```

#### Parâmetros
 **TableName**
Especifica o nome da tabela da qual a referência de banco de dados é removida.

# Observações

Se um banco de dados for excluído acidentalmente do disco, as referências ao banco de dados permanecem nas tabelas que anteriormente estavam contidas no banco de dados. FREE TABLE remove as referências de banco de dados de uma tabela, tornando possível abrir a tabela ou adicioná-la a um banco de dados diferente.

> **Cuidado:** FREE TABLE nunca deve ser emitido para remover uma tabela de um banco de dados se o banco de dados existir no disco. Se o banco de dados existir no disco, FREE TABLE pode tornar o banco de dados inutilizável. Use REMOVE TABLE em vez disso. Diferentemente de FREE TABLE, REMOVE TABLE remove todas as referências do banco de dados a índices primários, valores padrão e regras de validação associadas à tabela.

# Comando END TRANSACTION

Encerra a transação atual e salva quaisquer alterações feitas em tabelas, arquivos de memo de tabela ou arquivos de índice incluídos em uma transação.

```foxpro
END TRANSACTION
```

# Observações

Quaisquer atualizações no banco de dados que foram feitas entre o BEGIN TRANSACTION anterior e o END TRANSACTION são confirmadas. Se a transação é a primeira ou única transação (ou seja, a transação não está aninhada), as alterações são gravadas no disco.

Se uma transação estiver aninhada, END TRANSACTION faz com que todas as atualizações em cache sejam incorporadas ao próximo nível de transação superior. O aninhamento de transações tem o potencial de sobrescrever alterações feitas nos dados em um nível de transação superior.

Se END TRANSACTION gerar um erro (por exemplo, não há espaço em disco suficiente para gravar as alterações no disco), as alterações feitas durante a transação são canceladas e a transação é encerrada.

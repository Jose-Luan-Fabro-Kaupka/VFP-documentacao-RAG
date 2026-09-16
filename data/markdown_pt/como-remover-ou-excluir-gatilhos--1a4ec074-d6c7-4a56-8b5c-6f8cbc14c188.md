# Como: remover ou excluir gatilhos

Você pode remover um gatilho de uma tabela de banco de dados pela interface ou com o comando DELETE TRIGGER.

### Para excluir um gatilho
- Na guia Tabela do Designer de Tabelas (Visual FoxPro), selecione a expressão de gatilho na caixa Gatilho de inserção, Gatilho de atualização ou Gatilho de exclusão e exclua-a. -ou-
- Use o comando DELETE TRIGGER.

O exemplo a seguir remove o gatilho de atualização da tabela `customer`:

```foxpro
DELETE TRIGGER ON customer FOR UPDATE
```

Se você remover ou excluir uma tabela de um banco de dados, todos os gatilhos vinculados a essa tabela serão excluídos do banco de dados. No entanto, os procedimentos armazenados referenciados pelo gatilho removido ou excluído não serão excluídos.

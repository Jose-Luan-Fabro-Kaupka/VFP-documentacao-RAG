# Evento AfterCloseTables

Ocorre depois que as tabelas ou exibições especificadas no ambiente de dados de um formulário, conjunto de formulários ou relatório são liberadas.

```foxpro
PROCEDURE DataEnvironment.AfterCloseTables
```

# Observações

Aplica-se a: DataEnvironment Object

Para um formulário ou conjunto de formulários, o evento AfterCloseTables ocorre depois que o evento Unload do conjunto de formulários ou do formulário ocorre e depois que quaisquer tabelas ou exibições abertas pelo ambiente de dados são fechadas.

Para um relatório, o evento AfterCloseTables ocorre depois que quaisquer tabelas ou exibições abertas pelo ambiente de dados são fechadas.

O evento AfterCloseTables ocorre sempre que o método CloseTables é chamado. O evento Destroy do ambiente de dados e de seus objetos associados ocorre depois do evento AfterCloseTables.

# Variável de sistema _TASKLIST

Esta variável de sistema contém o nome do programa gerenciador da lista de tarefas.

```foxpro
_TASKLIST = cTasklistApplication
```

#### Parâmetros
 **cTasklistApplication**
Nome do programa Visual FoxPro que gerencia as informações da lista de tarefas. O programa gerenciador da lista de tarefas permite gerenciar a lista de bookmarks persistentes (Tasklist Shortcuts) para um documento aberto e adicionar ou excluir itens da lista de tarefas. Os itens da lista de tarefas são registros em foxtask.dbf que contêm informações de timestamp, filename, class, method, line number e line contents.

# Observações

Por padrão, _TASKLIST contém tasklist.app, instalado na pasta de aplicativos do usuário do Windows ou no local HOME( ). Você pode especificar um nome diferente para o aplicativo gerenciador da lista de tarefas.

A principal diferença entre bookmarks persistentes (Shortcuts) e Bookmarks é que Shortcuts estão disponíveis entre sessões de edição.

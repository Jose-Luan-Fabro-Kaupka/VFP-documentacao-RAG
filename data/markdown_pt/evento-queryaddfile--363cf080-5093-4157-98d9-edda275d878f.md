# Evento QueryAddFile

Ocorre imediatamente antes de um arquivo ser adicionado a um projeto.

```foxpro
PROCEDURE Object.QueryAddFile
LPARAMETERS cFileName
```

#### Parâmetros
 **cFileName**
Contém o nome do arquivo a ser adicionado ao projeto. cFileName é passado ao evento QueryAddFile depois que o método Add é executado, você escolhe Add no Project Manager ou escolhe Add File no menu Project.

# Observações

Aplica-se a: ProjectHook Object

Inclua NODEFAULT no evento QueryAddFile para impedir que um arquivo seja adicionado ao projeto.

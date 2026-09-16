# Evento QueryRunFile

Ocorre imediatamente antes de um arquivo ser executado ou um relatório ou etiqueta ser visualizado em um projeto.

```foxpro
PROCEDURE Object.QueryRunFile
LPARAMETERS oFile
```

#### Parâmetros
 **oFile**
Contém uma referência de objeto ao arquivo a ser executado ou visualizado. oFile é passado ao evento QueryRunFile após a execução do método Run, quando você escolhe Run ou Preview no Project Manager, ou quando você escolhe Run File ou Preview File no menu Project.

# Observações

Aplica-se a: ProjectHook Object

Inclua NODEFAULT no evento QueryRunFile para impedir que um arquivo seja executado ou visualizado.

# Evento QueryRemoveFile

Ocorre imediatamente antes de um arquivo ser removido de um projeto.

```foxpro
PROCEDURE Object.QueryRemoveFile
LPARAMETERS oFile, cClassName, lDeleteFile
```

#### Parâmetros
 **oFile**
Contém uma referência de objeto ao arquivo a ser removido do projeto. oFile é passado ao evento QueryRemoveFile após o método Remove ser executado, você escolher Remove no Project Manager ou escolher Remove File no menu Project.
**cClassName**
Contém o nome da classe a ser removida se o arquivo for uma biblioteca de classes visual .vcx.
**lDeleteFile**
Contém um valor lógico que indica se o arquivo deve ser excluído do disco além do projeto. lDeleteFile contém false (.F.) se Remove (remover do projeto) for escolhido na caixa de diálogo exibida quando você tenta remover um arquivo de um projeto. lDeleteFile contém true (.T.) se Delete (remover do projeto e excluir do disco) for escolhido na caixa de diálogo.

# Observações

Aplica-se a: ProjectHook Object

Inclua NODEFAULT no evento QueryRemoveFile para impedir que um arquivo seja removido do projeto.

# Evento QueryModifyFile

Ocorre imediatamente antes de um arquivo ser modificado em um projeto.

```foxpro
PROCEDURE Object.QueryModifyFile
LPARAMETERS oFile, cClassName
```

#### Parâmetros
 **oFile**
Contém uma referência ao objeto do arquivo a modificar. oFile é passado ao evento QueryModifyFile depois que o método Modify é executado, quando você escolhe Modificar no Gerenciador de Projetos ou Modificar Arquivo no menu Projeto.
**cClassName**
Contém o nome da classe a modificar se o arquivo for uma biblioteca de classes visuais .vcx.

# Observações

Aplica-se a: objeto ProjectHook

Inclua NODEFAULT no evento QueryModifyFile para impedir que um arquivo seja modificado no projeto.

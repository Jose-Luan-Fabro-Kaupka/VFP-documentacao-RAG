# Evento QueryNewFile

Ocorre quando o botão New é pressionado no Project Manager, imediatamente antes de um arquivo ser adicionado a um projeto.

```foxpro
PROCEDURE Object.QueryNewFile
LPARAMETERS cFileType
```

#### Parâmetros
 **cFileType**
Especifica o tipo de arquivo selecionado no Project Manager quando o botão New foi pressionado. Esses valores são os mesmos da propriedade Type do objeto File. O evento QueryNewFile também é suportado em itens de contêiner de banco de dados, um caso especial, pelos seguintes valores cFileType. Valor Constante FoxPro.H Tipo de arquivo Extensão d FILETYPE_DATABASE Database .dbc D FILETYPE_FREETABLE Free table .dbf Q FILETYPE_QUERY Query .qpr K FILETYPE_FORM Form .scx R FILETYPE_REPORT Report .frx B FILETYPE_LABEL Label .lbx V FILETYPE_CLASSLIB Visual class Library .vcx P FILETYPE_PROGRAM Program .prg M FILETYPE_MENU Menu .mnx T FILETYPE_TEXT Text file varies A tabela a seguir descreve os valores cFileType para itens específicos do contêiner DBC. Exceto pela tabela DBC, que adiciona uma tabela ao projeto, esses itens afetam apenas o DBC. Valor Tipo DBC Extensão p Stored Procedure t DBC table .dbf c Connection r Remote View l Local View

# Observações

A adição de bibliotecas Visual FoxPro (.FLL files) e aplicações (.APP files) não chama o evento QueryNewFile.

Como este evento não adiciona arquivos diretamente ao projeto, se você deseja adicionar outros arquivos quando QueryNewFile é chamado, deve fazer isso explicitamente com seu próprio código, usando o Add da coleção File dos objetos Project. Por exemplo, você poderia fazer isso se quisesse que o evento QueryNewFile chamasse um Wizard, que você criou, ao adicionar um novo arquivo de um tipo específico.

# Exemplo

```foxpro
     _VFP.ActiveProject.Files.Add(mynewfile)
```

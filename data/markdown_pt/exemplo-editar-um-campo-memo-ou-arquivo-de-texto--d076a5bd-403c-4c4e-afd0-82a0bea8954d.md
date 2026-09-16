# Exemplo Editar um campo memo ou arquivo de texto

Arquivo: ...\Samples\Solution\Controls\TXT_EDT\Editbox.scx

Este exemplo permite visualizar e editar texto de um campo memo ou de um arquivo de texto em uma caixa de edição.

Exibir texto de um campo memo é tão simples quanto definir o ControlSource da caixa de edição para o campo memo.

Há duas maneiras de editar um arquivo de texto em uma caixa de edição: usando funções de arquivo de baixo nível e criando um cursor para conter o texto. Este exemplo cria um cursor em vez de usar funções de arquivo de baixo nível.

# Editar um arquivo de texto com funções de arquivo de baixo nível.

Você pode abrir um arquivo usando FOPEN( ), ler o conteúdo do arquivo usando FREAD( ) e armazenar o conteúdo em uma variável de memória ou na propriedade Value da caixa de edição. Você pode então gravar alterações no arquivo usando FWRITE( ) e fechar o arquivo usando FCLOSE( ).

# Editar um arquivo de texto carregando-o em um campo de cursor

A vantagem de criar um cursor para um arquivo de texto, além do fato de o código ser um pouco mais simples, é que o Visual FoxPro gerencia a gravação de grandes quantidades de texto em um cursor em arquivos temporários se não houver memória suficiente.

```foxpro
IF SELECT("textfile") = 0
   CREATE CURSOR textfile (filename c(60),mem m)
   APPEND BLANK
ENDIF
REPLACE textfile.FileName WITH GETFILE("TXT")
IF EMPTY(textfile.FileName)
   RETURN
ENDIF
SELECT textfile
APPEND MEMO mem FROM (textfile.FileName) OVERWRITE
THIS.Parent.edtText.ControlSource = "textfile.mem"
THIS.Parent.cmdSave.Enabled = .T.
THIS.Parent.lblFileName.Caption = ALLTRIM(textfile.FileName)
THIS.Parent.Refresh
```

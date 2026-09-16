# Comando COPY MEMO

Copia o conteúdo do campo memo especificado no registro atual para um arquivo de texto.

```foxpro
COPY MEMO MemoFieldName TO FileName   [ADDITIVE]   [AS nCodePage]
```

#### Parâmetros
 **MemoFieldName**
Especifica o nome do campo memo copiado para o arquivo de texto.
**TO FileName**
Especifica o nome de um arquivo de texto novo ou existente para o qual o campo memo é copiado. Se você não fornecer uma extensão em FileName, uma extensão .txt é atribuída. Você também pode incluir um caminho com o nome do arquivo.
**ADDITIVE**
Anexa o conteúdo do campo memo ao final do arquivo de texto especificado. Se você omitir ADDITIVE, o conteúdo do campo memo substitui o conteúdo do arquivo de texto.
**AS nCodePage**
Especifica a página de código para o arquivo de texto que COPY MEMO cria. O Visual FoxPro copia o conteúdo do campo memo especificado e, ao copiar os dados, converte automaticamente os dados para a página de código especificada para o arquivo de texto. Se você especificar um valor para nCodePage que não é suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para o arquivo que o Visual FoxPro cria. Se AS nCodePage for omitido ou for 0, nenhuma conversão de página de código ocorre.

# Exemplo

No exemplo a seguir, o conteúdo do campo memo chamado `notes` é copiado para um arquivo chamado Test.txt. O campo memo é então copiado novamente e anexado ao final do arquivo de texto.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee && Opens Employee table
COPY MEMO notes TO test.txt
WAIT WINDOW 'Memo contents now in test.txt' NOWAIT
MODIFY FILE test.txt
COPY MEMO notes TO test.txt ADDITIVE
WAIT WINDOW 'Memo contents added again to test.txt' NOWAIT
MODIFY FILE test.txt
DELETE FILE test.txt
```

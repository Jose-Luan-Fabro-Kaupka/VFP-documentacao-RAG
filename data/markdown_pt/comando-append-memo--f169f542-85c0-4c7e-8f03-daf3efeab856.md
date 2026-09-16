# Comando APPEND MEMO

Copia o conteúdo de um arquivo de texto para um campo memo.

```foxpro
APPEND MEMO MemoFieldName FROM FileName[OVERWRITE] [AS nCodePage]
```

#### Parâmetros
 **MemoFieldName**
Especifica o nome do campo memo ao qual o arquivo será anexado.
**FROM FileName**
Especifica o arquivo de texto cujo conteúdo é copiado para o campo memo. Você deve incluir o nome completo do arquivo de texto, incluindo sua extensão.
**OVERWRITE**
Substitui o conteúdo atual do campo memo pelo conteúdo do arquivo.
**AS nCodePage**
Especifica a página de código do arquivo de texto copiado para o campo memo. O Microsoft Visual FoxPro copia o conteúdo do arquivo de texto e, ao copiar os dados para o campo memo, converte automaticamente os dados da página de código que você especificar para a página de código da tabela que contém o campo memo. Se a tabela que contém o campo memo não estiver marcada com uma página de código, o Visual FoxPro converte automaticamente os dados da página de código que você especificar para a página de código Visual FoxPro atual. Se você especificar um valor para nCodePage que não seja suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para a tabela ou arquivo anexado. Se você omitir a cláusula AS nCodePage ou especificar 0 para nCodePage, nenhuma conversão de página de código ocorre para o arquivo de texto.

# Observações

O arquivo de texto inteiro é anexado ao conteúdo do campo memo especificado no registro atual se overwrite for omitido.

# Exemplo

No exemplo a seguir, o conteúdo do campo memo `notes` é copiado para um arquivo chamado Test.txt. Test.txt é então anexado ao conteúdo do campo memo. Por fim, o conteúdo de Test.txt substitui o conteúdo atual do campo memo.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE employee  && Open Employee table
WAIT WINDOW 'Employee notes memo field - press ESC' NOWAIT
MODIFY MEMO notes NOEDIT  && Open the notes memo field
COPY MEMO notes TO test.txt  && Create test file from memo field
WAIT WINDOW 'TEST.TXT text file - press ESC' NOWAIT
MODIFY FILE test.txt NOEDIT && Open the text file
WAIT WINDOW 'Employee notes now appended - press ESC' NOWAIT
APPEND MEMO notes FROM test.txt  && Add contents of text file
MODIFY MEMO notes NOEDIT  && Display memo field again
WAIT WINDOW 'Overwrite Employee notes- press ESC' NOWAIT
APPEND MEMO notes FROM test.txt OVERWRITE  && Replace notes
MODIFY MEMO notes NOEDIT NOWAIT
DELETE FILE test.txt
```

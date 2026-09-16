# Comando APPEND PROCEDURES

Anexa procedimentos armazenados em um arquivo de texto aos procedimentos armazenados no banco de dados atual.

```foxpro
APPEND PROCEDURES FROM FileName   [AS nCodePage] [OVERWRITE]
```

#### Parâmetros
 **FileName**
Especifica o nome de um arquivo de texto do qual os procedimentos armazenados são anexados.
**AS nCodePage**
Especifica a página de código do arquivo de texto do qual os procedimentos armazenados são anexados. O Visual FoxPro copia o conteúdo do arquivo de texto e, ao fazer isso, converte automaticamente o conteúdo do arquivo de texto para a página de código que você especificar. Se você especificar um valor para nCodePage que não seja suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para o arquivo de texto do qual os procedimentos armazenados são anexados. Se você omitir AS nCodePage , o Visual FoxPro copia o conteúdo do arquivo de texto do qual os procedimentos armazenados são anexados e, ao fazer isso, converte automaticamente o conteúdo do arquivo de texto para a página de código atual do Visual FoxPro. A página de código atual do Visual FoxPro pode ser determinada com CPCURRENT( ). Se nCodePage for 0, o Visual FoxPro assume que a página de código do arquivo de texto do qual os procedimentos armazenados são anexados é a mesma da página de código do banco de dados atual e que nenhuma conversão para a página de código atual do Visual FoxPro ocorre.
**OVERWRITE**
Especifica que os procedimentos armazenados atuais no banco de dados sejam substituídos pelos do arquivo de texto. Se você omitir OVERWRITE, os procedimentos armazenados atuais no banco de dados não são substituídos, e os procedimentos armazenados no arquivo de texto são anexados aos procedimentos armazenados atuais.

# Observações

APPEND PROCEDURES não está disponível em um arquivo executável distribuído. Se seu aplicativo usar este comando, ele gerará o erro "Feature is not available." Para obter mais informações sobre arquivos Visual FoxPro restritos e distribuíveis, consulte Distributable and Restricted Visual FoxPro Features and Files

Use APPEND PROCEDURES para modificar programaticamente procedimentos armazenados em um banco de dados. Um banco de dados deve estar aberto e ser o atual quando APPEND PROCEDURES é emitido; caso contrário, o Visual FoxPro gera uma mensagem de erro.

> **Observação:** Para visualizar ou editar procedimentos armazenados pela interface do usuário, use o Database Designer.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata`. Uma tabela temporária chamada `mytable` com um único campo memo é criada, e REPLACE é usado para colocar um procedimento armazenado chamado `MyProcedure` no campo memo. COPY MEMO é usado para criar um arquivo de texto temporário chamado Mytemp.txt que contém o conteúdo do campo memo.

APPEND PROCEDURES é usado para anexar o procedimento armazenado do arquivo de texto temporário ao banco de dados. DISPLAY PROCEDURES exibe os procedimentos armazenados no banco de dados e depois a tabela temporária e o arquivo de texto são apagados.

```foxpro
CLOSE DATABASES
* Open the testdata database
OPEN DATABASE (HOME(2) + 'Data\testdata')
* Create a free, temporary table with one memo field called mProcedure
CREATE TABLE mytable FREE (mProcedure M)
APPEND BLANK          && Add a blank record to mytable
* Add PROCEDURE command, name, and carriage return/linefeed to
* memo field
REPLACE mProcedure WITH "PROCEDURE MyProcedure" + CHR(13) + CHR(10)
* Copy contents of memo field to temporary file
COPY MEMO mProcedure TO mytemp.txt
USE             && Close the temporary table
APPEND PROCEDURES FROM mytemp.txt   && Copy procedure to the database
CLEAR
* Display the procedures associated with the current database
DISPLAY PROCEDURES
DELETE FILE mytable.dbf     && Erase temporary table
DELETE FILE mytable.fpt     && Erase temporary table memo file
DELETE FILE mytemp.txt      && Erase temporary text file
```

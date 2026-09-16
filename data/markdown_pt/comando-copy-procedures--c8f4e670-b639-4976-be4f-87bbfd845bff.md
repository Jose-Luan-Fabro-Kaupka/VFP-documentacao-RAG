# Comando COPY PROCEDURES

Copia procedimentos armazenados no banco de dados atual para um arquivo de texto.

```foxpro
COPY PROCEDURES TO FileName   [AS nCodePage] [ADDITIVE]
```

#### Parâmetros
 **FileName**
Especifica o nome de um arquivo de texto para o qual os procedimentos armazenados são copiados. Se o arquivo não existir, o Visual FoxPro cria automaticamente.
**AS nCodePage**
Especifica a página de código para o arquivo de texto para o qual os procedimentos armazenados são copiados. O Visual FoxPro copia os procedimentos armazenados e, ao fazer isso, converte automaticamente os procedimentos armazenados para a página de código que você especifica. Se você especificar um valor para nCodePage que não é suportado, o Visual FoxPro gera uma mensagem de erro. Você pode usar GETCP( ) para nCodePage para exibir a caixa de diálogo Code Page, permitindo especificar uma página de código para o arquivo de texto para o qual os procedimentos armazenados são copiados. Se você omitir AS nCodePage ou se AS nCodePage for 0, nenhuma conversão de página de código ocorre.
**ADDITIVE**
Anexa os procedimentos armazenados ao final do arquivo de texto especificado. Se você omitir ADDITIVE, os procedimentos armazenados substituem o conteúdo do arquivo de texto.

# Observações

Use COPY PROCEDURES com APPEND PROCEDURES para modificar programaticamente procedimentos armazenados em um banco de dados. Um banco de dados deve estar aberto e atual quando COPY PROCEDURES é emitido; caso contrário, o Visual FoxPro gera uma mensagem de erro.

# Exemplo

O exemplo a seguir abre o banco de dados `testdata` e usa COPY PROCEDURES para copiar os procedimentos para um arquivo de texto temporário chamado Myproc.txt. MODIFY FILE é usado para abrir o arquivo de texto temporário, que estará vazio se não houver procedimentos armazenados no banco de dados.

Se não houver procedimentos armazenados no banco de dados, você pode executar o exemplo no tópico do comando APPEND PROCEDURES para adicionar um procedimento ao banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
COPY PROCEDURES TO myproc.txt && Copy stored procedures to a file
MODIFY FILE myproc.txt  && Open the file
DELETE FILE myproc.txt  && Erase the file
```

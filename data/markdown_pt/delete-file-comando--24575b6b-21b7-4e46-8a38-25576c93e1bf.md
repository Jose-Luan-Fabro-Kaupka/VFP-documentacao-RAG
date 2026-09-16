# DELETE FILE Comando

Apaga um ficheiro de um disco.

```foxpro
DELETE FILE [FileName | ?] [RECYCLE]
```

Parâmetros
**FileName**
Especifica o ficheiro a apagar. Tip FileName pode conter caracteres wildcard como * e ?. Por exemplo, para excluir arquivos de backup com a extensão .bak no diretório atual, problema DELETE FILE *.BAK. Se o Nome do Ficheiro contiver espaços, inclua todo o nome do ficheiro nas aspas.
**?**
Mostra a caixa de diálogo Excluir para que você possa escolher um arquivo para excluir.
**RECYCLE**
Specifies that the file is not immediately deleted from disk and is placed in the Windows Recycle Bin. Caution Any file deleted with this command cannot be retrieved. Even when the SET SAFETY command is set to ON, you are not warned before the file is deleted.

Observações

O arquivo que você deseja excluir não pode ser aberto quando DELETE FILE é emitido. O nome do arquivo deve incluir um caminho se estiver em uma unidade ou volume diferente, ou em um diretório diferente do padrão. Uma extensão de nome de arquivo deve ser incluída.

If the file you want to delete represents a table that is part of a database, you need to remove the table from the database before deleting the file. You can use the REMOVE TABLE command before using the DELETE FILE command. If you delete a table that has an associated .FPT memo file, be sure to delete the memo file.

Este comando não gera um erro se o arquivo especificado não existir.

The DELETE FILE command is the same as the ERASE command.

Exemplo

In the following example, the structure of Customer.dbf and all records in which the country equals USA are copied to a table named `backup`. The data in `backup` is then copied to a text file, `temp`, which is opened and then deleted once closed.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
COPY STRUCTURE TO backup
USE backup
APPEND FROM customer FOR country = 'USA'
COPY TO temp TYPE DELIMITED
WAIT WINDOW 'Press Esc to close and erase temp.txt' NOWAIT
MODIFY FILE temp.txt NOEDIT
DELETE FILE temp.txt
? IIF(FILE('temp.txt'),'File not deleted','File deleted')
USE
DELETE FILE backup.dbf
```

Veja também
- ERASE Command
- REMOVE TABLE Command
- SET SAFETY Command
- Commands (Visual FoxPro)
- Referência linguística (Visual FoxPro)

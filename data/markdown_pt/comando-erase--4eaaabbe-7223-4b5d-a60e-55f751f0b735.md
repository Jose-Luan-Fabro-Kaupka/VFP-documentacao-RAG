# Comando ERASE

Exclui um arquivo do disco.

> **Cuidado:** Tenha cuidado ao usar ERASE. Qualquer arquivo excluído com este comando não pode ser recuperado. Você não é avisado antes que o arquivo seja excluído, mesmo se SET SAFETY estiver ON.

```foxpro
ERASE FileName | ? [RECYCLE]
```

#### Parâmetros
 **FileName**
Especifica o arquivo a ser excluído. Inclua o caminho com o nome do arquivo se o arquivo estiver em uma unidade ou diretório diferente da unidade ou diretório atual. FileName pode conter caracteres curinga como * e ?, por exemplo, para excluir arquivos de backup com ERASE *.BAK. Se FileName contém espaços, coloque o nome completo do arquivo entre aspas.
**?**
Exibe a caixa de diálogo Excluir, na qual você pode escolher um arquivo a excluir.
**RECYCLE**
Especifica que o arquivo não é excluído imediatamente do disco, mas colocado na Lixeira do Windows.

# Observações

Este comando não gera um erro se o arquivo especificado não existir.

O comando DELETE FILE é o mesmo que o comando ERASE.

# Exemplo

No exemplo a seguir, a estrutura de CUSTOMER.DBF e todos os registros em que o país é USA são copiados para uma tabela chamada `backup`. Os dados em `backup` são então copiados para um arquivo de texto, `temp`, que é aberto e depois excluído quando é fechado.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer  && Opens customer table
COPY STRUCTURE TO backup
USE backup
APPEND FROM customer FOR country = 'USA'
COPY TO temp TYPE DELIMITED
WAIT WINDOW 'Press Esc to close and erase temp.txt' NOWAIT
MODIFY FILE temp.txt NOEDIT
ERASE temp.txt
? IIF(FILE('temp.txt'),'File not deleted','File deleted')
USE
ERASE backup.dbf
```

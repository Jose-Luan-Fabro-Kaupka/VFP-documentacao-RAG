# Comando RENAME

Altera o nome de um arquivo para um novo nome.

> **Observação:** Não use RENAME para alterar o nome de uma tabela em um banco de dados; RENAME não altera o nome da tabela no banco de dados. Em vez disso, use RENAME TABLE para alterar o nome de uma tabela em um banco de dados. Para obter mais informações, consulte Comando RENAME TABLE.

```foxpro
RENAME FileName1 TO FileName2
```

#### Parâmetros
 **FileName1 TO FileName2**
Especifica o nome do arquivo a ser alterado e o novo nome do arquivo. Inclua uma extensão de arquivo para cada arquivo. Observação Se as extensões de arquivo não estiverem incluídas, a extensão padrão .dbf é assumida. Para renomear um arquivo que não tem extensão, inclua um ponto (.) após o nome do arquivo. Se você renomear uma tabela livre que tem um arquivo de memo .fpt associado, certifique-se de renomear o arquivo de memo.

# Observações

FileName1 e FileName2 podem conter caracteres curinga como * e ?. Por exemplo, para renomear todos os arquivos de programa com a extensão .prg no diretório ou pasta atual para arquivos de backup com extensão .bak, emita RENAME *.prg TO *.bak.

Se os arquivos não estiverem no caminho padrão, inclua caminhos com um ou ambos os nomes de arquivo.

Se FileName1 e FileName2 estiverem em diretórios ou pastas diferentes, FileName1 é movido para o diretório ou pasta de FileName2.

Quando você emite RENAME, FileName2 não pode já existir e FileName1 deve existir e não pode estar aberto.

# Exemplo

O exemplo a seguir mostra como alternar nomes de arquivo entre dois arquivos. O Visual FoxPro gerará um erro se você tentar renomear um arquivo para um nome que já existe (isso é mostrado pela instrução Try…Catch). O exemplo usa várias chamadas RENAME com um arquivo temporário extra para realizar a troca de nomes.

```foxpro
STRTOFILE("File 1", "tmpFile1.txt")
STRTOFILE("File 2", "tmpFile2.txt")
TRY
RENAME tmpFile1.txt TO tmpFile2.txt
CATCH TO oError
? oError.Message
ENDTRY
RENAME tmpFile2.txt TO tmpFile2.bkup
RENAME tmpFile1.txt TO tmpFile2.txt
RENAME tmpFile2.bkup TO tmpFile1.txt
MODIFY FILE tmpFile1.txt NOWAIT
MODIFY FILE tmpFile2.txt NOWAIT
```

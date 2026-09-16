# Função FREAD( )

Retorna um número especificado de bytes de um arquivo aberto com uma função de baixo nível.

```foxpro
FREAD(nFileHandle, nBytes)
```

#### Parâmetros
 **nFileHandle**
Especifica o número do identificador de arquivo do qual FREAD( ) retorna dados. Você pode obter nFileHandle do valor de retorno de instruções FOPEN( ) ou FCREATE( ) bem-sucedidas.
**nBytes**
Especifica o número de bytes retornados por FREAD( ) com um limite de 65.535 bytes. FREAD( ) retorna dados a partir da posição atual do ponteiro de arquivo e continua até retornar nBytes bytes ou até encontrar o final do arquivo.

# Valor de retorno

Character

# Exemplo

O exemplo a seguir usa FREAD( ) para exibir o conteúdo de um arquivo. Se o arquivo estiver vazio, uma mensagem é exibida. Antes de usar este exemplo, você deve criar um arquivo de texto de exemplo chamado Test.txt.

```foxpro
Local gnFileHandle,nSize,cString
gnFileHandle = FOPEN("test.txt")
* Seek to end of file to determine number of bytes in the file.
nSize =  FSEEK(gnFileHandle, 0, 2)     && Move pointer to EOF
IF nSize <= 0
 * If file is empty, display an error message.
 WAIT WINDOW "This file is empty!" NOWAIT
ELSE
 * If file is not empty, store the file's contents in memory
 * and display the text in the main Visual FoxPro window.
 = FSEEK(gnFileHandle, 0, 0)      && Move pointer to BOF
 cString = FREAD(gnFileHandle, nSize)
 ? cString
ENDIF
= FCLOSE(gnFileHandle)         && Close the file
```

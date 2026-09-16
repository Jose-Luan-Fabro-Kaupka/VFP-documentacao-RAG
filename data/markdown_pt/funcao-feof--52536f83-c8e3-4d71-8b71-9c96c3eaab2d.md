# Função FEOF( )

Determina se o ponteiro de arquivo está posicionado no final de um arquivo.

```foxpro
FEOF(nFileHandle)
```

#### Parâmetros
 **nFileHandle**
Especifica o número de identificação do arquivo a ser verificado para a condição de fim de arquivo. FEOF( ) sempre retorna true (.T.) se você especificar um número de identificação de arquivo de uma porta de comunicação aberta com FOPEN( ).

# Valor de retorno

Logical

# Observações

Esta função de arquivo de baixo nível retorna true (.T.) se o ponteiro de arquivo está posicionado no final de um arquivo aberto com uma função de arquivo de baixo nível. FEOF( ) retorna false (.F.) se o ponteiro de arquivo não está no final do arquivo.

# Exemplo

```foxpro
*** Open the file test.txt ***
gnFileHandle = FOPEN('test.txt')
*** Move the file pointer to BOF ***
gnPosition = FSEEK(gnFileHandle, 0)
*** If file pointer is at BOF and EOF, the file is empty ***
*** Otherwise the file must have something in it ***
IF FEOF(gnFileHandle)
   WAIT WINDOW 'This file is empty!' NOWAIT
ELSE
   WAIT WINDOW 'This file has something in it!' NOWAIT
ENDIF
= FCLOSE(gnFileHandle)
```

# Função FCHSIZE( )

Altera o tamanho de um arquivo aberto com uma função de arquivo de baixo nível.

```foxpro
FCHSIZE(nFileHandle, nNewFileSize)
```

#### Parâmetros
 **nFileHandle**
Especifica o identificador de arquivo cujo tamanho você deseja alterar. O identificador de arquivo é retornado por FOPEN( ) quando você abre o arquivo ou por FCREATE( ) quando você cria o arquivo. Se um arquivo é aberto com FOPEN( ), ele deve ser aberto com privilégios de gravação ou leitura/gravação para que seu tamanho possa ser alterado.
**nNewFileSize**
Especifica o novo tamanho do arquivo em bytes. Se nNewFileSize for menor que o tamanho original do arquivo, o arquivo é truncado. Se nNewFileSize for maior que o tamanho original do arquivo, o tamanho do arquivo é aumentado.

# Valor de retorno

Numérico

# Observações

Use FCHSIZE( ) para aumentar o tamanho do arquivo ou truncar o arquivo após um byte especificado.

Quando o tamanho de um arquivo é aumentado, o Microsoft Visual FoxPro aloca setores para o arquivo na unidade onde o arquivo está aberto. Como FCHSIZE( ) não inicializa o novo espaço do arquivo, o espaço pode conter dados anteriores. Certifique-se de gerenciar o novo espaço do arquivo.

O tamanho final do arquivo em bytes é retornado. O Visual FoxPro retorna –1 se FCHSIZE( ) não conseguir alterar o tamanho do arquivo, por exemplo, se um identificador de arquivo inválido for especificado por falta de espaço em disco ou se o arquivo for somente leitura.

> **Dica:** Esta função pode ser usada para truncar um arquivo para o comprimento 0.

# Função FULLPATH( )

Retorna o caminho para um arquivo especificado ou o caminho relativo a outro arquivo.

```foxpro
FULLPATH(cFileName1 [, nMSDOSPath | cFileName2])
```

#### Parâmetros
 **cFileName1**
Especifica o arquivo para o qual o Visual FoxPro pesquisa. Observação Certifique-se de incluir a extensão do nome do arquivo. Se o arquivo está localizado no caminho do Visual FoxPro, o caminho é retornado com o nome do arquivo. Você pode especificar o caminho do Visual FoxPro usando o comando SET PATH. Se o arquivo não pode ser localizado no caminho do Visual FoxPro, FULLPATH( ) retorna o diretório atual, o caminho e o nome do arquivo como se o arquivo estivesse localizado no diretório padrão atual.
**nMSDOSPath**
Especifica pesquisar o caminho MS-DOS em vez do caminho do Visual FoxPro. nMSDOSPath pode ter qualquer valor numérico. Se o arquivo não pode ser localizado no caminho MS-DOS, FULLPATH( ) retorna o caminho e o nome do arquivo como se o arquivo estivesse localizado no diretório padrão atual.
**cFileName2**
Especifica um segundo nome de arquivo para pesquisar. Observação Certifique-se de incluir a extensão do nome do arquivo. FULLPATH( ) retorna o caminho para o primeiro arquivo relativo ao segundo arquivo.

# Valor de retorno

Character. FULLPATH( ) retorna um caminho de arquivo.

# Observações

Use a função FILE( ) para verificar se o arquivo realmente existe; caso contrário, se o arquivo não existir, a função retorna o nome do arquivo com o diretório atual.

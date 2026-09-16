# Função DisplayPath( )

Trunca expressões de caminho longas para um comprimento especificado para exibição.

```foxpro
DisplayPath(cFilename, nMaxLength)
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo no final do caminho de destino. Se você especificar uma cadeia de caracteres contendo apenas espaços como cFileName, o Visual FoxPro retorna o diretório atual. Se você especificar uma cadeia de caracteres vazia como cFileName, DISPLAYPATH( ) retorna uma cadeia de caracteres vazia. Você pode obter o caminho do diretório atual usando CURDIR( ). Observação Esta função não verifica a validade de cFileName e relatará a expressão de caminho truncada mesmo se o arquivo não existir.
**nMaxLength**
Especifica o comprimento máximo do resultado truncado. nMaxLength deve ser maior ou igual a 10 e menor ou igual a 260

# Retorna

Tipo de dados caractere. DisplayPath( ) retorna uma cadeia de caracteres e exibe o caminho em letras minúsculas.

# Observações

DisplayPath( ) retorna uma cadeia de caracteres adequada apenas para fins de exibição, portanto você não pode usar o resultado para referenciar um arquivo. O comprimento da cadeia de caracteres resultante é igual ou menor que nMaxLength. No entanto, o resultado não divide nomes de diretório. Se a inclusão de um nome de diretório exceder nMaxLength, o resultado é uma reticência (...). Se o nome do arquivo exceder nMaxLength, o resultado é o nome do arquivo mais a extensão.

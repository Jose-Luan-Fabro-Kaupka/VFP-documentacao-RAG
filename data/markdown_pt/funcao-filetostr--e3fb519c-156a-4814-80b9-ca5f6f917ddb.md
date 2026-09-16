# Função FILETOSTR( )

Retorna o conteúdo de um arquivo como uma cadeia de caracteres.

```foxpro
FILETOSTR(cFileName)
```

#### Parâmetros
 **cFileName**
Especifica o nome do arquivo cujo conteúdo é retornado como uma cadeia de caracteres. Se o arquivo estiver em um diretório diferente do diretório padrão atual, inclua um caminho com o nome do arquivo.

# Valor de retorno

Character

# Observações

Observe que o tamanho da cadeia de caracteres que FILETOSTR( ) retorna pode ser muito grande. A quantidade de memória ou espaço em disco disponível determina se você pode armazenar a cadeia de caracteres em uma variável de memória, elemento de matriz ou campo memo. Além disso, campos de caracteres no Visual FoxPro são limitados a 254 caracteres. Consulte Visual FoxPro System Capacities para obter mais informações sobre limitações em dados do tipo caractere.

# Exemplo

O código a seguir carrega REDIST.TXT em uma cadeia de caracteres e então conta o número de módulos de mesclagem mencionados no texto. REDIST.TXT é fornecido com o Microsoft Visual FoxPro e lista quais arquivos do Visual FoxPro podem ser redistribuídos com seus aplicativos.

```foxpro
CD HOME()
cRedist=FILETOSTR("REDIST.TXT")
?OCCURS(".MSM",cRedist)
```

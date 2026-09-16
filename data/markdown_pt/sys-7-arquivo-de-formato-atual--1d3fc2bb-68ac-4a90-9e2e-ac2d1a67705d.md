# SYS(7) - Arquivo de formato atual

Retorna o nome do arquivo de formato atual.

```foxpro
SYS(7 [, nWorkArea])
```

#### Parâmetros
 **nWorkArea**
Especifica o número da área de trabalho cujo nome de arquivo de formato SYS(7) retorna. Se omitido, usa a área atual.

# Valor de retorno

Character

# Observações

Um arquivo de formato é aberto com SET FORMAT. A cadeia de caracteres vazia é retornada se não houver um arquivo aberto na área especificada.

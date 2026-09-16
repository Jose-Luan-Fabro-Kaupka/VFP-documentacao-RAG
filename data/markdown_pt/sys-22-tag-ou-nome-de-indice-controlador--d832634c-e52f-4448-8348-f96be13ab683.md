# SYS(22) - Tag ou nome de índice controlador

Retorna o nome da tag de índice composto .cdx controladora mestra ou do arquivo de índice .idx de uma tabela.

```foxpro
SYS(22 [, nWorkArea])
```

# Valor de retorno

Character

# Observações

Você pode usar SET INDEX, SET ORDER e USE para especificar qual arquivo de índice .idx ou tag de índice composto .cdx é o arquivo de índice ou tag controladora mestra. Para obter mais informações sobre como especificar um índice ou tag controlador mestre, consulte Comando SET INDEX, Comando SET ORDER e Comando USE.

A cadeia de caracteres vazia é retornada se não houver uma tag de índice composto .cdx controladora mestra ou arquivo de índice .idx (por exemplo, SET ORDER TO é emitido para exibir e acessar a tabela na ordem natural dos registros).
 **nWorkArea**
Especifica o número da área de trabalho da tabela para a qual SYS(22) retorna o nome da tag de índice composto .cdx controladora mestra ou do arquivo de índice .idx.

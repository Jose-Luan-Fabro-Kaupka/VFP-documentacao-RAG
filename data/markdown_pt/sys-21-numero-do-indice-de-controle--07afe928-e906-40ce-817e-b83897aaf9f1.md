# SYS(21) - Número do índice de controle

Retorna, como uma cadeia de caracteres, o número da posição de índice da marca de índice composto .cdx ou do arquivo de índice .idx mestre de controle da área de trabalho selecionada no momento.

```foxpro
SYS(21)
```

# Valor de retorno

Caractere

# Observações

O número da posição de índice é determinado pela ordem em que os arquivos de índice .idx e as marcas de índice composto .cdx são especificados em USE e SET INDEX.

Você pode usar SET INDEX, SET ORDER e USE para especificar qual arquivo de índice .idx ou marca de índice composto .cdx é o arquivo ou a marca de índice mestre de controle. Para obter mais informações sobre como especificar um índice ou uma marca mestre de controle, consulte Comando SET INDEX, Comando SET ORDER e Comando USE.

"0" é retornado se não houver uma marca de índice composto .cdx ou um arquivo de índice .idx mestre de controle (por exemplo, SET ORDER TO é emitido para exibir e acessar a tabela na ordem natural dos registros).

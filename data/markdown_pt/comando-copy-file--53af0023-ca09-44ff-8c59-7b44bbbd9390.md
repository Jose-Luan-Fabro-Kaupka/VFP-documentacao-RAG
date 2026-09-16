# Comando COPY FILE

Duplica qualquer tipo de arquivo.

```foxpro
COPY FILE FileName1 TO FileName2
```

# Observações

COPY FILE cria uma duplicata do arquivo cujo nome é especificado em FileName1. Você pode usar COPY FILE para copiar qualquer tipo de arquivo. O arquivo a ser copiado não pode estar aberto. Você deve incluir as extensões tanto para o nome do arquivo de origem FileName1 quanto para o nome do arquivo de destino FileName2.

FileName1 e FileName2 podem conter caracteres curinga como * e ?. Por exemplo, para criar cópias de backup de todos os arquivos de programa com a extensão .prg no diretório atual, emita COPY FILE *.PRG TO *.BAK.

Se você usar COPY FILE para criar um backup de uma tabela que tem um campo memo, um índice estrutural ou ambos, certifique-se de copiar os arquivos .fpt e .cdx também.

# Comando COPY INDEXES

Cria tags de índice composto a partir de arquivos de índice de entrada única .idx.

```foxpro
COPY INDEXES IndexFileList | ALL   [TO CDXFileName]
```

#### Parâmetros
 **IndexFileList**
Especifica os arquivos de índice de entrada única .idx cujas expressões de índice são usadas para criar as tags. Separe os nomes dos arquivos de índice com vírgulas. O nome atribuído a cada tag é o nome raiz do arquivo de índice de entrada única correspondente. Se você criar uma tag a partir de um arquivo de índice que tenha o mesmo nome de uma tag existente, uma caixa de diálogo é exibida (se SAFETY estiver ON) perguntando se você deseja substituir a tag.
**ALL**
Especifica a criação de tags de índice a partir de todos os arquivos de índice de entrada única abertos.
**TO CDXFileName**
Cria tags em um arquivo de índice composto não estrutural. Especifique o nome do arquivo de índice composto não estrutural com CDXFileName . Se um arquivo de índice composto não estrutural com o nome especificado não existir, o Visual FoxPro cria um automaticamente.

# Observações

Um arquivo de índice composto é um arquivo de índice que contém entradas de índice separadas chamadas tags. Cada tag é identificada pelo seu nome de tag exclusivo. A extensão padrão para um arquivo de índice composto é .cdx.

Você deve abrir a tabela e os arquivos de índice de entrada única antes de usar COPY INDEXES. As expressões de índice dos arquivos de índice de entrada única são usadas para criar as novas tags.

Se você omitir a cláusula TO, as novas tags são adicionadas ao arquivo de índice composto estrutural que é aberto automaticamente com a tabela. Se não existir um arquivo de índice composto estrutural para a tabela, COPY INDEXES cria um.

Use COPY TAG para criar um arquivo de índice de entrada única a partir de tags de arquivo de índice composto.

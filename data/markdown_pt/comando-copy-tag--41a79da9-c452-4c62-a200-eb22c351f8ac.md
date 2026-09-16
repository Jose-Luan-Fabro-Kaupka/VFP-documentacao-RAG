# Comando COPY TAG

Cria um arquivo de índice de entrada única (.idx) a partir de uma tag em um arquivo de índice composto.

```foxpro
COPY TAG TagName [OF CDXFileName]   TO IndexFileName
```

#### Parâmetros
 **TagName**
Especifica a tag usada para criar o arquivo .idx de entrada única.
**OF CDXFileName**
Especifica o arquivo de índice composto que contém a tag. Inclua esta cláusula se houver tags com os mesmos nomes nos arquivos de índice composto abertos. Se você omitir OF CDXFileName, o Visual FoxPro procura a tag primeiro no arquivo de índice estrutural. Se não for encontrada lá, o Visual FoxPro pesquisa em todos os arquivos de índice composto não estruturais abertos.
**TO IndexFileName**
Especifica o nome do arquivo .idx de entrada única a ser criado.

# Observações

Use COPY TAG para criar um novo arquivo .idx de entrada única a partir de uma tag em um arquivo de índice composto .cdx.

O arquivo de índice composto do qual você cria o arquivo .idx de entrada única deve estar aberto. Arquivos de índice composto estruturais são abertos automaticamente quando você abre uma tabela. Índices compostos não estruturais devem ser abertos explicitamente com USE ... INDEX ou SET INDEX. Para obter mais informações sobre arquivos de índice composto, consulte INDEX Command.

Use COPY INDEX para criar tags em arquivos de índice composto a partir de arquivos .idx de entrada única.

# Comando SET VOLUME

Incluído para compatibilidade com versões anteriores. Mapeia designadores de unidade do MS-DOS (A:, B:, C: e assim por diante) para volumes ou pastas no FoxPro for Macintosh.

```foxpro
SET VOLUME cMS-DOSDrive TO [cMacintoshPath]
```

# Parâmetros
 **cMS-DOSDrive**
Especifica um designador de unidade do MS-DOS e pode ser qualquer letra de A a Z. O delimitador de unidade, dois pontos, como em A: ou C:, é opcional.
**cMacintoshPath**
Especifica um nome de volume, um nome de volume com um nome de pasta, uma pasta aninhada, notação abreviada do Macintosh (: ou ::) ou notação abreviada do MS-DOS (\ ou ..). Se cMacintoshPath incluir um nome de volume ou pasta que contenha um espaço, cMacintoshPath deve estar entre aspas. Se você incluir um caminho em cMacintoshPath que não seja totalmente qualificado, o caminho será relativo à pasta padrão atual.

# Observações

Mais eficaz no FoxPro for Macintosh.

SET VOLUME ajuda a mover aplicações criadas no FoxPro for MS-DOS e no Visual FoxPro para o FoxPro for Macintosh. Para cada ocorrência de um designador de unidade do MS-DOS especificado, o FoxPro for Macintosh substitui internamente o volume ou pasta do Macintosh que você designar.

Quando você inicia o FoxPro for Macintosh, não há designação padrão de volume ou pasta. No entanto, você pode especificar um volume ou pasta padrão em seu arquivo de configuração do Visual FoxPro com o item de configuração VOLUME.

Use DISPLAY STATUS para exibir o mapeamento atual de volume ou pasta.

# Exemplo

Os comandos a seguir mapeiam cada ocorrência de uma unidade C do MS-DOS para um volume do Macintosh chamado MacHD ou Mac HD:

```foxpro
SET VOLUME C: TO MacHD:
SET VOLUME C: TO 'Mac HD:'
SET VOLUME C TO 'Mac HD:'
```

Você também pode especificar uma pasta com um volume do Macintosh:

```foxpro
SET VOLUME C: TO MacHD:FolderOne
SET VOLUME C TO 'MacHD:Folder One'
```

Você também pode usar a notação abreviada do MS-DOS e do Macintosh. Para mapear cada ocorrência de uma unidade C do MS-DOS para o volume do Macintosh atual, execute o seguinte comando:

```foxpro
SET VOLUME C TO \
```

Para mapear cada ocorrência de uma unidade C do MS-DOS para o volume de inicialização do FoxPro for Macintosh, execute SET VOLUME sem cMacintoshPath:

```foxpro
SET VOLUME C TO
```

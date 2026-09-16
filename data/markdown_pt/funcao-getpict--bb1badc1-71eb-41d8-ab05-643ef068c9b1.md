# Função GETPICT( )

Exibe a caixa de diálogo Open Picture e retorna o nome do arquivo de imagem que você escolheu.

> **Observação:** Você pode visualizar imagens no Windows 2000 e posteriores clicando no ícone View Menu e depois em Thumbnails. O Visual FoxPro usa a exibição Thumbnails como configuração padrão para fornecer mini-visualizações de imagens. Portanto, a caixa de diálogo Open Picture não inclui mais um quadro para exibir uma imagem. A caixa de seleção Preview aparece na caixa de diálogo Open Picture somente ao executar o Visual FoxPro em sistemas operacionais anteriores ao Windows 2000.

```foxpro
GETPICT([cFileExtensions] [, cFileNameCaption] [, cOpenButtonCaption])
```

#### Parâmetros
 **cFileExtensions**
Especifica as extensões de arquivo dos arquivos de imagem exibidos na lista rolável quando o item de menu All Files não é escolhido. cFileExtensions pode ter as seguintes formas: Se cFileExtensions contém uma única extensão (por exemplo, .bmp), apenas arquivos com essa extensão são exibidos. cFileExtensions também pode conter curingas (* e ?). Todos os arquivos com extensões que atendem aos critérios de curinga são exibidos. Por exemplo, se cFileExtensions é ?X?, todos os arquivos com extensão .fxp, .exe e .txt são exibidos. Se cFileExtensions contém uma cadeia de caracteres vazia (""), todos os arquivos gráficos disponíveis (por exemplo, arquivos com extensões .bmp e .dib) são exibidos.
**CFileNameCaption**
Especifica a legenda exibida à esquerda da caixa de texto File Name. cFileNameCaption substitui "File Name" que aparece quando cFileNameCaption é omitido.
**cOpenButtonCaption**
Especifica uma legenda para o botão OK.

# Valor de retorno

Tipo de dados Caractere. Retorna o nome do arquivo de imagem que você escolheu.

# Observações

A função GETPICT( ) retorna a cadeia de caracteres vazia se você sair da caixa de diálogo Open Picture pressionando ESC, escolhendo o botão Cancel ou clicando no botão Close. A caixa de diálogo Open Picture exibida ao digitar GETPICT( ) na janela Command permite localizar rapidamente todos os arquivos gráficos suportados no Visual FoxPro. Em versões anteriores ao Visual FoxPro 8.0, marque a caixa de seleção Preview na caixa de diálogo Picture Open para exibir o arquivo gráfico atualmente selecionado.

A tabela a seguir lista os formatos de arquivo gráfico que o Visual FoxPro suporta.

| Formato gráfico | Extensão de arquivo |
| --- | --- |
| Animated Cursor | .ani |
| Bitmap | .bmp |
| Cursor | .cur |
| Device Independent Bitmap | .dib |
| Exchangeable Image File | .exif |
| Graphics Interchange Format | .gif, .gfa |
| Joint Photographic Electronic Group, JPEG File Interchange Format | .jpg, .jpeg, .jpe, .jfif |
| Icon | .ico |
| Portable Networks Graphics | .png |
| Tag Image File Format | .tif, .tiff |
| Windows Enhanced Metafile | .emf |

> **Observação:** No Visual FoxPro, arquivos de cursor, cursor animado e ícone podem ser usados como arquivos gráficos. Por exemplo, você pode especificar um arquivo de cursor animado para a propriedade Picture do controle Image (no entanto, o controle Image exibe a representação estática do cursor).

Use os comandos CLEAR para limpar todos os arquivos gráficos em cache, incluindo arquivos .gif e .jpg.

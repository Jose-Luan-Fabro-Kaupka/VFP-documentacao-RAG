# Comando SET ORDER

Designa um arquivo de índice controlador ou uma tag para uma tabela.

> **Observação:** O Visual FoxPro não oferece suporte a SET ORDER para índices binários.

```foxpro
SET ORDER TO [nIndexNumber | IDXIndexFileName | [TAG] TagName
   [OF CDXFileName] [IN nWorkArea | cTableAlias]
   [ASCENDING | DESCENDING]]
```

#### Parâmetros
 **nIndexNumber**
Especifica o número do arquivo de índice controlador ou da tag. nIndexNumber refere-se aos arquivos de índice conforme listados em USE ou SET INDEX. Arquivos .idx abertos são numerados primeiro na ordem em que aparecem em USE ou SET INDEX. As tags no arquivo .cdx estrutural (se existir) são numeradas em seguida na ordem em que foram criadas. Por fim, as tags em quaisquer arquivos .cdx independentes abertos são numeradas na ordem em que foram criadas. O exemplo a seguir ilustra como diferentes tipos de arquivos de índice e tags são numerados. (Os nomes de arquivo são apenas para ilustração e podem não existir.) Uma tabela chamada video.dbf é aberta com três índices (title.idx, costs.cdx e rating.idx) na primeira área de trabalho com este comando: USE video INDEX title.idx, costs.cdx, rating.idx IN 1 A tabela video tem um arquivo de índice composto estrutural (video.cdx) com duas tags, NUMBERSOLD e YEARSOLD. O arquivo .cdx estrutural é aberto automaticamente quando video é aberta. Como os arquivos .idx são numerados primeiro, emita SET ORDER TO 1 para tornar title.idx o índice controlador e SET ORDER TO 2 para tornar rating.idx o índice controlador: SET ORDER TO 1 Controlling index: C:\FOX30\TITLE.IDX SET ORDER TO 2 Controlling index: C:\FOX30\RATING.IDX As tags em video.cdx são numeradas em seguida: SET ORDER TO 3 Controlling index: C:\FOX30\VIDEO.CDX Tag: NUMBERSOLD SET ORDER TO 4 Controlling index: C:\FOX30\VIDEO.CDX Tag: YEARSOLD Por fim, as tags no arquivo independente costs.cdx são numeradas: SET ORDER TO 5 Controlling index: C:\FOX30\COSTS.CDX Tag: RENTALCOST SET ORDER TO 6 Controlling index: C:\FOX30\COSTS.CDX Tag: BUYCOST nIndexNumber também pode ser 0. Se você emitir SET ORDER TO 0, todos os arquivos de índice permanecem abertos e são atualizados quando registros são adicionados, excluídos ou modificados. No entanto, os registros na tabela são exibidos e acessados na ordem do número do registro e não em uma ordem indexada. Emitir SET ORDER TO sem argumentos adicionais é idêntico a emitir SET ORDER TO 0. Se nIndexNumber for maior que o número de arquivos .idx e tags de arquivos .cdx, o Visual FoxPro gera uma mensagem de erro.
**IDXIndexFileName**
Especifica um arquivo .idx como o arquivo de índice controlador.
**[TAG] TagName [OF CDXFileName ]**
Especifica uma tag de um arquivo .cdx como a tag controladora. O nome da tag pode ser de um arquivo .cdx estrutural ou de qualquer arquivo .cdx independente aberto. Se existirem nomes de tag idênticos em arquivos .cdx independentes abertos, use OF CDXFileName para especificar o arquivo .cdx que contém a tag. Observação O arquivo .idx tem precedência se existirem nomes duplicados de arquivo .idx e de tag.
**IN nWorkArea | cTableAlias**
Designa um arquivo de índice controlador ou uma tag para uma tabela aberta em uma área de trabalho diferente da área de trabalho atualmente selecionada. nWorkArea especifica o número da área de trabalho e cTableAlias especifica o alias de uma tabela.
**ASCENDING | DESCENDING**
Exibe e permite o acesso aos registros da tabela em ordem ascendente ou descendente. Incluir ASCENDING ou DESCENDING não altera o arquivo de índice ou a tag de nenhuma forma.

# Observações

Uma tabela pode ter muitos arquivos de índice abertos simultaneamente. No entanto, apenas um arquivo de índice simples (.idx) (o arquivo de índice controlador) ou uma tag de um arquivo de índice composto (.cdx) (a tag controladora) determina a ordem em que os registros de uma tabela são exibidos ou acessados. SET ORDER permite designar o arquivo de índice controlador ou a tag controladora. Certos comandos (SEEK, por exemplo) usam o arquivo de índice controlador ou a tag para pesquisar registros.

Você pode abrir arquivos de índice com uma tabela incluindo a cláusula INDEX no comando USE. Se uma tabela tem um arquivo .cdx estrutural associado, esse arquivo é aberto automaticamente com a tabela. Depois que uma tabela foi aberta, você pode abrir e fechar arquivos de índice para a tabela usando SET INDEX.

Por padrão, SET ORDER designa o índice controlador ou a tag controladora para a tabela aberta na área de trabalho atualmente selecionada.

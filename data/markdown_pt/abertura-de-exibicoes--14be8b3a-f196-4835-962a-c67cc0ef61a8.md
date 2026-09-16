# Abertura de exibições

Você pode usar exibições em janelas Browse, sessões de dados e programaticamente, da mesma forma que abre tabelas. Quando uma exibição é usada, ela é aberta como cursor em sua própria área de trabalho. Se for baseada em tabelas locais, o Visual FoxPro também abrirá as tabelas base em áreas de trabalho separadas. As tabelas base de uma exibição são aquelas acessadas pela instrução SQL SELECT especificada no comando CREATE SQL VIEW durante sua criação. No exemplo anterior, usar `product_view` também abre automaticamente a tabela `products`.
 A janela Data Session exibe a exibição e sua tabela base

Quando uma exibição é baseada em tabelas remotas, as tabelas base não são abertas em áreas de trabalho. Somente o nome da exibição remota aparece na janela Data Session.

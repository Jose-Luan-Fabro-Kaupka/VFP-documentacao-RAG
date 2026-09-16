# Rotinas de manipulação de janelas

Essas rotinas de API permitem criar, manipular e liberar janelas, e manipular a janela principal do Visual FoxPro.
 **Rotina de biblioteca de API _Dialog( )**
Apresenta ao usuário uma caixa de diálogo com o número de esquema de cores especificado e que contém o texto do corpo e o texto do botão especificados.
**Rotina de biblioteca de API _FindWindow( )**
Coloca o WHANDLE da janela à qual o ponto pt pertence na tela em wh.
**Rotina de biblioteca de API _FindWindowP( )**
Coloca o identificador da janela à qual o ponto pt pertence na tela em wh.
**Rotina de biblioteca de API _GlobalToLocal( )**
Traduz um ponto em coordenadas relativas à tela para coordenadas relativas à janela.
**Rotina de biblioteca de API _GlobalToLocalP( )**
Traduz um ponto em coordenadas relativas à tela para coordenadas relativas à janela em pixels.
**Rotina de biblioteca de API _PutChr( )**
Grava um caractere char na janela de saída atual em seu atributo normal (cor 0).
**Rotina de biblioteca de API _PutStr( )**
Grava uma cadeia de caracteres terminada em nulo na janela de saída atual em seu atributo normal (cor 0).
**Rotina de biblioteca de API _PutValue( )**
Formata o valor val e o grava na janela de saída atual.
**Rotina de biblioteca de API _WAttr( )**
Retorna o byte de atributo para o índice de cor no esquema da janela especificada.
**Rotina de biblioteca de API _WBottom( )**
Retorna a linha na tela onde a parte inferior da janela está localizada.
**Rotina de biblioteca de API _WBottomP( )**
Retorna a posição na tela em pixels onde a parte inferior da janela especificada está localizada.
**Rotina de biblioteca de API _WClear( )**
Apaga o conteúdo da janela especificada alterando a área de conteúdo para a cor de fundo padrão.
**Rotina de biblioteca de API _WClearRect( )**
Apaga uma área retangular de uma janela alterando-a para a cor de fundo padrão.
**Rotina de biblioteca de API _WClearRectP( )**
Apaga a porção retangular especificada de uma janela alterando-a para a cor de fundo padrão.
**Rotina de biblioteca de API _WClose( )**
Fecha uma janela e libera toda a memória associada a essa janela.
**Rotina de biblioteca de API _WFindTitle( )**
Passa o título de uma janela e retorna o WHANDLE.
**Rotina de biblioteca de API _WGetCursor( )**
Retorna a posição do cursor lógico na janela especificada.
**Rotina de biblioteca de API _WGetCursorP( )**
Retorna em pixels a posição de saída atual na janela especificada.
**Rotina de biblioteca de API _WGetPort( )**
Retorna o WHANDLE da janela que está atualmente selecionada para saída do usuário.
**Rotina de biblioteca de API _WHeight( )**
Retorna o número de linhas na área de conteúdo de uma janela.
**Rotina de biblioteca de API _WHeightP( )**
Retorna a altura em pixels da área de conteúdo da janela especificada.
**Rotina de biblioteca de API _WHide( )**
Remove uma janela da tela, mas mantém o controle de seu conteúdo para que ela possa ser exibida novamente, se desejado.
**Rotina de biblioteca de API _WLeft( )**
Retorna a coluna na tela onde a borda esquerda da janela está localizada.
**Rotina de biblioteca de API _WLeftP( )**
Retorna a posição na tela em pixels onde a borda esquerda da janela está localizada.
**Rotina de biblioteca de API _WMainWindow( )**
Retorna o WHANDLE da janela principal do Visual FoxPro.
**Rotina de biblioteca de API _WMove( )**
Move a janela especificada para um novo local especificado por pt.
**Rotina de biblioteca de API _WMoveP( )**
Move a janela especificada para um novo local especificado por pt.
**Rotina de biblioteca de API _WhToHwnd( )**
Passa o WHANDLE e retorna o HWND do Windows.
**Rotina de biblioteca de API _WOnTop( )**
Retorna o WHANDLE da janela mais à frente.
**Rotina de biblioteca de API _WOpen( )**
Cria uma nova janela nas coordenadas especificadas por top, left, bottom e right.
**Rotina de biblioteca de API _WOpenP( )**
Cria uma nova janela nas coordenadas especificadas por top, left, bottom e right.
**Rotina de biblioteca de API _WPosCursor( )**
Posiciona o cursor lógico da janela especificada no local especificado por pt.
**Rotina de biblioteca de API _WPosCursorP( )**
Posiciona o cursor lógico da janela especificada no local especificado em pixels por pt.
**Rotina de biblioteca de API _WPutChr( )**
Grava um caractere char na janela especificada na cor atual.
**Rotina de biblioteca de API _WPutStr( )**
Grava uma cadeia de caracteres terminada em nulo na janela especificada na cor atual.
**Rotina de biblioteca de API _WRight( )**
Retorna a coluna na tela onde a borda direita da janela está localizada.
**Rotina de biblioteca de API _WRightP( )**
Retorna a posição na tela em pixels onde a borda direita da janela está localizada.
**Rotina de biblioteca de API _WScroll( )**
Rola uma porção do conteúdo de uma janela para a esquerda ou para a direita e para cima ou para baixo.
**Rotina de biblioteca de API _WScrollP( )**
Rola uma porção do conteúdo de uma janela para a esquerda ou para a direita e para cima ou para baixo.
**Rotina de biblioteca de API _WSetAttr( )**
Altera o atributo para o índice de esquema de cores especificado no esquema de cores da janela indicada para o novo atributo attr.
**Rotina de biblioteca de API _WSelect( )**
Traz a janela especificada para a posição mais à frente na tela.
**Rotina de biblioteca de API _WSendBehind( )**
Envia a janela especificada para a posição mais atrás na tela.
**Rotina de biblioteca de API _WSetPort( )**
Altera a janela de saída do usuário para ser a janela especificada.
**Rotina de biblioteca de API _WSetTitle( )**
Altera o título de uma janela.
**Rotina de biblioteca de API _WShow( )**
Redisplaya uma janela oculta na tela.
**Rotina de biblioteca de API _WSize( )**
Define as novas dimensões da janela para a altura e a largura especificadas por h e v em pt.
**Rotina de biblioteca de API _WSizeP( )**
Define as novas dimensões da janela para a altura e a largura especificadas por h e v em pt.
**Rotina de biblioteca de API _WTitle( )**
Coloca o título terminado em nulo da janela wh em title.
**Rotina de biblioteca de API _WTop( )**
Retorna a linha na tela onde a parte superior da janela está localizada.
**Rotina de biblioteca de API _WTopP( )**
Retorna a posição na tela em pixels onde a parte superior da janela está localizada.
**Rotina de biblioteca de API _WWidth( )**
Retorna o número de colunas na área de conteúdo de uma janela.
**Rotina de biblioteca de API _WWidthP( )**
Retorna a largura em pixels da área de conteúdo da janela especificada.
**Rotina de biblioteca de API _WZoom( )**
Amplia uma janela para um novo estado.

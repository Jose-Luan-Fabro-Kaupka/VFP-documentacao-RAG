# Rotinas de menu

Estas rotinas de API permitem criar, manipular e liberar menus.
 **_ActivateMenu( ) API Library Routine**
Exibe o menu especificado na tela e retorna o controle imediatamente à rotina chamadora.
**_CountItems( ) API Library Routine**
Retorna o número de títulos ou barras de menu no menu especificado.
**_DeActivateMenu( ) API Library Routine**
Remove um menu da tela.
**_DisposeItem( ) API Library Routine**
Libera o item de menu especificado e libera todo o armazenamento associado a este item.
**_DisposeMenu( ) API Library Routine**
Libera o menu especificado e todos os seus itens e libera todo o armazenamento associado a este menu.
**_GetItemCmdKey( ) API Library Routine**
Copia a cadeia de atalho de teclado exibida para o item de menu especificado no buffer apontado pelo parâmetro text.
**_GetItemId( ) API Library Routine**
Retorna o identificador do item do item de índice no menu especificado.
**_GetItemSubMenu( ) API Library Routine**
Retorna o identificador do item de menu ou um submenu atribuído a um item de menu.
**_GetItemText( ) API Library Routine**
Copia o texto de uma barra de menu ou título de menu para o buffer apontado por text .
**_GetNewItemId( ) API Library Routine**
Retorna um identificador atualmente disponível para uso como identificador de item no menu especificado.
**_GetNewMenuId( ) API Library Routine**
Retorna um identificador disponível para uso como identificador de menu.
**_MenuId( ) API Library Routine**
Retorna o identificador de menu real que corresponde ao literal definido pelo sistema para o título ou menu do menu do sistema.
**_MenuInteract( ) API Library Routine**
Define itemid e menuid para indicar qual item de menu foi selecionado, se houver.
**_NewItem( ) API Library Routine**
Adiciona um item com o itemid especificado ao menu especificado por menuid .
**_NewMenu( ) API Library Routine**
Cria um novo menu do tipo de menu especificado.
**_OnSelection( ) API Library Routine**
Especifica uma rotina a ser executada quando o menu e o item especificados são selecionados.
**_SetItemCmdKey( ) API Library Routine**
Define o atalho de teclado para o item de menu especificado, bem como o texto exibido para o atalho de teclado.
**_SetItemSubMenu( ) API Library Routine**
Atribui um submenu a um item de menu. Isso pode ser usado para anexar um menu a um título ou um submenu a um item de menu.
**_SetItemText( ) API Library Routine**
Altera o texto exibido para um item de menu. O item pode ser um pad ou uma bar.
**_SetMenuPoint( ) API Library Routine**
Especifica o canto superior esquerdo, loc , de um menu.
**_SetMenuPointP( ) API Library Routine**
Especifica em pixels a posição na tela do canto superior esquerdo, loc , de um menu.

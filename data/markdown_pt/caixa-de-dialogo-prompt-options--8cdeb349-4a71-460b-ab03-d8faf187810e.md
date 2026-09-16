# Caixa de diálogo Prompt Options

Torna possível especificar opções para prompts em um sistema de menu personalizado. Use esta caixa de diálogo para definir atalhos de teclado, determinar quando o menu ou item de menu é desabilitado, incluir uma mensagem na barra de status quando o menu ou item de menu é selecionado, especificar um nome para um título de menu e controlar a localização do título do menu durante a edição visual OLE.

Esta caixa de diálogo aparece quando você escolhe o botão Options nos Menu and Shortcut Designers.
 **Commen t**
Fornece espaço para adicionar um comentário para uso pessoal apenas. Os comentários não afetam o código gerado de nenhuma forma; o Microsoft Visual FoxPro os ignora ao executar o programa de menu.
**Shortcut**
Define a tecla de atalho opcional para um menu ou item de menu. Os atalhos de teclado para itens de menu do Visual FoxPro são uma combinação da tecla CTRL e outra tecla.
**KeyLabel**
Exibe sua combinação de teclas. Se um item de menu não tiver um atalho de teclado, o Visual FoxPro exibe "(press the key)" na caixa KeyLabel. Pressione a combinação de teclas desejada para sua tecla de atalho.
**KeyText**
Exibe o texto que você deseja que apareça ao lado do item de menu. A menos que você altere, esta caixa repete o atalho de teclado da caixa KeyLabel. Por exemplo, se KeyLabel e KeyText fossem CTRL+R, você poderia alterar KeyText para ^R. Observação Você não pode atribuir CTRL+J como atalho de teclado para um item de menu.
**SkipFor**
Exibe a Expression Builder Dialog Box. Na caixa SkipFor do ExpressionBuilder, digite a expressão que determina se o menu ou item de menu está desabilitado ou habilitado. O menu ou item de menu é desabilitado se a expressão for true (.T.).
**Negotiate**
Especifica a localização dos títulos de menu quando o usuário edita um objeto OLE em sua aplicação.
**Container**
Especifica como o título do menu será mesclado quando o Visual FoxPro for o contêiner de um objeto ativo in-place. Observação As opções de negociação de menu estão disponíveis apenas para objetos OLE que podem ser editados in-place. A tabela a seguir lista o posicionamento do título do menu para cada configuração de negociação. Configuração Posicionamento None Especifica que o título do menu não seja colocado na barra de menu. Isso é o mesmo que não escolher nenhuma opção. Left Especifica que o título do menu seja colocado no grupo esquerdo de títulos de menu na barra de menu. Middle Especifica que o título do menu seja colocado no grupo central de títulos de menu na barra de menu. Right Especifica que o título do menu seja colocado no grupo direito de títulos de menu na barra de menu. Para obter mais informações sobre negociação de menu de objeto, consulte DEFINE PAD Command.
**Message**
Exibe a caixa de diálogo ExpressionBuilder. Na caixa Message do ExpressionBuilder, digite a mensagem que aparecerá na barra de status do Visual FoxPro que descreve a escolha do menu.
**Pad Name**
Torna possível especificar um título de menu opcional. O nome ou número usado no programa de menu gerado é opcional, e o Visual FoxPro fornece um se você não fornecer. Usando este nome ou número, você pode referenciar um menu ou item de menu em tempo de execução. Esta opção está disponível apenas para menus. Observação Esta opção está disponível apenas se a área Result na janela Menu Designer mostrar Command, Submenu ou Procedure.
**Picture**
Torna possível especificar um arquivo gráfico a ser exibido à esquerda do texto da barra de menu ou ao lado do recurso no menu do sistema Visual FoxPro.
**Bar #**
Torna possível especificar um título de menu de atalho opcional. Esta opção está disponível apenas para menus de atalho.

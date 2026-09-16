# Janela Command (Visual FoxPro)

A janela Command é uma janela de sistema do Visual FoxPro. Quando você escolhe comandos de menu, os comandos da linguagem Visual FoxPro são ecoados na janela Command.

Você também pode digitar comandos Visual FoxPro diretamente na janela Command. Na janela Command, você pode:
 - Excluir texto pressionando ESC se você ainda não pressionou ENTER para executar o comando.
- Reemitir um comando anterior colocando o cursor em qualquer lugar na linha de comando e pressionando ENTER.
- Reemitir um bloco de código selecionando-o e pressionando ENTER.
- Dividir comandos longos digitando um ponto e vírgula após um espaço no comando onde deseja a quebra e pressionando ENTER.
- Mover texto dentro da janela Command e para outras janelas de edição. Selecione o texto desejado e arraste-o para o local desejado.
- Copiar texto dentro da janela Command e colá-lo em outras janelas de edição sem usar comandos do menu Edit. Selecione o texto desejado, mantenha CTRL pressionado e arraste o texto para o local desejado.

Você pode alterar fonte, espaçamento entre linhas e recuo selecionando o comando apropriado no menu Format.

Clique com o botão direito na janela Command para exibir um menu de atalho com estas opções:
 - Cut, Copy, Paste . Mover ou excluir caracteres de e para a janela Command.
- Build Expression . Exibir a janela da caixa de diálogo Expression Builder, na qual você pode definir uma expressão usando comandos, literais, campos ou outras expressões. A expressão que você criar é colada na janela Command quando você clica em OK.
- Execute Selection . Executar o texto selecionado na janela Command como um novo comando.
- Clear . Remover a lista de comandos executados anteriormente da janela Command.
- Properties . Exibir a janela da caixa de diálogo Edit Properties, na qual você pode alterar o comportamento de edição, largura de tabulação, fontes e opções de coloração de sintaxe para a janela Command.

# Persistência do conteúdo

O conteúdo da janela Command é salvo automaticamente em um arquivo, _command.prg, a menos que a política de sistema noRecentDocHistory esteja habilitada ou você não esteja usando um arquivo de recursos FoxUser. Você pode limpar a janela selecionando Clear no menu de atalho da janela Command. Para permitir seu uso por várias instâncias do Visual FoxPro, o arquivo é lido somente ao iniciar o Visual FoxPro e gravado ao sair do Visual FoxPro. O arquivo está localizado no mesmo diretório do arquivo de recursos FoxUser. Você pode determinar ou alterar o local do arquivo de recursos na guia File Locations da caixa de diálogo Options ou via linguagem usando SET("RESOURCE") ou SET RESOURCE respectivamente.

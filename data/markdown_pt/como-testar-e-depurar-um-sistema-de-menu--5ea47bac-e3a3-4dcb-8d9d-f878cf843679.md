# Como: testar e depurar um sistema de menu

Você pode visualizar um sistema de menu enquanto o projeta ou pode testá-lo e depurá-lo após gerar o programa de menu.

### Para visualizar um sistema de menu enquanto o projeta
- Nos Menu and Shortcut Designers , escolha Preview .

Quando você escolhe Preview, o sistema de menu que você definiu aparece na parte superior da tela. Além disso, a caixa de diálogo Preview exibe o nome do arquivo (ou um nome de arquivo temporário) do sistema de menu.

Se você selecionar um título de menu ou item de menu, ele também aparece na caixa de diálogo Preview, junto com o comando atribuído a ele, se houver um.

### Para testar um sistema de menu
- No menu Menu, escolha Generate . Se você alterou o menu, o Visual FoxPro solicita que salve as alterações.
- Na caixa de diálogo Generate Menu, insira um nome para o programa de menu gerado digitando o nome na caixa Output File ou escolhendo o botão de diálogo.
- Escolha Generate para produzir um arquivo de programa de menu com extensão .mpr.
- No menu Program, escolha Do para executar o programa. Cuidado Se você modificar o programa de menu gerado (o arquivo .mpr), perderá as alterações quando modificar o menu usando os Menu and Shortcut Designers e regenerar o programa de menu.

Se o programa de menu não funcionar como esperado, use as ferramentas de diagnóstico fornecidas com o Visual FoxPro. Para obter mais informações, consulte Testing and Debugging Applications.

> **Dica:** Se você executar um aplicativo (arquivo .exe) em que o programa principal é um menu e o aplicativo termina assim que o menu é exibido, inclua o READ EVENTS Command no código de limpeza. Você também deve atribuir um comando CLEAR EVENTS ao comando de menu que permite ao usuário sair do sistema de menu.

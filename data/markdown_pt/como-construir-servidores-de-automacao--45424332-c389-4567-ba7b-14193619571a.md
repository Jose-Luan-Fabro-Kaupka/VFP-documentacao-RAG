# Como: construir servidores de automação

Você pode construir um servidor de automação como um arquivo executável (.exe) ou como um arquivo de biblioteca vinculada dinamicamente (.dll).

> **Observação:** Servidores de automação são invocados por meio de instanciação de classe; portanto, você pode construir um servidor de automação sem primeiro especificar um arquivo principal no Project Manager.

Para obter informações sobre como construir aplicações, consulte Como: construir aplicações.

### Para construir um servidor de automação (.dll)
- Abra o projeto de sua aplicação.
- No Project Manager , clique em Build .
- Na caixa de diálogo Build Options, clique em Single-threaded COM server (dll) ou Multi-threaded COM server (dll) .
- Selecione quaisquer outras opções desejadas e clique em OK . Dica Você pode visualizar e salvar mensagens de build que ocorrem durante o processo de build. Para obter mais informações, consulte Como: visualizar e salvar mensagens de build .
- Na caixa de diálogo Save As, especifique um nome para o arquivo e salve o arquivo.

Para obter mais informações, consulte Project Manager Window e Build Options Dialog Box.

### Para construir um servidor de automação programaticamente
- Use o comando BUILD EXE , BUILD DLL ou BUILD MTDLL .

Para obter mais informações, consulte BUILD EXE Command, BUILD DLL Command e BUILD MTDLL Command.

> **Observação:** Você deve incluir certas bibliotecas de vínculo dinâmico (.dll) ao distribuir seu servidor de automação. Para obter mais informações, consulte Automation Servers in Visual FoxPro .

Depois de construir o servidor de automação, as classes do servidor são listadas na caixa de diálogo Project Information. Você também pode especificar um arquivo de ajuda e um ID de contexto de ajuda para cada classe. Este arquivo de ajuda pode ser aberto na maioria dos navegadores de objetos genéricos. Você pode escolher valores de instanciação específicos da classe na caixa de diálogo Project Information. Para obter mais informações, consulte Servers Tab, Project Information Dialog Box.

> **Dica:** Para que as configurações alteradas na guia Servers tenham efeito, reconstrua o .dll ou .exe.

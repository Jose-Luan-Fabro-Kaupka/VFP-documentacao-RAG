# Como: compilar aplicativos

Quando você testou seu projeto de aplicativo para erros e ele inclui todos os arquivos necessários, você pode compilar um arquivo distribuível a partir do projeto seguindo as etapas em uma destas seções:
 - Compilando um aplicativo padrão do Visual FoxPro Descreve como compilar um arquivo de aplicativo padrão (.app) que é executado somente com o Visual FoxPro instalado.
- Compilando um arquivo executável do Visual FoxPro Descreve como compilar um arquivo executável (.exe) que é executado sem o Visual FoxPro.

Para obter informações sobre como compilar servidores Automation ou arquivos de biblioteca de vínculo dinâmico do Windows (.dll), consulte Como: compilar servidores Automation.

Para obter informações sobre como testar projetos de aplicativo, consulte Como: testar um projeto.

# Compilando um aplicativo padrão do Visual FoxPro

Você pode compilar um arquivo de aplicativo padrão do Visual FoxPro (.app) usando o Project Manager ou o comando BUILD APP. No entanto, mais opções de compilação estão disponíveis quando você usa o Project Manager. Para obter informações sobre como usar o comando BUILD APP, consulte Comando BUILD APP.

> **Observação:** Para compilar um arquivo .app, seu projeto deve ter um programa definido como programa principal. Para obter mais informações, consulte Como: definir o ponto de partida.

### Para compilar um arquivo de aplicativo padrão (.app)
- Abra o projeto do seu aplicativo.
- No Project Manager, escolha Build.
- Na caixa de diálogo Build Options, escolha Application (app).
- Selecione quaisquer outras opções desejadas e clique em OK. Dica Você pode visualizar e salvar mensagens de compilação que ocorrem durante o processo de compilação. Para obter mais informações, consulte Como: visualizar e salvar mensagens de compilação.
- Na caixa de diálogo Save As, especifique um nome para o arquivo e salve o arquivo.

Para obter mais informações, consulte Janela Project Manager e Caixa de diálogo Build Options.

# Compilando um arquivo executável do Visual FoxPro

Você pode compilar um arquivo executável do Visual FoxPro (.exe) usando o Project Manager ou o comando BUILD EXE. No entanto, mais opções de compilação estão disponíveis quando você usa o Project Manager. Para obter informações sobre como usar o comando BUILD EXE, consulte Comando BUILD EXE.

> **Observação:** Para compilar um arquivo .exe, seu projeto deve ter um programa definido como programa principal. Para obter mais informações, consulte Como: definir o ponto de partida.

### Para compilar um arquivo executável (.exe)
- Abra o projeto do seu aplicativo.
- No Project Manager, escolha Build.
- Na caixa de diálogo Build Options, escolha Win32 executable/COM server (exe).
- Selecione quaisquer outras opções desejadas e clique em OK. Dica Você pode visualizar e salvar mensagens de compilação que ocorrem durante o processo de compilação. Para obter mais informações, consulte Como: visualizar e salvar mensagens de compilação.
- Na caixa de diálogo Save As, especifique um nome para o arquivo e salve o arquivo.

Para obter mais informações, consulte Janela Project Manager e Caixa de diálogo Build Options.

> **Observação:** O arquivo .exe opera com certas bibliotecas de vínculo dinâmico (.dll) que fornecem um ambiente de tempo de execução completo do Visual FoxPro e que você precisa incluir ao distribuir seu aplicativo. Para obter mais informações, consulte Preparação para distribuição de aplicativos.

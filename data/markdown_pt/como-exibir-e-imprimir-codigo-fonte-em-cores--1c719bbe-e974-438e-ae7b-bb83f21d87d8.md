# Como: exibir e imprimir código-fonte em cores

Você pode exibir e imprimir código com sintaxe colorida na janela Command e nos editores do Visual FoxPro para arquivos de programa (.prg), métodos, procedimentos armazenados e memorandos.

As seções a seguir contêm mais informações:
 - Exibição de código-fonte em cores
- Impressão de código-fonte em cores

# Exibição de código-fonte em cores

Você pode ativar a coloração de sintaxe separadamente para cada janela de edição; contudo, as configurações escolhidas na guia Editor da caixa de diálogo Options se aplicam à janela Command e à maioria das outras janelas de edição. Para obter mais informações, consulte Guia Editor, caixa de diálogo Options e Janela de edição.

> **Observação:** Para exibir sintaxe colorida em aplicativos em tempo de execução, o Visual FoxPro deve estar configurado para isso. Esses aplicativos exibem apenas as configurações de cores padrão, pois não consultam no Registro do Windows as alterações feitas na caixa de diálogo Options.

Quando a sintaxe colorida está ativada, o Visual FoxPro executa compilação em segundo plano para a linha de código atual que está sendo digitada. Se a sintaxe for inválida, a linha será exibida com o estilo de formatação selecionado.

### Para exibir sintaxe colorida em uma janela de edição
- Abra a janela de edição desejada.
- No menu Edit, escolha Properties.
- Na caixa Edit Properties, marque Syntax coloring.
- Clique em OK.

A coloração de sintaxe será ativada para a janela selecionada. Para obter mais informações, consulte Caixa de diálogo Edit Properties.

Também é possível exibir arquivos de código-fonte na tela em cores usando o comando TYPE.

### Para personalizar as configurações de sintaxe colorida
- No menu Tools, escolha Options.
- Escolha a guia Editor.
- Em Syntax color settings, escolha as configurações desejadas.
- Ao terminar, clique em OK.

As configurações escolhidas entrarão em vigor.

### Para definir a formatação de sintaxe colorida inválida
- Ative a coloração de sintaxe na janela de edição.
- No menu Tools, escolha Options.
- Escolha a guia Editor.
- Na caixa Background Compile, escolha o estilo desejado.

A sintaxe inválida será exibida com o estilo escolhido.

# Impressão de código-fonte em cores

Você pode imprimir código-fonte em cores sempre que a sintaxe colorida aparecer, como em arquivos de programa, métodos, procedimentos armazenados e memorandos.

> **Observação:** É necessário estar conectado a uma impressora colorida para selecionar opções de impressão em cores. As cores de fundo definidas na guia Editor não são impressas. Se você selecionar impressão colorida, os hiperlinks aparecerão sublinhados.

### Para imprimir código-fonte em cores
- Abra o arquivo de programa ou código.
- No menu File, escolha Print.
- Na caixa Print, escolha a impressora colorida e clique em Preferences.
- Selecione as opções de impressão em cores disponíveis.
- Ao terminar, clique em Print.

Também é possível usar o comando TYPE com a cláusula TO PRINTER.

Para obter mais informações, consulte Caixa de diálogo Print (Visual FoxPro) e Comando TYPE.

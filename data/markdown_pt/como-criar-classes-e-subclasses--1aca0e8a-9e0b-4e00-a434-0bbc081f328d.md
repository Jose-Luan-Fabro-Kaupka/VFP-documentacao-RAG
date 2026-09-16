# Como: criar classes e subclasses

Você pode criar classes e subclasses usando o Designer de Classes do Visual FoxPro ou programaticamente. Ao usar o Designer de Classes para criar classes, você pode visualizar a classe enquanto a projeta.

> **Dica:** Por conveniência e rapidez, talvez seja melhor manter uma classe e todas as suas subclasses em uma única biblioteca de classes. Se uma classe contiver elementos de diferentes bibliotecas de classes, todas essas bibliotecas deverão estar abertas; portanto, o carregamento inicial da classe em tempo de design e de execução poderá ser mais demorado.

### Para criar uma classe ou subclasse
- No menu Arquivo, escolha Novo.
- Na caixa de diálogo Novo, escolha Classe e clique em Novo arquivo. A caixa de diálogo Nova classe será aberta.
- Na caixa Nome da classe da caixa de diálogo Nova classe, digite o nome da classe.
- Na caixa Baseada em, selecione o nome de uma classe base do Visual FoxPro. Dica Para criar uma classe definida pelo usuário, escolha Custom como classe base. Quando você escolhe a classe base Custom, a classe criada é uma classe não visual, que exibe um elemento visual em tempo de design, mas não em tempo de execução. Para obter mais informações, consulte Objeto Custom e Como: especificar a aparência de classes em tempo de design. -OU- Clique no botão de reticências (...) para selecionar um arquivo de biblioteca de classes visuais (.vcx).
- Na caixa Armazenar em, digite o nome do arquivo da biblioteca de classes para armazenar a classe.
- Clique em OK. O Designer de Classes será aberto e exibirá a classe.
- Quando terminar de criar a classe, salve-a. A classe será salva em um arquivo de biblioteca de classes visuais (.vcx) do Visual FoxPro.

O Visual FoxPro armazena as classes criadas com o Designer de Classes em arquivos de biblioteca de classes visuais (.vcx). Essas classes incluem classes visuais e não visuais.

Para obter mais informações sobre classes base no Visual FoxPro, consulte Classes base no Visual FoxPro. Para obter mais informações sobre o Designer de Classes, consulte Designer de Classes.

Você também pode adicionar classes e subclasses a uma biblioteca de classes existente. Para obter mais informações, consulte Como: adicionar classes e subclasses a bibliotecas de classes.

### Para criar classes ou subclasses em um projeto
- Abra o projeto do seu aplicativo.
- No Gerenciador de Projetos, escolha a guia Classes e clique em Novo. A caixa de diálogo Nova classe será aberta para que você especifique informações sobre a nova classe ou subclasse.
- Siga as etapas para criar uma classe ou subclasse.

Para obter mais informações, consulte Janela Gerenciador de Projetos.

### Para criar classes e subclasses programaticamente
- Use o comando CREATE CLASS ou o comando DEFINE CLASS.

O comando CREATE CLASS abre o Designer de Classes, enquanto o comando DEFINE CLASS destina-se ao uso programático. Você também pode criar e adicionar propriedades e métodos e adicionar código para responder a eventos da classe usando o comando DEFINE CLASS.

> **Observação:** Se você armazenar definições de classe em um arquivo de programa (.prg) ao usar DEFINE CLASS, poderá preceder, mas não suceder, as definições de classe com código de programa. Isso é semelhante a não colocar código de programa após procedimentos em um programa.

Para obter mais informações, consulte Comando CREATE CLASS e Comando DEFINE CLASS.

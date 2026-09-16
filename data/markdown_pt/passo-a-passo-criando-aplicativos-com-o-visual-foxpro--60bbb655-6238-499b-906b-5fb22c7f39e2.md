# Passo a passo: criando aplicativos com o Visual FoxPro

Você pode usar o Visual FoxPro para criar programas simples ou aplicativos de nível empresarial mais complexos, servidores e serviços Web XML. Você pode usar ferramentas para criar programas ou escrevê-los manualmente. Ao compilar programas Visual FoxPro, pode compilá-los como arquivos de aplicativo (.app) para execução em um ambiente Visual FoxPro ou como arquivos executáveis (.exe) ou bibliotecas de vínculo dinâmico (.dll) que podem ser chamados de qualquer lugar em um ambiente Microsoft Windows.

As seções a seguir neste passo a passo explicam como criar um programa simples e usá-lo como base para um aplicativo:
 - Usando dados
- Criando um programa para um formulário
- Criando um aplicativo

# Usando dados

Programas e aplicativos Visual FoxPro são baseados em dados em tabelas ou cursores. Os dados podem já existir no disco rígido, em um servidor remoto ou em um site Web, ou você pode criá-los no Visual FoxPro. Os dados podem estar em qualquer um dos formatos que o Visual FoxPro reconhece, incluindo objetos OLE.

Para este aplicativo de exemplo, os dados que você usará serão copiados da tabela Orders, que está incluída com o Visual FoxPro na pasta \Program Files\Microsoft Visual FoxPro 9\Samples\Data.

### Para mover dados de uma tabela para outra
- No menu Arquivo, clique em Exportar .
- Na lista suspensa Tipo na caixa de diálogo Exportar, selecione Visual FoxPro 3.0 (DBF).
- Na caixa de texto Para, digite myApp como o nome do arquivo que deseja criar.
- Clique no botão de reticências (...) e salve o arquivo na pasta Projetos do Visual FoxPro (..\My Documents\Visual FoxPro Projects).
- Na caixa de texto De na caixa de diálogo Exportar, clique no botão de reticências (...) e localize a tabela Orders.dbf na pasta \Program Files\Microsoft Visual FoxPro 9\Samples\Data.
- Na caixa de diálogo Exportar, clique em Opções .
- Na caixa de diálogo Opções de exportação, clique em Campos , mova cust_id , to_city , to_country e order_amt da lista Todos os campos para a lista Campos selecionados e clique em OK . Clique em OK mais duas vezes para fechar a caixa de diálogo Opções de exportação e a caixa de diálogo Exportar.
- No menu Arquivo, clique em Abrir .
- Na lista suspensa Arquivos do tipo, escolha Tabela , selecione a caixa de seleção abrir exclusivo e navegue até myApp.dbf .
- No menu Exibir, clique em Table Designer .
- Na guia Campos, selecione a linha to_city, clique na lista suspensa Índice e escolha Ascendente .
- Clique em OK e clique em Sim para tornar a alteração de estrutura permanente.
- No menu Janela, clique em Sessão de dados para ordenar a tabela de acordo com seu novo índice. Observação Você criou uma tabela que, por estar indexada, suporta cálculos de grupo no Report Designer .
- Na janela Sessão de dados, clique em Propriedades .
- Na lista suspensa Ordem do índice, selecione myApp:to_city e clique em OK . Você exportou campos selecionados de uma tabela para outra e depois definiu um índice na nova tabela. Deixe a janela Sessão de dados aberta e use esta tabela imediatamente para o restante deste exemplo.

# Criando um programa para um formulário

Você pode criar programas Visual FoxPro simples a partir dos menus e da IDE. Esses programas executam no Visual FoxPro ou acessam o Runtime do Visual FoxPro.

### Para criar o formulário
- No menu Arquivo, clique em Novo .
- Clique em Formulário e depois em Novo arquivo . Isso abre o Form Designer, adiciona o menu Formulário e a barra de ferramentas Form Controls e exibe a janela Propriedades do formulário. Se a barra de ferramentas não estiver visível, você pode abri-la no menu Exibir.
- Na janela Propriedades do formulário, selecione Caption e digite myForm .

### Para adicionar um rótulo
- Na barra de ferramentas Form Controls, clique em Label e arraste um retângulo no formulário.
- Na janela Propriedades do controle de rótulo, selecione Caption e altere para My Data Form . Depois, selecione FontSize e digite 20 .
- Se necessário, redimensione o rótulo para que o texto caiba.

### Para adicionar uma grade
- Na barra de ferramentas Form Controls, clique em Grid e desenhe um retângulo no formulário.
- Clique com o botão direito no controle Grid e selecione Builder no menu de atalho.
- No Grid Builder, selecione a tabela myApp .
- Na guia Grid Items, mova todos os itens da lista Available fields para a lista Selected fields e feche o construtor.

### Para adicionar um botão
- Na barra de ferramentas Form Controls, clique no ícone Command Button e desenhe um retângulo no formulário abaixo da grade.
- Clique duas vezes no botão recém-criado e digite o seguinte código no editor de código. Feche a janela de edição de código quando terminar. THISFORM.RELEASE Este código fechará o formulário quando você não precisar mais dele.
- Na janela Propriedades do controle de botão, selecione Caption e digite Exit .
- No menu Arquivo, clique em Salvar como e salve o formulário como myForm .
- Clique em Executar ( ! ) na barra de ferramentas para visualizar seu formulário.

### Para concluir o programa
- No menu Arquivo, clique em Novo .
- Clique em Programa e depois em Novo arquivo . Isso abre o editor do Visual FoxPro.
- No editor, digite o seguinte: DO FORM myForm.scx
- Salve este programa como myProgram . Isso cria um arquivo de programa Visual FoxPro (.prg) que executa seu formulário a partir do seguinte comando na janela Command: DO myProgram

Agora você colocou uma tabela (como grade), um rótulo e um botão em um formulário. Você criou um programa para executar na janela Command ou no menu Programa. Na próxima seção, o aplicativo troca um formulário de revisão de dados pela grade e o adiciona ao programa antes de compilá-lo em um arquivo.

# Criando um aplicativo

Executar o programa que você criou anteriormente requer que o Visual FoxPro esteja instalado no computador. No entanto, você pode criar um aplicativo com o Visual FoxPro que será executado em um computador que não tenha o Visual FoxPro instalado.

O programa anterior tem apenas um formulário e não tem muita funcionalidade. Esta seção orienta você na adição de um formulário de revisão de dados com alguns controles adicionais e depois na compilação dos dois formulários — primeiro em um aplicativo Visual FoxPro e depois em um aplicativo Windows. Um arquivo de aplicativo Visual FoxPro (.app) ou um arquivo executável Visual FoxPro (.exe) pode ser executado em plataformas Windows se o Visual FoxPro estiver instalado. Um aplicativo Visual FoxPro compilado como arquivo executável (.exe) também pode ser executado em plataformas Windows com apenas o Runtime do Visual FoxPro instalado.

Nesta seção, você criará um aplicativo usando o Application wizard, o Application builder e o Project manager.
 - O Application wizard cria um projeto e fornece a estrutura avançada de aplicativo para que você possa adicionar componentes que já criou ou criar um aplicativo do início ao fim, incluindo telas de abertura e outras melhorias.
- O Application builder permite adicionar tabelas, formulários e relatórios a um projeto existente.
- O Project manager, a ferramenta de construção de aplicativos mais fundamental no Visual FoxPro, fornece acesso a todos os componentes que você pode querer incluir em um aplicativo e os contém para compilação.

Para este passo a passo, você usa o Application wizard primeiro.

### Para criar um aplicativo
- No menu Ferramentas, aponte para Wizards e clique em Application .
- Na caixa Nome do projeto, digite MyApplication , salve o projeto na pasta Projetos do Visual FoxPro (..\My Documents\Visual FoxPro Projects) e clique em OK .

O Visual FoxPro se prepara para criar um arquivo de projeto com o nome que você especificou. Quando termina de criar o projeto, duas janelas aparecem: o Project Manager e o Application Builder. Nos procedimentos a seguir, você usa o Application Builder para adicionar componentes e funcionalidade ao seu aplicativo.

### Para especificar informações da tela de abertura e da caixa de diálogo Sobre
- Na guia General do Application Builder, clique no botão de reticências (...) ao lado da caixa Image.
- Encontre o logotipo do Visual FoxPro, fox.bmp , na pasta do Visual FoxPro (..\Program Files\Microsoft Visual FoxPro VersionNumber ) e clique em OK . Esta imagem aparecerá na tela de abertura do seu aplicativo. Observação Se você fechar o Application builder, pode reabri-lo clicando no menu Ferramentas, apontando para Wizards e clicando em All Wizards . Clique em Application Builder na caixa de diálogo Seleção de assistente e depois em OK .
- Na guia Credits do Application Builder , adicione as informações de autoria e versão apropriadas.

### Para especificar a fonte de dados
- Na guia Data, clique em Select e encontre e selecione myAPP (a tabela que você usou anteriormente no programa simples). Observação Você pode escolher qualquer tabela disponível. Esta guia também fornece botões para que você possa criar tabelas ou um banco de dados facilmente.

### Para criar um formulário e um relatório
- Na guia Data, você pode selecionar de listas de modelos de formulário e relatório que fazem parte do Advanced Application Framework (incluído no Application Builder). Aceite os valores padrão nas listas suspensas e clique em Generate . O Visual FoxPro gera um formulário e um relatório da tabela que você especifica e dá acesso a eles nas guias Forms e Reports do Application builder. Esses componentes tornam-se parte do projeto que você está construindo, e os arquivos são salvos nas pastas Forms ou Reports na pasta Projetos do Visual FoxPro (..\My Documents\Visual FoxPro Projects).

### Para adicionar controles ao formulário
- Na guia Forms do Application Builder, clique em Edit para abrir o Form Designer, onde você pode fazer quaisquer adições ou alterações. Como está, o formulário exibirá apenas o primeiro registro; portanto, você deve adicionar pelo menos mais um controle; neste procedimento, você adiciona dois.
- Na caixa de ferramentas do Form Designer, clique no ícone Button e arraste um retângulo no formulário. Na propriedade Caption, digite Next .
- Clique duas vezes no botão Next no formulário e digite o seguinte código no editor de código. Feche a janela de edição de código quando terminar. IF NOT EOF() SKIP ELSE GO TOP ENDIF THISFORM.REFRESH Este código percorre os registros da tabela e exibe cada registro. Você também poderia adicionar outro botão, com código apropriado, para voltar na tabela.
- Copie o botão Next e coloque a cópia na extremidade direita do formulário. Na propriedade Caption, digite Exit .
- Clique duas vezes no botão Exit e, na janela de edição do evento Click, substitua o código na janela pelo seguinte código e feche a janela: THISFORM.RELEASE Este código fecha seu formulário.

### Para adicionar cálculos ao relatório
- Na guia Reports do Application Builder, clique em Edit para MyApp para abrir o Report Designer . Expanda todas as faixas do relatório para facilitar as operações a seguir. Observação É aqui que você pode fazer quaisquer adições ou alterações, como reorganizar campos ou adicionar controles.
- No menu Exibir, clique em Data Environment .
- Clique com o botão direito na janela Data Environment e selecione Properties no menu de atalho. Isso definirá a janela Propriedades para o Dataenvironment .
- Na janela Propriedades, escolha o cursor na lista suspensa Properties Description e altere a propriedade Order para to_city para tornar o agrupamento possível.
- No menu Relatório, clique em Data Grouping .
- Na caixa de diálogo Data Grouping, clique no botão Add e depois clique duas vezes em to_city na lista Fields no Expression Builder . Clique em OK em ambas as caixas de diálogo.
- No Report Designer, copie e cole o elemento to_city e arraste o elemento colado da faixa Detail para a faixa Group Footer para totais de grupo. Repita este procedimento para colocar outra cópia do elemento to_city no Page Footer para a tabela inteira.
- Para cada cópia do elemento to_city, clique duas vezes no elemento para abrir a caixa de diálogo Report Expression.
- Clique em Calculations .
- Na caixa de diálogo Calculation Field, clique em Count . A lista suspensa Reset deve exibir a seleção padrão, que é o campo to_city. Isso significa que a função Count será redefinida para zero cada vez que o valor do elemento to_city mudar na passagem pela tabela. Isso está correto para a faixa Group Footer, mas você deve alterar esta seleção para o elemento to_city na faixa Page Footer.
- Depois de selecionar Count na caixa de diálogo Calculate Field do elemento to_city que você colocou na faixa Page Footer, altere o valor Reset para End of Report .
- Depois de definir o campo Calculation de cada elemento to_city, clique em OK para fechar a caixa de diálogo.
- Clique em OK para fechar o Application Builder.

> **Observação:** Além dos recursos que você especificou no Application wizard, o Visual FoxPro criou outros componentes para seu aplicativo. Quando você executar seu aplicativo, descobrirá um menu Arquivo personalizado e uma caixa de diálogo da qual pode executar seu formulário e seu relatório.

Agora você pode usar o Project manager para revisar os componentes que criou. Você descobrirá que o Application wizard criou muitos componentes, que você modificou no Application builder e nos designers de formulário e relatório. Você pode examinar e modificar esses componentes em várias ferramentas do Visual FoxPro, como os designers ou o Class Browser e o Object Browser.

Neste ponto, o uso mais importante do Project manager é concluir a compilação de seus arquivos em um aplicativo.

### Para concluir o aplicativo
- No Project Manager , clique em Build .
- Clique em Application (app) para criar um aplicativo a ser executado apenas no Visual FoxPro. Observação Se você selecionar Win 32 executable / COM server (exe) , cria um aplicativo que pode ser executado em um computador com apenas o Runtime do Visual FoxPro instalado.
- Clique em OK .

Quando o processo de compilação é concluído, você tem um aplicativo que pode executar no Visual FoxPro clicando duas vezes no arquivo .app. Quando o programa abre, exibe a tela de abertura e depois a caixa de diálogo Quick Start da qual você pode visualizar seu formulário e seu relatório. O aplicativo também fornece um item de menu Quick Start.

Para obter mais informações sobre como criar programas e aplicativos, consulte Application Wizard e Application Builder.

Para obter mais informações sobre o Project Manager e detalhes sobre opções de compilação de aplicativos, consulte Janela Project Manager e Caixa de diálogo Opções de compilação.

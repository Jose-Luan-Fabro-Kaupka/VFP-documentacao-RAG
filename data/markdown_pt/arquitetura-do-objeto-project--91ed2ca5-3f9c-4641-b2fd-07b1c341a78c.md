# Arquitetura do objeto Project

Um objeto Project do Visual FoxPro expõe a interface IDispatch para que clientes de automação, controles ActiveX e outros objetos COM possam acessar o objeto de projeto por meio de interfaces OLE padrão. Ao manipular projetos, os erros que podem ocorrer são erros OLE porque um objeto Project expõe a interface IDispatch.

# Eventos do projeto

As seções a seguir descrevem eventos e a ordem em que ocorrem quando projetos são criados, modificados, fechados, compilados e assim por diante.

### Criando um novo projeto

Os eventos a seguir ocorrem quando você executa CREATE PROJECT, cria um novo projeto no menu Arquivo ou clica no botão Novo na barra de ferramentas padrão para criar um novo projeto:
 - O objeto Project é criado.
- O objeto ProjectHook é instanciado.
- O evento Init do objeto ProjectHook ocorre. Se o evento Init retornar verdadeiro (.T.), o padrão, o projeto é criado e o projeto é exibido no Project Manager. Se o evento Init retornar falso (.F.), o projeto não é criado, os objetos Project e ProjectHook são liberados e o Project Manager não é exibido.

### Modificando um projeto existente

Os eventos a seguir ocorrem quando você executa MODIFY PROJECT, modifica um projeto existente no menu Arquivo ou clica no botão Abrir na barra de ferramentas padrão para abrir um projeto existente ou criar um novo projeto:
 - O objeto Project é criado. O objeto Project obtém seus valores do arquivo .pjx do projeto.
- O objeto ProjectHook é instanciado.
- O evento Init do objeto ProjectHook ocorre. Se o evento Init retornar verdadeiro (.T.) (o padrão), o projeto é aberto para modificação no Project Manager. Se o evento Init retornar falso (.F.), o projeto não é aberto para modificação, os objetos Project e ProjectHook são liberados e o Project Manager não é exibido.

### Fechando um projeto

Os eventos a seguir ocorrem quando um projeto aberto é fechado:
 - O evento Destroy do ProjectHook ocorre e o objeto ProjectHook é liberado.
- O objeto Project é liberado.

### Emitindo BUILD APP, BUILD DLL ou BUILD EXE

Os eventos a seguir ocorrem quando BUILD APP, BUILD DLL ou BUILD EXE é emitido:
 - O objeto Project é criado. O objeto Project obtém seus valores do arquivo .pjx do projeto.
- O objeto ProjectHook é instanciado.
- O evento Init do objeto ProjectHook ocorre. Se o evento Init retornar verdadeiro (.T.), o padrão, o evento BeforeBuild do ProjectHook ocorre. Se NODEFAULT for incluído no evento BeforeBuild, o .app, .dll ou .exe não é compilado. Caso contrário, o processo de compilação continua. Se algum arquivo for adicionado ao projeto durante o processo de compilação, o evento QueryAddFile do ProjectHook ocorre antes de cada arquivo ser adicionado. Se NODEFAULT for incluído no evento QueryAddFile, um arquivo não é adicionado ao projeto. Caso contrário, o arquivo é adicionado ao projeto. Quando o .app, .dll ou .exe é compilado com sucesso, o evento AfterBuild do ProjectHook ocorre, e depois o evento Destroy do ProjectHook ocorre. Se o evento Init retornar falso (.F.), o app, .dll ou .exe não é compilado, e os objetos Project e ProjectHook são liberados.

### Emitindo BUILD PROJECT

Os eventos a seguir ocorrem quando BUILD PROJECT com a cláusula FROM é emitido. Se a cláusula FROM for omitida, os eventos ocorrem na ordem descrita acima quando BUILD APP, BUILD DLL ou BUILD EXE é emitido.
 - O objeto Project é criado. O objeto Project obtém seus valores do arquivo .pjx do projeto.
- O objeto ProjectHook é instanciado.
- O evento Init do objeto ProjectHook ocorre. Se o evento Init retornar verdadeiro (.T.), o padrão, os arquivos especificados na cláusula FROM são adicionados individualmente ao projeto. O evento QueryAddFile do ProjectHook ocorre antes de cada arquivo ser adicionado ao projeto. Se NODEFAULT for incluído no evento QueryAddFile, o arquivo não é adicionado ao projeto. Caso contrário, o arquivo é adicionado ao projeto. O evento BeforeBuild do ProjectHook então ocorre. Se NODEFAULT for incluído no evento BeforeBuild, o projeto não é compilado. Caso contrário, o projeto é compilado.
- Quando a compilação do projeto é concluída, o evento AfterBuild do ProjectHook ocorre, e depois o evento Destroy do ProjectHook ocorre. Se o evento Init do ProjectHook retornar falso (.F.), o projeto não é compilado. Os objetos Project e ProjectHook são liberados e um novo arquivo .pjx não é criado.

### Usando uma operação de arrastar e soltar

Os eventos a seguir ocorrem quando você arrasta um arquivo ou um conjunto de arquivos sobre a seção de estrutura (treeview) do Project Manager:
 - Quando o ponteiro do mouse está posicionado sobre a seção de estrutura do Project Manager, o evento OLEDragOver do ProjectHook ocorre com o parâmetro nState definido como 0 (DRAG_ENTER em Foxpro.h). O evento OLEDragOver então ocorre repetidamente com o parâmetro nState definido como 2 (DRAG_OVER em Foxpro.h). Se o ponteiro do mouse sair da seção de estrutura do Project Manager, o evento OLEDragOver ocorre com o parâmetro nState definido como 1 (DRAG_LEAVE em Foxpro.h).
- O evento OLEDragDrop do ProjectHook ocorre se você soltar o botão do mouse enquanto o ponteiro do mouse está posicionado sobre a seção de estrutura do Project Manager. Por padrão, o Visual FoxPro adiciona cada arquivo solto no Project Manager ao projeto. O evento QueryAddFile do ProjectHook ocorre antes de cada arquivo ser adicionado ao projeto.

### Adicionando um arquivo com o botão Add

Os eventos a seguir ocorrem quando você adiciona um arquivo a um projeto clicando no botão Add no Project Manager:
 - A caixa de diálogo Abrir aparece.
- Se você selecionar um arquivo e escolher OK , um objeto de arquivo é criado para o arquivo selecionado.
- O evento QueryAddFile do ProjectHook ocorre e o nome do objeto de arquivo é passado para o evento. Se NODEFAULT for incluído no evento QueryAddFile, o arquivo não é adicionado ao projeto. Caso contrário, o arquivo é adicionado ao projeto.

### Adicionando um arquivo com o botão New

Os eventos a seguir ocorrem quando você adiciona um novo arquivo a um projeto clicando no botão New no Project Manager:
 - O designer ou editor apropriado para o arquivo é exibido.
- Quando o novo arquivo é salvo, a caixa de diálogo Salvar como é exibida. Clicar em Salvar cria um objeto de arquivo para o novo arquivo.
- O evento QueryAddFile do ProjectHook ocorre e o nome do objeto de arquivo é passado para o evento. Se NODEFAULT for incluído no evento QueryAddFile, o arquivo não é adicionado ao projeto. Caso contrário, o arquivo é adicionado ao projeto.

### Modificando um arquivo com o botão Modify

Os eventos a seguir ocorrem quando você modifica um arquivo em um projeto clicando no botão Modify no Project Manager:
 - O evento QueryModifyFile do ProjectHook ocorre antes do designer ou editor apropriado para o arquivo ser exibido.
- O objeto de arquivo do arquivo a modificar é passado como parâmetro para o evento QueryModifyFile. Se NODEFAULT for incluído no evento QueryModifyFile, o designer ou editor apropriado para o arquivo não é exibido e o arquivo não é modificado. Caso contrário, o arquivo é aberto no designer ou editor apropriado para modificação.

### Removendo um arquivo com o botão Remove

Os eventos a seguir ocorrem quando você remove um arquivo em um projeto clicando no botão Remove no Project Manager:
 - O evento QueryRemoveFile do ProjectHook ocorre.
- O objeto de arquivo do arquivo a ser removido é passado como parâmetro para o evento QueryRemoveFile. Se NODEFAULT for incluído no evento QueryRemoveFile, o arquivo não é removido do projeto. Caso contrário, o arquivo é removido do projeto.

### Executando um arquivo com o botão Run

Os eventos a seguir ocorrem quando você executa um arquivo em um projeto clicando no botão Run no Project Manager:
 - O evento QueryRunFile do ProjectHook ocorre.
- O objeto de arquivo do arquivo a ser executado é passado como parâmetro para o evento QueryRunFile. Se NODEFAULT for incluído no evento QueryRunFile, o arquivo não é executado. Caso contrário, o arquivo é executado.

### Recompilando um projeto ou compilando um arquivo com o botão Build

Os eventos a seguir ocorrem quando você recompila o projeto ou compila um .app, .dll ou .exe de um projeto clicando no botão Build no Project Manager:
 - A caixa de diálogo Build Options é exibida.
- Você pode escolher Rebuild Project , Build Application , Build Executable ou Build COM DLL , e especificar opções adicionais de compilação. Se você clicar em Cancelar , a compilação não ocorre.
- O evento BeforeBuild do ProjectHook ocorre se você clicar em OK , e o processo de compilação começa.
- Quando a compilação é concluída, o evento AfterBuild do ProjectHook ocorre.

# Métodos do Class Browser

Os seguintes métodos estão associados ao Class Browser. Para obter mais informações, consulte How to: Customize the Class Browser e Class Browser Window.
 **AddClass( )**
Copia uma classe de um arquivo de biblioteca de classes (.vcx) para outro. Usado após uma operação de arrastar e soltar entre instâncias do Class Browser e dependente da propriedade oSource. Se a classe especificada não existir, uma classe é criada.
**AddFile( [ cFileName ][, lIgnoreRefresh ] )**
Adiciona um arquivo de biblioteca de classes (.vcx) ou formulário (.scx) à lista de classes do Class Browser. Se nenhum parâmetro for passado, uma caixa de diálogo AddFile aparece usando o método GetFile( ) do Class Browser. Se lIgnoreRefresh for True (.T.), a lista de classes do Class Browser não é atualizada. Se você estiver adicionando vários arquivos, pode aguardar até que todas as classes sejam adicionadas antes de atualizar a lista.
**AddIn( cName [, cProgram ] [, cMethod ] [, cFileFilter ] [, cPlatform ] [, cComment ] )**
Instala ou remove o add-in especificado na tabela de registro Browser.dbf. A lista a seguir descreve os parâmetros disponíveis para este método: cName Especifica o nome do add-in. Não diferencia maiúsculas de minúsculas; no entanto, quando exibido em um menu, o valor aparece conforme inserido. cProgram Especifica o nome de um programa (.PRG), formulário (.scx), aplicação (.APP), arquivo executável (.EXE) ou programa compilado (.FXP) a executar. Se nenhuma extensão for fornecida, a extensão .PRG é assumida. Observação Se este argumento for .NULL., o add-in é marcado para exclusão em Browser.dbf e desabilitado no menu de atalho de add-in. cMethod Especifica um nome de método a usar como hook de evento. Se vazio, o add-in aparece no menu. cFileFilter Especifica uma lista de bibliotecas de classes e formulários que habilitam o add-in. Se vazio, o add-in está disponível para todas as bibliotecas de classes (.vcx) e formulários (.scx). cPlatform Especifica a plataforma na qual o add-in está disponível. Se vazio, o add-in está disponível em todas as plataformas suportadas pelo Visual FoxPro. cComment Especifica texto armazenado em um campo memo em Browser.dbf.
**AddInMenu( )**
Expande o menu que exibe os add-ins registrados.
**AddInMethod( cObjMethod )**
Executa qualquer add-in registrado para o método de objeto especificado. Exemplo: Para alterar o comportamento padrão do botão Help no Class Browser, use o seguinte código: _OBROWSER.AddInMethod("cmdHelp.click")
**AutoRefresh( )**
Determina se deve atualizar a exibição verificando informações atualizadas da biblioteca de classes (.vcx) na classe selecionada na lista de classes e verificando o número total de registros no arquivo de biblioteca de classes (.vcx) sendo editado. Este método é executado quando o formulário Class Browser é ativado.
**BinToInt( [ cBinaryValue ] )**
Retorna o equivalente inteiro de uma cadeia de caracteres representando um valor binário. Por exemplo, passar para este método um cBinaryValue de "11001" retornaria 25.
**CleanUpFile( )**
Remove registros do arquivo de biblioteca de classes (.vcx) associado à classe selecionada na lista de classes.
**ClearBrowser( )**
Somente para uso interno.
**ClearClass( [ lClearAll ] )**
Limpa o cache de classes da memória com o comando CLEAR CLASS para uma classe específica, ou todas as classes exibidas se lClearAll estiver definido como True (.T.).
**NewClass( )**
Cria uma subclasse da classe selecionada na lista de classes.
**DeactivateMenu( )**
Desativa o menu pop-up de add-in.
**DisplayMenu( tnMenuMode )**
Exibe o menu de atalho na localização atual do ponteiro do mouse. Se tnMenuMode for 0, o menu de atalho do formulário Class Browser é exibido; se 1, o menu de atalho da lista de classes; se 2, o menu de atalho da lista de membros.
**DoAddIn( [ cAddInName ] )**
Executa o add-in especificado do registro atual ou específico da tabela com o alias BROWSER.
**FileMatch( cFileName , cFileList )**
Compara o arquivo especificado contra a lista de arquivos especificada para determinar se o arquivo é um associado ao add-in.
**ExportClass( [ lShow ] [, tcExportToFileName ] )**
Gera e exibe o código-fonte de definição da classe selecionada ou do arquivo selecionado na lista de classes. A lista a seguir descreve os parâmetros disponíveis para este método: lShow Especifica se deve exibir o código. Se o parâmetro lShow for True (.T.), a janela Class Browser exibe o código. tcExportToFileName Especifica o nome do arquivo que receberá o código.
**FindClass( [ cFind ] )**
Encontra texto de classe dentro de uma classe.
**FormAddObject( oObject [, nXCoord ] [, nYCoord ] [, lActivateForm ] [, lDesignMode ][, lNoShow ] [, lNoErrors ] [, lBuilder ] [, oForm ] )**
Adiciona uma instância da classe selecionada na lista de classes a um formulário externo. A lista a seguir descreve os parâmetros disponíveis para este método: oObject Especifica uma referência ao contêiner de destino. Os valores podem ser "command" para a janela Command, "screen" para a área de trabalho do Visual FoxPro, ou "new". Você pode implementar essas opções com os seguintes comandos: _oBrowser.FormAddObject("command") _oBrowser.FormAddObject("-screen") _oBrowser.FormAddObject("new") nXCoord Especifica a posição horizontal do objeto dentro do contêiner. Se nenhum valor for passado, a posição atual do mouse é usada. nYCoord Especifica a posição vertical do objeto dentro do contêiner. Se nenhum valor for passado, a posição atual do mouse é usada. lActivateForm Se True (.T.), o formulário de destino é ativado quando o objeto é adicionado a ele; se False (.F.), o Class Browser permanece ativo. lDesignMode Se True (.T.), a referência do objeto é um objeto atualmente no Form Designer ou class designer. lNoShow Se True (.T.), a referência do objeto é um objeto atualmente no Form Designer ou class designer. lNoErrors Especifica se erros gerados na instanciação são ignorados. Se False (.F.), os erros são exibidos no Class Browser. lBuilder Especifica se um builder personalizado é iniciado após o objeto ser adicionado a um contêiner. oForm Especifica o contêiner ao qual um objeto é adicionado. oForm, um parâmetro opcional, é usado principalmente para conter o objeto host no modo de design.
**FormatMethods( cMethods )**
Formata o texto dos métodos gerados na exibição do código de definição da classe.
**FormatProperties( cProperties [, lAddObjectMode ] )**
Formata o texto das propriedades geradas na exibição do código-fonte de definição da classe.
**GetFile( [ cFileExt ] )**
Abre a caixa de diálogo GetFile( ) do Class Browser. O método GetFile( ) é usado internamente pelos botões Open ou Add no Class Browser. Sempre que o Class Browser solicita uma biblioteca de classes (.vcx) ou formulário (.scx), o método GetFile( ) é chamado internamente.
**GetTimeStamp( [ ntimestamp ] )**
Retorna o equivalente de caractere de um valor de timestamp. Se nenhum parâmetro for passado, retorna a cadeia de timestamp do arquivo atualmente selecionado.
**IndentText( cCode )**
Recua um bloco de texto uma tabulação.
**IntToBin( [ nInteger ] )**
Retorna uma cadeia de caracteres representando um valor binário que é o equivalente de um valor inteiro. Por exemplo, passar para este método um nInteger de 25 retornaria "11001".
**ModifyClass( )**
Abre a classe selecionada no Class Designer.
**MsgBox( cMessage [, nType ] [, cTitle ] )**
Exibe a caixa de mensagem do Class Browser. Semelhante à função MESSAGEBOX( ) do Visual FoxPro.
**NewFile( [ cFileName ] [, lOpenFile ] )**
Cria um novo arquivo de biblioteca de classes (.vcx). Se nenhum parâmetro for passado, a caixa de diálogo Open é exibida. Se parâmetros forem fornecidos, uma nova biblioteca de classes (.vcx) é criada e adicionada à lista de classes no Class Browser.
**OpenFile( [ cFileName ] )**
Abre um arquivo de biblioteca de classes (.vcx) ou formulário (.scx) existente. Se um nome de arquivo não for fornecido, a caixa de diálogo Open aparece.
**ProperBaseClass( cBaseClass )**
Retorna o nome da classe base com a capitalização adequada. Por exemplo, "combobox" retornaria como "ComboBox".
**RedefineClass( [ cAsClass ] [, cClassLoc ] )**
Altera a classe pai da classe selecionada na lista de classes.
**RefreshButtons( )**
Atualiza os botões de comando do Class Browser baseado no tipo de arquivo.
**RefreshClassIcon( )**
Recarrega o ícone da classe do arquivo de ícone.
**RefreshClassList( [ cDefaultClass ] [, lIgnoreTable ] )**
Atualiza a lista de classes.
**RefreshClassListSubclass( )**
Somente para uso interno.
**RefreshFileAttrib( )**
Atualiza o status de atributo de arquivo do nome de arquivo associado à classe selecionada na lista de classes.
**RefreshCaption( )**
Atualiza o Caption do Class Browser de um formulário.
**RefreshDescriptions( )**
Somente para uso interno. Atualiza as descrições de classes e membros.
**RefreshMembers( [ tcDefaultMember ] )**
Atualiza as guias Member para exibir informações associadas à classe selecionada na lista de classes e, se fornecido, o membro especificado.
**RefreshParentClassBrowser( )**
Atualiza o estado da barra de ferramentas ParentClass Browser.
**RefreshPrefRecNo( )**
Atualiza o ponteiro de registro de preferência Browser.dbf para o arquivo de biblioteca de classes (.vcx) ou formulário (.scx) sendo editado.
**RefreshRecNo( )**
Atualiza o ponteiro de registro atual da tabela de biblioteca de classes (.vcx) ou formulário (.scx) para o arquivo da classe selecionada.
**RemoveClass( [ lConfirm ] )**
Remove a classe selecionada na lista de classes de sua biblioteca de classes (.vcx) associada.
**RenameClass( [ cToClass ] )**
Altera o nome da classe da classe selecionada na lista de classes.
**ResetDefaults( )**
Restaura as configurações de exibição originais. Este método é chamado quando você escolhe Restore Defaults no menu de atalho.
**SavePreferences( )**
Salva as configurações de preferência atuais na tabela de registro Browser.dbf.
**ScaleResize( )**
Dimensiona os controles no formulário Class Browser para ajustar após o formulário ser redimensionado usando o evento Resize( ).
**SeekClass( [ cClass ][, cClassLibrary] )**
Move o ponteiro da lista de classes para uma classe ou índice específico na lista de classes. Pode usar o valor numérico da posição visual na lista de classes.
**SeekMember( tcMember )**
Move o ponteiro da lista de membros para um membro específico.
**SeekParentClass( )**
Exibe a classe pai da classe selecionada na lista de classes.
**SetBusyState( lBusyState )**
Define a propriedade lBusyStatus como True (.T.) ou False (.F.) baseado no parâmetro recebido; também define a forma do ponteiro do mouse como uma seta ou ampulheta.
**SetFont( [ cFontName ][, nFontSize ][, lFontBold ][, lFontItalic ] )**
Define a fonte e o tamanho da fonte usados pelo Class Browser para seu formulário, controles e caixas de diálogo. Se você não especificar um nome ou tamanho de fonte, SetFont( ) abre a caixa de diálogo Get Font.
**ShowMenu( aMenu [, cOnS election ] )**
Exibe um menu baseado em um array. Se um menu é um array de dimensão única, este método exibe uma lista de todos os itens no seu menu. Se o array é bidimensional com um item e uma ação, exibe os itens do menu e, quando o item é selecionado, executa a ação associada.
**TrimExt( cFileName [, lPlatformType ] )**
Trunca a extensão do nome do arquivo.
**TrimFile( cFileName [, lPlatformType ] )**
Trunca o nome do arquivo e retorna apenas o nome e o caminho do arquivo.
**TrimPath( cFileName [, lTrimExt ] [, lPlatformType ] )**
Trunca o nome do caminho.
**UpdateReferences( tcOldClassLoc, tcOldClass, tcNewClassLoc, tcNewClass [, tlAllInstances ] )**
Usado para atualizar referências de classes (subclasses e membros de objeto) ao renomear uma classe e ao mover uma classe de um class browser para outro. A lista a seguir descreve os parâmetros disponíveis para este método: tcOldClassLoc Especifica o conteúdo original do campo ClassLoc no arquivo .vcx ou .scx. tcOldClass Especifica o conteúdo original do campo Class no arquivo .vcx ou .scx. tcNewClassLoc Especifica o novo conteúdo do campo ClassLoc no arquivo .vcx ou .scx. tcNewClass Especifica o novo conteúdo do campo Class no arquivo .vcx ou .scx. tlAllInstances Se True (.T.), todos os arquivos em todas as janelas Class Browser são atualizados. Se False (.F.), apenas os arquivos na janela Class Browser atual são atualizados.
**VersionCheck( [ lShowErrorMsg ] )**
Valida o arquivo de biblioteca de classes (.vcx) ou formulário (.scx) aberto.
**ViewProperty( cProperty )**
Exibe o valor de uma propriedade específica da classe selecionada.
**WildcardMatch( cMatchExpList , cExpressionSearched )**
Compara cadeias de caracteres para uma correspondência de curinga com os filtros especificados na caixa Type.

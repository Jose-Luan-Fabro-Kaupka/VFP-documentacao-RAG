# Propriedades do Class Browser

As propriedades a seguir estão associadas ao Class Browser. Para obter mais informações, consulte How to: Customize the Class Browser e Class Browser Window.

> **Observação:** Propriedades marcadas como "Reference only" ou "Internal use only" são mantidas internamente e usadas pelo Class Browser. Evite alterar o valor de propriedades somente de referência; você pode causar erros no Class Browser.
 **lActive**
Somente referência. Retorna o status ativo do Class Browser. Se o Class Browser tem o foco, o valor é True (.T.).
**cAlias**
Retorna o alias da área de trabalho na sessão de dados do Class Browser associada à classe selecionada na lista de classes. Por padrão, a sessão de dados privada do Class Browser abre pelo menos dois aliases de tabela: BROWSER e METADATA. O alias BROWSER é para Browser.dbf e é compartilhado por todas as instâncias. O alias METADATA é para a biblioteca de classes (.vcx) ou formulário (.scx) aberto no Class Browser. Se mais de um arquivo estiver aberto, o alias METADATA é incrementado uma vez para cada arquivo aberto.
**cAddInMethod**
Somente referência. Retorna o nome do método que chamou o add-in externo em execução e é limpo quando a execução é concluída. Quando um add-in é executado, esta propriedade contém o nome do método que chamou o add-in.
**lAddInMode**
Retorna o status de um add-in do Class Browser. Se True (.T.), o add-in é chamado; se False (.F.), o add-in foi concluído.
**lAddInTrace**
Retorna o status do modo de exibição de trace que monitora os eventos de um add-in. Se True (.T.), mensagens que descrevem os eventos de um add-in são enviadas para a janela principal do Visual FoxPro.
**nAtPos**
Somente para uso interno. O valor padrão é 0.
**lAutoExpand**
Determina se a lista de classes expande ou recolhe automaticamente quando é atualizada. Se o valor é True (.T.), a lista de classes expande ou recolhe automaticamente as árvores de classes no outline. Se False (.F.), o outline da lista de classes não expande nem recolhe. O valor padrão é True (.T.).
**cBaseClass**
Somente referência. Retorna o nome da classe base da classe selecionada na lista de classes.
**cBrowserTable**
Somente referência. Retorna o caminho completo da tabela de registro Browser.dbf.
**lBusyState**
Somente referência. Retorna o status da operação de atualização do Class Browser. Se True (.T.), a operação de atualização está em andamento.
**cClass**
Somente referência. Retorna o nome da classe selecionada na lista de classes.
**nClassCount**
Somente referência. Retorna o número total de itens na lista de classes. O valor padrão é 0.
**cClassLibrary**
Somente referência. Retorna o nome da biblioteca de classes da classe selecionada na lista de classes.
**aClassList**
Somente referência. Uma matriz bidimensional de valores associados a uma biblioteca de classes (.vcx) ou arquivo de formulário (.scx) na lista de classes atual. Cada arquivo na lista tem seu próprio alias. Por exemplo, se a lista de classes exibe dois arquivos, os aliases são METADATA1 e METADATA2. A matriz contém a seguinte formação. Posição em aClassList Configuração [ nIndex ,1] Nome de uma classe [ nIndex ,2] Número do registro de metadados associado [ nIndex ,3] Nível de indentação do outline [ nIndex ,4] Nome do arquivo que contém a classe pai [ nIndex ,5] Nome da classe pai [ nIndex ,6] Nome do arquivo que contém a classe [ nIndex ,7] Nome do arquivo de ícone da classe [ nIndex ,8] BaseClass da classe [ nIndex ,9] Especifica se a classe é definida como OLE public
**nClassListIndex**
Somente referência. Retorna a posição da classe selecionada na lista de classes. O valor do primeiro item é 0. O valor padrão é – 1.
**nClassTimeStamp**
O valor TimeStamp (do campo TimeStamp em .vcx/.scx) para a classe selecionada.
**cClassType**
Somente referência. Retorna o filtro atual na lista de classes conforme especificado na caixa ClassType.
**tcClassType**
O filtro Type inicial para a lista de classes.
**tcDefaultClass**
Somente referência. Retorna o valor ou referência do segundo parâmetro passado a BROWSER.APP. Por exemplo, se você abrir o Class Browser digitando o seguinte código, esta propriedade retorna "baseform." DO (_BROWSER) WITH "wizstyle.vcx","baseform"
**lDescriptions**
Se True (.T.), descrições são exibidas para classes e membros.
**lDisplayHierarchyError**
Se uma mensagem de erro deve ser exibida quando classes sem ParentClasses válidas são carregadas no Class Browser. O padrão é True (.T.).
**nDisplayMode**
Somente referência. Retorna o modo de exibição especificado pelo grupo de opções de modo de exibição: 1 – hierárquico ou 2 – alfabético. O valor padrão é 1.
**lDragDrop**
Somente para uso interno. Se uma operação de arrastar está em andamento.
**cDragIcon**
Retorna o arquivo de cursor atual para o ícone de arrastar durante uma operação de arrastar.
**lEmptyFilter**
Se True (.T.), métodos vazios são exibidos na lista Members. O padrão é False (.F.).
**lError**
Retorna o status da verificação de erros. Se True (.T.), ocorreu um erro e a caixa de diálogo de erro do Class Browser é exibida. Quando o Class Browser é aberto, esta propriedade é definida como False (.F.). Se você deseja verificar erros, certifique-se de que esta propriedade esteja definida como False.
**lExpanded**
Somente para uso interno.
**nFileCount**
Somente referência. Retorna o número de arquivos de biblioteca de classes (.vcx) ou formulário (.scx) atualmente abertos no Class Browser. O valor padrão é 0.
**lFileMode**
Somente referência. Retorna o tipo do item selecionado na lista de classes. Se True (.T.), um arquivo está selecionado; se False (.F.), uma classe está selecionada.
**cFileName**
Somente referência. Retorna o caminho completo do arquivo associado à classe selecionada na lista de classes.
**tcFileName**
Somente referência. Retorna o valor ou referência do segundo parâmetro passado a BROWSER.APP. Por exemplo, se você abrir o Class Browser digitando o seguinte código, esta propriedade retorna "Wizstyle.vcx." DO (_BROWSER) WITH "wizstyle.vcx","baseform"
**aFiles**
Somente referência. Uma matriz de arquivos de biblioteca de classes (.vcx), formulário (.scx), aplicativo (.exe), biblioteca de objetos (.olb) e biblioteca de tipos (.tlb) atualmente abertos no Class Browser.
**cFilter**
Somente referência. Retorna a configuração atual do comando SET FILTER da tabela de metadados aberta para a classe selecionada na lista de classes.
**lFormAddObject**
Somente para uso interno.
**cGetFileExt**
Determina as extensões padrão do método GETFILE( ) do Class Browser. O valor padrão é "VCX;SCX;PJX;EXE;OLB;TLB."
**lHiddenFilter**
Se True (.T.), membros ocultos são exibidos na lista Members. O padrão é False (.F.).
**lIgnoreErrors**
Somente para uso interno.
**lInitialized**
Somente referência. Retorna o estado de inicialização do Class Browser. Se True (.T.), o Class Browser está inicializado; se False (.F.), o Class Browser não está inicializado.
**aInstances**
Somente referência. Uma matriz de instâncias associadas à classe selecionada na lista de classes. A funcionalidade é idêntica à da função AINSTANCE( ).
**nInstances**
Somente referência. Retorna o número total de instâncias associadas à classe selecionada na lista de classes usando AINSTANCE( ). O valor padrão é 0.
**cLastFindText**
Somente para uso interno.
**nLastHeight**
A altura inicial de um formulário antes de ocorrer um evento Resize. O valor padrão é (THIS.Height).
**nLastRecNo**
Somente para uso interno. O valor inicial é 1.
**cLastSetComp**
A configuração do comando SET COMPATIBLE quando o Class Browser foi carregado.
**cLastSetESC**
A configuração do comando SET ESCAPE quando o Class Browser foi carregado.
**cLastSetUDFParms**
A configuração do comando SET UDFPARMS quando o Class Browser foi carregado.
**cLastValue**
Somente para uso interno.
**nLastWidth**
Retorna a largura inicial de um formulário antes de ocorrer um evento Resize. O valor padrão é (THIS.Width).
**tlListBox**
Se um valor True (.T.) é passado ao Class Browser neste argumento, classes e membros são exibidos em list boxes em vez de controles tree view.
**lModalDialog**
Determina se a lista de classes é atualizada quando o Class Browser recupera o foco após ativar uma caixa de diálogo modal. Se True (.T.), a lista não é atualizada; se False (.F.), a lista é atualizada. O valor padrão é True (.T.).
**nMouseButton**
Somente para uso interno. Retorna qual botão do mouse foi pressionado.
**lNoDefault**
Retorna o status que indica como o comportamento padrão é tratado ao retornar de um add-in. Se True (.T.), o comportamento padrão é ignorado.
**lOutlineOCX**
Somente referência. Se True (.T.), classes e membros são exibidos em controles tree view. Você pode precisar dessa informação em um programa add-in.
**cParentClass**
Somente referência. Retorna o nome da classe pai da classe selecionada na lista de classes.
**lParentClassBrowser**
Se True (.T.), a barra de ferramentas Edit ParentClass Method é exibida. O padrão é True. Você pode clicar neste botão para visualizar ou editar imediatamente o método da classe pai no editor
**cParentClassBrowserCaption**
O caption da barra de ferramentas ParentClass Browser. O valor padrão é SPACE(10) + "ParentClass Browser"
**cParentClassSymbol**
Determina o símbolo exibido ao lado de uma classe para indicar que ela é uma subclasse de uma classe que não é exibida na lista Classes.
**nPixelOffset**
Somente para uso interno. Determina o número de pixels para cascatear várias instâncias do Class Browser. O valor padrão é 22.
**cPlatform**
Somente referência. Retorna o nome da plataforma atual.
**cProgramName**
Somente referência. Retorna o caminho completo do arquivo BROWSER.APP em execução.
**lProtectedFilter**
Se True (.T.), membros protected são exibidos na lista Members. O padrão é False (.F.).
**lReadOnly**
Somente referência. Retorna o status somente leitura do arquivo associado à classe selecionada na lista de classes.
**nRecCount**
Somente referência. Retorna o número total de registros nos arquivos de biblioteca de classes (.vcx) e formulário (.scx) abertos. O valor padrão é 0.
**lRefreshMode**
Somente para uso interno.
**lRelease**
Somente para uso interno. Especifica que o Class Browser é liberado automaticamente.
**lResizeMode**
Somente para uso interno. Retorna o status do modo de redimensionamento do Class Browser.
**lSCXMode**
Somente referência. Retorna o status do tipo de arquivo da classe selecionada na lista de classes. Se True (.T.), o arquivo é um formulário (.scx); se False (.F.), o arquivo é uma biblioteca de classes (.vcx).
**nShift**
Somente para uso interno. Estado da tecla SHIFT quando um botão do mouse é pressionado.
**oSource**
Somente referência. Retorna a referência de um objeto solto em um formulário a partir do Class Browser. Após a conclusão do método DragDrop, oSource é definido como null (.NULL.).
**cStartName**
Somente referência. Retorna a propriedade Name do Class Browser quando o Class Browser foi carregado, mas antes do nome ser incrementado. Por exemplo, o valor padrão é ClassBrowser e, para cada instância aberta, o nome é incrementado: ClassBrowser1, ClassBrowser2.
**nStrLen**
Somente para uso interno. O valor padrão é 0.
**cTimeStamp**
Somente referência. Retorna o valor do campo timestamp da classe selecionada na lista de classes.
**lVCXSCXMode**
Se True (.T.), a classe ou arquivo selecionado é um .vcx ou .scx, ou está em um .vcx ou .scx.
**tnWindowState**
Somente para uso interno. Se a janela do Class Browser está minimizada (1), maximizada (2) ou normal (0).

# Valores iniciais das propriedades do Class Browser

Quando uma instância do Class Browser é aberta, as propriedades são definidas com os valores padrão mostrados na tabela a seguir.

| Propriedade do Class Browser | Configuração inicial |
| --- | --- |
| cAddIn | "" |
| cAddInMethod | "" |
| cAlias | "" |
| Caption | "Class Browser" |
| cBaseClass | "" |
| cBrowserTable | "" |
| cClass | "" |
| cClassLibrary | "" |
| cClassTimeStamp | "" |
| cClasstype | "" |
| cDragIcon | "" |
| cFileName | "" |
| cFilter | "" |
| cGetFileExt | vcx;scx;pjx;exe;olb;tlb |
| cLastGetFileExt | "" |
| cLastSetComp | "" |
| cLastSetEsc | "" |
| cLastSetudfParms | "" |
| cLastValue | "" |
| cParentClass | "" |
| cParentClassSymbol | (IIF(VERSION(3)=="00",CHR(171),"<")) |
| cPlatform | "" |
| cProgramName | "" |
| cStartName | "" |
| DataSession | 2 |
| FontBold | .F. |
| FontName | "MS Sans Serif" |
| FontSize | 8 |
| Height | 360 |
| HelpContextID | 95825501 |
| Icon | Browser.ico |
| lAutoExpand | .T. |
| lDescriptions | .T. |
| lDisplayHierarchyError | .T. |
| Left | 0 |
| lParentClassBrowser | .T. |
| MinHeight | (175) |
| MinWidth | (250) |
| Name | "classbrowser" |
| nAtPos | 0 |
| nClassCount | 0 |
| nClassListIndex | -1 |
| nDisplayMode | 1 |
| nFileCount | 0 |
| nInstances | 0 |
| nLastHeight | (this.Height) |
| nLastRecNo | 1 |
| nLastWidth | (this.Width) |
| nMouseButton | 0 |
| nPixelOffset | 22 |
| nRecCount | 0 |
| nShift | 0 |
| nStrLen | 0 |
| nTimeStamp | 0 |
| oParentClassBrowser | .NULL. |
| oSource | .NULL. |
| ShowTips | .T. |
| Top | -1 |
| Width | 462 |

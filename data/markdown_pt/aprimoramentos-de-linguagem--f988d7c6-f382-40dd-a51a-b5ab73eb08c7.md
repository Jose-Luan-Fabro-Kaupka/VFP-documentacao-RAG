# Aprimoramentos de linguagem

Na versão atual do Visual FoxPro, você encontrará funcionalidade aprimorada por meio de comandos e funções novos e aprimorados. Expanda e recolha este tópico para ver informações sobre adições e melhorias diversas de linguagem.

# Aprimoramentos de classes

O Visual FoxPro contém aprimoramentos significativos de linguagem para classes, formulários, controles e recursos relacionados à orientação a objetos. Para obter mais informações, consulte Class Enhancements.

# Aprimoramentos de dados e XML

O Visual FoxPro contém aprimoramentos significativos de linguagem para recursos de dados, SQL e XML. Para obter mais informações, consulte SQL Language Improvements e Data and XML Feature Enhancements.

# Aprimoramentos do IDE

O Visual FoxPro contém vários aprimoramentos de linguagem para recursos relacionados ao IDE (Interactive Development Environment). Para obter mais informações, consulte Interactive Development Environment (IDE) Enhancements e Enhancements to Visual FoxPro Designers.

# Aprimoramentos de impressão e relatórios

O Visual FoxPro contém vários aprimoramentos de linguagem para suportar a nova funcionalidade de relatórios:
 - REPORT FORM Command Exibe ou imprime um relatório especificado por um arquivo de definições de relatório. Este comando foi aprimorado para suportar objetos Report Listener.
- SET REPORTBEHAVIOR Command Controla o uso de aplicativos Report Preview e Report Output com o Visual FoxPro Report System.
- SYS(2024) - Detect Report Cancellation Determina se o usuário cancelou um relatório em execução.

Além disso, há melhorias nos seguintes elementos de linguagem relacionados à impressão:
 - SYS(1037) - Page Setup Dialog Box Exibe a caixa de diálogo Page Setup padrão do Visual FoxPro ou de relatório, ou define as configurações da impressora para a impressora padrão no Visual FoxPro ou para o ambiente da impressora de relatório. Nesta versão, um novo parâmetro nValue está disponível.
- APRINTERS( ) Function Retorna um array de cinco colunas com o nome da impressora, porta conectada, driver, comentário e localização. As três últimas colunas estão disponíveis se o novo parâmetro opcional for passado.
- GETFONT( ) Function Contém uma configuração adicional para exibir apenas as fontes disponíveis na impressora padrão atual e valores esclarecidos para o script de idioma.

A nova funcionalidade de relatórios é descrita com mais detalhes em tópicos separados de relatórios. Para obter mais informações, consulte Guide to Reporting Improvements.

# Especificando arrays com mais de 65K elementos

Agora você pode especificar arrays contendo mais de 65.000 elementos, por exemplo, ao usar o comando DIMENSION. Arrays normais e arrays de membros têm um novo limite de 2GB. Arrays contendo objetos membros mantêm um limite de 65.000 elementos.

> **Observação:** O tamanho dos arrays também pode ser limitado pela memória disponível, o que afeta o desempenho, especialmente para arrays muito grandes. Certifique-se de que seu computador tenha memória suficiente para acomodar os limites superiores dos seus arrays.

O Library Construction Kit, que contém os arquivos Pro_Ext.h, WinAPIMS.lib e OcxAPI.lib, ainda tem um limite de 65.000 elementos. Para obter mais informações sobre esses arquivos, consulte Accessing the Visual FoxPro API, How to: Add Visual FoxPro API Calls e How to: Build and Debug Libraries and ActiveX Controls. O comando SAVE TO não suporta salvar arrays maiores que 65.000 elementos.

Para obter mais informações, consulte Visual FoxPro System Capacities e DIMENSION Command.

# Configuração STACKSIZE aumenta níveis de aninhamento para 64k

Para operações como o comando DO, você pode alterar o número padrão de níveis de aninhamento de 128 níveis para 32 e até 64.000 níveis de aninhamento incluindo a nova configuração STACKSIZE em um arquivo de configuração do Visual FoxPro.

> **Observação:** Você pode alterar o nível de aninhamento apenas durante a inicialização do Visual FoxPro.

Para obter mais informações, consulte Special Terms for Configuration Files e Visual FoxPro System Capacities.

# Tamanho de arquivo de programa e procedimento é irrestrito

Em versões anteriores do Visual FoxPro, o tamanho de um procedimento ou programa não podia exceder 65K. O Visual FoxPro agora remove essa restrição para programas e procedimentos. Para obter mais informações, consulte Visual FoxPro System Capacities.

# Configuração PROGCACHE do arquivo de configuração

Em versões anteriores do Visual FoxPro, você não podia especificar o tamanho do cache de programa ou a quantidade de memória reservada para executar programas. Esta configuração do arquivo de configuração permite controlar isso. É especialmente útil para cenários MTDLL. Para obter mais informações, consulte Special Terms for Configuration Files.

# Função ICASE( )

A nova função ICASE( ) permite avaliar uma lista de condições e retornar resultados dependendo do resultado da avaliação dessas condições. Para obter mais informações, consulte ICASE( ) Function.

# TTOC( ) converte expressões DateTime para formato XML DateTime

Você pode converter uma expressão DateTime em uma cadeia de caracteres no formato XML DateTime passando um novo valor opcional de 3 para a função TTOC( ). Para obter mais informações, consulte TTOC( ) Function.

# Comando SET COVERAGE disponível em tempo de execução

O comando SET COVERAGE agora está disponível em tempo de execução para que você possa depurar erros que ocorrem em tempo de execução, mas não em tempo de design. Para obter mais informações, consulte SET COVERAGE Command.

# Comando CLEAR ERROR

A nova cláusula ERROR do comando CLEAR permite redefinir as estruturas de erro como se nenhum erro tivesse ocorrido. Isso afeta as seguintes funções:
 - A função AERROR( ) retornará 0.
- A função ERROR( ) retornará 0.
- A saída de MESSAGE( ), MESSAGE(1) e SYS(2018) retornará uma cadeia de caracteres em branco.

O comando CLEAR não deve ser usado com a cláusula ERROR dentro de uma estrutura TRY...CATCH...FINALLY. Para obter mais informações, consulte CLEAR Commands.

# Gravar configurações da caixa de diálogo Options no registro usando SYS(3056)

A função SYS(3056) agora pode ser usada para gravar as configurações da caixa de diálogo Options no registro.

`SYS(3056 [, nValue ])`

A tabela a seguir lista os valores para nValue.

| nValue | Descrição |
| --- | --- |
| 1 | Atualizar apenas das configurações do registro, com exceção dos comandos SET e localizações de arquivo. |
| 2 | Gravar configurações no registro. |

Para obter mais informações, consulte SYS(3056) - Read Registry Settings.

# Comando FOR EACH ... ENDFOR preserva tipos de objeto

O Visual FoxPro agora inclui a palavra-chave FOXOBJECT para o comando FOR EACH ... ENDFOR para suportar a preservação de tipos de objeto nativos do Visual FoxPro.

`FOR EACH objectVar [AS Type [OF ClassLibrary ]] IN Group FOXOBJECT`

`Commands`

`[EXIT]`

`[LOOP]`

`ENDFOR | NEXT [Var]`

A palavra-chave FOXOBJECT especifica que o parâmetro objectVar criado será um objeto Visual FoxPro. A palavra-chave FOXOBJECT se aplica apenas a coleções baseadas em uma classe Collection nativa do Visual FoxPro. Coleções baseadas em COM não suportarão a palavra-chave FOXOBJECT.

Para obter mais informações, consulte FOR EACH ... ENDFOR Command.

# Aprimoramentos do comando SET PATH

O comando SET PATH agora suporta a palavra-chave ADDITIVE. A palavra-chave ADDITIVE acrescenta o caminho especificado ao final da lista SET PATH atual. Se o caminho já existir na lista SET PATH, o Visual FoxPro não o adiciona nem altera a ordem da lista. Caminhos especificados com a palavra-chave ADDITIVE devem ser cadeias de caracteres entre aspas ou expressões válidas.

Além disso, o comprimento da lista SET PATH foi aumentado para 4095 caracteres.

Para obter mais informações, consulte SET PATH Command.

# Funções Trim controlam quais caracteres são removidos

Agora é possível especificar quais caracteres são removidos de uma expressão ao usar as funções TRIM( ), LTRIM( ), RTRIM( ) e ALLTRIM( ).

`TRIM(cExpression[, nFlags] [, cParseChar [, cParseChar2 [, ...]]])`

`LTRIM(cExpression[, nFlags] [, cParseChar [, cParseChar2 [, ...]]])`

`RTRIM(cExpression[, nFlags] [, cParseChar [, cParseChar2 [, ...]]])`

`ALLTRIM(cExpression[, nFlags] [, cParseChar [, cParseChar2 [, ...]]])`

Você pode especificar que a remoção não diferencia maiúsculas de minúsculas usando o valor nFlag de 0 bit e 1.

O parâmetro cParseChar especifica uma ou mais cadeias de caracteres a serem removidas de cExpression. Um máximo de 23 cadeias de caracteres pode ser especificado em cParseChar.

Por padrão, se cParseChar não for especificado, espaços à esquerda e à direita são removidos de cadeias de caracteres ou bytes 0 são removidos para tipos de dados Varbinary.

Os parâmetros cParseChar são aplicados na ordem em que são inseridos. Quando uma correspondência é encontrada, cExpression é truncado e o processo se repete a partir do primeiro parâmetro cParseChar.

Para obter mais informações, consulte os tópicos TRIM( ) Function, LTRIM( ) Function, RTRIM( ) Function e ALLTRIM( ) Function.

# ALINES( ) oferece opções de análise mais flexíveis

A função ALINES( ) foi aprimorada para fornecer várias opções adicionais, como análise sem diferenciação de maiúsculas e minúsculas e tratamento melhorado de elementos de array vazios. Essas opções estão disponíveis usando o novo parâmetro nFlags que substitui o antigo terceiro parâmetro lTrim. Para obter mais informações, consulte ALINES( ) Function.

# Melhorias na instrução TEXT…ENDTEXT

Você pode usar o comando TEXT…ENDTEXT para eliminar quebras de linha usando a nova configuração PRETEXT. Um novo parâmetro FLAGS controla configurações adicionais de saída. Para obter mais informações, consulte TEXT ... ENDTEXT Command.

# Incluir delimitadores nos resultados de STREXTRACT( )

A função STREXTRACT( ) tem uma nova configuração nFlags que permite incluir os delimitadores especificados com a expressão retornada. Para obter mais informações, consulte STREXTRACT( ) Function.

# STRCONV( ) aprimorado para permitir Code Page e FontCharSet

Para certas configurações de conversão, você pode especificar uma configuração opcional de Code Page ou Fontcharset para uso na conversão. Para obter mais informações, consulte STRCONV( ) Function.

# TYPE( ) determina se uma expressão é um array

A função TYPE( ) aceita o parâmetro 1 para avaliar uma expressão e determinar se é um array.

`Type(cExpression, 1)`

Os seguintes valores de caractere são retornados se o parâmetro 1 for especificado.

| Valor de retorno | Descrição |
| --- | --- |
| A | cExpression é um array. |
| U | cExpression não é um array. |
| C | cExpression é uma coleção. |

cExpression deve ser passado como uma cadeia de caracteres.

Para obter mais informações, consulte TYPE( ) Function.

# BINTOC( ) e CTOBIN( ) têm capacidades adicionais de conversão

As funções BINTOC( ) e CTOBIN( ) têm parâmetros atualizados ou novos que fornecem mais controle sobre a saída dessas funções. Além disso, esses aprimoramentos oferecem algumas melhorias para trabalhar com rotinas Win32 API. Para obter mais informações, consulte BINTOC( ) Function e CTOBIN( ) Function.

# MROW( ) e MCOL( ) podem detectar a posição do ponteiro do mouse

As funções MROW( ) e MCOL( ) agora têm um parâmetro zero (0) para detectar a posição do ponteiro do mouse com base no formulário atualmente ativo em vez do formulário retornado pela função WOUTPUT( ). Embora normalmente façam referência ao mesmo formulário, se a propriedade AllowOutput do formulário estiver definida como False (.F.), WOUTPUT( ) não retorna o formulário ativo atual. A incompatibilidade de referências pode levar a resultados inesperados. Usando o parâmetro zero (0), você pode evitar posicionar incorretamente itens, como menus de atalho, pois o formulário atualmente ativo é sempre usado.

Para obter mais informações, consulte MROW( ) Function e MCOL( ) Function.

# INPUTBOX( ) retorna uma operação de cancelamento

A função INPUTBOX( ) contém um parâmetro adicional que permite determinar se o usuário cancelou a caixa de diálogo. Para obter mais informações, consulte INPUTBOX( ) Function.

# AGETCLASS( ) suportado para aplicativos em tempo de execução

A função AGETCLASS( ) agora é suportada para aplicativos em tempo de execução. Para obter mais informações, consulte AGETCLASS( ) Function.

# SYS(2019) amplia o tratamento de arquivos de configuração

Você pode usar SYS(2019) para obter o nome e a localização de arquivos de configuração internos e externos. Para obter mais informações, consulte SYS(2019) - Configuration File Name and Location.

# SYS(2910) controla a contagem de exibição de lista

Você pode controlar o número de itens que aparecem em uma lista suspensa, como a usada pela propriedade AutoComplete. Esta é a configuração disponível na guia View, Options Dialog Box da caixa de diálogo Options (Visual FoxPro).

Para obter mais informações, consulte SYS(2910) - List Display Count.

# SYS(3008) desativa dica de hiperlink

O Visual FoxPro exibirá uma dica como "CTRL+Click to follow the link" quando você passar o mouse sobre um hiperlink no editor. Se desejar que essa dica não apareça, você pode usar SYS(3008) para desativá-la. Esta função também é útil para aplicativos internacionais nos quais você não deseja exibir o texto em inglês para essa dica. Para obter mais informações, consulte SYS(3008) - Hyperlink Tooltips.

# SYS(3065) cache interno de programa

Você pode obter o cache interno de programa (configuração PROGCACHE do arquivo de configuração). Para obter mais informações, consulte SYS(3065) - Internal Program Cache.

# SYS(3101) tradução de code page COM

Agora você pode especificar um code page para usar na tradução de dados de caracteres envolvendo interoperabilidade COM. Para obter mais informações, consulte SYS(3101) - COM Code Page Translation.

# Suporte bidirecional para dicas e popups

Para aplicativos internacionais que exibem texto da direita para a esquerda, você pode usar os seguintes novos aprimoramentos para controlar a justificação do texto:
 - SYS(3009) - justifica à direita o texto em ToolTips.
- DEFINE POPUP…RTLJUSTIFY - justifica à direita os itens em um popup, como um menu de atalho.
- SET SYSMENU TO RTLJUSTIFY - justifica à direita um sistema de menus inteiro.

A função SYS(3009) é uma configuração global. Para obter mais informações, consulte SYS(3009) - Bidirectional Text Justification for ToolTips, DEFINE POPUP Command e SET SYSMENU Command.

# Suporte aprimorado a script de fonte

O Visual FoxPro 9.0 contém vários aprimoramentos que ampliam a capacidade de especificar um Font Language Script (ou FontCharSet) junto com as configurações de fonte existentes:
 - SYS(3007) - especifica um FontCharSet para ToolTips. Esta é uma configuração global.
- Cláusula FONT - a tabela a seguir lista comandos que suportam uma cláusula FONT opcional que permite a especificação de um FontCharSet no seguinte formato: FONT cFontName [, nFontSize [, nFontCharSet]] Command DEFINE MENU DEFINE POPUP DEFINE BAR DEFINE PAD DEFINE WINDOW MODIFY WINDOW BROWSE/EDIT/CHANGE ?/??
- Browse - a Font Dialog Box que você pode invocar selecionando o item de menu Font no menu Table com uma Browse Window ativa agora permite a seleção de um script de idioma de fonte. Você pode especificar um script de fonte padrão global na guia IDE, Options Dialog Box na caixa de diálogo Options (Visual FoxPro). Para fazer isso, você deve primeiro marcar a caixa de seleção Use font script.
- Editors - a Font Dialog Box que você pode invocar com uma janela de editor ativa selecionando o item de menu Font no menu Format ou no menu de atalho Edit Properties Dialog Box agora permite a seleção de um script de idioma de fonte. Você pode especificar um script de fonte padrão global na guia IDE, Options Dialog Box na caixa de diálogo Options (Visual FoxPro). Para fazer isso, você deve primeiro marcar a caixa de seleção Use font script.

Para obter mais informações, consulte SYS(3007) - ToolTipText Property Font Language Script, IDE Tab, Options Dialog Box e FontCharSet Property.

# Controle de tempo limite de ToolTip

Você pode especificar por quanto tempo um ToolTip é exibido se o ponteiro do mouse permanecer parado. Para obter mais informações, consulte _TOOLTIPTIMEOUT System Variable.

# Recursos do Tablet PC

Os seguintes recursos estão disponíveis para auxiliar aplicativos projetados para ser executados em um computador Tablet PC.
 - ISPEN( ) - determina se o último evento de mouse do aplicativo Visual FoxPro em um Tablet PC foi um toque com a caneta.
- _SCREEN.DisplayOrientation - esta propriedade de leitura/gravação especifica a orientação de exibição da tela para um Tablet PC. O valor retornado é a orientação atual.
- _TOOLTIPTIMEOUT - especifica por quanto tempo um ToolTip é exibido se o ponteiro do mouse permanecer parado.

Para obter mais informações, consulte ISPEN( ) Function, DisplayOrientation Property e _TOOLTIPTIMEOUT System Variable.

# Tratamento de eventos de mensagens do Windows

O Visual FoxPro permite interceptar e tratar mensagens de janela do sistema operacional Microsoft® Windows® usando funções BINDEVENT existentes. Alguns exemplos de eventos comuns que você pode desejar interceptar incluem:
 - Uma mensagem de broadcast de energia usada para interceptar atividades de standby ou desligamento.
- Eventos de inserção e remoção de mídia, como a inserção de um CD em uma unidade.
- A inserção e/ou remoção de um disco rígido Plug and Play (por exemplo, unidade USB).
- Interceptação de consultas de protetor de tela para impedir a ativação do protetor de tela.
- Alterações de fonte em nível de sistema operacional e alterações de tema do Windows XP.
- Novas conexões/compartilhamentos de rede adicionados ou removidos do sistema.
- Alternância entre aplicativos.

Você pode usar as funções BINDEVENT do Visual FoxPro para registrar (e cancelar o registro de) manipuladores de eventos usados para interceptar mensagens (ou seja, mensagens de janela da API Win32 que são processadas pela função Win32 WindowProc). Consulte o MSDN para mais detalhes.

A nova sintaxe BINDEVENT( ) requer o hWnd (inteiro) da janela que recebe a mensagem que você deseja interceptar e a mensagem específica (inteiro). Por exemplo, eventos de gerenciamento de energia como standby e desligamento usam a mensagem Win32 WM_POWERBROADCAST (valor de 536).

BINDEVENT(hWnd, nMessage, oEventHandler, cDelegate)

O exemplo a seguir ilustra a detecção de uma alteração de tema do Windows XP:

```foxpro
#DEFINE WM_THEMECHANGED    0x031A
#DEFINE GWL_WNDPROC    (-4)
PUBLIC oHandler
oHandler=CREATEOBJECT("AppState")
BINDEVENT(_SCREEN.hWnd, WM_THEMECHANGED, oHandler, "HandleEvent")
MESSAGEBOX("Test by changing Themes.")
DEFINE CLASS AppState AS Custom
nOldProc=0
PROCEDURE Destroy
    UNBINDEVENT(_SCREEN.hWnd, WM_THEMECHANGED)
ENDPROC
PROCEDURE Init
    DECLARE integer GetWindowLong IN WIN32API ;
        integer hWnd, ;
        integer nIndex
    DECLARE integer CallWindowProc IN WIN32API ;
        integer lpPrevWndFunc, ;
        integer hWnd,integer Msg,;
        integer wParam,;
        integer lParam
    THIS.nOldProc=GetWindowLong(_VFP.HWnd,GWL_WNDPROC)
ENDPROC
PROCEDURE HandleEvent(hWnd as Integer, Msg as Integer, ;
    wParam as Integer, lParam as Integer)
    lResult=0
    IF msg=WM_THEMECHANGED
        MESSAGEBOX("Theme changed...")
    ENDIF
    lResult=CallWindowProc(this.nOldProc,hWnd,msg,wParam,lParam)
    RETURN lResult
ENDPROC
ENDDEFINE
```

As seguintes funções SYS( ) também estão disponíveis para auxiliar no tratamento desses eventos:
 - SYS(2325) - retorna o hWnd de uma janela cliente a partir do WHANDLE da janela pai.
- SYS(2326) - retorna um WHANDLE do Visual FoxPro a partir do hWnd de uma janela.
- SYS(2327) - retorna o hWnd de uma janela a partir do WHANDLE de uma janela do Visual FoxPro.

Para obter mais informações, consulte BINDEVENT( ) Function, UNBINDEVENTS( ) Function e AEVENTS( ) Function. Consulte também SYS(2325) - WCLIENTWINDOW from Visual FoxPro WHANDLE, SYS(2326) - WHANDLE from a Window's hWnd e SYS(2327) - Window's hWnd from Visual FoxPro WHANDLE para tópicos relacionados. Consulte o MSDN como fonte de referência para detalhes sobre mensagens de janela específicas.

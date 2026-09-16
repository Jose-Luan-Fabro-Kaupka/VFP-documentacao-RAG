# Como: especificar e distribuir ReportBuilder.App

Ao escrever e distribuir aplicativos do Visual FoxPro, você pode optar por dar aos seus usuários a capacidade de personalizar alguns ou todos os layouts de relatório do seu aplicativo. O construtor de relatórios e os recursos de proteção de relatórios no Visual FoxPro 9.0 tornam isso uma solução mais segura e controlada para seu aplicativo.

Neste tópico, você aprenderá a redistribuir o aplicativo Report Builder padrão de duas maneiras:
 - Distribuir o Report Builder como um arquivo separado junto com seu próprio aplicativo e garantir que o Visual FoxPro seja direcionado para o local do arquivo reportbuilder.app em tempo de execução.
- Compilar os arquivos de origem do Report Builder diretamente em seu próprio aplicativo.

# Redistribuindo ReportBuilder.App com seu aplicativo

Por padrão, se ReportBuilder.App existir no mesmo diretório que os arquivos de tempo de execução do Visual FoxPro, então _REPORTBUILDER conterá o caminho completo e o nome do arquivo. Uma solução é garantir que o programa de instalação usado para distribuir seu aplicativo coloque ReportBuilder.App no mesmo diretório que os arquivos de tempo de execução. Alternativamente, você pode distribuir ReportBuilder.App no mesmo diretório que seu aplicativo, desde que defina explicitamente _REPORTBUILDER para apontar para sua cópia do arquivo ReportBuilder.App.

### Para garantir que o ambiente de tempo de execução do Visual FoxPro encontre sua cópia distribuída de ReportBuilder.App
- No programa principal do seu aplicativo, use código semelhante ao seguinte: * Obtenha o diretório inicial do aplicativo: cHomeDir = CURDIR() && use o método que preferir * Defina a variável de sistema para usar o caminho completo: _REPORTBUILDER = m.cHomeDir+"ReportBuilder.App" :

Você também pode usar uma linha em CONFIG.FPW:

`_REPORTBUILDER=<path>\ReportBuilder.App`

### Considerações

Se você distribuir ReportBuilder.App dessa maneira, não poderá especificar uma tabela de registro de manipuladores de eventos de relatório alternativa integrada ao arquivo APP do seu aplicativo. Isso ocorre porque o código em execução dentro de ReportBuilder.App não pode usar nenhum arquivo integrado em outros aplicativos (arquivos .app ou .exe).

# Integrando a origem do Report Builder em seu projeto

Em vez de distribuir o aplicativo compilado, você pode optar por incorporar o código-fonte do construtor de relatórios diretamente no projeto do seu aplicativo.

### Para integrar a origem do construtor de relatórios em seu aplicativo
- Descompacte o arquivo xsource.zip encontrado na pasta Tools\xsource\ no diretório inicial do Visual FoxPro.
- No programa principal do seu aplicativo, use código semelhante ao seguinte: * Garanta que a origem do construtor de relatórios seja incluída no projeto: EXTERNAL PROCEDURE frxbuilder.prg * Defina a variável de sistema para usar a versão de origem local: _REPORTBUILDER = "frxbuilder.prg" :
- Recompile seu projeto. O código-fonte do construtor de relatórios e a tabela de pesquisa de manipuladores de eventos serão adicionados ao seu projeto e compilados em seu aplicativo.

Em vez de usar a versão original da tabela de pesquisa de manipuladores de eventos, frxbuilder.dbf, você pode desejar personalizá-la. Tenha cuidado — seu projeto está referenciando sua cópia mestre da origem do construtor de relatórios. Você pode preferir remover o arquivo frxbuilder.dbf do seu projeto e substituí-lo por uma cópia personalizada local na árvore de origem do seu aplicativo.

Você não precisa manter o nome padrão para esta tabela. Se desejar, pode informar ao construtor de relatórios para usar uma tabela com nome alternativo:

### Para especificar uma tabela de registro de manipuladores de eventos alternativa
- Na parte de configuração do programa principal do seu aplicativo, use código semelhante ao seguinte: do frxBuilder with 3, "mylookup.dbf"

### Arquivos de origem compartilhados

ReportBuilder.App e ReportPreview.App têm os seguintes arquivos de origem em comum:
 - frxControls.vcx
- frxCommon.prg
- grabber.gif
- wwrite.ico
- foxpro_reporting.h

O Project Manager cria apenas uma referência a cada um desses arquivos no projeto do seu aplicativo, dependendo da ordem das instruções EXTERNAL no programa principal.

# Considerações para a Ajuda do Report Builder

As caixas de diálogo do Report Builder Application são fornecidas com informações de ajuda no arquivo de Ajuda do Visual FoxPro, associadas à propriedade HelpContextID (Visual FoxPro) de vários elementos da interface. O arquivo de Ajuda do Visual FoxPro não pode ser redistribuído com seu aplicativo. Para obter informações, consulte Recursos e arquivos distribuíveis e restritos do Visual FoxPro.

Ao distribuir o Report Builder Application ou seus componentes, e se você fornecer arquivos de ajuda para seus aplicativos, pode escolher uma das seguintes estratégias:
 - Criar tópicos de ajuda usando os IDs de contexto apropriados em seu arquivo de ajuda, correspondendo aos IDs de contexto que o Report Builder usa. Verifique as constantes de ID de ajuda definidas em FRXBUILDER.H para os IDs de contexto corretos a usar.
- Não criar tópicos de ajuda com esses IDs de contexto. Quando o usuário pressionar a tecla F1 ou usar um botão Help, seu arquivo de ajuda aparecerá com seu tópico de nível superior exibido.
- Alterar as constantes definidas em FRXBUILDER.H na origem do Report Builder para usar um ou mais IDs de contexto diferentes e criar um tópico ou vários tópicos em seu arquivo de ajuda para corresponder aos IDs de contexto que você usar. Você precisará recompilar ReportBuilder.App a partir do código-fonte para que essa alteração tenha efeito.

### Para especificar valores diferentes de ID de contexto de ajuda para componentes do Report Builder Application
- Modifique as constantes de ID de contexto de ajuda definidas em FRXBUILDER.H e salve suas alterações.
- Recompile o Report Builder Application ou recompile seu aplicativo se estiver compilando os componentes do Report Builder em seu aplicativo.

Ao distribuir o Report Builder Application ou seus componentes, e se você não fornecer um arquivo de ajuda para seu aplicativo, você tem as seguintes opções:
 - Distribuir ReportBuilder.app ou seus componentes como estão. Quando determinam que SET("HELP") = "OFF" , os componentes do ReportBuilder desabilitam o botão Help.
- Ajustar uma constante associada no arquivo frxbuilder.h para remover o botão Help.

### Para remover o botão Help dos elementos da interface do Report Builder Application
- Localize o arquivo frxbuilder.h na origem do Report Builder Application.
- Altere o valor da constante SHOW_HELP_BUTTON_ON_HANDLER_FORMS para False ( .F. ).
- Recompile o Report Builder Application ou recompile seu aplicativo se estiver compilando os componentes do Report Builder em seu aplicativo.

Para obter mais informações sobre o uso do sistema de ajuda do Visual FoxPro em aplicativos, consulte Comando SET TOPIC ID e Comando SET HELP.

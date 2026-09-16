# Passo a passo: criar um programa de instalação de aplicativo Visual FoxPro usando InstallShield

Quando você está pronto para distribuir um aplicativo, pode criar um programa de instalação para ajudar seus clientes a instalá-lo. Este passo a passo explica considerações que você deve fazer antes de distribuir o aplicativo e mostra como criar um projeto Setup, incluir arquivos e definir suas propriedades, e distribuir os arquivos do aplicativo a partir do Setup usando InstallShield Express Visual FoxPro Limited Edition.

Este passo a passo contém as seguintes seções:
 - Pré-requisitos
- Criando o programa de instalação usando InstallShield Express
- Distribuindo um aplicativo

Para obter mais informações sobre distribuição de aplicativos, consulte Distribuindo aplicativos.

# Pré-requisitos

O Visual FoxPro inclui a edição limitada do InstallShield Express versão 5.0, substituindo o Assistente de instalação encontrado em versões anteriores ao Visual FoxPro 7.0. Para aprender como instalar InstallShield Express Limited Edition no seu computador, consulte Como: instalar aplicativos adicionais.

> **Observação:** Você pode usar qualquer programa de criação de instalação que use a tecnologia Microsoft Windows Installer para criar um programa de instalação (.msi) ou módulos de mesclagem (.msm) compatíveis com Microsoft Windows Installer. Alguns cenários de distribuição exigem módulos de mesclagem além dos arquivos de runtime do Visual FoxPro. Para obter mais informações, consulte Cenários de distribuição do Visual FoxPro neste passo a passo.

As diretrizes do Logo do Windows 2000 exigem que programas de instalação sejam baseados na tecnologia Windows Installer. O Windows Installer faz parte dos esforços Windows 2000 e Zero Administration Windows para reduzir o custo geral de implantação, uso e gerenciamento de computadores desktop. Tanto a edição limitada quanto a completa do InstallShield Express usam Microsoft Installer, que oferece tecnologia abrangente e flexível de criação de Setup. Esta tecnologia permite que seus clientes instalem e configurem seu aplicativo com eficiência.

Este passo a passo não substitui a documentação do InstallShield Express, que você deve ler primeiro. É um suplemento para auxiliá-lo no uso do InstallShield Express para empacotar e distribuir aplicativos. Você também pode baixar os Componentes do Platform SDK para Desenvolvedores do Windows Installer no site de download da Microsoft em http://www.microsoft.com/msdownload/platformsdk/sdkupdate/.

Você deve considerar várias questões ao preparar um aplicativo para distribuição. Além de seguir o procedimento descrito no Processo de distribuição de aplicativos, você deve identificar a estrutura do seu aplicativo; decidir como entregar o aplicativo aos usuários e como organizar melhor seu programa de instalação. Quando você abordou todas essas questões, está pronto para distribuir seu aplicativo Visual FoxPro.

# Criando o programa de instalação usando InstallShield Express

Criar o projeto Setup é o primeiro passo na criação de um programa de instalação. O arquivo de projeto Setup (.ism) que você cria com InstallShield Express é baseado no arquivo de projeto do Windows Installer. Este arquivo armazena toda a lógica e informações necessárias para compilar um programa de instalação compatível com Windows Installer.

### Para criar um projeto Setup
- No menu Iniciar, aponte para Todos os programas . Aponte para InstallShield e clique em Express para abrir InstallShield Express.
- No menu Arquivo, clique em Novo para abrir a caixa de diálogo Novo projeto.
- Navegue até o local onde deseja salvar seu projeto, renomeie o nome de arquivo de projeto padrão na caixa Nome e local do projeto e clique em OK .
- Para criar seu programa de instalação em um idioma diferente do inglês, selecione um idioma alternativo na lista Idioma do projeto. Observação Após escolher um idioma, você não pode alterá-lo para o projeto.

### Definindo propriedades do projeto

Após criar um projeto Setup, você pode definir propriedades, como:
 - Nome do produto
- Versão do produto
- Ícones do produto
- Pasta de instalação padrão para todos os arquivos do aplicativo
- Nome e local de um arquivo Leiame

No mínimo, você deve especificar o nome do produto e uma pasta de instalação padrão para os arquivos do seu aplicativo. A propriedade INSTALLDIR no InstallShield Express especifica o local da pasta de instalação padrão, por exemplo, o diretório home do aplicativo. O local da pasta de instalação padrão especificada por INSTALLDIR é:

[ProgramFilesFolder]Nome da sua empresa\Nome do seu produto

> **Observação:** É recomendado que você altere Nome da sua empresa e Nome do seu produto para os nomes apropriados para seu aplicativo.

Você também pode especificar uma pasta diferente para seu aplicativo definindo INSTALLDIR para uma pasta com o nome do seu aplicativo conforme especificado por MyApp no exemplo a seguir:

[ProgramFilesFolder]\MyApp

Se você planeja instalar arquivos de dados ou banco de dados, também pode editar a propriedade DATABASEDIR para especificar a pasta de destino padrão para esses arquivos.

### Para especificar informações gerais para seu projeto Setup
- No nó Organizar sua instalação, clique em Informações gerais .
- Na lista de propriedades, clique duas vezes no campo de valor de uma propriedade para editar seu valor.
- Clique em outro lugar na lista de propriedades para ver suas alterações terem efeito.

### Dividindo seu produto em recursos

Da perspectiva do usuário do aplicativo e do InstallShield Express, um recurso é considerado um bloco de construção de um aplicativo. Recursos permitem que os usuários instalem partes de um aplicativo. Por exemplo, durante a instalação do Visual FoxPro, você pode especificar se deseja instalar os Exemplos do Visual FoxPro e as Ferramentas do Visual FoxPro como recursos.

> **Observação:** Dividir seu produto em recursos não é obrigatório ao criar um programa de instalação, embora possa ser útil para os usuários.

A configuração padrão para instalar recursos é Sempre instalar, que lista os componentes que instalam com todos os Tipos de instalação.

### Para criar um recurso
- No nó Organizar sua instalação, clique em Recursos .
- Para adicionar um novo recurso, clique com o botão direito no nó Recursos na visualização em árvore no painel central e clique em Novo recurso Ins .
- Digite um nome para o novo recurso e pressione ENTER.

Quando você identificou os recursos do seu produto, pode definir propriedades de recurso, como descrição do recurso, como o recurso é anunciado e se o recurso é obrigatório. Embora os recursos anunciados pareçam instalados para o usuário, não são instalados durante a instalação. O Windows Installer instala o recurso anunciado quando o usuário tenta usar o recurso pela primeira vez.

### Para definir uma propriedade de recurso
- Selecione o recurso para o qual deseja modificar propriedades.
- Na lista de propriedades, clique duas vezes no campo de valor da propriedade para editar seu valor. Para exibir mais opções, clique no botão de reticências (...) ou de seta que aparece ao lado do campo de valor da propriedade quando opções adicionais estão disponíveis.
- Digite ou selecione um novo valor para a propriedade.

Por exemplo, suponha que você queria fornecer a opção de instalar o arquivo de Ajuda do seu aplicativo. Siga as etapas para criar o recurso e nomeie-o "Arquivo de ajuda." Se você quer tornar a instalação do arquivo de Ajuda opcional, defina a propriedade Required como No. Se você quer que o recurso seja instalado na primeira vez que o usuário tentar invocar o recurso pressionando F1 para Ajuda, defina a propriedade Advertised como Yes.

### Especificando recursos para um tipo de instalação

Você pode incluir diferentes tipos de instalação em um programa de instalação e especificar quais recursos cada tipo de instalação deve instalar. Tipos de instalação oferecem diferentes níveis de instalação que o usuário pode escolher:
 - Instalação típica instala todos os recursos e arquivos.
- Instalação mínima instala o número mínimo de recursos e arquivos necessários para um aplicativo funcionar.
- Instalação personalizada permite especificar quais recursos instalar.

Você deve incluir pelo menos um tipo de instalação.

Todos os três tipos de instalação instalam recursos listados por Sempre instalar. Por exemplo, uma instalação básica inclui recursos listados por Sempre instalar e o tipo de instalação &Típica. O sinal de e comercial (&) no nome do tipo de instalação indica a tecla de acesso para um tipo de instalação específico na interface do usuário do Setup. Você pode incluir ou remover tipos de instalação dependendo se deseja que seja incluído, contanto que um permaneça disponível, ou renomear os tipos de instalação.

> **Observação:** Especificar recursos para cada tipo de instalação não é obrigatório ao criar um programa de instalação.

### Para selecionar tipos de instalação e especificar recursos para cada tipo de instalação
- No nó Organizar sua instalação, clique em Tipos de instalação .
- No painel Tipos de instalação, selecione a caixa de seleção para cada tipo de instalação que deseja incluir.
- No painel Recursos instalados para o tipo de instalação < selecionado >, selecione a caixa de seleção para cada recurso que deseja que este tipo de instalação instale.

### Adicionando arquivos ao Setup

O arquivo executável (.exe) geralmente é necessário para o usuário iniciar um aplicativo. Você pode adicionar este arquivo primeiro junto com outros arquivos que seu aplicativo requer, seguidos por quaisquer arquivos opcionais.

O Visual FoxPro fornece arquivos de recurso que ampliam a funcionalidade básica dos seus aplicativos, incluindo arquivos de recurso FoxUser, bibliotecas de API e controles Microsoft ActiveX. Se você usa esses arquivos, deve adicioná-los ao programa de instalação para que possam ser instalados ao executar o Setup. Para obter mais informações sobre arquivos de recurso que você pode usar, consulte Arquivos de recurso em aplicativos.

### Para visualizar arquivos que você pode adicionar ao Setup
- No nó Especificar dados do aplicativo, clique em Arquivos .

A visualização Arquivos é dividida em quatro painéis. Os painéis esquerdos exibem pastas nos computadores de origem e de destino. Os painéis direitos exibem os arquivos nessas pastas. A caixa Recurso aparece acima dos quatro painéis.

> **Observação:** A propriedade INSTALLDIR especifica o diretório que contém a pasta raiz dos arquivos do seu aplicativo e geralmente é especificada como o diretório de instalação de destino.

Antes de adicionar arquivos ao projeto Setup, você deve especificar o recurso com o qual associar esses arquivos selecionando-o na caixa Recurso.

> **Observação:** Adicione arquivos obrigatórios como recursos Sempre instalar.

Certifique-se de que o recurso apareça na caixa Recurso. Após selecionar o recurso, você pode adicionar arquivos ao projeto Setup copiando-os das pastas de origem para as pastas no computador de destino.

### Para adicionar arquivos da pasta de origem à pasta de destino
- No painel Pastas do computador de destino, selecione a pasta de destino onde deseja instalar o arquivo do aplicativo.
- No painel Arquivos do computador de origem, arraste o arquivo de origem para a pasta de destino. Observação A pasta especificada por INSTALLDIR no nó Informações gerais como o diretório de instalação padrão deve aparecer no painel Pastas do computador de destino. Arrastar o arquivo de origem para a pasta de destino apenas instrui o InstallShield Express onde localizar o arquivo de origem quando você compilar seu programa de instalação. Não move nem remove nenhum arquivo no computador de origem.

Você também pode visualizar uma lista de pastas predefinidas, como a pasta da área de trabalho, que pode selecionar e adicionar à lista de pastas do computador de destino.

### Para visualizar e adicionar pastas predefinidas
- No painel Pastas do computador de destino, clique com o botão direito em Computador de destino .
- Clique em Mostrar pastas predefinidas .
- Selecione a pasta que deseja adicionar. A pasta aparece na lista de pastas do computador de destino.

Você pode criar uma ou mais subpastas em uma pasta de destino.

### Para criar uma subpasta em uma pasta de destino
- Clique com o botão direito na pasta de destino e clique em Adicionar .
- Digite um nome para a nova pasta e pressione ENTER.

### Registrando arquivos

O Windows Installer inclui os seguintes recursos:
 - Reverter uma instalação malsucedida, retornando o computador de destino ao seu estado pré-instalação. Por exemplo, Servidores COM, como arquivos ActiveX, COM e COM+, exigem registro especial para que os aplicativos possam acessar suas interfaces. Esses arquivos .ocx, .exe e .dll tradicionalmente contêm funções de autoregistro que podem ser invocadas para registrar os arquivos durante a instalação. No entanto, confiar no autoregistro pode causar alguns problemas com o Windows Installer. Observação Ao registrar um Servidor COM, é altamente recomendado que você selecione Extrair informações COM em vez de Autoregistro como o tipo de registro para o arquivo. Se você selecionar Autoregistro , o Windows Installer não terá as informações necessárias para remover o Servidor COM do registro corretamente. Com programas de instalação tradicionalmente scriptados, o autoregistro era aceitável para instalar objetos COM e ainda é válido. No entanto, objetos COM de autoregistro não passam suas informações de instalação e registro ao Windows Installer. Portanto, o Windows Installer não pode reverter a instalação e registro de objetos COM autoregistrados ou anunciar esses objetos.
- Anunciar produtos instalados ou elementos individuais do produto, como objetos COM. O anúncio torna um produto ou objeto COM disponível para o usuário ou computador de destino sem instalar o produto até que o usuário ou outra função do computador tente acessar o elemento anunciado. O anúncio ocorre colocando um atalho no local apropriado, como o menu Iniciar ou o registro.

### Para registrar um servidor COM com InstallShield Express
- No nó Especificar dados do aplicativo, clique em Arquivos .
- Copie o arquivo do Servidor COM da pasta de origem para a pasta de destino.
- Clique com o botão direito no arquivo que deseja registrar e clique em Propriedades .
- Na caixa de diálogo Propriedades, clique na guia Configurações COM e .NET .
- Selecione um Tipo de registro .

Para obter mais informações sobre registro de Servidores COM, consulte Cenários de distribuição do Visual FoxPro.

### Selecionando objetos e módulos de mesclagem

Um módulo de mesclagem (arquivo .msm) contém toda a lógica, entradas de registro e arquivos necessários para instalar um aplicativo ou arquivos de runtime com sucesso. Se você fosse instalar seu aplicativo manualmente, precisaria copiar os arquivos de runtime do Visual FoxPro para o computador de destino e registrar esses arquivos. No entanto, se você selecionar o módulo de mesclagem Microsoft Visual FoxPro 9 Runtime Libraries, o InstallShield Express copia e registra os arquivos de runtime corretamente.

Para um aplicativo Visual FoxPro, você deve selecionar, no mínimo, os módulos Microsoft Visual FoxPro 9 Runtime Libraries e MSXML 4.0. Para obter mais informações sobre bibliotecas de runtime do Visual FoxPro, consulte Bibliotecas de runtime do Visual FoxPro.

> **Observação:** Quando você seleciona o módulo Microsoft Visual FoxPro 9 Runtime Libraries no InstallShield Express, as caixas de seleção para os módulos Microsoft Visual C Runtime Library 7.1 e GDI Plus Redist são selecionadas automaticamente e devem permanecer selecionadas. O Visual FoxPro 9.0 requer esses módulos; portanto, não desmarque a seleção desses módulos.

Existem dois módulos MSXML 4.0 que devem ser incluídos:
 - MSXML 4.0 (msxml4sxs32.msm)
- MSXML 4.0 (msxml4sys32.msm)

Você também deve incluir o módulo de mesclagem Microsoft Visual FoxPro 9 Report Applications, que contém aplicativos de runtime usados pelo mecanismo de relatórios do Visual FoxPro 9.0. Para obter mais informações, consulte Incluindo arquivos de relatório para distribuição.

Se seu aplicativo usa uma das funções CURSORTOXML( ), você também deve incluir os módulos de mesclagem MSXML 3.0. Estes incluem os seguintes:
 - MSXML 3.0 (msxml3_wim32.msm)
- Módulo de mesclagem Msxml3 Exception INF (msxml3inf_wim32.msm)
- Biblioteca padrão WebData (wdstddll_wim32.msm)

Se você está implantando seu aplicativo internacionalmente, pode precisar incluir um ou mais dos módulos de idioma de recurso Microsoft Visual FoxPro 9.

### Para selecionar objetos e módulos de mesclagem para instalação
- No nó Especificar dados do aplicativo, clique em Redistribuíveis .
- No painel Redistribuíveis do InstallShield, selecione a caixa de seleção para cada módulo de mesclagem que deseja instalar.
- Você pode instalar um módulo de mesclagem recurso por recurso selecionando ou desmarcando as caixas de seleção no painel Instalação condicional quando disponível.

Para obter mais informações sobre módulos de mesclagem, consulte Cenários de distribuição do Visual FoxPro.

### Criando atalhos e pastas

O InstallShield Express permite criar atalhos e pastas no menu Iniciar e na área de trabalho.

### Para criar pastas ou atalhos
- No nó Configurar o sistema de destino, clique em Atalhos/Pastas .
- Na visualização em árvore Atalhos no painel central, clique com o botão direito no nó onde deseja instalar um atalho ou pasta e clique em Novo atalho ou Nova pasta .
- Se você criou um atalho, deve especificar um arquivo de destino. Na caixa de diálogo Procurar destino do atalho, clique duas vezes no arquivo para o qual deseja criar um atalho na lista Examinar em. Você também pode associar seu atalho a um recurso navegando até a pasta que contém o arquivo associado ao recurso e selecionando o arquivo na lista.
- Digite um nome para o atalho ou pasta e pressione ENTER. Para renomear a pasta ou atalho, clique com o botão direito nele, clique em Renomear , digite um novo nome e pressione ENTER. Observação Os arquivos do seu aplicativo estão na parte inferior da lista Examinar em.

### Criando chaves de registro

Se seu aplicativo usa chaves de registro, por exemplo, para acompanhar opções do usuário, o InstallShield Express pode adicioná-las ao computador de destino durante a instalação. Se as chaves não existem no computador de desenvolvimento, você pode criá-las manualmente.

> **Observação:** Criar chaves de registro não é obrigatório ao criar um programa de instalação.

Entradas de registro são criadas em colmeias de registro. Colmeias de registro categorizam entradas de registro por função. Por exemplo, classes de Servidor COM são armazenadas na colmeia de registro HKEY_CLASSES_ROOT. Opções de software, como opções para o Visual FoxPro, são armazenadas na pasta Software na colmeia HKEY_CURRENT_USER.

### Para criar chaves de registro
- No nó Configurar o sistema de destino, clique em Registro .
- No painel de visualização Registro do computador de destino, clique com o botão direito na colmeia de registro desejada.
- No menu de atalho, aponte para Novo e clique em Chave .
- Digite um nome para a chave e pressione ENTER.
- Clique com o botão direito na nova chave, aponte para Novo e selecione o tipo de valor que deseja adicionar à chave.
- No painel de dados de registro do computador de destino, clique duas vezes na chave para inserir um valor de dados. Dependendo do tipo de chave, você pode inserir um nome para ela.

### Criando nomes de fonte de dados Open Database Connectivity (ODBC) (DSNs)

Se o computador de desenvolvimento tem DSNs previamente existentes, você pode instruir o InstallShield Express a instalar o DSN no computador de destino. Se você está instalando DSNs, deve incluir o módulo de mesclagem MDAC ao selecionar módulos de mesclagem caso o computador de destino não tenha componentes ODBC instalados.

> **Observação:** Criar DSNs ODBC não é obrigatório ao criar um programa de instalação.

### Para criar DSNs
- No nó Configurar o sistema de destino, clique em Recursos ODBC .
- Na visualização em árvore Recursos ODBC, selecione as caixas de seleção para os DSNs que deseja criar no computador de destino.

### Personalizando a aparência do Setup

Você pode selecionar e alterar a aparência das caixas de diálogo que os usuários veem ao instalar seu aplicativo. Você pode especificar imagens bitmap (.bmp) para cada caixa de diálogo e adicionar caixas de diálogo adicionais, por exemplo, para permitir que o usuário especifique uma pasta de destino.

> **Observação:** Personalizar a aparência do Setup não é obrigatório ao criar um programa de instalação.

### Para selecionar caixas de diálogo
- No nó Personalizar a aparência da instalação, selecione Caixas de diálogo .
- Na visualização em árvore Caixas de diálogo, selecione as caixas de diálogo que deseja exibir durante a instalação. Quando você seleciona uma caixa de diálogo, uma imagem da caixa de diálogo aparece no painel inferior esquerdo, e as propriedades da caixa de diálogo aparecem no painel superior direito.

### Para permitir que o usuário especifique uma pasta de destino
- No nó Personalizar a aparência da instalação, selecione Caixas de diálogo .
- Na visualização em árvore Caixas de diálogo, clique em Pasta de destino .

### Compilando seu programa de instalação

Após terminar de projetar e definir as propriedades para todos os elementos em seu projeto Setup, incluindo recursos, arquivos, atalhos, entradas de registro e interface do usuário, você está pronto para compilar seu programa de instalação.

Os tipos de compilação mais comumente selecionados são CD-ROM ou imagem única. Selecionar CD_ROM cria um programa de instalação que contém arquivos organizados em uma estrutura de diretórios. Selecionar SingleImage combina os arquivos em um único arquivo.

### Para compilar um programa de instalação
- No nó Preparar para liberação, clique em Compilar sua liberação .
- Na visualização em árvore Compilações, selecione o tipo de mídia que deseja compilar.
- Na lista de propriedades, defina ou edite as propriedades de compilação.
- Para compilar seu programa de instalação, clique com o botão direito no tipo de mídia selecionado e clique em Compilar . O InstallShield Express coloca o pacote de instalação compilado na seguinte pasta: <diretório do projeto>\Express\<tipo de mídia>\DiskImages\DISK1

### Testando seu programa de instalação

É importante testar seu programa de instalação. Você pode fazer isso sem executar a instalação real usando InstallShield Express.

### Para testar seu programa de instalação com InstallShield Express
- No nó Preparar para liberação, clique em Testar sua instalação .
- Na visualização em árvore Compilações, selecione o tipo de mídia contendo a compilação que deseja testar.
- Se você quer executar o programa de instalação e instalar seu aplicativo e seus arquivos no computador de desenvolvimento, clique em Executar sua instalação . -ou- Se você quer testar apenas as caixas de diálogo do Setup e quaisquer ações personalizadas que escolheu, clique em Testar sua instalação . Esta opção não instala nenhum arquivo nem faz alterações no sistema.

# Distribuindo um aplicativo

Após compilar e testar seu programa de instalação, você está pronto para distribuí-lo.

### Para distribuir seu programa de instalação
- No nó Preparar para liberação, clique em Distribuir sua liberação .
- Na visualização em árvore Compilações, selecione o tipo de mídia contendo a compilação que deseja distribuir.
- Insira o local ou clique em Procurar e navegue até o local onde seu pacote de instalação será copiado.
- Clique em Distribuir para local .

Você também pode copiar seu pacote de instalação para um local FTP.

Para informações adicionais e opções para distribuir aplicativos, consulte a documentação do InstallShield Express.

Este passo a passo assume que você está instalando um aplicativo Visual FoxPro simples que não tem dependências além das Bibliotecas de runtime do Visual FoxPro. As informações a seguir incluem instruções necessárias para cenários de distribuição além de instalar apenas aplicativos Visual FoxPro e seus dados nativos. Para esses cenários, adicione os módulos de mesclagem apropriados ao selecionar objetos e módulos de mesclagem para seu programa de instalação.

### Serviços Web e SOAP

Se seu aplicativo usa serviços Web ou SOAP, deve incluir os seguintes módulos de mesclagem:
 - Arquivos SOAP SDK (Soap_Core.msm)
- Máquina virtual Visual Basic (MSVBVM60.msm)
- Biblioteca Microsoft Component Category Manager (Comcat.msm)
- Microsoft OLE 2.40 (OLEAUT32.msm)

### Aplicativos usando componentes do aplicativo de relatório Visual FoxPro

Se seu aplicativo usa o Aplicativo de construtor de relatórios padrão, Aplicativo de saída de relatório ou Aplicativo de visualização de relatório, e você quer garantir que esses componentes estejam disponíveis para seu aplicativo por padrão, inclua o seguinte módulo de mesclagem:
 - Aplicativos de relatório Visual FoxPro 9 (vfp9rptapps.msm)

Para obter mais informações, consulte Incluindo arquivos de relatório para distribuição.

### Provedor OLE DB do Microsoft Visual FoxPro

O Provedor OLE DB do Visual FoxPro permite que tanto o Visual FoxPro quanto outros aplicativos acessem dados do Visual FoxPro usando OLE DB ou ActiveX® Data Objects (ADO). Para instalar o Provedor OLE DB do Visual FoxPro no computador de destino, inclua o módulo de mesclagem Microsoft Visual FoxPro OLE DB Provider (VfpOLEDB.msm).

### Controles ActiveX

Controles ActiveX são um elemento comum de muitos aplicativos Visual FoxPro. Para incluir controles ActiveX com seu Setup do InstallShield Express, deve incluir o módulo de mesclagem Microsoft Component Category Manager Library (Comcat.msm).

> **Observação:** Windows 2000 e Windows XP também instalam arquivos neste módulo de mesclagem.

Os controles ActiveX que você instala afetam o tipo de módulos de mesclagem que precisa instalar e as etapas extras que deve tomar para instalá-los.
 - Controles ActiveX comuns Estes são controles ActiveX comuns que acompanham o Visual FoxPro e o Microsoft Visual Studio. O InstallShield Express é fornecido com módulos de mesclagem para a maioria desses controles. Se necessário, adicione o módulo de mesclagem apropriado para o controle necessário. Por exemplo, se seu aplicativo usa o controle Treeview, deve incluir o módulo de mesclagem MSCOMCTL.msm. Observação Os Controles ActiveX comuns incluídos nos módulos de mesclagem do InstallShield Express contêm informações de registro compatíveis com Windows Installer.
- Controles Microsoft Foundation Class (MFC) Alguns controles mais antigos, como o controle Calendar, usam as bibliotecas MFC; portanto, é recomendado que você inclua os módulos de mesclagem MFC apropriados, como MFC42.msm. Como com controles VBCCE, você deve adicionar o controle manualmente ao projeto e definir várias configurações.
- Controles de terceiros Certifique-se de registrar quaisquer controles de terceiros incluídos. Além disso, pode precisar adicionar chaves de registro específicas usando a janela Registro do InstallShield Express para quaisquer requisitos de licenciamento necessários. Para obter mais informações sobre controles de terceiros, consulte a documentação fornecida pelo fornecedor sobre como e onde instalar esses controles. A documentação de controles de terceiros também deve fornecer informações sobre quaisquer arquivos de dependência necessários, como arquivos MFC.

Para garantir que o Windows Installer possa reverter ou anunciar arquivos instalados, você deve instalar arquivos de maneira compatível com os requisitos do Windows Installer. O autoregistro de arquivos não é compatível com os requisitos do Windows Installer. Você pode garantir que o InstallShield Express instale objetos COM compatíveis com Windows Installer seguindo as instruções sobre registro de arquivos neste tópico. Para obter mais informações, consulte a documentação online do InstallShield Express.

### Aplicativos usando HTML Help

Os módulos de mesclagem Biblioteca de suporte HTML Help do Microsoft Visual FoxPro (VFP9HTMLHelp.msm) incluem os arquivos FOXHHELP9.exe e FOXHHELPPS9.dll necessários para suportar HTML Help sensível ao contexto em seus aplicativos Visual FoxPro.

Além do seu arquivo .chm específico do aplicativo, você pode incluir os arquivos principais do visualizador HTML Help. Versões posteriores do Microsoft Internet Explorer incluem esses arquivos. Você também pode distribuí-los com o arquivo HHUPD.exe disponível na Microsoft Developer Network (MSDN).

### Aplicativos usando componentes MDAC

Para aplicativos Visual FoxPro executando em sistemas operacionais anteriores ao Windows 2000 ou Windows XP, é recomendado que você inclua o módulo de mesclagem Microsoft Data Access Components (MDAC) (MDAC25.msm) se seus aplicativos usam qualquer um dos seguintes componentes de dados:
 - Drivers ODBC, incluindo Driver ODBC Microsoft Visual FoxPro (VFPODBC.msm)
- Provedor OLE DB
- ADO, RDS

### Servidores COM

Os recursos de reversão e anúncio do Windows Installer permitem desfazer a instalação e registro de componentes se a instalação do produto não for bem-sucedida. No entanto, você deve instalar e registrar objetos COM corretamente para tornar esses recursos disponíveis. Para registrar objetos COM instalados corretamente, defina o Tipo de registro como Extrair informações COM. Objetos COM de autoregistro sacrificam a funcionalidade de reversão e anúncio do Windows Installer.

Para obter mais informações, consulte as instruções sobre registro de arquivos neste tópico.

### Aplicativos localizados

As Bibliotecas de runtime do Visual FoxPro (VFP9Runtime.msm) contêm o arquivo de recurso neutro em idioma padrão (VFP9renu.dll) usado para enviar todos os aplicativos em inglês (EUA). Se você quer incluir suporte para outro arquivo de recurso localizado (VFP9Rnnn.dll), inclua o módulo de mesclagem Microsoft Visual FoxPro Resource apropriado que contém o arquivo de recurso localizado desejado.

> **Observação:** Arquivos de recurso localizados não localizam as caixas de diálogo do Setup. Você pode selecionar o idioma desejado para as caixas de diálogo do Setup ao criar seu projeto Setup.

### Para incluir um arquivo de recurso localizado do Visual FoxPro
- No nó Especificar dados do aplicativo, clique em Redistribuíveis .
- Para identificar o módulo de mesclagem Microsoft Visual FoxPro Resource desejado, observe a descrição de cada módulo de mesclagem no painel inferior esquerdo.
- Selecione o módulo de mesclagem desejado. Por exemplo, para incluir o arquivo de recurso alemão, selecione o módulo de mesclagem VFP9rdeu.msm. A tabela a seguir lista os módulos de mesclagem disponíveis contendo os arquivos de recurso localizados correspondentes. Idioma Módulo de mesclagem Chinês, simplificado VFP9rchs.msm Chinês, tradicional VFP9rcht.msm Tcheco VFP9rcsy.msm Francês VFP9rfra.msm Alemão VFP9rdeu.msm Coreano VFP9rkor.msm Russo VFP9rrus.msm Espanhol, ordenação internacional VFP9resn.msm

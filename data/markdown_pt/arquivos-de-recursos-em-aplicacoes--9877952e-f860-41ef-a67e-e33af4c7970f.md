# Arquivos de recursos em aplicações

O Visual FoxPro fornece vários arquivos de recursos que ampliam a funcionalidade básica de suas aplicações, incluindo arquivos de recursos FoxUser, bibliotecas API e controles ActiveX. Se você usar esses arquivos, deve incluí-los em seu projeto ou árvore de distribuição.

A tabela a seguir lista alguns dos arquivos que você pode incluir em sua aplicação adicionando-os ao seu projeto. Para obter mais informações sobre como incluir arquivos em sua aplicação para distribuição, consulte Como: incluir arquivos com aplicações para distribuição.

| Se você está | Adicione estes arquivos ao seu projeto |
| --- | --- |
| Aplicando uma configuração personalizada à sua aplicação | Config.fpw |
| Aplicando configurações personalizadas à sua aplicação | FoxUser.dbf e FoxUser.fpt |

Para obter detalhes sobre como incluir arquivos em seu programa de instalação, consulte a ajuda associada ao programa de criação de instalação que você está usando. O programa de criação de instalação que você usa deve criar pacotes de instalação MSI usando a tecnologia Windows Installer.

# Arquivos de recursos FoxUser.*

Os arquivos de recursos do Visual FoxPro armazenam informações úteis para sua aplicação, incluindo posições de janelas, configurações de janelas Browse e definições de etiquetas. Se sua aplicação depende de configurações específicas para qualquer um desses itens de recurso, você também deve distribuir o banco de dados FoxUser e os arquivos memo ou os arquivos de recursos que você criar especificamente para sua aplicação. Esses arquivos de recursos consistem em uma tabela Visual FoxPro com um arquivo memo associado, geralmente chamados FoxUser.dbf e FoxUser.fpt.

> **Observação:** O arquivo de recursos FoxUser.dbf não é o mesmo que o arquivo de recursos específico de localidade que contém caixas de diálogo e mensagens de erro. O arquivo de recursos FoxUser.dbf armazena informações da aplicação, como macros que você definiu; o arquivo de recursos específico de localidade armazena cadeias de texto do sistema.

# Arquivos de biblioteca externa

Se sua aplicação inclui arquivos de biblioteca externa, como controles ActiveX (arquivos .ocx) ou bibliotecas API do Visual FoxPro (arquivos .fll), certifique-se de que eles estejam colocados no diretório apropriado em seu pacote de instalação. Você pode distribuir o arquivo Visual FoxPro FoxTools.fll com suas aplicações. Para obter mais informações sobre como criar bibliotecas externas para acessar a API do Visual FoxPro, consulte Acesso a APIs.

# Controles ActiveX e componentes COM

Se você incluir controles ActiveX ou criou um servidor Automation (um componente COM) como parte de sua aplicação, inclua quaisquer arquivos .ocx e .dll em seu projeto e certifique-se de que os arquivos de suporte necessários sejam instalados no local apropriado no computador do usuário.

> **Observação:** As diretrizes do Windows 2000 Logo não recomendam instalar componentes no diretório System do Windows. Você só pode distribuir controles ActiveX para os quais possui licença. Para servidores Automation, você também deve incluir arquivos de registro, como bibliotecas de tipos (arquivos .tlb) e arquivos de registro (.vbr), com sua aplicação.

Se você usar seu programa de criação de instalação para criar os discos de distribuição, pode incluir esses arquivos automaticamente. Ao fazer isso, o programa de criação de instalação garante que os componentes COM sejam registrados corretamente no computador do usuário quando a aplicação for instalada. Para obter mais informações sobre como incluir arquivos em seu programa de criação de instalação, consulte a ajuda associada ao programa.

Todos os usuários podem executar formulários contendo controles ActiveX; no entanto, sua aplicação não pode realizar certas tarefas se estiver sendo executada sob a versão run-time do Visual FoxPro. Lembre-se das seguintes diretrizes:
 - Sua aplicação deve estar sendo executada sob uma versão completa do Visual FoxPro para alterar formulários, classes ou subclasses que incluem controles ActiveX.
- Sua aplicação deve estar sendo executada sob uma versão completa do Visual FoxPro para adicionar controles ActiveX a formulários em tempo de execução. Por exemplo, a versão completa do Visual FoxPro é necessária para adicionar o controle Listview a um formulário executando o seguinte código: PUBLIC frmOleNewForm frmOleNewForm = CREATEOBJECT("form") frmOleNewForm.Show frmOleNewForm.ScaleMode = 3 frmOleNewForm.Addobject("NewListview","OLEControl",; "MSComctlLib.ListViewCtrl") Observação Quando um formulário é fechado, controles adicionados em tempo de execução não são salvos.
- Sua aplicação pode estar sendo executada sob a versão run-time ou completa do Visual FoxPro para adicionar controles ActiveX subclassificados a um formulário em tempo de execução. Por exemplo, você pode definir a subclasse RedListview da classe Listview e distribuir a subclasse em Olelib.vcx; todos os usuários podem então adicionar o controle RedListview a um formulário executando o seguinte código: PUBLIC frmOleNewForm frmOleNewForm = CREATEOBJECT("form") frmOleNewForm.Show frmOleNewForm.ScaleMode = 3 SET CLASSLIB TO CURR() + OLELIB.VCX frmOleNewForm.Addobject("NewListview","RedListview")

# Arquivos de configuração

Você pode usar o arquivo de configuração Config.fpw para estabelecer muitas configurações padrão do Visual FoxPro. Por exemplo, você pode alterar o título do Visual FoxPro, a cor de fundo e a forma como um usuário navega com o teclado.

Se você deseja que o arquivo de configuração seja somente leitura, coloque-o em seu projeto e marque-o como incluído. Se você deseja que a configuração seja modificável, coloque o arquivo em seu projeto e marque-o como excluído. Distribua o arquivo de configuração com sua aplicação ou arquivo executável, como um arquivo separado. Por padrão, o Visual FoxPro procura um arquivo de configuração chamado Config.fpw. No entanto, você pode especificar um nome de arquivo de configuração diferente usando a opção de linha de comando `-C` ao iniciar o Visual FoxPro.

Para obter mais informações sobre opções que você pode definir no arquivo de configuração, consulte "Usar um arquivo de configuração" em Personalizar o ambiente do Visual FoxPro.

# Arquivos de recursos específicos de localidade

Se você estiver distribuindo sua aplicação junto com a versão run-time do Visual FoxPro, pode ser necessário incluir um arquivo de recursos específico de localidade. Este arquivo contém as caixas de diálogo e outros elementos de interface do usuário que o Visual FoxPro usa para interagir com o usuário. Um arquivo de recursos run-time diferente existe para cada idioma em que o Visual FoxPro está disponível.

Para obter mais informações sobre como usar arquivos run-time específicos de localidade, consulte "Distribuir arquivos run-time específicos de localidade" em Desenvolver aplicações internacionais.

> **Observação:** O arquivo de recursos específico de localidade não é o mesmo que o arquivo de recursos FoxUser.dbf, que armazena informações da aplicação, como macros que você definiu. O arquivo de recursos específico de localidade armazena cadeias de texto do sistema.

Se você estiver criando uma aplicação para plataformas do Oriente Médio, certifique-se de adicionar o arquivo VBAME.DLL ao seu conjunto de distribuição e ter ele instalado no diretório System do Windows.

# Observação Você não pode distribuir Winhelp.exe nem os arquivos de Ajuda fornecidos com o Visual FoxPro.

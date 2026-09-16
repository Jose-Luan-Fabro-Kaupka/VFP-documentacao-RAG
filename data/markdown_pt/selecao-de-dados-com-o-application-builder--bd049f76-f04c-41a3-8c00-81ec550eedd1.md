# Seleção de dados com o Application Builder

Depois de planejar sua aplicação, você precisa selecionar as fontes de dados necessárias para o desenvolvimento da aplicação. Você pode usar a guia Data Tab, Application Builder para adicionar bancos de dados e tabelas à sua aplicação e ao projeto.

# Adicionando dados usando a guia Data

Se você já possui dados existentes, pode usar a guia Data para criar um ambiente de dados para sua aplicação adicionando tabelas livres ou tabelas de um banco de dados à aplicação. Assim que você especifica uma tabela, o Application Builder a exibe na grade e se prepara para criar um formulário e um relatório para a tabela. Neste ponto, você selecionou apenas quais fontes de dados incluir. Elas não são realmente adicionadas ao framework até que você selecione o botão Generate. Se você deseja adicionar apenas a fonte de dados e não ter novos formulários ou relatórios, desmarque as opções ao lado da entrada da tabela. Se você tiver uma caixa de seleção de formulário ou relatório marcada quando clicar no botão Generate, o assistente apropriado cria um novo documento para essa fonte de dados. Você pode selecionar um estilo visual para esses documentos nas listas suspensas Style.

Você pode editar esses documentos posteriormente na guia Form ou na guia Report do Application Builder. Se você tiver fontes de dados listadas na grade da guia Data e clicar no botão OK para sair do Application Builder, o Visual FoxPro solicita que você adicione as tabelas, formulários e relatórios ao seu projeto e aplicação. Clicar no botão Generate executa a mesma função.

Os documentos gerados pelo Application Builder contêm todos os campos da fonte de dados selecionada. Se você deseja mais controle sobre o layout do documento, execute o Form Wizard ou o Report Wizard diretamente do menu Wizards e adicione o documento recém-criado na guia Form ou na guia Report. Você também pode adicionar ou editar formulários ou relatórios no Application Builder.

Quando você usa o Application Builder para adicionar dados, eles são marcados no projeto como Excluded, o que significa que não são vinculados à aplicação compilada. Isso permite que você edite a tabela adicionada. Uma tabela incorporada em uma aplicação é somente leitura e não pode ser editada. Se você deseja incluir uma tabela no projeto e, assim, torná-la somente leitura (por exemplo, uma tabela de pesquisa especial cujos dados não mudarão), clique com o botão direito do mouse na tabela no Project Manager e selecione o item de menu Include.

# Criando dados usando a guia Data

Você também pode usar o Database Wizard ou os botões Database Wizard na guia Data para criar novas tabelas a serem adicionadas ao projeto e à aplicação. Esses assistentes criam novas estruturas de dados para sua aplicação na pasta de dados apropriada e permitem que você gere novos documentos da mesma maneira discutida anteriormente.

Os documentos básicos que o Application Builder cria contêm todos os campos nas tabelas nas quais se baseiam. Esses documentos são excelentes para entrada e relatório básicos de dados, mas você pode querer criar documentos para outros propósitos exclusivos em sua aplicação. O Form Wizard e o Report Wizard oferecem mais flexibilidade e as foundation classes incluídas no Component Gallery oferecem funcionalidade adicional a formulários e relatórios.

# Localizando dados

Se você usar o Application Builder para adicionar dados e documentos à sua aplicação, a vinculação de dados é tratada automaticamente. O Application Builder, no entanto, oferece uma opção Default Data Directory na guia Advanced Tab, Application Builder se você estiver codificando manualmente documentos para vincular a dados e precisar que o framework da aplicação trate a resolução de caminho de dados. Use essa configuração para especificar uma pasta que contém suas fontes de dados para fornecer informações de caminho apropriadas para esses dados.

# Importando dados

Em muitas aplicações, você pode já ter dados que deseja usar, mas eles não estão necessariamente no formato adequado. Podem estar em formato de texto simples ou de planilha. Nesses casos, você pode usar o Import Wizard para migrar seus dados para tabelas FoxPro. Você pode então adicionar facilmente essas tabelas à sua aplicação.

# Upsizing de dados

O Visual FoxPro inclui um assistente de upsizing que permite mover seus dados FoxPro para um banco de dados SQL Server. Se as demandas da sua aplicação exigirem o uso de um desses bancos de dados, você pode migrar facilmente seus dados existentes e manter a aplicação intacta.

O SQL Server Upsizing Wizard permite que você crie remote views em tabelas. Se você selecionar essa opção, as tabelas em seu banco de dados serão alteradas para remote views. Como os documentos (formulários ou relatórios) em sua aplicação estão vinculados apenas ao nome da fonte de dados, você ainda pode executar sua aplicação, mas os dados usados serão dados do SQL Server em vez de tabelas FoxPro.

Se você tiver dados existentes do SQL Server que deseja usar em sua aplicação, pode configurar facilmente um banco de dados Visual FoxPro contendo remote views apontando para essas fontes de dados. O framework da aplicação tratará essas fontes como se fossem tabelas FoxPro nativas.

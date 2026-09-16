# Aprimorando aplicativos usando tecnologia SQL Pass-Through

Seja criando e fazendo upsizing de um protótipo local funcional ou desenvolvendo seu aplicativo contra dados remotos usando remote views, você obtém acesso aos grandes armazenamentos de dados tipicamente disponíveis em um banco de dados servidor. Além disso, você pode aproveitar as capacidades de segurança e processamento de transações do servidor remoto. Enquanto remote views lidam com as principais tarefas de gerenciamento de dados, você pode aprimorar seu aplicativo usando tecnologia SQL pass-through (SPT) para criar objetos no servidor, executar stored procedures em um servidor e executar comandos usando sintaxe nativa do servidor.

Os tópicos a seguir discutem técnicas para implementar tecnologia cliente/servidor em um aplicativo funcional que usa remote views.

# Nesta seção
 **How to: Set Up an ODBC Data Source**
Descreve como instalar um driver ODBC e configurar uma fonte de dados ODBC para que você possa criar remote views ou usar SQL pass-through.
**Using SQL Pass-Through Technology**
Descreve como remote views fornecem o método mais fácil e comum para acessar e atualizar dados remotos. Os wizards de upsizing podem criar remote views automaticamente em seu banco de dados como parte do upsizing, ou você pode usar o Microsoft Visual FoxPro para criar remote views após o upsizing.
**Working with Remote Data Using SQL Pass-Through**
Explica que depois de recuperar um conjunto de resultados usando SQL pass-through, você pode visualizar e controlar as propriedades do cursor do conjunto de resultados usando as funções CURSORGETPROP( ) e CURSORSETPROP( ) do Microsoft Visual FoxPro.
**Handling SQL Pass-Through Errors**
Explica que o Microsoft Visual FoxPro armazena um erro retornado por uma função SQL pass-through em uma matriz.

# Seções relacionadas
 **Using Visual FoxPro**
Descreve recursos de programação do Visual FoxPro projetados para melhorar a produtividade do desenvolvedor, incluindo métodos Access e Assign, suporte para mais formatos de arquivo gráfico e linguagem para simplificar tarefas de programação.
**Developing Visual FoxPro Applications**
Inclui informações conceituais sobre como desenvolver aplicativos Visual FoxPro, instruções para criar bancos de dados e a interface do usuário, e outras tarefas necessárias para criar aplicativos Visual FoxPro.
**Application Planning**
Descreve como o planejamento cuidadoso economiza tempo, esforço e dinheiro e como muitas das decisões que você toma durante a fase de planejamento impactarão como você cria elementos do aplicativo.
**Creating Applications**
Discute como criar um aplicativo Visual FoxPro, que pode incluir um ou mais bancos de dados, um programa principal que configura o ambiente do sistema do aplicativo e uma interface do usuário composta de formulários, toolbars e menus.
**Web Services and Components**
Explica como você pode estender seu aplicativo Visual FoxPro para funcionar para múltiplos usuários e aproveitar controles Microsoft ActiveX e aplicativos habilitados para automação.
**Working with Data**
Descreve como criar aplicativos eficazes com índices, tabelas e bancos de dados baseados em seus requisitos de dados.
**Working with Projects**
Define um projeto como uma configuração e um grupo de arquivos que produzem um programa ou arquivo binário final ou arquivos.
**Compiling an Application**
Explica como usar a abordagem modular para que você possa verificar a funcionalidade de cada componente que cria antes de compilá-los em um aplicativo, que reúne os componentes executáveis do seu projeto.
**Testing and Debugging Applications**
Descreve ferramentas de depuração do Visual FoxPro que ajudam você a encontrar e corrigir quaisquer erros que descobrir em seus aplicativos.
**Distributing Applications**
Explica como preparar a distribuição do seu aplicativo incluindo todos os arquivos necessários e criando discos de distribuição, depois de concluir o desenvolvimento e os testes do aplicativo.

# Guia Projects, caixa de diálogo Options

Contém opções para o Project Manager.

Quando você escolhe Set As Default — que aparece em cada guia da caixa de diálogo — o Visual FoxPro salva as configurações de opção no registro (banco de dados de registro do sistema Windows).

# Ação de clique duplo em projeto

Especifica se o Visual FoxPro executa ou modifica um arquivo quando você clica duas vezes nele no Project Manager.
 **Run Selected File**
O Visual FoxPro executa o arquivo selecionado quando você clica duas vezes nele.
**Modify Selected File**
O Visual FoxPro abre o designer ou editor apropriado quando você clica duas vezes em um arquivo.
**Prompt for Wizards**
Especifica que o Visual FoxPro solicita que você use um assistente, se aplicável, quando você escolhe New File no menu Project ou escolhe New no Project Manager.
**Display user-defined container icons**
Especifica que o Visual FoxPro exibe ícones de contêiner definidos pelo usuário no Project Manager .

# Opções de controle de origem

As opções nesta caixa tornam possível especificar qual aplicativo de controle de origem usar e como o aplicativo de controle de origem funciona quando você adiciona, modifica ou remove componentes do seu projeto.
 **Active source control provider**
Especifica o nome do aplicativo de controle de origem a usar. O nome que você especificar aqui se aplicará a novos projetos. Quando você cria um projeto, o nome do aplicativo de controle de origem em vigor no momento é armazenado com o projeto para que o Visual FoxPro saiba qual aplicativo de controle de origem usar cada vez que o projeto é aberto. Para desabilitar o controle de origem, escolha None .
**Automatically add new projects to source control**
Especifica que você é solicitado a colocar um projeto sob controle de origem quando você o cria. Se você desmarcar esta opção, novos projetos não são colocados automaticamente sob controle de origem e você deve adicioná-los manualmente.
**Check out files upon modify**
Especifica que os arquivos são automaticamente retirados (check out) para um usuário que os modifica no Project Manager . Se um arquivo já estiver retirado, o Visual FoxPro exibe um erro. Se você desmarcar esta opção, usuários que tentarem modificar arquivos que não estão retirados no Project Manager podem visualizar os arquivos, mas não podem alterá-los. Observação Se os usuários modificarem arquivos de projeto usando comandos na janela Command (como MODIFY), devem retirar os arquivos primeiro.
**Add files to source control upon add**
Especifica que os arquivos adicionados ao projeto são automaticamente colocados sob controle de origem para esse projeto. Se você desmarcar esta opção, os arquivos que você adiciona tornam-se parte do projeto (o arquivo .pjx), mas não são colocados sob controle de origem. No entanto, você pode colocar manualmente arquivos de projeto sob controle de origem a qualquer momento. Observação Arquivos de banco de dados (.dbc), tabela (.dbf), biblioteca de API e aplicativo (.app) não são colocados sob controle de origem automaticamente quando adicionados a um projeto. No entanto, você pode colocar esses arquivos sob controle de origem manualmente.
**Remove files from source control upon removal from project**
Especifica que quando você remove um arquivo de um projeto, ele também é removido do controle de origem. Se você desmarcar esta opção, quando você remove um arquivo do projeto, as informações de controle de origem do arquivo permanecem no banco de dados de controle de origem. Isso mantém informações de arquivo sobre esse arquivo e, se o arquivo não for excluído do disco, torna possível acessá-lo usando o sistema de controle de origem fora do Visual FoxPro.
**Display dialog box for shortcut menu commands**
Especifica que quando você escolhe um comando de controle de origem no menu de atalho do projeto, o Visual FoxPro permite selecionar mais de um arquivo sobre o qual executar o comando selecionado. Se você desmarcar esta opção, o comando se aplica somente ao arquivo selecionado no projeto, mas isso pode ser substituído pressionando SHIFT+Botão direito do mouse e escolhendo o comando.
**Text generation**
Especifica o nome do aplicativo usado para criar uma representação de texto de arquivos binários (formulário, etiqueta, menu, relatório ou biblioteca de classes) cada vez que o arquivo é submetido (check in). O arquivo de texto resultante é submetido junto com o arquivo de origem da tabela e pode ser usado para criar um relatório das diferenças entre várias versões de um arquivo.
**Project class**
Exibe a caixa de diálogo Project Reference, tornando possível especificar uma classe ProjectHook padrão como modelo para novos projetos.

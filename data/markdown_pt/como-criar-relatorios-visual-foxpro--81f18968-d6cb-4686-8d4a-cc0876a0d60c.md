# Como: criar relatórios (Visual FoxPro)

Dependendo da complexidade do relatório ou do nível de personalização desejado, você pode criar relatórios de várias maneiras:
 - Crie um relatório simples de uma ou várias tabelas usando um assistente de relatório. Um assistente é a maneira mais fácil de começar a criar um relatório. Para mais informações, consulte Creating Reports Using Wizards.
- Crie um relatório simples de uma única tabela usando Quick Report no Report Designer. Quick Report é a maneira mais rápida de criar um relatório simples e oferece recursos de personalização do Report Designer. Para mais informações, consulte Creating Reports Using Quick Report.
- Crie um relatório personalizado ou modifique um relatório existente usando o Report Designer. O Report Designer inicia o processo de design de relatório com um layout de relatório em branco. O Report Designer e o Label Designer são semelhantes em funcionalidade, mas diferem na página e no papel padrão que usam. Para mais informações, consulte Creating Reports Using the Report Designer.

Você pode modificar qualquer arquivo de layout de relatório criado com o Report Designer.

# Criando relatórios usando assistentes

Você pode criar relatórios facilmente usando um assistente de relatório. Os assistentes de relatório ajudam a configurar e criar um layout de relatório usando suas respostas a uma série de perguntas. Você pode usar o Report Wizard para criar relatórios com tabelas únicas, por exemplo, para criar uma lista de nomes e endereços de uma tabela de clientes. Você pode usar o One-To-Many Report Wizard para criar relatórios com tabelas que têm uma relação pai-filho, por exemplo, para criar uma lista de pedidos de um cliente a partir de uma tabela de clientes e uma tabela de pedidos.

### Para iniciar um assistente de relatório
- Abra o projeto da sua aplicação.
- Na Project Manager, expanda o nó Documents.
- No nó Documents, clique em Reports e depois em New.
- Na caixa de diálogo New Report, clique em Report Wizard.
- Selecione o tipo de relatório que deseja criar.
- Siga as instruções nas telas do assistente.

Para mais informações, consulte Report Wizard e One-To-Many Report Wizard.

Você também pode iniciar assistentes no menu Tools clicando em Wizards e selecionando um assistente. Depois de criar um layout usando um assistente, personalize o layout usando o Report Designer.

# Criando relatórios usando Quick Report

Você pode criar relatórios rapidamente usando Quick Report, que cria um relatório simples de uma única tabela.

> **Dica:** Você pode usar Quick Report em arquivos de relatório existentes se a banda Detail estiver vazia. Se a banda Page Header contiver controles, Quick Report os preserva.

> **Observação:** Quick Report não adiciona campos General ao layout do relatório.

### Para criar um quick report
- Abra o projeto da sua aplicação.
- Na Project Manager, expanda o nó Documents.
- No nó Documents, clique em Reports e depois em New.
- Na caixa de diálogo New Report, clique em New Report. O Report Designer é aberto.
- No menu Report, clique em Quick Report.
- Na caixa de diálogo Open, navegue até o diretório que contém a tabela desejada e selecione a tabela.
- Na caixa de diálogo Quick Report, clique no layout de campos desejado.
- Para selecionar campos específicos a incluir, clique em Fields. Quando terminar de selecionar campos, clique em OK. Observação Por padrão, todos os campos, exceto campos General na tabela, são incluídos.
- Selecione ou limpe as configurações Title, Add alias ou Add table to data environment.
- Quando terminar na caixa de diálogo Quick Report, clique em OK.

Para mais informações, consulte Quick Report Dialog Box.

Você também pode iniciar um quick report no menu File clicando em New e, na caixa de diálogo New, clicando em Report e depois em New File. O Report Designer aparece. Para continuar, siga as etapas restantes descritas para criar um quick report.

Você pode criar um quick report programaticamente sem abrir o Report Designer usando a versão Quick Report do comando CREATE REPORT. Para mais informações, consulte CREATE REPORT - Quick Report Command.

# Criando relatórios usando o Report Designer

Você pode criar relatórios personalizados começando com um layout de relatório em branco no Report Designer.

> **Observação:** O Report Designer e o Label Designer são semelhantes em funcionalidade, mas diferem na página e no papel padrão que usam.

### Para iniciar o Report Designer
- Abra o projeto da sua aplicação.
- Na Project Manager, expanda o nó Documents.
- No nó Documents, clique em Reports e depois em New.
- Na caixa de diálogo New Report, clique em New Report. O Report Designer é aberto.

Para mais informações, consulte Report Designer.

Você também pode iniciar um novo relatório em branco no menu File clicando em New e, na caixa de diálogo New, clicando em Report e depois em New File.

Você pode abrir o Report Designer programaticamente usando os comandos CREATE REPORT e MODIFY REPORT. Para mais informações, consulte CREATE REPORT Command e MODIFY REPORT Command.

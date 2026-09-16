# Como: criar um novo formulário

Formulários exibem os campos e registros em suas tabelas e views e geralmente incluem controles de navegação para ajudá-lo a mover de registro em registro.

Você pode criar formulários no Visual FoxPro de qualquer uma das seguintes maneiras:
 - Use assistentes de formulário para criar formulários prontos para uso.
- Escolha Quick Form no menu Form para criar um formulário simples que você pode personalizar adicionando seus próprios controles.
- Use o Form Designer para modificar formulários existentes ou criar seus próprios formulários.

# Usando um assistente de formulário

Sempre que quiser criar um novo formulário, você pode usar um assistente de formulário para ajudá-lo a configurá-lo. O assistente fará uma série de perguntas e construirá um formulário para você com base em suas respostas. Você pode escolher entre várias opções de estilo diferentes e visualizar seu formulário antes de criá-lo.

### Para criar um novo formulário com um assistente
- Na janela Project Manager Window , selecione a guia Documents e selecione Forms .
- Escolha New .
- Escolha Form Wizard .
- Selecione o tipo de formulário que deseja criar.
- Siga as instruções nas telas do assistente.

Você também pode acessar os assistentes de formulário no menu escolhendo o comando Wizards no menu Tools e selecionando Form.

O Visual FoxPro fornece dois assistentes de formulário diferentes para ajudá-lo a criar formulários:
 - Para criar um formulário básico baseado em uma tabela, escolha o Form Wizard .
- Para criar um formulário que incorpora dados de duas tabelas vinculadas em um relacionamento um-para-muitos, escolha o One-To-Many Form Wizard .

Formulários que você cria com os assistentes de formulário têm um conjunto padrão de botões de navegação para que você possa exibir registros diferentes no formulário, editar registros, pesquisar registros e assim por diante. Se você criar um formulário dentro de um banco de dados, o assistente de formulário pode usar configurações de máscara de entrada e formato armazenadas no banco de dados.

# Iniciando o Form Designer

Se quiser criar seu próprio formulário sem usar um assistente, use o Form Designer. Com o Form Designer, você pode adicionar campos e controles ao seu formulário e personalizá-lo ajustando e alinhando os controles.

O comando Quick Form facilita o início da criação de um formulário. O comando Quick Form exibe o Form Builder, que adiciona campos selecionados de tabelas ou views ao seu formulário.

### Para criar um novo formulário
- Na janela Project Manager Window , escolha a guia Documents.
- Selecione o ícone Forms.
- Escolha New .
- Selecione New Form . A janela Form Designer aparece para que você possa começar a criar seu formulário. - OR - From the File menu, choose New , select Form , and choose New File . - OR - Use the CREATE FORM Command .

# Modificando um formulário

Se os formulários gerados por assistente ou builder não atenderem completamente às suas necessidades, você pode modificá-los com o Form Designer. Usando o Form Designer, é fácil mover e redimensionar controles, copiar ou excluir controles, alinhar controles e modificar a ordem de tabulação.

### Para modificar um formulário gerado
- No Project Manager, selecione a guia Documents.
- Escolha o ícone Forms e selecione o nome do formulário.
- Escolha Modify .

# Adicionando campos rapidamente

Quando quiser colocar rapidamente os campos de uma tabela ou view em um formulário, escolha Quick Form no menu Form. Quick Form inicia o Form Builder, que adiciona campos selecionados de uma tabela ou view ao seu formulário, usando o estilo de campo que você escolher. O Form Builder cria um formulário sem controles de navegação, para que você possa adicionar os seus. Você pode usar um control builder para adicionar controles de navegação ao seu formulário ou escolher da biblioteca predefinida de controles de navegação fornecida com o Visual FoxPro.

### Para adicionar campos a um formulário
- No Project Manager, abra o formulário.
- No Form Designer, vá ao menu Form e escolha Quick Form . O Form Builder aparece.
- Na guia Style, selecione o estilo desejado para o novo controle.
- Na guia Field Selection, selecione a origem dos campos e os campos que deseja adicionar.
- Escolha OK para gerar o formulário. - OR -
- Na barra de ferramentas Form Controls, escolha um controle de dados e arraste na janela Form Designer para criar o controle.
- Na janela Properties, escolha a guia Data e selecione a propriedade ControlSource.
- Digite um nome de campo. - OR - Selecione um campo da lista de campos disponíveis.

# Criação de interface do usuário sem programação

O Visual FoxPro fornece controles poderosos de dados e de interface do usuário que você pode adicionar a formulários usando o Form Designer, o que permite criar uma interface do usuário com pouco ou nenhum código. Por exemplo, você pode desenvolver formulários um-para-muitos facilmente vinculando um controle Grid a uma tabela, o que pode ser feito arrastando uma tabela para um formulário para criar o controle Grid. Para manter consistência com outros aplicativos, você também pode criar caixas de diálogo com guias ou suas próprias interfaces de builder com o controle page frame.

# Criando um formulário um-para-muitos

O Visual FoxPro facilita a configuração de formulários para exibir registros de tabelas relacionadas. Usando a janela Project Manager Window e o Form Designer, você pode simplesmente "arrastar e soltar" os campos necessários para configurar um formulário.
 Formulários um-para-muitos exibem dados de tabelas relacionadas.

Experimente configurar um formulário um-para-muitos usando duas tabelas relacionadas, como as tabelas Customers e Orders de Testdata.dbc.
 Após quatro etapas, formulários um-para-muitos estão...
 ...prontos para execução.

Especifique tabelas e views para seu formulário no ambiente de dados Você pode usar o ambiente de dados do seu formulário ou relatório para especificar as tabelas ou views usadas pelo seu formulário. Depois de adicionar as tabelas e views que contêm os registros que você deseja exibir no formulário, você pode arrastar os campos para o Form Designer.

Crie grades selecionando vários campos Você pode selecionar vários campos e arrastá-los para um formulário para criar um objeto Grid. Se você selecionar vários campos e arrastá-los com o botão direito do mouse, poderá escolher entre uma grade e vários controles. Você também pode clicar no item Fields em uma tabela e arrastá-lo para um formulário para criar uma grade incorporando todos os campos da tabela. Se você clicar com o botão direito em um único campo e arrastá-lo para um formulário, poderá criar uma classe de objeto diferente da que está atribuída como classe de objeto padrão.

# Dando aos formulários uma aparência profissional

Você pode ser criativo e personalizar o layout dos formulários e adicionar cores, formas e gráficos.

Alinhe controles com precisão Use a barra de ferramentas Layout para alinhar rapidamente controles e espaçá-los uniformemente no formulário.

Altere a cor de fundo Use a barra de ferramentas Color Palette.

Adicione gráficos e imagens Use os botões Line, Shape e Image na barra de ferramentas Form Controls.

Controle a exibição e a entrada de dados em uma caixa de combinação Você pode definir a propriedade Format Property e a propriedade InputMask Property para um controle Combo Box.

Remova uma borda em uma caixa de combinação ou Spinner Você pode usar a propriedade BorderStyle Property para remover uma borda do controle. Por exemplo, se você estiver usando controles de caixa de combinação ou spinner em uma grade, pode limpar a exibição removendo as linhas extras que a borda adiciona à grade.

Use as cores atuais do Windows para cores de formulário Você pode definir uma opção adicional na propriedade ColorSource Property que permite definir as cores do formulário com base no esquema de cores atual do Windows.

# Definindo as propriedades dos controles

Você pode aprimorar sua interface do usuário com as propriedades de controle no Visual FoxPro. Usando a janela Properties Window (Visual FoxPro), você pode ver e definir as propriedades associadas a cada objeto no seu formulário para determinar como um controle de formulário aparece e se comporta.

Use vinculação de dados com controles ActiveX Para vincular dados a controles ActiveX, você pode usar a propriedade ControlSource Property (se o controle suportá-la) na janela Properties para especificar um campo ou variável ao qual o controle está vinculado.

Controle a navegação em page frames Ao definir a ordem de tabulação no seu page frame, você pode controlar a ordem em que as páginas são exibidas. Isso também adiciona a capacidade de navegar para as diferentes páginas em um page frame com as teclas de seta direita e esquerda.

Controle a seleção de itens em controles List Box e Combo Box Quando uma caixa de listagem ou caixa de combinação está vinculada a um ControlSource numérico, o número de índice da lista do item é coletado, em vez do valor. Para coletar o valor real do item selecionado no controle, defina a propriedade BoundTo Property como True.

Selecione mais de 60 itens em uma caixa de listagem Você pode selecionar um número ilimitado de itens múltiplos em um ListBox Control.

Crie propriedades e métodos ocultos Você pode definir propriedades de acessibilidade nas propriedades e métodos que você cria como Public, Protected ou Hidden. Para alterar a acessibilidade de propriedades e métodos, use a guia Members Tab, Class Info Dialog Box.

| Para obter mais informações sobre | Consulte |
| --- | --- |
| Criação de formulários | Creating Forms |
| Uso de assistentes de formulário | Ajuda pressionando F1 no assistente. |
| Uso de builders | Ajuda pressionando F1 no builder. |
| Uso de controles | Ajuda pesquisando pelo nome do controle ou Using Controls |
| Uso de formulários em aplicativos | Creating Forms |

# Personalizando seu Form Designer

Para facilitar seu trabalho, você pode personalizar o Form Designer para corresponder ao seu estilo e necessidades de trabalho.

Salve alterações automaticamente Você pode definir opções para que o Visual FoxPro salve seus formulários automaticamente quando você sair do Form Designer. Na guia Forms Tab, Options Dialog Box, você pode escolher a opção Save Changes Before Running Form. Se você selecionar esta opção, pula a caixa de diálogo de confirmação e as alterações feitas no formulário atual são salvas automaticamente.

Altere a fonte na janela Properties Você pode escolher uma de três configurações de fonte no menu de atalho da janela Properties.

Use o teclado na janela Properties A janela Properties suporta navegação por teclado para percorrer a hierarquia de objetos, controles e ordens de tabulação. Use CTRL+PGUP e CTRL+PGDN para mover para cima e para baixo na lista.

| Para obter mais informações sobre | Consulte |
| --- | --- |
| O Form Designer e controles de formulário | Form Designer |
| Criação de formulários | Creating Forms |

# Adicionar controles de uma biblioteca de classes

Quando você precisa adicionar controles a um formulário para navegar pelos registros nele, pode escolher de uma biblioteca de controles, arrastar os controles necessários e executar o formulário. É simples assim.

### Adicionando controles VCR a um formulário um-para-muitos

Você pode usar o exemplo a seguir para ver como é fácil agilizar seu trabalho usando controles de bibliotecas de classes.
 Armazene conjuntos de controles complicados em uma biblioteca de classes para reutilização.

Adicione controles VCR a um formulário Ao abrir a biblioteca de classes de botões de exemplo (Buttons.vcx) fornecida com o Visual FoxPro, você pode adicionar facilmente um conjunto de botões de controle de navegação estilo VCR ao seu formulário. As bibliotecas de exemplo estão no diretório Visual FoxPro ...\Samples\Classes.
 Uma classe para controles VCR pode ser adicionada à sua barra de ferramentas.
 Controles são fáceis de adicionar ao seu formulário.

Defina a propriedade SkipTable Como este é um formulário um-para-muitos, você precisa especificar que o próximo registro na tabela principal é selecionado quando você escolhe o botão Next. Para fazer isso, abra a janela Properties Window (Visual FoxPro) e defina a propriedade SkipTable para que se refira à tabela principal.
 A propriedade SkipTable adiciona a funcionalidade final ao seu controle.

### Expandindo suas bibliotecas de classes

Você não precisa esperar que alguém venda classes e bibliotecas de controle; você pode fazer as suas próprias.

Crie suas próprias classes Você pode criar seus próprios controles e salvá-los em bibliotecas de classes. Você pode começar com classes padrão do Visual FoxPro e personalizá-las para criar sua própria versão, ou pode criar suas próprias classes.

Aponte para classes em aplicativos compilados Você pode usar o comando SET CLASSLIB Command para apontar para uma classe incluída em um aplicativo compilado.

Adicione e mantenha classes na barra de ferramentas Forms Control Toolbar Quando você adiciona uma classe à barra de ferramentas Forms Control Toolbar, a classe permanece na barra de ferramentas até que você clique novamente no botão View Classes e selecione Standard.

Visualize informações detalhadas sobre suas classes Usando a janela Class Browser Window, você pode visualizar toda a hierarquia de classes e objetos em uma biblioteca de classes ou formulário.

Crie suas próprias subclasses de controles ActiveX Você pode criar subclasses de todos os controles ActiveX fornecidos com o Visual FoxPro.

| Para obter mais informações sobre | Consulte |
| --- | --- |
| Uso do Class Designer | Ajuda pressionando F1 no Class Designer. |
| Definição de propriedades | Creating Forms |
| Criação de classes e uso de bibliotecas de classes | Object-Oriented Programming |

# Criando uma barra de menu e menus de atalho

Você pode usar os Menu and Shortcut Designers para adicionar uma barra de menu e menus a formulários em seu aplicativo. Com os Menu and Shortcut Designers, você pode criar menus de atalho e menus para formulários SDI.

Quando você cria um menu, tem a opção de adicionar um menu à barra de menu ou criar um menu de atalho. O Shortcut Designer apresenta a interface familiar do Menu Designer, mas permite projetar menus de atalho em vez de barras de menu e menus.

Depois de gerar seu menu de atalho, você pode anexá-lo a qualquer controle executando o menu no evento RightClick do controle.

# Criando relatórios

Quando chega a hora de imprimir dados importantes, você não quer gastar muito tempo formatando relatórios. É por isso que o Visual FoxPro fornece assistentes de relatório para agilizar o processo de relatório. Com assistentes de relatório, você pode selecionar os dados desejados de suas tabelas e views e apresentá-los no formato de aparência profissional de sua escolha.
 É fácil combinar informações de duas tabelas diferentes em um relatório um-para-muitos.

Usando os recursos de design de relatório do Visual FoxPro, você pode:

Use o botão Preview A última tela de um assistente de relatório tem um botão Preview para que você possa ver rapidamente se seu relatório está do jeito que deseja. Se não estiver, use o botão Back no assistente e faça os ajustes necessários.

Use Quick Report para resultados rápidos Se você estiver configurando seu próprio relatório no Report Designer, escolha Quick Report no menu Report para adicionar campos selecionados de uma tabela a um relatório.

Use resultados de consulta ou view em um relatório Quer imprimir os resultados de uma consulta? Escolha a opção Report na caixa de diálogo Query Destination Dialog Box. Você pode enviar os resultados da consulta para um relatório pré-formatado ou enviar a consulta para um assistente de relatório.

Crie um relatório um-para-muitos O One-To-Many Report Wizard facilita a configuração de um relatório que mostra campos de duas tabelas unidas em um relacionamento um-para-muitos. Por exemplo, experimente usar o assistente para criar um relatório a partir de duas tabelas relacionadas em Testdata.dbc.
 Assistentes de relatório recuperam registros e formatam o layout do relatório.

Use outros assistentes de relatório Experimente usar os outros assistentes de relatório. Para relatórios simples de uma tabela ou relatórios de resumo com totais, escolha Report Wizard.

Use o Report Designer Se você desejar personalizar ainda mais seu relatório gerado pelo assistente, basta abri-lo no Report Designer e adicionar os aprimoramentos necessários.

| Para obter mais informações sobre | Consulte |
| --- | --- |
| Report Wizard | Ajuda pressionando F1 no assistente. |
| Report Designer | How to: Create Reports (Visual FoxPro) |

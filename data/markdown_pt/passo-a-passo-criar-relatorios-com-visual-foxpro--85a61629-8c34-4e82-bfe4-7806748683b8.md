# Passo a passo: criar relatórios com Visual FoxPro

Você pode projetar e criar relatórios para fornecer clareza e legibilidade aos dados, transformando dados de desenvolvedor em informações para o usuário. Relatórios são ideais para exibir e distribuir dados porque você pode facilmente repetir, duplicar e compartilhá-los.

Este passo a passo mostra como criar relatórios do Visual FoxPro usando o Report wizard para obter rapidamente um relatório de qualquer tabela única ou relacionada. Se você deseja personalizar seu relatório ou adicionar elementos não relacionados a dados, use o Report designer.
 - Criando um Relatório de Tabela Única
- Criando um Relatório de Várias Tabelas

Para obter mais informações, consulte Trabalhando com Relatórios.

# Criando um Relatório de Tabela Única

Se você só deseja ver o que tem, use a janela Browse em qualquer tabela.

### Para acessar a janela Browse
- No menu File, abra a tabela.
- No menu View, selecione Browse .

Se você deseja imprimir ou enviar um relatório rapidamente, pode exportar o arquivo como texto e depois imprimir ou enviar o novo arquivo de texto. As opções da caixa de diálogo Export permitem selecionar partes da tabela para converter em texto. (Lembre-se de verificar a orientação do papel para tabelas largas.)

### Para relatar dados brutos de uma tabela como texto rapidamente
- No menu File, clique em Open .
- Na caixa de diálogo Open, selecione Table na lista suspensa Files of type, localize a tabela desejada e clique em OK .
- No menu View, clique em Browse . Isso exibe a tabela selecionada. Neste momento, na IDE, você pode alterar as larguras ou posições das colunas, ou fazer alterações permanentes no menu Table.
- No menu File, clique em Export .
- Na caixa de diálogo Export, selecione Delimited Text na lista suspensa Type. Se você fosse usar a tabela em outro aplicativo, como o Microsoft Excel, poderia selecionar o aplicativo na lista, e a tabela seria convertida para o formato adequado e salva com a extensão correta.
- Clique em To e insira o nome do arquivo do seu novo arquivo, incluindo a extensão.
- Na lista suspensa Field separator, selecione o delimitador desejado no novo arquivo e clique em OK .

### Visual FoxPro Report Wizard

Se você descobrir que precisa de apresentações formais, resumos ou cálculos, ou precisa usar as mesmas informações repetidamente, use o Report wizard ou o Report designer para gerar relatórios reutilizáveis, atualizáveis e modificáveis.

O Report wizard solicita escolhas que permitem criar rapidamente um relatório bem formatado de uma ou mais tabelas. Em muitas circunstâncias, esses relatórios rápidos funcionam muito bem.

### Para usar o Report wizard
- No menu File, clique em New .
- Na caixa de diálogo New, selecione Report .
- Clique no botão Wizard e selecione o tipo de relatório que deseja criar.

No wizard, você pode visualizar um relatório antes de salvá-lo. Além disso, pode salvá-lo e depois abri-lo no Report designer para usar a IDE do Visual FoxPro para adicionar ao seu design de relatório.

Para experimentar o Report wizard, use a tabela Labels.dbf, que acompanha o Visual FoxPro. Use os procedimentos a seguir para trabalhar com relatórios simples de uma tabela

### Para criar um Relatório simples usando a tabela Labels.dbf
- No menu File, clique em New .
- Na caixa de diálogo New, selecione Report e clique no botão Wizard.
- Na caixa de diálogo de seleção do Wizard, clique duas vezes em Report Wizard .
- No Report wizard, selecione Free Tables na caixa de listagem suspensa Databases and tables e selecione ou localize a tabela Labels.
- Selecione qualquer um ou todos os campos disponíveis e continue o wizard, fazendo as seleções apropriadas até a Etapa 5 .
- Na Etapa 5 , escolha um estilo e orientação de relatório. Além disso, você pode clicar em Summary options para acessar cinco funções — Sum , Avg , Count , Min e Max — para campos exibidos no seu relatório. As funções selecionadas são adicionadas automaticamente com legendas e posicionamento apropriados.
- Na Etapa 6 , clique no botão Preview para ver o relatório que suas seleções criariam se você clicasse em Finish . Você pode imprimir a visualização sem criar um arquivo de relatório. O Report wizard cria etiquetas e seleciona fontes, tamanhos de fonte, indentação e outras características de estilo e formatação para ajudar a transformar os dados da tabela em informações de relatório. Frequentemente, criar relatórios com o wizard é tão rápido quanto criar a cópia ad hoc da janela Browse, e os resultados geralmente ficam muito mais bonitos.
- Clique em Finish .

Para obter mais informações, consulte Report Wizard e One-To-Many Report Wizard.

### Visual FoxPro Report Designer

Você pode usar o Report designer para criar relatórios simples, chamados Quick Reports. Além disso, o Report designer é uma ferramenta poderosa para criar relatórios formatados. A principal diferença entre usar o Report wizard e usar o Report designer é que o designer oferece maior controle do posicionamento de dados e outros conteúdos.

### Para criar Quick Reports com o Report designer
- No menu File, clique em New .
- Na caixa de diálogo New, selecione Report e clique no botão New File.
- No menu Report, clique em Quick Report . Se você tem uma tabela aberta, o Visual FoxPro a usará como fonte do seu relatório. Se nenhuma tabela estiver aberta, o Visual FoxPro exibe a caixa de diálogo Open para que você possa escolher uma tabela.

O Report designer preenche as bandas Detail e Page Footer. Depois, os detalhes dependem de você. Você tem mais controle do que com o Report wizard; também tem mais responsabilidade. Se você deseja gerar informações, como somas, médias ou contagens, use Data Grouping no menu Report. Sua especificação para um grupo de dados pode ser tão simples quanto o nome do campo de índice selecionado no Expression builder.

Para incluir um cálculo no seu relatório, abra uma tabela ordenada (indexada em cust_id), crie um Quick Report como base, especifique agrupamento de dados e depois especifique como e onde no relatório o cálculo é exibido. Por fim, visualize, imprima e salve o relatório.

### Para criar um relatório contendo um cálculo
- No menu File, abra a tabela ..\samples\Data\orders.dbf.
- No menu Window, clique em Data Session e clique em Properties para a tabela orders. Na caixa de diálogo Work Area Properties, escolha Orders.cust_id como Index order, clique em OK e depois feche a caixa de diálogo Data Session.
- No menu File, clique em New . Na caixa de diálogo New, selecione Report e clique em New File .
- No menu Report, clique em Quick Report e selecione layout vertical. Clique no botão Fields, selecione os campos que deseja no relatório e clique em OK . Clique em OK na caixa de diálogo Quick Report. Observação Para este exemplo, você precisa dos campos Order_ID, Cust_ID e Order_amt.
- No menu Report, clique em Data Grouping . Na caixa de diálogo Data Grouping, clique no botão Add e na lista Fields no Expression Builder , clique duas vezes em Orders.cust_id . Clique em OK .
- Na banda Detail, faça uma cópia do campo order_amt, arraste a cópia para a banda Group Footer para totais de grupo e abra o Field Properties . Na guia Calculate, selecione a função Sum na caixa de listagem suspensa Calculate Type. Observação A caixa de listagem suspensa Reset based on exibe a seleção padrão, campo Order.cust_id. Esta configuração significa que a função Sum é reiniciada para zero cada vez que o valor do campo cust_id muda na passagem pela tabela.
- Na banda Detail, faça uma cópia do campo order_amt, arraste a cópia para a banda Page Footer para toda a tabela e abra o Field Properties . Na guia Calculate, selecione a função Sum na caixa de listagem suspensa Calculate Type e altere o valor Reset based on para Report .
- No menu Report, clique em Print Preview para ver o que você criou. Salve o relatório se estiver satisfeito com ele. A última página exibe o total de todos os pedidos — informação não incluída especificamente na tabela.

Enquanto o Report designer está aberto, você tem acesso a ferramentas e outros designers, para que possa revisar a tabela atual ou modificar o ambiente de dados selecionando outras tabelas ou índices. Além disso, você pode adicionar funcionalidade ao relatório através da barra de ferramentas Report Controls e do menu Report.

Para obter mais informações sobre o Report designer, consulte Report Designer e Report Band Properties Dialog Box.

# Criando um Relatório de Várias Tabelas

Além de dados de tabela única, relatórios do Visual FoxPro podem exibir dados de várias tabelas relacionadas e podem executar cálculos e produzir resumos.

Este procedimento usa duas tabelas, customer e orders, do banco de dados testdata.dbc na pasta Samples.

### Para criar um relatório usando o banco de dados Testdata que acompanha o Visual FoxPro
- No menu File, clique em New .
- Na caixa de diálogo New, selecione Report e clique no botão Wizard.
- Na caixa de diálogo de seleção do Wizard, clique duas vezes em One-To-Many Report Wizard .
- No One-To-Many Report wizard, selecione o banco de dados TESTDATA na lista suspensa Databases and Tables e selecione a tabela Customer.
- Na Etapa 1 do wizard, destaque a tabela Customer e selecione os campos cust_id e Customer na lista suspensa Available Fields.
- Na Etapa 2 , destaque a tabela Orders e selecione os campos cust_id , to_city e order_amt na lista suspensa Available Fields. Na Etapa 3 , você vê como as duas tabelas estão relacionadas — customer.cust_id a orders.cust_id ; em outras palavras, as tabelas estão indexadas em campos correspondentes. Se você deseja um relacionamento diferente, pode escolher nas listas suspensas das tabelas pai e filha. Se você alterar o relacionamento especificado, também precisará garantir que escolheu os campos corretos nas etapas 1 e 2.
- Na Etapa 5 , escolha um estilo e orientação de relatório. Além disso, você pode clicar em Summary options para acessar cinco funções — SUM , AVG , COUNT , MIN e MAX — para campos exibidos no seu relatório. As funções selecionadas são adicionadas automaticamente com legendas e posicionamento apropriados.
- Na Etapa 6 , clique em Preview para ver o relatório que suas seleções criariam se você clicasse em Finish . Você pode imprimir a visualização sem criar um arquivo de relatório.
- Clique em Finish .

Você pode criar o mesmo relatório no Report designer, mas para especificar o banco de dados e as tabelas, deve estabelecer o ambiente de dados do relatório. Você então usa esse ambiente de dados em um Quick Report ou através de arrastar e soltar na IDE para criar seu relatório.

Para amostras de vários tipos de relatório que você pode criar, consulte Solution Samples.

Para obter mais informações sobre o uso de relatórios, consulte Como: especificar expressões em controles de campo.

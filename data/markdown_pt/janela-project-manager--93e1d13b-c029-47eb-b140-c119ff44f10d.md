# Janela Project Manager

Use o Project Manager para organizar e gerenciar seus arquivos em projetos. Um projeto é uma coleção de arquivos, dados, documentos e objetos do Visual FoxPro que é salva como um arquivo com extensão .pjx. Quando a janela Project Manager está ativa, o Visual FoxPro exibe o menu Project na barra de menus.

Os itens no Project Manager são organizados em uma visualização semelhante a um esboço que você pode expandir ou recolher. Um sinal de mais aparece ao lado de um símbolo se houver um ou mais itens desse tipo no projeto. Clique no sinal de mais ao lado de um símbolo para ver os itens na lista. Clique no sinal de menos para recolher uma lista expandida.

Inicialmente, o Project Manager aparece como uma janela separada. Você pode mover o container, redimensioná-lo ou recolhê-lo para que apenas as guias sejam exibidas.

Como nas barras de ferramentas, você pode encaixar o Project Manager arrastando-o para o topo da tela ou clicando duas vezes na barra de título. Quando o Project Manager está encaixado, ele se torna parte da área de barra de ferramentas da janela. Você não pode expandir a janela Project Manager quando está encaixada; em vez disso, clique em guias individuais para usá-las. Você também pode destacar guias de um Project Manager encaixado.

Quando o Project Manager está encaixado, você pode clicar com o botão direito nele para exibir um menu de atalho. No Visual FoxPro 9.0, as seguintes opções estão disponíveis no menu de atalho:
 **Undock**
Restaura o Project Manager ao seu tamanho e localização anteriores.
**Close**
Fecha o Project Manager.
**Add Project to Source Control**
Se o software de controle de origem estiver instalado, adiciona o projeto ao controle de origem.
**Project Info**
Exibe a caixa de diálogo Project Information Dialog Box, permitindo visualizar e editar informações sobre o projeto e seus arquivos.
**Errors**
Abre uma janela Error que exibe erros encontrados quando um projeto ou aplicativo foi compilado.
**Build**
Exibe a caixa de diálogo Build Options Dialog Box. Esta caixa de diálogo permite compilar um projeto ou aplicativo, e você também pode compilar um executável ou servidor Automation.
**Refresh**
Atualiza a exibição visual do Project Manager.
**Clean Up Project**
Limpa um projeto removendo registros marcados para exclusão e compactando campos memo.
**Builder**
Exibe a caixa de diálogo Wizard Selection Dialog Box, contendo uma lista de assistentes dos quais você pode escolher
**Help**
Abre a janela Help.

Você pode personalizar sua área de trabalho visual alterando sua visualização do Project Manager ou definindo duplo clique para executar arquivos no Project Manager. Para mais informações, consulte Customizing the Visual FoxPro Environment.

# Guias

Exibe itens por categoria. Quando o Project Manager está recolhido, você pode destacar guias arrastando-as para fora do Project Manager. Para substituir uma guia, basta arrastá-la de volta à sua posição original ou clicar na caixa Close.

Para destacar uma guia, recolha o container, selecione uma guia e arraste-a para fora do Project Manager. Quando uma guia está flutuando, você pode acessar as opções no menu Project clicando com o botão direito do mouse na guia flutuante.

Se você deseja que a guia permaneça sempre no topo, clique no ícone de alfinete no topo da guia. A guia permanecerá no topo de outras janelas do Visual FoxPro. Você pode definir mais de uma guia como "always on top". Para remover a configuração "always on top" de uma guia, clique no ícone de alfinete novamente.

# Botão Expandir/Recolher

Expande e recolhe o Project Manager. Quando o Project Manager está recolhido, você pode "destacar" guias posicionando o ponteiro do mouse sobre uma guia e arrastando-a para fora do Project Manager.

# Lista de Itens

Lista os itens contidos no projeto em uma visualização semelhante a um esboço. Ícones aparecem à esquerda do item para identificar seu tipo.

O símbolo aparece ao lado de itens que estão excluídos do projeto.

Quando os arquivos são incluídos no projeto, eles são compilados em um único arquivo .app quando o projeto é compilado. Todos os arquivos incluídos são somente leitura em tempo de execução. No grupo Programs, Forms, Queries ou Menus, o nome do arquivo de programa principal aparece em negrito.

# Botões do Project Manager
 **New**
Cria um novo arquivo ou objeto. Este botão tem o mesmo efeito que o comando New File no menu Project. O tipo do novo arquivo ou objeto é o mesmo do item atualmente selecionado. Observação Arquivos criados no menu File não são automaticamente incluídos em um projeto. Arquivos criados do comando New File no menu Project (ou do botão New no Project Manager) são automaticamente incluídos em um projeto.
**Add**
Adiciona um arquivo existente ao projeto. Este botão tem o mesmo efeito que o comando Add File no menu Project. Depois de clicar em Add, você pode selecionar vários arquivos pressionando a tecla SHIFT ou CTRL na caixa de diálogo Open enquanto clica nos arquivos para adicioná-los.
**Modify**
Abre o item selecionado no designer apropriado. Este botão tem o mesmo efeito que o comando Modify File no menu Project.
**Browse**
Abre uma tabela em uma janela Browse. Este comando tem o mesmo efeito que o comando Browse File no menu Project, e é habilitado apenas quando uma tabela está selecionada.
**Close**
Fecha um banco de dados aberto. Este comando tem o mesmo efeito que o comando Close File no menu Project, e é habilitado apenas quando uma tabela está selecionada. Se o banco de dados selecionado já estiver fechado, este botão muda para Open.
**Open**
Abre um banco de dados. Este comando tem o mesmo efeito que o comando Open File no menu Project, e é habilitado apenas quando uma tabela está selecionada. Se o banco de dados selecionado já estiver aberto, este botão muda para Close.
**Remove**
Remove o arquivo ou objeto selecionado do projeto. O Visual FoxPro pergunta se você deseja apenas remover o arquivo do projeto ou se deseja remover do projeto e excluir do disco. Este comando tem o mesmo efeito que o comando Remove File no menu Project.
**Build**
Compila um projeto ou aplicativo e também pode compilar um executável ou servidor Automation. Este comando tem o mesmo efeito que o comando Build no menu Project.
**Preview**
Exibe o relatório ou etiqueta selecionado no modo Print Preview. Habilitado quando você seleciona um relatório ou etiqueta no Project Manager. Este comando tem o mesmo efeito que o comando Preview File no menu Project.
**Run**
Executa a consulta, formulário ou programa selecionado. Habilitado quando você seleciona uma consulta, formulário, menu ou programa no Project Manager. Este comando tem o mesmo efeito que o comando Run File no menu Project.

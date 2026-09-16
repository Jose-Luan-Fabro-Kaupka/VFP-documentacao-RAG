# Janela Class Browser

O Class Browser exibe classes em bibliotecas de classes ou formulários e informações de biblioteca de tipos em um arquivo de biblioteca de tipos (.tlb), biblioteca de objetos (.olb) ou executável (.exe). Você pode usar o Class Browser para visualizar, usar e gerenciar classes e seus membros definidos pelo usuário. Para obter mais informações, consulte Operating the Class Browser.

> **Observação:** Você pode abrir o menu de atalho do Class Browser clicando com o botão direito na janela Class Browser ou pressionando ALT+F10.

No Visual FoxPro 9.0, você também pode exibir definições de classes em arquivos de programa (.prg.). Muitos dos recursos do Class Browser disponíveis para bibliotecas de classes estão disponíveis para arquivos de programa. Você pode clicar duas vezes em um método ou evento para editar o código do método ou evento, e pode clicar duas vezes em uma propriedade para exibir seu valor. Você também pode clicar duas vezes em uma classe de programa para modificar sua estrutura. Classes em arquivos de programa podem ser visualizadas em exibições hierárquicas ou não hierárquicas, e você pode filtrar membros protected e hidden.
 **Class icon**
Exibe um ícone que representa uma classe ou biblioteca de classes selecionada. Este ícone aparece ao lado da caixa de tipo somente quando uma classe ou biblioteca de classes é selecionada na lista de classes do Class Browser. Você pode especificar um arquivo de ícone (.ico) ou bitmap (.bmp) diferente para uma classe. Para obter mais informações, consulte How to: Specify Design-Time Appearance for Classes .
**Type box**
Permite selecionar ou inserir um tipo de classe ou cadeia de caracteres para filtrar a movimentação. A lista suspensa mostra as classes base. A lista também mantém um histórico de tipos de classe e filtros que você selecionou ou inseriu para a instância atual do Class Browser.

Botões do Class Browser

Executa vários comandos do Class Browser. O menu de atalho do Class Browser fornece funcionalidade adicional. Para obter mais informações, consulte Class Browser Buttons.
 **Class List**
Exibe as classes e subclasses em um arquivo de biblioteca de classes (.vcx) aberto, um formulário (.scx) ou programa (.prg). Observação Um chevron (<<) ao lado de uma classe indica que a classe pai está localizada em um arquivo que não é exibido na lista de classes.
**Member list**
Exibe objetos membros e quaisquer propriedades e métodos definidos pelo usuário da classe ou formulário selecionado na lista de classes. Você pode filtrar esta lista selecionando uma das seguintes opções no menu de atalho da lista de membros: Protected filter Se um ícone protected (uma chave) é exibido ao lado do item de menu de atalho Protected filter, membros protected são exibidos na lista de membros. Membros protected também são indicados por um asterisco (*). Hidden filter Se um ícone hidden (um cadeado) é exibido ao lado do item de menu de atalho Hidden filter, membros hidden são exibidos na lista de membros. Membros hidden também são indicados por um acento circunflexo (^). Empty filter Se uma marca de seleção é exibida ao lado do item de menu de atalho Empty filter, métodos vazios são exibidos na lista de membros. Métodos vazios são indicados por um til (~).
**Class description box**
Exibe uma descrição para a classe selecionada. Esta caixa está localizada na parte inferior esquerda da janela Class Browser. Você pode editar a descrição nesta caixa.
**Member description box**
Exibe informações sobre o membro selecionado de uma classe. Esta caixa está localizada na parte inferior direita da janela Class Browser. Observação Para objetos membro, a caixa é somente leitura e exibe informações de classe e classe base. Para membros de propriedade ou método personalizados, a caixa exibe uma descrição que você pode editar. Para instâncias da classe, a caixa exibe uma descrição somente leitura que inclui o escopo da variável (public ou hidden), nomes de membros e valores de propriedade.

# Controles para ampliar formulários

Page frames tornam possível ampliar a área de superfície de seus formulários, e controles ActiveX tornam possível ampliar a funcionalidade de seus formulários.

# Usando page frames

Um page frame é um objeto contêiner que contém páginas. As páginas, por sua vez, contêm controles. As propriedades podem ser definidas no nível do page frame, da página ou do controle.

### Para ver exemplos de uso de page frames
- Execute Solution.app no diretório Visual FoxPro ...\Samples\Solution.
- Na visualização em árvore, clique em Controls e, em seguida, clique em Page frame.

Você pode pensar no page frame como um contêiner tridimensional que apresenta páginas em camadas. Apenas os controles na página superior (ou no topo do page frame) podem estar visíveis e ativos.

O page frame define a localização das páginas e a quantidade da página que está visível. O canto superior esquerdo de uma página é ancorado ao canto superior esquerdo do page frame. Os controles podem ser colocados em páginas que estão além das dimensões do page frame. Esses controles estão ativos, mas não estão visíveis, a menos que você altere programaticamente as propriedades Height e Width do page frame para tornar os controles visíveis.

# Usando páginas em uma aplicação

Com page frames e páginas, você pode criar formulários com guias ou caixas de diálogo com o mesmo tipo de capacidades de interface que você vê no Project Manager.

Além disso, page frames tornam possível definir uma região do formulário onde você pode facilmente trocar controles. Por exemplo, nos Wizards, a maior parte do formulário permanece constante, mas uma área do formulário muda com cada etapa. Em vez de criar cinco formulários para as etapas do assistente, você poderia criar um formulário com um page frame e cinco páginas.

Solution.app, no diretório Visual FoxPro ...\Samples\Solution, contém dois exemplos de page frame que demonstram o uso de frames com e sem guias.

# Adicionar page frames a um formulário

Você pode incluir um ou mais page frames em qualquer formulário.

### Para adicionar um page frame a um formulário
- Na barra de ferramentas Form Controls, escolha o botão Page Frame e arraste para dimensionar na janela Form.
- Defina a propriedade PageCount para indicar o número de páginas a incluir no frame.
- No menu de atalho do frame, escolha Edit para ativar o frame como um contêiner. A borda do page frame se alarga para indicar que está ativo.
- Adicione controles da mesma forma que você adicionaria a um formulário. Observação Como outros controles contêiner, você deve selecionar o page frame e escolher Edit no menu do botão direito do mouse, ou selecionar o contêiner na lista suspensa Object na janela Properties, para que o contêiner seja selecionado (tenha uma borda mais larga) antes de adicionar controles à página que você está projetando. Se você não ativar a página como um contêiner antes de adicionar controles, os controles serão adicionados ao formulário em vez da página, mesmo que possam parecer estar na página.

### Para selecionar uma página diferente no page frame
- Ative o page frame como um contêiner clicando com o botão direito do mouse e escolhendo Edit.
- Selecione a guia da página que deseja usar. -ou-
 - Selecione a página na caixa Object na janela Properties. -ou-
- Selecione a página na caixa Page na parte inferior do Form Designer.

# Adicionar controles a uma página

Quando você adiciona controles a uma página, eles estão visíveis e ativos apenas quando sua página está ativa.

### Para adicionar controles a uma página
- Na caixa Object da janela Properties, selecione a página. Uma borda aparece ao redor do page frame indicando que você pode manipular objetos contidos.
- Na barra de ferramentas Form Controls, escolha o botão do controle desejado e arraste para dimensionar na página.

# Gerenciar legendas longas em guias de página

Se as legendas em suas guias são mais longas do que podem ser exibidas na guia dada a largura do page frame e o número de páginas, você tem duas opções:
 - Defina a propriedade TabStretch como 1 - Single Row para mostrar apenas os caracteres das legendas que cabem nas guias. Single Row é o padrão.
- Defina a propriedade TabStretch como 0 - Multiple Rows para empilhar as guias de modo que toda a legenda em todas as guias esteja visível.

# Alterar páginas programaticamente

Se um page frame é exibido com guias ou não, você pode tornar uma página ativa programaticamente usando a propriedade ActivePage. Por exemplo, o código a seguir no procedimento de evento Click de um botão de comando em um formulário altera a página ativa de um page frame no formulário para a terceira página:

```foxpro
THISFORM.pgfOptions.ActivePage = 3
```

# Propriedades comuns de page frame

As seguintes propriedades de page frame são comumente definidas em tempo de design.

| Propriedade | Descrição |
| --- | --- |
| Tabs | Se as guias estão visíveis para as páginas. |
| TabStyle | Se as guias são todas do mesmo tamanho e juntas têm a mesma largura do page frame. |
| PageCount | O número de páginas no page frame. |

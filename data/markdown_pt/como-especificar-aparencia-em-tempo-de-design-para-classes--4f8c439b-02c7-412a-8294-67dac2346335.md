# Como: especificar aparência em tempo de design para classes

No Visual FoxPro, objetos e controles criados a partir de classes visuais exibem um elemento visual em tempo de design e em tempo de execução. No entanto, objetos e controles baseados em classes não visuais, como a classe Custom e o controle Timer, exibem um elemento visual em tempo de design, mas não em tempo de execução.

Em tempo de design, o Visual FoxPro exibe objetos criados a partir de classes não visuais com um gráfico padrão. No entanto, você pode alterar o gráfico padrão para que possa distinguir uma classe não visual de outra em tempo de design. No entanto, objetos criados a partir de classes não visuais não exibem esses gráficos em tempo de execução.

Você também pode especificar ícones de barra de ferramentas e de contêiner que aparecem para classes na IDE do Visual FoxPro. Você pode especificar ícones que aparecem na barra de ferramentas Forms Control e na Toolbox depois de adicionar classes a elas. Você também pode especificar ícones de contêiner que aparecem no Project Manager e no Class Browser.

### Para especificar um elemento visual para uma classe não visual
- Abra a classe no Class Designer . Para obter mais informações sobre como abrir classes, consulte How to: Modify Classes .
- Na barra de ferramentas do Visual FoxPro, clique em Properties Window .
- Na janela Properties, especifique um arquivo de imagem, como um arquivo bitmap (.bmp), para a propriedade Picture.
- Salve a classe.

Você pode especificar um ícone de barra de ferramentas para uma classe. Depois de adicionar a classe à barra de ferramentas Form Controls ou à Toolbox, o ícone da classe aparece na barra de ferramentas ou na Toolbox.

### Para especificar um ícone de barra de ferramentas para uma classe
- Abra a classe no Class Designer . Para obter mais informações sobre como abrir classes, consulte How to: Modify Classes . Quando a classe abre no Class Designer , o menu Class aparece.
- No menu Class, escolha Class Info .
- Na caixa Toolbar icon na caixa de diálogo Class Info, digite o nome e o caminho do arquivo de ícone (.ico) ou bitmap (.bmp). -OU- Clique no botão de reticências (...) para procurar um arquivo .ico ou .bmp.
- Clique em OK e salve a classe.

> **Observação:** O bitmap (.bmp file) para um ícone de barra de ferramentas tem 15 por 16 pixels. Se a imagem for maior ou menor, ela é dimensionada para 15 por 16 pixels e pode não ficar como você deseja.

Você pode especificar um ícone de contêiner para uma classe. O ícone da classe aparece em contêineres como o Project Manager e o Class Browser. No Class Browser, o ícone da classe aparece ao lado da classe na lista de classes e ao lado da caixa de tipo quando a classe é selecionada. Por padrão, o ícone de contêiner e o ícone de barra de ferramentas da classe são os mesmos da classe pai.

### Para especificar um ícone de contêiner para uma classe
- Abra a classe no Class Designer. Para obter mais informações sobre como abrir classes, consulte How to: Modify Classes . Quando a classe abre no Class Designer , o menu Class aparece.
- No menu Class, escolha Class Info .
- Na caixa Container icon da caixa de diálogo Class Info, digite o nome e o caminho do arquivo de ícone (.ico) ou bitmap (.bmp). -OU- Clique no botão de reticências (...) para procurar um arquivo .ico ou .bmp.
- Clique em OK e salve a classe.

Você também pode especificar o ícone de contêiner no Class Browser clicando com o botão direito na classe na lista de classes, escolhendo Container icon, selecionando um arquivo .ico ou .bmp e clicando em OK.

> **Dica:** Se você clicar em Cancel em vez de OK , o Visual FoxPro exibe uma mensagem perguntando se deseja redefinir o ícone para o padrão, que é o ícone que o Visual FoxPro usa para suas classes base. Se desejar que o ícone corresponda à sua classe base, escolha Yes .

O novo ícone substitui o ícone anterior na lista de classes. O ícone que aparece ao lado da lista de classes é atualizado quando você seleciona a classe na lista de classes.

> **Observação:** Se o ícone anterior do contêiner e da barra de ferramentas for o mesmo, então o novo ícone substitui tanto o ícone de contêiner quanto o de barra de ferramentas. Caso contrário, se o ícone anterior da barra de ferramentas era diferente do ícone de contêiner, somente o ícone de contêiner é alterado.

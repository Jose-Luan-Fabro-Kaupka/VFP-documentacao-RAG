# Como: adicionar objetos definidos pelo usuário a um formulário

Um dos recursos mais poderosos do Visual FoxPro é a capacidade de criar classes que podem ser facilmente usadas e reutilizadas em várias partes dos seus aplicativos. Depois de criar classes, você pode adicioná-las aos seus formulários.

### Para adicionar um objeto baseado em uma classe personalizada
- No Project Manager Window, arraste a classe para o contêiner.

Você também pode adicionar suas classes diretamente da barra de ferramentas Form Controls quando as adiciona à sua barra de ferramentas.

# Adicionando bibliotecas de classes à barra de ferramentas Controls

Você precisa registrar suas bibliotecas de classes antes que elas possam ser exibidas na barra de ferramentas Form Controls.

### Para registrar uma biblioteca de classes
- No menu Ferramentas, escolha Opções.
- Na caixa de diálogo Opções, escolha a guia Controls.
- Escolha Adicionar.
- Na caixa de diálogo Abrir, escolha uma biblioteca de classes para adicionar à lista Selecionados e escolha Abrir.
- Repita as etapas 3 e 4 até adicionar todas as bibliotecas que deseja registrar.

Classes nas bibliotecas de classes na lista Selecionados podem ser usadas no Form Designer tão facilmente quanto as classes base do Visual FoxPro.

> **Dica:** Se desejar que as bibliotecas de classes estejam disponíveis na barra de ferramentas Form Controls sempre que executar o Visual FoxPro, escolha Definir como padrão na caixa de diálogo Opções.

Você também pode registrar bibliotecas diretamente no Form Designer.

### Para registrar uma biblioteca de classes no Form Designer
- Na barra de ferramentas Form Controls, escolha o botão View Classes.
- No submenu, escolha Adicionar.
- Na caixa de diálogo Abrir, escolha uma biblioteca de classes para adicionar à barra de ferramentas Form Controls e escolha Abrir.

# Adicionando objetos a um formulário a partir de uma biblioteca de classes

Depois de adicionar bibliotecas de classes na guia Classes da caixa de diálogo Opções ou no submenu View Classes, você pode acessá-las no Form Designer.

### Para adicionar um objeto personalizado da barra de ferramentas Controls
- Na barra de ferramentas Form Controls, escolha o botão View Classes.
- Na lista de bibliotecas de classes registradas, selecione a biblioteca que contém o controle que deseja adicionar ao formulário. A barra de ferramentas é preenchida com os controles na biblioteca selecionada.
- Clique no controle desejado e arraste para dimensionar no formulário. Observação Você pode remover uma biblioteca de classes visuais do menu da barra de ferramentas View Classes selecionando a biblioteca na lista Selecionados na guia Controls da caixa de diálogo Opções e escolhendo Remover.

Quando você adiciona objetos a um formulário baseados em qualquer coisa diferente das classes base do Visual FoxPro, um caminho relativo para a biblioteca de classes (arquivo .vcx) é armazenado no arquivo .scx do formulário. Se você mover o formulário ou a biblioteca de classes para um local diferente, o Visual FoxPro exibe uma caixa de diálogo quando você tenta executar o formulário para que possa localizar manualmente a biblioteca de classes.

### Para determinar quantos controles há em um formulário
- Use a propriedade ControlCount.

A propriedade Controls (Visual FoxPro) do formulário permite referenciar cada controle no formulário. O programa a seguir imprime a propriedade Name (Visual FoxPro) de todos os controles no formulário atualmente ativo.

```foxpro
ACTIVATE SCREEN  && to print to the main Visual FoxPro window
FOR nCnt = 1 TO Application.ActiveForm.ControlCount
   ? Application.ActiveForm.Controls[nCnt].Name
ENDFOR
```
